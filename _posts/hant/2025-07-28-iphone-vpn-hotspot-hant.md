---
audio: false
generated: true
image: false
lang: hant
layout: post
title: iPhone VPN 非熱點共享
translated: true
type: note
---

是的，一般來說，在 iPhone 14 Pro Max 上使用 5G 流動數據並啟用像 Shadowrocket 這類 VPN 應用程式，同時分享個人熱點給你的 Mac 筆記型電腦是沒有問題的。這種設定通常不會產生內在衝突，因為 iOS 的設計本來就能同時處理這兩項功能，而不會互相干擾。

關於你的具體問題：連接到 iPhone 個人熱點的裝置（例如你的 Mac 筆記型電腦）的流量，並不會經過 iPhone 上設定的 VPN。相反地，熱點會直接分享原始的流動網絡連接，繞過 VPN 通道。這意味著：
- 你 iPhone 自身的應用程式和流量會使用 VPN（例如 Shadowrocket 的代理或通道）。
- 但 Mac 筆記型電腦的網絡流量會直接通過流動網絡，而不會經過 VPN 的加密或路由。

如果你希望 Mac 的流量也使用 VPN，你需要在 Mac 本身上直接設定一個 VPN。

[VPN 會監控我的熱點流量嗎？ - Accountable2You 支援](https://support.accountable2you.com/article/791-faq-does-the-vpn-monitor-my-hotspot-traffic)  
[如果我的筆記型電腦連接到手機的熱點，並且手機上啟用了 VPN，筆記型電腦是否也會獲得 VPN 安全保護？ - Quora](https://www.quora.com/If-I-am-connected-to-my-phones-hotspot-on-my-laptop-and-VPN-is-activated-on-the-phone-does-the-laptop-also-get-VPN-security-protection)  
[為什麼從 iPhone 分享給筆記型電腦的 WiFi 連接（個人熱點）不會經過 VPN？ - Apple Stack Exchange](https://apple.stackexchange.com/questions/400853/why-does-shared-wifi-connection-from-iphone-to-laptop-personal-hotspot-not-go)