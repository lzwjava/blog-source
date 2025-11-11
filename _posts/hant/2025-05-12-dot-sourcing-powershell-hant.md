---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast:free
title: 點源 PowerShell 腳本
translated: true
type: note
---

### 在 .ps1 檔案中使用點源載入 PowerShell 函式

點源載入（使用 `.` 運算子）會將 PowerShell 指令碼（.ps1 檔案）載入當前工作階段的記憶體中，使其函式與變數可供使用，但不會執行指令碼的頂層程式碼。這對於匯入模組或可重複使用的程式碼非常實用。

#### 基本語法
在 PowerShell 工作階段中執行此命令：
```
. Path\To\YourScript.ps1
```
- 將 `Path\To\YourScript.ps1` 替換為實際檔案路徑（建議使用絕對路徑以確保可靠性）。
- 範例：`. C:\Scripts\MyFunctions.ps1` – 這會將該檔案中的函式載入到您的工作階段。

#### 運作原理
- 指令碼中定義的函式可在當前工作階段中呼叫。
- 變數也會被匯入，但僅限於非本地作用域的變數。
- 避免在生產環境指令碼中使用點源載入；建議使用模組以獲得更好的組織結構。
- 提示：若路徑包含空格，請用引號包圍：`. "C:\My Scripts\Functions.ps1"`

常見問題：若指令碼存在語法錯誤，點源載入將失敗並顯示錯誤訊息。可透過命令提示字元執行 `PowerShell -Command ". .\YourScript.ps1"` 進行測試。

### 使用 PowerShell 執行原則

執行原則是安全性設定，用於限制 PowerShell 可執行的指令碼，防止惡意程式碼執行。這些原則按作用域設定（例如：整個電腦、特定使用者）。

#### 檢查當前原則
在 PowerShell 中執行：
```
Get-ExecutionPolicy
```
- 輸出範例：`Restricted`（阻止所有指令碼）、`AllSigned`（僅允許已簽署的指令碼）、`RemoteSigned`（遠端指令碼需簽署，本地指令碼允許）、或 `Unrestricted`。

#### 設定或變更原則
使用 `Set-ExecutionPolicy`（變更電腦層級原則需要管理員權限）：
- 允許本地編寫的指令碼範例：`Set-ExecutionPolicy RemoteSigned`
- 強制執行且不顯示提示：`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force`
- 按作用域設定：`Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope CurrentUser`（僅影響當前使用者帳戶）。

#### 常見原則
- `Restricted`：預設值；不執行任何指令碼。
- `AllSigned`：要求數位簽章（安全但不便）。
- `RemoteSigned`：平衡安全性——允許本地指令碼，遠端指令碼需簽署。
- `Unrestricted`：執行所有指令碼（有風險；請謹慎使用）。
- `Bypass`：完全無限制，適用於自動化環境。

提示：原則僅適用於主控台工作階段，除非另行設定，否則不影響 ISE 或 VS Code。可透過執行範例指令碼（如 `Write-Host "Hello"`）測試變更。詳情請參閱 Microsoft 文件：`help about_Execution_Policies`。若處於企業環境中，群組原則可能會覆蓋本地設定。