---
audio: false
generated: true
lang: fr
layout: post
title: Expérience et Table d'État de la Bascule JK
translated: true
type: note
---

**42. Expérience de la Bascule JK - Horloge à Déclenchement Monostable**
- **Objectif** : Comprendre le principe de fonctionnement et les caractéristiques d'une bascule JK.
- **Matériel** : Module de bascule JK, générateur d'impulsions, alimentation, fils de connexion, etc.

**Tableau 42 de Transition d'État**

| Q₂ⁿ | Q₁ⁿ | Q₀ⁿ | Q₂ⁿ⁺¹ | Q₁ⁿ⁺¹ | Q₀ⁿ⁺¹ | Z |
|-----|-----|-----|-------|-------|-------|---|
| 0   | 0   | 0   | 0     | 0     | 1     | 0 |
| 0   | 0   | 1   | 0     | 1     | 0     | 0 |
| 0   | 1   | 0   | 0     | 1     | 1     | 0 |
| 0   | 1   | 1   | 1     | 0     | 0     | 0 |
| 1   | 0   | 0   | 0     | 0     | 0     | 1 |

### Réponse :
Le tableau représente la transition d'état d'une bascule JK 3 bits où Q₂ⁿ, Q₁ⁿ et Q₀ⁿ sont les états actuels, et Q₂ⁿ⁺¹, Q₁ⁿ⁺¹ et Q₀ⁿ⁺¹ sont les états suivants après une impulsion d'horloge. La sortie Z est 1 uniquement lorsque l'état actuel est 100, indiquant une condition spécifique ou un signal de sortie. Ce comportement est typique d'une bascule JK, qui peut maintenir, mettre à 1, remettre à 0 ou basculer son état en fonction des entrées (J et K) et de l'impulsion d'horloge.

Analysons en détail le tableau de transition d'état de la bascule JK et expliquons son comportement.

### Aperçu d'une Bascule JK
Une bascule JK est un type de circuit logique séquentiel utilisé en électronique numérique pour stocker un seul bit de données. Elle possède deux entrées, J et K, une entrée d'horloge (CLK) et deux sorties, Q (l'état actuel) et Q' (le complément de Q). La bascule JK est une amélioration de la bascule SR car elle élimine l'état "invalide" (lorsque les deux entrées sont à 1). Son comportement est le suivant :

- **J = 0, K = 0** : Aucun changement (Q reste identique).
- **J = 0, K = 1** : Remise à zéro (Q devient 0).
- **J = 1, K = 0** : Mise à un (Q devient 1).
- **J = 1, K = 1** : Basculement (Q passe à l'état opposé).

Le tableau de l'image représente un système avec trois bascules JK (Q₂, Q₁, Q₀), formant une machine à états 3 bits, où Q₂ⁿ, Q₁ⁿ et Q₀ⁿ sont les états actuels, et Q₂ⁿ⁺¹, Q₁ⁿ⁺¹ et Q₀ⁿ⁺¹ sont les états suivants après une impulsion d'horloge. Z est un signal de sortie basé sur l'état actuel.

### Explication du Tableau de Transition d'État
Le tableau montre comment le système transitionne entre les états et quand la sortie Z est activée. Analysons chaque ligne :

| Q₂ⁿ | Q₁ⁿ | Q₀ⁿ | Q₂ⁿ⁺¹ | Q₁ⁿ⁺¹ | Q₀ⁿ⁺¹ | Z |
|-----|-----|-----|-------|-------|-------|---|
| 0   | 0   | 0   | 0     | 0     | 1     | 0 |
| 0   | 0   | 1   | 0     | 1     | 0     | 0 |
| 0   | 1   | 0   | 0     | 1     | 1     | 0 |
| 0   | 1   | 1   | 1     | 0     | 0     | 0 |
| 1   | 0   | 0   | 0     | 0     | 0     | 1 |

#### Ligne 1 : État 000 → 001, Z = 0
- **État Actuel (Q₂ⁿ, Q₁ⁿ, Q₀ⁿ)** : 000 (décimal 0)
- **État Suivant (Q₂ⁿ⁺¹, Q₁ⁿ⁺¹, Q₀ⁿ⁺¹)** : 001 (décimal 1)
- **Sortie Z** : 0
- **Explication** : Le système commence à l'état 000. Après une impulsion d'horloge, Q₀ bascule de 0 à 1 (probablement parce que J₀ = 1, K₀ = 1), tandis que Q₁ et Q₂ restent à 0 (possiblement J₁ = 0, K₁ = 0 ; J₂ = 0, K₂ = 0). Z est à 0, indiquant que la condition de sortie n'est pas remplie.

#### Ligne 2 : État 001 → 010, Z = 0
- **État Actuel** : 001 (décimal 1)
- **État Suivant** : 010 (décimal 2)
- **Sortie Z** : 0
- **Explication** : À partir de l'état 001, Q₀ bascule de 1 à 0 (J₀ = 1, K₀ = 1), Q₁ bascule de 0 à 1 (J₁ = 1, K₁ = 1), et Q₂ reste à 0. Z reste à 0.

#### Ligne 3 : État 010 → 011, Z = 0
- **État Actuel** : 010 (décimal 2)
- **État Suivant** : 011 (décimal 3)
- **Sortie Z** : 0
- **Explication** : À partir de l'état 010, Q₀ bascule de 0 à 1 (J₀ = 1, K₀ = 1), Q₁ reste à 1, et Q₂ reste à 0. Z est toujours à 0.

#### Ligne 4 : État 011 → 100, Z = 0
- **État Actuel** : 011 (décimal 3)
- **État Suivant** : 100 (décimal 4)
- **Sortie Z** : 0
- **Explication** : À partir de l'état 011, Q₀ bascule de 1 à 0, Q₁ bascule de 1 à 0, et Q₂ bascule de 0 à 1 (J₂ = 1, K₂ = 1). Z reste à 0.

#### Ligne 5 : État 100 → 000, Z = 1
- **État Actuel** : 100 (décimal 4)
- **État Suivant** : 000 (décimal 0)
- **Sortie Z** : 1
- **Explication** : À partir de l'état 100, Q₂ bascule de 1 à 0, Q₁ reste à 0, et Q₀ reste à 0. La sortie Z est à 1, indiquant que l'état 100 déclenche la condition de sortie (possiblement Z = Q₂ ET NON Q₁ ET NON Q₀).

### Comportement du Système
- **Séquence d'États** : Le système parcourt les états dans cet ordre : 000 → 001 → 010 → 011 → 100 → 000, et se répète. Il s'agit d'une séquence à 5 états (sur 8 états possibles pour 3 bits), suggérant une configuration spécifique des entrées J et K pour chaque bascule.
- **Sortie Z** : Z est à 1 uniquement lorsque l'état actuel est 100. Cela pourrait représenter une condition où le système signale l'achèvement d'un cycle ou un événement spécifique (par exemple, un compteur atteignant une certaine valeur).

### Interprétation Pratique
Cette configuration de bascules JK semble être un compteur modulo-5 (puisqu'il parcourt 5 états). Le compteur s'incrémente à chaque impulsion d'horloge, et la sortie Z signale lorsque l'état 100 est atteint avant de se réinitialiser à 000. De tels circuits sont utilisés dans les systèmes numériques pour le comptage, la division de fréquence ou la génération de séquences spécifiques.

### Résumé
Le circuit à bascules JK dans le tableau fonctionne comme une machine à états 3 bits avec un cycle à 5 états (000 → 001 → 010 → 011 → 100 → 000). La sortie Z est à 1 uniquement dans l'état 100, indiquant probablement un événement spécifique ou une condition de réinitialisation. Les transitions sont régies par les entrées J et K, qui sont configurées pour produire cette séquence.