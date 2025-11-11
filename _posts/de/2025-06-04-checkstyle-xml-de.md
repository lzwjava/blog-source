---
audio: false
generated: true
lang: de
layout: post
title: Checkstyle-Konfiguration
translated: true
type: note
---

Dies ist eine Checkstyle-Konfigurationsdatei, geschrieben in XML, die entwickelt wurde, um Codierungsstandards und Best Practices für Java-Code durchzusetzen, basierend auf Suns Codierungskonventionen, der Java Language Specification, Javadoc-Richtlinien und einigen zusätzlichen Best Practices. Checkstyle ist ein statisches Code-Analyse-Tool, das Java-Quellcode auf die Einhaltung eines definierten Regelwerks überprüft. Im Folgenden werde ich die Struktur und die wichtigsten Komponenten dieser Konfigurationsdatei erklären.

---

### **Überblick**
- **Zweck**: Die Datei definiert Regeln zur Überprüfung von Java-, Properties- und XML-Dateien auf Verstöße gegen Codierungsstandards, wie Formatierung, Namenskonventionen, Javadoc-Anforderungen und Codestruktur.
- **Struktur**: Die Konfiguration ist hierarchisch mit `<module>`-Elementen organisiert, beginnend mit einem root `Checker`-Modul, das andere Module für spezifische Prüfungen oder Filter enthält.
- **Standards**: Sie richtet sich nach:
  - Java Language Specification (Java SE 11)
  - Sun Code Conventions
  - Javadoc-Richtlinien
  - JDK API-Dokumentation
  - Allgemeinen Best Practices
- **Hauptmerkmale**:
  - Konfigurierbarer Schweregrad (auf `error` gesetzt).
  - Unterstützt Dateierweiterungen: `.java`, `.properties`, `.xml`.
  - Ermöglicht die Unterdrückung spezifischer Prüfungen über Suppression-Dateien oder `@SuppressWarnings`-Annotationen.

---

### **Root-Modul: `<module name="Checker">`**
Das `Checker`-Modul ist das oberste Modul, das alle Prüfungen und Filter orchestriert.

- **Eigenschaften**:
  - `severity="error"`: Behandelt alle Verstöße als Fehler (andere Optionen sind `warning` oder `info`).
  - `fileExtensions="java, properties, xml"`: Wendet Prüfungen auf `.java`-, `.properties`- und `.xml`-Dateien an.

- **Untermodule**:
  - **Dateifilter**:
    - `BeforeExecutionExclusionFileFilter`: Schließt `module-info.java`-Dateien von Prüfungen aus (verwendet Regex `module\-info\.java$`).
  - **Unterdrückungsfilter**:
    - `SuppressionFilter`: Lädt Unterdrückungsregeln aus einer Datei (Standard: `checkstyle-suppressions.xml`). Wenn die Datei fehlt, ist sie optional (`optional="true"`).
    - `SuppressWarningsFilter`: Ermöglicht die Unterdrückung spezifischer Prüfungen mittels `@SuppressWarnings("checkstyle:...")`-Annotationen im Code.
  - **Verschiedene Prüfungen**:
    - `JavadocPackage`: Stellt sicher, dass jedes Paket eine `package-info.java`-Datei mit Javadoc hat.
    - `NewlineAtEndOfFile`: Prüft, dass Dateien mit einem Zeilenumbruch enden.
    - `Translation`: Überprüft, dass Properties-Dateien (z.B. für Internationalisierung) die gleichen Schlüssel über alle Übersetzungen hinweg enthalten.
  - **Größenprüfungen**:
    - `FileLength`: Prüft die Gesamtlänge einer Datei (Standardlimits gelten, sofern nicht überschrieben).
    - `LineLength`: Stellt sicher, dass Zeilen in `.java`-Dateien eine Standardlänge (typischerweise 80 oder 120 Zeichen, konfigurierbar) nicht überschreiten.
  - **Whitespace-Prüfungen**:
    - `FileTabCharacter`: Verbietet Tabulatorzeichen in Quelldateien (erzwingt Leerzeichen für Einrückungen).
    - `RegexpSingleline`: Erkennt nachgestellte Leerzeichen (Zeilen, die mit `\s+$` enden) und meldet sie mit der Nachricht "Line has trailing spaces."
  - **Header-Prüfung** (Auskommentiert):
    - `Header`: Wenn nicht auskommentiert, würde es einen spezifischen Dateiheader (z.B. einen Copyright-Hinweis) aus einer in `checkstyle.header.file` angegebenen Datei für `.java`-Dateien erzwingen.

---

### **Untermodul: `<module name="TreeWalker">`**
Das `TreeWalker`-Modul verarbeitet den abstrakten Syntaxbaum (AST) von Java-Quellcode, um detaillierte Prüfungen durchzuführen. Es enthält eine Vielzahl von Untermodulen, gruppiert nach Kategorien.

#### **Javadoc-Prüfungen**
Diese erzwingen korrekte Javadoc-Kommentare für Klassen, Methoden und Variablen:
- `InvalidJavadocPosition`: Stellt sicher, dass Javadoc-Kommentare korrekt platziert sind (z.B. vor einer Klasse oder Methode, nicht anderswo).
- `JavadocMethod`: Prüft, dass Methoden korrekte Javadoc-Kommentare haben, einschließlich Parameter, Rückgabetypen und Ausnahmen.
- `JavadocType`: Stellt sicher, dass Klassen, Interfaces und Enums Javadoc-Kommentare haben.
- `JavadocVariable`: Erfordert Javadoc für public/protected Felder.
- `JavadocStyle`: Erzwingt stilistische Regeln für Javadoc (z.B. korrekte HTML-Tags, keine fehlerhaften Kommentare).
- `MissingJavadocMethod`: Markiert Methoden, denen Javadoc-Kommentare fehlen.

#### **Namenskonventionen**
Diese stellen sicher, dass Bezeichner (Variablen, Methoden, Klassen usw.) Namenskonventionen folgen:
- `ConstantName`: Konstanten (z.B. `static final`) müssen einem Namensmuster folgen (typischerweise `UPPER_CASE`).
- `LocalFinalVariableName`: Lokale `final` Variablen müssen einem Namensmuster folgen (z.B. `camelCase`).
- `LocalVariableName`: Lokale Variablen müssen einem Namensmuster folgen (z.B. `camelCase`).
- `MemberName`: Instanzfelder müssen einem Namensmuster folgen (z.B. `camelCase`).
- `MethodName`: Methoden müssen einem Namensmuster folgen (z.B. `camelCase`).
- `PackageName`: Pakete müssen einem Namensmuster folgen (z.B. Kleinbuchstaben mit Punkten, wie `com.example`).
- `ParameterName`: Methodenparameter müssen einem Namensmuster folgen (z.B. `camelCase`).
- `StaticVariableName`: Statische (non-final) Felder müssen einem Namensmuster folgen.
- `TypeName`: Klassen-/Interface-/Enum-Namen müssen einem Namensmuster folgen (z.B. `UpperCamelCase`).

#### **Import-Prüfungen**
Diese regulieren die Verwendung von `import`-Anweisungen:
- `AvoidStarImport`: Verbietet Wildcard-Imports (z.B. `import java.util.*`).
- `IllegalImport`: Blockiert Imports aus eingeschränkten Paketen (Standard: `sun.*`).
- `RedundantImport`: Markiert doppelte oder unnötige Imports.
- `UnusedImports`: Erkennt ungenutzte Imports (ignoriert Javadoc-bezogene Imports mit `processJavadoc="false"`).

#### **Größenprüfungen**
Diese begrenzen die Größe von Methoden und Parametern:
- `MethodLength`: Stellt sicher, dass Methoden eine maximale Anzahl von Zeilen nicht überschreiten (Standard typischerweise 150).
- `ParameterNumber`: Begrenzt die Anzahl der Parameter in einer Methode (Standard typischerweise 7).

#### **Whitespace-Prüfungen**
Diese erzwingen eine konsistente Verwendung von Leerzeichen im Code:
- `EmptyForIteratorPad`: Prüft die Abstände in leeren `for`-Loop-Iteratoren (z.B. `for (int i = 0; ; i++)`).
- `GenericWhitespace`: Stellt sicher, dass korrekte Abstände um generische Typen herum vorhanden sind (z.B. `List<String>`).
- `MethodParamPad`: Prüft die Abstände vor Methodenparameterlisten.
- `NoWhitespaceAfter`: Verbietet Leerzeichen nach bestimmten Tokens (z.B. `++` oder Arrays).
- `NoWhitespaceBefore`: Verbietet Leerzeichen vor bestimmten Tokens (z.B. Semikolons).
- `OperatorWrap`: Stellt sicher, dass Operatoren (z.B. `+`, `=`) in der korrekten Zeile stehen.
- `ParenPad`: Prüft die Abstände innerhalb von Klammern (z.B. `( x )` vs. `(x)`).
- `TypecastParenPad`: Stellt sicher, dass korrekte Abstände in Typecasts vorhanden sind.
- `WhitespaceAfter`: Erfordert Leerzeichen nach bestimmten Tokens (z.B. Kommas, Semikolons).
- `WhitespaceAround`: Stellt sicher, dass Leerzeichen um Operatoren und Schlüsselwörter herum vorhanden sind (z.B. `if (x == y)`).

#### **Modifier-Prüfungen**
Diese regulieren die Verwendung von Java-Modifiern:
- `ModifierOrder`: Stellt sicher, dass Modifier in der korrekten Reihenfolge sind (z.B. `public static final`, gemäß JLS).
- `RedundantModifier`: Markiert unnötige Modifier (z.B. `final` in einer `final`-Klasse).

#### **Block-Prüfungen**
Diese erzwingen die korrekte Verwendung von Codeblöcken (`{}`):
- `AvoidNestedBlocks`: Verbietet unnötige verschachtelte Blöcke (z.B. `{ { ... } }`).
- `EmptyBlock`: Markiert leere Blöcke (z.B. `{}`), sofern nicht beabsichtigt.
- `LeftCurly`: Stellt sicher, dass öffnende geschweifte Klammern (`{`) korrekt platziert sind (z.B. am Ende einer Zeile).
- `NeedBraces`: Erfordert geschweifte Klammern für Einzelanweisungsblöcke (z.B. `if (x) y();` muss `if (x) { y(); }` sein).
- `RightCurly`: Stellt sicher, dass schließende geschweifte Klammern (`}`) korrekt platziert sind (z.B. in einer neuen Zeile oder derselben Zeile, abhängig vom Stil).

#### **Coding-Problem-Prüfungen**
Diese identifizieren häufige Codierungsprobleme:
- `EmptyStatement`: Markiert leere Anweisungen (z.B. `;;`).
- `EqualsHashCode`: Stellt sicher, dass, wenn `equals()` überschrieben wird, auch `hashCode()` überschrieben wird.
- `HiddenField`: Erkennt Felder, die durch lokale Variablen oder Parameter verdeckt werden.
- `IllegalInstantiation`: Verbietet die Instanziierung bestimmter Klassen (z.B. `java.lang`-Klassen wie `String`).
- `InnerAssignment`: Untersagt Zuweisungen innerhalb von Ausdrücken (z.B. `if (x = y)`).
- `MagicNumber`: Markiert hartkodierte numerische Literale (z.B. `42`), sofern nicht in spezifischen Kontexten.
- `MissingSwitchDefault`: Erfordert einen `default`-Zweig in `switch`-Anweisungen.
- `MultipleVariableDeclarations`: Verbietet die Deklaration mehrerer Variablen in einer einzelnen Zeile (z.B. `int x, y;`).
- `SimplifyBooleanExpression`: Markiert übermäßig komplexe boolesche Ausdrücke (z.B. `if (x == true)`).
- `SimplifyBooleanReturn`: Vereinfacht boolesche Rückgabeanweisungen (z.B. `if (x) return true; else return false;`).

#### **Class-Design-Prüfungen**
Diese erzwingen gute Class-Design-Praktiken:
- `DesignForExtension`: Stellt sicher, dass nicht-finale Klassen protected oder abstract Methoden für Erweiterbarkeit haben.
- `FinalClass`: Markiert Klassen mit nur privaten Konstruktoren als Kandidaten für `final`.
- `HideUtilityClassConstructor`: Stellt sicher, dass Utility-Klassen (mit nur statischen Mitgliedern) private Konstruktoren haben.
- `InterfaceIsType`: Verbietet Interfaces, die ausschließlich als Marker-Interfaces (ohne Methoden) verwendet werden.
- `VisibilityModifier`: Erzwingt korrekte Sichtbarkeit für Felder (z.B. bevorzugt private Felder mit Gettern/Settern).

#### **Verschiedene Prüfungen**
- `ArrayTypeStyle`: Erzwingt einen konsistenten Array-Deklarationsstil (z.B. `int[]` vs. `int []`).
- `FinalParameters`: Erfordert, dass Methodenparameter `final` sind, wo möglich.
- `TodoComment`: Markiert `TODO`-Kommentare im Code (nützlich zur Verfolgung unvollständiger Arbeit).
- `UpperEll`: Stellt sicher, dass der Buchstabe `L` für long-Literale verwendet wird (z.B. `100L` statt `100l`).

#### **Unterdrückungsfilter (Innerhalb TreeWalker)**
- `SuppressionXpathFilter`: Ermöglicht die Unterdrückung von Prüfungen mittels XPath-Ausdrücken, die in einer Datei definiert sind (Standard: `checkstyle-xpath-suppressions.xml`, optional).
- `SuppressWarningsHolder`: Unterstützt `@SuppressWarnings("checkstyle:...")`-Annotationen zur Unterdrückung spezifischer Prüfungen innerhalb des AST.

---

### **Wichtige Punkte**
- **Konfigurierbarkeit**: Die meisten Module haben Standardeinstellungen, können aber über Eigenschaften angepasst werden (z.B. kann `LineLength` eine spezifische `max`-Länge setzen).
- **Unterdrückung**: Die Konfiguration unterstützt flexible Unterdrückung von Prüfungen über externe Dateien (`checkstyle-suppressions.xml`, `checkstyle-xpath-suppressions.xml`) oder Annotationen.
- **Erweiterbarkeit**: Zusätzliche Prüfungen können hinzugefügt werden, und bestehende können durch Auskommentieren oder Entfernen deaktiviert werden.
- **Dokumentation**: Die Konfiguration verweist auf Checkstyles Dokumentation (z.B. `https://checkstyle.org`) für Details zu jedem Modul.
- **Header-Prüfung**: Das `Header`-Modul ist auskommentiert, daher ist es nicht aktiv, es sei denn, es wird auskommentiert und mit einer Header-Datei konfiguriert.

---

### **Wie es verwendet wird**
1. **Integration**: Diese Datei wird typischerweise mit einem Build-Tool wie Maven, Gradle oder einem IDE-Plugin verwendet, um Checkstyle während des Build-Prozesses oder in der Entwicklung auszuführen.
2. **Verstoßmeldung**: Wenn Code gegen eine Regel verstößt (z.B. eine Zeile die maximale Länge überschreitet), meldet Checkstyle dies als Fehler (aufgrund von `severity="error"`).
3. **Unterdrückung**: Entwickler können spezifische Verstöße mit `@SuppressWarnings("checkstyle:<check-name>")` oder durch das Definieren von Regeln in Suppression-Dateien unterdrücken.
4. **Anpassung**: Eigenschaften wie `basedir`, `checkstyle.header.file` oder Suppression-Dateipfade können extern gesetzt werden (z.B. über Build-Tool-Konfigurationen).

---

### **Beispielverstöße**
- **JavadocMethod**: Eine public Methode ohne Javadoc löst einen Fehler aus.
- **LineLength**: Eine Zeile in einer `.java`-Datei, die das Standardmaximum (z.B. 80 Zeichen) überschreitet, wird markiert.
- **AvoidStarImport**: Die Verwendung von `import java.util.*` verursacht einen Fehler.
- **MagicNumber**: Das Schreiben von `int x = 42;` ohne eine benannte Konstante wird markiert.

---

Wenn Sie eine tiefere Erklärung eines spezifischen Moduls, Beispiele für Verstöße oder Anleitung zur Anpassung dieser Konfiguration benötigen, lassen Sie es mich wissen!