---
audio: false
generated: true
lang: de
layout: post
title: Oracle-Code-Konventionen für die Programmiersprache Java
translated: true
type: note
---

## 1. Dateiorganisation

### 1.1 Dateinamen
- Quelldateien müssen die Erweiterung `.java` haben
- Quelldateinamen müssen exakt mit dem Namen der öffentlichen Klasse in der Datei übereinstimmen
- Beispiele:
  - `MyClass.java` enthält eine öffentliche Klasse namens `MyClass`
  - `CircleShape.java` enthält eine öffentliche Klasse namens `CircleShape`

### 1.2 Dateistruktur
1. Kopfkommentare
2. Package-Anweisung
3. Import-Anweisungen
4. Klassen- und Interface-Deklarationen

## 2. Formatierung und Einrückung

### 2.1 Einrückung
- Verwenden Sie 4 Leerzeichen für die Einrückung (keine Tabs)
- Rücken Sie Fortsetzungszeilen um 8 Leerzeichen ein
- Geschweifte Klammern sollten vertikal ausgerichtet sein

### 2.2 Zeilenlänge
- Die empfohlene maximale Zeilenlänge beträgt 80 Zeichen
- Brechen Sie lange Anweisungen auf einer höheren logischen Ebene um

### 2.3 Zeilenumbruch
- Brechen Sie die Zeile vor einem Operator um
- Richten Sie die neue Zeile mit dem Anfang des Ausdrucks auf derselben Ebene aus

## 3. Kommentare

### 3.1 Dateikommentare
- Jede Quelldatei sollte mit einem Kommentarblock beginnen:
  ```java
  /*
   * Klassenname
   * 
   * Versionsinformation
   * 
   * Datum
   * 
   * Copyright-Hinweis
   */
  ```

### 3.2 Implementierungskommentare
- Verwenden Sie `/* */` für mehrzeilige Kommentare
- Verwenden Sie `//` für einzeilige Kommentare
- Kommentare sollten das "Warum" erklären, nicht das "Was"

### 3.3 Dokumentationskommentare
- Verwenden Sie Javadoc-Kommentare für Klassen, Interfaces und Methoden
- Enthalten Sie:
  - Kurzbeschreibung
  - `@param` für Methodenparameter
  - `@return` für Rückgabewerte
  - `@throws` für Ausnahmen

## 4. Deklarationen

### 4.1 Anzahl pro Zeile
- Eine Deklaration pro Zeile
- Empfohlen:
  ```java
  int level;        // Korrekt
  int size;         // Korrekt
  
  // Vermeiden:
  int level, size;  // Nicht empfohlen
  ```

### 4.2 Initialisierung
- Initialisieren Sie Variablen nach Möglichkeit bei der Deklaration
- Gruppieren Sie zusammengehörige Deklarationen

## 5. Anweisungen

### 5.1 Einfache Anweisungen
- Eine Anweisung pro Zeile
- Verwenden Sie ein Leerzeichen nach Kommas
- Verwenden Sie Leerzeichen um Operatoren

### 5.2 Zusammengesetzte Anweisungen
- Geschweifte Klammern werden bei `if`, `else`, `for`, `while`, `do`-Anweisungen verwendet, auch für einzeilige Blöcke

### 5.3 Return-Anweisungen
- Bevorzugen Sie explizites Return
- Vermeiden Sie unnötiges `else` nach `return`

## 6. Namenskonventionen

### 6.1 Package-Namen
- Nur Kleinbuchstaben
- Eindeutiges Präfix, oft umgekehrte Unternehmensdomain
- Beispiel: `com.company.project`

### 6.2 Klassen-Namen
- UpperCamelCase
- Substantiv oder Substantivgruppe
- Beispiele: `DataProcessor`, `HttpClient`

### 6.3 Interface-Namen
- Ähnlich wie Klassen-Namen
- Sollte Verhalten beschreiben
- Beispiele: `Runnable`, `Serializable`

### 6.4 Methoden-Namen
- lowerCamelCase
- Verb oder Verbgruppe
- Beispiele: `calculateTotal()`, `sendMessage()`

### 6.5 Variablen-Namen
- lowerCamelCase
- Aussagekräftig und beschreibend
- Vermeiden Sie Einzelbuchstaben-Namen, außer für temporäre Variablen

### 6.6 Konstanten-Namen
- ALL_GROSSBUCHSTABEN mit Unterstrichen
- Beispiel: `MAX_VALUE`, `COLOR_RED`

## 7. Programmierpraktiken

### 7.1 Sichtbarkeit
- Verwenden Sie die niedrigstmögliche Sichtbarkeit
- Bevorzugen Sie `private` gegenüber `public`
- Verwenden Sie Zugriffsmethoden für Klassenfelder

### 7.2 Variablenbereich
- Deklarieren Sie Variablen im kleinstmöglichen Bereich
- Initialisieren Sie Variablen nahe ihrer ersten Verwendung

### 7.3 Ausnahmebehandlung
- Schließen Sie immer eine Nachricht in Ausnahmen ein
- Fangen Sie spezifische Ausnahmen ab
- Verwenden Sie try-catch-finally angemessen

## 8. Best Practices

### 8.1 Vermeiden von Magic Numbers
- Verwenden Sie benannte Konstanten anstelle von Literalzahlen
- Verbessert die Lesbarkeit und Wartbarkeit des Codes

### 8.2 Bevorzugung von Unveränderlichkeit
- Verwenden Sie `final` für Variablen, die sich nicht ändern
- Erstellen Sie nach Möglichkeit unveränderliche Klassen

## Fazit
Diese Konventionen zielen darauf ab, die Lesbarkeit, Wartbarkeit und Konsistenz von Java-Projekten zu verbessern.