---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Git Diff-Tree 指南
translated: true
type: note
---

這是一份實用的 `git diff-tree` 端到端指南——包括它的作用、使用時機，以及實際工作中真正會用到的選項。我將避免使用大型表格，專注於提供可直接複製貼上的範例說明。

# `git diff-tree` 的實際功能

* 它比較**樹物件**。在日常使用中，通常意味著：「顯示**提交**與其父提交相比的變更內容。」
* 它屬於**底層指令**（適合腳本使用），與 `git show`/`git log` 這類面向用戶的指令不同。
* 它絕不會檢查你的工作目錄；只比較儲存在版本庫中的樹物件（提交、指向提交的標籤，或原始樹 ID）。

# 你會用到的基本形式

1. 將提交與其父提交進行比較

```bash
git diff-tree -p <commit>
```

如果 `<commit>` 有一個父提交，你會看到正常的修補檔。如果是合併提交，除非你特別要求（見下文），否則不會顯示任何內容。

2. 明確比較兩個樹物件/提交

```bash
git diff-tree -p <old-tree-or-commit> <new-tree-or-commit>
```

當你想比較任意兩個時間點，而不僅僅是「提交與父提交」時非常有用。

3. 僅顯示檔案名稱（無修補檔）

```bash
git diff-tree --name-only -r <commit>
```

加上 `-r` 以遞迴進入子目錄，這樣你會得到一個扁平化的列表。

4. 顯示帶有變更類型的名稱

```bash
git diff-tree --name-status -r <commit>
# 輸出類似以下的行：
# A path/to/newfile
# M path/to/modified
# D path/to/deleted
```

5. 顯示修補檔（完整差異）

```bash
git diff-tree -p <commit>            # 統一差異格式，類似 `git show`
git diff-tree -U1 -p <commit>        # 較少的上下文（1 行）
```

# 必須了解的選項（含原因與時機）

* `-r` — 遞迴進入子樹，以便查看所有嵌套路徑。沒有此選項時，變更的目錄可能只顯示為單一行。
* `--no-commit-id` — 在為每個提交輸出編寫腳本時，抑制「commit <sha>」標頭。
* `--root` — 當提交**沒有父提交**（初始提交）時，仍然顯示其與空樹的差異。
* `-m` — 對於合併提交，顯示**與每個父提交的差異**（產生多個差異）。
* `-c` / `--cc` — 合併提交的組合差異。`--cc` 是更精煉的視圖（`git show` 用於合併提交的方式）。
* `--name-only` / `--name-status` / `--stat` / `--numstat` — 不同的摘要樣式。`--numstat` 對腳本友好（新增/刪除的行數統計）。
* `--diff-filter=<set>` — 按變更類型篩選，例如 `--diff-filter=AM`（僅新增或修改）；常見字母：`A`dd（新增）、`M`odified（修改）、`D`eleted（刪除）、`R`enamed（重新命名）、`C`opied（複製）、`T`ype changed（類型變更）。
* `-M` / `-C` — 檢測重新命名和複製。可加上相似度閾值，例如 `-M90%`。
* `--relative[=<path>]` — 將輸出限制在子目錄內；沒有參數時，使用當前工作目錄。
* `-z` — 使用 **NUL 終止符**處理路徑，以便機器明確解析（處理檔案名稱中的換行符或製表符）。
* `--stdin` — 從標準輸入讀取提交（或配對）列表。這是實現快速批次操作的秘訣。

# 標準的腳本模式

### 1) 列出單一提交中變更的檔案

```bash
git diff-tree --no-commit-id --name-status -r <commit>
```

### 2) 批次處理多個提交（快速！）

```bash
git rev-list main --since="2025-08-01" |
  git diff-tree --stdin -r --no-commit-id --name-status
```

`--stdin` 避免了為每個提交生成 `git` 程序，對於大範圍的提交來說速度更快。

### 3) 僅顯示目錄中的新增和修改

```bash
git diff-tree -r --no-commit-id --name-status \
  --diff-filter=AM <commit> -- src/backend/
```

### 4) 計算每個檔案新增/刪除的行數（對腳本友好）

```bash
git diff-tree -r --no-commit-id --numstat <commit>
# 輸出："<added>\t<deleted>\t<path>"
```

### 5) 檢測並顯示提交中的重新命名

```bash
git diff-tree -r --no-commit-id -M --name-status <commit>
# 輸出類似："R100 old/name.txt\tnew/name.txt"
```

### 6) 合併提交的修補檔

```bash
git diff-tree -m -p <merge-commit>     # 每個父提交的修補檔
git diff-tree --cc <merge-commit>      # 組合視圖（單一修補檔）
```

### 7) 初始提交（無父提交）

```bash
git diff-tree --root -p <initial-commit>
```

# 理解原始記錄格式（如果你手動解析）

使用 `--raw`（某些模式隱含使用）來獲取最小化且穩定的記錄：

```
:100644 100644 <oldsha> <newsha> M<TAB>path
```

* 數字是檔案模式：`100644` 常規檔案，`100755` 可執行檔案，`120000` 符號連結，`160000` gitlink（子模組）。
* 狀態是單一字母（`A`、`M`、`D` 等），可能帶有分數（例如 `R100`）。
* 對於重新命名/複製，你會看到兩個路徑。使用 `-z` 時，欄位以 NUL 分隔；沒有 `-z` 時，則以製表符分隔。

**提示：** 如果你正在建構可靠的工具，請始終使用 `-z` 並以 NUL 分割。存在包含換行符的檔案名稱。

# 比較 `git diff-tree` 與相關指令（以便選擇正確的工具）

* `git diff`：比較**索引/工作樹**與 HEAD 或任意兩個提交/樹物件；用於互動式開發。
* `git show <commit>`：一個漂亮的包裝器，用於「與父提交的差異 + 元數據」。非常適合人類閱讀。
* `git log -p`：歷史記錄加上修補檔。對於範圍比較，通常比手動循環 `diff-tree` 更方便。
* `git diff-tree`：底層指令，用於**精確、可編寫腳本的每個提交差異**，並可透過 `--stdin` 進行批次處理。

# 真實世界範例

### 「這個 PR 合併提交中變更了什麼？」

```bash
git diff-tree --cc <merge-commit> | less
```

如果需要按父提交查看詳細資訊：

```bash
git diff-tree -m -p <merge-commit> | less
```

### 「將最新提交修改的檔案清單提供給 CI 步驟」

```bash
git diff-tree --no-commit-id --name-only -r HEAD > changed.txt
```

### 「最近 20 個提交中僅新增或修改的 Java 檔案」

```bash
git rev-list -n 20 HEAD |
  git diff-tree --stdin -r --no-commit-id --name-only --diff-filter=AM |
  grep -E '\.java$'
```

### 「總結發布標籤間的程式碼變動（新增/刪除的行數）」

```bash
git diff-tree -r --no-commit-id --numstat v1.2.0..v1.3.0
```

### 「安全處理奇怪的檔案名稱」

```bash
git diff-tree -z -r --no-commit-id --name-status <commit> |
  awk -v RS='\0' 'NR%2{status=$0; next}{printf "%s %s\n", status, $0}'
```

# 效能注意事項

* 對於大範圍的提交，優先使用 `--stdin` 與 `git rev-list`；這可以避免程序頻繁創建。
* 當你不需要行級變更時，跳過修補檔（使用 `--name-only`/`--name-status`）。
* 如果你重視速度勝過準確性，請避免使用重新命名檢測（`-M`、`-C`）。

# 陷阱與邊緣情況

* **合併提交預設無輸出。** 你必須傳遞 `-m`（按父提交）或 `--cc`/`-c`（組合視圖）。
* **初始提交是「空樹與樹的比較」。** 使用 `--root` 來強制顯示差異。
* **子模組** 顯示模式 `160000` 和一個 SHA（gitlink）。除非你在子模組版本庫內部進行比較，否則不會看到內部差異。
* **路徑規格放在 `--` 之後。** 如果你按路徑篩選，請將它們放在 `--` 之後以避免歧義。
* **包含空白字元/換行符的檔案名稱。** 如果你正在解析，請務必加上 `-z`。

# 實際可重用的快速「備忘片段」

```bash
# 變更的檔案（扁平列表）
git diff-tree --no-commit-id --name-only -r <commit>
```