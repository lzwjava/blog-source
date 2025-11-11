---
audio: false
generated: true
lang: hant
layout: post
title: 分歧的 Git 分支
translated: true
type: note
---

當你的本地 `main` 分支與遠端 `origin/main` 分支在 Git 中出現分歧——分別有 74 和 70 個不同的提交時，這表示它們共享一個共同祖先，但之後各自發展出獨特的提交記錄。你的目標是透過將本地分支重置到共同祖先（即「雙方的父節點」），然後使用 `git pull` 引入遠端變更，使你的本地 `main` 分支與 `origin/main` 一致，從而有效捨棄本地分歧的提交，改用遠端版本。以下是實現此目標的步驟。

### 修復分支分歧的步驟

1. **獲取最新的遠端變更**  
   首先確保你的本地儲存庫擁有來自遠端的最新資訊。這會更新你對 `origin/main` 的參考，但尚未更改你的本地 `main` 分支。

   ```bash
   git fetch origin
   ```

2. **尋找共同祖先提交**  
   使用 `git merge-base` 識別你的本地 `main` 與 `origin/main` 之間的共同祖先提交。這是分支開始分歧的節點。

   ```bash
   ancestor=$(git merge-base main origin/main)
   ```

   此命令會將共同祖先的提交雜湊值儲存在變數 `ancestor` 中。

3. **將本地 `main` 重置至共同祖先**  
   將你的本地 `main` 分支重置到共同祖先提交。`--hard` 選項會確保分支指標與你的工作目錄都更新，捨棄此點之後的所有本地提交與變更。

   ```bash
   git reset --hard $ancestor
   ```

   **注意**：此步驟將捨棄工作目錄與暫存區中所有未提交的變更，以及你的本地 `main` 分支中 74 個獨特的提交。若需保留這些內容，請先考慮建立備份分支（參閱下方的「可選備份」）。

4. **拉取遠端變更**  
   現在從 `origin/main` 拉取變更。由於你的本地 `main` 目前位於共同祖先，而 `origin/main` 領先 70 個提交，這將使你的本地 `main` 快轉至與 `origin/main` 一致。

   ```bash
   git pull origin main
   ```

   完成後，你的本地 `main` 分支將與 `origin/main` 完全相同，所有本地分歧的提交皆已捨棄。

### 完整命令序列

以下是需執行的完整命令序列：

```bash
git fetch origin
ancestor=$(git merge-base main origin/main)
git reset --hard $ancestor
git pull origin main
```

### 發生什麼事？
- **步驟 1 之後**：你的本地儲存庫知悉 `origin/main` 的最新狀態。
- **步驟 2 之後**：你已識別出共同祖先提交（例如雜湊值如 `abc123`）。
- **步驟 3 之後**：你的本地 `main` 被重置至 `abc123`，失去 74 個獨特的本地提交。
- **步驟 4 之後**：`git pull` 將 `main` 快轉至 `origin/main`，引入遠端分支的 70 個提交。

結果是你的本地 `main` 與 `origin/main` 完全一致，達成使用遠端分支的目標。

### 可選備份
如果你不確定是否要捨棄本地提交，並希望稍後保留它們，請在重置前建立備份分支：

```bash
git branch backup-main
```

在執行 `git reset` 命令前運行此指令。你的 74 個本地提交將保留在 `backup-main` 上，之後如有需要可重新檢視。

### 重要注意事項
- **未提交的變更**：如果你有未提交的變更（位於工作目錄或暫存區）且希望保留，請在重置前儲存它們：
  ```bash
  git stash
  ```
  完成流程後，你可使用 `git stash pop` 取回它們。
- **為何此方法有效**：重置至共同祖先並拉取變更，可確保乾淨地快轉至 `origin/main`，避免直接拉取分歧分支時可能產生的合併衝突。

遵循這些步驟，你將成功重置本地 `main` 分支以符合 `origin/main`，達成預期目標。