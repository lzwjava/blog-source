---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Maximale Übertragungseinheit kurz erklärt
translated: true
type: note
---

### Was ist MTU in Netzwerken?

**MTU** steht für **Maximum Transmission Unit**. Sie bezieht sich auf die maximale Größe (in Bytes) eines einzelnen Datenpakets, das über eine Netzwerkschnittstelle oder ein Protokoll übertragen werden kann, ohne in kleinere Teile fragmentiert werden zu müssen.

#### Wichtige Details:
- **Typische Werte**:
  - Ethernet-Netzwerke verwenden oft eine MTU von 1500 Bytes (der Standard für die meisten IP-basierten Netzwerke).
  - Jumbo Frames können auf unterstützter Hardware bis zu 9000 Bytes oder mehr betragen.
  - IPv6 hat eine minimale MTU von 1280 Bytes.
- **Warum das wichtig ist**:
  - **Effizienz**: Größere MTUs reduzieren den Overhead (z.B. weniger Header pro Dateneinheit) und verbessern den Durchsatz.
  - **Fragmentierungsprobleme**: Wenn ein Paket die MTU eines Links überschreitet, kann es geteilt (fragmentiert) oder verworfen werden, was zu Verzögerungen, Neuübertragungen oder Fehlern (wie "packet too big" ICMP-Nachrichten) führt.
  - **Path MTU Discovery (PMTUD)**: Geräte nutzen diesen Prozess, um die kleinste MTU entlang eines Netzwerkpfades zu finden und die Paketgrößen entsprechend anzupassen, um Fragmentierung zu vermeiden.
- **Häufige Probleme**: Nicht übereinstimmende MTUs zwischen Geräten (z.B. VPN-Tunnel) können Verbindungsprobleme verursachen. Sie können die MTU mit Tools wie `ifconfig` (Linux/macOS) oder `netsh` (Windows) überprüfen oder setzen.

Kurz gesagt definiert die MTU das "maximale Nutzlast"-Limit für Pakete und sorgt so für einen Ausgleich zwischen Geschwindigkeit und Kompatibilität im Netzwerkdesign.

Für mehr Tiefe: [Maximum transmission unit - Wikipedia](https://en.wikipedia.org/wiki/Maximum_transmission_unit)