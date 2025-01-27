---
audio: true
lang: de
layout: post
title: Lightning zu Ethernet Adapter
translated: true
---

Ich habe kürzlich ein neues Produkt ausprobiert, das ich noch nie zuvor verwendet hatte. Es hat mich etwa 44 CNY auf JD.com gekostet. Ähnliche Produkte kosten auf Walmart.com etwa 15 USD.

Es funktioniert einwandfrei, und es sind keine zusätzlichen Einstellungen erforderlich. Ein "Ethernet"-Menüpunkt erscheint, nachdem der Adapter angeschlossen wurde.

Ich habe die Speedtest iOS-App verwendet, um die Geschwindigkeit zu testen. Die Ergebnisse sind unten dargestellt.

| Netzwerktyp                     | Entfernung   | Download-Geschwindigkeit (MBPS) | Upload-Geschwindigkeit (MBPS) | Verbindung             |
|----------------------------------|------------|-----------------------|---------------------|------------------|
| Modem -> TP-LINK Router -> Telefon | ca. 30m | 2.90                  | 4.82                | Guangzhou -> Macao |
| Modem -> Kabel -> Telefon          | ca. 30m | 84.9                  | 59.7                | Guangzhou -> Macao |

Dies ist ein etwas naiver Test. Ich vermute, dass ein Grund für den Unterschied in den Geschwindigkeiten darin liegt, dass die Verbindung vom Modem zum TP-LINK Router etwa 20m beträgt und die Verbindung vom TP-LINK Router zum Telefon etwa 10m. Zusätzlich verwendet der TP-LINK Router eine Wireless Bridge, um sich mit dem Modem zu verbinden.


{: .centered }
![](assets/images/lightning/l1.jpg){: .responsive }
*Quelle: iOS*{: .caption }

{: .centered }
![](assets/images/lightning/l2.jpg){: .responsive }
*Quelle: Walmart.com*{: .caption }

{: .centered }
![](assets/images/network_speed_chart.jpg){: .responsive }
*Quelle: network_plot.py*{: .caption }