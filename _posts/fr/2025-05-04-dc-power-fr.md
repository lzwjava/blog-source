---
audio: false
generated: true
lang: fr
layout: post
title: Alimentations à courant continu
translated: true
type: note
---

Ce tutoriel propose une exploration détaillée des **alimentations à courant continu**, en se concentrant sur les **circuits redresseurs et filtres** (redresseurs demi-onde et pleine onde) et les différences entre les **régulateurs linéaires et à découpage**. Il comprend des explications théoriques, des exemples pratiques, des conceptions de circuits et des applications réelles pour garantir une compréhension approfondie pour les débutants et les apprenants intermédiaires.

---

## Table des matières
1. **Introduction aux alimentations à courant continu**
2. **Circuits redresseurs et filtres**
   - Redresseur demi-onde
   - Redresseur pleine onde (Configuration en pont)
   - Circuits de filtrage
3. **Régulateurs linéaires vs à découpage**
   - Régulateurs linéaires
   - Régulateurs à découpage (Buck, Boost, Buck-Boost)
4. **Exemples pratiques et conception de circuits**
5. **Applications et considérations**
6. **Conclusion**

---

## 1. Introduction aux alimentations à courant continu
Une **alimentation à courant continu** convertit le courant alternatif (AC) en courant continu (DC) pour alimenter des dispositifs électroniques tels que les microcontrôleurs, les capteurs et les circuits intégrés. Le processus implique typiquement :
- **Le redressement** : Conversion du AC en DC pulsatoire.
- **Le filtrage** : Lissage du DC pulsatoire.
- **La régulation** : Stabilisation de la tension ou du courant de sortie.

Les alimentations à courant continu sont essentielles en électronique, garantissant que les dispositifs reçoivent une alimentation stable et à faible bruit. Les deux composants principaux abordés ici sont les **circuits redresseurs/filtres** et les **régulateurs de tension** (linéaires et à découpage).

---

## 2. Circuits redresseurs et filtres

Les circuits redresseurs convertissent le AC en DC, et les filtres lissent la sortie pour réduire l'ondulation. Décomposons cela.

### a. Redresseur demi-onde
Le **redresseur demi-onde** est le circuit de redressement le plus simple, utilisant une seule diode.

#### Fonctionnement
- **Entrée** : Tension AC (par exemple, d'un transformateur).
- **Opération** : La diode conduit uniquement pendant l'alternance positive de la forme d'onde AC, bloquant l'alternance négative.
- **Sortie** : DC pulsatoire avec la même fréquence que l'AC d'entrée, contenant uniquement les alternances positives (ou négatives, selon l'orientation de la diode).

#### Schéma de circuit
```
Source AC ----> Diode (D1) ----> Charge (R) ----> Masse
```
- **Composants** :
  - **Diode** : Par exemple, 1N4007 (diode redresseuse généraliste).
  - **Charge** : Une résistance ou un circuit électronique.

#### Caractéristiques
- **Tension de sortie** : Approximativement \\( V_{sortie} = V_{entrée(crête)} - V_{diode} \\) (où \\( V_{diode} \approx 0.7V \\) pour les diodes au silicium).
- **Efficacité** : Faible (~40,6 %), car seule la moitié de la période AC est utilisée.
- **Ondulation** : Élevée, car la sortie est intermittente.

#### Avantages
- Simple et peu coûteux.
- Nécessite un minimum de composants.

#### Inconvénients
- Inefficace (gaspille la moitié de la période AC).
- Ondulation élevée, nécessitant de gros filtres pour un DC lisse.

---

### b. Redresseur pleine onde (Configuration en pont)
Le **redresseur pleine onde** utilise à la fois les alternances positives et négatives de l'entrée AC, produisant une sortie DC plus constante.

#### Fonctionnement
- **Configuration** : Utilise quatre diodes dans une configuration **redresseur en pont**.
- **Opération** :
  - Pendant l'alternance positive, deux diodes conduisent, dirigeant le courant à travers la charge.
  - Pendant l'alternance négative, les deux autres diodes conduisent, maintenant la même direction du courant à travers la charge.
- **Sortie** : DC pulsatoire avec une fréquence double de celle de l'AC d'entrée.

#### Schéma de circuit
```
       Entrée AC
         ------
        |      |
   D1 --|-->|--|-->|-- D2
        |      |       |
        |      R       |
        |      |       |
   D3 --|<--|--|<--|-- D4
        |      |
         ------
       Masse
```
- **Composants** :
  - **Diodes** : Quatre diodes (par exemple, 1N4007).
  - **Charge** : Résistance ou circuit.
  - **Transformateur** (optionnel) : Abaisse la tension AC.

#### Caractéristiques
- **Tension de sortie** : \\( V_{sortie} = V_{entrée(crête)} - 2V_{diode} \\) (deux diodes conduisent à la fois, donc une chute d'environ 1,4V pour les diodes au silicium).
- **Efficacité** : Plus élevée (~81,2 %) que le redresseur demi-onde.
- **Ondulation** : Plus faible que le redresseur demi-onde, car les impulsions se produisent deux fois par cycle.

#### Avantages
- Plus efficace, utilise la totalité de la période AC.
- Ondulation réduite, nécessitant des filtres plus petits.

#### Inconvénients
- Plus complexe (quatre diodes).
- Chute de tension légèrement plus élevée (due aux deux diodes).

---

### c. Circuits de filtrage
Les redresseurs produisent un DC pulsatoire, qui n'est pas adapté à la plupart des applications électroniques en raison de l'**ondulation** (variations de tension). Les filtres lissent la sortie pour obtenir un DC quasi constant.

#### Filtre courant : Filtre capacitif
Un **filtre capacitif** est la méthode la plus courante, placée en parallèle avec la charge.

#### Fonctionnement
- **Charge** : Pendant le pic de la forme d'onde redressée, le condensateur se charge jusqu'à la tension de crête.
- **Décharge** : Lorsque la tension redressée chute, le condensateur se décharge à travers la charge, maintenant une tension plus constante.
- **Résultat** : DC plus lisse avec une ondulation réduite.

#### Schéma de circuit (Redresseur pleine onde avec filtre capacitif)
```
       Entrée AC
         ------
        |      |
   D1 --|-->|--|-->|-- D2
        |      |       |
        |      R       C (Condensateur)
        |      |       |
   D3 --|<--|--|<--|-- D4
        |      |
         ------
       Masse
```
- **Composants** :
  - **Condensateur** : La valeur dépend du courant de charge et de la tolérance d'ondulation (par exemple, 1000µF pour des charges modérées).
  - **Charge** : Résistance ou circuit.

#### Calcul de l'ondulation
La tension d'ondulation (\\( V_o \\)) peut être approximée par :
\\[ V_o \approx \frac{I_{charge}}{f \cdot C} \\]
Où :
- \\( I_{charge} \\) : Courant de charge (A).
- \\( f \\) : Fréquence de la sortie redressée (par exemple, 120Hz pour un redresseur pleine onde avec une entrée AC à 60Hz).
- \\( C \\) : Capacité (F).

#### Exemple
Pour un courant de charge de 100mA, un condensateur de 1000µF et une fréquence de 120Hz :
\\[ V_o \approx \frac{0.1}{120 \cdot 1000 \times 10^{-6}} \approx 0.833V \\]
Cette ondulation peut être acceptable pour certaines applications mais peut être réduite avec un condensateur plus grand ou un filtrage supplémentaire (par exemple, des filtres LC).

#### Autres filtres
- **Filtre à inductance** : Utilise une inductance en série avec la charge pour s'opposer aux changements rapides de courant.
- **Filtre LC** : Combine une inductance et un condensateur pour une meilleure réduction de l'ondulation.
- **Filtre Pi** : Configuration condensateur-inductance-condensateur (C-L-C) pour un DC très lisse.

---

## 3. Régulateurs linéaires vs à découpage

Après le redressement et le filtrage, la tension DC peut encore varier avec les changements d'entrée ou la demande de charge. Les **régulateurs de tension** stabilisent la sortie. Il existe deux types principaux : les **régulateurs linéaires** et les **régulateurs à découpage**.

### a. Régulateurs linéaires
Les régulateurs linéaires fournissent une tension de sortie stable en dissipant l'excès de puissance sous forme de chaleur.

#### Fonctionnement
- Agit comme une résistance variable, ajustant la résistance pour maintenir une tension de sortie constante.
- Nécessite que la tension d'entrée soit supérieure à la tension de sortie souhaitée (tension de dropout).

#### Exemple : Régulateur linéaire 7805
Le **7805** est un régulateur linéaire populaire fournissant une sortie fixe de 5V.

#### Schéma de circuit
```
Vin ----> [7805] ----> Vsortie (5V)
       |         |
      C1        C2
       |         |
      Masse    Masse
```
- **Composants** :
  - **CI 7805** : Sortie de 5V (jusqu'à 1A avec un dissipateur thermique approprié).
  - **Condensateurs** : C1 (0,33µF) et C2 (0,1µF) pour la stabilité.
  - **Vin** : Typiquement 7-12V (doit être > 5V + tension de dropout, ~2V).

#### Caractéristiques
- **Sortie** : Fixe (par exemple, 5V pour le 7805) ou ajustable (par exemple, LM317).
- **Efficacité** : Faible, car l'excès de tension est dissipé sous forme de chaleur (\\( Efficacité \approx \frac{V_{sortie}}{V_{entrée}} \\)).
- **Bruit** : Faible, idéal pour les circuits analogiques sensibles.

#### Avantages
- Conception simple, facile à mettre en œuvre.
- Faible bruit de sortie, adapté aux circuits audio et de précision.
- Peu coûteux.

#### Inconvénients
- Inefficace, surtout avec de grandes différences de tension.
- Génère de la chaleur, nécessitant des dissipateurs thermiques pour les courants élevés.
- Limité à l'abaissement de tension (sortie < entrée).

---

### b. Régulateurs à découpage
Les régulateurs à découpage utilisent une commutation haute fréquence pour contrôler le transfert d'énergie, atteignant une efficacité élevée.

#### Fonctionnement
- Un interrupteur (généralement un MOSFET) s'ouvre et se ferme rapidement, contrôlant le flux d'énergie à travers les inductances et les condensateurs.
- Un circuit de rétroaction ajuste le cycle de service (duty cycle) de la commutation pour maintenir une sortie stable.

#### Types de régulateurs à découpage
1. **Buck (Abaisseur)** : Réduit la tension (par exemple, 12V à 5V).
2. **Boost (Élévateur)** : Augmente la tension (par exemple, 5V à 12V).
3. **Buck-Boost** : Peut augmenter ou réduire la tension (par exemple, 9V à 5V ou 12V).

#### Schéma de circuit (Exemple convertisseur Buck)
```
Vin ----> Interrupteur (MOSFET) ----> Inductance ----> Vsortie
       |                            |
      Diode                       Condensateur
       |                            |
      Masse                       Masse
```
- **Composants** :
  - **MOSFET** : Contrôle la commutation.
  - **Inductance** : Stocke l'énergie pendant le cycle "on".
  - **Condensateur** : Lisse la sortie.
  - **Diode** : Fournit un chemin pour le courant de l'inductance pendant le cycle "off".
  - **CI Contrôleur** : Par exemple, LM2596 (convertisseur Buck ajustable).

#### Caractéristiques
- **Efficacité** : Élevée (80-95 %), car une puissance minimale est dissipée sous forme de chaleur.
- **Bruit** : Plus élevé que les régulateurs linéaires en raison de la commutation.
- **Flexibilité** : Peut augmenter, réduire ou faire les deux.

#### Avantages
- Haute efficacité, idéal pour les dispositifs alimentés par batterie.
- Conceptions compactes avec des dissipateurs thermiques plus petits.
- Polyvalent (configurations Buck, Boost ou Buck-Boost).

#### Inconvénients
- Plus complexe, nécessitant des inductances et une conception soignée.
- Le bruit de commutation peut interférer avec les circuits sensibles.
- Coût plus élevé dû aux composants supplémentaires.

---

## 4. Exemples pratiques et conception de circuits

### Exemple 1 : Alimentation 5V DC avec redresseur demi-onde et régulateur linéaire
**Objectif** : Concevoir une alimentation 5V DC à partir d'un transformateur 9V AC.
**Étapes** :
1. **Redressement** : Utiliser une diode 1N4007 pour le redressement demi-onde.
2. **Filtrage** : Ajouter un condensateur de 1000µF pour lisser la sortie.
3. **Régulation** : Utiliser un régulateur 7805 pour une sortie stable de 5V.

**Circuit** :
```
9V AC ----> 1N4007 ----> 1000µF ----> 7805 ----> 5V
                     |             |        |
                    Masse         C1       C2
                                   |        |
                                  Masse    Masse
```
- **C1** : 0,33µF (stabilité d'entrée).
- **C2** : 0,1µF (stabilité de sortie).

**Considérations** :
- Le transformateur doit fournir >7V DC après redressement (9V AC est suffisant).
- Ajouter un dissipateur thermique au 7805 si le courant de charge dépasse 500mA.

---

### Exemple 2 : Alimentation 5V DC avec redresseur pleine onde et régulateur à découpage
**Objectif** : Concevoir une alimentation 5V haute efficacité à partir d'un transformateur 12V AC.
**Étapes** :
1. **Redressement** : Utiliser un redresseur en pont (quatre diodes 1N4007).
2. **Filtrage** : Ajouter un condensateur de 2200µF.
3. **Régulation** : Utiliser un convertisseur Buck LM2596.

**Circuit** :
```
12V AC ----> Redresseur en pont ----> 2200µF ----> LM2596 ----> 5V
                         |                       |
                        Masse                   Masse
```
- **LM2596** : Configuré pour une sortie de 5V (ajustable via des résistances de rétroaction).
- **Condensateurs** : Suivre la datasheet du LM2596 pour les condensateurs d'entrée/sortie.

**Considérations** :
- Assurer une sélection appropriée de l'inductance (selon la datasheet du LM2596).
- Ajouter un filtrage CEM si utilisé dans des applications sensibles au bruit.

---

## 5. Applications et considérations

### Applications
- **Redresseurs demi-onde** : Dispositifs peu coûteux et de faible puissance (par exemple, chargeurs de batterie simples).
- **Redresseurs pleine onde** : Alimentations généralistes pour l'électronique.
- **Régulateurs linéaires** : Circuits audio, capteurs de précision et dispositifs de faible puissance.
- **Régulateurs à découpage** : Ordinateurs portables, smartphones, pilotes LED et systèmes alimentés par batterie.

### Considérations de conception
- **Exigences de la charge** : S'assurer que l'alimentation peut gérer le courant maximal.
- **Efficacité** : Choisir des régulateurs à découpage pour les applications de forte puissance.
- **Bruit** : Utiliser des régulateurs linéaires ou un filtrage supplémentaire pour les circuits sensibles.
- **Gestion thermique** : Inclure des dissipateurs thermiques ou une conception de PCB appropriée pour la dissipation thermique.
- **Caractéristiques des composants** : Sélectionner les diodes, condensateurs et régulateurs avec des tensions/courants nominaux appropriés.

---

## 6. Conclusion
Les alimentations à courant continu sont essentielles pour alimenter les dispositifs électroniques, et comprendre leurs composants—redresseurs, filtres et régulateurs—est essentiel pour concevoir des systèmes fiables. Les **redresseurs demi-onde** sont simples mais inefficaces, tandis que les **redresseurs pleine onde** offrent de meilleures performances. Les **régulateurs linéaires** sont idéaux pour les applications à faible bruit mais gaspillent de l'énergie, tandis que les **régulateurs à découpage** offrent une haute efficacité pour les dispositifs modernes gourmands en énergie. En combinant ces éléments de manière réfléchie, vous pouvez créer des alimentations robustes adaptées à des besoins spécifiques.

Pour un apprentissage pratique, essayez de construire les exemples de circuits en utilisant une platine d'essai ou un logiciel de simulation comme LTspice. Expérimentez avec différentes valeurs de condensateurs ou types de régulateurs pour observer leur impact sur les performances.