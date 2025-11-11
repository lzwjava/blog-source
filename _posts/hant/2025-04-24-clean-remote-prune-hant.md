---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 使用修剪功能清理遠端分支
translated: true
type: note
---

`git fetch --prune` 是一種保持本地遠端分支參照整潔且最新的方法。

### 功能說明

* **`git fetch`** 通常會更新你本地儲存庫中遠端分支的狀態（例如 `origin/main`、`origin/feature-x`），而不會影響你自己的本地分支。
* 隨著時間推移，遠端儲存庫可能會刪除或重新命名某些分支。若未進行清理，你的本地儲存庫仍會顯示那些過時的遠端追蹤分支（例如 `origin/feature-old`）。
* **加上 `--prune` 參數** 會告訴 Git：*「如果遠端已不存在某個分支，就刪除我本地對應的遠端追蹤參照。」*

因此，在執行 `git fetch --prune` 後，你本地的遠端分支列表就會與遠端當前狀態完全一致。

### 範例

1. 遠端擁有分支：`main`、`feature-a`
2. 你執行 `git fetch` → 現在你本地有 `origin/main`、`origin/feature-a`
3. 有人在遠端刪除了 `feature-a`
4. 若你執行 `git fetch`，本地仍會看到 `origin/feature-a`（過時參照）
5. 若你執行 `git fetch --prune`，Git 會發現 `feature-a` 已消失，並從本地儲存庫移除 `origin/feature-a`

### 實用價值

* 保持 `git branch -r`（遠端分支列表）整潔
* 避免切換或合併到上游已不存在分支時產生混淆
* 常與別名搭配使用（例如 `git fetch -p`），或透過以下設定設為預設行為：

  ```bash
  git config fetch.prune true
  ```

這樣每次執行 `git fetch` 時就會自動清理過時分支。

---

你是否還想了解**修剪機制與標籤的互動關係**（由於 `git fetch --prune` 預設僅處理分支，而標籤的處理方式有所不同）？