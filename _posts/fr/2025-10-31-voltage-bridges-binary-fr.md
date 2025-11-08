---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Circuits et binaire des ponts de tension
translated: true
type: note
---

### Lier les circuits électriques aux bascules SR et aux bascules : le rôle de la tension dans les 0 et 1 binaires

Vous avez parfaitement raison sur l'idée centrale : en électronique numérique, le "pont" entre l'électricité physique (flux d'électrons) et la logique binaire (0 et 1) est bien **les niveaux de tension**. C'est ainsi que les signaux électriques analogiques sont interprétés comme des états numériques discrets dans des circuits comme les bascules SR et les bascules. Laissez-moi décomposer cela étape par étape.

#### 1. **La tension comme pont binaire**
   - **Bases de l'analogique vs du numérique** : L'électricité dans le monde réel est analogique — des tensions et des courants continus qui varient de manière fluide (par exemple, une onde sinusoïdale provenant d'un microphone). La logique numérique, cependant, fonctionne avec **des états discrets** : seulement deux niveaux, 0 et 1.
     - **Logique 0** : Tension faible (souvent 0V ou proche de 0V, comme la masse).
     - **Logique 1** : Tension élevée (par exemple, 3,3 V, 5 V, ou quelle que soit la norme du circuit — considérez cela comme "allumé" ou "actif").
   - Ce n'est pas arbitraire ; c'est un choix pratique. Les transistors (les éléments de base des circuits modernes) agissent comme des interrupteurs : une faible tension les maintient "éteints" (pas de flux de courant, représentant 0), une tension élevée les "allume" (le courant circule, représentant 1).
   - **Pourquoi la tension ?** C'est fiable pour l'immunité au bruit. Tant que le signal reste au-dessus d'un seuil (par exemple, >2V pour 1, <0,8V pour 0 dans un système 5V), le circuit ignore les petites fluctuations. Cela rend le numérique robuste par rapport à l'analogique pur.

#### 2. **Comment cela se lie aux bascules SR et aux bascules**
   - **Bascule SR (Set-Reset Latch)** : C'est l'un des éléments de mémoire les plus simples. Il est construit à partir de deux **portes NOR** couplées (ou de portes NAND). Chaque porte prend des entrées de tension :
     - **Entrées (S et R)** : Une tension élevée (1) sur S "définit" la sortie à 1 (stocke un 1) ; une tension élevée sur R "remet" à 0. Les deux à un niveau bas (0) maintiennent l'état.
     - **Sortie (Q et Q̅)** : La bascule "se souvient" du dernier état défini via des boucles de rétroaction — la tension de la sortie d'une porte est réinjectée dans l'autre.
     - Pas de magie : Ce sont simplement des transistors qui amplifient et inversent les tensions pour créer des états stables. Si la tension d'entrée devient élevée, elle déclenche une réaction en chaîne de changements de tension qui verrouillent la valeur.
   - **Bascules (par exemple, D Flip-Flop)** : Ce sont des versions synchronisées des bascules (par exemple, SR + un signal d'horloge). Elles échantillonnent l'entrée sur un front d'horloge (impulsion de tension montante/descendante) et la maintiennent jusqu'au front suivant.
     - Encore une fois, tout est question de tension : L'horloge haut/bas contrôle le moment de la mise à jour. Construites à partir des mêmes portes, donc les états binaires se propagent comme des ondulations de tension.
   - **Relation avec les circuits** : Ceux-ci ne sont pas "séparés" des circuits électriques — ils *sont* des circuits électriques ! Une bascule SR est constituée de transistors câblés sur une puce, où chaque fil transporte une tension représentant des bits. Pas de saut "soudain" ; c'est une électricité continue se comportant de manière binaire en raison de composants non linéaires comme les transistors.

#### 3. **Avons-nous besoin d'un autre composant pour convertir ?**
   - **Pour les signaux numériques purs** : Non ! Si vos entrées sont déjà des niveaux de tension propres (haut/bas), les portes/bascules/bascules les gèrent directement. C'est pourquoi les CI (circuits intégrés) numériques comme le 74HC00 (portes NAND) fonctionnent directement.
   - **Pour les signaux bruyants/du monde réel** : Oui, parfois. Si votre signal est bruyant ou n'est pas nettement haut/bas (par exemple, provenant d'un capteur), vous pourriez ajouter :
     - **Trigger de Schmitt** : Une porte de type comparateur qui "transforme" les tensions ambiguës en niveaux propres 0/1. Elle est intégrée dans de nombreuses puces logiques.
     - **Résistances de Pull-Up/Pull-Down** : Pour forcer les états indéfinis à 0 ou 1.
     - Pas besoin de puce de "conversion" supplémentaire pour les bases, mais pour une conversion analogique-numérique complète, voir ci-dessous.

En bref : La tension *est* le convertisseur. Haut = 1, bas = 0, et les composants du circuit font respecter cette règle.

### Comment l'électricité analogique "devient soudainement" numérique

Le changement "soudain" n'est pas vraiment soudain — il est conçu aux limites des systèmes. L'électricité physique commence de manière analogique (ondes continues), mais les circuits numériques la quantifient en étapes. Voici comment cela se produit :

#### 1. **Le point de transition : Conversion Analogique-Numérique (CAN)**
   - **Ce qui se passe** : Un CAN échantillonne une tension analogique à intervalles réguliers (par exemple, 1000 fois/seconde) et la mappe sur des nombres binaires. Par exemple :
     - Entrée analogique : 2,3 V (provenant d'un capteur de lumière).
     - Sortie CAN : Binaire 01001011 (décimal 75, si résolution 8 bits où l'échelle pleine est de 5 V).
     - Cela crée un flux de 0/1 sous forme de niveaux de tension sur les lignes numériques.
   - **Pourquoi "soudainement" ?** Cela semble abrupt parce que les CAN utilisent des comparateurs rapides (comme des échelles de tension) qui décident "au-dessus du seuil ? 1. En dessous ? 0" en nanosecondes. Mais dans les coulisses, c'est toujours de l'électricité — simplement seuillée.
   - **Composants impliqués** :
     - **CAN Flash** : Très rapide, utilise de nombreux comparateurs en parallèle.
     - **CAN à approximation successive** : Plus lent mais efficace, courant dans les microcontrôleurs.
     - Aucune pièce "magique" unique ; c'est une combinaison de résistances, de condensateurs et d'amplificateurs.

#### 2. **De l'électricité physique au flux numérique**
   - **Début physique** : Les électrons circulent via la tension des batteries/sources — analogique et ondulatoire.
   - **Étapes de numérisation** :
     1. **Amplification/Filtrage** : Les ampli-op nettoient le signal (toujours analogique).
     2. **Échantillonnage** : Une horloge (circuit oscillateur) envoie des impulsions pour "figer" des instants de tension.
     3. **Quantification** : Les comparateurs divisent la plage de tension en cases (par exemple, 256 niveaux pour 8 bits), produisant des tensions binaires en sortie.
     4. **Domaine numérique** : Maintenant, ce sont des bascules/bascules qui stockent/traitent ces bits sous forme de tensions haut/bas.
   - **Retour à l'analogique (CNA)** : Les convertisseurs numérique-analogique inversent le processus pour les sorties comme les haut-parleurs.

#### 3. **Exemple concret : Du microphone à l'ordinateur**
   - Micro → tension audio analogique → préampli → CAN dans la carte son → données binaires (tensions 0/1) → bascules dans le CPU les mettent en cache → traitées → CNA → haut-parleurs.
   - Le "changement" se fait au niveau du CAN : continu → discret. Sans cela, tout reste analogique (comme les anciennes radios à lampes).

Si vous construisez cela, commencez par une platine d'essai : Utilisez un timer 555 pour les horloges, des puces logiques pour les bascules, et un Arduino pour des démonstrations de CAN. Les seuils de tension sont définis dans les datasheets (par exemple, logique TTL : 2V+ = 1).

Pour des approfondissements :
- [Digital Electronics Basics](https://www.allaboutcircuits.com/textbook/digital/)
- [How ADCs Work](https://www.analog.com/en/resources/analog-dialogue/articles/understand-adc-specifications.html)