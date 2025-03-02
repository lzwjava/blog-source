---
audio: false
generated: false
lang: de
layout: post
title: Analyse der ChatGPT iOS VPN-Erkennung
translated: true
---

Heute habe ich festgestellt, dass die ChatGPT iOS-App nun die Anmeldung mit einem VPN in China ermöglicht. Zuvor wurde eine Blockierungsmeldung angezeigt, wie die unten abgebildete.

Allerdings funktioniert es bis heute einwandfrei mit einem VPN.

Ich erinnere mich, dass es bei der ersten Veröffentlichung der ChatGPT iOS-App kein Problem war, sie mit einem VPN zu nutzen. Später wurde die VPN-Erkennung jedoch strenger, was das Einloggen erschwerte. Zum Glück scheint diese Einschränkung in letzter Zeit gelockert worden zu sein.

Bei weiteren Tests stellte ich fest, dass ich die App nicht aufrufen konnte, wenn ich ein VPN in der DigitalOcean-Region Singapur verwendete. Allerdings funktionierte es einwandfrei, wenn ich VPNs aus Taiwan oder dem Vereinigten Königreich (bereitgestellt von https://zhs.cloud) nutzte.

Es scheint, dass die VPN-Erkennung von ChatGPT für iOS auf bestimmten IP-Adressen basiert. Einige Cloud-Anbieter oder bestimmte IP-Adressen sind gesperrt, was das inkonsistente Verhalten in Abhängigkeit vom Standort des VPN-Servers erklären könnte.

![](assets/images/chatgpt/block.jpg){: .responsive }

![](assets/images/chatgpt/c1.png){: .responsive }