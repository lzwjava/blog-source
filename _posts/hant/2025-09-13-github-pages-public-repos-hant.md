---
audio: false
date: 2025-09-13
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: GitHub Pages 要求使用公開儲存庫
translated: true
type: note
---

沒錯 — 如果你將 GitHub Pages 儲存庫設為私人，就會失去免費的 GitHub Pages 託管服務。

GitHub Pages 僅在儲存庫為**公開**狀態時才能自動運作。若儲存庫設為私人，`github.io` 網站將無法發布，除非你使用**啟用了私人儲存庫 Pages 功能的 GitHub Enterprise 方案**（此為付費功能，不包含在免費或標準個人帳戶中）。

因此，對於你的個人部落格 `username.github.io`：

* **公開儲存庫** → GitHub Pages 會自動構建並發佈至 `https://username.github.io/`
* **私人儲存庫（免費帳戶）** → GitHub Pages 功能將被停用
* **私人儲存庫（Enterprise 方案）** → 仍可正常運作，但僅限於組織已啟用私人儲存庫 Pages 功能的情況

需要我進一步說明替代方案嗎（例如保持主儲存庫為私人狀態，僅將 `_site` 輸出內容同步至獨立的公開儲存庫進行發布）？