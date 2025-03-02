---
audio: false
generated: false
lang: ja
layout: post
title: ChatGPT iOS VPN検証の分析
translated: true
---

今日、中国でVPNを使用してChatGPTのiOSアプリにログインできるようになったことを発見しました。以前は、以下のようなブロックプロンプトが表示されていました。

しかし、現時点ではVPNを使用すれば問題なく動作します。

ChatGPTのiOSアプリが初めてリリースされた時、VPNを使って利用しても問題なかったことを覚えています。その後、VPNの検出が厳しくなり、ログインが難しくなりました。幸い、最近はこの制限が緩和されたようです。

さらにテストを進めたところ、DigitalOceanのシンガポールリージョンのVPNを使用している場合、アプリにアクセスできないことがわかりました。しかし、台湾や英国のVPN（https://zhs.cloud 提供）を使用すると、完璧に動作しました。

ChatGPT iOSのVPN検出は、特定のIPアドレスに基づいているようです。一部のクラウドプロバイダーや特定のIPアドレスが禁止されているため、VPNサーバーの場所によって動作が一貫しないことが説明されるかもしれません。

![](assets/images/chatgpt/block.jpg){: .responsive }

![](assets/images/chatgpt/c1.png){: .responsive }