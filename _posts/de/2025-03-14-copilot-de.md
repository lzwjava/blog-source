---
audio: false
generated: true
lang: de
layout: post
title: Verwenden von GitHub Copilot in Visual Studio Code
translated: true
type: note
---

Um GitHub Copilot in Visual Studio Code (VSCode) zu verwenden, befolgen Sie diese Schritte:

### 1. Installieren Sie die Copilot-Erweiterung
- Öffnen Sie VSCode auf Ihrem Computer.
- Navigieren Sie zur **Erweiterungsansicht**:
  - Klicken Sie auf das Erweiterungssymbol in der Aktivitätsleiste auf der linken Seite des Fensters, oder
  - Drücken Sie `Strg+Umschalt+X` (oder `Cmd+Umschalt+X` auf macOS).
- Geben Sie in die Suchleiste **"GitHub Copilot"** ein.
- Suchen Sie die offizielle **GitHub Copilot**-Erweiterung in den Ergebnissen und klicken Sie auf **Installieren**.

### 2. Melden Sie sich bei GitHub an
- Nach der Installation der Erweiterung müssen Sie sich mit Ihrem GitHub-Konto authentifizieren, da Copilot ein GitHub-Produkt ist.
- Möglicherweise werden Sie nach der Installation automatisch zur Anmeldung aufgefordert. Falls nicht:
  - Öffnen Sie die **Befehlspalette** durch Drücken von `Strg+Umschalt+P` (oder `Cmd+Umschalt+P` auf macOS).
  - Geben Sie **"GitHub Copilot: Sign in"** ein und wählen Sie es aus.
- Befolgen Sie die Anweisungen auf dem Bildschirm, um sich bei Ihrem GitHub-Konto anzumelden. Dies kann die Autorisierung von VSCode über ein Browserfenster beinhalten.

### 3. Beginnen Sie mit der Verwendung von Copilot
- Sobald Sie angemeldet sind, wird Copilot aktiviert und beginnt Ihnen beim Programmieren zu helfen.
- **Code-Vorschläge**: Während Sie tippen, schlägt Copilot Code-Vervollständigungen oder ganze Zeilen vor. Um einen Vorschlag zu akzeptieren, drücken Sie die `Tab`-Taste.
- **Inline-Chat**: Für zusätzliche Hilfe, wie das Stellen von Fragen zu Ihrem Code oder das Anfordern spezifischer Programmierhilfe:
  - Drücken Sie `Strg+I`, um das Inline-Chat-Feature direkt in Ihrem Editor zu öffnen.
  - Geben Sie Ihre Frage oder Anfrage ein, und Copilot wird mit Vorschlägen oder Erklärungen antworten.

### Zusätzliche Tipps
- Copilot funktioniert am besten, wenn Sie klaren Kontext in Ihrem Code bieten (z. B. Kommentare oder Funktionsnamen).
- Um mehr Funktionen zu erkunden oder Ihre Nutzung zu verfeinern, sehen Sie sich die offizielle **GitHub Copilot-Dokumentation** oder Online-Tutorials für detaillierte Anleitungen und Beispiele an.

Das war's! Mit diesen Schritten programmieren Sie im Handumdrehen mit KI-gestützter Hilfe in VSCode.

---

Um detaillierter zu erklären, wie GitHub Copilot in Visual Studio Code (VSCode) funktioniert, lassen Sie uns seine Funktionalität, die Integration in Ihren Programmierprozess und die zugrunde liegende Technologie aufschlüsseln. Copilot ist ein KI-gestütztes Tool, das Entwickler unterstützt, indem es Code-Vorschläge generiert und interaktive Hilfe bietet, um das Programmieren schneller und effizienter zu machen. Im Folgenden werde ich seine Schlüsselmechanismen und Funktionen im Detail erläutern.

---

### **1. Integration in VSCode**
GitHub Copilot operiert als Erweiterung innerhalb von VSCode, einem der beliebtesten Code-Editoren. So wird es eingerichtet und beginnt zu arbeiten:

- **Installation**: Sie installieren die GitHub Copilot-Erweiterung aus dem VSCode Marketplace und melden sich mit Ihrem GitHub-Konto an. Je nach Nutzung kann ein Abonnement (privat oder geschäftlich) erforderlich sein.
- **Echtzeit-Aktivierung**: Nach der Installation beginnt Copilot automatisch zu arbeiten, sobald Sie tippen. Es integriert sich nahtlos in den Editor und erscheint als Teil Ihres natürlichen Workflows, ohne dass für grundlegende Vorschläge eine manuelle Aktivierung erforderlich ist.

---

### **2. Wie Copilot Code-Vorschläge generiert**
Die Kernfunktionalität von Copilot ist seine Fähigkeit, Code basierend auf dem, was Sie schreiben, vorherzusagen und vorzuschlagen. So funktioniert es:

- **AI-Modell**: Copilot wird von **OpenAI's Codex** angetrieben, einem Machine-Learning-Modell, das auf einem riesigen Datensatz mit öffentlichem Code aus GitHub-Repositories, Dokumentation und anderen Quellen trainiert wurde. Codex ist eine spezialisierte Version von Modellen wie GPT-3, die für Programmieraufgaben feinabgestimmt ist.
- **Kontextanalyse**: Während Sie tippen, untersucht Copilot den Kontext Ihres Codes, einschließlich:
  - Der Programmiersprache (z. B. Python, JavaScript, Java).
  - Dem Inhalt der aktuellen Datei, wie bestehende Funktionen oder Variablen.
  - Geschriebenen Kommentaren, die seine Vorschläge leiten können.
  - Gängigen Codierungsmustern und Konventionen, die es aus seinen Trainingsdaten gelernt hat.
- **Vorhersageprozess**: Basierend auf diesem Kontext sagt Copilot vorher, was Sie als Nächstes schreiben möchten. Vorschläge können reichen von:
  - Dem Vervollständigen einer einzelnen Zeile (z. B. das Beenden einer Schleife oder Bedingung).
  - Dem Schreiben ganzer Funktionen oder Klassen.
  - Dem Vorschlagen von Algorithmen oder Lösungen für Probleme, die durch Ihren Code impliziert werden.

- **Beispiel**: Angenommen, Sie programmieren in Python und tippen `def factorial(n):`. Copilot könnte vorschlagen:
  ```python
  def factorial(n):
      if n == 0:
          return 1
      else:
          return n * factorial(n - 1)
  ```
  Es leitet die rekursive Natur einer Fakultätsfunktion aus dem Namen und Kontext ab.

- **Anzeige von Vorschlägen**: Vorschläge erscheinen als ausgegrauter (Geister-)Text im Editor. Sie können:
  - `Tab` drücken, um den Vorschlag zu akzeptieren.
  - Weitertippen, um ihn zu ignorieren.
  - `Alt+]` (oder `Option+]` auf macOS) verwenden, um durch mehrere Vorschläge zu blättern, falls Copilot Alternativen anbietet.

---

### **3. Inline-Chat für interaktive Hilfe**
Über passive Vorschläge hinaus bietet Copilot ein **Inline-Chat**-Feature für eine direktere Interaktion mit der KI. Dies ermöglicht es Ihnen, Fragen zu stellen oder Anweisungen innerhalb von VSCode zu geben.

- **Zugriff**: Drücken Sie `Strg+I` (oder `Cmd+I` auf macOS), um die Inline-Chat-Oberfläche in Ihrem Editor zu öffnen.
- **Fähigkeiten**:
  - **Code-Generierung**: Geben Sie eine Anfrage wie "Schreibe eine Funktion, die einen String in JavaScript umkehrt" ein, und Copilot könnte antworten mit:
    ```javascript
    function reverseString(str) {
        return str.split('').reverse().join('');
    }
    ```
  - **Erklärungen**: Fragen Sie "Erkläre diesen Code", und Copilot wird die Logik des ausgewählten Codeblocks erläutern.
  - **Debugging**: Beschreiben Sie ein Problem (z. B. "Warum funktioniert meine Schleife nicht?"), und es könnte Lösungen vorschlagen oder potenzielle Probleme hervorheben.
- **Anwendungsfall**: Wenn Sie bei einer Aufgabe feststecken, agiert der Inline-Chat wie ein Programmierassistent und bietet maßgeschneiderte Hilfe, ohne dass Sie Ihren Editor verlassen müssen.

---

### **4. Technische Architektur**
Hier ist ein tieferer Blick darauf, wie Copilot im Hintergrund operiert:

- **Codex-Modell**: Das Rückgrat von Copilot, Codex, ist ein transformerbasiertes neuronales Netzwerk, das entwickelt wurde, um Code zu verstehen und zu generieren. Es wurde auf Milliarden von Codezeilen in Dutzenden von Sprachen trainiert, was es ermöglicht, verschiedene Programmieraufgaben zu bewältigen.
- **Echtzeit-Kommunikation**: Die VSCode-Erweiterung sendet den Kontext Ihres Codes (z. B. die aktuelle Datei und Cursorposition) an die Server von GitHub, wo das Codex-Modell ihn verarbeitet und Vorschläge zurückgibt. Dies geschieht fast augenblicklich, dank optimierter Cloud-Infrastruktur.
- **Datenschutz**: GitHub betont, dass Ihr Code nicht gespeichert oder zur erneuten Trainierung des Modells verwendet wird. Vorschläge werden auf Basis vorab trainierter Daten generiert, was Ihre Arbeit privat hält.

---

### **5. Sprach- und Framework-Unterstützung**
Copilot ist sehr vielseitig und unterstützt eine breite Palette von Programmiersprachen und Frameworks, einschließlich:
- **Sprachen**: Python, JavaScript/TypeScript, Java, C++, C#, Go, Ruby, PHP, HTML/CSS, SQL und mehr.
- **Frameworks**: Es erkennt Muster in Frameworks wie React, Django, Spring oder TensorFlow und bietet relevante Vorschläge basierend auf dem Kontext.

Wenn Sie beispielsweise in einem React-Projekt arbeiten und `const [` tippen, könnte Copilot einen `useState`-Hook vorschlagen:
```javascript
const [count, setCount] = useState(0);
```

---

### **6. Lernen und Anpassung**
Copilot passt sich mit der Zeit Ihrer Programmierumgebung an:
- **Projektkontext**: Es lernt aus der aktuellen Datei und Projektstruktur und verbessert so die Relevanz der Vorschläge, während Sie arbeiten.
- **Kein persönliches Training**: Während es nicht auf Ihrem individuellen Code trainiert (aus Datenschutzgründen), verbessert sich das breitere Modell durch aggregierte Nutzungsdaten aller Copilot-Benutzer, verfeinert durch die Ingenieure von GitHub.

---

### **7. Praktische Workflow-Integration**
So passt Copilot in eine typische Programmier-Sitzung:

- **Starten einer Funktion**: Sie tippen eine Funktionssignatur, und Copilot vervollständigt den Körper basierend auf dem Namen oder Kommentaren.
- **Optionen erkunden**: Wenn Sie unsicher sind, wie Sie etwas implementieren sollen, kann der Inline-Chat Beispiele oder Alternativen liefern.
- **Beschleunigung von Wiederholungen**: Für repetitive Aufgaben (z. B. das Schreiben von API-Aufrufen oder Boilerplate-Code) schlägt Copilot sofort Code vor und reduziert manuellen Aufwand.
- **Lernwerkzeug**: Durch das Überprüfen seiner Vorschläge oder das Anfordern von Erklärungen können Sie neue Techniken oder Syntax lernen.

- **Beispiel-Workflow**:
  1. Sie tippen: `# Funktion zum Abrufen von Daten von einer API`.
  2. Copilot schlägt vor:
     ```python
     import requests

     def fetch_data(url):
         response = requests.get(url)
         return response.json()
     ```
  3. Sie akzeptieren es mit `Tab` und passen es bei Bedarf an.

---

### **8. Einschränkungen und Best Practices**
Obwohl leistungsstark, ist Copilot nicht fehlerfrei. Hier ist, was Sie beachten sollten:
- **Genauigkeit**: Vorschläge basieren auf Mustern in seinen Trainingsdaten, daher können sie gelegentlich veraltet, ineffizient oder falsch sein. Überprüfen Sie den Code immer.
- **Kein Ersatz**: Es ist ein Assistent, kein Programmierer. Sie müssen die Vorschläge verstehen, um sicherzustellen, dass sie zu Ihrem Projekt passen.
- **Lizenzierung**: Da es auf öffentlichem Code trainiert wurde, seien Sie vorsichtig bei der Verwendung von generiertem Code in proprietären Projekten – prüfen Sie bei Bedarf die Lizenzauswirkungen.
- **Beste Praxis**: Verwenden Sie beschreibende Namen und Kommentare, um Copilot zu leiten, und nutzen Sie den Inline-Chat für komplexe Aufgaben oder Klärungen.

---

### **Zusammenfassung**

GitHub Copilot funktioniert in VSCode, indem es OpenAI's Codex verwendet, um den Kontext Ihres Codes zu analysieren und Echtzeit-Vorschläge zu generieren, von einzelnen Zeilen bis zu vollständigen Funktionen. Es integriert sich nahtlos in Ihren Editor und bietet sowohl passive Vervollständigungen (akzeptiert mit `Tab`) als auch interaktive Hilfe über Inline-Chat (`Strg+I`). Es unterstützt zahlreiche Sprachen und Frameworks, passt sich Ihrem Projekt an und steigert die Produktivität. Es ist jedoch am effektivsten, wenn es mit Ihrem eigenen Programmierwissen kombiniert wird – überprüfen Sie seine Ausgabe, experimentieren Sie mit seinen Funktionen und verwenden Sie es als Werkzeug, um Ihre Fähigkeiten zu verbessern, nicht zu ersetzen.