# 在地化方法與 AI 使用揭露
# Localization Methodology & AI Disclosure

## 目的

本文件說明《STEINS;GATE 比翼雙飛的戀人》台灣繁體中文化模組在翻譯、術語統一、AI 輔助、審查與來源使用上的基本方法。

本文件不取代 `authority/` 內主要供工具與維護流程使用的 machine-readable bindings、Planner decisions 或 accepted artifact records。

## 翻譯權威順序

本專案採 **JP-first** 原則。語意與術語判定的主要優先順序如下：

1. **日文原文**；
2. **既有官方繁體中文**，適用時優先參考 *STEINS;GATE ELITE* 的官方繁體中文譯名與系列術語；
3. **官方英文版本**；
4. **既有簡體中文／舊繁體中文譯名**；
5. **第三方資料與台灣玩家社群長期使用的譯名／用語慣例**。

日文原文始終是最高語意依據。

官方繁體中文主要用於既有角色名、組織名、地名、科學／技術概念、網路文化詞彙與系列固定術語的一致性；官方英文則作為語意理解、斷句、對照與來源恢復時的輔助資料，不高於日文原文。

台灣玩家社群慣用譯名屬於補充參考，主要用於既有系列文化、台灣自然用語與玩家長期熟悉的稱呼。這不代表本專案直接複製或整合某一個未具名民間翻譯專案的完整文本。

## 目標語言

目標語言為自然的 **台灣繁體中文**，而非機械式簡繁轉換。

翻譯與校對時會特別處理：

- 台灣／中國大陸詞彙差異；
- 日文直譯與不自然語序；
- 主詞、指涉、否定、條件、因果與語氣強度；
- 角色個別口吻；
- 宅文化、網路語言與雙關；
- Science Adventure 系列既有術語一致性；
- UI、TIPS、郵件與一般對話的不同文體需求。

## GPT-5.6 Sol 使用揭露

本專案的主要在地化工作流程使用 **OpenAI GPT-5.6 Sol** 作為主要語言模型工具之一，涵蓋大量：

- 初步翻譯與重譯；
- 台灣用語改寫；
- 角色語氣調整建議；
- 日／英／中語意對照；
- 術語一致性檢查；
- finding 分析與 corrective translation 輔助；
- 文件、validation ledger 與維護資料整理。

本專案因此屬於 **AI-assisted localization / AI 輔助在地化**，而不是一次性自動機器翻譯。

AI 輸出不會因模型產生本身而自動成為最終譯文。最終內容仍需符合專案既定的來源權威、術語規範、審查 finding、Planner adjudication、結構驗證與 runtime/playtest evidence。

模型名稱的揭露只描述本專案實際使用的工具，不代表 OpenAI 對本遊戲、原作權利人或本 fan-localization project 的贊助、認可或官方參與。

## 官方中文與系列術語

本專案會主動參考既有 *STEINS;GATE* 系列官方繁體中文譯名，以減少同一概念在不同作品之間產生不必要的名稱漂移。

適用時，*STEINS;GATE ELITE* 的官方繁體中文譯名是重要的 terminology reference。若官方譯名與本作日文語境、來源概念或台灣自然語言存在明確衝突，仍會回到日文原文重新判定，而不是盲目替換。

公開 Repository 中保留的 `SGMDE_BlindReview_Normative_Terminology_v2.2.md` 是既有術語治理成果之一；它是語意 constraint，而不是無條件的字串 replacement table。

## 台灣社群用語參考

對沒有適用官方譯名、不同官方版本存在差異，或涉及網路／宅文化、迷因與口語表現的項目，本專案會參考台灣玩家社群長期使用的稱呼與語感。

此類參考的原則是：

- 不高於日文原文；
- 不高於適用的官方系列固定譯名；
- 優先選擇台灣玩家自然理解的表達；
- 若來源或社群譯法存在衝突，保留查證與 adjudication，而不是默認沿用。

若未來能明確確認某個公開 Wiki、翻譯專案或特定貢獻者對本模組形成可辨識的直接貢獻，應在 [`CREDITS.md`](CREDITS.md) 具名致謝，而不以「社群慣用」模糊代替具名 attribution。

## 審查與驗證

翻譯完成並不代表直接發布。專案流程包含：

- bounded batch translation；
- terminology / source authority 檢查；
- independent review；
- finding adjudication；
- corrective implementation；
- script / SCX / MPK 結構驗證；
- runtime obligations；
- 實機遊玩與顯示測試；
- deterministic Gate / release verification。

這些流程的存在是為了降低單一翻譯者或單一模型輸出直接進入 release 的風險。

## 官方語料與公開 Repository 邊界

官方日文、官方英文及其他官方中文版本的文本著作權仍分別屬原權利人所有。

這些資料在專案中作為翻譯、語意核對、術語比對、alignment 與 source recovery 的參考，不代表本專案取得其著作權或重新授權權利。

為避免不必要地重新散布完整官方語料，公開 Repository 不 wholesale 收錄完整 JP / official EN / official TC corpus 或內部 alignment corpus。

公開／私有來源結構請參閱 [`SOURCE_LAYOUT.md`](SOURCE_LAYOUT.md)；原作權利與第三方授權範圍請參閱 [`../legal/NOTICE.md`](../legal/NOTICE.md) 與 [`../legal/THIRD_PARTY_NOTICES.md`](../legal/THIRD_PARTY_NOTICES.md)。
