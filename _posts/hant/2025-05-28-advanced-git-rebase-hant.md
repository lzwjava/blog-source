---
audio: false
generated: true
lang: hant
layout: post
title: 高級 Git 教學：Rebase、Merge、衝突解決與 Squash
translated: true
type: note
---

本指南涵蓋了 `git rebase` 與 `git merge` 的進階用法、解決衝突、使用 `ours` 與 `theirs` 策略，以及壓縮提交。我將針對每個主題提供簡潔的說明與實用範例，重點放在進階工作流程，並假設您已熟悉基本的 Git 指令。

## 1. Git Merge：進階用法
`git merge` 將多個開發序列合併為一個統一的歷史記錄。進階用法包括處理複雜合併、使用合併策略以及管理合併提交。

### 主要合併策略
- **遞迴（預設）**：處理多個共同祖先，適用於大多數合併。
  - 範例：`git merge --strategy=recursive 分支名稱`
- **Ours**：保留目前分支的變更，捨棄合併分支的變更。
  - 範例：`git merge --strategy=ours 功能分支`
- **Theirs**：並非真正的策略，但可模擬實現（詳見下文衝突解決）。
- **Octopus**：同時合併多個分支（用於超過 2 個分支的情況）。
  - 範例：`git merge 分支1 分支2 分支3`

### 進階合併選項
- `--no-ff`：即使可以快轉，仍強制建立合併提交，以保留分支歷史。
  - 範例：`git merge --no-ff 功能分支`
- `--squash`：將合併分支的所有提交壓縮為目前分支上的一個提交。
  - 範例：`git merge --squash 功能分支 && git commit`
- `--allow-unrelated-histories`：合併沒有共同歷史記錄的分支。
  - 範例：`git merge --allow-unrelated-histories 外部儲存庫分支`

### 範例：使用無快轉合併
```bash
git checkout main
git merge --no-ff feature-branch
# 建立合併提交，保留功能分支的歷史記錄
```

## 2. Git Rebase：進階用法
`git rebase` 透過移動或修改提交來重寫歷史記錄，以建立線性歷史。它對於清理分支非常強大，但會改變歷史記錄，因此在共享分支上使用時需謹慎。

### 變基類型
- **標準變基**：將目前分支的提交重新應用到基礎分支上。
  - 範例：`git rebase main`（在 `feature-branch` 上執行）
- **互動式變基**：允許編輯、壓縮或重新排序提交。
  - 範例：`git rebase -i main`

### 互動式變基指令
執行 `git rebase -i <base>`（例如 `git rebase -i HEAD~3` 用於最後 3 個提交）。這將開啟編輯器，其中包含以下指令：
- `pick`：保留提交不變。
- `reword`：編輯提交訊息。
- `edit`：暫停變基以修改提交。
- `squash`：與前一個提交合併。
- `fixup`：類似 squash，但捨棄提交訊息。
- `drop`：移除提交。

### 範例：互動式變基
要壓縮最後 3 個提交：
```bash
git rebase -i HEAD~3
# 在編輯器中，將要合併的提交的 "pick" 改為 "squash" 或 "fixup"
# 儲存並退出以完成
```

### 變基到不同的基礎
要將分支移動到新的基礎（例如，將 `feature-branch` 從 `old-base` 移動到 `main`）：
```bash
git rebase --onto main old-base feature-branch
```

### 包含合併提交的變基
預設情況下，變基會扁平化合併提交。要保留它們：
```bash
git rebase -i --preserve-merges main
```

### 中止變基
如果出現問題：
```bash
git rebase --abort
```

## 3. 解決合併/變基衝突
當 Git 無法自動協調變更時，就會發生衝突。`merge` 和 `rebase` 都可能導致衝突，解決方式類似。

### 解決衝突的步驟
1. **識別衝突**：Git 暫停並列出衝突檔案。
   - 對於合併：`git status` 顯示有衝突的檔案。
   - 對於變基：在 `git rebase -i` 期間，逐個提交解決衝突。
2. **編輯衝突檔案**：開啟檔案並尋找衝突標記：
   ```text
   <<<<<<< HEAD
   您的變更
   =======
   傳入的變更
   >>>>>>> branch-name
   ```
   手動編輯以保留所需的變更，然後移除標記。
3. **標記為已解決**：
   - 對於合併：`git add <檔案>`
   - 對於變基：`git add <檔案>`，然後 `git rebase --continue`
4. **完成過程**：
   - 合併：`git commit`（Git 可能會自動產生提交訊息）。
   - 變基：`git rebase --continue` 直到所有提交都應用完畢。

### 範例：解決合併衝突
```bash
git checkout main
git merge feature-branch
# 發生衝突
git status  # 列出衝突檔案
# 編輯檔案以解決衝突
git add resolved-file.txt
git commit  # 完成合併
```

### 範例：解決變基衝突
```bash
git checkout feature-branch
git rebase main
# 發生衝突
# 編輯衝突檔案
git add resolved-file.txt
git rebase --continue
# 重複直到變基完成
```

## 4. 在衝突解決中使用 Ours 和 Theirs
在衝突期間，您可能希望偏袒某一方的變更（`ours` 或 `theirs`）。`ours` 和 `theirs` 的含義取決於操作類型。

### 合併：Ours 與 Theirs
- `ours`：來自目前分支的變更（例如 `main`）。
- `theirs`：來自被合併分支的變更（例如 `feature-branch`）。
- 使用 `--strategy-option`（`-X`）標記：
  - 保留 `ours`：`git merge -X ours feature-branch`
  - 保留 `theirs`：`git merge -X theirs feature-branch`

### 變基：Ours 與 Theirs
- `ours`：來自基礎分支的變更（例如 `main`）。
- `theirs`：來自被變基分支的變更（例如 `feature-branch`）。
- 在變基衝突解決期間使用：
  ```bash
  git checkout --ours file.txt  # 保留基礎分支的版本
  git checkout --theirs file.txt  # 保留被變基分支的版本
  git add file.txt
  git rebase --continue
  ```

### 範例：使用 Theirs 合併
要將 `feature-branch` 合併到 `main` 並偏袒 `feature-branch` 的變更：
```bash
git checkout main
git merge -X theirs feature-branch
```

### 範例：使用 Ours 變基
在將 `feature-branch` 變基到 `main` 時，透過保留 `main` 的版本解決衝突：
```bash
git checkout feature-branch
git rebase main
# 發生衝突
git checkout --ours file.txt
git add file.txt
git rebase --continue
```

## 5. 壓縮提交
壓縮將多個提交合併為一個，從而建立更整潔的歷史記錄。這通常透過互動式變基完成。

### 壓縮提交的步驟
1. 為所需的提交啟動互動式變基：
   ```bash
   git rebase -i HEAD~n  # n = 要壓縮的提交數量
   ```
2. 在編輯器中，將要合併到前一個提交的提交的 `pick` 更改為 `squash`（或 `fixup`）。
3. 儲存並退出。Git 可能會提示編輯合併後提交的訊息。
4. 推送更新後的歷史記錄（如果已共享，則強制推送）：
   ```bash
   git push --force-with-lease
   ```

### 範例：壓縮 3 個提交
```bash
git rebase -i HEAD~3
# 編輯器顯示：
# pick abc123 提交 1
# pick def456 提交 2
# pick ghi789 提交 3
# 更改為：
# pick abc123 提交 1
# squash def456 提交 2
# squash ghi789 提交 3
# 儲存並退出
# 如有提示，編輯合併後的提交訊息
git push --force-with-lease
```

### 在合併期間壓縮
要在合併期間壓縮分支的所有提交：
```bash
git checkout main
git merge --squash feature-branch
git commit  # 建立單一提交
```

## 最佳實踐與提示
- **變基前備份**：變基會重寫歷史記錄。建立備份分支：
  ```bash
  git branch backup-branch
  ```
- **避免對共享分支進行變基**：在公開分支上重寫歷史記錄可能會對協作者造成問題。請改用 `merge`。
- **為安全起見使用 `--force-with-lease`**：當推送重寫的歷史記錄時，這可以防止覆蓋他人的變更。
- **解決衝突後進行測試**：確保您的專案在解決衝突後能夠建置且測試通過。
- **使用工具解決衝突**：像 VS Code、SourceTree 或 `git mergetool` 這樣的 GUI 工具可以簡化衝突解決。
- **與團隊溝通**：如果在團隊中工作，請協調變基以避免衝突。

## 常見陷阱
- **在變基中遺失工作**：始終備份或使用 `git reflog` 來恢復遺失的提交。
- **誤用 Ours/Theirs**：在合併與變基情境中，仔細檢查哪個分支是 `ours` 與 `theirs`。
- **未經協調強制推送**：強制推送共享分支可能會干擾團隊成員。請使用 `--force-with-lease` 並進行溝通。

## 從錯誤中恢復
- **檢視歷史記錄**：使用 `git reflog` 查看先前的狀態並恢復遺失的提交：
  ```bash
  git reflog
  git checkout <提交雜湊值>
  ```
- **重設到合併前狀態**：
  ```bash
  git reset --hard HEAD^  # 復原最後一個合併提交
  ```
- **中止合併**：如果合併出錯：
  ```bash
  git merge --abort
  ```

本指南為進階 Git 工作流程提供了堅實的基礎。對於特定情境或錯誤，請告訴我，我可以深入探討或搜尋即時解決方案！