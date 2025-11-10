---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 在 VS Code 中排除忽略的檔案
translated: true
type: note
---

你可以透過調整 `settings.json` 中的三項設定，讓「前往檔案」（快速開啟，Ctrl + P）包含位於你的 `.gitignore` 中的檔案：

1. **讓搜尋忽略你的 `.gitignore` 規則**

   ```jsonc
   "search.useIgnoreFiles": false,      // 不遵循 .gitignore
   "search.useGlobalIgnoreFiles": false // 不遵循你的全域 gitignore
   ```
2. **確保你的排除模式不會隱藏那些檔案**
   預設情況下 VS Code 會將所有來自 `files.exclude` 的模式繼承到 `search.exclude` 中。如果你曾手動排除了 `.gitignore` 中的目錄，請重新啟用它們：

   ```jsonc
   "search.exclude": {
     "**/.git": false,          // 確實索引 .git（如需要）
     "**/.gitignore": false     // 絕對不要隱藏你的 .gitignore 檔案本身
     // …其他你想覆寫的模式
   }
   ```
3. **重新載入視窗**
   儲存你的使用者或工作區設定後，執行 **Developer: Reload Window**（⇧ ⌘ P → 「Reload Window」）讓檔案索引器讀取變更。

現在當你按下 Ctrl + P 時，就會看到*所有*的檔案名稱——無論是否被忽略。（[stackoverflow.com][1]）

[1]: https://stackoverflow.com/questions/62855190/how-do-you-include-git-ignored-files-in-vscode-quick-search?utm_source=chatgpt.com "How do you include git ignored files in VSCode quick search"