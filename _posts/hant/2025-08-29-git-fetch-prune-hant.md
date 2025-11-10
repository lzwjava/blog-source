---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Git 擷取與清理概覽
translated: true
type: note
---

### 什麼是 `git fetch`？
`git fetch` 會從遠端儲存庫下載最新變更（提交、分支、標籤），但不會將它們合併到你目前的分支中。它會更新你本地的遠端追蹤分支（例如 `origin/main`）以符合遠端狀態。這能讓你的本地儲存庫保持同步，但不會改變你的工作檔案或本地分支。

### 什麼是 `--prune` 選項？
`--prune` 標記會指示 Git 刪除遠端已不存在的遠端追蹤分支。舉例來說，若有人在 GitHub 上刪除了一個分支，你本地的副本（例如 `origin/old-branch`）仍會保留，除非進行了修剪操作。

### `git fetch --prune` 如何運作？
- **執行方式**：以 `git fetch --prune`（或簡寫 `git fetch -p`）執行。它將 fetch 和 prune 操作合併為一個指令。
- **步驟**：
  1. Git 連接到遠端並擷取更新，更新遠端追蹤分支以反映新的提交、新增的分支或已刪除的分支。
  2. 它會掃描過時的遠端追蹤分支（那些在遠端沒有對應分支的本地追蹤分支）並在本機刪除它們。
- **結果**：你的本地儲存庫保持最新且整潔。不會進行任何合併操作——這是一個唯讀的同步過程。

### 實際範例
假設你有：
- 本地分支：`main`，追蹤 `origin/main`。
- 一個過時的本地遠端追蹤分支：`origin/deleted-feature`。

對 `origin` 執行 `git fetch --prune`：
- 擷取任何新的提交。
- 移除 `origin/deleted-feature`（因為它在遠端已不存在）。
- 不會觸及你的本地分支。

### 這意味著什麼
這意味著「擷取最新的遠端數據並清理本地儲存庫中過時的參考」。定期使用此指令可避免因舊分支引用而產生混淆。它等同於先執行 `git fetch` 再執行 `git remote prune origin`，但以更便捷的方式結合。為安全起見，它僅影響遠端追蹤分支，不會觸及你自身的工作內容。