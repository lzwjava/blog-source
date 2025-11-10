---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 使用 Git 模式暫存檔案
translated: true
type: note
---

### 在 Git 中使用模式暫存檔案

Git 的 `git add` 指令接受檔案路徑和萬用字元模式（如 `*.java`）來暫存符合條件的檔案。您可以執行多個 `git add` 指令來暫存不同的檔案集合，然後分別提交。這樣可以實現選擇性暫存，以便進行分組提交（例如，一個提交用於 Java 檔案，另一個用於其餘檔案）。

#### 基礎範例：先暫存並提交 Java 檔案
1. **暫存所有 .java 檔案**：
   ```bash
   git add "*.java"
   ```
   - 這會暫存當前目錄及子目錄中所有以 `.java` 結尾的未追蹤或已修改檔案。
   - 使用雙引號（`"`）可避免在許多系統（例如 Bash）上出現 shell 擴展問題。

2. **提交已暫存的 Java 檔案**：
   ```bash
   git commit -m "Add Java files"
   ```
   - 這僅提交已暫存的檔案（Java 檔案）。

3. **暫存其餘所有檔案**：
   ```bash
   git add .
   ```
   - 這會暫存所有剩餘的未追蹤/已修改檔案（包括當前目錄的內容）。

4. **提交其餘檔案**：
   ```bash
   git commit -m "Add other files"
   ```

- **注意事項**：
  - 在第一次提交後，`git add .` 不會重新暫存已提交的檔案；它僅影響未暫存的變更。
  - 在每次 `add` 後檢查 `git status` 以確認暫存內容。
  - 如果您有嵌套目錄，`*.java` 會捕獲任意深度的檔案。

#### 處理排除或更多模式
如果您想要在單一步驟中包含 `*.java` 但排除其他檔案，Git 的 `git add` 不支援直接否定模式，例如 `"!*.java"`。（您的範例語法 `"!*.java"` 在 Git 指令中無效。）相反，請使用多個 `git add` 呼叫，如上所述，或者：

- 使用特定路徑：`git add file1.txt file2.md` 進行手動選擇。
- 對於進階排除：暫時使用 `.gitignore` 隱藏檔案，添加您想要的內容，然後恢復 `.gitignore`。或者使用 `git add -A`（添加所有內容），但配合選擇性暫存。
- 互動式添加：`git add -p` 進行區塊逐塊暫存。
- 預覽變更：`git add --dry-run "*.java"` 顯示將要暫存的內容而不實際執行。

#### 分開提交的提示
- 在提交前始終使用 `git diff --cached` 進行審查。
- 對於較大的儲存庫，考慮使用 `git add --all` 或 `git add -A` 一次性暫存所有變更，然後如有需要，使用 `git reset HEAD <file>` 選擇性地取消暫存。
- 如果模式無效，請確保使用了引號且您的 shell 支援萬用字元（例如，在 Windows 中，使用 Git Bash）。對於大小寫不敏感，Git 尊重您的系統設定（請參閱 `core.ignorecase`）。

如果這不符合您的意圖（例如，如果您指的是像在 `.gitignore` 中的排除模式），請提供更多詳細資訊！