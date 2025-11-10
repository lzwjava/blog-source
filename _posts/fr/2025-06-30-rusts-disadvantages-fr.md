---
audio: false
generated: true
lang: fr
layout: post
title: Les forces et les défis de Rust
translated: true
type: note
---

Rust est un langage de programmation très estimé, notamment pour la programmation système où la performance et la sécurité de la mémoire sont primordiales. Cependant, comme tout langage, il présente son propre ensemble d'inconvénients et de points de critique de la part des ingénieurs et des entreprises :

### 1. Courbe d'apprentissage abrupte

C'est sans doute la plainte la plus courante. Les fonctionnalités fondamentales de Rust, bien que puissantes, introduisent de nouveaux concepts qui peuvent être difficiles pour les développeurs, en particulier ceux venant de langages à gestion automatique de la mémoire (comme Python, Java ou Go) ou avec des systèmes de types moins stricts :

* **Propriété et Emprunt (Ownership and Borrowing) :** Ce modèle unique de gestion de la mémoire, imposé par le « vérificateur d'emprunt » (borrow checker), est le super-pouvoir de Rust pour la sécurité mémoire sans ramasse-miettes. Cependant, il nécessite une manière de penser complètement différente pour gérer la durée de vie des données et les références. Les développeurs se retrouvent souvent à « combattre le vérificateur d'emprunt » au début.
* **Durées de vie (Lifetimes) :** Les annotations de durée de vie explicites (`'a`) peuvent ajouter de la complexité et du bruit visuel, surtout dans le code générique, et nécessitent une compréhension approfondie de la validité des références de données.
* **Erreurs du Compilateur :** Bien que le compilateur de Rust soit connu pour ses messages d'erreur détaillés et utiles, ils peuvent tout de même être intimidants et nécessiter un effort significatif pour être compris et résolus, en particulier pour les débutants.
* **Surcharge de Concepts :** Rust intègre des concepts de divers paradigmes (fonctionnel, orienté objet, bas niveau), incluant les traits, les macros et le filtrage par motif (pattern matching), ce qui peut être beaucoup à assimiler en une fois.

### 2. Temps de compilation plus lents

Comparé à des langages comme Go, les temps de compilation de Rust peuvent être notablement plus lents, surtout pour les gros projets ou avec de nombreuses dépendances. Cela est dû à :

* **Analyse Statique Approfondie :** Le vérificateur d'emprunt et le système de types complexe effectuent des vérifications approfondies au moment de la compilation pour garantir la sécurité mémoire et prévenir les bogues de concurrence. Cette analyse, bien que bénéfique pour la sécurité à l'exécution, ajoute une surcharge à la compilation.
* **Monomorphisation et Génériques :** L'approche de Rust pour les génériques (monomorphization) génère un code spécialisé pour chaque type concret utilisé, ce qui peut augmenter la taille du binaire et le temps de compilation.
* **Gestion des Dépendances :** Bien que Cargo (le gestionnaire de paquets de Rust) soit excellent, les projets peuvent accumuler de nombreuses dépendances (crates), chacune nécessitant une compilation, ce qui peut contribuer à allonger les temps de construction.

### 3. Écosystème moins mature (par rapport aux langages plus anciens)

Bien qu'en croissance rapide, l'écosystème de Rust est encore plus jeune que celui de langages comme C++, Java ou Python. Cela peut entraîner :

* **Moins de Bibliothèques et d'Outils :** Bien que de nombreuses bibliothèques essentielles existent, vous pourriez trouver des lacunes ou des options moins matures pour des cas d'utilisation spécifiques par rapport à des langages plus établis. Cela peut signifier plus de « réinvention de la roue » ou le recours à des blocs `unsafe` pour FFI (Foreign Function Interface) avec des bibliothèques C/C++.
* **Support des EDI :** Bien que des outils comme `rust-analyzer` offrent une excellente intégration avec les EDI, l'expérience globale des outils pourrait ne pas être aussi fluide et riche en fonctionnalités que pour certains langages très matures.

### 4. Verbosité et Code Répétitif

Dans certaines situations, le code Rust peut être plus verbeux ou nécessiter plus de code répétitif que d'autres langages, surtout lorsqu'il s'agit de gérer les erreurs ou certains modèles de conception.

* **Gestion Explicite des Erreurs :** L'accent mis par Rust sur la gestion explicite des erreurs (en utilisant les énumérations `Result` et `Option` avec `match` ou l'opérateur `?`) est une force pour la fiabilité, mais cela peut conduire à plus de lignes de code par rapport aux langages qui reposent sur les exceptions.
* **Absence d'Arguments Étiquetés/Optionnels :** Cela peut parfois conduire à des signatures de fonction plus maladroites ou à la nécessité d'utiliser des modèles de construction (builder patterns) pour des configurations complexes.

### 5. Difficulté de Recrutement et d'Intégration

Pour les entreprises, la courbe d'apprentissage abrupte se traduit par des défis dans l'acquisition de talents et le temps de montée en compétence des nouveaux employés :

* **Bassin de Talents Plus Restreint :** Comparé aux langages largement adoptés comme Python ou JavaScript, le bassin de développeurs Rust expérimentés est plus petit, ce qui rend plus difficile de trouver et de recruter des talents.
* **Intégration Plus Longue :** Même les développeurs expérimentés ont besoin de temps pour devenir compétents dans les paradigmes uniques de Rust, ce qui peut impacter la productivité initiale et les calendriers des projets.

### 6. Mentalité « Rewrite It in Rust » (Une perception, plutôt qu'un inconvénient technique)

Certains dans la communauté expriment une inquiétude quant à une poussée enthousiaste, parfois dogmatique, pour « tout réécrire en Rust », même lorsque cela pourrait ne pas être la solution la plus pratique ou nécessaire pour un problème donné. Cela peut parfois conduire à du scepticisme ou de la résistance de la part de ceux qui sont en dehors de la communauté Rust immédiate.

### Conclusion

Malgré ces inconvénients, les points forts de Rust en matière de performance, de sécurité mémoire et de concurrence sont convaincants, ce qui en fait un choix solide pour la programmation système, le web assembly, les outils en ligne de commande et d'autres applications critiques pour la performance. Les plaintes proviennent souvent des compromis inhérents à un langage conçu pour de telles garanties solides, qui oblige les développeurs à apprendre une nouvelle façon de penser la programmation. À mesure que le langage et son écosystème mûrissent, certains de ces points sensibles sont susceptibles de s'atténuer.