---
audio: false
generated: true
lang: fr
layout: post
title: Amplificateurs opérationnels
translated: true
type: note
---

Voici un tutoriel complet sur les **amplificateurs opérationnels (AOP) et leurs applications**, couvrant les sujets spécifiés : caractéristiques et paramètres des AOP (court-circuit virtuel, ouvert virtuel), circuits typiques à AOP (amplificateurs inverseurs/non inverseurs, intégrateurs/dérivateurs) et applications non linéaires (comparateurs, générateurs de formes d'ondes). Ce tutoriel est conçu pour être exhaustif, adapté aux débutants et techniquement précis, avec des exemples pratiques et des explications.

---

Les amplificateurs opérationnels (AOP) sont des amplificateurs électroniques polyvalents et à haut gain, largement utilisés dans les circuits analogiques pour le traitement du signal, l'amplification, le filtrage, et plus encore. Ce tutoriel vous guidera à travers leurs caractéristiques, leurs circuits clés et leurs applications non linéaires.

---

### **1. Caractéristiques et paramètres des AOP**

Un amplificateur opérationnel est un amplificateur à gain élevé, à couplage direct, avec des entrées différentielles et une sortie unique. Il est généralement utilisé avec des composants de contre-réaction externes (résistances, condensateurs, etc.) pour définir sa fonction. Voici les principales caractéristiques et paramètres d'un AOP idéal, ainsi que leurs implications pratiques.

#### **Caractéristiques d'un AOP idéal**
1. **Gain en boucle ouverte infini (A_OL)**
   - Le gain en boucle ouverte (sans contre-réaction) est théoriquement infini, ce qui signifie qu'une différence infime entre les bornes d'entrée produit une grande sortie. En pratique, les AOP réels ont des gains en boucle ouverte de 10^5 à 10^6.
   - **Implication** : Permet un contrôle précis lorsque la contre-réaction est appliquée.

2. **Impédance d'entrée infinie**
   - Les bornes d'entrée ne consomment aucun courant (l'impédance d'entrée idéale est infinie). Dans les AOP réels, l'impédance d'entrée est typiquement de l'ordre des mégaohms aux gigaohms.
   - **Implication** : L'AOP ne charge pas la source du signal d'entrée, préservant ainsi l'intégrité du signal.

3. **Impédance de sortie nulle**
   - La sortie peut piloter n'importe quelle charge sans chute de tension. Les AOP réels ont une faible impédance de sortie (par exemple, 10–100 ohms).
   - **Implication** : Assure un transfert de signal efficace vers l'étage suivant.

4. **Bande passante infinie**
   - Un AOP idéal amplifie toutes les fréquences de manière égale. En pratique, le produit gain-bande passante limite les performances (par exemple, une bande passante à gain unitaire de 1 MHz pour un AOP 741).
   - **Implication** : La bande passante diminue avec l'augmentation du gain dans les configurations en boucle fermée.

5. **Tension de décalage nulle**
   - Sans signal d'entrée, la sortie est nulle. Les AOP réels ont de faibles tensions de décalage (microvolts à millivolts) qui peuvent nécessiter une compensation.
   - **Implication** : Minimise la sortie non désirée dans les applications de précision.

6. **Taux de réjection du mode commun (CMRR) infini**
   - L'AOP rejette les signaux communs aux deux entrées (par exemple, le bruit). Les AOP réels ont un CMRR élevé (80–120 dB).
   - **Implication** : Réduit le bruit dans les applications de signaux différentiels.

#### **Concepts clés : Court-circuit virtuel et Ouvert virtuel**
- **Court-circuit virtuel**
  - Dans une configuration à contre-réaction négative, le gain élevé en boucle ouverte force la différence de tension entre les entrées inverseuse (-) et non inverseuse (+) à être presque nulle.
  - **Explication** : L'AOP ajuste sa sortie pour que V+ ≈ V- (en supposant une contre-réaction négative). C'est ce qu'on appelle un "court-circuit virtuel" car les entrées ne sont pas physiquement court-circuitées mais se comportent comme si elles l'étaient.
  - **Exemple** : Dans un amplificateur inverseur, si l'entrée non inverseuse est mise à la masse (0 V), l'AOP ajuste la sortie pour maintenir l'entrée inverseuse à environ 0 V.

- **Ouvert virtuel**
  - En raison de l'impédance d'entrée infinie, aucun courant ne circule dans les bornes d'entrée de l'AOP.
  - **Explication** : Cet "ouvert virtuel" signifie que les entrées agissent comme si elles étaient déconnectées du circuit en termes de flux de courant, permettant à tout le courant d'entrée de circuler à travers les composants externes.
  - **Exemple** : Dans un suiveur de tension, aucun courant ne circule dans les entrées de l'AOP, ce qui en fait un tampon idéal.

#### **Paramètres pratiques**
- **Slew Rate (Taux de montée)** : Taux de variation maximal de la tension de sortie (par exemple, 0,5 V/µs pour un AOP 741). Limite les performances à haute fréquence.
- **Courant de polarisation d'entrée** : Faibles courants (nA à pA) requis par les entrées des AOP réels.
- **Taux de réjection de l'alimentation (PSRR)** : Capacité à rejeter le bruit de l'alimentation.
- **Bruit** : Le bruit interne limite les performances dans les applications à faible signal.

---

### **2. Circuits typiques à AOP**

Les AOP sont généralement utilisés dans des configurations en boucle fermée avec une contre-réaction négative pour créer des circuits stables et prévisibles. Voici les circuits les plus courants : amplificateurs inverseurs et non inverseurs, intégrateurs et dérivateurs.

#### **Amplificateur inverseur**
- **Fonction** : Amplifie le signal d'entrée et inverse sa phase (décalage de phase de 180°).
- **Circuit** :
  - Le signal d'entrée (V_in) est appliqué à l'entrée inverseuse (-) via la résistance R1.
  - L'entrée non inverseuse (+) est mise à la masse (0 V).
  - Une résistance de contre-réaction (R_f) connecte la sortie (V_out) à l'entrée inverseuse.
- **Équations clés** :
  - Gain en tension : \\( A_v = -\frac{R_f}{R_1} \\)
  - Tension de sortie : \\( V_{out} = -\frac{R_f}{R_1} \cdot V_{in} \\)
  - Impédance d'entrée : Approximativement \\( R_1 \\).
- **Court-circuit virtuel** : L'entrée inverseuse est à 0 V (identique à l'entrée non inverseuse mise à la masse).
- **Exemple** : Pour \\( R_1 = 10 \, \text{k}\Omega \\), \\( R_f = 20 \, \text{k}\Omega \\), et \\( V_{in} = 1 \, \text{V} \\) :
  - Gain : \\( A_v = -\frac{20k}{10k} = -2 \\)
  - Sortie : \\( V_{out} = -2 \cdot 1 = -2 \, \text{V} \\).
- **Applications** : Amplificateurs audio, inversion de signal, amplificateurs sommateur.

#### **Amplificateur non inverseur**
- **Fonction** : Amplifie le signal d'entrée sans inversion de phase.
- **Circuit** :
  - Le signal d'entrée (V_in) est appliqué à l'entrée non inverseuse (+).
  - La résistance de contre-réaction (R_f) connecte la sortie à l'entrée inverseuse (-), avec la résistance R_1 connectée entre l'entrée inverseuse et la masse.
- **Équations clés** :
  - Gain en tension : \\( A_v = 1 + \frac{R_f}{R_1} \\)
  - Tension de sortie : \\( V_{out} = \left(1 + \frac{R_f}{R_1}\right) \cdot V_{in} \\)
  - Impédance d'entrée : Très élevée (en raison de l'entrée non inverseuse).
- **Court-circuit virtuel** : La tension de l'entrée inverseuse est égale à V_in (en raison de la contre-réaction).
- **Exemple** : Pour \\( R_1 = 10 \, \text{k}\Omega \\), \\( R_f = 30 \, \text{k}\Omega \\), et \\( V_{in} = 1 \, \text{V} \\) :
  - Gain : \\( A_v = 1 + \frac{30k}{10k} = 4 \\)
  - Sortie : \\( V_{out} = 4 \cdot 1 = 4 \, \text{V} \\).
- **Applications** : Tampon de signal, mise à l'échelle de tension.

#### **Intégrateur**
- **Fonction** : Intègre le signal d'entrée dans le temps, produisant une sortie proportionnelle à l'intégrale de l'entrée.
- **Circuit** :
  - Le signal d'entrée (V_in) est appliqué à l'entrée inverseuse via la résistance R.
  - Un condensateur (C) est placé dans le chemin de contre-réaction (de la sortie à l'entrée inverseuse).
  - L'entrée non inverseuse est mise à la masse.
- **Équations clés** :
  - Tension de sortie : \\( V_{out} = -\frac{1}{R \cdot C} \int V_{in}(t) \, dt \\)
  - La sortie est l'intégrale négative de l'entrée.
- **Court-circuit virtuel** : L'entrée inverseuse est à 0 V.
- **Considérations pratiques** :
  - Une résistance en parallèle avec le condensateur peut être ajoutée pour limiter le gain en basse fréquence et empêcher la saturation.
  - Limité par le slew rate de l'AOP et la fuite du condensateur.
- **Exemple** : Pour \\( R = 10 \, \text{k}\Omega \\), \\( C = 1 \, \mu\text{F} \\), et une tension constante \\( V_{in} = 1 \, \text{V} \\) :
  - Sortie : \\( V_{out} = -\frac{1}{10k \cdot 1\mu} \int 1 \, dt = -100 \cdot t \, \text{V/s} \\).
  - Après 1 ms : \\( V_{out} = -0.1 \, \text{V} \\).
- **Applications** : Ordinateurs analogiques, traitement du signal, filtres passe-bas.

#### **Dérivateur**
- **Fonction** : Dérive le signal d'entrée, produisant une sortie proportionnelle à la vitesse de variation de l'entrée.
- **Circuit** :
  - Le signal d'entrée (V_in) est appliqué via un condensateur (C) à l'entrée inverseuse.
  - Une résistance (R) est placée dans le chemin de contre-réaction.
  - L'entrée non inverseuse est mise à la masse.
- **Équations clés** :
  - Tension de sortie : \\( V_{out} = -R \cdot C \cdot \frac{dV_{in}}{dt} \\)
  - La sortie est la dérivée négative de l'entrée.
- **Court-circuit virtuel** : L'entrée inverseuse est à 0 V.
- **Considérations pratiques** :
  - Susceptible d'amplifier le bruit haute fréquence ; une petite résistance en série avec le condensateur d'entrée peut stabiliser le circuit.
- **Exemple** : Pour \\( R = 10 \, \text{k}\Omega \\), \\( C = 1 \, \mu\text{F} \\), et \\( V_{in} = t \, \text{V} \\) (rampe linéaire) :
  - Sortie : \\( V_{out} = -10k \cdot 1\mu \cdot \frac{d(t)}{dt} = -0.01 \, \text{V} \\).
- **Applications** : Détection de front, filtres passe-haut.

---

### **3. Applications non linéaires**

Les AOP peuvent fonctionner en modes non linéaires (sans contre-réaction négative ou avec des composants spécifiques) pour effectuer des tâches telles que la comparaison de signaux ou la génération de formes d'ondes.

#### **Comparateur**
- **Fonction** : Compare deux tensions d'entrée et délivre en sortie un signal haut ou bas selon laquelle est la plus grande.
- **Circuit** :
  - Une entrée (par exemple, V_ref) est appliquée à l'entrée non inverseuse (+).
  - L'autre entrée (V_in) est appliquée à l'entrée inverseuse (-).
  - Aucune contre-réaction (configuration en boucle ouverte).
- **Fonctionnement** :
  - Si V_in > V_ref, la sortie bascule vers la tension d'alimentation négative (par exemple, -V_cc).
  - Si V_in < V_ref, la sortie bascule vers la tension d'alimentation positive (par exemple, +V_cc).
- **Caractéristiques clés** :
  - Fonctionne en mode boucle ouverte, utilisant le gain élevé de l'AOP pour produire une sortie binaire.
  - Les AOP réels ont des slew rates finis, causant un léger retard dans la commutation.
- **Exemple** : Pour V_ref = 2 V et V_in = 3 V, avec des alimentations ±12 V :
  - Puisque V_in > V_ref, V_out ≈ -12 V.
- **Applications** :
  - Détecteurs de passage par zéro, détecteurs de seuil, conversion analogique-numérique.
- **Considérations pratiques** :
  - Ajouter une hystérésis (contre-réaction positive) pour éviter les oscillations près du seuil (configuration trigger de Schmitt).
  - Les circuits intégrés comparateurs dédiés (par exemple, LM339) sont souvent préférés pour une commutation plus rapide.

#### **Générateurs de formes d'ondes**
- **Fonction** : Générer des formes d'ondes périodiques (par exemple, carrée, triangulaire ou sinusoïdale) en utilisant des AOP avec des réseaux de contre-réaction.
- **Types** :
  1. **Générateur d'onde carrée (Multivibrateur astable)** :
     - **Circuit** : Utilise un AOP avec une contre-réaction positive via des résistances et un condensateur dans le chemin de contre-réaction négative.
     - **Fonctionnement** : Le condensateur se charge et se décharge entre des tensions de seuil fixées par les résistances, provoquant la commutation de la sortie entre les tensions d'alimentation.
     - **Fréquence** : Déterminée par la constante de temps RC, par exemple, \\( f = \frac{1}{2 \cdot R \cdot C \cdot \ln(3)} \\) (approximatif pour certaines configurations).
     - **Exemple** : Pour \\( R = 10 \, \text{k}\Omega \\), \\( C = 0.1 \, \mu\text{F} \\), la fréquence est d'environ 1 kHz.
     - **Applications** : Signaux d'horloge, génération d'impulsions.

  2. **Générateur d'onde triangulaire** :
     - **Circuit** : Combine généralement un générateur d'onde carrée (comparateur avec contre-réaction positive) avec un intégrateur.
     - **Fonctionnement** : L'onde carrée pilote l'intégrateur, produisant une rampe linéaire (onde triangulaire).
     - **Exemple** : Une onde carrée de 1 kHz appliquée à un intégrateur avec \\( R = 10 \, \text{k}\Omega \\), \\( C = 0.1 \, \mu\text{F} \\) produit une onde triangulaire de 1 kHz.
     - **Applications** : Signaux de test, modulation de largeur d'impulsion (PWM).

  3. **Générateur d'onde sinusoïdale (Oscillateur à pont de Wien)** :
     - **Circuit** : Utilise une contre-réaction positive via un réseau sélectif en fréquence (résistances et condensateurs) et une contre-réaction négative pour la stabilisation de l'amplitude.
     - **Fonctionnement** : Oscille à une fréquence où le déphasage est nul, par exemple, \\( f = \frac{1}{2 \pi R C} \\).
     - **Exemple** : Pour \\( R = 1.59 \, \text{k}\Omega \\), \\( C = 0.01 \, \mu\text{F} \\), la fréquence est d'environ 10 kHz.
     - **Applications** : Génération de signal audio, tests.

---

### **Considérations pratiques de conception**
1. **Alimentation** : Les AOP nécessitent des alimentations doubles (par exemple, ±12 V) ou simples (par exemple, 0 à 5 V pour les AOP rail-à-rail). Assurez-vous que la tension d'alimentation supporte la plage du signal d'entrée et de sortie.
2. **Sélection des composants** : Utilisez des résistances et des condensateurs de précision pour un gain et une réponse en fréquence précis. Consultez les datasheets des AOP pour les spécifications de bande passante, slew rate et bruit.
3. **Stabilité** : Évitez les oscillations en assurant une contre-réaction appropriée et en découplant les alimentations avec des condensateurs (par exemple, 0,1 µF près de l'AOP).
4. **Limitations** : Les AOP réels s'écartent du comportement idéal (par exemple, gain fini, bande passante, slew rate). Sélectionnez des AOP comme le LM358 (usage général), le TL081 (faible bruit) ou l'OPA2134 (qualité audio) en fonction des besoins de l'application.

---

### **Exemple d'application : Préamplificateur audio**
Concevons un simple préamplificateur audio inverseur :
- **Exigences** : Amplifier un signal audio de 50 mV à 500 mV (gain = 10).
- **Circuit** : Amplificateur inverseur avec \\( R_1 = 10 \, \text{k}\Omega \\), \\( R_f = 100 \, \text{k}\Omega \\).
- **Calcul** : \\( A_v = -\frac{100k}{10k} = -10 \\), \\( V_{out} = -10 \cdot 0.05 = -0.5 \, \text{V} \\).
- **Considérations** : Utilisez un AOP à faible bruit (par exemple, OPA2134), ajoutez un condensateur de couplage pour bloquer la composante continue et assurez-vous que l'alimentation supporte la plage du signal (par exemple, ±5 V).

---

### **Conclusion**
Les amplificateurs opérationnels sont des éléments fondamentaux en électronique analogique, offrant une flexibilité pour l'amplification, le traitement du signal et la génération de formes d'ondes. En comprenant leurs caractéristiques (court-circuit virtuel, ouvert virtuel, etc.) et en maîtrisant les circuits clés (amplificateurs inverseurs/non inverseurs, intégrateurs, dérivateurs, comparateurs, générateurs de formes d'ondes), vous pouvez concevoir une large gamme de circuits. Tenez toujours compte des limitations du monde réel et sélectionnez soigneusement les composants pour des performances optimales.

Pour approfondir, expérimentez avec des outils de simulation comme LTspice ou le prototypage sur plaque d'essai, et référez-vous aux datasheets des AOP pour des applications spécifiques.

---

Si vous souhaitez une simulation de circuit spécifique, une dérivation mathématique ou un graphique (par exemple, la réponse en fréquence d'un intégrateur), faites-le moi savoir et je pourrai fournir plus de détails ou des visualisations !