# STEINS;GATE 比翼雙飛的戀人 — 台灣繁體中文化模組

*STEINS;GATE: My Darling's Embrace — Traditional Chinese (Taiwan) Localization Module*

> 本專案為玩家製作的非官方台灣繁體中文化模組，並非 MAGES. Inc.、Spike Chunsoft Co., Ltd. 或其他原作權利人製作或認可的官方繁體中文版。完整權利與第三方聲明請參閱 [`legal/`](legal/)。

## 專案簡介

本模組提供 Steam 英文版 *STEINS;GATE: My Darling's Embrace* 的台灣繁體中文在地化內容，並使用 EasyPatcher 將 `patch/berd/` 中的中文化資料套用至使用者自行持有的遊戲安裝目錄。

- **適用版本**：Steam 英文版
- **Steam App ID**：`970560`
- **介面／文本目標**：台灣繁體中文

套用前請使用乾淨的 Steam 英文版遊戲檔案，或保留由乾淨英文版建立的 `USRDIR.bak`。EasyPatcher 支援 Steam 安裝路徑自動偵測。

## 翻譯與在地化方法

本專案採 **JP-first** 的在地化原則：日文原文是最高語意依據；既有官方繁體中文譯名與術語（適用時優先參考 *STEINS;GATE ELITE*）用於系列術語一致性；官方英文作為語意輔助；台灣玩家社群長期使用的譯名與用語慣例則作為補充參考。

主要在地化工作流程使用 **OpenAI GPT-5.6 Sol** 作為語言模型工具，並搭配專案級術語規範、批次審查、finding adjudication、corrective translation、結構驗證與實機測試。AI 輸出不會因模型產生本身而自動成為最終譯文。

詳細說明請參閱 [`docs/LOCALIZATION_METHODOLOGY.md`](docs/LOCALIZATION_METHODOLOGY.md)。

## 下載

請至 [GitHub Releases](https://github.com/hwakeyeTW/MagesTools/releases/latest) 下載最新版本的《STEINS;GATE 比翼雙飛的戀人》台灣繁體中文化模組。

各版本的檔案名稱、版本資訊與完整性驗證資料，以對應的 Release 頁面為準。

## 文件索引

| 文件 / 路徑 | 內容 |
| --- | --- |
| [`docs/LOCALIZATION_METHODOLOGY.md`](docs/LOCALIZATION_METHODOLOGY.md) | 翻譯權威順序、AI 使用揭露、官方／社群譯名參考原則。 |
| [`docs/CREDITS.md`](docs/CREDITS.md) | 原作、工具、字型、AI 工具與社群致謝。 |
| [`legal/NOTICE.md`](legal/NOTICE.md) | 非官方專案、原作權利、商標與授權範圍聲明。 |
| [`legal/NOTICE.en.md`](legal/NOTICE.en.md) | `legal/NOTICE.md` 的英文參考版本。 |
| [`legal/THIRD_PARTY_NOTICES.md`](legal/THIRD_PARTY_NOTICES.md) | MagesTools、字型與其他第三方元件資訊。 |
| [`legal/THIRD_PARTY_NOTICES.en.md`](legal/THIRD_PARTY_NOTICES.en.md) | 第三方聲明的英文參考版本。 |
| [`docs/SOURCE_LAYOUT.md`](docs/SOURCE_LAYOUT.md) | 公開／私有來源與 Repository path 分工。 |
| [`docs/MAINTENANCE.md`](docs/MAINTENANCE.md) | 維護資料與 repository-native maintenance 說明。 |
| [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md) | 重製與驗證資訊。 |
| [`CHANGELOG.md`](CHANGELOG.md) | 公開版本變更紀錄。 |
| [`NOTICE.md`](NOTICE.md) | 穩定的 Notice 入口，導向 `legal/` 內完整聲明。 |

## 專案結構

- `patch/berd/` — EasyPatcher 使用的公開中文化資料。
- `docs/` — 人類可讀的翻譯方法、來源結構、維護、重製與致謝文件。
- `legal/` — 原作權利、第三方 attribution 與授權文件。
- `authority/` — release、private source、tooling 與 path 的 machine-readable exact bindings。
- `maintenance/` — repository-native 維護實作與驗證參考。
- `milestones/` — accepted milestone 的選定 immutable evidence。

完整官方日文／官方英文語料、alignment 與 recovered-source corpus 不隨公開 Repository 完整散布；其來源綁定請參閱 `authority/` 與 [`docs/SOURCE_LAYOUT.md`](docs/SOURCE_LAYOUT.md)。

使用者文件以「**模組**」稱呼完整中文化成果；既有 `Patches/`、`patch/berd/`、EasyPatcher，以及已發布檔名中的 `Patch` 等技術路徑、工具名稱或既有 artifact identity 仍維持原名。

## 問題回報

若遊玩過程中發現翻譯、顯示、TIPS 或其他模組相關問題，請透過本 Repository 的 Issues 回報。若能提供截圖、劇情／場景位置與重現方式，會更有助於確認。
