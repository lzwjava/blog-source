---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Rebase 根提交基礎指南
translated: true
type: note
---

`git rebase --root` 是一種特殊的 rebase 形式，可讓你重新改寫儲存庫的**最初提交**。通常 `git rebase` 需要一個父提交作為 rebase 基礎，但 `--root` 選項會將根提交（沒有父提交的第一個提交）也視為可 rebase 的對象。

以下是實際運作方式：

### 1. 標準 rebase 與根 rebase 的比較

* **一般 `git rebase`**：你將提交重新應用到另一個分支或提交之上，從選定的基礎點開始改寫歷史。
* **`git rebase --root`**：它不是從根提交之後開始，而是直接改寫根提交本身。你可以拆分它、將它與後續提交合併，甚至完全替換它。

### 2. 典型使用場景

* **編輯首次提交訊息**
  若想改寫專案的最初提交訊息，可執行：

  ```bash
  git rebase --root -i
  ```

  並將第一個提交的 `pick` 改為 `reword`。

* **將根提交與後續提交合併**
  例如，若你的首次提交僅是基礎架構（如 `README`），可將其與後續提交合併以簡化歷史記錄。

* **拆分根提交**
  若首次提交包含過多內容（例如整個專案程式碼），可在互動式 rebase 中將其拆分為多個邏輯提交。

### 3. 內部運作原理

* Git 會為根提交建立一個臨時的「虛擬」父提交，以便從頭開始應用 rebase 操作。
* 每個提交都會被重新演播（rebase），就像儲存庫以不同方式起始一樣。
* 你實際上是在重寫儲存庫歷史的基礎。

### 4. 範例工作流程

```bash
git rebase --root -i
```

你將看到類似以下的編輯器內容：

```
pick a1b2c3d Initial commit
pick d4e5f6g Add feature A
pick h7i8j9k Add feature B
```

在此你可進行以下操作：

* 將根提交的 `pick` 改為 `reword` → 修改其提交訊息。
* 將 `pick` 改為 `squash` → 將根提交與後續提交合併。
* 根據需要重新排序或拆分。

### ⚠️ 重要注意事項

`git rebase --root` 會**改寫歷史記錄**，因此僅應在未推送/未共享的分支上執行，否則後續必須強制推送。在共享分支上使用此操作，可能會導致協作者混淆與衝突。

---

需要我進一步展示具體的**歷史記錄前後對照範例**（含提交雜湊值）嗎？這樣你就能清楚看到 `git rebase --root` 如何實際改變提交記錄。