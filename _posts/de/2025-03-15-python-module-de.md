---
audio: false
generated: true
lang: de
layout: post
title: Wie Module in Python funktionieren
translated: true
type: note
---

In Python ist ein **Modul** eine Datei mit Python-Code – wie Funktionen, Klassen und Variablen –, den Sie in anderen Python-Skripten importieren und verwenden können. Module sind eine grundlegende Funktion von Python, die Ihnen hilft, Ihren Code zu organisieren, Wiederverwendung zu fördern und Wiederholungen zu vermeiden. Lassen Sie uns untersuchen, wie sie funktionieren und wie Sie andere Python-Dateien oder Module in Ihren Projekten verwenden können.

---

#### Was ist ein Modul?
Ein Modul ist einfach eine `.py`-Datei mit Python-Code. Wenn Sie ein Modul in ein anderes Skript importieren, führt Python den Code in dieser Datei aus und macht dessen Inhalte (Funktionen, Klassen, Variablen usw.) für Sie nutzbar. Python wird mit einer umfangreichen Standardbibliothek von eingebauten Modulen (z. B. `math`, `os`, `sys`) geliefert, und Sie können auch Ihre eigenen benutzerdefinierten Module erstellen.

Zum Beispiel, wenn Sie eine Datei namens `greetings.py` mit folgendem Code haben:
```python
def say_hello(name):
    print(f"Hello, {name}!")
```
Diese Datei ist ein Modul namens `greetings`. Sie können es in ein anderes Skript importieren, um die Funktion `say_hello` zu verwenden.

---

#### Wie man andere Python-Dateien oder Module verwendet
Um Code aus einer anderen Python-Datei (Modul) zu verwenden, verwenden Sie die `import`-Anweisung. So funktioniert es Schritt für Schritt:

1. **Grundlegendes Importieren**
   - Wenn sich das Modul im selben Verzeichnis wie Ihr Skript befindet, können Sie es anhand seines Namens (ohne die `.py`-Endung) importieren.
   - Beispiel: In einer Datei namens `main.py` können Sie schreiben:
     ```python
     import greetings
     greetings.say_hello("Alice")
     ```
   - Das Ausführen von `main.py` gibt aus: `Hello, Alice!`
   - Verwenden Sie die Punktnotation (`module_name.item_name`), um auf die Inhalte des Moduls zuzugreifen.

2. **Importieren spezifischer Elemente**
   - Wenn Sie nur bestimmte Funktionen oder Variablen aus einem Modul benötigen, verwenden Sie die Syntax `from ... import ...`.
   - Beispiel:
     ```python
     from greetings import say_hello
     say_hello("Bob")
     ```
   - Dies gibt aus: `Hello, Bob!`
   - Jetzt können Sie `say_hello` direkt verwenden, ohne es mit dem Modulnamen zu prefixen.

3. **Importieren mit Aliasnamen**
   - Sie können einem Modul zur Bequemlichkeit mit `as` einen kürzeren Namen (Alias) geben.
   - Beispiel:
     ```python
     import greetings as g
     g.say_hello("Charlie")
     ```
   - Ausgabe: `Hello, Charlie!`

4. **Alles importieren**
   - Sie können alle Inhalte eines Moduls mit `from module_name import *` importieren, aber dies wird generell nicht empfohlen, da es Ihren Namensraum überladen und Namenskonflikte verursachen kann.
   - Beispiel:
     ```python
     from greetings import *
     say_hello("Dana")
     ```
   - Ausgabe: `Hello, Dana!`

---

#### Wo sucht Python nach Modulen?
Python sucht in einer Liste von Verzeichnissen nach Modulen, die in `sys.path` definiert ist. Dazu gehören:
- Das Verzeichnis des Skripts, das Sie ausführen (aktuelles Verzeichnis).
- Die in der Umgebungsvariable `PYTHONPATH` aufgeführten Verzeichnisse (falls gesetzt).
- Standardorte, an denen die Standardbibliothek von Python installiert ist.

Wenn sich Ihr Modul in einem anderen Verzeichnis befindet, können Sie:
- Es in dasselbe Verzeichnis wie Ihr Skript verschieben.
- Sein Verzeichnis programmgesteuert zu `sys.path` hinzufügen:
  ```python
  import sys
  sys.path.append('/pfad/zum/verzeichnis')
  import mymodule
  ```

---

#### Eingebaute Module
Die Standardbibliothek von Python bietet viele nützliche Module, die Sie importieren können, ohne sie selbst zu erstellen. Zum Beispiel:
- `import math` ermöglicht Ihnen die Verwendung von `math.sqrt(16)` (gibt `4.0` zurück) oder `math.pi` (gibt `3.14159...` zurück).
- `import os` bietet Funktionen zur Interaktion mit dem Betriebssystem.

---

#### Pakete
Ein **Paket** ist ein Verzeichnis, das mehrere Module und eine spezielle `__init__.py`-Datei (die leer sein kann) enthält. Zum Beispiel, wenn Sie haben:
```
mypackage/
    __init__.py
    greetings.py
```
Sie können das `greetings`-Modul wie folgt importieren:
```python
import mypackage.greetings
mypackage.greetings.say_hello("Eve")
```
Oder:
```python
from mypackage.greetings import say_hello
say_hello("Eve")
```

---

#### Wie Module ausgeführt werden
Wenn Sie ein Modul importieren, führt Python den gesamten Code in diesem Modul einmal aus und cached ihn. Nachfolgende Importe verwenden die gecachte Version. Wenn ein Modul Code auf oberster Ebene enthält (z. B. eine `print`-Anweisung), wird dieser während des Imports ausgeführt. Zum Beispiel:
```python
# mymodule.py
print("Module is being imported!")
def my_function():
    print("Function called!")
```
```python
# main.py
import mymodule
```
Das Ausführen von `main.py` gibt aus: `Module is being imported!`

Um Code einzubinden, der nur ausgeführt wird, wenn das Modul direkt ausgeführt wird (nicht importiert), verwenden Sie:
```python
if __name__ == "__main__":
    print("This runs only if the module is run directly!")
```
Dies ist nützlich für Tests oder zum Definieren eines Haupt-Einstiegspunkts für das Modul.

---

#### Beispiel
Hier ist ein vollständiges Beispiel:
1. Erstellen Sie `math_utils.py`:
   ```python
   def add(a, b):
       return a + b
   ```
2. Erstellen Sie `main.py` im selben Verzeichnis:
   ```python
   import math_utils
   result = math_utils.add(3, 4)
   print(result)  # Gibt aus: 7
   ```
3. Alternativ:
   ```python
   from math_utils import add
   print(add(3, 4))  # Gibt aus: 7
   ```

---

#### Wichtige Erkenntnisse
- Module sind Python-Dateien, die Sie importieren können, um Code wiederzuverwenden.
- Verwenden Sie `import module_name`, um mit Punktnotation auf Inhalte zuzugreifen, oder `from module_name import item` für direkten Zugriff.
- Module können benutzerdefinierte Dateien, eingebaute Bibliotheksmodule oder Teil von Paketen sein.
- Python findet Module mithilfe von `sys.path`, und Sie können größere Projekte mit Paketen organisieren.

Dies behandelt die Grundlagen, wie Module in Python funktionieren und wie Sie andere Python-Dateien oder Module in Ihren Skripten verwenden können!