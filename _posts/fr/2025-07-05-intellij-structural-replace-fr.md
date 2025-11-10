---
audio: false
generated: true
lang: fr
layout: post
title: Maîtriser le remplacement structurel d'IntelliJ
translated: true
type: note
---

D'accord, décomposons la fonctionnalité de Remplacement Structurel d'IntelliJ IDEA.

Le Remplacement Structurel d'IntelliJ IDEA est une fonctionnalité incroyablement puissante, mais souvent sous-utilisée, qui vous permet de trouver et de remplacer des modèles de code en fonction de leur **structure** plutôt que de leur simple contenu textuel. Cela va bien au-delà d'une simple recherche et remplacement de texte, permettant des refactorisations complexes, l'application de normes de style de code et la correction de bogues dans une grande base de code.

Voici un guide complet :

-----

## IntelliJ IDEA Remplacement Structurel : Un Guide Complet

### 1. Qu'est-ce que la Recherche et le Remplacement Structurels (SSR) ?

Fondamentalement, la SSR dans IntelliJ IDEA consiste à travailler avec des Arbres de Syntaxe Abstraite (AST). Au lieu de rechercher des chaînes de caractères littérales, vous définissez un *modèle* qui décrit la structure du code que vous souhaitez trouver (Recherche Structurelle) et un autre modèle qui décrit comment vous souhaitez le transformer (Remplacement Structurel).

Cela vous permet de :

* **Refactoriser le code :** Changer la façon dont les méthodes sont appelées, réorganiser les paramètres, encapsuler les champs, etc.
* **Appliquer des standards de codage :** Assurer une utilisation cohérente de constructions de langage spécifiques ou d'appels d'API.
* **Corriger des bogues courants :** Identifier et corriger des erreurs logiques récurrentes.
* **Migrer des API :** Mettre à jour le code lorsque les bibliothèques ou les frameworks changent.
* **Nettoyer le code obsolète :** Trouver et remplacer les utilisations d'anciennes API par les nouvelles.

### 2. Accéder à la Recherche et au Remplacement Structurels

Vous pouvez accéder à la boîte de dialogue SSR de deux manières :

* **Aller dans Édition -> Rechercher -> Rechercher Structurellement...** (pour la recherche)
* **Aller dans Édition -> Rechercher -> Remplacer Structurellement...** (pour le remplacement direct)

La boîte de dialogue pour les deux est très similaire, "Remplacer Structurellement" ajoutant simplement un champ "Modèle de Remplacement".

### 3. Comprendre la Boîte de Dialogue de Recherche Structurelle

La boîte de dialogue de Recherche Structurelle est l'endroit où vous définissez votre modèle de recherche.

#### 3.1. Modèle de Recherche

C'est la partie la plus cruciale. Vous écrivez un extrait de code qui représente la *structure* que vous recherchez.

**Concepts Clés :**

* **Code Littéral :** Tout code que vous écrivez directement sera comparé littéralement.
* **Variables :** Utilisez des variables pour représenter les parties du code qui peuvent varier. Les variables sont définies à l'aide d'une syntaxe spéciale puis configurées avec des contraintes.
    * **Syntaxe variable courante :** `$nomVariable$` (entre signes dollar).
    * **Exemple :** `System.out.println($arg$);` trouvera tout appel `System.out.println`, où `$arg$` correspondra à ce qui se trouve à l'intérieur des parenthèses.

#### 3.2. Contraintes de Script (sur les variables)

Après avoir défini des variables dans votre "Modèle de Recherche", vous devez spécifier leurs contraintes. Cela se fait en sélectionnant la variable dans le modèle (ou en plaçant votre curseur dessus) puis en utilisant le bouton "Modifier les variables" (souvent une petite icône de crayon à côté du champ du modèle ou accessible via l'onglet "Variables").

Les contraintes courantes incluent :

* **Texte (regexp) :** Une expression régulière que le contenu textuel de la variable doit correspondre.
* **Type (regexp) :** Une expression régulière que le type de la variable doit correspondre (par exemple, `java.lang.String`, `int[]`).
* **Count :** Spécifie combien de fois un élément variable peut apparaître (par exemple, `[0, N]`, `[1, N]`, `[1, 1]`). Ceci est particulièrement utile pour les collections d'instructions ou les paramètres de méthode.
* **Référence :** Si la variable représente un identifiant (comme un nom de méthode ou un nom de variable), vous pouvez la contraindre à se référer à un type ou une déclaration spécifique.
* **Within :** Contraint la variable à être dans une certaine portée ou déclaration.
* **Not RegExp :** Exclut les correspondances basées sur une expression régulière.
* **Condition (script Groovy) :** C'est la contrainte la plus puissante. Vous pouvez écrire un script Groovy qui s'évalue à `true` ou `false`. Ce script a accès à l'élément correspondant et à ses propriétés, permettant une logique très complexe.
    * **Exemple de Script :** Pour vérifier si la valeur d'une variable entière est supérieure à 10 : `_target.text.toInteger() > 10` (où `_target` est l'élément correspondant pour la variable).

#### 3.3. Options

Sous le modèle, il y a diverses options pour affiner votre recherche :

* **Contexte :** Définit la portée de la recherche (par exemple, projet entier, module, répertoire, fichiers sélectionnés, portée personnalisée).
* **Type de fichier :** Restreint la recherche à des types de fichiers spécifiques (Java, Kotlin, XML, etc.).
* **Sensible à la casse :** Bascule standard de sensibilité à la casse.
* **Correspondre à la casse/mots entiers :** Applicable pour le texte dans le modèle.
* **Correspondre aux sauts de ligne :** Important pour les modèles multi-lignes.
* **Sauvegarder le modèle :** Sauvegarde votre modèle de recherche actuel pour une utilisation future.

### 4. Comprendre la Boîte de Dialogue de Remplacement Structurel

La boîte de dialogue de Remplacement Structurel ajoute un champ "Modèle de Remplacement" au "Modèle de Recherche" et aux "Variables" que vous définissez pour la recherche.

#### 4.1. Modèle de Remplacement

C'est là que vous définissez comment la structure de code trouvée doit être transformée.

* **Variables du Modèle de Recherche :** Vous pouvez utiliser les mêmes variables définies dans votre "Modèle de Recherche" dans le "Modèle de Remplacement". Le contenu correspondant à la variable dans la recherche sera inséré dans le modèle de remplacement.
* **Nouveau Code :** Vous pouvez introduire de nouveaux éléments de code, réorganiser ceux existants ou supprimer des parties.
* **Exemple :**
    * **Modèle de Recherche :** `System.out.println($arg$);`
    * **Modèle de Remplacement :** `LOGGER.info($arg$);`
    * Cela changerait `System.out.println("Hello");` en `LOGGER.info("Hello");`.

#### 4.2. Raccourcir les Noms Qualifiés Complets

Cette option (souvent activée automatiquement) tente de remplacer les noms de classe entièrement qualifiés (par exemple, `java.util.ArrayList`) par leurs noms courts (par exemple, `ArrayList`) et d'ajouter les instructions d'importation nécessaires. Ceci est crucial pour maintenir un code lisible.

#### 4.3. Formatage

IntelliJ IDEA reformatera généralement le code remplacé selon les paramètres de style de code de votre projet, ce qui est très souhaitable.

### 5. Exemples Pratiques

Illustrons avec quelques scénarios courants.

#### Exemple 1 : Remplacer `System.out.println` par un Logger

**Objectif :** Changer tous les `System.out.println("message");` en `LOGGER.info("message");` (en supposant que `LOGGER` est un champ static final).

1.  **Ouvrir le Remplacement Structurel :** `Édition -> Rechercher -> Remplacer Structurellement...`
2.  **Modèle de Recherche :**
    ```java
    System.out.println($arg$);
    ```
3.  **Variables :** Cliquez sur "Modifier les variables" ou allez dans l'onglet "Variables".
    * Sélectionnez `$arg$`.
    * **Count :** `[1, 1]` (un argument).
    * **Type (regexp) :** `java.lang.String` (si vous voulez seulement remplacer les littéraux de chaîne, sinon laissez vide pour n'importe quel type).
4.  **Modèle de Remplacement :**
    ```java
    LOGGER.info($arg$);
    ```
5.  **Exécuter :** Cliquez sur "Find" pour prévisualiser les changements, puis "Replace All" si vous êtes satisfait.

#### Exemple 2 : Permuter les Paramètres d'une Méthode

**Objectif :** Changer `someMethod(paramA, paramB)` en `someMethod(paramB, paramA)`.

1.  **Modèle de Recherche :**
    ```java
    someMethod($paramA$, $paramB$);
    ```
2.  **Variables :**
    * `$paramA$` : `Count: [1,1]`, `Type (regexp): .*` (n'importe quel type)
    * `$paramB$` : `Count: [1,1]`, `Type (regexp): .*` (n'importe quel type)
3.  **Modèle de Remplacement :**
    ```java
    someMethod($paramB$, $paramA$);
    ```

#### Exemple 3 : Encapsuler un Champ (Cas Simple)

**Objectif :** Si vous avez des champs publics comme `public String name;` et que vous voulez remplacer l'accès direct `obj.name` par `obj.getName()`. (Ceci est un exemple simplifié ; souvent, vous utiliseriez des refactorisations dédiées pour l'encapsulation).

1.  **Modèle de Recherche :**
    ```java
    $object$.$fieldName$;
    ```
2.  **Variables :**
    * `$object$` : `Count: [1,1]`, `Type (regexp): .*`
    * `$fieldName$` : `Count: [1,1]`, `Text (regexp): name` (cibler spécifiquement le champ `name`).
3.  **Modèle de Remplacement :**
    ```java
    $object$.get$fieldName$();
    ```
    * **Note :** Vous devrez peut-être ajuster la capitalisation si `get$fieldName$` ne capitalise pas automatiquement `name` en `Name`. Pour cela, vous pourriez utiliser un script Groovy sur `$fieldName$` dans le modèle de remplacement, mais cela devient plus complexe. Une approche plus simple pour ce cas spécifique est souvent d'utiliser deux SSR ou une refactorisation dédiée. Pour `get$fieldName$()`, l'IDE gère généralement la capitalisation pour les modèles de getters courants.

#### Exemple 4 : Trouver les Blocs `catch` Vides

**Objectif :** Trouver tous les blocs `catch` qui sont vides (ou qui ne contiennent que des commentaires/espaces blancs).

1.  **Modèle de Recherche :**
    ```java
    try {
        $statements$;
    } catch ($exceptionType$ $exceptionVariable$) {
        $emptyBody$;
    }
    ```
2.  **Variables :**
    * `$statements$` : `Count: [0, N]` (zéro ou plusieurs instructions dans le bloc try)
    * `$exceptionType$` : `Count: [1,1]`
    * `$exceptionVariable$` : `Count: [1,1]`
    * `$emptyBody$` : `Count: [0, 0]` (c'est la clé pour un corps vide)

#### Exemple 5 : Utiliser un Script Groovy pour des Conditions Avancées

**Objectif :** Trouver les instructions `if` où la condition est une constante `true`.

1.  **Modèle de Recherche :**
    ```java
    if ($condition$) {
        $thenBranch$;
    }
    ```
2.  **Variables :**
    * `$condition$` : `Count: [1,1]`
        * **Condition (script Groovy) :** `_target.text == "true"` (cela vérifie le texte littéral de la condition).
    * `$thenBranch$` : `Count: [0, N]`

### 6. Conseils et Bonnes Pratiques

* **Commencez Simple :** Commencez par des modèles de base et ajoutez progressivement de la complexité.
* **Utilisez d'abord `Find` :** Utilisez toujours "Find" (Recherche Structurelle) avant "Replace" pour prévisualiser les correspondances et vous assurer que votre modèle est correct.
* **Testez sur une Petite Portée :** Avant d'exécuter un remplacement à grande échelle, testez votre modèle sur un petit ensemble de fichiers isolés.
* **Sauvegardez les Modèles :** Sauvegardez les modèles fréquemment utilisés ou complexes pour une réutilisation facile.
* **Tirez Parti des Modèles Existants :** IntelliJ IDEA est livré avec de nombreux modèles de Recherche et Remplacement Structurels prédéfinis. Vous pouvez les trouver en cliquant sur l'icône "loupe avec un plus" dans la boîte de dialogue SSR et en parcourant les modèles existants. Ce sont d'excellentes ressources d'apprentissage.
* **La Puissance du Script Groovy :** Pour des correspondances très spécifiques ou sensibles au contexte, les scripts Groovy sont inestimables. Apprenez les bases de l'accès aux éléments (`_target`, `_target.parent`, `_target.text`, `_target.type`, etc.) dans le script.
* **Comprendre les Types de Correspondance :** Soyez conscient de ce que vos variables correspondent (par exemple, une instruction, une expression, un type, un nom de variable). Cela influence les contraintes que vous pouvez appliquer.
* **Expressions Régulières :** Une bonne compréhension des expressions régulières améliorera considérablement votre capacité à définir des contraintes `Text` et `Type`.
* **Débogage :** Si votre modèle ne correspond pas comme prévu, simplifiez-le. Supprimez les contraintes une par une jusqu'à ce qu'il commence à correspondre, puis réintroduisez-les pour identifier le problème.
* **Sauvegardez Votre Code :** Avant toute opération de remplacement structurel majeur sur une grande base de code, assurez-vous d'avoir une sauvegarde ou de travailler dans un système de contrôle de version où vous pouvez facilement annuler les changements.

### 7. Limitations

* **Complexité :** Les remplacements très complexes ou hautement contextuels peuvent être difficiles ou impossibles à exprimer uniquement avec la SSR. Parfois, un plugin IntelliJ IDEA personnalisé ou un script dédié pourrait être plus approprié.
* **Performance :** Les modèles extrêmement larges ou complexes exécutés sur une très grande base de code peuvent être lents.
* **Ambiguïté :** Soyez prudent avec les modèles trop généraux, car ils pourraient correspondre et modifier involontairement du code que vous ne souhaitiez pas.

-----

En maîtrisant la Recherche et le Remplacement Structurels d'IntelliJ IDEA, vous acquérez un outil puissant pour maintenir la qualité du code, effectuer des refactorisations à grande échelle et automatiser les modifications de code fastidieuses. C'est une fonctionnalité qui permet véritablement aux développeurs de travailler plus efficacement et de manière plus cohérente dans leurs projets.