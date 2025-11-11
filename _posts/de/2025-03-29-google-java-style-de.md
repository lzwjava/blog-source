---
audio: false
generated: true
lang: de
layout: post
title: Google Java Style Guide
translated: true
type: note
---

## 1. Grundlagen zu Quelldateien
- **Dateibenennung**:
  - Quelldateien werden mit dem groß-/kleinschreibungs-sensitiven Namen der Top-Level-Klasse benannt, die sie enthalten
  - Dateien müssen UTF-8-Kodierung verwenden
  - Sonderzeichen in Dateinamen sind nicht erwünscht

## 2. Struktur von Quelldateien
### Organisation von Quelldateien
1. Package-Anweisung
2. Import-Anweisungen
3. Genau eine Top-Level-Klasse

### Regeln für Import-Anweisungen
- Keine Wildcard-Imports
- Statische Imports sind erlaubt
- Imports sind in einer bestimmten Reihenfolge organisiert:
  - Alle statischen Imports
  - Alle nicht-statischen Imports
  - Innerhalb jeder Gruppe sind die Imports alphabetisch sortiert

## 3. Formatierungsrichtlinien

### Einrückung und geschweifte Klammern
- Verwenden Sie 2 Leerzeichen für die Einrückung (keine Tabs)
- Geschweifte Klammern werden mit `if`, `else`, `for`, `do` und `while`-Anweisungen verwendet, selbst für einzeilige Blöcke
- K&R-Stil der Klammerplatzierung wird empfohlen
  ```java
  public void method() {
    if (condition) {
      // Code-Block
    }
  }
  ```

### Zeilenlänge und Umbruch
- Maximale Zeilenlänge beträgt 100 Zeichen
- Zeilenumbrüche sind bei höherem Syntax-Level zu bevorzugen
- Wenn Methodenaufrufketten umgebrochen werden, erfolgt der Umbruch vor dem `.`

## 4. Namenskonventionen

### Allgemeine Regeln
- **Packages**: Kleinbuchstaben, keine Unterstriche
- **Klassen**: UpperCamelCase
- **Methoden**: lowerCamelCase
- **Konstanten**: UPPER_SNAKE_CASE
- **Nicht-Konstante Felder**: lowerCamelCase
- **Parameter**: lowerCamelCase
- **Lokale Variablen**: lowerCamelCase

### Spezifische Namenspraktiken
- Vermeiden Sie Abkürzungen
- Ausnahmenamen müssen mit `Exception` enden
- Testklassen werden `TestClassName` genannt

## 5. Programmierpraktiken

### Java-Sprachregeln
- **Ausnahmen**:
  - Fangen Sie spezifische Exceptions
  - Vermeiden Sie leere Catch-Blöcke
  - Fügen Sie immer eine detaillierte Fehlermeldung hinzu
- **Final-Schlüsselwort**:
  - Verwenden Sie `final` für Methodenparameter
  - Bevorzugen Sie immutable Objects
- **Annotationen**:
  - `@Override` ist für überschreibende Methoden verpflichtend
  - Verwenden Sie Standard-Annotationen angemessen

### Codestruktur
- Bevorzugen Sie Komposition gegenüber Vererbung
- Halten Sie Methoden kurz und fokussiert
- Eine Anweisung pro Zeile
- Vermeiden Sie tiefe Verschachtelung von Bedingungen

## 6. Kommentare und Dokumentation

### Javadoc-Richtlinien
- Alle öffentlichen Klassen und Methoden müssen Javadoc haben
- Javadoc-Kommentare beginnen mit `/**`
- Fügen Sie Beschreibung, Parameter, Rückgabewerte und Ausnahmen ein
- Verwenden Sie `@param`, `@return`, `@throws` Tags

### Inline-Kommentare
- Verwenden Sie sie sparsam
- Erklären Sie das "Warum", nicht das "Was"
- Halten Sie Kommentare prägnant und aussagekräftig

## 7. Überlegungen zur Versionskontrolle
- Vermeiden Sie das Committen von auskommentiertem Code
- Verwenden Sie stattdessen Features des Versionskontrollsystems, um Änderungen zu verfolgen

## 8. Leistungsüberlegungen
- Bevorzugen Sie erweiterte `for`-Schleifen
- Verwenden Sie `StringBuilder` für String-Verkettung
- Schließen Sie Ressourcen mit try-with-resources
- Vermeiden Sie das Erstellen unnötiger Objekte

## 9. Testprinzipien
- Schreiben Sie Unit-Tests
- Streben Sie eine hohe Code-Abdeckung an
- Verwenden Sie JUnit für Tests
- Mocken Sie externe Abhängigkeiten
- Testen Sie Randfälle und Fehlerbedingungen

## 10. Zusätzliche Tools
- Google stellt einen Java-Formatter und statische Analysetools bereit
- CheckStyle und Error Prone können zur Durchsetzung von Stilrichtlinien verwendet werden

## Schlussfolgerung
Der Google Java Style Guide bietet einen umfassenden Satz von Richtlinien, um konsistenten, lesbaren und wartbaren Java-Code über Projekte hinweg sicherzustellen.