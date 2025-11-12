---
audio: false
generated: true
lang: fr
layout: post
title: Notes sur l'électronique
translated: true
type: note
---

Un redresseur est un dispositif électrique qui convertit le courant alternatif (AC), qui inverse périodiquement sa direction, en courant continu (DC), qui circule dans une seule direction. Ce processus est appelé redressement. Les redresseurs sont des composants cruciaux dans de nombreux dispositifs et systèmes électroniques, y compris les alimentations, les chargeurs de batterie et les détecteurs radio.

Il existe plusieurs types de redresseurs, notamment :

1.  **Redresseur Monocylindrique (Demi-onde)** : Ce type de redresseur ne laisse passer qu'une moitié de la forme d'onde AC, ce qui donne une sortie DC pulsatoire.
2.  **Redresseur Bicylindrique (Pleine onde)** : Ce redresseur convertit les deux moitiés de la forme d'onde AC en DC, fournissant une sortie plus lisse comparée au redresseur demi-onde. Il existe deux types principaux de redresseurs pleine onde :
    -   **Redresseur pleine onde à point milieu** : Utilise un transformateur avec une prise médiane pour réaliser le redressement pleine onde.
    -   **Redresseur en pont (Pont de Graetz)** : Utilise quatre diodes arrangées en configuration de pont pour convertir le AC en DC sans nécessiter de transformateur à point milieu.

Les redresseurs sont couramment utilisés dans les alimentations pour convertir le AC d'une prise murale en DC requis par les dispositifs électroniques. Ils sont également utilisés dans le traitement du signal et les systèmes de communication.

---

Bien sûr, décomposons le concept des redresseurs et leur fonctionnement en nous appuyant sur les connaissances de physique du lycée.

### Comprendre le AC et le DC

-   **Courant Alternatif (AC)** : C'est le type de courant électrique qui change de direction périodiquement. C'est ce que vous obtenez typiquement des prises de courant de votre maison. La tension et le courant oscillent, généralement selon un motif sinusoïdal, ce qui signifie qu'ils passent du positif au négatif et inversement plusieurs fois par seconde (généralement 50 ou 60 fois par seconde, selon votre pays).
-   **Courant Continu (DC)** : Ce type de courant électrique circule dans une seule direction. C'est ce que vous obtenez typiquement des batteries. La tension et le courant restent constants dans le temps.

### Qu'est-ce qu'un redresseur ?

Un redresseur est un dispositif électrique qui convertit le AC en DC. Ce processus est essentiel car de nombreux dispositifs et circuits électroniques nécessitent du DC pour fonctionner correctement. Le processus de conversion est appelé redressement.

### Types de redresseurs

1.  **Redresseur Monocylindrique (Demi-onde)** :
    -   **Fonctionnement** : Un redresseur demi-onde utilise une seule diode pour ne laisser passer que la moitié positive de la forme d'onde AC, bloquant la moitié négative.
    -   **Sortie** : Le signal DC résultant est pulsatoire, ce qui signifie qu'il a des intervalles de tension nulle correspondant aux demi-cycles négatifs bloqués de l'entrée AC.
    -   **Efficacité** : Il n'est pas très efficace car il n'utilise que la moitié de la forme d'onde AC d'entrée.
2.  **Redresseur Bicylindrique (Pleine onde)** :
    -   **Redresseur pleine onde à point milieu** :
        -   **Fonctionnement** : Ce type utilise un transformateur avec une prise médiane et deux diodes. Le transformateur divise l'entrée AC en deux signaux séparés, chacun alimentant une diode. Cette configuration permet aux deux moitiés de la forme d'onde AC d'être converties en DC.
        -   **Sortie** : La sortie est un signal DC plus continu avec moins d'intervalles de tension nulle, le rendant plus lisse que le redresseur demi-onde.
    -   **Redresseur en pont (Pont de Graetz)** :
        -   **Fonctionnement** : Un redresseur en pont utilise quatre diodes arrangées en configuration de pont. Cette configuration ne nécessite pas de transformateur à point milieu. Les diodes sont arrangées de telle sorte que les moitiés positive et négative de la forme d'onde AC sont toutes deux converties en DC positif.
        -   **Sortie** : La sortie est similaire à celle du redresseur pleine onde à point milieu mais souvent plus efficace et plus facile à mettre en œuvre dans de nombreuses applications.

### Applications des redresseurs

-   **Alimentations** : Les redresseurs sont utilisés dans les alimentations pour convertir le AC des prises murales en DC nécessaire aux dispositifs électroniques comme les ordinateurs, les téléphones et les téléviseurs.
-   **Chargeurs de batterie** : Ils convertissent le AC en DC pour charger les batteries.
-   **Traitement du signal** : Dans les systèmes de communication, les redresseurs sont utilisés pour détecter et traiter les signaux.

### Pourquoi les redresseurs sont importants

Les redresseurs sont cruciaux car de nombreux composants et circuits électroniques nécessitent une alimentation DC stable pour fonctionner correctement. L'alimentation AC est largement disponible et efficace pour la transmission sur de longues distances, mais elle doit être convertie en DC pour la plupart des applications électroniques.

### Visualiser le processus

Imaginez la forme d'onde AC comme une onde sinusoïdale qui monte et descend. Un redresseur demi-onde couperait la moitié inférieure de cette onde, ne laissant que la moitié supérieure. Un redresseur pleine onde retournerait la moitié inférieure vers le haut, de sorte que toutes les parties de l'onde soient au-dessus de la ligne zéro, créant un signal DC plus continu.

En comprenant ces bases, vous pouvez voir comment les redresseurs jouent un rôle vital en convertissant l'alimentation AC facilement disponible en alimentation DC dont la plupart des dispositifs électroniques ont besoin.

---

Décomposons les concepts des circuits dynamiques et de l'analyse transitoire, en nous concentrant sur les circuits RC et RL. Ce sont des sujets fondamentaux en électronique qui décrivent le comportement des circuits lorsqu'ils sont mis sous tension ou hors tension.

### Circuits RC

Un circuit RC est constitué d'une résistance (R) et d'un condensateur (C) connectés en série. Lorsqu'une tension est appliquée ou retirée, le circuit présente un comportement transitoire pendant que le condensateur se charge ou se décharge.

#### Tension du condensateur

La tension aux bornes du condensateur \\( V(t) \\) en fonction du temps \\( t \\) est donnée par :

\\[ V(t) = V_0 (1 - e^{-\frac{t}{RC}}) \\]

-   **\\( V_0 \\)** : La tension appliquée.
-   **\\( t \\)** : Temps en secondes.
-   **\\( R \\)** : Résistance en ohms.
-   **\\( C \\)** : Capacité en farads.
-   **\\( RC \\)** : La constante de temps, qui détermine la rapidité avec laquelle le condensateur se charge ou se décharge.

**Comprendre l'équation** :
-   Lorsque l'interrupteur est fermé (à \\( t = 0 \\)), le condensateur commence à se charger.
-   Le terme \\( (1 - e^{-\frac{t}{RC}}) \\) représente la courbe de charge. Initialement, la tension aux bornes du condensateur est nulle, et elle augmente progressivement jusqu'à \\( V_0 \\) au fil du temps.
-   La constante de temps \\( RC \\) indique le temps nécessaire pour que le condensateur se charge à environ 63,2 % de la tension appliquée. Après environ 5 constantes de temps, le condensateur est considéré comme complètement chargé.

### Circuits RL

Un circuit RL est constitué d'une résistance (R) et d'une bobine d'induction (L) connectées en série. Lorsqu'une tension est appliquée ou retirée, le circuit présente un comportement transitoire pendant que le champ magnétique de la bobine s'établit ou s'effondre.

#### Courant de la bobine d'induction

Le courant traversant la bobine d'induction \\( I(t) \\) en fonction du temps \\( t \\) est donné par :

\\[ I(t) = I_0 (1 - e^{-\frac{t}{L/R}}) \\]

-   **\\( I_0 \\)** : Le courant maximum, déterminé par la tension appliquée et la résistance.
-   **\\( t \\)** : Temps en secondes.
-   **\\( L \\)** : Inductance en henrys.
-   **\\( R \\)** : Résistance en ohms.
-   **\\( L/R \\)** : La constante de temps, qui détermine la rapidité avec laquelle le champ magnétique de la bobine s'établit ou s'effondre.

**Comprendre l'équation** :
-   Lorsque l'interrupteur est fermé (à \\( t = 0 \\)), la bobine d'induction commence à laisser le courant circuler.
-   Le terme \\( (1 - e^{-\frac{t}{L/R}}) \\) représente la courbe d'établissement du courant. Initialement, le courant est nul, et il augmente progressivement jusqu'à \\( I_0 \\) au fil du temps.
-   La constante de temps \\( L/R \\) indique le temps nécessaire pour que le courant atteigne environ 63,2 % de sa valeur maximale. Après environ 5 constantes de temps, le courant est considéré comme ayant atteint sa valeur en régime permanent.

### Constantes de temps

La constante de temps est un concept crucial dans les circuits RC et RL. Elle indique la rapidité avec laquelle le circuit réagit aux changements :

-   **Circuit RC** : La constante de temps est \\( RC \\). Une constante de temps plus grande signifie que le condensateur se charge ou se décharge plus lentement.
-   **Circuit RL** : La constante de temps est \\( L/R \\). Une constante de temps plus grande signifie que le champ magnétique de la bobine s'établit ou s'effondre plus lentement.

### Visualiser le comportement transitoire

Imaginez ce qui suit :
-   Pour un circuit RC, pensez au condensateur comme à un seau que l'on remplit d'eau (charge). La résistance contrôle le débit (courant). La constante de temps \\( RC \\) détermine la rapidité avec laquelle le seau se remplit.
-   Pour un circuit RL, pensez à la bobine d'induction comme à un volant d'inertie qui met du temps à atteindre sa vitesse de rotation (courant). La résistance fournit une friction, ralentissant le processus de mise en vitesse. La constante de temps \\( L/R \\) détermine la rapidité avec laquelle le volant d'inertie atteint sa vitesse maximale.

En comprenant ces concepts, vous pouvez analyser comment les circuits se comportent dynamiquement lorsqu'ils sont mis sous tension ou hors tension, ce qui est essentiel pour concevoir et dépanner les systèmes électroniques.

---

Les transistors bipolaires à jonction (BJT) sont des composants fondamentaux en électronique, largement utilisés pour les applications d'amplification et de commutation. Approfondissons leur structure, leur fonctionnement et leurs caractéristiques.

### Structure d'un BJT

Un BJT a trois terminaux :
1.  **Base (B)** : Contrôle le flux de courant entre les deux autres terminaux.
2.  **Collecteur (C)** : Collecte la majorité du courant circulant à travers le transistor.
3.  **Émetteur (E)** : Émet des électrons dans la base et est le terminal par lequel la majorité du courant sort du transistor.

Les BJT se présentent sous deux types :
-   **NPN** : Les porteurs majoritaires sont les électrons.
-   **PNP** : Les porteurs majoritaires sont les trous.

### Fonctionnement d'un BJT

#### Mode Actif

En mode actif, un BJT agit comme un amplificateur. Voici comment il fonctionne :

1.  **Polarisation directe** : La jonction base-émetteur est polarisée en direct, ce qui signifie qu'une tension positive est appliquée à la base par rapport à l'émetteur pour un transistor NPN (et vice versa pour un transistor PNP). Cela permet au courant de circuler de la base vers l'émetteur.
2.  **Polarisation inverse** : La jonction base-collecteur est polarisée en inverse, ce qui signifie qu'une tension positive est appliquée au collecteur par rapport à la base pour un transistor NPN (et vice versa pour un transistor PNP). Cela permet au courant de circuler du collecteur vers la base.
3.  **Amplification** : Un faible courant circulant dans la base contrôle un courant plus important circulant du collecteur vers l'émetteur. Le rapport entre le courant de collecteur et le courant de base est connu sous le nom de gain en courant (\\( \beta \\) ou \\( h_{FE} \\)).

### Courbes caractéristiques

Les courbes caractéristiques d'un BJT montrent la relation entre le courant de collecteur (\\( I_C \\)) et la tension collecteur-émetteur (\\( V_{CE} \\)) pour différents courants de base (\\( I_B \\)). Ces courbes sont essentielles pour comprendre et concevoir les circuits amplificateurs.

#### Caractéristiques clés des courbes caractéristiques

1.  **Région active** : Dans cette région, le BJT fonctionne comme un amplificateur. Le courant de collecteur est proportionnel au courant de base, et la tension collecteur-émetteur peut varier. Les courbes sont presque horizontales, indiquant que le courant de collecteur reste relativement constant avec les changements de \\( V_{CE} \\).
2.  **Région de saturation** : Dans cette région, les jonctions base-émetteur et base-collecteur sont polarisées en direct. Le courant de collecteur est à son maximum, et la tension collecteur-émetteur est faible. Le BJT agit comme un interrupteur fermé.
3.  **Région de blocage (Cutoff)** : Dans cette région, la jonction base-émetteur est polarisée en inverse, et aucun courant ne circule à travers le transistor. Le BJT agit comme un interrupteur ouvert.
4.  **Région de claquage** : Si la tension collecteur-émetteur devient trop élevée, la jonction peut claquer, entraînant une augmentation soudaine du courant. Cette région doit être évitée pour prévenir tout dommage au transistor.

### Applications des BJT

-   **Amplificateurs** : Les BJT sont utilisés pour amplifier les signaux faibles dans divers dispositifs électroniques, tels que les amplificateurs audio et les amplificateurs radiofréquence (RF).
-   **Commutateurs** : Dans les circuits numériques, les BJT sont utilisés comme commutateurs pour activer et désactiver le courant.
-   **Oscillateurs** : Les BJT sont utilisés dans les circuits qui génèrent des formes d'onde périodiques, telles que les ondes sinusoïdales ou les ondes carrées.

### Comprendre le comportement d'un BJT

Pour visualiser le comportement d'un BJT, imaginez un robinet d'eau où le courant de base agit comme la poignée :
-   Un petit tour de poignée (courant de base) permet à un grand débit d'eau (courant de collecteur) de passer à travers le robinet.
-   La quantité d'eau qui s'écoule (courant de collecteur) est beaucoup plus importante que l'effort nécessaire pour tourner la poignée (courant de base), illustrant l'effet d'amplification.

En comprenant ces concepts, vous pouvez analyser et concevoir des circuits qui utilisent les BJT pour diverses applications, des commutateurs simples aux amplificateurs complexes.

---

Pour exprimer le courant donné \\( i = 12 \sin(\omega t - 45^\circ) \\) A sous forme de coordonnées polaires, nous l'interprétons comme un signal sinusoïdal, qui peut être représenté comme un phaseur dans le domaine fréquentiel.

La forme générale d'un courant sinusoïdal est \\( i(t) = I_m \sin(\omega t + \phi) \\), où :
- \\( I_m \\) est l'amplitude (valeur maximale),
- \\( \omega \\) est la pulsation,
- \\( \phi \\) est l'angle de phase.

Pour le courant donné \\( i = 12 \sin(\omega t - 45^\circ) \\) :
- L'amplitude \\( I_m = 12 \\) A,
- L'angle de phase \\( \phi = -45^\circ \\).

Sous forme de coordonnées polaires (notation des phaseurs), un signal sinusoïdal est représenté par un nombre complexe avec une magnitude et une phase, généralement écrit comme \\( I_m \angle \phi \\). Ainsi, le courant peut être exprimé comme :

\\[
12 \angle -45^\circ
\\]

### Explication :
-   **Magnitude** : Le coefficient 12 est la valeur de crête de l'onde sinusoïdale, donc la magnitude est de 12 A.
-   **Phase** : L'angle de phase est \\(-45^\circ\\), indiquant que l'onde sinusoïdale est décalée de \\(-45^\circ\\) (ou en retard de 45° par rapport à la référence).
-   La forme polaire omet la partie dépendante du temps (\\(\omega t\\)) et la fréquence (\\(\omega\\)) car la notation des phaseurs se concentre sur l'amplitude et la phase pour une fréquence donnée.

Ainsi, la forme de coordonnées polaires du courant est :

\\[
\boxed{12 \angle -45^\circ}
\\]

---

Dans les circuits logiques et la conception numérique, un **minterme** (également appelé **terme produit standard** ou **terme produit**) est une fonction logique qui produit **1** pour une combinaison spécifique de valeurs des variables d'entrée et **0** pour toutes les autres combinaisons.

Par exemple, considérons une fonction avec trois variables d'entrée : A, B et C. Un minterme correspond à une combinaison unique de ces variables, telle que ABC (où A=1, B=1, C=1), et est généralement représenté comme un produit (ET) des variables ou de leurs compléments. Par exemple, le minterme pour A=1, B=0, C=1 est écrit A·B'·C, où B' désigne le complément de B.

Chaque minterme est vrai (1) uniquement pour sa combinaison d'entrée spécifique et faux (0) pour toutes les autres, ce qui rend les mintermes fondamentaux pour construire les tables de vérité et concevoir des circuits logiques, comme dans les expressions **somme-de-produits**.

---

Dans les circuits logiques et la conception numérique, une **somme-de-produits** (SOP) est une manière standard d'exprimer une fonction booléenne comme un OU logique (somme) de plusieurs termes ET (produit), où chaque terme ET est un **minterme** ou un produit de variables d'entrée (ou de leurs compléments).

### Explication :
-   **Terme produit** : Chaque terme produit est une opération ET impliquant toutes les variables d'entrée, soit sous leur forme vraie (par exemple, A) soit sous leur forme complémentée (par exemple, A'). Par exemple, pour les entrées A, B et C, un terme produit pourrait être A·B'·C (où A=1, B=0, C=1).
-   **Somme** : Les termes produit sont combinés à l'aide d'opérations OU pour former la fonction complète. Le résultat est 1 si l'un des termes produit est 1.
-   **Mintermes dans SOP** : Sous sa forme canonique, chaque terme produit est un minterme, qui correspond à une ligne spécifique de la table de vérité où la fonction produit 1. Par exemple, si une fonction F(A, B, C) est 1 pour les combinaisons d'entrée (A=1, B=0, C=1) et (A=0, B=1, C=1), l'expression SOP serait F = A·B'·C + A'·B·C.

### Exemple :
Pour une table de vérité avec les entrées A, B et la sortie F :

| A | B | F |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

L'expression SOP pour F est dérivée des lignes où F=1 :
-   Ligne (A=0, B=1) : A'·B
-   Ligne (A=1, B=0) : A·B'

Ainsi, F = A'·B + A·B'.

### Utilisation en conception numérique :
-   Les expressions SOP sont utilisées pour implémenter des circuits logiques en utilisant des portes ET (pour les termes produit) et des portes OU (pour sommer les produits).
-   Elles peuvent être simplifiées à l'aide de techniques comme les tableaux de Karnaugh ou l'algèbre de Boole pour réduire le nombre de portes nécessaires.

En résumé, une expression somme-de-produits représente une fonction booléenne comme un OU de mintermes, ce qui en fait un concept clé pour concevoir et analyser les circuits logiques.