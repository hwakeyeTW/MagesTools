# 來源與目錄結構

本中文化模組採分層 Repository 結構，將 runtime patch data、machine-readable authority、維護實作、使用者文件，以及著作權／第三方聲明分開保存，避免所有資訊都堆疊在單一 README 中。

## 公開模組目錄

- `patch/berd/` — EasyPatcher 實際使用的公開中文化資料。
- `docs/` — 翻譯方法、致謝、維護、重製、術語與來源結構等人類可讀文件。
- `legal/` — 原作權利聲明、第三方 attribution 與相關授權文件。
- `authority/` — release、private source、tooling 與 path 的 machine-readable exact bindings。
- `maintenance/` — repository-native 維護實作與保留的驗證參考資料。
- `milestones/` — accepted milestone 的選定 immutable evidence。

使用者可見文件以「**中文化模組**」描述完整專案；既有 `Patches/`、`patch/berd/`、EasyPatcher，以及已發布 artifact 名稱中的 `Patch` 等技術路徑與實作名稱維持原名。

## 來源語料邊界

Private JP／官方英文／alignment／recovered-source corpus 保存在 `hwakeyeTW/MagesTranslationSources` 對應的系列／遊戲／語系路徑中，並透過本模組的 authority metadata 綁定。

公開 Repository 不完整重製或散布翻譯與術語查證過程所使用的官方日文、英文或其他官方語言 corpus。

完整 frozen B-postfix maintenance archive 仍維持 external/archive-only，不 wholesale 複製進任何 Git history。

## 人類可讀的來源與方法說明

翻譯來源優先順序與 AI 使用揭露請參閱 [`LOCALIZATION_METHODOLOGY.md`](LOCALIZATION_METHODOLOGY.md)。

原作、工具、字型、AI 工具與社群致謝請參閱 [`CREDITS.md`](CREDITS.md)。

著作權與第三方授權資訊請參閱 [`../legal/`](../legal/)。
