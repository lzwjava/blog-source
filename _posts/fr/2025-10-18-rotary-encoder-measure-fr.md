---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Codeurs rotatifs mesurent la rotation
translated: true
type: note
---

### Qu'est-ce qu'un codeur rotatif ?

Un **codeur rotatif** est un type de capteur électromécanique utilisé pour détecter et mesurer la position angulaire ou la rotation d'un arbre (comme dans les boutons, les cadrans ou les roues) dans les dispositifs mécaniques. Il convertit le mouvement de rotation en signaux numériques ou analogiques, permettant aux appareils de suivre l'amplitude et la direction d'une rotation. Ils sont courants dans de nombreuses applications, allant des boutons de volume sur les équipements audio aux volants dans la robotique et les machines industrielles.

#### Types principaux
Il existe deux types principaux, basés sur leur méthode de suivi de position :

| Type              | Description | Idéal pour |
|-------------------|-------------|----------|
| **Incrémental**  | Émet des impulsions (ou "ticks") pour chaque petit changement de rotation, comptant les pas par rapport à un point de départ. La position est calculée en suivant ces changements dans le temps. | Les mouvements continus et graduels comme les molettes de défilement ou la rétroaction des moteurs où la position absolue n'est pas critique. |
| **Absolu**     | Fournit un code numérique unique pour chaque position angulaire possible, il connaît donc la position exacte même après une perte de puissance. | Les applications de précision comme les ascenseurs ou les machines CNC où il est essentiel de connaître la position "d'origine" sans réinitialisation. |

#### Comment cela fonctionne (version simplifiée)
- **Optique** : Une source lumineuse éclaire à travers un disque à motifs (avec des fentes ou des marques) fixé à l'arbre rotatif. Un capteur détecte les interruptions de la lumière pour générer des signaux.
- **Magnétique** : Utilise des aimants et des capteurs à effet Hall pour détecter les changements dans les champs magnétiques lorsque l'arbre tourne.
- **Mécanique** : Style plus ancien avec des contacts directs, mais moins fiable en raison de l'usure.

Les "changements de position graduels" que vous avez mentionnés correspondent parfaitement aux codeurs rotatifs incrémentaux, car ils excellent à détecter les rotations fluides et incrémentales sans avoir besoin de se réinitialiser.

Si ce n'est pas tout à fait ce que vous entendiez par "qu'est-ce que c'est ?" (par exemple, si vous pensez à un dispositif spécifique ou à une comparaison), n'hésitez pas à clarifier !