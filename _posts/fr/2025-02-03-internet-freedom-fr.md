---
audio: true
lang: fr
layout: post
title: Le chemin vers la liberté d'internet
translated: true
---

## Voyage

De 2010 à 2013, j'ai utilisé Goagent et l'outil proxy SwitchyOmega pour contourner le GFW.

Entre 2014 et 2015, j'ai utilisé Qujing (曲径) pour le proxy et j'ai suivi son auteur sur Twitter, qui vit maintenant au Japon.

De juin 2016 à juillet 2018, j'ai utilisé Digital Ocean pour héberger mon serveur proxy shadowsocks.

À partir de 2019, j'ai commencé à utiliser https://zhs.cloud.

En mars 2023, j'ai commencé à utiliser une carte SIM de Macao dans mon téléphone portable pour accéder à internet sans proxy ni VPN. Cela coûtait environ 150 CNY par mois pour 20 Go de données cellulaires, et j'ai utilisé cette méthode pendant environ un an.

En 2024, j'ai recommencé à utiliser Outline Manager avec mon serveur proxy shadowsocks, en expérimentant avec différents fournisseurs de cloud.

Actuellement, ma configuration préférée est Outline Manager avec un serveur Aliyun Hong Kong pour l'utilisation quotidienne et un serveur non-Hong Kong (comme Singapour ou le Japon) pour les outils d'IA. Je conserve la même configuration des règles de proxy utilisée dans Shadowrocket ou Clash.

## La différence par rapport à l'inversion de la myopie

Un défi consiste à lutter contre le GFW, qui est d'origine humaine. L'autre consiste à aborder les principes de la fonction musculaire oculaire.

Il est facile de mesurer l'efficacité d'une solution proxy. Cependant, inverser la myopie nécessite du temps pour déterminer si le globe oculaire change.

## Similitudes avec l'inversion de la myopie

Une similitude est que tant une solution proxy que des lunettes avec une réduction de 200 degrés fonctionnent souvent bien. L'une implique l'accès à internet, l'autre l'amélioration de la vue. Les deux s'attaquent à des problèmes très importants.

Le principe sous-jacent est que si nous comprenons comment fonctionne le GFW et trouvons un moyen de le contourner, la solution devrait être simple.

## Raisonnement et nuances

Je ne comprends toujours pas parfaitement comment fonctionne le GFW. Lorsque l'IP de mon serveur proxy est bloquée, j'ai maintenant plus de moyens d'enquêter sur la cause.

Je peux vérifier si le blocage se produit sur le réseau cellulaire ou le haut débit domestique. S'il s'agit du réseau cellulaire, je peux vérifier s'il s'agit de la 4G ou de la 5G.

De même, si ma myopie ne s'améliore pas après six mois ou un an, je dois étudier s'il existe des différences entre mes yeux. Je dois également considérer si j'ai vu des choses à peine clairement sans forcer mes yeux pendant la majeure partie de l'année.

## Situation actuelle

Mon serveur proxy fonctionne actuellement très bien. Les vitesses de téléchargement sur mon téléphone atteignent 80 Mbps, et les vitesses de téléchargement atteignent 50 Mbps lors de la connexion au serveur proxy de Hong Kong. Il en va de même pour mon ordinateur portable.

J'utilise les mêmes configurations proxy sur mon ordinateur portable et mes téléphones, et elles fonctionnent parfaitement. Normalement, j'utilise un serveur proxy pour visiter des sites en dehors de la Chine, et j'utilise un serveur non-HK pour les outils d'IA.

## Récupération

Si les choses sont cassées, ma méthode de récupération est simple. Je n'ai qu'à changer l'IP élastique de mon serveur proxy Aliyun Hong Kong et à télécharger la nouvelle URL proxy sur le stockage cloud. Cela signifie que je dois exécuter deux scripts, ce qui prend environ une minute, et mon ordinateur portable et mes téléphones peuvent mettre à jour l'adresse du serveur proxy.

## Regret

J'ai trop souvent et trop longtemps combattu le GFW. J'ai essayé de nombreux protocoles proxy, sachant qu'ils seraient détectés par le GFW et interdits. Sans serveur proxy fiable, il est difficile de configurer un proxy sur un routeur OpenWrt.

Je regrette de ne pas avoir appris plus tôt les techniques des fournisseurs de proxy, comme [zhs.cloud](https://zhs.cloud). Je connais maintenant la plupart de leurs secrets.

L'autre chose est que chaque fois que mon serveur proxy était banni, je n'y réfléchissais pas trop. Il semblait qu'il suffisait de configurer un nouveau serveur proxy pour obtenir une nouvelle adresse IP qui n'avait pas été bannie. Mais c'était une pensée superficielle.

## Métriques

Je regrette de ne pas avoir utilisé Speedtest plus tôt. Je connaissais le nom de l'outil depuis longtemps, mais je n'ai pas appris à l'utiliser correctement.

Il est bon d'utiliser Speedtest fréquemment lors de la connexion à des stations de signal mobile 5G ou 4G ou à un réseau haut débit domestique.

Pour inverser la myopie, c'est la même chose. J'ai acheté une table d'examen visuelle en C et une table d'examen visuelle standard.

Pas de mesure, pas d'amélioration. Mesurer les choses vous aide à apprendre. L'utilisation fréquente de Speedtest m'aide à constater que sur un réseau 5G, il est facile de dépasser 100 Mbps, tandis que sur un réseau haut débit domestique, il est difficile de dépasser 100 Mbps.

## Il est encore tôt

Le mur du GFW tombera-t-il dans les prochaines années ? C'est difficile à dire.

Lorsque, après avoir inversé ma myopie pendant deux ans, j'ai dit à mon ami que ma méthode d'inversion devait être améliorée et que je devais porter des lunettes avec 200 degrés de moins que mon ordonnance réelle au lieu de 150 degrés de moins.

Il a dit que ce n'était pas un problème, que c'était bien, pas une perte de temps, et que c'était encore tôt. Oui. Ces choses sont fondamentales. Comme la myopie, les gens devraient la découvrir plus tôt. Todd Becker a partagé cette découverte sur YouTube en 2014, et les vidéos ont gagné plus d'un million de vues. Et maintenant, nous sommes en 2025, combien de personnes le savent vraiment dans le monde ? Je suppose que ce sera moins de 10 000.
