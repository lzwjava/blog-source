---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Principes et applications du code Gray
translated: true
type: note
---

### Qu'est-ce que le code Gray ?

Le code Gray (également appelé code binaire réfléchi) est un système de numération binaire conçu pour que **deux valeurs consécutives (ou adjacentes) diffèrent par exactement un bit**. Cette propriété minimise les erreurs pendant les transitions, car un seul bit doit changer lors du passage d'un nombre au suivant. Il est particulièrement utile dans des applications comme :
- Les **codeurs rotatifs** (par exemple, dans les dispositifs mécaniques comme les boutons ou les roues, où la position change progressivement).
- La **détection/correction d'erreurs** dans les communications numériques.
- Les **tableaux de Karnaugh** en conception de logique numérique pour simplifier l'algèbre de Boole.

Contrairement au code binaire standard, où des nombres adjacents peuvent différer par plusieurs bits (ce qui peut provoquer des "parasites" ou des erreurs), le code Gray garantit des transitions fluides à un seul bit.

### Fonctionnement du code Gray
La règle clé est : **Deux codes successifs quelconques diffèrent par une seule position de bit**.

#### Exemple simple : Séquence de code Gray sur 2 bits (pour les nombres 0 à 3)
Voici une comparaison entre le binaire standard et le code Gray :

| Décimal | Binaire Standard | Code Gray | Différence de bit par rapport au précédent |
|---------|------------------|-----------|---------------------------------------------|
| 0       | 00               | 00        | (Point de départ)                           |
| 1       | 01               | 01        | 1 bit (le moins significatif)               |
| 2       | 10               | 11        | 1 bit (le moins significatif)               |
| 3       | 11               | 10        | 1 bit (le plus significatif)                |

- En **binaire standard**, la transition de 1 (01) à 2 (10) bascule *deux* bits, ce qui pourrait causer des erreurs.
- En **code Gray**, chaque étape bascule *exactement un* bit, ce qui correspond à votre description de "deux codes continus ne diffèrent que par un seul élément".

#### Génération du code Gray
Vous pouvez convertir le binaire en code Gray en utilisant une simple opération XOR :
- Gray(n) = n XOR (n >> 1) (où >> est un décalage à droite de 1 bit).

Par exemple :
- Binaire 2 (10 en décimal) : 10 XOR 01 = 11 (code Gray pour 2).
- Pour revenir en arrière : Binaire(n) = Gray(n) XOR (Gray(n) >> 1).

Ce modèle peut être étendu à n'importe quel nombre de bits (par exemple, 3 bits, 4 bits, etc.), en maintenant toujours la propriété de différence à un seul bit.

Si vous avez un cas d'utilisation spécifique ou souhaitez des exemples pour plus de bits, faites-le-moi savoir !