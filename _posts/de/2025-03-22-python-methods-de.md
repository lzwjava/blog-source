---
audio: false
generated: true
lang: de
layout: post
title: Python-Methoden
translated: true
type: note
---

Lassen Sie mich diesen Python-One-Liner Schritt für Schritt aufschlüsseln:

### Befehl:
```bash
python -c "from hcloud import Client; c = Client(token='fake'); print(dir(c.servers)); print('\nActions:'); print(dir(c.actions))"
```

### Erklärung:

1. **`python -c`**:
   - Dies weist den Python-Interpreter an, den nachfolgenden Code als Zeichenkette direkt von der Kommandozeile auszuführen, anstatt eine `.py`-Datei auszuführen.

2. **`from hcloud import Client`**:
   - Dies importiert die `Client`-Klasse aus dem `hcloud`-Modul. Die `hcloud`-Bibliothek ist das offizielle Python SDK für die Interaktion mit der Hetzner Cloud API (ein Cloud-Hosting-Anbieter). Es ermöglicht Ihnen, Server, Actions, Images usw. programmatisch zu verwalten.

3. **`c = Client(token='fake')`**:
   - Dies erzeugt eine Instanz der `Client`-Klasse und initialisiert sie mit einem API-Token. Hier ist `'fake'` ein Platzhalter-Token (kein echtes). In der Praxis würden Sie `'fake'` durch einen gültigen Hetzner Cloud API-Token ersetzen, um Anfragen an deren API zu authentifizieren.

4. **`print(dir(c.servers))`**:
   - `c.servers` ist ein Attribut des `Client`-Objekts, das Zugriff auf serverbezogene Funktionalität bietet (z.B. Erstellen, Löschen oder Auflisten von Servern).
   - `dir()` ist eine eingebaute Python-Funktion, die eine Liste aller Attribute und Methoden eines Objekts als Zeichenketten zurückgibt. Also listet `dir(c.servers)` alles auf, was Sie mit dem `servers`-Objekt tun können (z.B. Methoden wie `create`, `get_by_id` usw.).
   - Dies gibt die Liste auf der Konsole aus und zeigt, welche Operationen für die Serververwaltung verfügbar sind.

5. **`print('\nActions:')`**:
   - Dies gibt einen Zeilenumbruch (`\n`) gefolgt von der Zeichenkette `'Actions:'` aus, um die Ausgabe von `dir(c.servers)` vom nächsten Teil zur besseren Lesbarkeit zu trennen.

6. **`print(dir(c.actions))`**:
   - `c.actions` ist ein weiteres Attribut des `Client`-Objekts, das Zugriff auf aktionsbezogene Funktionalität bietet (z.B. Verfolgen des Status von Operationen wie dem Neustart eines Servers).
   - Ähnlich wie zuvor listet `dir(c.actions)` alle verfügbaren Attribute und Methoden des `actions`-Objekts auf.
   - Dies gibt die Liste auf der Konsole aus und zeigt, was Sie mit Actions tun können.

### Was macht es?
- Dieser Befehl ist im Wesentlichen eine schnelle Möglichkeit, die `servers`- und `actions`-Module der `hcloud`-Bibliothek zu inspizieren. Er gibt aus:
  1. Eine Liste aller verfügbaren Methoden und Attribute zur Serververwaltung (`c.servers`).
  2. Eine Liste aller verfügbaren Methoden und Attribute zur Action-Verwaltung (`c.actions`).

### Beispielausgabe:
Wenn Sie dies mit einem gültigen Token (und der installierten `hcloud`-Bibliothek) ausführen würden, könnte die Ausgabe vereinfacht so aussehen:
```
['create', 'delete', 'get_all', 'get_by_id', 'power_off', 'power_on', ...]
Actions:
['get_all', 'get_by_id', 'sort', ...]
- Die erste Zeile zeigt Methoden wie `create` oder `delete` für die Serververwaltung.
- Nach "Actions:" zeigt es Methoden wie `get_all` zum Abrufen von Action-Details.

### Voraussetzungen:
- Sie benötigen das `hcloud` Python-Paket installiert (`pip install hcloud`).
- Ein echter API-Token von Hetzner Cloud wäre für die tatsächliche Funktionalität erforderlich, aber dieser spezifische Befehl inspiziert nur die Bibliothek und führt keine API-Aufrufe durch.

### Zweck:
Dies wird wahrscheinlich für Debugging- oder Explorationszwecke verwendet, um zu sehen, welche Methoden in der `hcloud`-Bibliothek verfügbar sind, ohne die vollständige Dokumentation zu lesen.

Lassen Sie mich wissen, wenn Sie möchten, dass ich einen Teil näher untersuche!