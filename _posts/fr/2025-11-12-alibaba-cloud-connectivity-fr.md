---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Options de Connectivité Internationale d'Alibaba Cloud
translated: true
type: note
---

Oui, vous pouvez acheter des serveurs (spécifiquement des instances ECS) sur Alibaba Cloud (Aliyun) qui prennent en charge une connectivité internationale haut débit, y compris des options qui utilisent des routes premium similaires à CN2 pour de meilleures performances sortantes de la Chine continentale vers l'étranger. Cependant, ce n'est pas toujours explicitement étiqueté "CN2" dans les régions continentales comme `cn-guangzhou`, et la disponibilité peut dépendre de votre configuration. Voici une répartition basée sur les offres actuelles :

### Options en Chine Continentale (ex : Région de cn-guangzhou)
- Les instances ECS d'Alibaba Cloud dans les régions continentales utilisent par défaut un réseau multi-ligne BGP, qui se connecte aux principaux opérateurs comme China Telecom, China Unicom et China Mobile. Cela peut emprunter des chemins premium, y compris CN2 (l'épine dorsale internationale haut de gamme de China Telecom), mais ce n'est pas garanti pour chaque instance — cela dépend du routage du trafic et de l'optimisation de l'opérateur.
- Pour une optimisation haut débit sortante vers l'étranger (ce que vous appelez "export port"), vous pouvez activer **Global Internet Access (GIA)**. Ce service fournit des liaisons dédiées et premium entre la Chine continentale et les destinations internationales, réduisant la latence (souvent à ~1ms pour le trafic transfrontalier) et améliorant la vitesse/la fiabilité. Il est conçu exactement pour des scénarios comme le vôtre, où vous avez besoin de connexions rapides depuis la Chine.
  - Comment le configurer : Achetez une instance ECS dans la région `cn-guangzhou` (idéale puisque vous êtes à Guangzhou pour une faible latence locale). Ensuite, associez une IP Élastique (EIP) avec une bande passante premium via la Passerelle NAT. Activez GIA sur l'EIP pour un routage international amélioré.
  - Bande passante : Vous pouvez monter en charge jusqu'à des débits élevés (ex : 100 Mbps+), avec une tarification à la demande ou par abonnement. Le débit sortant de pointe peut être limité (ex : 30 Mbps sur certains plans de base), mais les options premium permettent d'aller plus haut.
  - Coût : Démarre à un prix bas pour l'ECS de base (ex : ~5-10$/mois pour l'entrée de gamme), mais la bande passante premium ajoute des coûts basés sur l'utilisation.
- Note : Si votre objectif est purement d'avoir un haut débit vers l'étranger, les instances en Chine continentale peuvent toujours subir des ralentissements liés au GFW ou une congestion sur les routes non-premium. GIA aide à atténuer ce problème.

### Alternative de la Région de Hong Kong (Recommandée pour une Garantie CN2)
- Si vous voulez une connectivité CN2 explicite, optez pour la région Chine (Hong Kong) (`cn-hongkong`). Alibaba Cloud y annonce des lignes CN2 pour une bande passante internationale premium, optimisée pour un débit sortant rapide de la Chine vers les destinations globales (contournant certains problèmes de routage du continent).
  - Pourquoi cela convient : Guangzhou est très proche de HK, donc votre accès local au serveur aurait une latence minimale (~10-20ms). C'est essentiellement "depuis la Chine" mais avec de meilleures vitesses de sortie vers l'étranger.
  - Configuration : Achetez une instance ECS dans `cn-hongkong`, et sélectionnez une EIP premium. CN2 est intégré pour le trafic international.
  - C'est une option populaire pour les utilisateurs du sud de la Chine ayant besoin d'un accès global haut débit, car HK n'est pas soumis aux mêmes restrictions continentales.

### Comment Acheter
1. Connectez-vous à votre compte Aliyun (ou créez-en un sur aliyun.com/international pour la version globale).
2. Allez dans la console ECS, sélectionnez la région (`cn-guangzhou` pour le continent ou `cn-hongkong` pour une garantie CN2).
3. Choisissez le type d'instance, l'OS et la bande passante (sélectionnez les options premium/internationales lors de la configuration de l'EIP).
4. Pour GIA en Chine continentale : Activez-le via la Passerelle NAT ou la console EIP après la création de l'instance.
- Si vous êtes nouveau, une vérification d'identité en temps réel est requise pour les ressources en Chine continentale.
- Testez les vitesses après la configuration en utilisant des outils comme speedtest.net vers des serveurs à l'étranger.

Si vous avez besoin des meilleures vitesses absolues vers l'étranger et qu'un petit saut ne vous dérange pas, HK avec CN2 est la solution. Pour une solution strictement en Chine continentale, GIA s'en approche avec un routage premium.

Références :  
[Global Internet Access - Alibaba Cloud](https://www.alibabacloud.com/en/solutions/global-internet-access)  
[Tips for an SSR server on Alibaba Cloud](https://www.tipsforchina.com/tips-for-alibaba-hong-kong-aliyun.html)  
[Alibaba mainland China VPS feedback - LowEndTalk](https://lowendtalk.com/discussion/111525/alibaba-mainland-china-vps-feedback)  
[What cloud service providers work well in both China and the US? - Quora](https://www.quora.com/What-cloud-service-providers-work-well-in-both-China-and-the-US)  
[Lower the latency of your application in China with BGP Pro](https://albertoroura.com/lower-the-latency-of-your-application-in-china-with-bgp-pro/)