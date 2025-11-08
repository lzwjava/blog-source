---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Analyse du réseau CN1 de China Telecom
translated: true
type: note
---

D'après le traceroute que vous avez partagé depuis un WiFi du magasin de proximité Meiyijia à Guangzhou, il semble qu'il utilise le réseau principal standard de China Telecom, ChinaNet (souvent appelé CN1), et non le réseau premium CN2. Voici une analyse rapide des raisons :

### Indicateurs clés du Traceroute
- **Sauts 5–10 (réseau principal China Telecom)** : Les IP comme 14.147.135.198, 183.56.34.41, 202.97.93.89–202.97.116.210, et 203.215.237.42 font toutes partie de l'AS4134 (ChinaNet), le réseau principal national/international de China Telecom. Elles sont courantes sur les lignes haut débit standard.
  - La plage 202.97.x.x est spécifiquement ChinaNet (pas CN2).
  - 203.215.237.42 est situé à Xiamen, Fujian (toujours en Chine), et appartient à CHINANET Fujian Province Network (AS4134).
- **Aucune signature CN2** : Le réseau CN2 (AS4809) montre typiquement des IP dans des plages comme 59.43.0.0/16 ou 121.59.0.0/16 pendant la phase du réseau principal. Votre trace n'en contient aucune.
- **Chemin de sortie** : Le trafic quitte la Chine via une remise standard de ChinaNet à Microsoft (Azure) à Tokyo (saut 11 : 104.44.235.92), puis route vers le sud jusqu'à Singapour (sauts 14–15). C'est un chemin courant et non optimisé pour les connexions China Telecom basiques — le détour par le Japon ajoute environ 300ms de latence, ce qui correspond à la congestion du CN1. Le CN2 utilise souvent des sorties directes par Hong Kong ou des sorties Asie-Pacifique plus courtes pour une latence réduite (~150–200ms vers GitHub depuis Guangzhou).
- **Contexte** : Les magasins Meiyijia à Guangzhou utilisent généralement le haut débit grand public/commercial de China Telecom, qui utilise par défaut ChinaNet (CN1) sauf s'il est explicitement amélioré vers CN2 GIA (un module complémentaire payant pour les entreprises).

### Comparaison rapide CN1 vs. CN2

| Aspect          | CN1 (ChinaNet)                          | CN2 (Premium)                          |
|-----------------|-----------------------------------------|----------------------------------------|
| **Numéro AS**   | AS4134                                 | AS4809                                |
| **Latence typique vers GitHub (depuis Guangzhou)** | 250–400ms (congestionné, routes indirectes) | 100–200ms (optimisé, sorties directes)   |
| **Plages d'IP**   | 202.97.x.x, 183.56.x.x, etc.           | 59.43.x.x, 121.59.x.x, etc.           |
| **Cas d'usage**    | Haut débit standard domicile/entreprise       | VPS/cloud/entreprise (coût supplémentaire)     |
| **Style de chemin**  | Détourne souvent (ex: via Japon/Corée)  | Direct vers les hubs HK/US/Asie             |

Si vous souhaitez confirmer ou tester davantage :
- Exécutez `traceroute github.com` pendant les heures de pointe (par exemple, le soir) pour vérifier la présence de congestion.
- Faites un ping vers un site de test CN2 comme `www.cn2.net` — si la latence est inférieure à 200ms, vous pourriez avoir un accès partiel au CN2.
- Contactez le support de Meiyijia ou de China Telecom pour connaître le type de votre ligne (mentionnez "CN2 GIA" si vous souhaitez une amélioration).

[Présentation de China Telecom CN2](https://www.ctamericas.com/company/global-network/cn2/)  
[IPinfo pour 203.215.237.42](https://ipinfo.io/203.215.237.42)  
[Guide CN2 vs ChinaNet](http://chihengcloud.com/en/blog/cloudservice/what-is-cn2-network-a-3-minute-guide-to-types-and-features/)