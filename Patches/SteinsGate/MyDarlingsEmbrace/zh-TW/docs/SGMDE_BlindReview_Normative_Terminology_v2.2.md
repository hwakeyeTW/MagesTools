# SGMDE Blind Review Normative Terminology v2.2

> Purpose: minimal, history-blind terminology constraints for the Fresh Independent Blind Full-Script Translation Review.
> Source: SGMDE Blind Review Normative Terminology v2.1 + PADJ-READY01 / MANUAL-DECISION-001 (170 rows; pending/candidate 0).

## Usage rules

- This is a **semantic terminology constraint, not a blind string-replacement table**.
- Determine the Japanese concept, grammatical role, ruby/base-text structure, quotation status, and local context before applying a term.
- `TIPS` rows primarily constrain the corresponding Tips title/concept; do not force a Tips title into unrelated ordinary prose merely because the surface Japanese overlaps.
- `CORE` rows constrain recurring names, organizations, technologies, places, and fixed concepts where the identified Japanese concept is actually present.
- If the Japanese source and a listed scope appear incompatible, report `TERMINOLOGY_SCOPE_CONFLICT` instead of silently forcing the glossary.
- Exact Latin width/casing is normative where the required TC form is intentionally ASCII (for example `UPX`, `w`, `@ch`, `COMIMA`, `MewTube`, `MMORPG`).

## Normative rows

| ID | Scope | JP / reading | Required TC | Allowed aliases | Lock class | Confidence | Scope note |
|---|---|---|---|---|---|---|---|
| TIP-001 | TIPS | あるまだかいせん | 無敵艦隊海戰 |  | KEEP_LOCK | MEDIUM |  |
| TIP-002 | TIPS | あわせ | 團體 Cosplay | 合 Cos / Gathering | JP_TW_LOCK | MEDIUM |  |
| TIP-003 | TIPS | あんざいせんせい | 安西教練 |  | KEEP_LOCK | MEDIUM |  |
| TIP-004 | TIPS | いちじでんち | 一次電池 |  | KEEP_LOCK | MEDIUM |  |
| TIP-005 | TIPS | いまきたさんぎょう | 今北產業 |  | KEEP_LOCK | MEDIUM |  |
| TIP-006 | TIPS | いんようごぎょうしそう | 陰陽五行思想 |  | KEEP_LOCK | MEDIUM |  |
| TIP-007 | TIPS | うぷ | ＵＰ |  | KEEP_LOCK | MEDIUM |  |
| TIP-008 | TIPS | えきさいとせんせい | Excite老師 |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-009 | TIPS | おつ | 乙 |  | REBOOT_OVERRIDE | HIGH |  |
| TIP-010 | TIPS | おでんかん | 關東煮罐頭 |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-011 | TIPS | おふかい | 網聚 |  | KEEP_LOCK | MEDIUM |  |
| TIP-012 | TIPS | かいちゅー | 懷啾～ | カイちゅ〜 | JP_TW_LOCK | MEDIUM |  |
| TIP-013 | TIPS | かいば | 海馬迴 |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-014 | TIPS | かたづけられないおんな | 邋遢女 |  | KEEP_LOCK | MEDIUM |  |
| TIP-015 | TIPS | かっぷやきそばゆーま | 杯裝速食炒麵ＵＭＡ |  | KEEP_LOCK | MEDIUM |  |
| TIP-016 | TIPS | かべいろい | 卡貝羅伊 | Kabeiroi / カベイロイ | JP_TW_LOCK | MEDIUM |  |
| TIP-017 | TIPS | かみよもじ | 神代文字 | 神代文字 | JP_TW_LOCK | HIGH |  |
| TIP-018 | TIPS | かもぷり | 卡莫普莉 | カモプリ | JP_TW_LOCK | MEDIUM |  |
| TIP-019 | TIPS | きかん | 機關 |  | KEEP_LOCK | MEDIUM |  |
| TIP-020 | TIPS | きゃすとおふ | Cast Off | キャストオフ | JP_TW_LOCK | MEDIUM |  |
| TIP-021 | TIPS | くろと | 克洛特 | クロト | JP_TW_LOCK | HIGH |  |
| TIP-022 | TIPS | くんかくんか | 嗅嗅 | くんかくんか / Sniff Sniff | JP_TW_LOCK | MEDIUM |  |
| TIP-023 | TIPS | けだもののやり | 野獸之槍 |  | KEEP_LOCK | MEDIUM |  |
| TIP-024 | TIPS | こうかくきどうめいさいぼーる | 攻殼機動迷彩球 |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-025 | TIPS | こうりん | 降臨 |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-026 | TIPS | こみま | COMIMA |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-027 | TIPS | こんた | 昆太 | こん太 / Conta | JP_TW_LOCK | MEDIUM |  |
| TIP-028 | TIPS | さーせん | 搜哩 |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-029 | TIPS | さいみんりょうほう | 催眠療法 |  | KEEP_LOCK | MEDIUM |  |
| TIP-030 | TIPS | さいりうむせーばー | 超級螢光劍 |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-031 | TIPS | さばげー | 生存遊戲 |  | KEEP_LOCK | MEDIUM |  |
| TIP-032 | TIPS | さもとらけのにけ | 薩莫色雷斯的勝利女神 | Nike of Samothrace | JP_TW_LOCK | HIGH |  |
| TIP-033 | TIPS | さる | 猴子 |  | KEEP_LOCK | MEDIUM |  |
| TIP-034 | TIPS | じーくしおん | 西翁萬歲 | Sieg Scion | JP_TW_LOCK | MEDIUM |  |
| TIP-035 | TIPS | しぇう゛ん | 修芬 | Sjöfn | JP_TW_LOCK | MEDIUM |  |
| TIP-036 | TIPS | しじんそうおう | 四神相應 |  | KEEP_LOCK | MEDIUM |  |
| TIP-037 | TIPS | しねまこんぷれっくす | 影城 | Cinema Complex / 複合式影城 | JP_TW_LOCK | HIGH |  |
| TIP-038 | TIPS | じょうこう | 常考 |  | KEEP_LOCK | MEDIUM |  |
| TIP-039 | TIPS | しょうわくせいあぽふぃす | 小行星阿波菲斯 |  | KEEP_LOCK | MEDIUM |  |
| TIP-040 | TIPS | じょんたいたー | 約翰・提托 |  | ELITE_OFFICIAL_LOCK | HIGH | TIPS-title scope. Outside the TIPS title, compare CORE-012 rather than forcing this form; if scope is unclear, flag TERMINOLOGY_SCOPE_CONFLICT. |
| TIP-041 | TIPS | すーぱーはかー | 超級哈客 |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-042 | TIPS | せいぶこうえんゆうえんち | 西武公園遊樂園 | 西武公園ゆうえんち | JP_TW_LOCK | MEDIUM |  |
| TIP-043 | TIPS | せんすいえいほう | 潛水泳法 |  | KEEP_LOCK | MEDIUM |  |
| TIP-044 | TIPS | そんなそうびでだいじょうぶか | 這樣的裝備沒問題嗎？ | そんな装備で大丈夫か？ | JP_TW_LOCK | MEDIUM |  |
| TIP-045 | TIPS | だーりんのばかぁ | 達令你這個笨蛋！ | Darling, You Idiot! | JP_TW_LOCK | MEDIUM |  |
| TIP-046 | TIPS | だいびる | DAI大樓 |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-047 | TIPS | たけこぷかめらー | 竹蜻蜓相機 |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-048 | TIPS | だごん | 大袞 |  | KEEP_LOCK | MEDIUM |  |
| TIP-049 | TIPS | ちぇしゃねこ | 笑笑貓 | 柴郡貓 / Cheshire Cat | ELITE_OFFICIAL_LOCK | HIGH | Primary form is 笑笑貓. 柴郡貓 and Cheshire Cat are allowed aliases where the source/context explicitly calls for an alias or explanation. |
| TIP-050 | TIPS | ちゅうにびょう | 中二病 |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-051 | TIPS | つんでれ | 傲嬌 |  | KEEP_LOCK | MEDIUM |  |
| TIP-052 | TIPS | つんどら | 冰山 |  | KEEP_LOCK | MEDIUM |  |
| TIP-053 | TIPS | でんぱじゃっく | 電波劫持 |  | KEEP_LOCK | MEDIUM |  |
| TIP-054 | TIPS | でんわれんじかっこかり | 電話微波爐（暫定） | 電話レンジ（仮） / PhoneWave | JP_TW_LOCK | HIGH | Applies to the exact provisional-name concept 電話レンジ（仮）. Bare 電話レンジ does not automatically license adding （暫定）. |
| TIP-055 | TIPS | とうきょうはんず | 東京手創館 | 東京ハンズ / Tokyo Hands | JP_TW_LOCK | MEDIUM |  |
| TIP-056 | TIPS | どくたーぺっぱー | Dr. Pepper |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-057 | TIPS | なかざわこと | 中澤琴 |  | KEEP_LOCK | MEDIUM |  |
| TIP-058 | TIPS | にこにやなどうが | niconiya動畫 |  | ELITE_CONTEXT_LOCK | HIGH |  |
| TIP-059 | TIPS | にっちさんぎょう | 利基產業 | ニッチ産業 / Niche Industry | JP_TW_LOCK | HIGH |  |
| TIP-060 | TIPS | にやなま | Niya直播 | ニヤ生 / Niya Live / niconiya直播 | JP_TW_LOCK | MEDIUM |  |
| TIP-061 | TIPS | ぬえ | 鵺 |  | KEEP_LOCK | MEDIUM |  |
| TIP-062 | TIPS | ねおち | 睡著了 | 寝落ち | JP_TW_LOCK | MEDIUM |  |
| TIP-063 | TIPS | ねんどどーるぷち | 小黏土娃娃 | ねんどどーるぷち / Nendodoru Petite | JP_TW_LOCK | MEDIUM |  |
| TIP-064 | TIPS | のいずきゃんせりんぐへっどほん | 降噪耳機 |  | KEEP_LOCK | MEDIUM |  |
| TIP-065 | TIPS | のうかがく | 腦科學 |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-066 | TIPS | ののさん | 乃乃小姐 |  | KEEP_LOCK | MEDIUM |  |
| TIP-067 | TIPS | ばーろーのあれ | 「笨蛋」的那個東西 | バーローのアレ | JP_TW_LOCK | MEDIUM |  |
| TIP-068 | TIPS | はげどう | 激同 |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-069 | TIPS | ぱだわん | 帕達萬 | Padawan / Pada-wan | JP_TW_LOCK | MEDIUM |  |
| TIP-070 | TIPS | ぱんつじゃないからはずかしくないもん | 因為不是小褲褲所以才不會害羞呢 |  | KEEP_LOCK | MEDIUM |  |
| TIP-071 | TIPS | ひーとあいらんどげんしょう | 熱島效應 |  | KEEP_LOCK | MEDIUM |  |
| TIP-072 | TIPS | ひえひえぴたぴた | 退熱貼 |  | KEEP_LOCK | MEDIUM |  |
| TIP-073 | TIPS | ひかりでんち | 太陽能電池 | 光電池 / Photo Cell | JP_TW_LOCK | HIGH |  |
| TIP-074 | TIPS | びっくりめがねちゃん | 驚奇小眼鏡 | びっくりメガネちゃん / Surprise Specs | JP_TW_LOCK | MEDIUM |  |
| TIP-075 | TIPS | びっとりゅうしほう | Bit粒子砲 |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-076 | TIPS | ふぁふにーる | 法芙尼爾 |  | KEEP_LOCK | MEDIUM |  |
| TIP-077 | TIPS | ふかきものども | 深潛者 |  | KEEP_LOCK | MEDIUM |  |
| TIP-078 | TIPS | ぶきやほんぽ | 武器屋總店 |  | KEEP_LOCK | MEDIUM |  |
| TIP-079 | TIPS | ふじょし | 腐女 |  | KEEP_LOCK | MEDIUM |  |
| TIP-080 | TIPS | ぷっしゅしきえんとうじょう | 推按式圓柱鎖 |  | KEEP_LOCK | MEDIUM |  |
| TIP-081 | TIPS | ふにとびょるぐ | Hnitbjörg | 夫尼特彪格 / フニトビョルグ | JP_TW_LOCK | MEDIUM |  |
| TIP-082 | TIPS | ふらぐ | FLAG |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-083 | TIPS | ぶらちゅー | 血之旋律 |  | KEEP_LOCK | MEDIUM |  |
| TIP-084 | TIPS | ふれいや | 芙蕾雅 |  | KEEP_LOCK | MEDIUM |  |
| TIP-085 | TIPS | ふれーむわーく | 框架 |  | KEEP_LOCK | MEDIUM |  |
| TIP-086 | TIPS | ほうれんそう | 報連相 | ホウレンソウ / Ho-Ren-So | JP_TW_LOCK | HIGH |  |
| TIP-087 | TIPS | ほーみんぐ・でぃーう゛ぁ | 淚濕女神的歸還 | Homing Diva / 泣き濡れし女神の帰還 | JP_TW_LOCK | MEDIUM |  |
| TIP-088 | TIPS | ぽけべる | B.B.Call |  | ELITE_OFFICIAL_LOCK | HIGH | TIPS title/concept form only. Ordinary dialogue/prose ポケベル should be localized contextually as 呼叫器, not mechanically replaced with B.B.Call. |
| TIP-089 | TIPS | ぼっち | 邊緣人 | ぼっち / Loner | JP_TW_LOCK | MEDIUM |  |
| TIP-090 | TIPS | まいんどこんとろーる | 心智控制 | Mind Control | JP_TW_LOCK | MEDIUM |  |
| TIP-091 | TIPS | またつまらぬものをつなげてしまったばいごえもん | 又接了個無聊的東西by五右衛門 |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-092 | TIPS | まな | 真名 |  | KEEP_LOCK | MEDIUM |  |
| TIP-093 | TIPS | みーみる | 密米爾 | Mímir / ミーミル | JP_TW_LOCK | HIGH | Applies to the Mímir name itself. In ruby/compound naming constructions, preserve the Japanese structural relationship and do not replace the whole phrase blindly. |
| TIP-094 | TIPS | みゅうつべ | MewTube |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-095 | TIPS | みらーれすいちがん | 無反光鏡相機 |  | KEEP_LOCK | MEDIUM |  |
| TIP-096 | TIPS | めいどきっさ | 女僕咖啡廳 |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-097 | TIPS | もあっどすねーく | 諜龍 |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-098 | TIPS | もしかしておらおらですかーっ | 難道是歐啦歐啦嗎ー!? |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-099 | TIPS | やんでれ | 病嬌 |  | KEEP_LOCK | MEDIUM |  |
| TIP-100 | TIPS | らいねっとかける | 雷網路翔 |  | ELITE_COMPONENT_LOCK | HIGH | Base RaiNet Tips name. AccessNo derivative titles use their own TIP-101–TIP-113 exact forms. |
| TIP-101 | TIPS | らいねっとかけるあくせすなんばーわん | 雷網路翔　■ＡｃｃｅｓｓＮｏ．１ |  | ELITE_COMPONENT_LOCK | HIGH | Exact TIPS derivative title; component-derived from the frozen 雷網路翔 base name. |
| TIP-102 | TIPS | らいねっとかけるあくせすなんばーつー | 雷網路翔　■ＡｃｃｅｓｓＮｏ．２ |  | ELITE_COMPONENT_LOCK | HIGH | Exact TIPS derivative title; component-derived from the frozen 雷網路翔 base name. |
| TIP-103 | TIPS | らいねっとかけるあくせすなんばーすりー | 雷網路翔　■ＡｃｃｅｓｓＮｏ．３ |  | ELITE_OFFICIAL_LOCK | HIGH | Exact TIPS derivative title; direct ELITE evidence also confirms 雷網路翔 as the base name. |
| TIP-104 | TIPS | らいねっとかけるあくせすなんばーふぉー | 雷網路翔　■ＡｃｃｅｓｓＮｏ．４ |  | ELITE_COMPONENT_LOCK | HIGH | Exact TIPS derivative title; component-derived from the frozen 雷網路翔 base name. |
| TIP-105 | TIPS | らいねっとかけるあくせすなんばーふぁいぶ | 雷網路翔　■ＡｃｃｅｓｓＮｏ．５ |  | ELITE_COMPONENT_LOCK | HIGH | Exact TIPS derivative title; component-derived from the frozen 雷網路翔 base name. |
| TIP-106 | TIPS | らいねっとかけるあくせすなんばーしっくす | 雷網路翔　■ＡｃｃｅｓｓＮｏ．６ |  | ELITE_COMPONENT_LOCK | HIGH | Exact TIPS derivative title; component-derived from the frozen 雷網路翔 base name. |
| TIP-107 | TIPS | らいねっとかけるあくせすなんばーせぶん | 雷網路翔　■ＡｃｃｅｓｓＮｏ．７ |  | ELITE_COMPONENT_LOCK | HIGH | Exact TIPS derivative title; component-derived from the frozen 雷網路翔 base name. |
| TIP-108 | TIPS | らいねっとかけるあくせすなんばーえいと | 雷網路翔　■ＡｃｃｅｓｓＮｏ．８ |  | ELITE_COMPONENT_LOCK | HIGH | Exact TIPS derivative title; component-derived from the frozen 雷網路翔 base name. |
| TIP-109 | TIPS | らいねっとかけるあくせすなんばーないん | 雷網路翔　■ＡｃｃｅｓｓＮｏ．９ |  | ELITE_COMPONENT_LOCK | HIGH | Exact TIPS derivative title; component-derived from the frozen 雷網路翔 base name. |
| TIP-110 | TIPS | らいねっとかけるあくせすなんばーてん | 雷網路翔　■ＡｃｃｅｓｓＮｏ．１０ |  | ELITE_COMPONENT_LOCK | HIGH | Exact TIPS derivative title; component-derived from the frozen 雷網路翔 base name. |
| TIP-111 | TIPS | らいねっとかけるあくせすなんばーいれぶん | 雷網路翔　■ＡｃｃｅｓｓＮｏ．１１ |  | ELITE_COMPONENT_LOCK | HIGH | Exact TIPS derivative title; component-derived from the frozen 雷網路翔 base name. |
| TIP-112 | TIPS | らいねっとかけるあくせすなんばーとぅえるぶ | 雷網路翔　■ＡｃｃｅｓｓＮｏ．１２ |  | ELITE_COMPONENT_LOCK | HIGH | Exact TIPS derivative title; component-derived from the frozen 雷網路翔 base name. |
| TIP-113 | TIPS | らいねっとかけるあくせすなんばーさーてぃーん | 雷網路翔　■ＡｃｃｅｓｓＮｏ．１３ |  | ELITE_COMPONENT_LOCK | HIGH | Exact TIPS derivative title; component-derived from the frozen 雷網路翔 base name. |
| TIP-114 | TIPS | らっしゅがーど | 防磨衣 | Rash Guard / 水母衣 | JP_TW_LOCK | MEDIUM |  |
| TIP-115 | TIPS | らのべ | 輕小說 |  | KEEP_LOCK | MEDIUM |  |
| TIP-116 | TIPS | りあじゅう | 現充 |  | KEEP_LOCK | MEDIUM |  |
| TIP-117 | TIPS | りあじゅうばくはつしろ | 現充爆炸吧 |  | KEEP_LOCK | MEDIUM |  |
| TIP-118 | TIPS | ろーあんぐらー | 低角度攝淫師 |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-119 | TIPS | ろーれらい | 羅蕾萊 |  | KEEP_LOCK | MEDIUM |  |
| TIP-120 | TIPS | ろぼとみー | 額前葉腦白質切離術 |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-121 | TIPS | わしんとんじょうやく | 華盛頓公約 |  | KEEP_LOCK | MEDIUM |  |
| TIP-122 | TIPS | えーてぃーえふ | ATF |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-123 | TIPS | しーあいえー | ＣＩＡ |  | KEEP_LOCK | MEDIUM |  |
| TIP-124 | TIPS | でぃーめーる | D-Mail |  | KEEP_LOCK | MEDIUM |  |
| TIP-125 | TIPS | どきゅん | ＤＱＮ |  | KEEP_LOCK | MEDIUM |  |
| TIP-126 | TIPS | えふいーたうんず | ＦＥ－ＴＯＷＮＳ |  | KEEP_LOCK | MEDIUM |  |
| TIP-127 | TIPS | じーえす | ＧＳ |  | KEEP_LOCK | MEDIUM |  |
| TIP-128 | TIPS | きたこれ | 來啦 |  | ELITE_OFFICIAL_LOCK | HIGH |  |
| TIP-129 | TIPS | えむしーすりーせぶん | ＭＣ－７７７ |  | KEEP_LOCK | MEDIUM |  |
| TIP-130 | TIPS | えむえむおーあーるぴーじー | MMORPG |  | KEEP_LOCK | MEDIUM |  |
| TIP-131 | TIPS | えぬえすえっくす | ＮＳＸ |  | KEEP_LOCK | MEDIUM |  |
| TIP-132 | TIPS | えぬぜっとはちまるしー | ＮＺ８０Ｃ |  | KEEP_LOCK | MEDIUM |  |
| TIP-133 | TIPS | ぴーえっくすななじゅうはち | ＰＸ－７８ |  | KEEP_LOCK | MEDIUM |  |
| TIP-134 | TIPS | ゆーぴーえっくす | UPX | ＵＰＸ | ELITE_OFFICIAL_LOCK | HIGH | Normalize the localized output to ASCII UPX. Fullwidth ＵＰＸ is retained only as an alias/source-form reference. |
| TIP-135 | TIPS | わらい | w | ｗ | ELITE_OFFICIAL_LOCK | HIGH | Normalize the localized internet-laughter marker to ASCII w. Fullwidth ｗ is an alias/source-form reference. |
| TIP-136 | TIPS | あっとちゃんねる | @ch | @channel / ＠ｃｈａｎｎｅｌ / ＠ch | ELITE_OFFICIAL_LOCK | HIGH | @ch is the fictional board name itself. Do not describe it as merely an abbreviation of @channel. |
| CORE-001 | CORE | 岡部倫太郎 | 岡部倫太郎 |  | CORE_LOCK | HIGH |  |
| CORE-002 | CORE | 牧瀬紅莉栖 | 牧瀨紅莉栖 |  | CORE_LOCK | HIGH |  |
| CORE-003 | CORE | 椎名まゆり | 椎名真由理 |  | HISTORICAL_VARIANT_LOCK | HIGH |  |
| CORE-004 | CORE | 橋田至 | 橋田至 |  | CORE_LOCK | HIGH |  |
| CORE-005 | CORE | 阿万音鈴羽 | 阿萬音鈴羽 |  | CORE_LOCK | HIGH |  |
| CORE-006 | CORE | 桐生萌郁 | 桐生萌郁 |  | CORE_LOCK | HIGH |  |
| CORE-007 | CORE | 漆原るか | 漆原琉華 |  | CORE_LOCK | HIGH |  |
| CORE-008 | CORE | フェイリス・ニャンニャン | 菲伊麗絲‧喵喵 |  | CORE_LOCK | HIGH |  |
| CORE-009 | CORE | 天王寺裕吾 | 天王寺裕吾 |  | CORE_LOCK | HIGH |  |
| CORE-010 | CORE | 天王寺綯 | 天王寺綯 |  | CORE_LOCK | HIGH |  |
| CORE-011 | CORE | ドクター中鉢 | 中鉢博士 |  | CORE_LOCK | HIGH |  |
| CORE-012 | CORE | ジョン・タイター | 約翰・提托 | John Titor | ELITE_OFFICIAL_LOCK | HIGH | Use 約翰・提托 as the primary Traditional Chinese character name in ordinary/core scope. `John Titor` is an allowed Latin-script alias/reference form, not a mandatory replacement. |
| CORE-013 | CORE | メタルうーぱ | 金屬烏帕 |  | CORE_LOCK | HIGH |  |
| CORE-014 | CORE | ダイバージェンスメーター | 世界線變動率探測儀 | Divergence Meter / 變動率探測儀 | CORE_LOCK | MEDIUM |  |
| CORE-015 | CORE | IBN5100 | IBN5100 |  | CORE_LOCK | HIGH |  |
| CORE-016 | CORE | SERN | SERN |  | CORE_LOCK | HIGH |  |
| CORE-017 | CORE | ラウンダー | Rounder | 巡行者 / SERN 執行部隊 | CORE_LOCK | MEDIUM |  |
| CORE-018 | CORE | コミックマーケット | Comic Market |  | CORE_LOCK | HIGH | Formal event name コミックマーケット. Do not conflate with the separate parody/TIPS term COMIMA (TIP-026). |
| CORE-019 | CORE | 秋葉原ラジオ会館 | 秋葉原無線電會館 |  | CORE_LOCK | HIGH |  |
| CORE-020 | CORE | Dメール | D-Mail |  | CORE_LOCK | HIGH |  |
| CORE-021 | CORE | タイムリープマシン | 時間跳躍機 |  | CORE_LOCK | HIGH |  |
| CORE-022 | CORE | リフター | 升力器 |  | CORE_LOCK | HIGH |  |
| CORE-023 | CORE | ECHELON | 梯隊系統 |  | CORE_LOCK | HIGH |  |
| CORE-024 | CORE | 電話レンジ（仮） | 電話微波爐（暫定） |  | CORE_LOCK | HIGH | Applies when the Japanese source explicitly contains 電話レンジ（仮）. Do not add the provisional qualifier to a deliberately bare 電話レンジ occurrence. |
| CORE-025 | CORE | リーディング・シュタイナー | 命運探知之魔眼 |  | CORE_LOCK | HIGH |  |
| CORE-026 | CORE | 雷ネット翔 | 雷網路翔 |  | CORE_LOCK | HIGH | Core/base localization of 雷ネット翔. TIPS AccessNo titles are separately frozen as TIP-100–TIP-113. |
| CORE-027 | CORE | Jellyman's Report | Jellyman's Report | 膠化人報告 / Jellyman | CORE_LOCK | MEDIUM |  |
| CORE-028 | CORE | アトラクタフィールド | 世界線收束範圍 |  | CORE_LOCK | HIGH |  |
| CORE-029 | CORE | オペレーション・スクルド | 掌管未來的女神作戰 |  | CORE_LOCK | HIGH |  |
| CORE-030 | CORE | FB | FB |  | CORE_LOCK | HIGH |  |
| CORE-031 | CORE | 未来ガジェット | 未來工具 | Future Gadget | CORE_LOCK | HIGH | Future Gadget base term. Use 未來工具 for the identified concept, not the stale 未來道具 form. |
| CORE-032 | CORE | 未来ガジェット研究所 | 未來工具研究所 | Future Gadget Laboratory | CORE_LOCK | HIGH | Future Gadget Laboratory organization name; keep the full organization form 未來工具研究所. |
| CORE-033 | CORE | オペレーション・シェヴン | Operation Sjöfn |  | CORE_LOCK | HIGH | Narrative/ruby operation-name form. When JP presents the ruby/base pair `愛を司る女神` + `作戦` / `オペレーション・シェヴン`, preserve the localized base title and render the visible ruby/codename as `Operation Sjöfn` in parentheses immediately after the base title. Use one U+0020 space; no U+30FB middle dot; halfwidth Latin; NFC U+00F6. Do not replace the base title with the codename. Do not extend TIP-035 primary `修芬` into prose by default. |
| CORE-034 | CORE | サンボ | 桑博 |  | CORE_LOCK | HIGH | Akihabara shop proper-name concept. Authority: `MANUAL_PRODUCT_DECISION + JP_SOURCE`. Official-EN `Sanbo` / `Sambo` inconsistency is not normative for TC. Use `桑博` for the exact proper-name concept; do not import `牛肉飯店` into the name unless the local JP independently supplies a generic shop description. |

## Scope-conflict reminder

- `TIP-040` and `CORE-012` both use the primary Traditional Chinese form `約翰・提托`. `John Titor` remains an allowed Latin-script alias/reference form where the source or presentation specifically calls for it.
- `TIP-088` is the TIPS-title form `B.B.Call`; ordinary `ポケベル` dialogue/prose is not automatically this title.
- `電話レンジ（仮）` includes the provisional qualifier. A bare `電話レンジ` occurrence must be judged from the source rather than normalized by substring.
- `TIP-035` remains the TIPS primary form `修芬`; `CORE-033` separately fixes the narrative/ruby codename surface as `Operation Sjöfn` only where that JP operation-name layer is present.
