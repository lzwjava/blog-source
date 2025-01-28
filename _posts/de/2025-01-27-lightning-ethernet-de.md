---
audio: true
lang: de
layout: post
title: Blitz zu Ethernet Adapter
translated: true
---

Ich habe kürzlich ein neues Produkt ausprobiert, das ich noch nie zuvor verwendet hatte. Es kostete mich etwa 44 CNY auf JD.com. Ähnliche Produkte kosten etwa 15 USD auf Walmart.com.

Es funktioniert perfekt und es sind keine zusätzlichen Einstellungen erforderlich. Ein "Ethernet"-Menüpunkt erscheint nach dem Einstecken des Adapters.

Ich habe die Speedtest iOS-App verwendet, um die Geschwindigkeit zu testen. Die Ergebnisse sind unten dargestellt.

| Netzwerktyp                      | Entfernung | Download-Geschwindigkeit (MBPS) | Upload-Geschwindigkeit (MBPS) | Leitung             |
|----------------------------------|------------|---------------------------------|-------------------------------|---------------------|
| Modem -> TP-LINK Router -> Telefon | ca. 30m    | 2.90                            | 4.82                          | Guangzhou -> Macao  |
| Modem -> Kabel -> Telefon         | ca. 30m    | 84.9                            | 59.7                          | Guangzhou -> Macao  |

In einem Test sind die Ping-Antwortzeiten (ms) unten dargestellt:

| Metrik   | Wert  | Jitter |
|----------|-------|--------|
| Leerlauf | 33    | 68     |
| Download | 1885  | 110    |
| Upload   | 127   | 54     |

Dies ist ein etwas naiver Test. Ich vermute, dass ein Grund für den Unterschied in den Geschwindigkeiten ist, dass die Verbindung von Modem -> TP-LINK Router etwa 20m beträgt und die Verbindung von TP-LINK Router -> Telefon etwa 10m. Außerdem verwendet der TP-LINK Router eine drahtlose Brücke, um sich mit dem Modem zu verbinden.

Speedtest ist ein nützliches Tool. Wenn Sie einen Server in der Alibaba Cloud verwenden und die Bandbreite auf 5Mbps einstellen, liefert die Verwendung der App zum Testen Ergebnisse von etwa 5Mbps.

Interessant ist, dass es keine Möglichkeit gibt, eine Verbindung zu priorisieren, wenn sowohl Wi-Fi als auch Ethernet verbunden sind. Sie können in dieser Konfiguration nur Ethernet verwenden. Wenn Sie Wi-Fi verwenden möchten, müssen Sie den Ethernet-Adapter abziehen.

{: .centered }
![](assets/images/lightning/l1.jpg){: .responsive }
*Quelle: iOS*{: .caption }

{: .centered }
![](assets/images/lightning/l2.jpg){: .responsive }
*Quelle: Walmart.com*{: .caption }

{: .centered }
![](assets/images/lightning/n.jpg){: .responsive }
*Quelle: network_plot.py*{: .caption }