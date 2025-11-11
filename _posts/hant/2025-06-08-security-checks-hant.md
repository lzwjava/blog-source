---
audio: false
generated: true
lang: hant
layout: post
title: Gemini 與 Grok 安全檢查對決
translated: true
type: note
---

* **Gemini (gemini.google.com):** 當您直接透過 `gemini.google.com` 存取 Google 的 Gemini 時，通常不會出現「Cloudflare 人工驗證」（例如 CAPTCHA 或「正在驗證您是否為人類」頁面）。Google 擁有自身的內部機制來偵測機器人並進行使用者驗證。

* **Grok (grok.com):** 是的，Grok 經常使用 Cloudflare 的安全防護措施，包括其「驗證您是否為人類」的檢查。許多用戶回報在嘗試存取 `grok.com` 時會遇到 Cloudflare 的 Turnstile（其 CAPTCHA 的替代方案）。這是網站防範機器人與濫用行為的常見方式。