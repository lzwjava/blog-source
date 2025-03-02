---
audio: false
generated: true
lang: fr
layout: post
title: Routeur Mesh
translated: true
---

## TP-Link AX3000 - TL-XDR 3050

J'ai commencé à utiliser un routeur maillé en 2023. J'ai acheté un système TP-Link AX3000 composé de deux routeurs maillés : une unité principale et une unité satellite. Cela m'a coûté environ 484 CNY à l'époque, mais maintenant, il ne coûte que 395 CNY sur JD.com.

J'ai initialement utilisé ce système dans ma grande maison, mais je l'ai ensuite déplacé chez mes parents.

## ZTE AC1200

Pendant quelques jours du Nouvel An chinois 2025, ma famille est restée dans ma grande maison et a de nouveau connu une mauvaise qualité de réseau WiFi. Pour remédier à cela, j'ai acheté un autre routeur maillé, le ZTE AC1200, qui coûte environ 108 CNY.

Des produits similaires disponibles chez Walmart incluent le routeur maillé WiFi TP-Link, le routeur maillé double bande Eero et le NetGear Nighthawk AX3000. Les prix de la plupart de ces produits varient entre 50 USD et 200 USD.

Pour le routeur maillé ZTE AC1200, je pouvais simplement en acheter un et utiliser le mode pont, lui permettant de recevoir un signal WiFi et ensuite d'émettre son propre signal WiFi. Cela fonctionne parfaitement. À l'origine, l'adresse du domaine du routeur était 192.168.5.1. Après avoir activé le mode pont, cette adresse IP n'est plus accessible. Au lieu de cela, 192.168.1.1 vous redirigera vers le routeur principal de votre réseau domestique. À ce stade, vous pouvez accéder au centre de contrôle du routeur en naviguant vers http://zte.home.

Si vous pouvez accéder au routeur principal, vous pouvez voir les appareils connectés et leurs adresses IP. Ensuite, vous pouvez essayer d'accéder à chaque appareil pour déterminer lequel est le sous-routeur. Dans mon cas, c'était 192.168.1.23, qui est l'adresse du routeur maillé ZTE AC1200.

Pour les téléphones portables, que nous déplaçons dans la maison, il est préférable d'utiliser le canal 2,4 GHz car il est plus stable. Pour les ordinateurs portables ou de bureau, que nous utilisons généralement dans nos chambres ou bureaux, il est préférable d'utiliser le canal 5 GHz car il est plus rapide.

Après l'avoir utilisé pendant plusieurs jours, je trouve qu'il est un peu médiocre. La vitesse ou le signal est moins bon que celui du TL-XDR 3050.

{: .centered }
![](assets/images/cable-tester/zte.jpg){: .responsive }
*Source : JD.com*{: .caption }

{: .centered }
![](assets/images/cable-tester/netgear.jpg){: .responsive }
*Source : Walmart.com*{: .caption }

## Alimentation 12V pour les routeurs

Un câble élévateur de tension USB peut être utilisé pour alimenter les routeurs à l'aide d'une batterie externe.

Cependant, dans certains cas, le câble élévateur d'une batterie externe peut ne pas être en mesure de configurer correctement le routeur. Le routeur peut redémarrer continuellement.

{: .centered }
![](assets/images/cable-tester/12v.jpg){: .responsive }
*Source : JD.com*{: .caption }

## Deux façons d'aider un sous-routeur à trouver le routeur principal

Parfois, un sous-routeur ne peut pas facilement trouver le routeur principal lorsque le signal est faible.

Si nous devons placer le sous-routeur loin du routeur principal, je me demande s'il est plus rapide de le connecter d'abord à un endroit proche, puis de le déplacer plus loin, plutôt que d'essayer de le connecter lorsqu'il est déjà dans un endroit éloigné.

Maintenir une connexion lorsqu'ils sont proches leur permet de communiquer entre eux. J'ai trouvé cette méthode plus efficace.