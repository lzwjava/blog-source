---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Java-Programmierprüfung Lernleitfaden
translated: true
type: note
---

Hier ist ein praktischer, prüfungsorientierter Leitfaden für den **ersten Teil von „08553 Einführung in die Programmierung — Java“**, basierend auf dem *Lehrplan der Nationalen Hochschulselbststudiumsprüfung in China*. Er konzentriert sich auf Konzepte, Beispiele und Kernpunkte, die Einsteiger unbedingt beherrschen müssen.

---

## 1. Überblick über die Java-Sprache

### 1.1 Java-Merkmale

* **Plattformunabhängigkeit:** Java-Code wird in *Bytecode* kompiliert, der auf jedem Gerät mit einer *Java Virtual Machine (JVM)* läuft — „Write once, run anywhere.“
* **Objektorientiert:** Unterstützt *Verkapselung, Vererbung* und *Polymorphie*.
* **Sicher und robust:** Automatische Speicherverwaltung (Garbage Collection) und strenge Typüberprüfung reduzieren Fehler.
* **Multithreading:** Unterstützt die gleichzeitige Ausführung mehrerer Aufgaben.
* **Umfangreiche Standardbibliothek (API):** Enthält vorgefertigte Klassen für Mathematik, Strings, Dateien, Netzwerke usw.

### 1.2 Java-Versionen und Komponenten

* **JDK (Java Development Kit):** Für Entwickler — enthält Compiler (`javac`), JVM und Entwicklungswerkzeuge.
* **JRE (Java Runtime Environment):** Für Endbenutzer — enthält JVM + Kernbibliotheken.
* **API (Application Programming Interface):** Javas eingebaute Klassenbibliotheken, wie z.B. `java.lang`, `java.util`, `java.io` usw.

---

## 2. Java-Entwicklungswerkzeuge (IDE und CLI)

### 2.1 Gängige IDEs

Für die Prüfung reicht es, deren Zweck zu kennen:

* **Eclipse, IntelliJ IDEA, NetBeans:** Werden verwendet, um Java-Code einfach zu schreiben, zu kompilieren und auszuführen.

### 2.2 Kommandozeilen-Workflow

Typische Kompilierungs- und Ausführungsschritte:

1. **Schreibe** deinen Code in eine `.java`-Datei, z.B. `Hello.java`
2. **Kompiliere** sie:

   ```bash
   javac Hello.java
   ```

   → Erzeugt `Hello.class` (Bytecode-Datei)
3. **Führe** sie aus:

   ```bash
   java Hello
   ```

   (Keine `.class`-Erweiterung beim Ausführen)

### 2.3 Einfaches Beispiel

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, Java!");
    }
}
```

---

## 3. Richtlinien für den Programmierstil

### 3.1 Namenskonventionen

* **Klassen:** `CamelCase`, erster Buchstabe groß → `StudentInfo`
* **Variablen & Methoden:** `camelCase`, beginnen klein → `studentName`, `calculateScore()`
* **Konstanten:** Nur Großbuchstaben mit Unterstrichen → `MAX_SIZE`

### 3.2 Einrückung und Kommentare

* Verwende **konsistente Einrückung** (typischerweise 4 Leerzeichen).
* Schreibe klare **Kommentare**:

  ```java
  // Dies ist ein einzeiliger Kommentar
  /* Dies ist ein mehrzeiliger Kommentar */
  ```

### 3.3 Codestruktur

Folge einer logischen Gruppierung und Lesbarkeit:

* Jede Datei enthält **eine öffentliche Klasse** mit dem **gleichen Namen** wie die Datei.
* Halte Zeilen kurz und aussagekräftig; eine Anweisung pro Zeile.

---

## 4. Häufige Programmierfehler und Debugging-Grundlagen

### 4.1 Syntaxfehler

Werden vom Compiler erkannt:

* Fehlendes Semikolon `;`
* Nicht übereinstimmende geschweifte Klammern `{ }`
* Falsche Groß-/Kleinschreibung (Java unterscheidet zwischen **Groß- und Kleinschreibung**)

  ```java
  System.out.println("Hi"); // korrekt
  system.out.println("Hi"); // Fehler
  ```

### 4.2 Laufzeitfehler

Treten während der Programmausführung auf:

* Division durch Null
* Array-Index außerhalb der Grenzen
* Null-Zeiger-Ausnahmen (Null Pointer Exceptions)

### 4.3 Logikfehler

Das Programm läuft, liefert aber eine falsche Ausgabe.
→ Verwende **Ausgabeanweisungen** oder **Debugger-Tools** in IDEs, um Variablenwerte schrittweise zu verfolgen.

---

## 5. Kernpunkte für die Prüfung

* Verstehe die **Rollen und Unterschiede von JDK, JRE, JVM**.
* Wisse, wie man Java **sowohl von der IDE als auch von der Kommandozeile aus kompiliert und ausführt**.
* Merke dir die **grundlegenden Syntaxregeln** und **Stilstandards**.
* Sei in der Lage, **häufige Fehler zu identifizieren** und ihre Ursachen zu erklären.
* Übe das Schreiben kleiner Programme, die:

  * Nachrichten ausgeben
  * Variablen und Ausdrücke verwenden
  * Der korrekten Struktur und Namensgebung folgen

---

## 6. Beispiel einer Prüfungsfrage

**Beispiel 1:**

> Welche der folgenden Aussagen über Java ist *falsch*?
> A. Java unterstützt Plattformunabhängigkeit durch Bytecode
> B. Java-Programme müssen immer in nativen Maschinencode kompiliert werden
> C. Die JVM führt kompilierten Bytecode aus
> D. Java-Programme können auf jedem System mit installierter JVM ausgeführt werden

**Antwort:** B

**Beispiel 2:**

> Welcher Befehl kompiliert eine Java-Quelldatei namens `Test.java`?
> A. java Test
> B. javac Test.java
> C. run Test
> D. compile Test

**Antwort:** B

---

Möchtest du, dass ich mit **Teil II: Grundlegende Syntax und Datentypen** fortfahre (dem nächsten Hauptabschnitt in diesem Kurs)? Er wird der gleichen klaren, prüfungsorientierten Struktur folgen.