---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 強制純代碼輸出方法
translated: true
type: note
---

明白了——你希望 Claude Code（以及你那些調用它的「路由」工作流程）只輸出**程式碼**，完全**不含內嵌註解、文件字串或解釋說明**。以下是三種可靠的實現方法，從最溫和到最嚴格。不用表格——直接列出步驟。

---

# 1) 將規則寫入 `CLAUDE.md`（全域或專案級）

Claude Code 會自動載入「記憶」檔案並在各工作階段中遵循。加入一條簡短明確的規則：

**全域（所有專案）：** `~/.claude/CLAUDE.md`  
**專案級（納入版本控制）：** `./CLAUDE.md`

```md
# 輸出規則
- 生成程式碼時，僅輸出程式碼本身。
- 除非我明確要求，否則不要包含內嵌註解、區塊註解、文件字串或解釋性文字。
- 保持訊息簡潔；若需解釋，請放在程式碼區塊之後，且僅在我要求時才這麼做。
```

提示：你可以透過 `/memory` 管理這些記憶檔案，或在 Claude Code 中透過以 `#` 開頭的訊息快速新增。（[Anthropic][1]）

---

# 2) 建立**自訂輸出樣式**以禁止註解（較強制）

輸出樣式會修改 Claude Code 的**系統提示**。建立一個並切換至該樣式：

**建立：**

```
/output-style:new 我需要一個輸出樣式，總是輸出不含任何註解或文件字串的程式碼，且不加解釋。
```

這會在 `~/.claude/output-styles/…` 下建立一個檔案。你可以編輯它以確保規則明確無誤：

```md
---
name: 僅程式碼（無註解）
description: 總是輸出不含註解/文件字串的程式碼；除非被要求，否則不加解釋。
---
# 指示
- 你正處於「僅程式碼」模式。
- 絕不包含內嵌註解、區塊註解或文件字串。
- 除非明確要求，否則不要在程式碼前後添加說明文字。

## 具體行為
- 若任務暗示需要測試，僅輸出測試檔案的程式碼。
- 若需要澄清，請簡要提問，無需解釋。
```

**啟用：**

```
/output-style "僅程式碼（無註解）"
```

（輸出樣式會直接改變系統提示；你可隨時使用 `/output-style` 切換。）（[Anthropic][2]）

---

# 3) 在執行時附加額外系統提示（最強制／每工作階段）

若你從 CLI 或指令碼啟動 Claude Code，請加入：

```bash
claude --append-system-prompt "總是僅輸出程式碼。無內嵌註解、無區塊註解、無文件字串、無解釋說明，除非明確要求。"
```

你也可以透過 `/config` 設定此選項，若你偏好持續性的專案設定。（Anthropic 指出你可以使用 `--append-system-prompt` 來修改 Claude Code 的行為。）（[Anthropic][3]）

---

## 應在何處設定「路由」層級的規則

* 若你的「Claude Code 路由」僅是你在各代碼庫中的常規 Claude Code 工作階段，建議使用**全域記憶**（`~/.claude/CLAUDE.md`）或**自訂輸出樣式**，讓規則隨處生效。（[Anthropic][1]）
* 若你透過指令碼啟動，請內建 `--append-system-prompt` 參數，讓每次執行都繼承該規則。（[Anthropic][3]）

---

## 額外防護措施（可選但實用）

* 在專案記憶中，加入**「違規處理」**條款，讓模型自我檢查：「若你即將輸出註解/文件字串，請停止並移除它們。」
* 若你有時*需要*註解，可在提示中加入一次性覆寫指令：「這次請包含簡短註解。」

就這樣。如果你告訴我你如何啟動 Claude Code（桌面端、VS Code、JetBrains 或終端機），我可以提供對應的現成程式碼片段。

[1]: https://docs.anthropic.com/en/docs/claude-code/memory "Manage Claude's memory - Anthropic"
[2]: https://docs.anthropic.com/en/docs/claude-code/output-styles "Output styles - Anthropic"
[3]: https://docs.anthropic.com/en/docs/claude-code/settings "Claude Code settings - Anthropic"