---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 使用 Subl 命令行工具
translated: true
type: note
---

### 在 Sublime Text 中使用 `subl` 指令

好消息——你的 `subl` 命令行工具已經安裝完成並可正常運作（從 `--help` 的輸出內容可見）！這是 Sublime Text 建置版 4200（最新版本），而 `subl` 正是用於開啟檔案、目錄等功能的官方命令行介面。對開發者和進階使用者來說，它的功能極為多樣化。

我將透過實際範例為你詳細解說。請在終端機的任何目錄下執行這些指令。核心語法如下：
```
subl [參數] [檔案或目錄]
```

#### 1. **基礎用法：開啟檔案或目錄**
- **開啟當前目錄**（將其作為專案/資料夾載入 Sublime）：
  ```
  subl .
  ```
  - 此指令會開啟新視窗並顯示當前資料夾的內容。

- **開啟特定檔案**：
  ```
  subl myfile.txt
  ```
  - 在預設視窗（或依需求在新視窗）中開啟 `myfile.txt`。

- **開啟多個檔案/目錄**：
  ```
  subl file1.txt file2.js ~/Documents/myproject/
  ```
  - 在 Sublime 中開啟所有指定項目。

- **在指定行/列開啟**（適用於快速跳轉至錯誤位置）：
  ```
  subl myfile.py:42          # 在第 42 行開啟
  subl myfile.py:42:5        # 在第 42 行第 5 列開啟
  ```

#### 2. **常用參數（取自說明文件）**
以下是最實用的標記搭配使用範例。可根據需求組合使用（例如 `subl -n file.txt`）。

- **`-n` 或 `--new-window`**：始終在新視窗中開啟。
  ```
  subl -n myfile.txt
  ```
  - 當你需要與現有的 Sublime 工作階段分開時非常實用。

- **`-a` 或 `--add`**：將檔案/資料夾加入*當前*已開啟的 Sublime 視窗。
  ```
  subl -a newfolder/
  ```
  - 不會建立新視窗——非常適合用於建構工作區。

- **`-w` 或 `--wait`**：等待使用者在 Sublime 中關閉檔案後，終端機指令才會完成執行。
  ```
  subl -w myfile.txt
  ```
  - 適用於腳本情境（例如在建置完成後開啟檔案並等待檢閱）。從標準輸入讀取時會自動啟用此功能。

- **`-b` 或 `--background`**：開啟時不將 Sublime 切換至前景（保持終端機焦點）。
  ```
  subl -b myfile.txt
  ```

- **`-s` 或 `--stay`**：關閉檔案後保持 Sublime 處於焦點狀態（僅在搭配 `-w` 時相關）。
  ```
  subl -w -s myfile.txt
  ```
  - 避免自動切換回終端機。

- **`--project <project>`**：開啟特定的 Sublime 專案檔案（`.sublime-project`）。
  ```
  subl --project MyProject.sublime-project
  ```
  - 專案可儲存工作區、設定等內容。可透過 Sublime 的 File > Save Project 建立專案。

- **`--command <command>`**：執行 Sublime 指令（例如外掛動作）而不開啟檔案。
  ```
  subl --command "build"    # 若已設定建置系統，則觸發建置指令
  ```
  - 可透過 Sublime 主控台（View > Show Console）查看可用指令。

- **`--launch-or-new-window`**：僅在 Sublime 未執行時才開啟新視窗。
  ```
  subl --launch-or-new-window .
  ```
  - 能有效率地進行快速檢視，避免畫面雜亂。

- **標準輸入支援**（編輯管線輸入內容）：
  ```
  echo "Hello World" | subl -   # 在 Sublime 中開啟標準輸入以供編輯
  subl - > output.txt          # 編輯標準輸入並將變更儲存至 output.txt
  ```
  - 在 Sublime 中編輯後，儲存並關閉即可繼續。

- **`--safe-mode`**：在無外掛或自訂設定的模式下啟動 Sublime（用於疑難排解）。
  ```
  subl --safe-mode myfile.txt
  ```

- **其他標記**：
  - `-h` 或 `--help`：顯示你已查看過的說明內容。
  - `-v` 或 `--version`：顯示版本資訊（例如 `subl -v`）。

#### 3. **日常使用技巧**
- **檔名以 `-` 開頭**：若檔名形似參數標記（例如 `-config`），可使用 `--` 進行區隔：
  ```
  subl -- -config.json
  ```
- **建立便利的別名**：在 shell 設定檔中（zsh 為 `~/.zshrc`，bash 為 `~/.bash_profile`）加入捷徑：
  ```
  alias st='subl'     # 更簡短的別名
  alias stt='subl -n' # 用於新分頁/視窗
  ```
  執行 `source ~/.zshrc` 重新載入設定。
- **在腳本/GIT 中應用**：可在掛鉤或別名中使用，例如透過 `git diff | subl -` 檢視變更內容。
- **與 `open` 指令比較**：既然已設定好 `subl`，它比 `open -a "Sublime Text"` 更優越，因為支援行號定位、專案開啟等進階功能。
- **疑難排解**：
  - 若 `subl` 無法運作，請重新執行我之前回覆中提到的符號連結安裝步驟。
  - 處理大型專案時，建議使用 `-a` 參數避免開啟過多視窗。
  - 在 macOS 上若遇到焦點切換問題，可先嘗試不使用 `-b` 參數。

以上內容涵蓋了你所需功能的 90%！建議先在專案資料夾中嘗試 `subl .` 指令並多加實驗。如果你有特定工作流程或錯誤狀況，歡迎提供更多細節以獲得客製化建議。