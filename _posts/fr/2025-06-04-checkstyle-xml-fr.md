---
audio: false
generated: true
lang: fr
layout: post
title: Configuration de Checkstyle
translated: true
type: note
---

Il s'agit d'un fichier de configuration Checkstyle écrit en XML, conçu pour appliquer des standards de codage et des bonnes pratiques pour le code Java basé sur les conventions de codage Sun, la spécification du langage Java, les directives Javadoc et quelques bonnes pratiques supplémentaires. Checkstyle est un outil d'analyse statique de code qui vérifie le code source Java pour s'assurer qu'il respecte un ensemble de règles définies. Ci-dessous, je vais expliquer la structure et les composants clés de ce fichier de configuration.

---

### **Aperçu**
- **Objectif** : Le fichier définit des règles pour vérifier les fichiers Java, properties et XML afin de détecter les violations des standards de codage, telles que le formatage, les conventions de nommage, les exigences Javadoc et la structure du code.
- **Structure** : La configuration est organisée hiérarchiquement à l'aide d'éléments `<module>`, commençant par un module racine `Checker`, qui contient d'autres modules pour des vérifications ou des filtres spécifiques.
- **Standards** : Il est aligné sur :
  - La spécification du langage Java (Java SE 11)
  - Les conventions de code Sun
  - Les directives Javadoc
  - La documentation de l'API JDK
  - Les bonnes pratiques générales
- **Fonctionnalités clés** :
  - Sévérité configurable (définie sur `error`).
  - Prend en charge les extensions de fichier : `.java`, `.properties`, `.xml`.
  - Permet la suppression de vérifications spécifiques via des fichiers de suppression ou des annotations `@SuppressWarnings`.

---

### **Module racine : `<module name="Checker">`**
Le module `Checker` est le module de plus haut niveau qui orchestre toutes les vérifications et tous les filtres.

- **Propriétés** :
  - `severity="error"` : Traite toutes les violations comme des erreurs (les autres options incluent `warning` ou `info`).
  - `fileExtensions="java, properties, xml"` : Applique les vérifications aux fichiers `.java`, `.properties` et `.xml`.

- **Sous-modules** :
  - **Filtres de Fichier** :
    - `BeforeExecutionExclusionFileFilter` : Exclut les fichiers `module-info.java` des vérifications (en utilisant l'expression rationnelle `module\-info\.java$`).
  - **Filtres de Suppression** :
    - `SuppressionFilter` : Charge les règles de suppression à partir d'un fichier (par défaut : `checkstyle-suppressions.xml`). Si le fichier est manquant, il est optionnel (`optional="true"`).
    - `SuppressWarningsFilter` : Permet la suppression de vérifications spécifiques en utilisant les annotations `@SuppressWarnings("checkstyle:...")` dans le code.
  - **Vérifications Diverses** :
    - `JavadocPackage` : S'assure que chaque package a un fichier `package-info.java` avec Javadoc.
    - `NewlineAtEndOfFile` : Vérifie que les fichiers se terminent par un caractère de nouvelle ligne.
    - `Translation` : Vérifie que les fichiers properties (par exemple, pour l'internationalisation) contiennent les mêmes clés entre les traductions.
  - **Vérifications de Taille** :
    - `FileLength` : Vérifie la longueur totale d'un fichier (les limites par défaut s'appliquent sauf si elles sont remplacées).
    - `LineLength` : S'assure que les lignes dans les fichiers `.java` ne dépassent pas une longueur par défaut (généralement 80 ou 120 caractères, configurable).
  - **Vérifications des Espaces Blancs** :
    - `FileTabCharacter` : Interdit les caractères de tabulation dans les fichiers source (impose l'utilisation d'espaces pour l'indentation).
    - `RegexpSingleline` : Détecte les espaces blancs de fin (lignes se terminant par `\s+$`) et les signale avec le message "Line has trailing spaces."
  - **Vérification d'En-tête** (Commentée) :
    - `Header` : Si décommenté, imposerait un en-tête de fichier spécifique (par exemple, un avis de copyright) à partir d'un fichier spécifié dans `checkstyle.header.file` pour les fichiers `.java`.

---

### **Sous-module : `<module name="TreeWalker">`**
Le module `TreeWalker` traite l'arbre de syntaxe abstraite (AST) du code source Java pour effectuer des vérifications détaillées. Il contient une variété de sous-modules regroupés par catégorie.

#### **Vérifications Javadoc**
Elles imposent des commentaires Javadoc appropriés pour les classes, méthodes et variables :
- `InvalidJavadocPosition` : S'assure que les commentaires Javadoc sont correctement placés (par exemple, avant une classe ou une méthode, et non ailleurs).
- `JavadocMethod` : Vérifie que les méthodes ont des commentaires Javadoc appropriés, incluant les paramètres, les types de retour et les exceptions.
- `JavadocType` : S'assure que les classes, interfaces et enums ont des commentaires Javadoc.
- `JavadocVariable` : Exige un Javadoc pour les champs public/protected.
- `JavadocStyle` : Impose des règles stylistiques pour Javadoc (par exemple, des balises HTML appropriées, pas de commentaires mal formés).
- `MissingJavadocMethod` : Signale les méthodes manquant de commentaires Javadoc.

#### **Conventions de Nommage**
Elles s'assurent que les identifiants (variables, méthodes, classes, etc.) suivent les conventions de nommage :
- `ConstantName` : Les constantes (par exemple, `static final`) doivent suivre un modèle de nommage (généralement `UPPER_CASE`).
- `LocalFinalVariableName` : Les variables locales `final` doivent suivre un modèle de nommage (par exemple, `camelCase`).
- `LocalVariableName` : Les variables locales doivent suivre un modèle de nommage (par exemple, `camelCase`).
- `MemberName` : Les champs d'instance doivent suivre un modèle de nommage (par exemple, `camelCase`).
- `MethodName` : Les méthodes doivent suivre un modèle de nommage (par exemple, `camelCase`).
- `PackageName` : Les packages doivent suivre un modèle de nommage (par exemple, minuscules avec des points, comme `com.example`).
- `ParameterName` : Les paramètres de méthode doivent suivre un modèle de nommage (par exemple, `camelCase`).
- `StaticVariableName` : Les champs statiques (non finaux) doivent suivre un modèle de nommage.
- `TypeName` : Les noms de classe/interface/enum doivent suivre un modèle de nommage (par exemple, `UpperCamelCase`).

#### **Vérifications d'Import**
Elles réglementent l'utilisation des instructions `import` :
- `AvoidStarImport` : Interdit les imports avec caractère générique (par exemple, `import java.util.*`).
- `IllegalImport` : Bloque les imports de packages restreints (par défaut `sun.*`).
- `RedundantImport` : Signale les imports en double ou inutiles.
- `UnusedImports` : Détecte les imports inutilisés (ignore les imports liés à Javadoc avec `processJavadoc="false"`).

#### **Vérifications de Taille**
Elles limitent la taille des méthodes et des paramètres :
- `MethodLength` : S'assure que les méthodes ne dépassent pas un nombre maximum de lignes (par défaut généralement 150).
- `ParameterNumber` : Limite le nombre de paramètres dans une méthode (par défaut généralement 7).

#### **Vérifications des Espaces Blancs**
Elles imposent une utilisation cohérente des espaces blancs dans le code :
- `EmptyForIteratorPad` : Vérifie le remplissage dans les itérateurs de boucle `for` vides (par exemple, `for (int i = 0; ; i++)`).
- `GenericWhitespace` : Assure un espacement correct autour des types génériques (par exemple, `List<String>`).
- `MethodParamPad` : Vérifie l'espacement avant les listes de paramètres de méthode.
- `NoWhitespaceAfter` : Interdit l'espace blanc après certains jetons (par exemple, `++` ou les tableaux).
- `NoWhitespaceBefore` : Interdit l'espace blanc avant certains jetons (par exemple, les points-virgules).
- `OperatorWrap` : S'assure que les opérateurs (par exemple, `+`, `=`) sont sur la ligne correcte.
- `ParenPad` : Vérifie l'espacement à l'intérieur des parenthèses (par exemple, `( x )` vs. `(x)`).
- `TypecastParenPad` : Assure un espacement correct dans les conversions de type.
- `WhitespaceAfter` : Exige un espace blanc après certains jetons (par exemple, les virgules, les points-virgules).
- `WhitespaceAround` : Assure un espace blanc autour des opérateurs et des mots-clés (par exemple, `if (x == y)`).

#### **Vérifications de Modificateur**
Elles réglementent l'utilisation des modificateurs Java :
- `ModifierOrder` : S'assure que les modificateurs sont dans le bon ordre (par exemple, `public static final`, selon JLS).
- `RedundantModifier` : Signale les modificateurs inutiles (par exemple, `final` dans une classe `final`).

#### **Vérifications de Bloc**
Elles imposent une utilisation correcte des blocs de code (`{}`) :
- `AvoidNestedBlocks` : Interdit les blocs imbriqués inutiles (par exemple, `{ { ... } }`).
- `EmptyBlock` : Signale les blocs vides (par exemple, `{}`) sauf s'ils sont intentionnels.
- `LeftCurly` : S'assure que les accolades ouvrantes (`{`) sont correctement placées (par exemple, à la fin d'une ligne).
- `NeedBraces` : Exige des accolades pour les blocs à instruction unique (par exemple, `if (x) y();` doit être `if (x) { y(); }`).
- `RightCurly` : S'assure que les accolades fermantes (`}`) sont correctement placées (par exemple, sur une nouvelle ligne ou sur la même ligne, selon le style).

#### **Vérifications de Problèmes de Codage**
Elles identifient les problèmes de codage courants :
- `EmptyStatement` : Signale les instructions vides (par exemple, `;;`).
- `EqualsHashCode` : S'assure que si `equals()` est redéfini, `hashCode()` l'est aussi.
- `HiddenField` : Détecte les champs masqués par des variables locales ou des paramètres.
- `IllegalInstantiation` : Interdit l'instanciation de certaines classes (par exemple, les classes `java.lang` comme `String`).
- `InnerAssignment` : Interdit les assignations dans les expressions (par exemple, `if (x = y)`).
- `MagicNumber` : Signale les littéraux numériques codés en dur (par exemple, `42`) sauf dans des contextes spécifiques.
- `MissingSwitchDefault` : Exige une clause `default` dans les instructions `switch`.
- `MultipleVariableDeclarations` : Interdit la déclaration de plusieurs variables sur une seule ligne (par exemple, `int x, y;`).
- `SimplifyBooleanExpression` : Signale les expressions booléennes trop complexes (par exemple, `if (x == true)`).
- `SimplifyBooleanReturn` : Simplifie les instructions de retour booléennes (par exemple, `if (x) return true; else return false;`).

#### **Vérifications de Conception de Classe**
Elles imposent de bonnes pratiques de conception de classe :
- `DesignForExtension` : S'assure que les classes non finales ont des méthodes protected ou abstract pour l'extensibilité.
- `FinalClass` : Signale les classes avec uniquement des constructeurs privés comme candidates pour `final`.
- `HideUtilityClassConstructor` : S'assure que les classes utilitaires (avec uniquement des membres statiques) ont des constructeurs privés.
- `InterfaceIsType` : Interdit les interfaces utilisées uniquement comme interfaces marqueurs (sans méthodes).
- `VisibilityModifier` : Impose une visibilité correcte pour les champs (par exemple, préfère les champs privés avec des getters/setters).

#### **Vérifications Diverses**
- `ArrayTypeStyle` : Impose un style de déclaration de tableau cohérent (par exemple, `int[]` vs. `int []`).
- `FinalParameters` : Exige que les paramètres de méthode soient `final` lorsque c'est possible.
- `TodoComment` : Signale les commentaires `TODO` dans le code (utile pour suivre le travail incomplet).
- `UpperEll` : S'assure que la lettre `L` est utilisée pour les littéraux longs (par exemple, `100L` au lieu de `100l`).

#### **Filtres de Suppression (Dans TreeWalker)**
- `SuppressionXpathFilter` : Permet la suppression de vérifications en utilisant des expressions XPath définies dans un fichier (par défaut : `checkstyle-xpath-suppressions.xml`, optionnel).
- `SuppressWarningsHolder` : Prend en charge les annotations `@SuppressWarnings("checkstyle:...")` pour supprimer des vérifications spécifiques au sein de l'AST.

---

### **Points Clés**
- **Configurabilité** : La plupart des modules ont des paramètres par défaut mais peuvent être personnalisés via des propriétés (par exemple, `LineLength` peut définir une longueur `max` spécifique).
- **Suppression** : La configuration prend en charge une suppression flexible des vérifications via des fichiers externes (`checkstyle-suppressions.xml`, `checkstyle-xpath-suppressions.xml`) ou des annotations.
- **Extensibilité** : Des vérifications supplémentaires peuvent être ajoutées, et les existantes peuvent être désactivées en les commentant ou en les supprimant.
- **Documentation** : La configuration fait référence à la documentation de Checkstyle (par exemple, `https://checkstyle.org`) pour les détails de chaque module.
- **Vérification d'En-tête** : Le module `Header` est commenté, donc il n'est pas actif sauf s'il est décommenté et configuré avec un fichier d'en-tête.

---

### **Comment il est Utilisé**
1. **Intégration** : Ce fichier est généralement utilisé avec un outil de build comme Maven, Gradle, ou un plugin d'IDE pour exécuter Checkstyle pendant le processus de build ou en développement.
2. **Rapport de Violation** : Lorsque le code viole une règle (par exemple, une ligne dépasse la longueur maximale), Checkstyle la signale comme une erreur (en raison de `severity="error"`).
3. **Suppression** : Les développeurs peuvent supprimer des violations spécifiques en utilisant `@SuppressWarnings("checkstyle:<check-name>")` ou en définissant des règles dans des fichiers de suppression.
4. **Personnalisation** : Des propriétés comme `basedir`, `checkstyle.header.file`, ou les chemins des fichiers de suppression peuvent être définis extérieurement (par exemple, via des configurations d'outil de build).

---

### **Exemples de Violations**
- **JavadocMethod** : Une méthode publique sans Javadoc déclenchera une erreur.
- **LineLength** : Une ligne dans un fichier `.java` dépassant le maximum par défaut (par exemple, 80 caractères) sera signalée.
- **AvoidStarImport** : Utiliser `import java.util.*` causera une erreur.
- **MagicNumber** : Écrire `int x = 42;` sans constante nommée sera signalé.

---

Si vous avez besoin d'une explication plus approfondie d'un module spécifique, d'exemples de violations ou de conseils pour personnaliser cette configuration, faites-le-moi savoir !