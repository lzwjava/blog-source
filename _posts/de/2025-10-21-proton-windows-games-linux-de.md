---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Proton ermöglicht Windows-Spiele unter Linux
translated: true
type: note
---

### Was ist Proton?

Proton ist eine von Valve entwickelte Kompatibilitätsschicht, die direkt in den Steam-Client integriert ist und es ermöglicht, Spiele und Anwendungen, die nur für Windows verfügbar sind, nahtlos auf Linux-basierten Systemen (wie SteamOS auf dem Steam Deck oder Standard-Linux-Distributionen) auszuführen. Es ist im Wesentlichen Steams eingebaute Lösung für "Linux via Proton", die es Nutzern erlaubt, eine riesige Bibliothek an PC-Spielen zu spielen, ohne eine Windows-Installation oder Dual-Boot-Setup zu benötigen.

#### Wie funktioniert es?
- **Kern-Technologie**: Proton basiert auf Wine (einer freien Kompatibilitätsschicht, die Windows-API-Aufrufe in Linux-Entsprechungen übersetzt), wurde jedoch mit Valve-spezifischen Optimierungen erweitert, einschließlich der DirecX-zu-Vulkan-Übersetzung via DXVK und VKD3D. Dies macht es für Spiele effizienter.
- **Steam-Integration**: In Steam klicken Sie einfach mit der rechten Maustaste auf ein Spiel, gehen zu Eigenschaften > Kompatibilität und aktivieren "Nutzung eines bestimmten Steam Play-Kompatibilitätstools erzwingen" (wählen Sie eine Proton-Version aus). Steam übernimmt den Rest – lädt Proton bei Bedarf herunter und startet das Spiel, als wäre es nativ für Linux.
- **Versionen**: Proton gibt es in experimentellen und stabilen Versionen. Stand 2025 unterstützt die neueste stabile Version (z.B. Proton 9.x oder höher) Tausende von Titeln mit "Platinum"- oder "Gold"-Bewertungen auf ProtonDB (eine Community-Datenbank für Kompatibilitätsberichte).

#### Vorteile für Linux-Gaming
- **Benutzerfreundlichkeit**: Für die meisten Spiele ist keine manuelle Konfiguration erforderlich – es ist "Plug-and-Play" innerhalb von Steam.
- **Leistung**: Oft erreicht oder übertrifft sie die native Windows-Leistung unter Linux aufgrund von Optimierungen, insbesondere auf Hardware wie AMD-GPUs. Einige Spiele laufen sogar besser auf Linux-Handhelds als auf vergleichbaren Windows-Setups.
- **Ökosystem-Auswirkung**: Proton hat Linux zu einer praktikablen Gaming-Plattform gemacht, treibt Geräte wie den Steam Deck an und trägt zu einer breiteren Akzeptanz von Open-Source-Technologie im Gaming bei.

Wenn Sie es einrichten, stellen Sie sicher, dass Ihre Linux-Distribution Vulkan-Treiber installiert hat (z.B. via Mesa für AMD/Intel). Bei Problemen sollten Sie ProtonDB für spielspezifische Tipps konsultieren.

#### Referenzen
- [Valve's Proton GitHub Repository](https://github.com/ValveSoftware/Proton)
- [Steam Community Guide: Proton 101](https://steamcommunity.com/app/221410/discussions/0/1636417404917541481/)
- [Rocky Linux Docs: Gaming on Linux with Proton](https://docs.rockylinux.org/10/desktop/gaming/proton/)