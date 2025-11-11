---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 按作者壓縮 Git 提交記錄
translated: true
type: note
---

### 理解目標
Git 沒有內建的「按作者壓縮提交」指令，但你可以使用互動式 rebase 來手動分組並壓縮提交。這個方法的思路是：取最後 10 個提交（假設涉及 3 位不同的作者），將每位作者的提交合併為單一提交，最終得到 3 個提交。

此方法假設：
- 你位於包含這些提交的分支上（例如 main 或 feature 分支）。
- 提交是線性的（沒有合併提交）。
- 你預先知道作者是誰。

如果提交是非線性或結構複雜的，可能需要仔細處理以避免衝突。

### 按作者壓縮提交的步驟
1. **檢查最新的 10 個提交**  
   執行 `git log --oneline -10` 查看最後 10 個提交，包括其哈希值、作者和提交訊息。識別作者（例如，可透過 `git log --format="%an" -10 | sort | uniq` 列出不重複的作者）。

2. **開始互動式 Rebase**  
   找到第 10 個提交之前的提交。如果你的最新提交在 HEAD，且共有 10 個提交，則基準點為 `HEAD~10`。執行：  
   ```
   git rebase -i HEAD~10
   ```  
   這會開啟編輯器（預設為 vim），其中列出最後 10 個提交。內容類似：  
   ```
   pick abc123 Author A 的第一個提交  
   pick def456 Author A 的第二個提交  
   pick ghi789 Author B 的提交  
   pick jkl012 Author C 的提交  
   ...（更多提交）
   ```  
   - 每一行開頭都是 `pick`。

3. **標記要按作者壓縮的提交**  
   對於每位作者，將他們的所有提交（除了你希望保留的第一個提交外）的 `pick` 改為 `s`（squash）。決定：
   - 每位作者保留一個提交（選擇最早或最相關的提交作為基礎）。
   - 將該作者的其他提交改為 `s`，將其壓縮到基礎提交中。  
   範例（針對 3 位作者）：  
   ```
   pick abc123 Author A 的第一個提交（保留此提交）  
   s    def456 Author A 的第二個提交（壓縮到上一個提交中）  
   pick ghi789 Author B 的提交（保留此提交）  
   pick jkl012 Author C 的第一個提交（保留此提交）  
   s    mno345 Author C 的第二個提交（壓縮到上一個提交中）  
   ```  
   儲存並退出編輯器。這將開始 rebase 過程。

4. **在 Rebase 過程中編輯提交訊息**  
   對於每個壓縮操作，Git 會暫停並讓你編輯提交訊息（合併被壓縮的提交）。將其更新為類似「Author A 的壓縮提交：描述」的內容。儲存並繼續。  
   如果還有更多壓縮操作，請為每位作者重複此步驟。在每次編輯後執行 `git rebase --continue`。  
   如果出現衝突（在簡單的壓縮中較少見），請使用 `git add <file>` 解決衝突，然後執行 `git rebase --continue`。

5. **驗證並推送**  
   Rebase 完成後，檢查記錄：`git log --oneline -10`。你應該看到 3 個提交，每位作者各一個。  
   如果推送到共享分支，請強制推送（因為 rebase 會改寫歷史）：`git push --force-with-lease origin 分支名稱`。  
   **警告：** 僅在確定舊提交在其他地方不需要時才強制推送，因為這會改寫歷史記錄。

### 提示與注意事項
- 如果作者有許多提交，請在 rebase 列表中有效分組（例如將 Author A 的所有提交放在一起等）。
- 對於自動化需求，可使用 `git-interactive-rebase-tool` 或腳本等工具，但手動 rebase 更直接。
- 如果需要按確切作者篩選，請事先使用 `git log --author="作者名稱"` 確認。
- 先在備份分支上測試，以避免資料遺失。

有關 rebase 的更多資訊：`git help rebase`。如果這與你的具體情況不符，請提供更多關於提交結構的詳細資訊。