---
audio: false
generated: true
lang: hant
layout: post
title: 分叉的 Git 分支
translated: true
---

當你的本地 `main` 分支和遠端的 `origin/main` 分支在 Git 中分歧時—分別有 74 和 70 個不同的提交—這意味著它們共享一個共同的祖先，但自那以後已經發展出獨特的提交。你的目標是使你的本地 `main` 分支與 `origin/main` 相匹配，通過將你的本地分支重置到共同祖先（即「雙方的父親」）然後使用 `git pull` 來引入遠端變更，有效地丟棄你的本地分歧提交，以遠端的為主。以下是實現這一目標的步驟。

### 修復分歧的步驟

1. **獲取最新的遠端變更**
   首先，確保你的本地存儲庫有最新的遠端信息。這將更新你對 `origin/main` 的參考，而不會立即改變你的本地 `main` 分支。

   ```bash
   git fetch origin
   ```

2. **找到共同祖先提交**
   使用 `git merge-base` 來識別本地 `main` 和 `origin/main` 之間的共同祖先提交。這是分支分歧的點。

   ```bash
   ancestor=$(git merge-base main origin/main)
   ```

   這個命令將共同祖先的提交哈希存儲在變量 `ancestor` 中。

3. **將本地 `main` 重置到共同祖先**
   將你的本地 `main` 分支重置到共同祖先提交。`--hard` 選項確保分支指針和你的工作目錄都會更新，丟棄所有本地提交和變更。

   ```bash
   git reset --hard $ancestor
   ```

   **注意**：這一步將丟棄工作目錄和暫存區中的所有未提交變更，以及本地 `main` 的 74 個獨特提交。如果需要保留這些，請考慮先創建一個備份分支（見「可選備份」）。

4. **拉取遠端變更**
   現在，從 `origin/main` 拉取變更。由於你的本地 `main` 現在在共同祖先，而 `origin/main` 領先 70 個提交，這將快進你的本地 `main` 以匹配 `origin/main`。

   ```bash
   git pull origin main
   ```

   完成後，你的本地 `main` 分支將與 `origin/main` 完全相同，所有本地分歧提交都被丟棄。

### 完整命令序列

這是要執行的完整命令序列：

```bash
git fetch origin
ancestor=$(git merge-base main origin/main)
git reset --hard $ancestor
git pull origin main
```

### 發生了什麼？
- **步驟 1 後**：你的本地存儲庫知道 `origin/main` 的最新狀態。
- **步驟 2 後**：你已經識別了共同祖先提交（例如，哈希值 `abc123`）。
- **步驟 3 後**：你的本地 `main` 重置到 `abc123`，丟失了 74 個獨特的本地提交。
- **步驟 4 後**：`git pull` 快進 `main` 到 `origin/main`，引入了 70 個遠端分支的提交。

結果是你的本地 `main` 完全匹配 `origin/main`，實現了使用遠端分支的目標。

### 可選備份
如果你不確定是否要丟棄本地提交並希望保留它們以便日後使用，請在重置之前創建一個備份分支：

```bash
git branch backup-main
```

在 `git reset` 命令之前運行這個命令。你的 74 個本地提交將保留在 `backup-main` 上，你可以日後隨時查看它們。

### 重要說明
- **未提交變更**：如果你有未提交的變更（在工作目錄或暫存區中），並且希望保留它們，請在重置之前將它們暫存：
  ```bash
  git stash
  ```
  完成過程後，你可以使用 `git stash pop` 來檢索它們。
- **為什麼這樣有效**：重置到共同祖先並拉取確保了對 `origin/main` 的清潔快進，避免了直接拉取時可能出現的分歧分支的合併衝突。

按照這些步驟，你將成功地將本地 `main` 重置為與 `origin/main` 相匹配。