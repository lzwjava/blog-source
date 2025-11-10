---
audio: false
generated: true
image: false
lang: ja
layout: post
title: iPhoneのVPN、ホットスポットには非対応
translated: true
type: note
---

はい、一般的にiPhone 14 Pro MaxでShadowrocketのようなVPNアプリを有効にした5Gモバイルデータ通信を使用しながら、Macノートパソコンに個人用ホットスポットを共有しても問題ありません。この設定には通常、根本的な衝突はなく、iOSは両方の機能を同時に処理できるように設計されており、一方が他方を無効化することはありません。

具体的な質問について：iPhoneの個人用ホットスポットに接続されたデバイス（Macノートパソコンなど）からのトラフィックは、iPhone自体で設定されたVPNを経由しません。代わりに、ホットスポットはVPNトンネルをバイパスして、生のモバイル接続を直接共有します。これはつまり：
- iPhone自体のアプリとトラフィックはVPN（例：Shadowrocketのプロキシやトンネル）を使用します。
- しかし、Macノートパソコンのインターネットトラフィックは、VPNの暗号化やルーティングが適用されず、モバイルネットワークを直接通過します。

MacのトラフィックにもVPNを使用させたい場合は、Mac自体に直接VPNを設定する必要があります。

[VPNはホットスポットのトラフィックを監視しますか？ - Accountable2Youサポート](https://support.accountable2you.com/article/791-faq-does-the-vpn-monitor-my-hotspot-traffic)  
[スマートフォンのホットスポットに接続しているノートパソコンで、スマートフォンでVPNが有効になっている場合、ノートパソコンもVPNのセキュリティ保護を受けますか？ - Quora](https://www.quora.com/If-I-am-connected-to-my-phones-hotspot-on-my-laptop-and-VPN-is-activated-on-the-phone-does-the-laptop-also-get-VPN-security-protection)  
[iPhoneからノートパソコンへのWiFi共有（個人用ホットスポット）がVPNを経由しないのはなぜですか？ - Apple Stack Exchange](https://apple.stackexchange.com/questions/400853/why-does-shared-wifi-connection-from-iphone-to-laptop-personal-hotspot-not-go)