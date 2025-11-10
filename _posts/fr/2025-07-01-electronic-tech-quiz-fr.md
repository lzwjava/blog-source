---
audio: false
generated: true
lang: fr
layout: post
title: Quiz d'auto-apprentissage en technologie électronique
translated: true
type: note
---

Voici un exemple de quiz conçu pour un examen d'auto-apprentissage basé sur le plan fourni pour *Fondamentaux de la Technologie Électronique (III)*, édité par Wen Xidong et publié par Economic Science Press. Le quiz couvre les concepts clés de l'électronique analogique, de l'électronique numérique et des applications pratiques, conçu pour tester la compréhension fondamentale adaptée à un examen d'auto-apprentissage en Chine. Les questions sont un mélange de formats à choix multiples, à réponse courte et de résolution de problèmes pour refléter les styles d'examen typiques.

---

### Exemple de Quiz : Fondamentaux de la Technologie Électronique (III)
**Examen d'Auto-apprentissage**
**Instructions** : Répondez à toutes les questions. Montrez vos calculs pour les questions de résolution de problèmes. Chaque question vaut le nombre de points indiqué. Total : 100 points.

---

#### Partie I : Électronique Analogique (40 points)

1.  **Choix Multiple : Analyse de Circuits (5 points)**
    Laquelle des propositions suivantes décrit correctement la Loi des Tensions de Kirchhoff (LTC) ?
    a) La somme des courants entrants à un nœud est égale à la somme des courants sortants.
    b) La somme des chutes de tension autour d'une boucle fermée est égale à zéro.
    c) La résistance totale dans un circuit en série est la somme des résistances individuelles.
    d) La tension aux bornes de branches parallèles est différente.
    **Réponse** : b) La somme des chutes de tension autour d'une boucle fermée est égale à zéro.

2.  **Réponse Courte : Configurations d'Amplificateurs (10 points)**
    Expliquez brièvement la différence entre les configurations Émetteur Commun (EC) et Collecteur Commun (CC) d'un amplificateur à BJT en termes de leurs caractéristiques d'entrée/sortie et de leurs applications typiques.
    **Exemple de Réponse** :
    - **Configuration EC** : Gain en tension élevé, impédance d'entrée modérée et sortie inversée. Utilisée dans les applications nécessitant une amplification, comme les amplificateurs audio.
    - **Configuration CC** : Gain en tension unitaire, impédance d'entrée élevée, faible impédance de sortie, sortie non inversée. Souvent utilisée comme tampon ou étage d'adaptation d'impédance.

3.  **Résolution de Problème : Amplificateurs Opérationnels (15 points)**
    Un circuit amplificateur opérationnel inverseur a une résistance de contre-réaction \\( R_f = 10 \, \text{k}\Omega \\) et une résistance d'entrée \\( R_{\text{in}} = 2 \, \text{k}\Omega \\). La tension d'entrée est \\( V_{\text{in}} = 1 \, \text{V} \\).
    a) Calculez la tension de sortie \\( V_{\text{out}} \\).
    b) Quel est le gain du circuit ?
    **Solution** :
    a) Pour un ampli-op inverseur, \\( V_{\text{out}} = -\left(\frac{R_f}{R_{\text{in}}}\right) V_{\text{in}} = -\left(\frac{10 \, \text{k}\Omega}{2 \, \text{k}\Omega}\right) \cdot 1 \, \text{V} = -5 \, \text{V} \\).
    b) Gain \\( A = -\frac{R_f}{R_{\text{in}}} = -\frac{10}{2} = -5 \\).

4.  **Choix Multiple : Alimentations à Courant Continu (10 points)**
    Quel est un avantage clé d'un régulateur à découpage par rapport à un régulateur linéaire ?
    a) Coût inférieur
    b) Efficacité supérieure
    c) Conception plus simple
    d) Meilleure régulation de la tension
    **Réponse** : b) Efficacité supérieure

---

#### Partie II : Électronique Numérique (40 points)

5.  **Choix Multiple : Portes Logiques (5 points)**
    Quelle porte logique produit une sortie de 1 uniquement lorsque toutes ses entrées sont à 0 ?
    a) AND
    b) OR
    c) NOR
    d) XOR
    **Réponse** : c) NOR

6.  **Réponse Courte : Logique Combinatoire (10 points)**
    Décrivez la fonction d'un multiplexeur et fournissez une application pratique.
    **Exemple de Réponse** : Un multiplexeur sélectionne l'un des plusieurs signaux d'entrée et le transmet à une sortie unique en fonction des lignes de sélection. Il agit comme un sélecteur de données. **Application** : Utilisé dans les systèmes de communication pour acheminer plusieurs flux de données sur un seul canal.

7.  **Résolution de Problème : Logique Séquentielle (15 points)**
    Conception d'un compteur binaire montant de 3 bits utilisant des bascules JK. Fournissez la table d'état et décrivez l'opération pour un cycle d'horloge à partir de l'état 010 (binaire 2).
    **Solution** :
    - **Table d'État** :
      | État Présent (Q2 Q1 Q0) | État Suivant (Q2 Q1 Q0) | Entrées JK (J2 K2 | J1 K1 | J0 K0) |
      |-------------------------|-----------------------|-----------------------|
      | 010                     | 011                   | 0 0 | 0 0 | 1 1 |
    - **Opération** : À partir de l'état 010, au cycle d'horloge suivant, Q0 bascule (0 → 1), Q1 et Q2 restent inchangés, ce qui donne 011 (binaire 3). J0 = K0 = 1 pour basculer Q0 ; les autres sont indifférents ou à 0.

8.  **Choix Multiple : Dispositifs Logiques Programmables (10 points)**
    Laquelle des propositions suivantes est une caractéristique d'un FPGA ?
    a) Structure logique fixe
    b) Blocs logiques et interconnexions reprogrammables
    c) Prend uniquement en charge les circuits analogiques
    d) Ne peut pas être programmé en utilisant HDL
    **Réponse** : b) Blocs logiques et interconnexions reprogrammables

---

#### Partie III : Applications Pratiques (20 points)

9.  **Réponse Courte : Outils de Simulation (10 points)**
    Expliquez le rôle des outils de simulation comme Multisim dans la conception de circuits électroniques. Pourquoi sont-ils utiles pour les étudiants apprenant les *Fondamentaux de la Technologie Électronique* ?
    **Exemple de Réponse** : Multisim permet aux étudiants de concevoir, simuler et tester des circuits virtuellement avant de les construire, réduisant ainsi les erreurs et les coûts. Il aide à visualiser le comportement des circuits (par exemple, tension, courant) et à expérimenter avec les paramètres, améliorant la compréhension de concepts comme les amplificateurs et les circuits logiques.

10. **Résolution de Problème : Systèmes Mixtes (10 points)**
    Un système de surveillance de température utilise un capteur analogique délivrant 0–5 V et un affichage numérique via un CAN 3 bits. Si la tension de référence du CAN est de 5 V, calculez le pas de tension et la sortie numérique pour une lecture du capteur de 3,75 V.
    **Solution** :
    - Pas de tension = \\( \frac{V_{\text{ref}}}{2^n} = \frac{5 \, \text{V}}{2^3} = 0,625 \, \text{V} \\).
    - Sortie numérique = \\( \text{floor}\left(\frac{3,75}{0,625}\right) = \text{floor}(6) = 110 \\) (binaire).

---

### Notes pour la Préparation à l'Examen d'Auto-apprentissage en Chine
- **Structure** : Le quiz est conçu pour s'aligner sur le format des examens d'auto-apprentissage en Chine, qui met souvent l'accent sur la compréhension théorique, la résolution de problèmes et les applications pratiques. Les questions sont équilibrées pour tester la mémoire, l'analyse et les compétences en conception.
- **Conseils d'Étude** :
  - Concentrez-vous sur la maîtrise des lois fondamentales (par exemple, Ohm, Kirchhoff) et de leurs applications.
  - Entraînez-vous à concevoir des circuits de base (par exemple, amplificateurs, compteurs) en utilisant des composants standard.
  - Utilisez des outils de simulation comme Multisim ou Proteus pour vérifier vos conceptions.
  - Revoyez minutieusement les caractéristiques des semi-conducteurs et le fonctionnement des portes logiques.
- **Ressources** : Le manuel *Fondamentaux de la Technologie Électronique (III)* par Wen Xidong (Economic Science Press) est la ressource principale. Complétez avec des tutoriels en ligne ou des plateformes comme Coursera pour les simulations de circuits et les bases du HDL.
- **Contexte de l'Examen** : Les examens d'auto-apprentissage en Chine, tels que ceux administrés par le National Education Examinations Authority (NEEA), nécessitent une préparation disciplinée. Les annales (si disponibles) et les exercices de chapitre du manuel sont essentiels pour réussir.

Si vous souhaitez des questions supplémentaires, des sujets spécifiques mis en avant ou une concentration sur des questions liées aux travaux pratiques, faites-le moi savoir ! Je peux également fournir un corrigé plus détaillé ou adapter le quiz à un format d'examen spécifique.