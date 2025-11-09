---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Git Check-Ignore 指令概覽
translated: true
type: note
---

### 什麼是 `git check-ignore`？

`git check-ignore` 指令是一個 Git 工具，用於判斷特定檔案或路徑是否被 Git 的忽略機制（例如 `.gitignore` 檔案、`.git/info/exclude` 或全域忽略檔案（透過 `core.excludesFile`）所忽略。它在除錯檔案為何未被追蹤或加入儲存庫時特別有用。

如果路徑被忽略，該指令會輸出該路徑（並可選擇性地輸出匹配模式）。如果未被忽略，則不會有任何輸出（退出代碼為 0）。這使得它在自動化腳本中非常方便使用。

### 基本用法

執行指令時可檢查一個或多個路徑：

```
git check-ignore <路徑名稱>...
```

- **範例**：檢查單一檔案是否被忽略：
  ```
  git check-ignore path/to/myfile.txt
  ```
  - 輸出：若被忽略，則顯示 `path/to/myfile.txt`。若未被忽略，則不顯示任何內容。

- **範例**：檢查多個檔案：
  ```
  git check-ignore file1.txt file2.txt dir/file3.txt
  ```
  - 僅輸出被忽略的路徑，每行一個。

### 主要選項

| 選項 | 描述 | 範例 |
|--------|-------------|---------|
| `-v`, `--verbose` | 顯示匹配的忽略模式（例如來自 `.gitignore` 的行）。 | `git check-ignore -v path/to/myfile.txt`<br>輸出：`path/to/myfile.txt: .gitignore:1:*.txt`（路徑 + 檔案:行數:模式） |
| `-q`, `--quiet` | 抑制輸出，但仍使用退出代碼（0 表示未被忽略，1 表示被忽略）。在腳本中很有用。 | `git check-ignore -q path/to/myfile.txt`<br>（無輸出；檢查 `$?` 以獲取退出代碼） |
| `--stdin` | 從標準輸入讀取路徑，而非從指令行讀取。 | `echo "file1.txt\nfile2.txt" \| git check-ignore --stdin` |
| `--non-matching` | 反轉輸出：顯示*未被*忽略的路徑。 | `git check-ignore --non-matching -v file1.txt file2.txt` |

### 常見使用情境

1. **除錯 `.gitignore` 規則**：
   - 如果 `git status` 未顯示你預期的檔案，請執行 `git check-ignore -v <檔案>` 以查看具體是哪條規則忽略了它。
   - 範例輸出：`src/logs/app.log: .gitignore:5:logs/*`（表示 `.gitignore` 第 5 行的規則匹配）。

2. **在腳本中使用**：
   - 檢查檔案是否應被加入：
     ```
     if git check-ignore -q myfile.txt; then
         echo "檔案被忽略，跳過..."
     else
         git add myfile.txt
     fi
     ```

3. **批次檢查**：
   - 列出目錄中所有被忽略的檔案：
     ```
     find . -type f -print0 | xargs -0 git check-ignore
     ```

### 提示
- 它遵循 Git 的忽略堆疊：本機 `.gitignore`、全域排除設定等。
- 適用於未追蹤的檔案或已在儲存庫中的檔案（但會根據忽略規則進行檢查）。
- 更多詳細資訊，請參閱官方文件。

[Git check-ignore 文件](https://git-scm.com/docs/git-check-ignore)  
[Stack Overflow：顯示哪些特定檔案被 gitignore 忽略的 Git 指令](https://stackoverflow.com/questions/466764/git-command-to-show-which-specific-files-are-ignored-by-gitignore)  
[使用 git check-ignore 除錯你的 .gitignore](https://alexwlchan.net/til/2020/using-git-check-ignore-to-debug-your-gitignore/)