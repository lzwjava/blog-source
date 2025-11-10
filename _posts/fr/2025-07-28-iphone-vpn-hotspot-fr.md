---
audio: false
generated: true
image: false
lang: fr
layout: post
title: VPN sur iPhone, pas sur le partage de connexion
translated: true
type: note
---

Oui, il est généralement possible d'utiliser votre iPhone 14 Pro Max sur un réseau de données cellulaires 5G avec une application VPN comme Shadowrocket activée, tout en partageant une connexion personnelle (hotspot) avec votre MacBook. Il n'y a généralement pas de conflit inhérent dans cette configuration, car iOS est conçu pour gérer les deux fonctionnalités simultanément sans en désactiver une ou l'autre.

Concernant votre question spécifique : Le trafic des appareils connectés au hotspot personnel de votre iPhone (comme votre MacBook) n'emprunte **pas** le VPN configuré sur l'iPhone lui-même. Au lieu de cela, le hotspot partage la connexion cellulaire brute directement, en contournant le tunnel VPN. Cela signifie :
- Les applications et le trafic propres à votre iPhone utiliseront le VPN (par exemple, le proxy ou le tunnel de Shadowrocket).
- Mais le trafic Internet du MacBook passera directement par le réseau cellulaire sans que le chiffrement ou le routage du VPN ne lui soit appliqué.

Si vous souhaitez que le trafic du Mac utilise également un VPN, vous devez en configurer un directement sur le Mac lui-même.

[Does the VPN monitor my Hotspot traffic? - Accountable2You Support](https://support.accountable2you.com/article/791-faq-does-the-vpn-monitor-my-hotspot-traffic)
[If I am connected to my phone's hotspot on my laptop and VPN is activated on the phone, does the laptop also get VPN security protection? - Quora](https://www.quora.com/If-I-am-connected-to-my-phones-hotspot-on-my-laptop-and-VPN-is-activated-on-the-phone-does-the-laptop-also-get-VPN-security-protection)
[Why does shared WiFi connection from iPhone to laptop (personal hotspot) not go through VPN? - Apple Stack Exchange](https://apple.stackexchange.com/questions/400853/why-does-shared-wifi-connection-from-iphone-to-laptop-personal-hotspot-not-go)