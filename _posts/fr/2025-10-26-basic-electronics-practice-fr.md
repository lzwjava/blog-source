---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Exercices pratiques de technologie électronique de base
translated: true
type: note
---

### Questions pratiques pour la technologie électronique de base (III) - 04730 (Examen national d'auto-apprentissage, 610201)

Pour vous aider à préparer l'examen, j'ai compilé une série de questions pratiques basées sur des sujets d'examens antérieurs. Ceci est un extrait partiel de l'examen national d'avril 2021, traduit en anglais pour plus de clarté. L'examen comprend généralement 15 questions à choix unique (1 point chacune), 15 questions à compléter (1 point chacune), des questions à réponse courte, des problèmes de calcul et des questions de conception/analyse. Les sujets couvrent l'analyse de circuits, les semi-conducteurs, les amplificateurs, les amplificateurs opérationnels, les alimentations et la logique numérique.

Concentrez-vous sur la compréhension de concepts comme la résonance, la polarisation des transistors, les circuits à ampli-op, la rectification et les portes logiques. Entraînez-vous aux calculs et à l'analyse de circuits.

#### Section 1 : Questions à choix unique (15 questions au total dans l'examen complet ; extrait partiel ici)
Chaque question vaut 1 point. Choisissez la bonne option.

1. Parmi les formes d'onde de tension suivantes, celle qui représente un signal de tension continue pulsée est :  
   (Note : Se réfère aux formes d'onde typiques ; généralement, celle avec une ondulation sur une ligne de base continue.)

4. La principale raison de la dérive du point zéro dans un circuit amplificateur multi-étages à couplage direct est :  
   A. Les erreurs de valeur des résistances  
   B. La dispersion des paramètres des transistors  
   C. Les effets de la température sur les paramètres des transistors  
   D. La tension d'alimentation instable

5. Pour un transistor fonctionnant dans la région active, si le courant de base \\( I_b \\) augmente de 12 μA à 22 μA, et que le courant de collecteur \\( I_c \\) passe de 1 mA à 2 mA, alors son gain en courant \\( \beta \\) est d'environ :  
   A. 83  
   B. 91  
   C. 100  
   D. 183

6. Pour superposer une tension continue sur une tension sinusoïdale, le circuit opérationnel approprié à utiliser est :  
   A. Un circuit opérationnel proportionnel  
   B. Un circuit opérationnel d'addition/soustraction  
   C. Un circuit opérationnel intégrateur  
   D. Un circuit opérationnel différentiateur

7. Dans un circuit opérationnel proportionnel non-inverseur construit avec un amplificateur opérationnel intégré, la tension d'entrée est de 1 V. Si la résistance de rétroaction est court-circuitée pour une raison quelconque, la tension de sortie du circuit opérationnel à ce moment est :  
   A. 0 V  
   B. 1 V  
   C. La sortie de saturation positive  
   D. La sortie de saturation négative

8. La tension moyenne mesurée aux bornes de la résistance de charge dans un circuit redresseur monophasé à demi-onde est de 4,5 V. Alors, la valeur efficace de la tension secondaire du transformateur \\( U \\) est :  
   A. 5 V  
   B. 7,07 V  
   C. 10 V  
   D. 14,14 V

9. Le régulateur de tension linéaire intégré CW78L15 peut fournir une tension de sortie \\( U \\) et un courant de sortie \\( I \\) de :  
   A. \\( U = +15 \\) V, \\( I = 0,1 \\) A  
   B. \\( U = -15 \\) V, \\( I = 0,1 \\) A  
   C. \\( U = +15 \\) V, \\( I = 0,5 \\) A  
   D. \\( U = -15 \\) V, \\( I = 0,5 \\) A

10. Le code BCD (8421) correspondant au nombre décimal (65)<sub>10</sub> est :  
    A. 11100101  
    B. 01100101  
    C. 10000010  
    D. 10000001

11. Dans toutes les conditions qui déterminent un événement, dès qu'une ou plusieurs conditions sont remplies, l'événement se produit. Ceci relève de :  
    A. La logique OU  
    B. La logique ET  
    C. La logique NON  
    D. La logique NON-OU

12. Parmi les affirmations suivantes concernant les minterms, la correcte est :  
    A. Pour tout minterm, un seul ensemble de valeurs des variables d'entrée le rend égal à 1  
    B. Pour les mêmes valeurs de variables, le produit de deux minterms quelconques est toujours 1  
    C. Sous des valeurs de variables arbitraires, la somme de tous les minterms est 0  
    D. Pour une fonction logique à n variables, il y a n minterms

13. Lorsque l'entrée d'un décodeur pour afficheur sept segments à anode commune est 0100, les sorties qui sont à 0 sont :  
    A. a, c, f, g  
    B. a, d, e  
    C. b, c, f, g  
    D. g, d, e

14. Ce qui suit appartient à un composant de circuit combinatoire est :  
    A. Un compteur synchrone  
    B. Un comparateur de données  
    C. Un registre à décalage  
    D. Un compteur asynchrone

15. Lors de la conception logique avec un PLA, l'expression de la fonction logique doit être exprimée comme :  
    A. L'expression "ET-OU" la plus simple  
    B. L'expression "OU-ET" la plus simple  
    C. L'expression "ET-OU" standard  
    D. L'expression "OU-ET" standard

#### Section 2 : Questions à compléter (15 questions au total dans l'examen complet ; extrait partiel ici)
Chaque blanc vaut 1 point. Remplissez le(s) mot(s) ou valeur(s) manquant(e)s.

16. Une bobine d'induction avec une réactance inductive de 10 Ω, lorsque la fréquence du signal de tension à ses bornes augmente d'un facteur 1 (double), sa valeur de réactance inductive est de ____ Ω.

17. La condition de résonance dans un circuit série RLC est ____.

18. Une lampe torche fonctionne à 3,2 V. Lorsque le filament chauffe, sa résistance est de 3,9 Ω. Le courant fourni par la batterie est d'environ ____ A (conserver une décimale).

19. Parmi les trois circuits amplificateurs de base construits avec des transistors bipolaires, celui dont le facteur d'amplification de tension est approximativement égal à 1 est le circuit amplificateur ____.

20. Lorsqu'une jonction PN est polarisée en direct, le courant est important ; lorsqu'elle est polarisée en inverse, le courant est très faible. Cette caractéristique est appelée la caractéristique ____ de la jonction PN.

21. Deux signaux de magnitude égale mais de polarité opposée sont appelés des signaux ____.

22. L'étage d'entrée d'un amplificateur opérationnel intégré adopte généralement un circuit ____.

*(Note : L'examen complet se poursuit avec d'autres questions à compléter, des réponses courtes comme expliquer le court-circuit virtuel/la masse virtuelle des ampli-op, des schémas de circuit pour l'analyse, des calculs pour les gains des amplificateurs, l'efficacité des redresseurs, et des problèmes de conception numérique comme les tables de vérité ou les tableaux de Karnaugh.)*

### Conseils pour la préparation
- **Revoyez les sujets clés** : Signaux sinusoïdaux, réseaux passifs, semi-conducteurs (diodes/transistors), amplificateurs à BJT (émetteur commun, suiveur d'émetteur), ampli-ops (inverseur/non-inverseur, intégrateurs), redresseurs/filtres, régulateurs de tension, logique numérique (portes, bascules, compteurs, décodeurs).
- **Entraînez-vous aux calculs** : Utilisez la loi d'Ohm, les lois de Kirchhoff, les formules de résonance (\\( f = 1/(2\pi\sqrt{LC}) \\)), les équations des transistors (\\( I_c = \beta I_b \\)), les gains des ampli-op (\\( A = -R_f/R_{in} \\)).
- **Structure de l'examen** : 100 points au total, 150 minutes. Viser 60% pour réussir.
- Pour les sujets d'examens antérieurs complets et les réponses, téléchargez-les depuis des sites fiables d'auto-examen (souvent en PDF). Entraînez-vous en conditions chronométrées.

### Références
- [Questions d'examen d'avril 2021 (source partielle)](https://mzk.cwjedu.com/lnzt/8222)
- [Collection de sujets d'examens antérieurs](https://www.zikaosw.cn/lnzt/subject-799.html)
- [Discussion sur l'examen d'avril 2023](https://www.bilibili.com/read/cv25932203/)
- [Exemples de questions d'analyse](https://wenku.baidu.com/view/a2a96333b90d6c85ec3ac6bf.html)