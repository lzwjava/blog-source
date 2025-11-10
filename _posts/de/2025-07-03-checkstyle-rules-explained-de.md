---
audio: false
generated: true
lang: de
layout: post
title: Checkstyle Regeln kurz erklärt
translated: true
type: note
---

Im Folgenden werde ich jede Regel der bereitgestellten Checkstyle-Konfigurationsdatei erklären, zusammen mit einem kurzen Codebeispiel, das die Regel **verletzen** würde, und einer kurzen Beschreibung, warum sie beanstandet wird. Die Regeln sind, wie in Ihrer Beschreibung, nach Kategorien gruppiert, und ich werde die Erklärungen prägnant halten, während ich auf Klarheit achte. Jedes Beispiel geht davon aus, dass die Regel mit Standardeinstellungen aktiv ist, sofern nicht anders angegeben. Für Regeln mit konfigurierbaren Eigenschaften (z. B. maximale Zeilenlänge) verwende ich typische Standardwerte (z. B. 80 Zeichen für LineLength), sofern nicht anders vermerkt.

---

### Root-Modul: `<module name="Checker">`
Das `Checker`-Modul ist die oberste Steuerungskomponente für alle Prüfungen und Filter. Es gilt für `.java`-, `.properties`- und `.xml`-Dateien und setzt den Schweregrad auf `error`.

#### Eigenschaften
- **severity="error"**: Alle Verstöße werden als Fehler behandelt.
- **fileExtensions="java, properties, xml"**: Prüfungen gelten für diese Dateitypen.

---

### Datei-Filter
Diese filtern, welche Dateien geprüft werden.

1.  **BeforeExecutionExclusionFileFilter**
    - **Zweck**: Schließt Dateien aus, die auf einen Regex passen (z. B. `module-info.java`).
    - **Beispiel für einen Verstoß**:
      ```java
      // module-info.java
      module com.example {
          requires java.base;
      }
      ```
    - **Warum beanstandet**: Diese Datei passt auf den Regex `module\-info\.java$` und wird von Prüfungen ausgeschlossen. Für diese Datei tritt kein Verstoß auf, aber andere Dateien werden weiterhin geprüft.

2.  **SuppressionFilter**
    - **Zweck**: Unterdrückt Prüfungen basierend auf Regeln in einer Datei (z. B. `checkstyle-suppressions.xml`).
    - **Beispiel für einen Verstoß**: Wenn `checkstyle-suppressions.xml` `LineLength` für eine bestimmte Datei unterdrückt, wird eine lange Zeile in dieser Datei nicht beanstandet. Ohne Unterdrückung:
      ```java
      public class MyClass { // Diese Zeile ist sehr lang und überschreitet die standardmäßige Maximallänge von 80 Zeichen, was einen Fehler verursacht.
      }
      ```
    - **Warum beanstandet**: Ohne eine Unterdrückungsregel verstößt die lange Zeile gegen `LineLength`.

3.  **SuppressWarningsFilter**
    - **Zweck**: Ermöglicht die Unterdrückung von Prüfungen mittels `@SuppressWarnings("checkstyle:<check-name>")`.
    - **Beispiel für einen Verstoß**:
      ```java
      public class MyClass {
          int my_field; // Verletzt MemberName (nicht camelCase)
      }
      ```
      ```java
      @SuppressWarnings("checkstyle:MemberName")
      public class MyClass {
          int my_field; // Kein Verstoß aufgrund der Unterdrückung
      }
      ```
    - **Warum beanstandet**: Ohne Unterdrückung verstößt `my_field` gegen `MemberName` (erwartet camelCase, z. B. `myField`).

---

### Verschiedene Prüfungen (Miscellaneous Checks)
Diese gelten für allgemeine Dateieigenschaften.

4.  **JavadocPackage**
    - **Zweck**: Stellt sicher, dass jedes Paket eine `package-info.java` mit Javadoc hat.
    - **Beispiel für einen Verstoß**:
      ```java
      // com/example/package-info.java (fehlend oder ohne Javadoc)
      package com.example;
      ```
    - **Warum beanstandet**: Fehlender Javadoc-Kommentar (z. B. `/** Paketbeschreibung */`).

5.  **NewlineAtEndOfFile**
    - **Zweck**: Stellt sicher, dass Dateien mit einem Zeilenumbruch enden.
    - **Beispiel für einen Verstoß**:
      ```java
      public class MyClass {} // Kein Zeilenumbruch am Ende
      ```
    - **Warum beanstandet**: Die Datei endet ohne ein Newline-Zeichen.

6.  **Translation**
    - **Zweck**: Überprüft `.properties`-Dateien für Internationalisierung auf konsistente Schlüssel.
    - **Beispiel für einen Verstoß**:
      ```properties
      # messages.properties
      key1=Hello
      key2=World
      ```
      ```properties
      # messages_fr.properties
      key1=Bonjour
      # Fehlender key2
      ```
    - **Warum beanstandet**: `messages_fr.properties` enthält `key2` nicht, obwohl es in `messages.properties` existiert.

---

### Größenprüfungen (Size Checks)
Diese setzen Grenzen für Datei- und Zeilenlängen.

7.  **FileLength**
    - **Zweck**: Begrenzt die Gesamtzahl der Zeilen in einer Datei (Standard typisch 2000 Zeilen).
    - **Beispiel für einen Verstoß**: Eine Java-Datei mit 2001 Zeilen.
    - **Warum beanstandet**: Überschreitet das Standard-Zeilenlimit.

8.  **LineLength**
    - **Zweck**: Stellt sicher, dass Zeilen eine maximale Länge nicht überschreiten (Standard 80 Zeichen).
    - **Beispiel für einen Verstoß**:
      ```java
      public class MyClass { public void myMethodWithVeryLongNameToExceedEightyCharactersInALine() {} }
      ```
    - **Warum beanstandet**: Die Zeile überschreitet 80 Zeichen.

---

### Leerzeichenprüfungen (Whitespace Checks)
Diese erzwingen eine konsistente Verwendung von Leerzeichen.

9.  **FileTabCharacter**
    - **Zweck**: Verbietet Tabulatorzeichen (`\t`) in Quelldateien.
    - **Beispiel für einen Verstoß**:
      ```java
      public class MyClass {
      →    int x; // Tabulatorzeichen für Einrückung verwendet
      }
      ```
    - **Warum beanstandet**: Tabs werden anstelle von Leerzeichen verwendet.

10. **RegexpSingleline**
    - **Zweck**: Erkennt nachgestellte Leerzeichen (Zeilen, die mit `\s+$` enden).
    - **Beispiel für einen Verstoß**:
      ```java
      public class MyClass {   // Nachgestellte Leerzeichen
      }
      ```
    - **Warum beanstandet**: Die Zeile endet mit Leerzeichen.

---

### Header-Prüfung (Auskommentiert)
11. **Header**
    - **Zweck**: Erzwingt einen bestimmten Datei-Header (z. B. Copyright-Hinweis) aus `checkstyle.header.file`.
    - **Beispiel für einen Verstoß** (falls aktiviert):
      ```java
      // Fehlender Header
      public class MyClass {}
      ```
    - **Warum beanstandet**: Fehlender erforderlicher Header (z. B. `// Copyright 2025 Example Inc.`).

---

### Untermodul: `<module name="TreeWalker">`
Der `TreeWalker` verarbeitet den Java-AST für detaillierte Prüfungen.

#### Javadoc-Prüfungen
Diese erzwingen korrekte Javadoc-Kommentare.

12. **InvalidJavadocPosition**
    - **Zweck**: Stellt sicher, dass Javadoc-Kommentare vor Klassen/Methoden stehen, nicht anderswo.
    - **Beispiel für einen Verstoß**:
      ```java
      public class MyClass {
          /** Dies ist ein falsch platzierter Javadoc */
          int x;
      }
      ```
    - **Warum beanstandet**: Javadoc steht nicht vor einer Klassen-/Methodendeklaration.

13. **JavadocMethod**
    - **Zweck**: Prüft Methoden auf korrekte Javadoc-Dokumentation (Parameter, Rückgabe, Exceptions).
    - **Beispiel für einen Verstoß**:
      ```java
      public int add(int a, int b) { return a + b; }
      ```
    - **Warum beanstandet**: Fehlende Javadoc-Dokumentation für die public-Methode.

14. **JavadocType**
    - **Zweck**: Stellt sicher, dass Klassen/Interfaces/Enums Javadoc haben.
    - **Beispiel für einen Verstoß**:
      ```java
      public class MyClass {}
      ```
    - **Warum beanstandet**: Fehlende Javadoc-Dokumentation für die Klasse.

15. **JavadocVariable**
    - **Zweck**: Verlangt Javadoc für public/protected Felder.
    - **Beispiel für einen Verstoß**:
      ```java
      public class MyClass {
          public int x;
      }
      ```
    - **Warum beanstandet**: Fehlende Javadoc-Dokumentation für das public-Feld.

16. **JavadocStyle**
    - **Zweck**: Erzwingt Javadoc-Stil (z. B. gültiges HTML, keine fehlerhaften Kommentare).
    - **Beispiel für einen Verstoß**:
      ```java
      /** Fehlender Punkt am Ende */
      public class MyClass {}
      ```
    - **Warum beanstandet**: Der Javadoc-Kommentar hat keinen Punkt am Ende.

17. **MissingJavadocMethod**
    - **Zweck**: Markiert Methoden, denen Javadoc fehlt.
    - **Beispiel für einen Verstoß**:
      ```java
      public void myMethod() {}
      ```
    - **Warum beanstandet**: Der public-Methode fehlt die Javadoc-Dokumentation.

---

#### Namenskonventionen
Diese erzwingen Benennungsmuster.

18. **ConstantName**
    - **Zweck**: Konstanten (`static final`) müssen `UPPER_CASE` sein.
    - **Beispiel für einen Verstoß**:
      ```java
      public class MyClass {
          static final int myConstant = 42;
      }
      ```
    - **Warum beanstandet**: `myConstant` sollte `MY_CONSTANT` sein.

19. **LocalFinalVariableName**
    - **Zweck**: Lokale `final` Variablen müssen `camelCase` sein.
    - **Beispiel für einen Verstoß**:
      ```java
      public void myMethod() {
          final int MY_VAR = 1;
      }
      ```
    - **Warum beanstandet**: `MY_VAR` sollte `myVar` sein.

20. **LocalVariableName**
    - **Zweck**: Lokale Variablen müssen `camelCase` sein.
    - **Beispiel für einen Verstoß**:
      ```java
      public void myMethod() {
          int MY_VAR = 1;
      }
      ```
    - **Warum beanstandet**: `MY_VAR` sollte `myVar` sein.

21. **MemberName**
    - **Zweck**: Instanzfelder müssen `camelCase` sein.
    - **Beispiel für einen Verstoß**:
      ```java
      public class MyClass {
          int my_field;
      }
      ```
    - **Warum beanstandet**: `my_field` sollte `myField` sein.

22. **MethodName**
    - **Zweck**: Methoden müssen `camelCase` sein.
    - **Beispiel für einen Verstoß**:
      ```java
      public void MyMethod() {}
      ```
    - **Warum beanstandet**: `MyMethod` sollte `myMethod` sein.

23. **PackageName**
    - **Zweck**: Pakete müssen kleingeschrieben sein und Punkte enthalten (z. B. `com.example`).
    - **Beispiel für einen Verstoß**:
      ```java
      package com.Example;
      ```
    - **Warum beanstandet**: `Example` sollte `example` sein.

24. **ParameterName**
    - **Zweck**: Methodenparameter müssen `camelCase` sein.
    - **Beispiel für einen Verstoß**:
      ```java
      public void myMethod(int MY_PARAM) {}
      ```
    - **Warum beanstandet**: `MY_PARAM` sollte `myParam` sein.

25. **StaticVariableName**
    - **Zweck**: Statische (non-final) Felder müssen einem Benennungsmuster folgen.
    - **Beispiel für einen Verstoß**:
      ```java
      public class MyClass {
          static int MY_FIELD;
      }
      ```
    - **Warum beanstandet**: `MY_FIELD` sollte `myField` sein (angenommen camelCase).

26. **TypeName**
    - **Zweck**: Klassen-/Interface-/Enum-Namen müssen `UpperCamelCase` sein.
    - **Beispiel für einen Verstoß**:
      ```java
      public class myClass {}
      ```
    - **Warum beanstandet**: `myClass` sollte `MyClass` sein.

---

#### Import-Prüfungen
Diese regulieren Import-Anweisungen.

27. **AvoidStarImport**
    - **Zweck**: Verbietet Wildcard-Imports (z. B. `import java.util.*`).
    - **Beispiel für einen Verstoß**:
      ```java
      import java.util.*;
      ```
    - **Warum beanstandet**: Verwendet `*` anstelle spezifischer Imports (z. B. `import java.util.List`).

28. **IllegalImport**
    - **Zweck**: Blockiert Imports aus eingeschränkten Paketen (z. B. `sun.*`).
    - **Beispiel für einen Verstoß**:
      ```java
      import sun.misc.Unsafe;
      ```
    - **Warum beanstandet**: `sun.misc.Unsafe` ist in einem eingeschränkten Paket.

29. **RedundantImport**
    - **Zweck**: Markiert doppelte oder unnötige Imports.
    - **Beispiel für einen Verstoß**:
      ```java
      import java.util.List;
      import java.util.List;
      ```
    - **Warum beanstandet**: Doppelter Import von `List`.

30. **UnusedImports**
    - **Zweck**: Erkennt ungenutzte Imports.
    - **Beispiel für einen Verstoß**:
      ```java
      import java.util.List;
      public class MyClass {}
      ```
    - **Warum beanstandet**: `List` ist importiert, wird aber nicht verwendet.

---

#### Größenprüfungen
Diese begrenzen die Anzahl von Methoden und Parametern.

31. **MethodLength**
    - **Zweck**: Begrenzt die Methodenlänge (Standard typisch 150 Zeilen).
    - **Beispiel für einen Verstoß**: Eine Methode mit 151 Zeilen.
    - **Warum beanstandet**: Überschreitet das Standard-Zeilenlimit.

32. **ParameterNumber**
    - **Zweck**: Begrenzt die Anzahl der Methodenparameter (Standard typisch 7).
    - **Beispiel für einen Verstoß**:
      ```java
      public void myMethod(int a, int b, int c, int d, int e, int f, int g, int h) {}
      ```
    - **Warum beanstandet**: 8 Parameter überschreiten das Standardlimit von 7.

---

#### Leerzeichenprüfungen
Diese erzwingen konsistente Leerzeichen im Code.

33. **EmptyForIteratorPad**
    - **Zweck**: Prüft die Leerzeichen in leeren `for`-Loop-Iteratoren.
    - **Beispiel für einen Verstoß**:
      ```java
      for (int i = 0; ; i++) {}
      ```
    - **Warum beanstandet**: Der leere Iterator-Abschnitt sollte ein Leerzeichen haben (z. B. `for (int i = 0; ; i++)`).

34. **GenericWhitespace**
    - **Zweck**: Stellt sicher, dass Abstände um generische Typen herum eingehalten werden (z. B. `List<String>`).
    - **Beispiel für einen Verstoß**:
      ```java
      List<String>list;
      ```
    - **Warum beanstandet**: Kein Leerzeichen zwischen `>` und `list`.

35. **MethodParamPad**
    - **Zweck**: Prüft die Leerzeichen vor Methodenparameterlisten.
    - **Beispiel für einen Verstoß**:
      ```java
      public void myMethod (int x) {}
      ```
    - **Warum beanstandet**: Das Leerzeichen vor `(int x)` ist falsch.

36. **NoWhitespaceAfter**
    - **Zweck**: Verbietet Leerzeichen nach bestimmten Tokens (z. B. `++`).
    - **Beispiel für einen Verstoß**:
      ```java
      int x = y ++ ;
      ```
    - **Warum beanstandet**: Leerzeichen nach `++`.

37. **NoWhitespaceBefore**
    - **Zweck**: Verbietet Leerzeichen vor bestimmten Tokens (z. B. `;`).
    - **Beispiel für einen Verstoß**:
      ```java
      int x = 1 ;
      ```
    - **Warum beanstandet**: Leerzeichen vor `;`.

38. **OperatorWrap**
    - **Zweck**: Stellt sicher, dass Operatoren in der korrekten Zeile stehen.
    - **Beispiel für einen Verstoß**:
      ```java
      int x = 1 +
          2;
      ```
    - **Warum beanstandet**: `+` sollte am Ende der ersten Zeile stehen.

39. **ParenPad**
    - **Zweck**: Prüft die Leerzeichen innerhalb von Klammern.
    - **Beispiel für einen Verstoß**:
      ```java
      if ( x == y ) {}
      ```
    - **Warum beanstandet**: Leerzeichen innerhalb von `(` und `)` sind falsch.

40. **TypecastParenPad**
    - **Zweck**: Stellt sicher, dass die Abstände in Typecasts korrekt sind.
    - **Beispiel für einen Verstoß**:
      ```java
      Object o = ( String ) obj;
      ```
    - **Warum beanstandet**: Leerzeichen innerhalb von `( String )` sind falsch.

41. **WhitespaceAfter**
    - **Zweck**: Verlangt Leerzeichen nach bestimmten Tokens (z. B. Kommas).
    - **Beispiel für einen Verstoß**:
      ```java
      int[] arr = {1,2,3};
      ```
    - **Warum beanstandet**: Fehlendes Leerzeichen nach den Kommas.

42. **WhitespaceAround**
    - **Zweck**: Stellt sicher, dass Leerzeichen um Operatoren/Schlüsselwörter vorhanden sind.
    - **Beispiel für einen Verstoß**:
      ```java
      if(x==y) {}
      ```
    - **Warum beanstandet**: Fehlende Leerzeichen um `==` und `if`.

---

#### Modifier-Prüfungen
Diese regulieren Java-Modifier.

43. **ModifierOrder**
    - **Zweck**: Stellt sicher, dass Modifier in der korrekten Reihenfolge sind (gemäß JLS).
    - **Beispiel für einen Verstoß**:
      ```java
      static public final int x = 1;
      ```
    - **Warum beanstandet**: Falsche Reihenfolge; sollte `public static final` sein.

44. **RedundantModifier**
    - **Zweck**: Markiert unnötige Modifier.
    - **Beispiel für einen Verstoß**:
      ```java
      public final class MyClass {
          public final void myMethod() {}
      }
      ```
    - **Warum beanstandet**: `final` bei einer Methode in einer `final`-Klasse ist redundant.

---

#### Block-Prüfungen
Diese erzwingen die korrekte Verwendung von Codeblöcken.

45. **AvoidNestedBlocks**
    - **Zweck**: Verbietet unnötige verschachtelte Blöcke.
    - **Beispiel für einen Verstoß**:
      ```java
      public void myMethod() {
          { int x = 1; }
      }
      ```
    - **Warum beanstandet**: Unnötiger verschachtelter Block.

46. **EmptyBlock**
    - **Zweck**: Markiert leere Blöcke.
    - **Beispiel für einen Verstoß**:
      ```java
      if (x == 1) {}
      ```
    - **Warum beanstandet**: Leerer `if`-Block.

47. **LeftCurly**
    - **Zweck**: Stellt sicher, dass öffnende geschweifte Klammern korrekt platziert sind.
    - **Beispiel für einen Verstoß**:
      ```java
      public class MyClass
      {
      }
      ```
    - **Warum beanstandet**: `{` sollte in derselben Zeile wie `class` stehen.

48. **NeedBraces**
    - **Zweck**: Verlangt geschweifte Klammern für Einzelanweisungsblöcke.
    - **Beispiel für einen Verstoß**:
      ```java
      if (x == 1) y = 2;
      ```
    - **Warum beanstandet**: Fehlende geschweifte Klammern; sollte `{ y = 2; }` sein.

49. **RightCurly**
    - **Zweck**: Stellt sicher, dass schließende geschweifte Klammern korrekt platziert sind.
    - **Beispiel für einen Verstoß**:
      ```java
      public class MyClass {
      }
      ```
    - **Warum beanstandet**: `}` sollte in einer neuen Zeile stehen (abhängig vom Stil).

---

#### Prüfungen für Coding-Probleme
Diese identifizieren häufige Codeprobleme.

50. **EmptyStatement**
    - **Zweck**: Markiert leere Anweisungen.
    - **Beispiel für einen Verstoß**:
      ```java
      int x = 1;; // Extra Semikolon
      ```
    - **Warum beanstandet**: Das extra `;` erzeugt eine leere Anweisung.

51. **EqualsHashCode**
    - **Zweck**: Stellt sicher, dass `equals()` und `hashCode()` gemeinsam überschrieben werden.
    - **Beispiel für einen Verstoß**:
      ```java
      public class MyClass {
          @Override
          public boolean equals(Object o) { return true; }
      }
      ```
    - **Warum beanstandet**: Fehlende `hashCode()`-Überschreibung.

52. **HiddenField**
    - **Zweck**: Erkennt Felder, die durch lokale Variablen/Parameter verdeckt werden.
    - **Beispiel für einen Verstoß**:
      ```java
      public class MyClass {
          int x;
          public void setX(int x) { this.x = x; }
      }
      ```
    - **Warum beanstandet**: Der Parameter `x` verdeckt das Feld `x`.

53. **IllegalInstantiation**
    - **Zweck**: Verbietet die Instanziierung bestimmter Klassen.
    - **Beispiel für einen Verstoß**:
      ```java
      String s = new String("test");
      ```
    - **Warum beanstandet**: Unnötige Instanziierung von `String`.

54. **InnerAssignment**
    - **Zweck**: Verbietet Zuweisungen in Ausdrücken.
    - **Beispiel für einen Verstoß**:
      ```java
      if (x = 1) {}
      ```
    - **Warum beanstandet**: Zuweisung `x = 1` im Ausdruck.

55. **MagicNumber**
    - **Zweck**: Markiert hartkodierte numerische Literale.
    - **Beispiel für einen Verstoß**:
      ```java
      int x = 42;
      ```
    - **Warum beanstandet**: `42` sollte eine benannte Konstante sein (z. B. `static final int MY_CONST = 42;`).

56. **MissingSwitchDefault**
    - **Zweck**: Verlangt einen `default`-Zweig in `switch`-Anweisungen.
    - **Beispiel für einen Verstoß**:
      ```java
      switch (x) {
          case 1: break;
      }
      ```
    - **Warum beanstandet**: Fehlender `default`-Zweig.

57. **MultipleVariableDeclarations**
    - **Zweck**: Verbietet mehrere Variablen in einer Deklaration.
    - **Beispiel für einen Verstoß**:
      ```java
      int x, y;
      ```
    - **Warum beanstandet**: Sollte `int x; int y;` sein.

58. **SimplifyBooleanExpression**
    - **Zweck**: Markiert komplexe boolesche Ausdrücke.
    - **Beispiel für einen Verstoß**:
      ```java
      if (x == true) {}
      ```
    - **Warum beanstandet**: Sollte `if (x)` sein.

59. **SimplifyBooleanReturn**
    - **Zweck**: Vereinfacht boolesche Rückgabeanweisungen.
    - **Beispiel für einen Verstoß**:
      ```java
      if (x) return true; else return false;
      ```
    - **Warum beanstandet**: Sollte `return x;` sein.

---

#### Prüfungen für Klassendesign
Diese erzwingen gutes Klassendesign.

60. **DesignForExtension**
    - **Zweck**: Stellt sicher, dass nicht-finale Klassen protected/abstract Methoden haben.
    - **Beispiel für einen Verstoß**:
      ```java
      public class MyClass {
          public void myMethod() {}
      }
      ```
    - **Warum beanstandet**: Nicht-finale Klasse hat eine nicht-protected/nicht-abstrakte Methode.

61. **FinalClass**
    - **Zweck**: Markiert Klassen mit privaten Konstruktoren als Kandidaten für `final`.
    - **Beispiel für einen Verstoß**:
      ```java
      public class MyClass {
          private MyClass() {}
      }
      ```
    - **Warum beanstandet**: Sollte `final` sein, da sie nicht erweitert werden kann.

62. **HideUtilityClassConstructor**
    - **Zweck**: Stellt sicher, dass Utility-Klassen private Konstruktoren haben.
    - **Beispiel für einen Verstoß**:
      ```java
      public class MyUtils {
          public static void doSomething() {}
      }
      ```
    - **Warum beanstandet**: Fehlender privater Konstruktor für die Utility-Klasse.

63. **InterfaceIsType**
    - **Zweck**: Verbietet Marker-Interfaces (ohne Methoden).
    - **Beispiel für einen Verstoß**:
      ```java
      public interface MyMarker {}
      ```
    - **Warum beanstandet**: Das Interface hat keine Methoden.

64. **VisibilityModifier**
    - **Zweck**: Erzwingt eine korrekte Feld-Sichtbarkeit (bevorzugt private mit Gettern/Settern).
    - **Beispiel für einen Verstoß**:
      ```java
      public class MyClass {
          public int x;
      }
      ```
    - **Warum beanstandet**: Feld `x` sollte `private` mit Zugriffsmethoden sein.

---

#### Verschiedene Prüfungen (Miscellaneous Checks)
Zusätzliche Prüfungen für Codequalität.

65. **ArrayTypeStyle**
    - **Zweck**: Erzwingt einen konsistenten Array-Deklarationsstil (`int[]` vs. `int []`).
    - **Beispiel für einen Verstoß**:
      ```java
      int x[];
      ```
    - **Warum beanstandet**: Sollte `int[] x` sein.

66. **FinalParameters**
    - **Zweck**: Verlangt, dass Methodenparameter `final` sind, wo möglich.
    - **Beispiel für einen Verstoß**:
      ```java
      public void myMethod(int x) {}
      ```
    - **Warum beanstandet**: Parameter `x` sollte `final int x` sein.

67. **TodoComment**
    - **Zweck**: Markiert `TODO`-Kommentare.
    - **Beispiel für einen Verstoß**:
      ```java
      // TODO: Fix this
      public void myMethod() {}
      ```
    - **Warum beanstandet**: `TODO`-Kommentar erkannt.

68. **UpperEll**
    - **Zweck**: Stellt sicher, dass `L` für long-Literale verwendet wird (nicht `l`).
    - **Beispiel für einen Verstoß**:
      ```java
      long x = 100l;
      ```
    - **Warum beanstandet**: `100l` sollte `100L` sein.

---

#### Unterdrückungsfilter (Inside TreeWalker)
Diese erlauben die Unterdrückung innerhalb des AST.

69. **SuppressionXpathFilter**
    - **Zweck**: Unterdrückt Prüfungen mittels XPath-Ausdrücken aus einer Datei (z. B. `checkstyle-xpath-suppressions.xml`).
    - **Beispiel für einen Verstoß**: Ähnlich wie `SuppressionFilter`, verwendet aber XPath (z. B. Unterdrückung von `JavadocMethod` für eine bestimmte Methode).

70. **SuppressWarningsHolder**
    - **Zweck**: Unterstützt `@SuppressWarnings("checkstyle:...")` im AST.
    - **Beispiel für einen Verstoß**:
      ```java
      public class MyClass {
          int MY_FIELD; // Verletzt MemberName
      }
      ```
      ```java
      @SuppressWarnings("checkstyle:MemberName")
      public class MyClass {
          int MY_FIELD; // Kein Verstoß
      }
      ```
    - **Warum beanstandet**: Ohne Unterdrückung verstößt `MY_FIELD` gegen `MemberName`.

---

### Wichtige Hinweise
- **Konfigurierbarkeit**: Regeln wie `LineLength` oder `MethodLength` können benutzerdefinierte Schwellenwerte haben (z. B. `max="120"` für `LineLength`).
- **Unterdrückung**: Verwenden Sie `@SuppressWarnings("checkstyle:<check-name>")` oder Suppression-Dateien, um bestimmte Prüfungen zu umgehen.
- **Integration**: Laufen mit Maven/Gradle oder IDE-Plugins; Fehler werden während des Builds gemeldet.
- **Header-Prüfung**: Inaktiv, es sei denn, sie wird auskommentiert und mit `checkstyle.header.file` konfiguriert.

Wenn Sie spezifische Anpassungsbeispiele benötigen (z. B. Ändern von `LineLength` auf 120), Behebungen für Verstöße oder Integrationsdetails, lassen Sie es mich wissen!