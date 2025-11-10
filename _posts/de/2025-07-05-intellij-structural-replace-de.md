---
audio: false
generated: true
lang: de
layout: post
title: Beherrschen des Strukturellen Ersetzens in IntelliJ
translated: true
type: note
---

Sicher, lassen Sie uns die Funktion "Structural Replace" von IntelliJ IDEA aufschlüsseln.

Die Funktion "Structural Replace" von IntelliJ IDEA ist eine unglaublich leistungsstarke, aber oft ungenutzte Funktion, die es Ihnen ermöglicht, Codemuster basierend auf ihrer **Struktur** zu finden und zu ersetzen, und nicht nur basierend auf ihrem Textinhalt. Dies geht weit über die einfache Textsuche und -ersetzung hinaus und ermöglicht komplexe Refactorings, die Durchsetzung von Codierungsstilen und die Behebung von Fehlern in einer großen Codebasis.

Hier ist eine umfassende Anleitung:

-----

## IntelliJ IDEA Structural Replace: Eine umfassende Anleitung

### 1. Was ist Structural Search and Replace (SSR)?

Im Kern geht es bei SSR in IntelliJ IDEA um die Arbeit mit Abstract Syntax Trees (ASTs). Anstatt nach literalem Text zu suchen, definieren Sie ein *Muster*, das die Struktur des Codes beschreibt, den Sie finden möchten (Structural Search), und ein weiteres Muster, das beschreibt, wie Sie ihn transformieren möchten (Structural Replace).

Dies ermöglicht Ihnen:

* **Code refactoren:** Die Art und Weise ändern, wie Methoden aufgerufen werden, Parameter neu anordnen, Felder kapseln usw.
* **Codierungsstandards durchsetzen:** Konsistente Verwendung bestimmter Sprachkonstrukte oder API-Aufrufe sicherstellen.
* **Häufige Fehler beheben:** Wiederkehrende logische Fehler identifizieren und korrigieren.
* **APIs migrieren:** Code aktualisieren, wenn sich Bibliotheken oder Frameworks ändern.
* **Veralteten Code bereinigen:** Alte API-Verwendungen finden und durch neue ersetzen.

### 2. Zugriff auf Structural Search and Replace

Sie können auf den SSR-Dialog auf zwei Arten zugreifen:

* **Gehe zu Edit -> Find -> Search Structurally...** (für die Suche)
* **Gehe zu Edit -> Find -> Replace Structurally...** (für den direkten Ersatz)

Der Dialog für beide ist sehr ähnlich, wobei "Replace Structurally" lediglich ein "Replace Template"-Feld hinzufügt.

### 3. Den Structural Search-Dialog verstehen

Der Structural Search-Dialog ist der Ort, an dem Sie Ihr Suchmuster definieren.

#### 3.1. Suchvorlage (Search Template)

Dies ist der wichtigste Teil. Sie schreiben ein Code-Snippet, das die *Struktur* repräsentiert, nach der Sie suchen.

**Schlüsselkonzepte:**

* **Literal Code:** Jeder Code, den Sie direkt schreiben, wird wörtlich übereinstimmen.
* **Variablen:** Verwenden Sie Variablen, um Teile des Codes darzustellen, die variieren können. Variablen werden mit einer speziellen Syntax definiert und dann mit Einschränkungen konfiguriert.
    * **Häufige Variablensyntax:** `$VariablenName$` (in Dollarzeichen eingeschlossen).
    * **Beispiel:** `System.out.println($arg$);` findet jeden `System.out.println`-Aufruf, wobei `$arg$` auf das passt, was innerhalb der Klammern steht.

#### 3.2. Skript-Einschränkungen (für Variablen)

Nachdem Sie Variablen in Ihrer "Search Template" definiert haben, müssen Sie deren Einschränkungen spezifizieren. Dies geschieht, indem Sie die Variable in der Vorlage auswählen (oder den Cursor darauf setzen) und dann die Schaltfläche "Edit variables" verwenden (oft ein kleiner Stiftsymbol neben dem Vorlagenfeld oder über den Tab "Variables" zugänglich).

Häufige Einschränkungen sind:

* **Text (regexp):** Ein regulärer Ausdruck, dem der Textinhalt der Variable entsprechen muss.
* **Type (regexp):** Ein regulärer Ausdruck, dem der Typ der Variable entsprechen muss (z.B. `java.lang.String`, `int[]`).
* **Count:** Gibt an, wie oft ein Variablenelement erscheinen kann (z.B. `[0, N]`, `[1, N]`, `[1, 1]`). Dies ist besonders nützlich für Sammlungen von Anweisungen oder Methodenparametern.
* **Reference:** Wenn die Variable einen Bezeichner darstellt (wie einen Methoden- oder Variablennamen), können Sie ihn so einschränken, dass er auf einen bestimmten Typ oder eine bestimmte Deklaration verweist.
* **Within:** Schränkt die Variable auf einen bestimmten Gültigkeitsbereich oder eine bestimmte Deklaration ein.
* **Not RegExp:** Schließt Übereinstimmungen basierend auf einem regulären Ausdruck aus.
* **Condition (Groovy script):** Dies ist die leistungsstärkste Einschränkung. Sie können ein Groovy-Skript schreiben, das zu `true` oder `false` ausgewertet wird. Dieses Skript hat Zugriff auf das gefundene Element und seine Eigenschaften, was sehr komplexe Logik ermöglicht.
    * **Beispielskript:** Um zu prüfen, ob der Wert einer Integer-Variable größer als 10 ist: `_target.text.toInteger() > 10` (wobei `_target` das gefundene Element für die Variable ist).

#### 3.3. Optionen

Unterhalb der Vorlage gibt es verschiedene Optionen, um Ihre Suche zu verfeinern:

* **Context:** Definiert den Gültigkeitsbereich der Suche (z.B. gesamtes Projekt, Modul, Verzeichnis, ausgewählte Dateien, benutzerdefinierter Bereich).
* **File type:** Schränkt die Suche auf bestimmte Dateitypen ein (Java, Kotlin, XML usw.).
* **Case sensitive:** Standard-Umschaltung für Groß-/Kleinschreibung.
* **Match case/whole words:** Anwendbar für Text innerhalb der Vorlage.
* **Match line breaks:** Wichtig für mehrzeilige Muster.
* **Save Template:** Speichert Ihre aktuelle Suchvorlage für die zukünftige Verwendung.

### 4. Den Structural Replace-Dialog verstehen

Der Structural Replace-Dialog fügt dem "Search Template" und den für die Suche definierten "Variables" ein "Replace Template"-Feld hinzu.

#### 4.1. Ersetzungsvorlage (Replace Template)

Hier definieren Sie, wie die gefundene Codestruktur transformiert werden soll.

* **Variablen aus der Suchvorlage:** Sie können dieselben Variablen, die in Ihrer "Search Template" definiert sind, innerhalb der "Replace Template" verwenden. Der Inhalt, der durch die Variable in der Suche gefunden wurde, wird in die Ersetzungsvorlage eingefügt.
* **Neuer Code:** Sie können neue Codeelemente einführen, vorhandene neu anordnen oder Teile entfernen.
* **Beispiel:**
    * **Suchvorlage:** `System.out.println($arg$);`
    * **Ersetzungsvorlage:** `LOGGER.info($arg$);`
    * Dies würde `System.out.println("Hello");` in `LOGGER.info("Hello");` ändern.

#### 4.2. Shorten FQ Names

Diese Option (oft automatisch aktiviert) versucht, vollqualifizierte Klassennamen (z.B. `java.util.ArrayList`) durch ihre Kurznamen (z.B. `ArrayList`) zu ersetzen und die notwendigen Import-Anweisungen hinzuzufügen. Dies ist entscheidend, um lesbaren Code zu erhalten.

#### 4.3. Formatierung

IntelliJ IDEA wird den ersetzten Code normalerweise gemäß den Code-Style-Einstellungen Ihres Projekts neu formatieren, was sehr wünschenswert ist.

### 5. Praktische Beispiele

Lassen Sie uns dies mit einigen gängigen Szenarien veranschaulichen.

#### Beispiel 1: Ersetzen von `System.out.println` durch einen Logger

**Ziel:** Ändere alle `System.out.println("message");` in `LOGGER.info("message");` (angenommen, `LOGGER` ist ein statisches final-Feld).

1.  **Structural Replace öffnen:** `Edit -> Find -> Replace Structurally...`
2.  **Suchvorlage:**
    ```java
    System.out.println($arg$);
    ```
3.  **Variablen:** Klicken Sie auf "Edit variables" oder gehen Sie zum Tab "Variables".
    * Wählen Sie `$arg$`.
    * **Count:** `[1, 1]` (ein Argument).
    * **Type (regexp):** `java.lang.String` (wenn Sie nur String-Literale ersetzen möchten, andernfalls leer lassen für jeden Typ).
4.  **Ersetzungsvorlage:**
    ```java
    LOGGER.info($arg$);
    ```
5.  **Ausführen:** Klicken Sie auf "Find", um die Änderungen in der Vorschau zu sehen, dann "Replace All", wenn Sie zufrieden sind.

#### Beispiel 2: Vertauschen von Methodenparametern

**Ziel:** Ändere `someMethod(paramA, paramB)` in `someMethod(paramB, paramA)`.

1.  **Suchvorlage:**
    ```java
    someMethod($paramA$, $paramB$);
    ```
2.  **Variablen:**
    * `$paramA$`: `Count: [1,1]`, `Type (regexp): .*` (beliebiger Typ)
    * `$paramB$`: `Count: [1,1]`, `Type (regexp): .*` (beliebiger Typ)
3.  **Ersetzungsvorlage:**
    ```java
    someMethod($paramB$, $paramA$);
    ```

#### Beispiel 3: Kapseln eines Feldes (einfacher Fall)

**Ziel:** Wenn Sie öffentliche Felder wie `public String name;` haben und den direkten Zugriff `obj.name` durch `obj.getName()` ersetzen möchten. (Dies ist ein vereinfachtes Beispiel; oft würden Sie dedizierte Refactorings für die Kapselung verwenden).

1.  **Suchvorlage:**
    ```java
    $object$.$fieldName$;
    ```
2.  **Variablen:**
    * `$object$`: `Count: [1,1]`, `Type (regexp): .*`
    * `$fieldName$`: `Count: [1,1]`, `Text (regexp): name` (speziell das Feld `name` anzielen).
3.  **Ersetzungsvorlage:**
    ```java
    $object$.get$fieldName$();
    ```
    * **Hinweis:** Möglicherweise müssen Sie die Großschreibung anpassen, wenn `get$fieldName$` nicht automatisch `name` zu `Name` großschreibt. Dafür könnten Sie ein Groovy-Skript für `$fieldName$` innerhalb der Ersetzungsvorlage verwenden, aber das wird komplexer. Ein einfacherer Ansatz für diesen speziellen Fall sind oft zwei SSRs oder ein dediziertes Refactoring. Für `get$fieldName$()` behandelt die IDE die Großschreibung normalerweise für gängige Getter-Muster.

#### Beispiel 4: Finden leerer `catch`-Blöcke

**Ziel:** Finde alle `catch`-Blöcke, die leer sind (oder nur Kommentare/Leerzeichen enthalten).

1.  **Suchvorlage:**
    ```java
    try {
        $statements$;
    } catch ($exceptionType$ $exceptionVariable$) {
        $emptyBody$;
    }
    ```
2.  **Variablen:**
    * `$statements$`: `Count: [0, N]` (null oder mehr Anweisungen im try-Block)
    * `$exceptionType$`: `Count: [1,1]`
    * `$exceptionVariable$`: `Count: [1,1]`
    * `$emptyBody$`: `Count: [0, 0]` (dies ist der Schlüssel für einen leeren Körper)

#### Beispiel 5: Verwenden von Groovy-Skript für erweiterte Bedingungen

**Ziel:** Finde `if`-Anweisungen, bei denen die Bedingung eine Konstante `true` ist.

1.  **Suchvorlage:**
    ```java
    if ($condition$) {
        $thenBranch$;
    }
    ```
2.  **Variablen:**
    * `$condition$`: `Count: [1,1]`
        * **Condition (Groovy script):** `_target.text == "true"` (dies prüft den literalen Text der Bedingung).
    * `$thenBranch$`: `Count: [0, N]`

### 6. Tipps und Best Practices

* **Fangen Sie einfach an:** Beginnen Sie mit grundlegenden Mustern und steigern Sie allmählich die Komplexität.
* **Verwenden Sie zuerst `Find`:** Verwenden Sie immer "Find" (Structural Search) vor "Replace", um die Übereinstimmungen in der Vorschau zu sehen und sicherzustellen, dass Ihr Muster korrekt ist.
* **Testen Sie in einem kleinen Gültigkeitsbereich:** Testen Sie Ihr Muster vor einem großflächigen Ersatz an einem kleinen, isolierten Satz von Dateien.
* **Vorlagen speichern:** Speichern Sie häufig verwendete oder komplexe Vorlagen zur einfachen Wiederverwendung.
* **Nutzen Sie vorhandene Vorlagen:** IntelliJ IDEA bringt viele vordefinierte Structural Search and Replace-Vorlagen mit. Sie finden diese, indem Sie auf das "Lupe mit Plus"-Symbol im SSR-Dialog klicken und die vorhandenen Vorlagen durchsuchen. Dies sind ausgezeichnete Lernressourcen.
* **Leistung von Groovy-Skripten:** Für sehr spezifische oder kontextsensitive Übereinstimmungen sind Groovy-Skripte unschätzbar. Lernen Sie die Grundlagen, wie auf Elemente (`_target`, `_target.parent`, `_target.text`, `_target.type` usw.) innerhalb des Skripts zugegriffen wird.
* **Verstehen Sie die Übereinstimmungstypen:** Seien Sie sich bewusst, was Ihre Variablen abgleichen (z.B. eine Anweisung, ein Ausdruck, ein Typ, ein Variablenname). Dies beeinflusst die Einschränkungen, die Sie anwenden können.
* **Reguläre Ausdrücke:** Ein gutes Verständnis von regulären Ausdrücken wird Ihre Fähigkeit, `Text`- und `Type`-Einschränkungen zu definieren, erheblich verbessern.
* **Debugging:** Wenn Ihr Muster nicht wie erwartet übereinstimmt, vereinfachen Sie es. Entfernen Sie Einschränkungen nacheinander, bis es beginnt, Übereinstimmungen zu finden, und führen Sie sie dann wieder ein, um das Problem einzugrenzen.
* **Sichern Sie Ihren Code:** Stellen Sie vor jedem größeren Structural Replace-Vorgang in einer großen Codebasis sicher, dass Sie ein Backup haben oder in einem Versionskontrollsystem arbeiten, in dem Sie Änderungen leicht rückgängig machen können.

### 7. Einschränkungen

* **Komplexität:** Sehr komplexe oder stark kontextbezogene Ersetzungen könnten schwierig oder unmöglich sein, allein mit SSR auszudrücken. Manchmal ist ein benutzerdefiniertes IntelliJ IDEA-Plugin oder ein dediziertes Skript möglicherweise angemessener.
* **Leistung:** Extrem breite oder komplexe Muster, die auf einer sehr großen Codebasis ausgeführt werden, können langsam sein.
* **Mehrdeutigkeit:** Seien Sie vorsichtig mit zu allgemeinen Mustern, da sie möglicherweise unbeabsichtigt Code finden und ändern, den Sie nicht beabsichtigt hatten.

-----

Durch die Beherrschung von IntelliJ IDEA's Structural Search and Replace erhalten Sie ein leistungsstarkes Werkzeug zur Aufrechterhaltung der Codequalität, zur Durchführung großflächiger Refactorings und zur Automatisierung langwieriger Codeänderungen. Es ist eine Funktion, die Entwickler wirklich befähigt, effizienter und konsistenter in ihren Projekten zu arbeiten.