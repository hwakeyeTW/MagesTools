# MagesTools

This is an all-in-one toolset for the MAGES (aka 5pb.) visual novel engine.

Major functions:
- MPK unpacking / packing
- SCX string exporting / patching

## EasyPatcher（繁體中文）

此 fork 的 EasyPatcher 介面已在地化為台灣繁體中文，並加入 Steam 遊戲安裝路徑自動偵測。

啟動時會依序：
1. 檢查 `berd/meta.json` 的 `default_path`。
2. 從 Windows Registry 找出 Steam 安裝位置。
3. 讀取 `steamapps/libraryfolders.vdf`，掃描所有 Steam Library。
4. 若 `meta.json` 提供 `steam_app_id`，優先讀取對應的 `appmanifest_<appid>.acf`。
5. 若未提供 App ID，則使用 `default_path` 的最後一層資料夾名稱尋找遊戲。
6. 只接受內含 `USRDIR` 的目錄為有效遊戲路徑。

若只找到一個候選路徑，EasyPatcher 會自動填入；若找到多個且無法安全判定，會保留手動選擇，不會任意挑選。

`steam_app_id` 為選填欄位，舊版 `meta.json` 不需要修改即可繼續使用。例如：

```json
{
  "name": "Example Patch",
  "default_path": "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Example Game",
  "steam_app_id": "123456"
}
```
