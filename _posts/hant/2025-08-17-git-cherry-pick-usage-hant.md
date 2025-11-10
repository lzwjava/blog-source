---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Git Cherry-Pick 概述與用法
translated: true
type: note
---

### 什麼是 Git Cherry-Pick？

Git cherry-pick 是一個指令，允許您將特定提交（或一組提交）中的變更套用到當前分支上，並創建一個包含這些變更的新提交。當您想從某個分支中選取特定修復或功能，而不想合併整個分支時，這個指令非常有用。與合併（會整合所有歷史記錄）不同，cherry-pick 會選擇性地複製變更。

### Git Cherry-Pick 的內部運作原理

1. **選擇提交**：您指定一個包含所需變更的提交哈希值（例如，透過 `git log` 查找）。

2. **套用變更**：Git 從該提交中提取差異（實際的程式碼變更），並嘗試將其套用到當前分支的工作目錄中，盡可能使用 Git 的三方合併邏輯。

3. **創建新提交**：如果成功，您的分支上會創建一個新提交，其中包含：
   - 與原始提交相同的變更。
   - 一個新的提交哈希值（因為這是一個全新的提交）。
   - 一個引用原始提交的提交訊息（例如，透過 `-x` 標記附加「cherry picked from commit <hash>」）。

   如果出現合併衝突（例如，目標分支有不兼容的變更），Git 會暫停並讓您手動解決衝突後再提交。

此過程不會改變原始提交的歷史記錄——它只是複製變更。這使得 cherry-pick 非常適合用於回溯修復錯誤或選擇性地套用功能。

### 基本使用步驟

1. 確保您位於目標分支上（使用 `git checkout <branch>` 切換）。
2. 找到您想要的提交哈希值（例如，`git log --oneline`）。
3. 執行：`git cherry-pick <commit-hash>`
   - 多個提交：`git cherry-pick <hash1> <hash2>`
   - 使用選項如 `-n`（不提交，用於暫存）或 `-x`（引用原始提交）。
4. 如果出現衝突，編輯檔案，使用 `git add` 暫存，然後執行 `git cherry-pick --continue`。
5. 如果中途放棄：`git cherry-pick --abort`。

### 示例情境

假設您有一個功能分支，提交記錄為 A -> B -> C，而您想將提交 B cherry-pick 到主分支上。

- 在主分支上：`git checkout main`
- `git cherry-pick B`（將 B 替換為實際的哈希值）

這會將 B 的變更作為新提交 D 添加到主分支上，而不會引入 A 或 C。原始的 B 仍保留在功能分支中。

### 注意事項與提示

- 避免 cherry-pick 合併提交（具有多個父提交的提交），因為這可能導致問題——使用 `git cherry-pick -m 1 <merge-commit>` 來指定父提交。
- 它不會保留提交的元數據，如作者日期，但 `git cherry-pick --edit` 允許您修改訊息。
- 對於連續的變更，按順序 cherry-pick 多個提交以避免遺漏依賴項。
- cherry-pick 後務必進行測試，因為如果上下文不同，可能會引入錯誤。

更多詳細資訊，官方 Git 文檔提供了全面的指南：https://git-scm.com/docs/git-cherry-pick。如果您遇到特定問題，請分享您的 Git 日誌輸出！