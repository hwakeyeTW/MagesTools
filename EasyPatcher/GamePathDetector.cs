using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using Microsoft.Win32;

namespace EasyPatcher
{
    internal static class GamePathDetector
    {
        public static List<string> FindCandidates(string defaultPath, string steamAppId)
        {
            var candidates = new HashSet<string>(StringComparer.OrdinalIgnoreCase);

            AddCandidate(candidates, defaultPath);

            var libraries = GetSteamLibraries();
            if (!string.IsNullOrWhiteSpace(steamAppId))
            {
                foreach (var library in libraries)
                {
                    var installDir = ReadSteamInstallDir(library, steamAppId);
                    if (!string.IsNullOrWhiteSpace(installDir))
                    {
                        AddCandidate(candidates, Path.Combine(library, "steamapps", "common", installDir));
                    }
                }
            }

            var folderName = GetDirectoryName(defaultPath);
            if (!string.IsNullOrWhiteSpace(folderName))
            {
                foreach (var library in libraries)
                {
                    AddCandidate(candidates, Path.Combine(library, "steamapps", "common", folderName));
                }
            }

            return candidates
                .Where(IsValidGameDirectory)
                .Select(Path.GetFullPath)
                .OrderBy(p => p, StringComparer.OrdinalIgnoreCase)
                .ToList();
        }

        public static bool IsValidGameDirectory(string path)
        {
            if (string.IsNullOrWhiteSpace(path))
            {
                return false;
            }

            try
            {
                return Directory.Exists(path) && Directory.Exists(Path.Combine(path, "USRDIR"));
            }
            catch
            {
                return false;
            }
        }

        private static void AddCandidate(HashSet<string> candidates, string path)
        {
            if (string.IsNullOrWhiteSpace(path))
            {
                return;
            }

            try
            {
                candidates.Add(Path.GetFullPath(Environment.ExpandEnvironmentVariables(path)));
            }
            catch
            {
                // Ignore malformed paths from metadata or registry values.
            }
        }

        private static string GetDirectoryName(string path)
        {
            if (string.IsNullOrWhiteSpace(path))
            {
                return null;
            }

            try
            {
                return new DirectoryInfo(path.TrimEnd(Path.DirectorySeparatorChar, Path.AltDirectorySeparatorChar)).Name;
            }
            catch
            {
                return null;
            }
        }

        private static List<string> GetSteamLibraries()
        {
            var libraries = new HashSet<string>(StringComparer.OrdinalIgnoreCase);
            foreach (var steamRoot in GetSteamRoots())
            {
                if (!Directory.Exists(steamRoot))
                {
                    continue;
                }

                libraries.Add(steamRoot);
                var libraryFile = Path.Combine(steamRoot, "steamapps", "libraryfolders.vdf");
                if (!File.Exists(libraryFile))
                {
                    continue;
                }

                try
                {
                    var text = File.ReadAllText(libraryFile);
                    foreach (Match match in Regex.Matches(text, "\\\"(?<key>[^\\\"]+)\\\"\\s+\\\"(?<value>[^\\\"]+)\\\""))
                    {
                        var key = match.Groups["key"].Value;
                        if (!string.Equals(key, "path", StringComparison.OrdinalIgnoreCase) &&
                            !Regex.IsMatch(key, "^\\d+$"))
                        {
                            continue;
                        }

                        var value = match.Groups["value"].Value.Replace("\\\\", "\\");
                        if (Directory.Exists(Path.Combine(value, "steamapps")))
                        {
                            libraries.Add(value);
                        }
                    }
                }
                catch
                {
                    // Keep the Steam root even if libraryfolders.vdf cannot be read.
                }
            }

            return libraries.ToList();
        }

        private static IEnumerable<string> GetSteamRoots()
        {
            var roots = new HashSet<string>(StringComparer.OrdinalIgnoreCase);

            AddRegistryValue(roots, Registry.CurrentUser, @"Software\Valve\Steam", "SteamPath");
            AddRegistryValue(roots, Registry.CurrentUser, @"Software\Valve\Steam", "InstallPath");
            AddRegistryValue(roots, Registry.LocalMachine, @"SOFTWARE\Valve\Steam", "InstallPath");
            AddRegistryValue(roots, Registry.LocalMachine, @"SOFTWARE\WOW6432Node\Valve\Steam", "InstallPath");

            var programFilesX86 = Environment.GetFolderPath(Environment.SpecialFolder.ProgramFilesX86);
            if (!string.IsNullOrWhiteSpace(programFilesX86))
            {
                roots.Add(Path.Combine(programFilesX86, "Steam"));
            }

            return roots;
        }

        private static void AddRegistryValue(HashSet<string> roots, RegistryKey hive, string subKey, string valueName)
        {
            try
            {
                using (var key = hive.OpenSubKey(subKey))
                {
                    var value = key == null ? null : key.GetValue(valueName) as string;
                    if (!string.IsNullOrWhiteSpace(value))
                    {
                        roots.Add(value.Replace('/', Path.DirectorySeparatorChar));
                    }
                }
            }
            catch
            {
                // Registry lookup is best-effort only.
            }
        }

        private static string ReadSteamInstallDir(string library, string steamAppId)
        {
            var manifest = Path.Combine(library, "steamapps", "appmanifest_" + steamAppId + ".acf");
            if (!File.Exists(manifest))
            {
                return null;
            }

            try
            {
                var text = File.ReadAllText(manifest);
                var match = Regex.Match(text, "\\\"installdir\\\"\\s+\\\"(?<dir>[^\\\"]+)\\\"", RegexOptions.IgnoreCase);
                return match.Success ? match.Groups["dir"].Value : null;
            }
            catch
            {
                return null;
            }
        }
    }
}
