---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: Git Rebase 移除提交
translated: true
type: note
---

是的 — 完全正確。

當你在互動式 `git rebase -i` 中使用 **`drop`** 時，意思是 **「將這個提交從歷史記錄中完全移除」**。

實際發生的情況如下：

* Git 在重新套用其他提交時，會**跳過套用**該提交。
* 最終產生的分支看起來就像該提交**從未存在過** — 其變更內容和提交訊息都會消失。
* 後續提交仍會被套用（前提是它們不依賴被移除的變更）。

範例：

```bash
git rebase -i HEAD~4
```

你可能會看到類似這樣的內容：

```
pick a1b2c3d 修正拼寫錯誤
pick b2c3d4e 新增 README
pick c3d4e5f 實作登入功能
pick d4e5f6g 新增除錯日誌
```

如果你將最後一行改為：

```
drop d4e5f6g 新增除錯日誌
```

那麼在儲存並關閉編輯器後，Git 會重新調整分支並**排除該提交**。

所以沒錯 — 「drop」= **從分支歷史記錄中刪除該提交**。

需要我說明這與 `revert`（*撤銷*提交但保留記錄）的區別嗎？