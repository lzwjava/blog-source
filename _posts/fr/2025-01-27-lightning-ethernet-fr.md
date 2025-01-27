---
audio: true
lang: fr
layout: post
title: Adaptateur Lightning vers Ethernet
translated: true
---

J'ai récemment essayé un nouveau produit que je n'avais jamais utilisé auparavant. Il m'a coûté environ 44 CNY sur JD.com. Des produits similaires coûtent environ 15 USD sur Walmart.com.

Il fonctionne parfaitement, et aucun réglage supplémentaire n'est nécessaire. Un élément de menu "Ethernet" apparaît après avoir branché l'adaptateur.

J'ai utilisé l'application iOS Speedtest pour tester la vitesse. Les résultats sont présentés ci-dessous.

| Type de réseau                     | Distance   | Vitesse de téléchargement (MBPS) | Vitesse de téléversement (MBPS) | Ligne             |
|----------------------------------|------------|-----------------------|---------------------|------------------|
| Modem -> Routeur TP-LINK -> Téléphone | environ 30m | 2.90                  | 4.82                | Guangzhou -> Macao |
| Modem -> Câble -> Téléphone          | environ 30m | 84.9                  | 59.7                | Guangzhou -> Macao |

Il s'agit d'un test quelque peu naïf. Je soupçonne qu'une des raisons de la différence de vitesse est que la connexion entre le Modem et le Routeur TP-LINK est d'environ 20m, et la connexion entre le Routeur TP-LINK et le Téléphone est d'environ 10m. De plus, le Routeur TP-LINK utilise un pont sans fil pour se connecter au modem.


{: .centered }
![](assets/images/lightning/l1.jpg){: .responsive }
*Source : iOS*{: .caption }

{: .centered }
![](assets/images/lightning/l2.jpg){: .responsive }
*Source : Walmart.com*{: .caption }

{: .centered }
![](assets/images/network_speed_chart.jpg){: .responsive }
*Source : network_plot.py*{: .caption }