---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Comprendre la Bascule SR
translated: true
type: note
---

### Qu'est-ce qu'une bascule SR ?
Une **bascule SR** (Set-Reset Latch) est un élément fondamental en électronique numérique et en architecture des ordinateurs. C'est un type de **flip-flop** qui stocke un seul bit d'information (0 ou 1) et le "mémorise" jusqu'à ce qu'il soit explicitement modifié par des signaux d'entrée. Le "SR" signifie **Set** (pour forcer la sortie à 1) et **Reset** (pour forcer la sortie à 0).

Une bascule SR de base est généralement construite en utilisant deux **portes NOR** (ou des portes NAND dans une variante) croisées. Voici un diagramme textuel simple de la version basée sur des NOR :

```
   S ───┐
        │ NOR1 ── Q
        │    │
   R ───┘    │
             │
             └─ NOR2 ── Q' (complément de Q)
                  │
                  └────── rétroaction vers NOR1
```

- **S** (Set) : Lorsqu'il est à l'état haut (1), met Q à 1.
- **R** (Reset) : Lorsqu'il est à l'état haut (1), met Q à 0.
- **Q** : La sortie stockée (la "mémoire").
- La boucle de rétroaction entre les portes permet au circuit de "verrouiller" l'état même après que S et R soient revenus à 0.

### Que signifie "Latch" (Bascule) ici ?
Le terme **bascule** (latch) fait référence à la capacité du circuit à **maintenir (ou "verrouiller") un état stable** dans le temps, sans avoir besoin d'une alimentation d'entrée continue pour le conserver. C'est comme un interrupteur qui reste en position après l'avoir actionné—jusqu'à ce que vous l'actionniez à nouveau.

- **Pas seulement abstrait** : Bien que "bascule" soit une idée conceptuelle en conception de logique numérique (une abstraction pour un comportement de mémoire), elle est implémentée comme un **circuit électrique réel**. Vous pouvez la construire avec des composants physiques comme des transistors ou des portes logiques sur une puce (par exemple, dans des circuits intégrés comme la série 7400).

- **Logique vs Circuit** : C'est les deux !
  - **Configuration logique** : En théorie, c'est un modèle de logique booléenne où les sorties dépendent des entrées et de la rétroaction (par exemple, Q = ¬(S ∨ ¬Q) dans la version NOR).
  - **Circuit électrique** : En pratique, c'est un matériel câblé qui fonctionne avec des niveaux de tension (par exemple, une logique 5V). Les portes sont alimentées par l'électricité, et les signaux se propagent sous forme de courants/tensions.

### Est-ce un concept abstrait ?
Oui, partiellement—**bascule** est un **modèle abstrait** en informatique et en conception numérique, représentant la forme la plus simple de mémoire bistable (deux états stables). Mais il est ancré dans la physique : le circuit exploite l'hystérésis électronique (rétroaction) pour stocker l'état. Sans le circuit physique, l'abstraction ne fonctionnerait pas.

Si vous le simulez ou l'étudiez :
- Utilisez des outils comme Logisim ou Tinkercad pour un circuit virtuel.
- Table de vérité pour la bascule SR (version NOR) :

| S | R | Q (suivant) | Q' (suivant) | Description     |
|---|----|-------------|--------------|-----------------|
| 0 | 0  | Q (préc.)   | Q' (préc.)   | Maintien (verrouillage) |
| 0 | 1  | 0           | 1            | Reset           |
| 1 | 0  | 1           | 0            | Set             |
| 1 | 1  | ?           | ?            | Invalide (condition de course)  |

Ce comportement de "maintien" lorsque S=R=0 est ce qui en fait une bascule—c'est de la mémoire !

Pour des approfondissements, consultez des ressources comme "Digital Design" de Morris Mano. Si vous avez un diagramme spécifique ou une simulation en tête, partagez plus de détails !