---
audio: false
generated: true
lang: fr
layout: post
title: Conservation de l'énergie dans les boucles de circuit
translated: true
type: note
---

La loi des tensions de Kirchhoff (KVL) est un principe fondamental de l'analyse des circuits électriques. Elle est souvent appelée la deuxième loi de Kirchhoff ou la règle des mailles.

**L'idée centrale : La conservation de l'énergie**

La façon la plus simple de comprendre la loi des tensions de Kirchhoff est de penser à la **conservation de l'énergie**. Imaginez que vous marchiez le long d'un chemin fermé (une "maille") dans un circuit. En chemin, vous rencontrez différents composants comme des batteries et des résistances.

*   **Batteries (Sources de tension) :** Ces composants donnent de l'énergie aux charges du circuit. Ils "élèvent" l'énergie potentielle des charges, ce qui se traduit par une *élévation* de tension.
*   **Résistances (Charges) :** Ces composants consomment de l'énergie, en la convertissant en chaleur. Lorsque les charges les traversent, elles "perdent" de l'énergie potentielle, ce qui se traduit par une *chute* de tension.

La loi des tensions de Kirchhoff stipule que si vous partez d'un point quelconque d'une maille fermée, que vous parcourez la maille entière et que vous revenez à votre point de départ, **la somme algébrique de toutes les élévations et chutes de tension rencontrées doit être égale à zéro**.

**Pensez-y comme à des montagnes russes :**

Imaginez des montagnes russes.
*   La montée initiale est comme une batterie – elle ajoute de l'énergie potentielle au wagon.
*   Les descentes et les virages sont comme des résistances – le wagon perd de l'énergie potentielle (et gagne de l'énergie cinétique, mais celle-ci est éventuellement dissipée en chaleur ou en son).
*   Si le circuit des montagnes russes est une boucle fermée, lorsque le wagon revient au point de départ, son énergie potentielle totale (par rapport au point de départ) doit être la même que lorsqu'il est parti. Toute "élévation" de l'énergie potentielle due à la montée initiale doit être compensée par des "baisses" d'énergie potentielle le long du reste du parcours.

**Principes clés et comment appliquer la loi des tensions de Kirchhoff :**

1.  **Maille fermée :** La loi des tensions de Kirchhoff ne s'applique qu'à une maille fermée dans un circuit. Une maille est un chemin quelconque qui commence et se termine au même point sans répéter un nœud intermédiaire.
2.  **Somme algébrique :** Cela signifie que vous devez prendre en compte la *polarité* (le signe) de chaque tension.
    *   **Élévation de tension :** Si vous vous déplacez de la borne négative vers la borne positive d'un composant (comme une batterie), c'est une élévation de tension, et vous attribuez un signe positif à cette tension.
    *   **Chute de tension :** Si vous vous déplacez de la borne positive vers la borne négative d'un composant (comme une résistance où le courant circule du positif vers le négatif), c'est une chute de tension, et vous attribuez un signe négatif à cette tension. (Ou l'inverse, tant que vous êtes cohérent).
3.  **Cohérence de direction :** Choisissez une direction pour parcourir la maille (horaire ou anti-horaire) et respectez-la. Le résultat final sera le même quelle que soit la direction choisie, bien que les signes des termes individuels puissent s'inverser.
4.  **Énoncé mathématique :**
    \\(\sum V = 0\\)
    où \\(\sum V\\) représente la somme algébrique de toutes les tensions autour de la maille.

**Exemple :**

Considérons un circuit série simple avec une batterie (Tension \\(V_{source}\\)) et deux résistances (\\(R_1\\) et \\(R_2\\)).

Si le courant circule dans le sens horaire :
*   Lorsque vous traversez la batterie du négatif au positif, vous avez une élévation de tension (\\(+V_{source}\\)).
*   Lorsque vous traversez \\(R_1\\) dans le sens du courant, vous avez une chute de tension (\\(-V_1 = -IR_1\\)).
*   Lorsque vous traversez \\(R_2\\) dans le sens du courant, vous avez une chute de tension (\\(-V_2 = -IR_2\\)).

Application de la loi des tensions de Kirchhoff autour de la maille :
\\(V_{source} - V_1 - V_2 = 0\\)
ou
\\(V_{source} = V_1 + V_2\\)

Cette équation simple montre que la tension totale fournie par la source est répartie (ou chutée) aux bornes des résistances de la maille.

**Pourquoi la loi des tensions de Kirchhoff est-elle importante ?**

*   **Analyse de circuits :** La loi des tensions de Kirchhoff est indispensable pour analyser les circuits électriques, en particulier les circuits complexes avec plusieurs mailles et sources de tension.
*   **Résolution d'inconnues :** En établissant des équations de la loi des tensions de Kirchhoff pour diverses mailles, vous pouvez créer un système d'équations qui permet de résoudre les tensions, courants et résistances inconnus dans le circuit.
*   **Fondement pour d'autres méthodes :** La loi des tensions de Kirchhoff est une pierre angulaire pour des techniques d'analyse de circuits plus avancées comme l'analyse des mailles.

En substance, la loi des tensions de Kirchhoff est un outil puissant qui nous aide à comprendre comment l'énergie est distribuée et conservée dans un circuit électrique.