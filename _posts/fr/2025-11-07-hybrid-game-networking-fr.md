---
audio: false
generated: true
image: false
lang: fr
layout: post
model: moonshotai/kimi-k2-thinking
title: Réseautage Hybride pour le Développement de Jeux
translated: true
type: note
---

Vous avez raison — l'explication de la Personne B est parfaitement juste.

Ce n'est **pas redondant** car la **fiabilité sélective** offre aux développeurs de jeux exactement ce dont ils ont besoin : un contrôle précis du comportement réseau. Voici pourquoi cette approche hybride est logique :

### Le Compromis
- **TCP** : Garantit la livraison et l'ordre, mais ses mécanismes de retransmission et de contrôle de congestion introduisent de la latence — ce qui est inacceptable pour les jeux au rythme rapide.
- **UDP simple** : Rapide et sans ordre, mais totalement non fiable — problématique pour les événements de jeu critiques.

### La Fiabilité Sélective sur UDP
Les jeux peuvent choisir précisément ce qui a besoin de garanties et ce qui n'en a pas besoin :

**Fiable (Ordonné, Accusé de réception)**
- Actions du joueur : tirer, activation de capacité
- Changements d'état du jeu : ramassage d'objets, mort d'un joueur, mise à jour du score
- Prévention de la triche : vérification des transactions

**Non fiable (Meilleur effort)**
- Mises à jour de position/rotation : le nouveau paquet remplace les anciens
- Chat vocal : une perte occasionnelle est tolérable
- Effets de particules, éléments visuels non critiques

### Exemples Concrets
- **Quake III Arena** (et de nombreux jeux FPS depuis)
- La bibliothèque **ENet** (populaire dans le milieu des jeux indé multi-joueurs)
- **RakNet** (utilisé dans *Minecraft* avant son rachat par Microsoft)

Cette approche évite le **blocage en tête de ligne** (où un seul paquet perdu bloque tous ceux qui le suivent) tout en garantissant l'arrivée des données critiques. C'est le meilleur des deux mondes pour les applications interactives en temps réel où chaque milliseconde compte.