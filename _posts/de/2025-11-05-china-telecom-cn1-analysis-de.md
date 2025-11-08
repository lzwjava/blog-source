---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Analyse des China Telecom CN1-Netzwerks
translated: true
type: note
---

Basierend auf dem von Ihnen geteilten Traceroute von einem Meiyijia Convenience Store WiFi in Guangzhou scheint dies das Standard-ChinaNet-Backbone von China Telecom zu sein (oft als CN1 bezeichnet), nicht das Premium-CN2-Netzwerk. Hier ist eine kurze Aufschlüsselung, warum:

### Wichtige Indikatoren aus dem Traceroute
- **Hops 5–10 (China Telecom Backbone)**: IPs wie 14.147.135.198, 183.56.34.41, 202.97.93.89–202.97.116.210 und 203.215.237.42 gehören alle zu AS4134 (ChinaNet), dem Haupt-Backbone von China Telecom für den Inlands- und Internationalverkehr. Diese sind bei Standard-Breitbandanschlüssen üblich.
  - Der Bereich 202.97.x.x ist spezifisch für ChinaNet (nicht CN2).
  - 203.215.237.42 befindet sich in Xiamen, Fujian (immer noch innerhalb Chinas) und gehört zu CHINANET Fujian Province Network (AS4134).
- **Keine CN2-Signaturen**: CN2 (AS4809) zeigt typischerweise IPs in Bereichen wie 59.43.0.0/16 oder 121.59.0.0/16 während der Backbone-Phase. Ihr Trace erreicht keine davon.
- **Ausgangspfad**: Der Verkehr verlässt China über eine Standard-ChinaNet-Übergabe an Microsoft (Azure) in Tokyo (Hop 11: 104.44.235.92) und routet dann südwärts nach Singapur (Hops 14–15). Dies ist ein üblicher, nicht optimierter Pfad für grundlegende China Telecom-Verbindungen – der Umweg über Japan fügt ~300ms Latenz hinzu, was mit CN1-Überlastung übereinstimmt. CN2 nutzt oft direkte Ausgänge über Hongkong oder kürzere Asia-Pacific-Routen für geringere Latenz (~150–200ms zu GitHub von Guangzhou).
- **Kontext**: Meiyijia-Filialen in Guangzhou nutzen in der Regel Consumer-/Geschäftskunden-Breitband von China Telecom, das standardmäßig auf ChinaNet (CN1) eingestellt ist, es sei denn, es wurde explizit auf CN2 GIA aufgerüstet (ein kostenpflichtiges Enterprise-Add-on).

### CN1 vs. CN2 Schneller Vergleich

| Aspekt          | CN1 (ChinaNet)                          | CN2 (Premium)                          |
|-----------------|-----------------------------------------|----------------------------------------|
| **AS-Nummer**   | AS4134                                 | AS4809                                |
| **Typische Latenz zu GitHub (von Guangzhou)** | 250–400ms (überlastet, indirekte Routen) | 100–200ms (optimiert, direkte Ausgänge)   |
| **IP-Bereiche**   | 202.97.x.x, 183.56.x.x, etc.           | 59.43.x.x, 121.59.x.x, etc.           |
| **Einsatzzweck**    | Standard-Haushalts-/Geschäftskunden-Breitband       | VPS/Cloud/Enterprise (Zusatzkosten)     |
| **Pfadstil**  | Oft Umwege (z.B. über Japan/Korea)  | Direkt zu HK/US/Asia-Hubs             |

Wenn Sie dies bestätigen oder weiter testen möchten:
- Führen Sie `traceroute github.com` während der Hauptverkehrszeiten (z.B. abends) aus, um auf weitere Überlastung zu prüfen.
- Pingen Sie eine CN2-Testseite wie `www.cn2.net` – wenn die Latenz unter 200ms liegt, haben Sie möglicherweise teilweisen CN2-Zugang.
- Kontaktieren Sie den Meiyijia- oder China Telecom-Support bezüglich Ihres Leitungstyps (erwähnen Sie "CN2 GIA" bei einem Upgrade).

[China Telecom CN2 Overview](https://www.ctamericas.com/company/global-network/cn2/)  
[IPinfo für 203.215.237.42](https://ipinfo.io/203.215.237.42)  
[CN2 vs ChinaNet Guide](http://chihengcloud.com/en/blog/cloudservice/what-is-cn2-network-a-3-minute-guide-to-types-and-features/)