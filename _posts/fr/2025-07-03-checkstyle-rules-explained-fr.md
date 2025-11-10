---
audio: false
generated: true
lang: fr
layout: post
title: Règles Checkstyle expliquées brièvement
translated: true
type: note
---

Ci-dessous, je vais expliquer chaque règle du fichier de configuration Checkstyle que vous avez fourni, ainsi qu'un petit exemple de code qui **violerait** la règle et une brève description de la raison pour laquelle elle est signalée. Les règles sont regroupées par catégorie comme dans votre description, et je garderai les explications concises tout en assurant la clarté. Chaque exemple suppose que la règle est active avec les paramètres par défaut, sauf indication contraire. Pour les règles avec des propriétés configurables (par exemple, la longueur maximale de ligne), j'utiliserai les valeurs par défaut typiques (par exemple, 80 caractères pour LineLength) sauf indication contraire.

---

### Module racine : `<module name="Checker">`
Le module `Checker` est l'orchestrateur principal de toutes les vérifications et filtres. Il s'applique aux fichiers `.java`, `.properties` et `.xml` et définit la sévérité sur `error`.

#### Propriétés
- **severity="error"** : Toutes les violations sont traitées comme des erreurs.
- **fileExtensions="java, properties, xml"** : Les vérifications s'appliquent à ces types de fichiers.

---

### Filtres de fichiers
Ces filtres déterminent quels fichiers sont vérifiés.

1.  **BeforeExecutionExclusionFileFilter**
    - **Objectif** : Exclut les fichiers correspondant à une regex (par exemple, `module-info.java`).
    - **Exemple de violation** :
      ```java
      // module-info.java
      module com.example {
          requires java.base;
      }
      ```
    - **Pourquoi signalé** : Ce fichier correspond à la regex `module\-info\.java$` et est exclu des vérifications. Aucune violation ne se produit pour ce fichier, mais les autres fichiers sont toujours vérifiés.

2.  **SuppressionFilter**
    - **Objectif** : Supprime les vérifications en fonction des règles d'un fichier (par exemple, `checkstyle-suppressions.xml`).
    - **Exemple de violation** : Si `checkstyle-suppressions.xml` supprime `LineLength` pour un fichier spécifique, une longue ligne dans ce fichier ne sera pas signalée. Sans suppression :
      ```java
      public class MyClass { // Cette ligne est très longue et dépasse la longueur maximale par défaut de 80 caractères, provoquant une erreur.
      }
      ```
    - **Pourquoi signalé** : Sans règle de suppression, la longue ligne viole `LineLength`.

3.  **SuppressWarningsFilter**
    - **Objectif** : Permet la suppression des vérifications en utilisant `@SuppressWarnings("checkstyle:<check-name>")`.
    - **Exemple de violation** :
      ```java
      public class MyClass {
          int my_field; // Viole MemberName (pas camelCase)
      }
      ```
      ```java
      @SuppressWarnings("checkstyle:MemberName")
      public class MyClass {
          int my_field; // Aucune violation due à la suppression
      }
      ```
    - **Pourquoi signalé** : Sans suppression, `my_field` viole `MemberName` (attend camelCase, par exemple `myField`).

---

### Vérifications diverses
Celles-ci s'appliquent aux propriétés générales des fichiers.

4.  **JavadocPackage**
    - **Objectif** : Garantit que chaque package a un `package-info.java` avec Javadoc.
    - **Exemple de violation** :
      ```java
      // com/example/package-info.java (manquant ou sans Javadoc)
      package com.example;
      ```
    - **Pourquoi signalé** : Commentaire Javadoc manquant (par exemple, `/** Description du package */`).

5.  **NewlineAtEndOfFile**
    - **Objectif** : Garantit que les fichiers se terminent par un saut de ligne.
    - **Exemple de violation** :
      ```java
      public class MyClass {} // Pas de saut de ligne à la fin
      ```
    - **Pourquoi signalé** : Le fichier se termine sans caractère de saut de ligne.

6.  **Translation**
    - **Objectif** : Vérifie que les fichiers `.properties` pour l'internationalisation ont des clés cohérentes.
    - **Exemple de violation** :
      ```properties
      # messages.properties
      key1=Hello
      key2=World
      ```
      ```properties
      # messages_fr.properties
      key1=Bonjour
      # Clé key2 manquante
      ```
    - **Pourquoi signalé** : `messages_fr.properties` n'a pas de `key2`, qui existe dans `messages.properties`.

---

### Vérifications de taille
Celles-ci imposent des limites sur la longueur des fichiers et des lignes.

7.  **FileLength**
    - **Objectif** : Limite le nombre total de lignes dans un fichier (par défaut typiquement 2000 lignes).
    - **Exemple de violation** : Un fichier Java de 2001 lignes.
    - **Pourquoi signalé** : Dépassement de la limite de lignes par défaut.

8.  **LineLength**
    - **Objectif** : Garantit que les lignes ne dépassent pas une longueur maximale (par défaut 80 caractères).
    - **Exemple de violation** :
      ```java
      public class MyClass { public void myMethodWithVeryLongNameToExceedEightyCharactersInALine() {} }
      ```
    - **Pourquoi signalé** : La ligne dépasse 80 caractères.

---

### Vérifications des espaces blancs
Celles-ci imposent une utilisation cohérente des espaces blancs.

9.  **FileTabCharacter**
    - **Objectif** : Interdit les caractères de tabulation (`\t`) dans les fichiers source.
    - **Exemple de violation** :
      ```java
      public class MyClass {
      →    int x; // Caractère de tabulation utilisé pour l'indentation
      }
      ```
    - **Pourquoi signalé** : Des tabulations sont utilisées au lieu d'espaces.

10. **RegexpSingleline**
    - **Objectif** : Détecte les espaces blancs de fin de ligne (lignes se terminant par `\s+$`).
    - **Exemple de violation** :
      ```java
      public class MyClass {   // Espaces en fin de ligne
      }
      ```
    - **Pourquoi signalé** : La ligne se termine par des espaces blancs.

---

### Vérification d'en-tête (commentée)
11. **Header**
    - **Objectif** : Impose un en-tête de fichier spécifique (par exemple, une notice de copyright) à partir de `checkstyle.header.file`.
    - **Exemple de violation** (si activé) :
      ```java
      // En-tête manquant
      public class MyClass {}
      ```
    - **Pourquoi signalé** : Manque l'en-tête requis (par exemple, `// Copyright 2025 Example Inc.`).

---

### Sous-module : `<module name="TreeWalker">`
Le `TreeWalker` traite l'AST Java pour des vérifications détaillées.

#### Vérifications Javadoc
Celles-ci imposent des commentaires Javadoc appropriés.

12. **InvalidJavadocPosition**
    - **Objectif** : Garantit que les commentaires Javadoc sont avant les classes/méthodes, et non ailleurs.
    - **Exemple de violation** :
      ```java
      public class MyClass {
          /** Ceci est un Javadoc mal placé */
          int x;
      }
      ```
    - **Pourquoi signalé** : Le Javadoc n'est pas avant une déclaration de classe/méthode.

13. **JavadocMethod**
    - **Objectif** : Vérifie que les méthodes ont un Javadoc approprié (paramètres, retour, exceptions).
    - **Exemple de violation** :
      ```java
      public int add(int a, int b) { return a + b; }
      ```
    - **Pourquoi signalé** : Javadoc manquant pour la méthode publique.

14. **JavadocType**
    - **Objectif** : Garantit que les classes/interfaces/enums ont un Javadoc.
    - **Exemple de violation** :
      ```java
      public class MyClass {}
      ```
    - **Pourquoi signalé** : Javadoc manquant pour la classe.

15. **JavadocVariable**
    - **Objectif** : Requiert un Javadoc pour les champs publics/protégés.
    - **Exemple de violation** :
      ```java
      public class MyClass {
          public int x;
      }
      ```
    - **Pourquoi signalé** : Javadoc manquant pour le champ public.

16. **JavadocStyle**
    - **Objectif** : Impose le style Javadoc (par exemple, HTML valide, pas de commentaires mal formés).
    - **Exemple de violation** :
      ```java
      /** Point manquant à la fin */
      public class MyClass {}
      ```
    - **Pourquoi signalé** : Le Javadoc manque un point à la fin.

17. **MissingJavadocMethod**
    - **Objectif** : Signale les méthodes manquant de Javadoc.
    - **Exemple de violation** :
      ```java
      public void myMethod() {}
      ```
    - **Pourquoi signalé** : La méthode publique manque de Javadoc.

---

#### Conventions de nommage
Celles-ci imposent des modèles de nommage.

18. **ConstantName**
    - **Objectif** : Les constantes (`static final`) doivent être en `MAJUSCULES_AVEC_UNDERSCORE`.
    - **Exemple de violation** :
      ```java
      public class MyClass {
          static final int myConstant = 42;
      }
      ```
    - **Pourquoi signalé** : `myConstant` devrait être `MY_CONSTANT`.

19. **LocalFinalVariableName**
    - **Objectif** : Les variables locales `final` doivent être en `camelCase`.
    - **Exemple de violation** :
      ```java
      public void myMethod() {
          final int MY_VAR = 1;
      }
      ```
    - **Pourquoi signalé** : `MY_VAR` devrait être `myVar`.

20. **LocalVariableName**
    - **Objectif** : Les variables locales doivent être en `camelCase`.
    - **Exemple de violation** :
      ```java
      public void myMethod() {
          int MY_VAR = 1;
      }
      ```
    - **Pourquoi signalé** : `MY_VAR` devrait être `myVar`.

21. **MemberName**
    - **Objectif** : Les champs d'instance doivent être en `camelCase`.
    - **Exemple de violation** :
      ```java
      public class MyClass {
          int my_field;
      }
      ```
    - **Pourquoi signalé** : `my_field` devrait être `myField`.

22. **MethodName**
    - **Objectif** : Les méthodes doivent être en `camelCase`.
    - **Exemple de violation** :
      ```java
      public void MyMethod() {}
      ```
    - **Pourquoi signalé** : `MyMethod` devrait être `myMethod`.

23. **PackageName**
    - **Objectif** : Les packages doivent être en minuscules avec des points (par exemple, `com.example`).
    - **Exemple de violation** :
      ```java
      package com.Example;
      ```
    - **Pourquoi signalé** : `Example` devrait être `example`.

24. **ParameterName**
    - **Objectif** : Les paramètres de méthode doivent être en `camelCase`.
    - **Exemple de violation** :
      ```java
      public void myMethod(int MY_PARAM) {}
      ```
    - **Pourquoi signalé** : `MY_PARAM` devrait être `myParam`.

25. **StaticVariableName**
    - **Objectif** : Les champs statiques (non finaux) doivent suivre un modèle de nommage.
    - **Exemple de violation** :
      ```java
      public class MyClass {
          static int MY_FIELD;
      }
      ```
    - **Pourquoi signalé** : `MY_FIELD` devrait être `myField` (en supposant camelCase).

26. **TypeName**
    - **Objectif** : Les noms de classes/interfaces/enums doivent être en `UpperCamelCase`.
    - **Exemple de violation** :
      ```java
      public class myClass {}
      ```
    - **Pourquoi signalé** : `myClass` devrait être `MyClass`.

---

#### Vérifications d'import
Celles-ci régulent les instructions d'import.

27. **AvoidStarImport**
    - **Objectif** : Interdit les imports avec wildcard (par exemple, `import java.util.*`).
    - **Exemple de violation** :
      ```java
      import java.util.*;
      ```
    - **Pourquoi signalé** : Utilise `*` au lieu d'imports spécifiques (par exemple, `import java.util.List`).

28. **IllegalImport**
    - **Objectif** : Bloque les imports de packages restreints (par exemple, `sun.*`).
    - **Exemple de violation** :
      ```java
      import sun.misc.Unsafe;
      ```
    - **Pourquoi signalé** : `sun.misc.Unsafe` est dans un package restreint.

29. **RedundantImport**
    - **Objectif** : Signale les imports en double ou inutiles.
    - **Exemple de violation** :
      ```java
      import java.util.List;
      import java.util.List;
      ```
    - **Pourquoi signalé** : Import en double de `List`.

30. **UnusedImports**
    - **Objectif** : Détecte les imports non utilisés.
    - **Exemple de violation** :
      ```java
      import java.util.List;
      public class MyClass {}
      ```
    - **Pourquoi signalé** : `List` est importé mais non utilisé.

---

#### Vérifications de taille
Celles-ci limitent le nombre de méthodes et de paramètres.

31. **MethodLength**
    - **Objectif** : Limite la longueur des méthodes (par défaut typiquement 150 lignes).
    - **Exemple de violation** : Une méthode de 151 lignes.
    - **Pourquoi signalé** : Dépassement de la limite de lignes par défaut.

32. **ParameterNumber**
    - **Objectif** : Limite le nombre de paramètres de méthode (par défaut typiquement 7).
    - **Exemple de violation** :
      ```java
      public void myMethod(int a, int b, int c, int d, int e, int f, int g, int h) {}
      ```
    - **Pourquoi signalé** : 8 paramètres dépassent la limite par défaut de 7.

---

#### Vérifications des espaces blancs
Celles-ci imposent un espacement cohérent dans le code.

33. **EmptyForIteratorPad**
    - **Objectif** : Vérifie l'espacement dans les itérateurs vides des boucles `for`.
    - **Exemple de violation** :
      ```java
      for (int i = 0; ; i++) {}
      ```
    - **Pourquoi signalé** : La section d'itérateur vide devrait avoir un espace (par exemple, `for (int i = 0; ; i++)`).

34. **GenericWhitespace**
    - **Objectif** : Garantit l'espacement autour des types génériques (par exemple, `List<String>`).
    - **Exemple de violation** :
      ```java
      List<String>list;
      ```
    - **Pourquoi signalé** : Pas d'espace entre `>` et `list`.

35. **MethodParamPad**
    - **Objectif** : Vérifie l'espacement avant les listes de paramètres de méthode.
    - **Exemple de violation** :
      ```java
      public void myMethod (int x) {}
      ```
    - **Pourquoi signalé** : L'espace avant `(int x)` est incorrect.

36. **NoWhitespaceAfter**
    - **Objectif** : Interdit l'espace blanc après certains jetons (par exemple, `++`).
    - **Exemple de violation** :
      ```java
      int x = y ++ ;
      ```
    - **Pourquoi signalé** : Espace après `++`.

37. **NoWhitespaceBefore**
    - **Objectif** : Interdit l'espace blanc avant certains jetons (par exemple, `;`).
    - **Exemple de violation** :
      ```java
      int x = 1 ;
      ```
    - **Pourquoi signalé** : Espace avant `;`.

38. **OperatorWrap**
    - **Objectif** : Garantit que les opérateurs sont sur la ligne correcte.
    - **Exemple de violation** :
      ```java
      int x = 1 +
          2;
      ```
    - **Pourquoi signalé** : `+` devrait être à la fin de la première ligne.

39. **ParenPad**
    - **Objectif** : Vérifie l'espacement à l'intérieur des parenthèses.
    - **Exemple de violation** :
      ```java
      if ( x == y ) {}
      ```
    - **Pourquoi signalé** : Les espaces à l'intérieur de `(` et `)` sont incorrects.

40. **TypecastParenPad**
    - **Objectif** : Garantit l'espacement dans les casts de type.
    - **Exemple de violation** :
      ```java
      Object o = ( String ) obj;
      ```
    - **Pourquoi signalé** : Les espaces à l'intérieur de `( String )` sont incorrects.

41. **WhitespaceAfter**
    - **Objectif** : Requiert un espace blanc après certains jetons (par exemple, les virgules).
    - **Exemple de violation** :
      ```java
      int[] arr = {1,2,3};
      ```
    - **Pourquoi signalé** : Espace manquant après les virgules.

42. **WhitespaceAround**
    - **Objectif** : Garantit un espace blanc autour des opérateurs/mots-clés.
    - **Exemple de violation** :
      ```java
      if(x==y) {}
      ```
    - **Pourquoi signalé** : Espaces manquants autour de `==` et `if`.

---

#### Vérifications de modificateurs
Celles-ci régulent les modificateurs Java.

43. **ModifierOrder**
    - **Objectif** : Garantit que les modificateurs sont dans le bon ordre (selon JLS).
    - **Exemple de violation** :
      ```java
      static public final int x = 1;
      ```
    - **Pourquoi signalé** : Ordre incorrect ; devrait être `public static final`.

44. **RedundantModifier**
    - **Objectif** : Signale les modificateurs inutiles.
    - **Exemple de violation** :
      ```java
      public final class MyClass {
          public final void myMethod() {}
      }
      ```
    - **Pourquoi signalé** : `final` sur une méthode dans une classe `final` est redondante.

---

#### Vérifications de blocs
Celles-ci imposent une utilisation correcte des blocs de code.

45. **AvoidNestedBlocks**
    - **Objectif** : Interdit les blocs imbriqués inutiles.
    - **Exemple de violation** :
      ```java
      public void myMethod() {
          { int x = 1; }
      }
      ```
    - **Pourquoi signalé** : Bloc imbriqué inutile.

46. **EmptyBlock**
    - **Objectif** : Signale les blocs vides.
    - **Exemple de violation** :
      ```java
      if (x == 1) {}
      ```
    - **Pourquoi signalé** : Bloc `if` vide.

47. **LeftCurly**
    - **Objectif** : Garantit que les accolades ouvrantes sont placées correctement.
    - **Exemple de violation** :
      ```java
      public class MyClass
      {
      }
      ```
    - **Pourquoi signalé** : `{` devrait être sur la même ligne que `class`.

48. **NeedBraces**
    - **Objectif** : Requiert des accolades pour les blocs à instruction unique.
    - **Exemple de violation** :
      ```java
      if (x == 1) y = 2;
      ```
    - **Pourquoi signalé** : Accolades manquantes ; devrait être `{ y = 2; }`.

49. **RightCurly**
    - **Objectif** : Garantit que les accolades fermantes sont placées correctement.
    - **Exemple de violation** :
      ```java
      public class MyClass {
      }
      ```
    - **Pourquoi signalé** : `}` devrait être sur une nouvelle ligne (selon le style).

---

#### Vérifications de problèmes de codage
Celles-ci identifient les problèmes de codage courants.

50. **EmptyStatement**
    - **Objectif** : Signale les instructions vides.
    - **Exemple de violation** :
      ```java
      int x = 1;; // Point-virgule supplémentaire
      ```
    - **Pourquoi signalé** : Le `;` supplémentaire crée une instruction vide.

51. **EqualsHashCode**
    - **Objectif** : Garantit que `equals()` et `hashCode()` sont tous deux redéfinis.
    - **Exemple de violation** :
      ```java
      public class MyClass {
          @Override
          public boolean equals(Object o) { return true; }
      }
      ```
    - **Pourquoi signalé** : Redéfinition de `hashCode()` manquante.

52. **HiddenField**
    - **Objectif** : Détecte les champs masqués par des variables locales/paramètres.
    - **Exemple de violation** :
      ```java
      public class MyClass {
          int x;
          public void setX(int x) { this.x = x; }
      }
      ```
    - **Pourquoi signalé** : Le paramètre `x` masque le champ `x`.

53. **IllegalInstantiation**
    - **Objectif** : Interdit l'instanciation de certaines classes.
    - **Exemple de violation** :
      ```java
      String s = new String("test");
      ```
    - **Pourquoi signalé** : Instanciation inutile de `String`.

54. **InnerAssignment**
    - **Objectif** : Interdit les affectations dans les expressions.
    - **Exemple de violation** :
      ```java
      if (x = 1) {}
      ```
    - **Pourquoi signalé** : Affectation `x = 1` dans l'expression.

55. **MagicNumber**
    - **Objectif** : Signale les littéraux numériques codés en dur.
    - **Exemple de violation** :
      ```java
      int x = 42;
      ```
    - **Pourquoi signalé** : `42` devrait être une constante nommée (par exemple, `static final int MY_CONST = 42;`).

56. **MissingSwitchDefault**
    - **Objectif** : Requiert un cas `default` dans les instructions `switch`.
    - **Exemple de violation** :
      ```java
      switch (x) {
          case 1: break;
      }
      ```
    - **Pourquoi signalé** : Cas `default` manquant.

57. **MultipleVariableDeclarations**
    - **Objectif** : Interdit plusieurs variables dans une seule déclaration.
    - **Exemple de violation** :
      ```java
      int x, y;
      ```
    - **Pourquoi signalé** : Devrait être `int x; int y;`.

58. **SimplifyBooleanExpression**
    - **Objectif** : Signale les expressions booléennes complexes.
    - **Exemple de violation** :
      ```java
      if (x == true) {}
      ```
    - **Pourquoi signalé** : Devrait être `if (x)`.

59. **SimplifyBooleanReturn**
    - **Objectif** : Simplifie les instructions de retour booléennes.
    - **Exemple de violation** :
      ```java
      if (x) return true; else return false;
      ```
    - **Pourquoi signalé** : Devrait être `return x;`.

---

#### Vérifications de conception de classe
Celles-ci imposent une bonne conception de classe.

60. **DesignForExtension**
    - **Objectif** : Garantit que les classes non finales ont des méthodes protégées/abstraites.
    - **Exemple de violation** :
      ```java
      public class MyClass {
          public void myMethod() {}
      }
      ```
    - **Pourquoi signalé** : La classe non finale a une méthode non protégée/abstraite.

61. **FinalClass**
    - **Objectif** : Signale les classes avec des constructeurs privés comme candidates pour `final`.
    - **Exemple de violation** :
      ```java
      public class MyClass {
          private MyClass() {}
      }
      ```
    - **Pourquoi signalé** : Devrait être `final` puisqu'elle ne peut pas être étendue.

62. **HideUtilityClassConstructor**
    - **Objectif** : Garantit que les classes utilitaires ont des constructeurs privés.
    - **Exemple de violation** :
      ```java
      public class MyUtils {
          public static void doSomething() {}
      }
      ```
    - **Pourquoi signalé** : Constructeur privé manquant pour la classe utilitaire.

63. **InterfaceIsType**
    - **Objectif** : Interdit les interfaces marqueurs (sans méthodes).
    - **Exemple de violation** :
      ```java
      public interface MyMarker {}
      ```
    - **Pourquoi signalé** : L'interface n'a pas de méthodes.

64. **VisibilityModifier**
    - **Objectif** : Impose une visibilité correcte des champs (préfère privé avec getters/setters).
    - **Exemple de violation** :
      ```java
      public class MyClass {
          public int x;
      }
      ```
    - **Pourquoi signalé** : Le champ `x` devrait être `private` avec des accesseurs.

---

#### Vérifications diverses
Vérifications supplémentaires pour la qualité du code.

65. **ArrayTypeStyle**
    - **Objectif** : Impose un style de déclaration de tableau cohérent (`int[]` vs `int []`).
    - **Exemple de violation** :
      ```java
      int x[];
      ```
    - **Pourquoi signalé** : Devrait être `int[] x`.

66. **FinalParameters**
    - **Objectif** : Requiert que les paramètres de méthode soient `final` lorsque c'est possible.
    - **Exemple de violation** :
      ```java
      public void myMethod(int x) {}
      ```
    - **Pourquoi signalé** : Le paramètre `x` devrait être `final int x`.

67. **TodoComment**
    - **Objectif** : Signale les commentaires `TODO`.
    - **Exemple de violation** :
      ```java
      // TODO: Corriger ceci
      public void myMethod() {}
      ```
    - **Pourquoi signalé** : Commentaire `TODO` détecté.

68. **UpperEll**
    - **Objectif** : Garantit le `L` pour les littéraux longs (pas `l`).
    - **Exemple de violation** :
      ```java
      long x = 100l;
      ```
    - **Pourquoi signalé** : `100l` devrait être `100L`.

---

#### Filtres de suppression (dans TreeWalker)
Celles-ci permettent la suppression dans l'AST.

69. **SuppressionXpathFilter**
    - **Objectif** : Supprime les vérifications en utilisant des expressions XPath d'un fichier (par exemple, `checkstyle-xpath-suppressions.xml`).
    - **Exemple de violation** : Similaire à `SuppressionFilter` mais utilise XPath (par exemple, supprimer `JavadocMethod` pour une méthode spécifique).

70. **SuppressWarningsHolder**
    - **Objectif** : Prend en charge `@SuppressWarnings("checkstyle:...")` dans l'AST.
    - **Exemple de violation** :
      ```java
      public class MyClass {
          int MY_FIELD; // Viole MemberName
      }
      ```
      ```java
      @SuppressWarnings("checkstyle:MemberName")
      public class MyClass {
          int MY_FIELD; // Aucune violation
      }
      ```
    - **Pourquoi signalé** : Sans suppression, `MY_FIELD` viole `MemberName`.

---

### Notes clés
- **Configurabilité** : Des règles comme `LineLength` ou `MethodLength` peuvent avoir des seuils personnalisés (par exemple, `max="120"` pour `LineLength`).
- **Suppression** : Utilisez `@SuppressWarnings("checkstyle:<check-name>")` ou des fichiers de suppression pour contourner des vérifications spécifiques.
- **Intégration** : Exécutez avec Maven/Gradle ou des plugins IDE ; les erreurs sont rapportées pendant les builds.
- **Vérification d'en-tête** : Inactive sauf si décommentée et configurée avec `checkstyle.header.file`.

Si vous avez besoin d'exemples de personnalisation spécifiques (par exemple, changer `LineLength` à 120), de corrections de violations ou de détails d'intégration, faites-le-moi savoir !