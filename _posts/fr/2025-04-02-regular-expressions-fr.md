---
audio: false
generated: true
lang: fr
layout: post
title: Expressions régulières
translated: true
type: note
---

Les expressions régulières, souvent abrégées en "regex" ou "regexp", sont un outil puissant et polyvalent pour la recherche de motifs dans le texte. Elles offrent un moyen concis et flexible de rechercher, manipuler et valider des chaînes de caractères en fonction de modèles définis. Bien que la syntaxe puisse sembler intimidante au premier abord, la maîtrise des regex peut considérablement améliorer vos capacités de traitement de texte dans divers langages de programmation, éditeurs de texte et outils en ligne de commande.

Ce guide vous accompagnera des concepts de base aux concepts plus avancés des expressions régulières.

**I. Les Fondamentaux : Les Éléments de Base des Regex**

À la base, une regex est une séquence de caractères qui définit un modèle de recherche. Ces caractères peuvent être littéraux (correspondant à eux-mêmes) ou spéciaux (ayant une signification spécifique).

**A. Caractères Littéraux :**

La plupart des caractères dans une regex se correspondent littéralement. Par exemple :

* `abc` correspondra à la séquence exacte "abc" dans une chaîne.
* `123` correspondra à la séquence exacte "123".
* `hello` correspondra à la séquence exacte "hello".

**B. Métacaractères : Les Pouvoirs Spéciaux**

Les métacaractères sont les éléments de base qui donnent sa puissance aux regex. Ils ont une signification spéciale et ne se correspondent pas littéralement. Voici les plus courants :

1.  **`.` (Point) :** Correspond à n'importe quel caractère unique *sauf* un saut de ligne (`\n` par défaut).
    * `a.c` correspondra à "abc", "adc", "a1c", "a c", mais pas à "ac" ou "abbc".

2.  **`^` (Accent Circonflexe) :**
    * **À l'intérieur d'une classe de caractères (voir ci-dessous) :** Nie l'ensemble, correspondant à tout caractère *non* présent dans l'ensemble.
    * **En dehors d'une classe de caractères :** Correspond au début d'une chaîne (ou au début d'une ligne en mode multiligne).
        * `^hello` correspondra à "hello world" mais pas à "say hello".

3.  **`$` (Signe Dollar) :** Correspond à la fin d'une chaîne (ou à la fin d'une ligne en mode multiligne).
    * `world$` correspondra à "hello world" mais pas à "world hello".

4.  **`*` (Astérisque) :** Correspond au caractère ou au groupe précédent zéro fois ou plus.
    * `ab*c` correspondra à "ac", "abc", "abbc", "abbbc", etc.

5.  **`+` (Signe Plus) :** Correspond au caractère ou au groupe précédent une fois ou plus.
    * `ab+c` correspondra à "abc", "abbc", "abbbc", mais pas à "ac".

6.  **`?` (Point d'Interrogation) :**
    * Correspond au caractère ou au groupe précédent zéro ou une fois (le rendant optionnel).
        * `ab?c` correspondra à "ac" et "abc", mais pas à "abbc".
    * Utilisé comme modificateur de quantificateur pour rendre une correspondance non gourmande (voir section Quantificateurs).

7.  **`{}` (Accolades) :** Spécifie le nombre exact ou la plage d'occurrences du caractère ou du groupe précédent.
    * `a{3}` correspond exactement à trois "a" (par exemple, "aaa").
    * `a{2,4}` correspond entre deux et quatre "a" (par exemple, "aa", "aaa", "aaaa").
    * `a{2,}` correspond à deux "a" ou plus (par exemple, "aa", "aaa", "aaaa", ...).

8.  **`[]` (Crochets) :** Définit une classe de caractères, correspondant à n'importe quel caractère unique à l'intérieur des crochets.
    * `[abc]` correspondra à "a", "b" ou "c".
    * `[a-z]` correspondra à n'importe quelle lettre minuscule de "a" à "z" (plage).
    * `[0-9]` correspondra à n'importe quel chiffre de "0" à "9".
    * `[A-Za-z0-9]` correspondra à n'importe quel caractère alphanumérique.
    * `[^abc]` (avec `^` au début) correspondra à n'importe quel caractère *sauf* "a", "b" ou "c".

9.  **`\` (Barre Oblique Inverse) :** Échappe le caractère suivant, traitant un métacaractère comme un caractère littéral ou introduisant une séquence de caractères spéciaux.
    * `\.` correspondra à un point littéral ".".
    * `\*` correspondra à un astérisque littéral "*".
    * `\d` correspond à n'importe quel chiffre (équivalent à `[0-9]`).
    * `\D` correspond à n'importe quel caractère non chiffre (équivalent à `[^0-9]`).
    * `\s` correspond à n'importe quel caractère d'espacement (espace, tabulation, saut de ligne, etc.).
    * `\S` correspond à n'importe quel caractère non-espace.
    * `\w` correspond à n'importe quel caractère de mot (alphanumérique et tiret bas, équivalent à `[a-zA-Z0-9_]`).
    * `\W` correspond à n'importe quel caractère non-mot (équivalent à `[^a-zA-Z0-9_]`).
    * `\b` correspond à une frontière de mot (la position entre un caractère de mot et un caractère non-mot).
    * `\B` correspond à une non-frontière de mot.
    * `\n` correspond à un caractère de saut de ligne.
    * `\r` correspond à un caractère de retour chariot.
    * `\t` correspond à un caractère de tabulation.

10. **`|` (Barre Verticale) :** Agit comme un opérateur "OU", correspondant soit à l'expression avant, soit à l'expression après la barre.
    * `cat|dog` correspondra à "cat" ou "dog".

11. **`()` (Parenthèses) :**
    * **Regroupement :** Regroupe des parties d'une regex, vous permettant d'appliquer des quantificateurs ou l'opérateur OU à l'ensemble du groupe.
        * `(ab)+c` correspondra à "abc", "ababc", "abababc", etc.
        * `(cat|dog) food` correspondra à "cat food" ou "dog food".
    * **Groupes de Capture :** Capture le texte correspondant à l'expression entre les parenthèses. Ces groupes capturés peuvent être référencés ultérieurement (par exemple, pour le remplacement ou l'extraction).

**II. Quantificateurs : Contrôler la Répétition**

Les quantificateurs spécifient combien de fois un élément précédent (caractère, groupe ou classe de caractères) peut se produire.

* `*` : Zéro fois ou plus
* `+` : Une fois ou plus
* `?` : Zéro ou une fois
* `{n}` : Exactement `n` fois
* `{n,}` : `n` fois ou plus
* `{n,m}` : Entre `n` et `m` fois (inclusif)

**Correspondance Gourmande vs Non Gourmande :**

Par défaut, les quantificateurs sont **gourmands**, ce qui signifie qu'ils essaient de correspondre à autant de caractères que possible dans la chaîne. Vous pouvez rendre un quantificateur **non gourmand** (ou paresseux) en ajoutant un `?` après celui-ci. Les quantificateurs non gourmands essaient de correspondre à la chaîne la plus courte possible.

* `a.*b` (gourmand) sur "axxbxb" correspondra à "axxbxb".
* `a.*?b` (non gourmand) sur "axxbxb" correspondra à "axb" puis à "xb".

**III. Ancres : Spécifier la Position**

Les ancres ne correspondent à aucun caractère elles-mêmes, mais affirment une position dans la chaîne.

* `^` : Correspond au début de la chaîne (ou de la ligne).
* `$` : Correspond à la fin de la chaîne (ou de la ligne).
* `\b` : Correspond à une frontière de mot.
* `\B` : Correspond à une non-frontière de mot.

**IV. Classes de Caractères : Ensembles Prédéfinis**

Les classes de caractères fournissent des raccourcis pour les ensembles de caractères couramment utilisés.

* `\d` : Correspond à n'importe quel chiffre (0-9).
* `\D` : Correspond à n'importe quel caractère non chiffre.
* `\s` : Correspond à n'importe quel caractère d'espacement (espace, tabulation, saut de ligne, retour chariot, saut de page).
* `\S` : Correspond à n'importe quel caractère non-espace.
* `\w` : Correspond à n'importe quel caractère de mot (alphanumérique et tiret bas : a-zA-Z0-9_).
* `\W` : Correspond à n'importe quel caractère non-mot.

**V. Regroupement et Capture**

Les parenthèses `()` servent à deux fins principales :

* **Regroupement :** Permet d'appliquer des quantificateurs ou l'opérateur OU à une séquence de caractères.
* **Capture :** Crée un groupe de capture, qui stocke la partie de la chaîne qui correspond à l'expression entre les parenthèses. Ces groupes capturés peuvent être consultés et utilisés pour des références arrière ou des remplacements.

**Références Arrière :**

Vous pouvez vous référer à des groupes capturés précédemment dans la même regex en utilisant `\1`, `\2`, `\3`, etc., où le numéro correspond à l'ordre de la parenthèse ouvrante du groupe de capture.

* `(.)\1` correspondra à n'importe quel caractère suivi du même caractère (par exemple, "aa", "bb", "11").
* `(\w+) \1` correspondra à un mot suivi d'un espace puis du même mot (par exemple, "hello hello").

**Groupes Non Capturants :**

Si vous avez besoin de regrouper des parties d'une regex sans créer un groupe de capture, vous pouvez utiliser `(?:...)`. Ceci est utile pour des raisons de clarté ou de performance.

* `(?:ab)+c` correspondra à "abc", "ababc", etc., mais ne capturera pas "ab".

**VI. Assertions Arrière/Avant : Affirmations Sans Consommation**

Les assertions arrière/avant sont des assertions de largeur nulle qui vérifient la présence d'un motif avant ou après la position actuelle dans la chaîne sans inclure la partie correspondante de l'assertion dans la correspondance globale.

* **Assertion Avant Positive `(?=...)` :** Affirme que le motif à l'intérieur des parenthèses doit suivre la position actuelle.
    * `\w+(?=:)` correspondra à n'importe quel mot suivi d'un deux-points, mais le deux-points lui-même ne fera pas partie de la correspondance (par exemple, dans "name:", il correspondra à "name").

* **Assertion Avant Négative `(?!...)` :** Affirme que le motif à l'intérieur des parenthèses *ne doit pas* suivre la position actuelle.
    * `\w+(?!:)` correspondra à n'importe quel mot non suivi d'un deux-points (par exemple, dans "name value", il correspondra à "name" et "value").

* **Assertion Arrière Positive `(?<=...)` :** Affirme que le motif à l'intérieur des parenthèses doit précéder la position actuelle. Le motif à l'intérieur de l'assertion arrière doit avoir une largeur fixe (pas de quantificateurs variables comme `*` ou `+`).
    * `(?<=\$)\d+` correspondra à un ou plusieurs chiffres précédés d'un signe dollar, mais le signe dollar lui-même ne fera pas partie de la correspondance (par exemple, dans "$100", il correspondra à "100").

* **Assertion Arrière Négative `(?<!...)` :** Affirme que le motif à l'intérieur des parenthèses *ne doit pas* précéder la position actuelle. Le motif à l'intérieur de l'assertion arrière doit avoir une largeur fixe.
    * `(?<!\$)\d+` correspondra à un ou plusieurs chiffres non précédés d'un signe dollar (par exemple, dans "100$", il correspondra à "100").

**VII. Drapeaux (Modificateurs) : Contrôler le Comportement des Regex**

Les drapeaux (ou modificateurs) sont utilisés pour modifier le comportement du moteur d'expressions régulières. Ils sont généralement spécifiés au début ou à la fin du motif regex, selon l'implémentation. Les drapeaux courants incluent :

* **`i` (Insensible à la casse) :** Rend la correspondance insensible à la casse. `[a-z]` correspondra aux lettres minuscules et majuscules.
* **`g` (Global) :** Trouve toutes les correspondances dans la chaîne, pas seulement la première.
* **`m` (Multiligne) :** Fait que `^` et `$` correspondent au début et à la fin de chaque ligne (délimitées par `\n` ou `\r`) au lieu du début et de la fin de la chaîne entière.
* **`s` (Dotall / Single line) :** Fait que le métacaractère `.` corresponde à n'importe quel caractère, y compris les sauts de ligne.
* **`u` (Unicode) :** Active la prise en charge complète d'Unicode pour les classes de caractères et autres fonctionnalités.
* **`x` (Étendu / Verbeux) :** Permet d'écrire des regex plus lisibles en ignorant les espaces et les commentaires dans le motif (utile pour les regex complexes).

**VIII. Applications Pratiques des Regex**

Les regex sont utilisées de manière intensive dans divers domaines :

* **Éditeurs de Texte (par exemple, Notepad++, Sublime Text, VS Code) :** Recherche et remplacement de texte basés sur des motifs.
* **Langages de Programmation (par exemple, Python, JavaScript, Java, C#) :**
    * Validation des entrées utilisateur (par exemple, adresses e-mail, numéros de téléphone, URLs).
    * Extraction d'informations spécifiques à partir de texte (par exemple, dates, numéros, balises).
    * Remplacement de parties d'une chaîne basé sur un motif.
    * Analyse de fichiers journaux ou d'autres données textuelles structurées.
* **Outils en Ligne de Commande (par exemple, `grep`, `sed`, `awk`) :** Recherche et manipulation de fichiers texte.
* **Développement Web :** Validation de formulaire, routage d'URL, traitement de contenu.
* **Science des Données :** Nettoyage de données, extraction de données, reconnaissance de motifs.
* **Sécurité :** Détection d'intrusion, analyse de journaux.

**IX. Regex dans Différents Langages de Programmation**

La plupart des langages de programmation modernes ont une prise en charge intégrée des expressions régulières, bien que la syntaxe spécifique et les fonctionnalités puissent varier légèrement. Vous trouverez généralement les fonctionnalités regex dans les bibliothèques standard ou les modules.

* **Python :** Le module `re`.
* **JavaScript :** L'objet intégré `RegExp` et les méthodes de chaîne comme `match()`, `replace()`, `search()`, `split()`.
* **Java :** Le package `java.util.regex`.
* **C# (.NET) :** L'espace de noms `System.Text.RegularExpressions`.
* **PHP :** Les fonctions comme `preg_match()`, `preg_replace()`, `preg_match_all()`.

**X. Conseils pour Écrire des Regex Efficaces**

* **Commencez Simple :** Commencez par un motif de base et ajoutez progressivement de la complexité.
* **Testez Fréquemment :** Utilisez des testeurs de regex en ligne ou les outils regex de votre langage de programmation pour tester vos motifs sur des exemples de données.
* **Soyez Spécifique :** Évitez les motifs trop larges qui pourraient correspondre à du texte non souhaité.
* **Utilisez les Classes de Caractères et les Quantificateurs avec Sagesse :** Ils sont puissants mais peuvent aussi conduire à des comportements inattendus s'ils ne sont pas utilisés correctement.
* **Comprenez la Correspondance Gourmande vs Non Gourmande :** Choisissez le comportement approprié à vos besoins.
* **Utilisez le Regroupement et la Capture avec Jugement :** Capturez seulement ce dont vous avez besoin. Utilisez des groupes non capturants lorsque la capture n'est pas requise.
* **Documentez Vos Regex :** Pour les motifs complexes, ajoutez des commentaires (surtout lors de l'utilisation du drapeau `x`) pour expliquer leur objectif.
* **Considérez les Cas Limites :** Pensez aux différentes variations du texte d'entrée et assurez-vous que votre regex les gère correctement.
* **Décomposez les Problèmes Complexes :** Si vous avez une tâche de correspondance très complexe, envisagez de la décomposer en plusieurs motifs regex plus simples.

**XI. Ressources d'Apprentissage**

* **Testeurs de Regex en Ligne :** regex101.com, regexr.com, regextester.com
* **Documentation Spécifique au Langage :** Reportez-vous à la documentation regex de votre langage de programmation choisi.
* **Tutoriels et Cours en Ligne :** Des plateformes comme Coursera, Udemy et YouTube proposent des cours complets sur les regex.
* **Livres :** "Mastering Regular Expressions" de Jeffrey Friedl est une ressource très recommandée.

**Conclusion**

Les expressions régulières sont un outil indispensable pour toute personne travaillant avec des données textuelles. Bien que la courbe d'apprentissage initiale puisse sembler raide, la capacité de rechercher, manipuler et valider efficacement du texte en fonction de modèles complexes est une compétence précieuse. En comprenant les concepts fondamentaux, les métacaractères, les quantificateurs et autres fonctionnalités des regex, vous pouvez considérablement améliorer votre productivité et vos capacités de résolution de problèmes dans un large éventail d'applications. La pratique est la clé pour maîtriser les regex, alors n'hésitez pas à expérimenter et à explorer différents modèles pour diverses tâches de traitement de texte.