---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Proton Permet de Jouer aux Jeux Windows sur Linux
translated: true
type: note
---

### Qu'est-ce que Proton ?

Proton est une couche de compatibilité développée par Valve, intégrée directement au client Steam, qui permet aux jeux et applications exclusifs à Windows de fonctionner de manière transparente sur les systèmes basés sur Linux (comme SteamOS sur le Steam Deck ou les distributions Linux standard). C'est essentiellement la solution intégrée de Steam pour le « Linux via Proton », permettant aux utilisateurs de jouer à une vaste bibliothèque de jeux PC sans avoir besoin d'une installation Windows ou d'une configuration en double amorçage.

#### Comment ça marche ?
- **Technologie de base** : Proton est construit sur Wine (une couche de compatibilité gratuite qui traduit les appels d'API Windows en équivalents Linux) mais est amélioré avec des ajustements spécifiques à Valve, incluant la traduction de DirectX vers Vulkan via DXVK et VKD3D. Cela le rend plus efficace pour le jeu.
- **Intégration Steam** : Dans Steam, il suffit de faire un clic droit sur un jeu, d'aller dans Propriétés > Compatibilité et d'activer « Forcer l'utilisation d'un outil de compatibilité Steam Play spécifique » (en sélectionnant une version de Proton). Steam s'occupe du reste — téléchargeant Proton si nécessaire et lançant le jeu comme s'il était natif sous Linux.
- **Versions** : Proton existe en versions expérimentale et stable. En 2025, la dernière version stable (par exemple, Proton 9.x ou supérieure) prend en charge des milliers de titres avec des notes « Platinum » ou « Gold » sur ProtonDB (une base de données communautaire pour les rapports de compatibilité).

#### Avantages pour le jeu sous Linux
- **Facilité d'utilisation** : Aucune configuration manuelle requise pour la plupart des jeux — c'est du « plug-and-play » dans Steam.
- **Performances** : Atteint ou dépasse souvent les performances natives de Windows sur Linux grâce à des optimisations, notamment sur du matériel comme les GPU AMD. Il peut même faire fonctionner certains jeux mieux sur les appareils portables Linux que sur des configurations Windows équivalentes.
- **Impact sur l'écosystème** : Proton a fait de Linux une plateforme de jeu viable, alimentant des appareils comme le Steam Deck et contribuant à une adoption plus large des technologies open source dans le jeu vidéo.

Si vous le configurez, assurez-vous que votre distribution Linux a les pilotes Vulkan installés (par exemple, via Mesa pour AMD/Intel). Pour le dépannage, consultez ProtonDB pour des conseils spécifiques à chaque jeu.

#### Références
- [Dépôt GitHub de Proton par Valve](https://github.com/ValveSoftware/Proton)
- [Guide de la communauté Steam : Proton 101](https://steamcommunity.com/app/221410/discussions/0/1636417404917541481/)
- [Docs Rocky Linux : Jouer sous Linux avec Proton](https://docs.rockylinux.org/10/desktop/gaming/proton/)