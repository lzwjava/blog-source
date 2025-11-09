---
audio: false
date: 2025-09-11
generated: true
image: false
lang: de
layout: post
model: mistralai/mistral-medium-3.1
title: Grenzen von LLMs in komplexen Arbeitsabläufen
translated: true
type: note
---

Du hast absolut recht! LLMs (einschließlich mir) glänzen bei **kleinen, fokussierten Aufgaben** – wie das Erklären eines einzelnen Konzepts, das Erstellen eines kurzen Code-Snippets oder das Debuggen eines spezifischen Fehlers – aber sie scheitern bei **komplexen, mehrstufigen Workflows**, die Folgendes beinhalten:

1. **Mehrere miteinander verbundene Konfigurationen** (z. B. Maven `pom.xml`-Dateien, Jacoco-Agent-Argumente, Python-Test-Integration).
2. **Zustandsbehaftete Abhängigkeiten** (z. B. "Zuerst `module-A/pom.xml` aktualisieren, dann `mvn test` mit diesen Flags ausführen, dann Berichte zusammenführen").
3. **Systemübergreifende Interaktionen** (z. B. Java + Python + CI-Tools wie Jenkins/GitHub Actions).
4. **Kontextwechsel** (z. B. "Vergiss jetzt den Java-Teil – wie parsen wir das Jacoco-XML in Python?").

---

### **Warum LLMs bei komplexen Workflows scheitern**
1. **Kein persistenter Speicher**: Wir "erinnern" uns nicht an vergangene Schritte, es sei denn, du erinnerst uns explizit daran (und selbst dann sind Kontextfenster begrenzt).
2. **Lineares Denken**: Wir generieren Antworten Schritt für Schritt, können aber Abhängigkeiten nicht dynamisch verfolgen (z. B. "Hast du `mvn clean` vor dem Agenten ausgeführt?").
3. **Überoptimierung für einzelne Antworten**: Wir sind darauf trainiert, *eine* vollständige Antwort zu geben, keine iterative Anleitung.
4. **Keine Ausführungsumgebung**: Wir können keine Befehle ausführen, um zu überprüfen, ob `jacoco:prepare-agent` in deinem Setup tatsächlich funktioniert hat.

---

### **Besserer Ansatz: 'Teile und verifiziere'**
Für Probleme wie **Jacoco + Multi-Module-Maven + Python-Tests** unterteile sie in **atomare Schritte** und verifiziere jeden einzelnen. Beispiel:

#### **Schritt 1: Jacoco-Agent-Setup überprüfen (Java-Seite)**
```bash
# In EINEM Modul (z. B. module-A):
mvn clean test -Pcoverage
```
- **Prüfung**: Existiert `target/site/jacoco/index.html`?
- **Debuggen**: Wenn nicht, teile den `pom.xml`-Ausschnitt für Jacoco und das Fehlerprotokoll mit.

#### **Schritt 2: Kombinierten Bericht generieren (Multi-Module)**
```bash
mvn jacoco:report-aggregate
```
- **Prüfung**: Wurde `target/site/jacoco-aggregate/index.html` erstellt?
- **Debuggen**: Wenn fehlend, überprüfe die `<module>`-Pfade in der Eltern-`pom.xml`.

#### **Schritt 3: Export für Python (XML/CSV)**
```bash
# Jacoco-Binärdatei in XML konvertieren
java -jar jacoco-cli.jar report jacoco.exec --xml output.xml
```
- **Prüfung**: Enthält `output.xml` `<package>`-Tags?
- **Debuggen**: Wenn leer, stelle sicher, dass die Tests mit dem Agenten liefen (`-javaagent:jacocoagent.jar`).

#### **Schritt 4: Python-Integration**
```python
import xml.etree.ElementTree as ET
tree = ET.parse("output.xml")
coverage = tree.find(".//counter[@type='LINE'][@covered]")
print(f"Covered lines: {coverage.get('covered')}/{coverage.get('missed')}")
```
- **Prüfung**: Gibt das Skript die erwarteten Zahlen aus?
- **Debuggen**: Wenn nicht, teile die XML-Struktur und den Python-Fehler mit.

---

### **Wie man effektiv mit LLMs arbeitet**
1. **Isoliere das Problem**:
   - *"Hier ist meine `pom.xml` für module-A. Warum fügt `jacoco:prepare-agent` das VM-Arg nicht hinzu?"*
   - *(Besser als: "Hilf mir, Jacoco für 5 Module + Python einzurichten.")*

2. **Teile minimalen, reproduzierbaren Kontext**:
   - Fehlerprotokolle, Konfigurationssnippets (nicht ganze Dateien) und **was du versucht hast**.

3. **Iteratives Debugging**:
   - **Du**: "Schritt 1 ist mit `No tests run` fehlgeschlagen. Hier ist das Protokoll."
   - **LLM**: "Füge `<test>`-Goals zu deinem `maven-surefire-plugin` hinzu."
   - **Du**: "Jetzt funktioniert Schritt 2, aber der Bericht ist leer..."

4. **Nutze uns für 'Mikro-Aufgaben'**:
   - *"Schreibe ein Python-Skript, das Jacoco-XML parst und fehlschlägt, wenn die Coverage < 80% ist."*
   - *"Erkläre das `<execution>`-Tag in Maven für Jacoco."*

---

### **Tools zur Automatisierung komplexer Workflows**
Da LLMs keinen Zustand verwalten können, verwende:
- **Shell-Skripte** (z. B. `setup_coverage.sh`, um Maven/Python-Befehle zu verketten).
- **Makefiles** (definiere `make test-coverage`, um alle Schritte auszuführen).
- **CI-Vorlagen** (GitHub Actions/Jenkins-Pipelines mit expliziten Schritten).
- **Docker** (containerisiere die Umgebung, um "works on my machine"-Probleme zu vermeiden).

---
### **Wichtigste Erkenntnis**
**LLMs sind wie eine hochgezüchtete `man`-Page oder Stack Overflow auf Steroiden** – großartig für **einzelne Bausteine**, aber nicht für die Orchestrierung ganzer Systeme. Für komplexe Aufgaben:
1. **Zerlege sie**.
2. **Verifiziere jeden Schritt**.
3. **Stelle gezielte Fragen**.

Möchtest du, dass ich tiefer in einen der oben genannten Schritte eintauchte (z. B. Jacoco-XML-Parsing in Python oder Multi-Module-Maven-Setups)?