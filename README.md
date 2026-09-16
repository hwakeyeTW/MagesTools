# MagesTools

本 Repository 為 [`fengberd/MagesTools`](https://github.com/fengberd/MagesTools) 的 fork，主要提供 MAGES（5pb.）視覺小說引擎相關工具，並作為本專案各遊戲中文化模組的公開來源 Repository。

## 主要功能

- MPK 解包／封包；
- SCX 字串匯出／套用；
- 透過 EasyPatcher 套用遊戲中文化資料。

Repository 層級的軟體依 [`LICENSE`](LICENSE) 所載授權條款提供。各遊戲中文化模組可能另有原作權利、第三方授權、來源權威與維護資訊，請依各模組目錄內文件為準。

## Repository 結構

| 路徑 | 用途 |
| --- | --- |
| `EasyPatcher/` | EasyPatcher 原始碼與介面實作。 |
| `MagesLib/` | 共用的 MAGES 格式解析／寫入函式庫。 |
| `MagesTools/` | 一般 MAGES 工具。 |
| `Scripts/` | 輔助處理與建置腳本。 |
| `lib/` | Repository 軟體使用的共用 binary dependency。 |
| `Patches/` | 依遊戲／系列／語系區分的中文化模組來源、authority、維護資料與文件。 |

各遊戲中文化專案的索引請參閱 [`Patches/README.md`](Patches/README.md)。

## 中文化模組

目前公開的中文化專案包括：

- [`STEINS;GATE 比翼雙飛的戀人 — 台灣繁體中文化模組`](Patches/SteinsGate/MyDarlingsEmbrace/zh-TW/README.md)

各模組的著作權與第三方聲明、翻譯方法、致謝、維護與 authority 資料，皆依專案結構保存在各自的遊戲／語系目錄中，而不重複堆疊於 Repository 根目錄。

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

## 上游專案與授權

原始 MagesTools 上游專案：

- Repository：[`fengberd/MagesTools`](https://github.com/fengberd/MagesTools)
- 原始軟體著作權聲明：`Copyright (c) 2020 FENGberd`
- 授權：MIT License

本 fork 保留原始工具鏈 lineage，並加入台灣繁體中文 EasyPatcher 介面、Steam 安裝路徑偵測，以及各遊戲中文化模組所需的公開維護資料。
