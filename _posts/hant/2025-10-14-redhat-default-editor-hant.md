---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 紅帽企業 Linux 預設文字編輯器
translated: true
type: note
---

### Red Hat Enterprise Linux 中的預設文字編輯器

在 Red Hat Enterprise Linux (RHEL) 中，預設文字編輯器是 **Vi**（通常別名為 **Vim**，全稱為 "Vi IMproved"）。Vi 是一款模態式命令列文字編輯器，自 1970 年代以來一直是類 Unix 系統的標準配備。它輕量、無處不在，並透過 `vim-minimal` 或 `vim-enhanced` 套件預先安裝於大多數 RHEL 系統中。

#### 為何選擇 Vi/Vim？
- 在圖形介面編輯器不適用的伺服器環境中，它能高效運作。
- 指令以鍵盤為基礎：插入模式用於輸入（`i`），命令模式用於編輯（例如：`dd` 刪除一行，`:wq` 儲存並離開）。
- 若您是初次使用，雖然需要學習曲線，但熟練後功能非常強大。

#### 檢查與使用方法
- 執行 `vi filename.txt`（或 `vim filename.txt`）來開啟檔案。
- 若要檢查當前預設編輯器：`echo $EDITOR`（通常輸出 `/usr/bin/vi`）。
- 若您偏好其他編輯器（如先前查詢中的 Emacs），可在 `~/.bashrc` 中設定 `export EDITOR=emacs`。

如需快速入門，請輸入 `vimtutor` 啟動互動式教學課程。

[如何開始使用 Vi 編輯器 - Red Hat](https://www.redhat.com/en/blog/get-started-vi-editor)  
[Linux 技能：9 個教學讓您更深入掌握文字編輯器 - Red Hat](https://www.redhat.com/en/blog/text-editor-roundup-2022)