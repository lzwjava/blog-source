---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Git 變基壓縮順序詳解
translated: true
type: note
---

當你執行 `git rebase -i`（互動式 rebase）來壓縮提交時，Git 會遵循一個非常特定的順序和邏輯：

---

### 1. 預設順序

當你啟動互動式 rebase（例如 `git rebase -i HEAD~5`）時，Git 會在你的編輯器中開啟**從最舊到最新排列的提交清單**（頂部 = 最舊，底部 = 最新）。
這個順序很重要：這是 Git 嘗試在新基礎上重新執行的序列。

---

### 2. Pick 與 Squash

* **pick** → 保持提交不變。
* **squash（或 s）** → 將此提交與**標記為 `pick` 的前一個提交**合併。
* **fixup（或 f）** → 與 squash 相同，但會丟棄提交訊息（僅保留第一個提交的訊息）。

所以如果你寫入：

```
pick  a1b2c3  Initial feature
squash d4e5f6  Minor fix
squash g7h8i9  Small cleanup
pick  j1k2l3  Another feature
```

Git 會將 `d4e5f6` 和 `g7h8i9` 合併到 `a1b2c3` 中，產生單一提交。

---

### 3. 重新排列提交

你可以**直接在 rebase 編輯器中重新排序提交**，透過上下移動行來實現。
例如：

```
pick  a1b2c3  Initial feature
pick  j1k2l3  Another feature
squash d4e5f6  Minor fix
squash g7h8i9  Small cleanup
```

在這裡，Git 會先套用 `a1b2c3`，然後是 `j1k2l3`。
`squash` 提交（`d4e5f6` 和 `g7h8i9`）現在會壓縮到 **`j1k2l3`** 中，因為 squash 總是合併到最近的前一個 `pick` 中。

---

### 4. 編輯訊息

壓縮後，Git 會暫停並讓你**編輯壓縮提交的提交訊息**。你可以：

* 保留所有訊息。
* 手動合併它們。
* 僅保留第一個訊息。

---

### 5. 常見陷阱

* 如果你將 `squash` 放在第一個提交（前面沒有 `pick`），Git 會拋出錯誤——它需要一個基礎提交來進行壓縮。
* 如果在重新排序後提交發生衝突，你需要在 rebase 過程中手動解決衝突。
* 重新排序可能會顯著改變歷史記錄；僅在尚未推送/共享的分支上進行，除非你確定要改寫歷史記錄。

---

✅ 簡而言之：

* 提交以**最舊 → 最新**的順序列出。
* `pick` 保留提交，`squash` 合併到**最近的前一個 `pick`** 中。
* 你可以在編輯器中手動重新排列提交；squash 總是將後面的提交附加到前一個被選取的提交中。

---

你想讓我用**提交歷史記錄的前後對比例子**（顯示壓縮前後的 `git log --oneline`）來說明這一點嗎？這通常會讓順序更清晰。