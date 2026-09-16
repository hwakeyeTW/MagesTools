# MagesTools

This repository is a fork of [`fengberd/MagesTools`](https://github.com/fengberd/MagesTools), an all-in-one toolset for the MAGES (aka 5pb.) visual novel engine.

Major functions include:

- MPK unpacking / packing;
- SCX string exporting / patching;
- EasyPatcher-based game localization deployment.

The repository-level software remains governed by the repository [`LICENSE`](LICENSE). Game-specific localization modules may include separate rights, notices, source authority, maintenance metadata, and third-party attributions under their own paths.

## Repository structure

| Path | Purpose |
| --- | --- |
| `EasyPatcher/` | EasyPatcher source and UI implementation. |
| `MagesLib/` | Shared MAGES format parsing / writing library. |
| `MagesTools/` | General MAGES utility tooling. |
| `Scripts/` | Auxiliary processing/build scripts. |
| `lib/` | Shared binary dependencies used by repository software. |
| `Patches/` | Game/series/locale-specific localization module sources, authority metadata, maintenance material, and documentation. |

See [`Patches/README.md`](Patches/README.md) for the game-localization project index.

## Localization modules

Current public localization work includes:

- [`STEINS;GATE: My Darling's Embrace — 台灣繁體中文化模組`](Patches/SteinsGate/MyDarlingsEmbrace/zh-TW/README.md)

Game-specific legal notices, translation methodology, third-party acknowledgements, and release authority are maintained inside each module directory rather than duplicated at repository root.

## EasyPatcher（繁體中文）

此 fork 的 EasyPatcher 介面已在地化為台灣繁體中文，並加入 Steam 遊戲安裝路徑自動偵測。

啟動時會依序：

1. 檢查 `berd/meta.json` 的 `default_path`。
2. 從 Windows Registry 找出 Steam 安裝位置。
3. 讀取 `steamapps/libraryfolders.vdf`，掃描所有 Steam 遊戲庫。
4. 若 `meta.json` 提供 `steam_app_id`，優先讀取對應的 `appmanifest_<appid>.acf`。
5. 若未提供 App ID，則使用 `default_path` 最後一層的資料夾名稱來尋找遊戲。
6. 只有包含 `USRDIR` 的資料夾才會視為有效的遊戲路徑。

若只找到一個可能的路徑，EasyPatcher 會自動填入；若找到多個且無法安全判斷，則會讓使用者手動選擇，不會任意挑選。

`steam_app_id` 為選填欄位，舊版 `meta.json` 不需要修改即可繼續使用。例如：

```json
{
  "name": "Example Patch",
  "default_path": "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Example Game",
  "steam_app_id": "123456"
}
```

## Upstream and license

Original MagesTools upstream:

- Repository: [`fengberd/MagesTools`](https://github.com/fengberd/MagesTools)
- Original software copyright: `Copyright (c) 2020 FENGberd`
- License: MIT

This fork retains that upstream lineage while adding Taiwan Traditional Chinese EasyPatcher localization, Steam installation-path detection, and game-specific localization-module maintenance material.
