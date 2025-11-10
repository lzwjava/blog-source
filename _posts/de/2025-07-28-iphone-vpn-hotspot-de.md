---
audio: false
generated: true
image: false
lang: de
layout: post
title: VPN auf iPhone, nicht auf Hotspot
translated: true
type: note
---

Ja, es ist in der Regel in Ordnung, dein iPhone 14 Pro Max mit 5G-Mobilfunkdaten zu verwenden, während eine VPN-App wie Shadowrocket aktiviert ist und du einen persönlichen Hotspot für deinen Mac Laptop freigibst. Normalerweise gibt es keinen inherenten Konflikt in diesem Setup, da iOS dafür ausgelegt ist, beide Funktionen gleichzeitig zu handhaben, ohne dass eine davon deaktiviert wird.

Bezüglich deiner spezifischen Frage: Der Datenverkehr von Geräten, die mit dem persönlichen Hotspot deines iPhones verbunden sind (wie dein Mac Laptop), wird nicht durch das auf dem iPhone konfigurierte VPN geleitet. Stattdessen teilt der Hotspot die ursprüngliche Mobilfunkverbindung direkt und umgeht den VPN-Tunnel. Das bedeutet:
-   Die eigenen Apps und der Datenverkehr deines iPhones werden das VPN verwenden (z.B. den Proxy oder Tunnel von Shadowrocket).
-   Der Internetverkehr des Mac Laptops geht jedoch direkt über das Mobilfunknetz, ohne die Verschlüsselung oder das Routing des VPN.

Wenn du möchtest, dass der Verkehr des Macs ebenfalls ein VPN verwendet, müsstest du eines direkt auf dem Mac selbst einrichten.

[Does the VPN monitor my Hotspot traffic? - Accountable2You Support](https://support.accountable2you.com/article/791-faq-does-the-vpn-monitor-my-hotspot-traffic)
[If I am connected to my phone's hotspot on my laptop and VPN is activated on the phone, does the laptop also get VPN security protection? - Quora](https://www.quora.com/If-I-am-connected-to-my-phones-hotspot-on-my-laptop-and-VPN-is-activated-on-the-phone-does-the-laptop-also-get-VPN-security-protection)
[Why does shared WiFi connection from iPhone to laptop (personal hotspot) not go through VPN? - Apple Stack Exchange](https://apple.stackexchange.com/questions/400853/why-does-shared-wifi-connection-from-iphone-to-laptop-personal-hotspot-not-go)