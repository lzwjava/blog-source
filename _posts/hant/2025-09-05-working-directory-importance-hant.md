---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 工作目錄對編程代理的重要性
translated: true
type: note
---

沒錯——你的直覺是對的。

當你運行 **Claude Code**、**Codex** 或類似編碼代理時，工作目錄非常重要，因為：

### 1. 檔案操作的情境

如果你從父目錄運行代理，但實際程式碼位於子目錄內，你將需要不斷引用像 `subdir/foo.py` 這樣的路徑。這會造成額外負擔。直接在子目錄中運行意味著相對路徑（如 `./foo.py`）就能正常運作。

### 2. 依賴項解析

許多專案使用 `requirements.txt`、`pyproject.toml`、`package.json` 或 `pom.xml`，這些檔案假設**當前工作目錄**是專案根目錄。如果你從錯誤的目錄開始：

* Python/JavaScript 可能無法正確找到依賴項。
* 建置工具如 Maven/Gradle/NPM 可能會失敗。
* 你的虛擬環境可能無法正常啟動。

### 3. Git 與版本控制

Git 指令的行為會根據你所在的位置而有所不同：

* 在專案根目錄 → 按預期工作。
* 在子模組或嵌套目錄中 → 可能顯示不完整的歷史記錄或錯誤的儲存庫。

### 4. 配置與代理

Claude Code（以及 Codex、Copilot CLI 等）通常會讀取：

* `.env` 檔案
* `.gitignore`
* 專案配置（`.clauderc`、`.editorconfig` 等）

如果你不在預期的專案根目錄/子目錄中，代理可能無法讀取正確的設定。

---

✅ **最佳實踐：**

* 如果子目錄是一個**獨立專案**（有自己的 `package.json`、`pom.xml` 等），請在該目錄中運行代理。
* 如果它只是較大專案的一部分（如單一根目錄下的 `src/`），請從**根目錄**運行，以確保配置/依賴項保持一致。

需要我建議一個**工作流程設置**，讓你可以無縫地在子專案之間切換，而無需每次都手動 `cd` 嗎？