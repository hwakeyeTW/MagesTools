# MAGES 遊戲中文化模組

此目錄保存各遊戲／語系專屬的中文化模組來源與維護資料。EasyPatcher、MagesLib 等共用工具仍維持在 Repository 根層級，不重複複製到各遊戲專案中。

本 Repository 對完整中文化成果使用「**模組**」一詞；既有 `Patches/` 目錄名稱，以及 patch data、`patch/berd/`、EasyPatcher 等技術名稱，則維持既有實作與路徑命名。

## 目錄結構

`Patches/<Series>/<Game>/<Locale>/`

各遊戲／語系目錄自行保存：

- 中文化資料；
- 說明文件；
- 著作權／第三方聲明與授權文件；
- 維護腳本與驗證資料（工程／維護用途）；
- machine-readable authority（主要供工具與自動化／維護流程使用）；
- selected milestone evidence（專案紀錄／驗證用途）。

## 現有專案

- [`SteinsGate/`](SteinsGate/) — STEINS;GATE 系列中文化模組。
  - [`MyDarlingsEmbrace/zh-TW/`](SteinsGate/MyDarlingsEmbrace/zh-TW/) — *STEINS;GATE: My Darling's Embrace* 台灣繁體中文化模組。
