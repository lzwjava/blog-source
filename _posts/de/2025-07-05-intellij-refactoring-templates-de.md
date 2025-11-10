---
audio: false
generated: true
lang: de
layout: post
title: IntelliJ Strukturelle Ersetzungsvorlagen
translated: true
type: note
---

Hier sind 10 Beispiele für Structural Replacement-Templates von IntelliJ, zur besseren Übersicht kategorisiert. Diese können unglaublich mächtig für Refactoring, die Durchsetzung von Coding-Standards und die Automatisierung gängiger Code-Transformationen sein.

**Grundlegendes Refactoring & Vereinfachung:**

1.  **Ersetze `if (condition) return true; else return false;` durch `return condition;`**

      * **Such-Template:**
        ```java
        if ($CONDITION$) {
            return true;
        } else {
            return false;
        }
        ```
      * **Ersatz-Template:**
        ```java
        return $CONDITION$;
        ```
      * **Kontext:** Vereinfacht boolesche Rückgabestatements.

2.  **Ersetze `if (condition) { statement; }` durch `if (!condition) { continue/break/return; }` (Guard Clause)**

      * **Such-Template:**
        ```java
        if ($CONDITION$) {
            $STATEMENTS$;
        }
        ```
      * **Ersatz-Template:** (Hier geht es mehr um das Vorschlagen einer Transformation; den inneren Teil würden Sie manuell anpassen)
        ```java
        if (!$CONDITION$) {
            // Erwägen Sie continue, break oder return hier
        }
        $STATEMENTS$;
        ```
      * **Kontext:** Ermutigt zur Verwendung von Guard Clauses für einen sauberen Codefluss. Typischerweise würden Sie eine "Replace with"-Aktion verwenden, nachdem die Struktur gefunden wurde.

**Collection & Stream-Operationen:**

3.  **Ersetze `for (Type item : collection) { if (item.getProperty() == value) { ... } }` durch Stream `filter`**

      * **Such-Template:**
        ```java
        for ($TYPE$ $ITEM$ : $COLLECTION$) {
            if ($ITEM$.$METHOD$($VALUE$)) {
                $STATEMENTS$;
            }
        }
        ```
      * **Ersatz-Template:**
        ```java
        $COLLECTION$.stream()
            .filter($ITEM$ -> $ITEM$.$METHOD$($VALUE$))
            .forEach($ITEM$ -> $STATEMENTS$); // Oder .map().collect(), etc.
        ```
      * **Kontext:** Migration von traditionellen Schleifen zu Java Streams für Filterungen. Dies ist ein allgemeines Beispiel; für `map`, `collect` usw. benötigen Sie wahrscheinlich spezifischere Templates.

4.  **Ersetze `new ArrayList<>().add(item1); new ArrayList<>().add(item2);` durch `List.of(item1, item2);`**

      * **Such-Template:** (Dies könnte mehrere Templates für eine unterschiedliche Anzahl von `add`-Aufrufen erfordern, oder einen komplexeren Regex für `add`-Aufrufe. Ein einfacherer Ansatz für 2 Items):
        ```java
        java.util.ArrayList<$TYPE$> $LIST$ = new java.util.ArrayList<>();
        $LIST$.add($ITEM1$);
        $LIST$.add($ITEM2$);
        ```
      * **Ersatz-Template:**
        ```java
        java.util.List<$TYPE$> $LIST$ = java.util.List.of($ITEM1$, $ITEM2$);
        ```
      * **Kontext:** Verwendung von Java 9+ `List.of()` für immutable Listen.

**Fehlerbehandlung & Ressourcenmanagement:**

5.  **Ersetze `try { ... } catch (Exception e) { e.printStackTrace(); }` durch spezifischeres Logging**

      * **Such-Template:**
        ```java
        try {
            $STATEMENTS$;
        } catch (java.lang.Exception $EXCEPTION$) {
            $EXCEPTION$.printStackTrace();
        }
        ```
      * **Ersatz-Template:**
        ```java
        try {
            $STATEMENTS$;
        } catch (java.lang.Exception $EXCEPTION$) {
            // Ersetzen Sie dies durch Ihr bevorzugtes Logging-Framework, z.B.:
            // logger.error("Ein Fehler ist aufgetreten", $EXCEPTION$);
            throw new RuntimeException($EXCEPTION$); // Oder werfen Sie eine spezifischere Exception erneut
        }
        ```
      * **Kontext:** Ermutigt zu einer ordentlichen Fehlerprotokollierung anstelle des einfachen Ausgebens von Stack Traces.

6.  **Ersetze `try { ... } finally { closeable.close(); }` durch `try-with-resources`**

      * **Such-Template:**
        ```java
        java.io.Closeable $CLOSEABLE$ = null;
        try {
            $CLOSEABLE$ = $INITIALIZATION$;
            $STATEMENTS$;
        } finally {
            if ($CLOSEABLE$ != null) {
                $CLOSEABLE$.close();
            }
        }
        ```
      * **Ersatz-Template:**
        ```java
        try ($CLOSEABLE$ = $INITIALIZATION$) {
            $STATEMENTS$;
        }
        ```
      * **Kontext:** Modernisierung des Ressourcenmanagements durch Verwendung von `try-with-resources` (Java 7+).

**Klassen- & Methodenstruktur:**

7.  **Finde Felder, die `final` sein können**

      * **Such-Template:**
        ```java
        class $CLASS$ {
            $TYPE$ $FIELD$;
        }
        ```
      * **Ersatz-Template:** (Dies dient eher zum Finden, dann verwenden Sie einen Quick Fix)
        ```java
        class $CLASS$ {
            // Erwägen Sie, dieses Feld final zu machen, wenn es nur einmal zugewiesen wird
            final $TYPE$ $FIELD$;
        }
        ```
      * **Kontext:** Identifizierung von Möglichkeiten, die Unveränderlichkeit zu verbessern. Sie würden einen Filter einrichten, um nur Felder ohne mehrere Zuweisungen anzuzeigen.

8.  **Ersetze `private static final Logger logger = LoggerFactory.getLogger(MyClass.class);` durch ein benutzerdefiniertes Logger-Utility**

      * **Such-Template:**
        ```java
        private static final org.slf4j.Logger $LOGGER_VAR$ = org.slf4j.LoggerFactory.getLogger($CLASS_NAME$.class);
        ```
      * **Ersatz-Template:**
        ```java
        private static final org.slf4j.Logger $LOGGER_VAR$ = com.yourcompany.util.LoggerProvider.getLogger(); // Oder ein spezifischeres getLogger($CLASS_NAME$.class) von Ihrem Utility
        ```
      * **Kontext:** Durchsetzung eines spezifischen Logger-Initialisierungsmusters in Ihrer Codebase.

**Annotations & Boilerplate:**

9.  **Füge `@Override` zu Methoden hinzu, die Superclass-Methoden überschreiben (falls fehlend)**

      * **Such-Template:** (Dies ist komplexer und wird oft besser von IntelliJs eingebauten Inspections gehandhabt, aber zur Demonstration)
        ```java
        class $CLASS$ {
            $RETURN_TYPE$ $METHOD$($PARAMS$) {
                $STATEMENTS$;
            }
        }
        ```
      * **Ersatz-Template:** (Auch hier: zum Finden, dann Anwenden eines Quick Fixes)
        ```java
        class $CLASS$ {
            @Override // Hinzufügen, falls es eine Superclass-Methode überschreibt
            $RETURN_TYPE$ $METHOD$($PARAMS$) {
                $STATEMENTS$;
            }
        }
        ```
      * **Kontext:** Durchsetzung von Best Practices und Auffangen von Tippfehlern. Sie würden einen Filter verwenden, um zu prüfen, ob die Methode in einer Superclass/Schnittstelle existiert.

10. **Ersetze repetitive `getter/setter`-Methoden durch Lombok-Annotationen**

      * **Such-Template:** (Für einen einzelnen Getter wäre dies für eine Klasse sehr repetitiv)
        ```java
        public $TYPE$ get$PROPERTY_NAME$() {
            return this.$FIELD_NAME$;
        }
        ```
      * **Ersatz-Template:** (Dies ist konzeptionell, da Sie den Getter löschen und `@Getter` zum Feld oder zur Klasse hinzufügen würden)
        ```java
        // Erwägen Sie, dies durch @lombok.Getter auf dem Feld zu ersetzen:
        // @lombok.Getter
        // private $TYPE$ $FIELD_NAME$;
        ```
      * **Kontext:** Automatisierung des Übergangs zu Lombok. Für eine vollständige Klasse könnten Sie die Klasse selbst ins Visier nehmen und `@Data` oder `@Getter/@Setter`-Annotationen basierend auf dem Vorhandensein dieser Methoden vorschlagen. Dies ist eine der fortgeschritteneren und potenziell mehrstufigen Transformationen.

**So verwenden Sie sie in IntelliJ:**

1.  Gehen Sie zu `Analyze` -> `Inspect Code...`
2.  Klicken Sie im Fenster `Inspection Profile` auf die `...` neben dem Profilnamen, um es zu bearbeiten.
3.  Navigieren Sie zu `Java` -> `General` -> `Structural Search Inspection`.
4.  Klicken Sie auf die `+` Schaltfläche, um ein neues Such-/Ersatz-Template hinzuzufügen.
5.  Definieren Sie Ihr `Search Template` und `Replacement Template`.
6.  Verwenden Sie den Tab `Variables`, um Einschränkungen für Ihre Variablen zu definieren (z.B. Typ, Text, Anzahl).
7.  Führen Sie die Inspection für Ihren Code aus. IntelliJ wird Ersetzungen vorschlagen oder Funde hervorheben.

Diese Beispiele demonstrieren die Vielseitigkeit von Structural Search and Replace. Je spezifischer und eingeschränkter Ihre Templates sind, desto genauer und nützlicher werden die Ersetzungen sein.