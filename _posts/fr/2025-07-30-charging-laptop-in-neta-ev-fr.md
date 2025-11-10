---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Recharger un ordinateur portable Lenovo dans une Neta EV
translated: true
type: note
---

### Comprendre le problème de charge de votre ordinateur portable Lenovo dans une Neta EV

D'après les détails que vous avez décrits, il semble que vous essayiez de charger votre ordinateur portable Lenovo (probablement via son port Type-C, avec un chargeur compatible) depuis votre voiture électrique Neta de deux manières différentes :

1.  **Via le port allume-cigare (à l'intérieur de la voiture)** : Cela implique de brancher un adaptateur ou un onduleur dans la prise 12V de l'allume-cigare pour créer une prise de courant ou une connexion USB-C. Cette méthode ne fonctionne pas pour charger votre ordinateur portable.

2.  **Via la prise de charge lente externe (à l'extérieur de la voiture)** : Cela utilise la prise de charge de la voiture avec un adaptateur "pistolet de charge" et un câble passés par la fenêtre jusqu'à une prise à l'intérieur, puis vous connectez le chargeur Type-C de votre ordinateur portable. Cette méthode fonctionne parfaitement.

La différence essentielle se résume aux **limitations de puissance de sortie, aux types de tension et à la conception du système** dans les véhicules électriques (VE) comme les modèles Neta (par exemple, Neta V ou similaire). Je vais expliquer étape par étape pourquoi une méthode échoue tandis que l'autre réussit, en me basant sur les spécifications typiques des VE et les fonctionnalités de Neta.

#### 1. Pourquoi le port allume-cigare ne peut pas charger votre ordinateur portable
-   **Puissance de sortie limitée** : L'allume-cigare dans la plupart des voitures, y compris les VE comme Neta, est une prise 12V DC conçue pour des accessoires de faible puissance (par exemple, des chargeurs de téléphone ou de petits gadgets). Dans les VE Neta, elle est généralement évaluée à environ 120-180W maximum (selon les standards automobiles 12V généraux, car elle est fusible à 10-15A). Cependant, la puissance de sortie continue réelle est souvent inférieure en raison de la chaleur, du câblage et des limites du fusible.
    -   Si vous utilisez un onduleur (pour convertir le 12V DC en AC pour un chargeur d'ordinateur portable standard) ou un adaptateur USB-C de voiture direct, les pertes de rendement peuvent réduire la puissance utilisable à 80-100W ou moins. Les ordinateurs portables Lenovo nécessitent souvent 45-100W+ pour une charge correcte (par exemple, 65W pour de nombreux modèles ThinkPad), surtout si l'ordinateur est en cours d'utilisation. Si la puissance descend en dessous de ce seuil, la charge s'arrête ou devient trop lente pour être enregistrée.
    -   Les chutes de tension ou l'instabilité du système 12V (courant dans les VE, où il est alimenté par un convertisseur DC-DC à partir de la batterie haute tension) peuvent également empêcher une charge fiable.

-   **Incompatibilité avec les appareils à forte demande** : Les ordinateurs portables ont besoin d'une alimentation stable et de haute puissance (Power Delivery ou PD) via le Type-C. Les adaptateurs de voiture bon marché branchés sur la prise allume-cigare atteignent souvent un maximum de 18-30W PD, ce qui peut suffire pour une charge lente d'un téléphone mais pas pour un ordinateur portable. Même avec un onduleur, s'il est sous-dimensionné ou si la surchauffe du port, il s'arrête.

-   **Contraintes spécifiques aux VE** : Dans les VE, le système 12V est auxiliaire (pas directement issu de la batterie principale) et priorisé pour les éléments essentiels comme les phares et l'infodivertissement. Il n'est pas conçu pour des charges élevées continues comme la charge d'un ordinateur portable, ce qui pourrait vider la batterie 12V ou déclencher des coupures de sécurité.

En bref, le port allume-cigare ne fournit tout simplement pas assez de puissance constante pour les besoins de votre ordinateur portable Lenovo.

#### 2. Pourquoi la méthode utilisant la prise de charge lente externe fonctionne
-   **Cela utilise la fonction V2L (Vehicle-to-Load)** : Les VE Neta (comme la Neta V) prennent en charge le V2L, ce qui transforme la voiture en une source d'alimentation mobile. Vous branchez un adaptateur V2L spécial (ressemblant souvent à un pistolet de charge) dans la prise de charge AC externe, qui puise dans la batterie haute tension et délivre une puissance AC (par exemple, 220V dans de nombreuses régions).
    -   Le V2L de Neta peut délivrer jusqu'à 3 300W (3,3kW), bien plus que nécessaire pour un ordinateur portable. C'est comme brancher l'appareil sur une prise murale domestique – une alimentation AC stable et puissante sans pertes significatives.
    -   En passant le câble par la fenêtre jusqu'à une prise à l'intérieur, vous étendez essentiellement une prise pleine puissance à l'intérieur de la voiture. Le chargeur Type-C de votre ordinateur portable (qui convertit le AC en DC) reçoit exactement la puissance dont il a besoin, comme à la maison.

-   **Aucune limitation de puissance ici** : Le V2L contourne le système 12V basse puissance et utilise l'onduleur/chargeur de bord de la voiture directement à partir de la batterie principale. Il est conçu pour des charges plus élevées (par exemple, des appareils électroménagers, des outils ou même du matériel de camping), donc charger un ordinateur portable de 65-100W est sans effort. Il évite également les problèmes de rendement car il s'agit d'une sortie AC native.

-   **Avantages en matière de sécurité et de conception** : Le V2L inclut des protections contre les surcharges, et comme il est externe, il n'interfère pas avec les systèmes internes de la voiture. Note : Assurez-vous que votre modèle Neta a le V2L activé (la plupart des modèles récents l'ont) et utilisez l'adaptateur officiel pour éviter tout risque.

#### Correctifs ou alternatives possibles
-   Pour le port allume-cigare : Essayez un onduleur de haute qualité évalué pour au moins 150W de puissance continue, ou un chargeur de voiture USB-C PD dédié de 60W+. Mais même dans ce cas, cela pourrait ne pas fonctionner de manière fiable dans votre Neta en raison des limites du 12V – testez avec la voiture en marche pour maintenir la charge de la batterie.
-   Tenez-vous en au V2L pour une charge fiable, mais soyez attentif à la décharge de la batterie (il utilise la batterie principale du VE, surveillez donc l'état de charge (SOC) pour éviter de vous retrouver en panne).
-   Si votre ordinateur portable le prend en charge, un câble USB-C direct depuis un port USB de voiture haute puissance (si votre Neta en possède un) pourrait mieux fonctionner que l'allume-cigare.
-   Conseil général : Vérifiez toujours le manuel d'utilisation de votre Neta pour les spécifications exactes des ports et de l'utilisation du V2L.

Si cela ne correspond pas exactement à votre configuration (par exemple, modèle Neta spécifique ou détails de l'adaptateur), fournissez plus d'informations pour une explication sur mesure !

[Manuel d'utilisation de la Neta V](https://www.netaauto.co/resource/upload/User%27s%2520Manual%2520of%2520NETA%2520V.pdf)
[Spécifications officielles de la NETA V](https://www.neta.co.th/en/product/NetaV)
[La Neta V lancée en Malaisie](https://cleantechnica.com/2023/05/15/the-neta-v-launched-in-malaysia-is-now-the-most-affordable-ev-in-the-country/)
[Vehicle to Load (V2L) : Qu'est-ce que c'est et comment ça marche](https://www.joosup.com/vehicle-to-load/)
[Est-il possible de charger un ordinateur portable dans un véhicule électrique ?](https://www.reddit.com/r/electricvehicles/comments/15jp7w1/is_it_possible_to_charge_a_laptop_in_an_ev/)