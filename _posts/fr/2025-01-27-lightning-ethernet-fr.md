---
audio: true
lang: fr
layout: post
title: Adaptateur Lightning vers Ethernet
translated: true
---

J'ai récemment essayé un nouveau produit que je n'avais jamais utilisé auparavant. Il m'a coûté environ 44 CNY sur JD.com. Des produits similaires coûtent environ 15 USD sur Walmart.com.

Il fonctionne parfaitement, et aucun réglage supplémentaire n'est nécessaire. Un élément de menu "Ethernet" apparaît après avoir branché l'adaptateur.

J'ai utilisé l'application Speedtest sur iOS pour tester la vitesse. Les résultats sont présentés ci-dessous.

| Type de réseau                     | Distance   | Vitesse de téléchargement (MBPS) | Vitesse de téléversement (MBPS) | Ligne             |
|----------------------------------|------------|-----------------------|---------------------|------------------|
| Modem -> Routeur TP-LINK -> Téléphone | environ 30m | 2.90                  | 4.82                | Guangzhou -> Macao |
| Modem -> Câble -> Téléphone          | environ 30m | 84.9                  | 59.7                | Guangzhou -> Macao |

Dans un test, les résultats de réactivité du ping (ms) sont présentés ci-dessous :

| Métrique   | Valeur | Jitter |
|----------|-------|--------|
| Inactif     | 33    | 68     |
| Téléchargement | 1885  | 110    |
| Téléversement   | 127   | 54     |

Il s'agit d'un test quelque peu naïf. Je soupçonne qu'une des raisons de la différence de vitesses est que la connexion entre le Modem et le Routeur TP-LINK est d'environ 20m, et la connexion entre le Routeur TP-LINK et le Téléphone est d'environ 10m. De plus, le Routeur TP-LINK utilise un pont sans fil pour se connecter au modem.

Ce qui est intéressant, c'est que si vous connectez à la fois le Wi-Fi et l'Ethernet, il n'y a aucun moyen de privilégier l'un par rapport à l'autre. Vous ne pouvez utiliser que l'Ethernet dans cette configuration. Si vous souhaitez utiliser le Wi-Fi, vous devez débrancher l'adaptateur Ethernet.

{: .centered }
![](assets/images/lightning/l1.jpg){: .responsive }
*Source : iOS*{: .caption }

{: .centered }
![](assets/images/lightning/l2.jpg){: .responsive }
*Source : Walmart.com*{: .caption }

{: .centered }
![](assets/images/lightning/n.jpg){: .responsive }
*Source : network_plot.py*{: .caption }