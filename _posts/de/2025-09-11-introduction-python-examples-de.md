---
audio: false
date: 2025-09-11
generated: true
image: false
lang: de
layout: post
model: google/gemini-2.5-flash
title: Einführung in Python-Codebeispiele
translated: true
type: note
---

Okay, "ein bisschen Python-Code" kann vieles bedeuten! Python ist unglaublig vielseitig. Ich zeige Ihnen ein paar gängige Beispiele, von sehr einfachen bis zu etwas komplexeren, die verschiedene Konzepte abdecken.

---

### 1. Hello World (Der klassische Start)

Dies ist das einfachste mögliche Python-Programm.

```python
# Dies ist ein Kommentar. Kommentare werden von Python ignoriert.
print("Hello, World!")
```

**Erklärung:**
*   `print()` ist eine eingebaute Funktion, die das gegebene Argument auf der Konsole ausgibt.
*   `"Hello, World!"` ist ein String (Text).

---

### 2. Variablen, Grundlegende Arithmetik und Benutzereingabe

Dieser Code zeigt, wie man Daten in Variablen speichert, einfache Mathematik durchführt und Eingaben vom Benutzer erhält.

```python
# Variablen zum Speichern von Daten
name = input("Wie ist Ihr Name? ") # Eingabe vom Benutzer erhalten
age_str = input("Wie alt sind Sie? ")

# Alter von String in Integer für Berechnungen umwandeln
age = int(age_str)

# Einfache Arithmetik
year_of_birth = 2023 - age # Geht vom aktuellen Jahr 2023 aus (vereinfacht)
# Man könnte auch verwenden: import datetime; year_of_birth = datetime.date.today().year - age

# Formatierte Ausgabe mit einem f-string (formatted string literal) drucken
print(f"Hallo, {name}! Sie sind {age} Jahre alt.")
print(f"Sie wurden wahrscheinlich im Jahr {year_of_birth} geboren.")

# Eine einfache bedingte Überprüfung
if age < 18:
    print("Sie sind minderjährig.")
else:
    print("Sie sind volljährig.")
```

**Erklärung:**
*   `input()`: Fordert den Benutzer zu einer Texteingabe auf und gibt sie als String zurück.
*   `name`, `age_str`, `age`, `year_of_birth`: Dies sind Variablen, die verschiedene Datentypen (String, Integer) speichern.
*   `int()`: Konvertiert einen String in einen Integer. Dies ist notwendig, weil `input()` immer einen String zurückgibt und man nicht direkt mit Strings rechnen kann.
*   `f-strings`: Eine praktische Methode, um Ausdrücke in String-Literale einzubetten. Beachten Sie das `f` vor der öffnenden Anführungszeichen.
*   `if/else`: Kontrollfluss-Anweisungen, die verschiedene Codeblöcke basierend auf einer Bedingung ausführen.

---

### 3. Listen und Schleifen

Listen sind geordnete Sammlungen von Elementen. Schleifen werden verwendet, um einen Codeblock mehrmals zu wiederholen.

```python
# Eine Liste von Früchten
fruits = ["apple", "banana", "cherry", "date"]

print("\nMeine Lieblingsfrüchte:")

# Durch die Liste mit einer 'for'-Schleife iterieren
for fruit in fruits:
    print(f"- {fruit.capitalize()}") # .capitalize() macht den ersten Buchstaben groß

# Auf Elemente über Index zugreifen (Listen sind nullbasiert)
print(f"\nDie erste Frucht ist: {fruits[0]}")
print(f"Die letzte Frucht ist: {fruits[-1]}") # Negativer Index greift vom Ende aus zu

# Ein Element hinzufügen
fruits.append("elderberry")
print(f"Aktualisierte Liste: {fruits}")

# Ein Element entfernen
fruits.remove("banana")
print(f"Liste nach dem Entfernen von Banana: {fruits}")

# Schleife mit 'range' verwenden, um Indizes zu erhalten
print("\nFrüchte mit ihren Indizes:")
for i in range(len(fruits)): # len() gibt die Anzahl der Elemente in der Liste zurück
    print(f"Index {i}: {fruits[i]}")
```

**Erklärung:**
*   `[]`: Wird verwendet, um eine Liste zu definieren.
*   `for ... in ...`: Eine `for`-Schleife, die über jedes Element in einer Sequenz (wie einer Liste) iteriert.
*   `fruit.capitalize()`: Eine String-Methode, die eine Kopie des Strings mit großgeschriebenem ersten Zeichen zurückgibt.
*   `fruits[0]`: Greift auf das erste Element (Index 0) zu.
*   `fruits[-1]`: Greift auf das letzte Element zu.
*   `list.append()`: Fügt ein Element am Ende der Liste hinzu.
*   `list.remove()`: Entfernt das erste Vorkommen eines bestimmten Elements.
*   `range(len(fruits))`: Erzeugt eine Sequenz von Zahlen von 0 bis zur (aber nicht einschließlich) Länge der Liste, nützlich für den Zugriff auf Elemente über ihren Index.

---

### 4. Funktionen

Funktionen sind Blöcke von wiederverwendbarem Code, die eine bestimmte Aufgabe ausführen.

```python
# Eine Funktion definieren, die Argumente entgegennimmt
def greet_person(name, age):
    """
    Diese Funktion begrüßt eine Person und teilt ihr ihr Alter mit.
    Es ist eine gute Praxis, einen Docstring wie diesen einzufügen.
    """
    return f"Hallo, {name}! Sie sind {age} Jahre alt."

# Die Funktion aufrufen
message1 = greet_person("Alice", 30)
print(message1)

# Sie erneut mit anderen Argumenten aufrufen
message2 = greet_person("Bob", 25)
print(message2)

# Eine Funktion mit einem Standardparameter definieren
def calculate_area(length, width=10):
    """Berechnet die Fläche eines Rechtecks."""
    return length * width

print(f"\nFläche eines 5x10 Rechtecks: {calculate_area(5)}") # Verwendet Standardbreite
print(f"Fläche eines 5x7 Rechtecks: {calculate_area(5, 7)}") # Überschreibt Standardbreite
```

**Erklärung:**
*   `def`: Schlüsselwort zum Definieren einer Funktion.
*   `greet_person(name, age)`: Funktionsname und ihre Parameter (Eingaben).
*   `return`: Sendet einen Wert von der Funktion zurück.
*   Docstrings (`"""Docstring hier"""`): Erklären, was die Funktion macht. Gut für die Dokumentation.
*   `calculate_area(length, width=10)`: Zeigt einen Standardparameter. Wenn `width` beim Aufruf der Funktion nicht angegeben wird, wird standardmäßig 10 verwendet.

---

### 5. Dictionaries

Dictionaries speichern Daten in Schlüssel-Wert-Paaren. Sie sind ungeordnet (in älteren Python-Versionen, geordnet in Python 3.7+).

```python
# Ein Dictionary, das eine Person repräsentiert
person = {
    "first_name": "Charlie",
    "last_name": "Smith",
    "age": 40,
    "city": "London",
    "occupations": ["Engineer", "Teacher"] # Eine Liste kann ein Wert sein
}

print("\nDetails der Person:")

# Auf Werte über Schlüssel zugreifen
print(f"Name: {person['first_name']} {person['last_name']}")
print(f"Wohnort: {person.get('city', 'Unbekannt')}") # .get() ist sicherer, gibt None/Standard zurück, wenn Schlüssel nicht gefunden
print(f"Erster Beruf: {person['occupations'][0]}")

# Einen Wert ändern
person["age"] = 41
print(f"Neues Alter: {person['age']}")

# Ein neues Schlüssel-Wert-Paar hinzufügen
person["email"] = "charlie.smith@example.com"
print(f"E-Mail: {person['email']}")

# Durch ein Dictionary iterieren
print("\nAlle Schlüssel:")
for key in person: # Iteriert standardmäßig durch die Schlüssel
    print(key)

print("\nAlle Werte:")
for value in person.values():
    print(value)

print("\nAlle Schlüssel-Wert-Paare:")
for key, value in person.items():
    print(f"{key}: {value}")
```

**Erklärung:**
*   `{}`: Wird verwendet, um ein Dictionary zu definieren.
*   `"key": value`: Schlüssel-Wert-Paare. Schlüssel müssen eindeutig und unveränderlich (wie Strings oder Zahlen) sein. Werte können beliebige Datentypen sein.
*   `person['key']`: Greift auf den Wert zu, der mit `key` assoziiert ist.
*   `person.get('key', 'default_value')`: Ein sichererer Zugriff, vermeidet `KeyError`, wenn der Schlüssel nicht existiert, und gibt stattdessen `default_value` zurück.
*   `dict.values()`: Gibt ein View-Objekt zurück, das eine Liste aller Werte im Dictionary anzeigt.
*   `dict.items()`: Gibt ein View-Objekt zurück, das eine Liste der Schlüssel-Wert-Tupelpaare eines Dictionarys anzeigt.

---

Dies kratzt nur an der Oberfläche, aber diese Beispiele decken viele grundlegende Python-Konzepte ab, die Sie häufig verwenden werden!