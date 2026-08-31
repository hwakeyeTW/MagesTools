using System;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Reflection;
using System.Windows.Forms;
using System.IO.Compression;
using System.Collections.Generic;

using fastJSON;

using Mages.Script;
using Mages.Package;

namespace EasyPatcher
{
    public partial class MainForm : Form
    {
        public const string PATCH_DIR = "berd/";

        public MainForm()
        {
            InitializeComponent();
            linkLabel_version.Text = "v" + Assembly.GetExecutingAssembly().GetName().Version.ToString();

            var meta = JSON.ToObject<Dictionary<string, dynamic>>(File.ReadAllText(PATCH_DIR + "meta.json"));
            Text += " - " + GetMetaString(meta, "name");
            pictureBox_main.ImageLocation = Path.GetFullPath(PATCH_DIR + GetMetaString(meta, "image"));
            textBox_log.Text = GetMetaString(meta, "notice").Replace("\n", Environment.NewLine);
            if (textBox_log.Text.Length > 0)
            {
                textBox_log.AppendText(Environment.NewLine);
            }

            var defaultPath = GetMetaString(meta, "default_path");
            var steamAppId = GetMetaString(meta, "steam_app_id");
            DetectAndFillGamePath(defaultPath, steamAppId);
        }

        private static string GetMetaString(Dictionary<string, dynamic> meta, string key)
        {
            if (!meta.ContainsKey(key) || meta[key] == null)
            {
                return string.Empty;
            }

            return Convert.ToString(meta[key]);
        }

        private void DetectAndFillGamePath(string defaultPath, string steamAppId)
        {
            var candidates = GamePathDetector.FindCandidates(defaultPath, steamAppId);
            if (candidates.Count == 1)
            {
                textBox_path.Text = candidates[0];
                Log("[路徑] 已自動偵測遊戲安裝位置：" + candidates[0]);
                return;
            }

            if (candidates.Count > 1)
            {
                string preferred = null;
                try
                {
                    if (GamePathDetector.IsValidGameDirectory(defaultPath))
                    {
                        var normalizedDefault = Path.GetFullPath(defaultPath);
                        preferred = candidates.FirstOrDefault(p =>
                            string.Equals(p, normalizedDefault, StringComparison.OrdinalIgnoreCase));
                    }
                }
                catch
                {
                    preferred = null;
                }

                if (!string.IsNullOrWhiteSpace(preferred))
                {
                    textBox_path.Text = preferred;
                    Log("[路徑] 偵測到多個遊戲位置，已採用修補檔預設位置：" + preferred);
                }
                else
                {
                    textBox_path.Text = defaultPath;
                    Log("[路徑] 偵測到多個可能的遊戲位置，為避免誤選，請手動選擇正確位置：");
                    foreach (var candidate in candidates)
                    {
                        Log("[路徑]   " + candidate);
                    }
                }
                return;
            }

            textBox_path.Text = defaultPath;
            Log("[路徑] 未自動偵測到遊戲位置，請確認路徑或按「瀏覽...」手動選擇。");
        }

        public void Log(string data)
        {
            Action append = () => textBox_log.AppendText(DateTime.Now.ToString() + " " + data + Environment.NewLine);
            if (InvokeRequired)
            {
                Invoke(append);
            }
            else
            {
                append();
            }
        }

        public void Oops(string e)
        {
            Log(e);
            MessageBox.Show(e, "致命錯誤", MessageBoxButtons.OK, MessageBoxIcon.Error);
        }

        public bool patchSCX(Dictionary<string, MPKEntry> mpk, string charset, Dictionary<string, dynamic> scx)
        {
            Log("[SCX] 正在套用 SCX 修補資料...");
            foreach (KeyValuePair<string, dynamic> kv in scx)
            {
                if (!mpk.ContainsKey(kv.Key))
                {
                    Oops("[SCX] 找不到檔案 " + kv.Key);
                    return false;
                }
                Log("[SCX] 正在對 " + kv.Key + " 套用修補資料...");

                using (var ms = new MemoryStream())
                using (var reader = new SCXReader(mpk[kv.Key].Data, charset))
                using (var writer = new SCXWriter(ms, charset))
                {
                    var sb = new StringBuilder();
                    if (!SCX.ApplyPatch(kv.Value, reader, writer, sb))
                    {
                        Log(sb.ToString());
                        Oops("[SCX] 修補資料套用失敗");
                        return false;
                    }
                    mpk[kv.Key].SetData(ms.ToArray());
                }
            }
            return true;
        }

        public bool patchFile(Dictionary<string, MPKEntry> mpk, Dictionary<string, dynamic> data)
        {
            Log("[FILE] 正在套用檔案修補資料...");
            foreach (KeyValuePair<string, dynamic> kv in data)
            {
                if (!mpk.ContainsKey(kv.Key))
                {
                    Log("[FILE] 找不到檔案 " + kv.Key);
                    continue;
                }
                Log("[FILE] 正在取代檔案 " + kv.Key + " ...");
                using (var ms = new MemoryStream(Convert.FromBase64String(kv.Value)))
                using (var gzip = new GZipStream(ms, CompressionMode.Decompress))
                using (var output = new MemoryStream())
                {
                    gzip.CopyTo(output);
                    mpk[kv.Key].SetData(output.ToArray());
                }
            }
            return true;
        }

        private void textBox_path_DragOver(object sender, DragEventArgs e)
        {
            if (e.Data.GetDataPresent(DataFormats.FileDrop) || e.Data.GetDataPresent(DataFormats.Text))
            {
                e.Effect = DragDropEffects.Copy;
            }
        }

        private void textBox_path_DragDrop(object sender, DragEventArgs e)
        {
            var box = sender as TextBox;
            if (e.Data.GetDataPresent(DataFormats.FileDrop))
            {
                box.Text = (e.Data.GetData(DataFormats.FileDrop) as string[])[0];
            }
            else if (e.Data.GetDataPresent(DataFormats.Text))
            {
                box.Text = e.Data.GetData(DataFormats.Text) as string;
            }
        }

        private void button_patch_Click(object sender, EventArgs e)
        {
            textBox_log.Clear();
            button_patch.Enabled = false;
            ThreadPool.QueueUserWorkItem(s =>
            {
                try
                {
                    var usrdir = Path.Combine(textBox_path.Text, "USRDIR");
                    Log("[BERD] 正在尋找 USRDIR...");
                    if (!Directory.Exists(usrdir))
                    {
                        Oops("[BERD] 找不到 USRDIR，請確認遊戲安裝路徑是否正確。");
                        Invoke(new Action(() => button_patch.Enabled = true));
                        return;
                    }

                    var bakdir = usrdir + ".bak";
                    if (!Directory.Exists(bakdir))
                    {
                        Log("[BERD] 找不到備份資料夾，正在建立...");
                        Directory.CreateDirectory(bakdir);
                    }

                    foreach (var patch in Directory.GetFiles(PATCH_DIR, "*.json").Select(p => JSON.ToObject<Dictionary<string, dynamic>>(File.ReadAllText(p))))
                    {
                        if (!patch.ContainsKey("file"))
                        {
                            continue;
                        }
                        string file = patch["file"];
                        if (!File.Exists(Path.Combine(bakdir, file)))
                        {
                            Log("[BERD] 正在備份 " + file + "...");
                            File.Copy(Path.Combine(usrdir, file), Path.Combine(bakdir, file));
                        }

                        MPK mpk = null;
                        Log("[MPK] 正在載入 " + file + "...");
                        using (var reader = new BinaryReader(File.OpenRead(Path.Combine(bakdir, file))))
                        {
                            mpk = MPK.ReadFile(reader);
                        }

                        var entries = mpk.Entries.ToDictionary(k => k.Name, v => v);
                        switch (patch["type"])
                        {
                        case "scx":
                            if (!patchSCX(entries, patch["charset_preset"] + patch["charset"], patch["data"]))
                            {
                                return;
                            }
                            break;
                        case "file":
                            if (!patchFile(entries, patch["data"]))
                            {
                                return;
                            }
                            break;
                        default:
                            Oops("未知的修補類型");
                            Invoke(new Action(() => button_patch.Enabled = true));
                            return;
                        }

                        Log("[MPK] 正在重新封裝 " + file + "...");
                        using (var writer = new BinaryWriter(File.Open(Path.Combine(usrdir, file), FileMode.Create)))
                        {
                            mpk.Write(writer);
                            Log("[MPK] 封裝完成：" + writer.BaseStream.Position);
                        }
                    }

                    MessageBox.Show("修補檔套用完成，請確認遊戲是否能正常執行。", "完成", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    Log("[EasyPatcher] 作業完成，請確認遊戲是否能正常執行。");
                }
                catch (Exception ex)
                {
                    Oops(ex.ToString());
                    Log("[EasyPatcher] 發生致命錯誤");
                }
                Invoke(new Action(() => button_patch.Enabled = true));
            });
        }

        private void button_delete_bak_Click(object sender, EventArgs e)
        {
            try
            {
                var usrdir = Path.Combine(textBox_path.Text, "USRDIR");
                if (!Directory.Exists(usrdir))
                {
                    Oops("找不到 USRDIR，請確認遊戲安裝路徑是否正確。");
                    return;
                }
                var bakdir = usrdir + ".bak";
                if (!Directory.Exists(bakdir))
                {
                    Oops("找不到備份資料夾。");
                    return;
                }
                if (MessageBox.Show("確定要刪除備份資料夾嗎？\n刪除後若要還原修補內容，必須重新驗證遊戲檔案完整性，\n而且可能影響後續修補版本的套用。", "操作確認", MessageBoxButtons.OKCancel, MessageBoxIcon.Warning) != DialogResult.OK)
                {
                    return;
                }
                Directory.Delete(bakdir, true);
                MessageBox.Show("備份資料夾已刪除。", "完成", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            catch (Exception ex)
            {
                Oops(ex.ToString());
            }
        }

        private void button_save_Click(object sender, EventArgs e)
        {
            var save = new SaveFileDialog
            {
                Filter = "日誌檔案 (*.log)|*.log",
                DefaultExt = "log",
                CheckPathExists = true
            };
            if (save.ShowDialog() == DialogResult.OK)
            {
                using (var writer = new StreamWriter(save.OpenFile()))
                {
                    writer.Write(textBox_log.Text);
                }
            }
        }

        private void button_select_Click(object sender, EventArgs e)
        {
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                textBox_path.Text = folderBrowserDialog1.SelectedPath;
            }
        }

        private void linkLabel_version_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start("https://github.com/hwakeyeTW/MagesTools");
        }
    }
}
