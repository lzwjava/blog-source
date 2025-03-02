---
audio: false
generated: false
lang: de
layout: post
title: Ethernet-Adapter mit Blitzanschluss
translated: true
---

Ich habe kürzlich ein neues Produkt ausprobiert, das ich noch nie zuvor verwendet hatte. Es kostete mich etwa 44 CNY auf JD.com. Ähnliche Produkte kosten etwa 15 USD auf Walmart.com.

Es funktioniert perfekt, und keine zusätzlichen Einstellungen sind erforderlich. Nach dem Einstecken des Adapters erscheint ein Menüpunkt "Ethernet".

Ich habe die Speedtest iOS App verwendet, um die Geschwindigkeit zu testen. Die Ergebnisse sind unten aufgeführt.

| Netzwerktyp                     | Entfernung  | Download Geschwindigkeit (MBPS) | Upload Geschwindigkeit (MBPS) | Leitung           |
|----------------------------------|-------------|-------------------------------|-------------------------------|-------------------|
| Modem -> TP-LINK Router -> Telefon | etwa 30m  | 2.90                      | 4.82                        | Guangzhou -> Macao   |
| Modem -> Kabel -> Telefon       | etwa 30m  | 84.9                      | 59.7                        | Guangzhou -> Macao   |

Bei einem Test sind die Ping (ms) Reaktionsfähigkeitsergebnisse unten aufgeführt:

| Metrik    | Wert  | Jitter |
|-----------|-------|--------|
| Leerlauf  | 33    | 68     |
| Download  | 1885  | 110    |
| Upload    | 127   | 54     |

Dies ist ein etwas naiver Test. Ich vermute, dass einer der Gründe für die Unterschiede in den Geschwindigkeiten darin besteht, dass die Verbindung von Modem -> TP-LINK Router etwa 20m beträgt und die Verbindung von TP-LINK Router -> Telefon etwa 10m beträgt. Zusätzlich verwendet der TP-LINK Router eine drahtlose Brücke, um eine Verbindung zum Modem herzustellen.

Speedtest ist ein nützliches Werkzeug. Wenn Sie einen Server in Alibaba Cloud verwenden und die Bandbreite auf 5 Mbps einstellen, dann wird die Verwendung der App zum Testen etwa 5 Mbps ergeben.

Das Interessante ist, dass, wenn Sie sowohl Wi-Fi als auch Ethernet verbinden, es keine Möglichkeit gibt, das eine gegenüber dem anderen zu priorisieren. Sie können in dieser Konfiguration nur Ethernet verwenden. Wenn Sie Wi-Fi verwenden möchten, müssen Sie den Ethernet-Adapter abziehen.

{: .centered }
![](assets/images/lightning/l1.jpg){: .responsive }
*Quelle: iOS*{: .caption }

{: .centered }
![](assets/images/lightning/l2.jpg){: .responsive }
*Quelle: Walmart.com*{: .caption }

{: .centered }
![](assets/images/lightning/n.jpg){: .responsive }
*Quelle: network_plot.py*{: .caption }