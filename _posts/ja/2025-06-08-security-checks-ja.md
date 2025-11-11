---
audio: false
generated: true
lang: ja
layout: post
title: ジェミニ対グロックのセキュリティチェック
translated: true
type: note
---

* **Gemini (gemini.google.com):** GoogleのGeminiは、通常 `gemini.google.com` を直接アクセスする際に「Cloudflareによる人間確認」（CAPTCHAや「Verifying you are human」ページなど）を表示しません。Googleはボット検出とユーザー確認のために独自の内部メカニズムを有しています。

* **Grok (grok.com):** はい、GrokはCloudflareのセキュリティ対策、特に「Verify you are human」確認を頻繁に利用します。多くのユーザーが `grok.com` にアクセスしようとした際に、CloudflareのTurnstile（CAPTCHAの代替手段）に遭遇したと報告しています。これは、ウェブサイトがボットや悪用から保護するための一般的な方法です。