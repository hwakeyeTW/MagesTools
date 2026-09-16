# 第三方專案與元件聲明

> English reference version: [`THIRD_PARTY_NOTICES.en.md`](THIRD_PARTY_NOTICES.en.md)

本文件記錄與《STEINS;GATE 比翼雙飛的戀人》台灣繁體中文化模組及其工具／建置 lineage 有實質關聯的第三方專案與元件。

本文件用於 attribution 與 provenance 說明，不取代各第三方專案原始授權文字。

## MagesTools / EasyPatcher / MagesLib

上游專案：

- 專案：**MagesTools**
- Repository：<https://github.com/fengberd/MagesTools>
- 原始作者／著作權聲明：`Copyright (c) 2020 FENGberd`
- 授權：**MIT License**

目前的 <https://github.com/hwakeyeTW/MagesTools> 為該專案的 fork，保留上游工具鏈 lineage，並加入台灣繁體中文 EasyPatcher 介面、Steam 安裝路徑偵測，以及各遊戲中文化模組所需的維護資料。

上游 MIT License 副本保存在 [`licenses/MAGES_TOOLS_MIT.txt`](licenses/MAGES_TOOLS_MIT.txt)。

本中文化模組使用 EasyPatcher 與 MagesLib 進行 patch 套用與 MAGES 格式處理。v1.0.0 所接受的 exact binary／tooling identity 另記錄於 `../authority/TOOLING_REFERENCE.json`；machine-readable release authority 不應由本文件推定。

## fastJSON

`fastJSON.dll` 為 EasyPatcher／MagesTools 軟體 lineage 使用的 JSON dependency，並繼承自原始 MagesTools distribution。

就目前文件修訂而言，這顆 inherited DLL 的 exact historical binary-version provenance 與對應授權聲明，尚未由 binary 本身獨立確認。因此本文件**不會**僅依現行其他 upstream repository 的狀態，替該歷史 binary 推定或重新指定授權。

在文件正式併入主要分支前，較理想的處理方式為以下其一：

1. 確認 exact inherited binary provenance／license，並在此補充；或
2. 明確保留「繼承自原始 MagesTools distribution」的 attribution，而不超出已驗證的 provenance 範圍。

此不確定性僅涉及 attribution 文件完整度，不改變已接受 v1.0.0 模組內 binary identity。

## GenYo Gothic / 源樣黑體

本專案字型生成／維護流程所使用的字型來源包括：

- 字型家族／專案：**GenYo Gothic / 源樣黑體**
- 上游 Repository：<https://github.com/ButTaiwan/genyog-font>
- 維護者／專案作者：**ButTaiwan**
- 本專案相關建置來源：`GenYoGothic2TW-M.otf`
- 授權：**SIL Open Font License 1.1**

GenYo Gothic 上游專案說明該字型家族衍生自 Adobe **Source Han Sans / 思源黑體**，並以 SIL Open Font License 1.1 授權。

本模組的一般公開遊戲 distribution 包含由該字型生成的遊戲 FONT texture，而不是把來源 OTF 當作一般使用者模組檔案重新散布。

上游 OFL 文字副本保存在 [`licenses/GENYO_GOTHIC_OFL-1.1.txt`](licenses/GENYO_GOTHIC_OFL-1.1.txt)。

## Source Han Sans lineage

GenYo Gothic 上游隨附的 OFL 文字包含：

`Copyright 2014-2019 Adobe (http://www.adobe.com/), with Reserved Font Name 'Source'.`

Source Han Sans／Source 名稱、著作權、Reserved Font Name 與衍生字型條件，仍依適用的 SIL Open Font License 條款為準。

## OpenAI GPT-5.6 Sol

本專案在大量翻譯、重譯、台灣用語改寫、審查輔助、一致性分析與專案維護流程中，使用 **OpenAI GPT-5.6 Sol** 作為主要語言模型工具。

此處揭露僅用於說明專案流程透明度；不代表 OpenAI 是原作遊戲或本非官方中文化模組的作者、發行者、贊助者或背書者。

AI 輔助在地化方法與 acceptance boundary 請參閱 [`../docs/LOCALIZATION_METHODOLOGY.md`](../docs/LOCALIZATION_METHODOLOGY.md)。

## 原作遊戲素材

原始 *STEINS;GATE* 遊戲素材與官方翻譯文本並非本 Repository 的第三方開源 dependency，也不因上述聲明而被重新授權。相關權利仍屬各自權利人所有；請參閱 [`NOTICE.md`](NOTICE.md)。
