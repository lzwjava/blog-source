---
audio: false
generated: true
image: false
lang: es
layout: post
title: VPN en iPhone, No en Punto de Acceso
translated: true
type: note
---

Sí, generalmente está bien usar tu iPhone 14 Pro Max con datos celulares 5G y una app VPN como Shadowrocket habilitada, mientras compartes el hotspot personal con tu MacBook. Normalmente no hay un conflicto inherente en esta configuración, ya que iOS está diseñado para manejar ambas funciones simultáneamente sin desactivar una u otra.

Con respecto a tu pregunta específica: El tráfico de los dispositivos conectados al hotspot personal de tu iPhone (como tu MacBook) *no* se enruta a través de la VPN configurada en el propio iPhone. En cambio, el hotspot comparte la conexión celular directamente, omitiendo el túnel de la VPN. Esto significa:
- Las apps y el tráfico propios de tu iPhone usarán la VPN (por ejemplo, el proxy o túnel de Shadowrocket).
- Pero el tráfico de internet del MacBook irá directamente a través de la red celular sin el cifrado o enrutamiento de la VPN aplicado.

Si deseas que el tráfico del Mac también use una VPN, necesitarías configurar una directamente en el Mac.

[Does the VPN monitor my Hotspot traffic? - Accountable2You Support](https://support.accountable2you.com/article/791-faq-does-the-vpn-monitor-my-hotspot-traffic)  
[If I am connected to my phone's hotspot on my laptop and VPN is activated on the phone, does the laptop also get VPN security protection? - Quora](https://www.quora.com/If-I-am-connected-to-my-phones-hotspot-on-my-laptop-and-VPN-is-activated-on-the-phone-does-the-laptop-also-get-VPN-security-protection)  
[Why does shared WiFi connection from iPhone to laptop (personal hotspot) not go through VPN? - Apple Stack Exchange](https://apple.stackexchange.com/questions/400853/why-does-shared-wifi-connection-from-iphone-to-laptop-personal-hotspot-not-go)