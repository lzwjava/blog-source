---
audio: false
generated: false
lang: fr
layout: post
title: Analyse de la détection de VPN sur iOS par ChatGPT
translated: true
---

Aujourd'hui, j'ai découvert que l'application ChatGPT pour iOS permet désormais de se connecter avec un VPN en Chine. Auparavant, elle affichait un message de blocage, comme celui illustré ci-dessous.

Cependant, à ce jour, cela fonctionne correctement avec un VPN.

Je me souviens que lorsque l'application ChatGPT pour iOS a été lancée pour la première fois, l'utiliser avec un VPN ne posait aucun problème. Plus tard, la détection des VPN est devenue plus stricte, rendant la connexion difficile. Heureusement, il semble que cette restriction ait été assouplie récemment.

Après des tests supplémentaires, j'ai constaté qu'en utilisant un VPN de la région de Singapour de DigitalOcean, je ne pouvais pas accéder à l'application. Cependant, en utilisant des VPN de Taïwan ou du Royaume-Uni (fournis par https://zhs.cloud), cela fonctionnait parfaitement.

Il semble que la détection des VPN sur ChatGPT pour iOS soit basée sur des adresses IP spécifiques. Certains fournisseurs de services cloud ou certaines adresses IP sont interdits, ce qui pourrait expliquer le comportement incohérent en fonction de l'emplacement du serveur VPN.

![](assets/images/chatgpt/block.jpg){: .responsive }

![](assets/images/chatgpt/c1.png){: .responsive }