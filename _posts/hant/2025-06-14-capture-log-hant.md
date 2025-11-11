---
audio: false
generated: true
lang: hant
layout: post
title: 擷取日誌
translated: true
type: note
---

在 GNOME Terminal 中，「全選」選項（通常透過 `編輯 > 全選` 或 `Ctrl+Shift+A` 存取）僅會選取目前螢幕上可見的文字。若要選取終端機中的**所有文字**（包括滾動緩衝區中超出可見範圍的內容），您可以使用以下其中一種方法：

### 方法 1：增加滾動緩衝區並手動選取
1. **確保啟用滾動緩衝區**：
   - 在 GNOME Terminal 中前往 `編輯 > 設定檔偏好設定`。
   - 在「滾動」標籤頁下，確保滾動緩衝區設定為較高數值或「無限制」，以擷取所有終端機輸出。
2. **手動選取**：
   - 使用滑鼠或 `Shift+Page Up` 滾動至終端機輸出的頂部。
   - 從頂部點擊並拖曳至底部，以手動選取所有文字。
   - 或者，使用 `Shift+Home` 跳至緩衝區開頭，然後點擊拖曳或使用 `Shift+End` 選取至結尾。

### 方法 2：使用指令擷取所有輸出
若想擷取所有終端機輸出（包括滾動緩衝區），您可以使用指令重新導向或複製輸出：
1. **重新導向輸出至檔案**：
   - 若知道產生輸出的指令，可透過重新導向重新執行：
     ```bash
     command > output.txt
     ```
     這會將所有輸出儲存至 `output.txt`，之後即可開啟並選取。
2. **使用 `script` 記錄終端機工作階段**：
   - 透過以下指令開始記錄工作階段：
     ```bash
     script output.log
     ```
   - 執行您的指令，然後輸入 `exit` 停止記錄。
   - 開啟 `output.log` 以選取所有文字。

### 方法 3：透過終端機指令複製滾動緩衝區
1. 使用 `tee` 指令或類似工具在執行指令時擷取輸出：
   ```bash
   command | tee output.txt
   ```
   這會在終端機顯示輸出並同時儲存至 `output.txt`。
2. 在文字編輯器中開啟檔案，即可輕鬆選取所有文字。

### 方法 4：使用 `tmux` 或 `screen` 進行進階控制
若經常需要擷取所有終端機輸出：
1. **安裝並使用 `tmux`**：
   - 安裝 `tmux`：
     ```bash
     sudo apt install tmux  # 在 Debian/Ubuntu 上
     ```
   - 啟動 `tmux` 工作階段：
     ```bash
     tmux
     ```
   - 執行您的指令。
   - 透過 `Ctrl+b, [` 進入滾動模式，然後按 `Ctrl+a, Ctrl+e` 選取緩衝區中的所有文字。
   - 透過 `Ctrl+b, ]` 複製（需先設定 `tmux` 啟用複製功能）。
2. **儲存 tmux 緩衝區**：
   - 將整個緩衝區儲存至檔案：
     ```bash
     tmux capture-pane -S - -E - -b 0 -J > output.txt
     ```
   - 開啟 `output.txt` 以選取所有文字。

### 限制
- GNOME Terminal 本身未提供透過 GUI「選取所有滾動緩衝區」的內建功能。
- 若未設定為無限制，滾動緩衝區大小可能會限制可用的文字量。
- 對於極大量的輸出，使用 `tmux`、`screen` 或重新導向至檔案會更可靠。

若需要進一步說明或協助特定指令，請告知！