---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: RHEL 精簡版預設文字編輯器
translated: true
type: note
---

在 Red Hat Enterprise Linux (RHEL) 中，特別是在最小化安裝（伺服器與輕量設定的預設選項）環境下，預設僅提供由 `vim-minimal` 套件提供的文字編輯器 **vi**。這為您提供了經典 `vi` 指令的基本相容實現，用於在終端機中編輯檔案。

- **完整版 `vim`**（具備更多功能、語法突顯等增強特性的版本）預設並未安裝。您可透過 `sudo dnf install vim-enhanced` 指令新增。
- **Nano** 與 **Emacs** 未包含在最小化安裝中。這些編輯器可在套件庫中取得，但需要明確安裝：
  - 安裝 Nano：`sudo dnf install nano`
  - 安裝 Emacs：`sudo dnf install emacs`

此設計旨在保持最小化安裝的精簡性（總計約 200-300 個套件），以優先考慮安全性與效能。若您執行的是完整桌面或伺服器安裝（非最小化），根據所選環境可能會納入更多工具。

[Nano 入門指南 (Red Hat)](https://www.redhat.com/en/blog/getting-started-nano)  
[為何 RHEL 預設安裝兩個 vim？](https://unix.stackexchange.com/questions/699071/why-rhel-has-two-vim-installed-by-default)  
[RHEL 9 套件清單](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/package_manifest/index)