---
audio: false
generated: true
lang: de
layout: post
title: Installieren und Verwenden der Gemini CLI
translated: true
type: note
---

Hier ist eine kurze Anleitung zur Installation, Einrichtung und Verwendung des **Google Gemini CLI**, einem Open-Source-AI-Agenten, der die Gemini-Funktionen in Ihr Terminal für Coding, Task-Automatisierung und mehr integriert. Diese Anleitung basiert auf den neuesten verfügbaren Informationen vom 29. Juni 2025.

---

## **Google Gemini CLI Guide**

### **Was ist Gemini CLI?**
Gemini CLI ist ein Open-Source-Kommandozeilen-Tool, das von Google entwickelt wurde und die Leistungsfähigkeit des Gemini 2.5 Pro Modells (mit einem 1-Million-Token-Kontextfenster) in Ihr Terminal bringt. Es unterstützt Coding, Debugging, Content-Generierung, Task-Automatisierung und multimodale Aufgaben wie Bild- und Videogenerierung. Es ist kostenlos mit einem Google-Konto nutzbar und integriert sich mit Tools wie Google Search und Model Context Protocol (MCP) Servern.

---

### **Voraussetzungen**
- **Node.js**: Version 18 oder höher. Prüfen mit `node -v`. Bei Bedarf von [nodejs.org](https://nodejs.org) installieren.
- **Google-Konto**: Erforderlich für den kostenlosen Zugang zu Gemini 2.5 Pro (60 Anfragen/Minute, 1.000 Anfragen/Tag).
- (Optional) **API-Schlüssel**: Für höhere Limits oder spezifische Modelle, generieren Sie einen unter [Google AI Studio](https://aistudio.google.com).
- (Optional) **Docker**: Für die MCP-Server-Integration (z.B. GitHub-Tools).

---

### **Installation**
Es gibt zwei Möglichkeiten, mit Gemini CLI zu beginnen:

1. **Global installieren**:
   ```bash
   npm install -g @google/gemini-cli
   gemini
   ```
   Dies installiert die CLI global und führt sie mit dem Befehl `gemini` aus.

2. **Ohne Installation ausführen**:
   ```bash
   npx https://github.com/google-gemini/gemini-cli
   ```
   Dies führt die CLI direkt ohne Installation aus, ideal zum Testen.

---

### **Einrichtung**
1. **CLI starten**:
   - Führen Sie `gemini` in Ihrem Terminal aus.
   - Beim ersten Start wählen Sie ein Thema (z.B. ASCII, dunkel, hell) und drücken die Eingabetaste.

2. **Authentifizierung**:
   - Wählen Sie **Login with Google** für kostenlosen Zugang (empfohlen für die meisten Benutzer).
   - Ein Browserfenster öffnet sich; melden Sie sich mit Ihrem Google-Konto an.
   - Alternativ verwenden Sie einen API-Schlüssel:
     - Generieren Sie einen Schlüssel unter [Google AI Studio](https://aistudio.google.com).
     - Setzen Sie ihn als Umgebungsvariable:
       ```bash
       export GEMINI_API_KEY=IHR_API_SCHLUESSEL
       ```
     - Dies ist nützlich für höhere Limits oder den Unternehmenseinsatz.

3. **Navigieren Sie zu Ihrem Projekt**:
   - Führen Sie `gemini` im Stammverzeichnis Ihres Projekts aus, um Kontext für codebezogene Aufgaben bereitzustellen.

---

### **Grundlegende Verwendung**
Gemini CLI arbeitet in einer interaktiven Read-Eval-Print Loop (REPL)-Umgebung. Geben Sie Befehle oder natürliche Sprachbefehle ein, um mit dem Gemini-Modell zu interagieren. Hier sind einige häufige Aufgaben:

1. **Code-Erklärung**:
   - Navigieren Sie zu einem Projektordner und führen Sie aus:
     ```bash
     gemini
     ```
   - Prompt: `Erkläre die Architektur dieses Projekts` oder `Beschreibe die Hauptfunktion in main.py`.
   - Die CLI liest Dateien und liefert eine strukturierte Erklärung.

2. **Code-Generierung**:
   - Prompt: `Erstelle eine einfache To-Do-App in HTML, CSS und JavaScript`.
   - Die CLI generiert den Code und kann ihn auf Anfrage in Dateien speichern.

3. **Debugging**:
   - Fügen Sie eine Fehlermeldung oder Stack-Trace ein und fragen Sie: `Was verursacht diesen Fehler?`.
   - Die CLI analysiert den Fehler und schlägt Korrekturen vor, möglicherweise unter Verwendung von Google Search für zusätzlichen Kontext.

4. **Dateiverwaltung**:
   - Prompt: `Organisiere meine PDF-Rechnungen nach Monat der Ausgabe`.
   - Die CLI kann Dateien manipulieren oder Formate konvertieren (z.B. Bilder zu PNG).

5. **GitHub-Integration**:
   - Verwenden Sie MCP-Server für GitHub-Aufgaben (z.B. das Auflisten von Issues):
     - Konfigurieren Sie einen GitHub-MCP-Server in `.gemini/settings.json` mit einem Personal Access Token (PAT).
     - Prompt: `Hole alle offenen Issues, die mir im foo/bar Repo zugewiesen sind`.
   - Führen Sie `/mcp` aus, um konfigurierte MCP-Server und Tools aufzulisten.

6. **Multimodale Aufgaben**:
   - Generieren Sie Medien mit Tools wie Imagen oder Veo:
     - Prompt: `Erstelle ein kurzes Video über die Abenteuer einer Katze in Australien mit Veo`.

---

### **Hauptfunktionen**
- **Kontextdateien (GEMINI.md)**: Fügen Sie eine `GEMINI.md`-Datei in Ihrem Projektstammverzeichnis hinzu, um Coding-Stile, Projektregeln oder Präferenzen zu definieren (z.B. "Verwende async/await für JavaScript"). Die CLI nutzt dies für maßgeschneiderte Antworten.
- **Integrierte Tools**:
   - `/tools`: Listet verfügbare Tools auf (z.B. Google Search, Dateioperationen).
   - `/compress`: Fasst den Chat-Kontext zusammen, um Tokens zu sparen.
   - `/bug`: Melden Sie Issues direkt an das Gemini CLI GitHub-Repo.
- **Nicht-interaktiver Modus**: Für Skripte, Befehle pipen:
   ```bash
   echo "Schreibe ein Python-Skript" | gemini
   ```
- **Konversationsspeicher**: Speichern Sie den Sitzungsverlauf mit `/save <tag>` und setzen Sie ihn mit `/restore <tag>` fort.
- **Benutzerdefinierte Konfiguration**:
   - Bearbeiten Sie `~/.gemini/settings.json` für globale Einstellungen oder `.gemini/settings.json` in einem Projekt für lokale Einstellungen.
   - Beispiel: MCP-Server oder benutzerdefinierte Themen festlegen.

---

### **Tipps und Tricks**
- **Beginnen Sie mit Plänen**: Fragen Sie bei komplexen Aufgaben zuerst nach einem Plan: `Erstelle einen detaillierten Implementierungsplan für ein Login-System`. Dies sorgt für eine strukturierte Ausgabe.
- **Nutzen Sie lokalen Kontext**: Kodieren Sie projektspezifische Details in `GEMINI.md` anstatt sich auf MCP-Server zu verlassen, für schnellere, zuverlässigere Antworten.
- **Debugging**: Aktivieren Sie die ausführliche Protokollierung mit `DEBUG=true gemini` für detaillierte Anfrage-/Antwort-Informationen.
- **Überprüfen Sie Änderungen**: Überprüfen Sie Dateiänderungen oder Befehle immer, bevor Sie sie genehmigen (tippen Sie `y` zur Bestätigung).
- **Erkunden Sie Tools**: Führen Sie `/tools` aus, um integrierte Fähigkeiten wie Websuche oder Speichern des Speichers zu entdecken.

---

### **Fehlerbehebung**
- **Authentifizierungsprobleme**: Stellen Sie sicher, dass Ihr Google-Konto oder API-Schlüssel gültig ist. Verwenden Sie `/auth`, um die Methode zu wechseln.
- **Ratenbegrenzungen**: Das kostenlose Kontingent erlaubt 60 Anfragen/Minute und 1.000/Tag. Für höhere Limits verwenden Sie einen API-Schlüssel oder Vertex AI.
- **Fehler**: Überprüfen Sie den [Fehlerbehebungsleitfaden](https://github.com/google-gemini/gemini-cli/docs/troubleshooting.md) auf GitHub.
- **Langsame Antworten**: Die CLI befindet sich in der Vorschauphase und kann bei API-Aufrufen langsam sein. Geben Sie Feedback auf GitHub.

---

### **Erweiterte Verwendung**
- **MCP-Server-Integration**:
  - Richten Sie einen GitHub-MCP-Server für Repository-Interaktionen ein:
    - Erstellen Sie einen GitHub PAT mit den notwendigen Berechtigungen.
    - Fügen Sie ihn zu `.gemini/settings.json` hinzu:
      ```json
      {
        "mcpServers": [
          {
            "name": "github",
            "url": "http://localhost:8080",
            "type": "github"
          }
        ]
      }
      ```
    - Führen Sie einen Docker-Container für den MCP-Server aus (siehe GitHub-Dokumentation).
- **Skripterstellung**: Automatisieren Sie Aufgaben durch Integration von Gemini CLI in Skripte:
  ```bash
  gemini --non-interactive "Generiere ein Bash-Skript zum Sichern meiner Dateien"
  ```
- **Multimodale Prompts**:
  - Beispiel: `Beschreibe dieses Bild: pfad/zum/bild.jpg` (erfordert ein vision-fähiges Modell wie `gemini-pro-vision`).

---

### **Einschränkungen**
- **Vorschau-Phase**: Gemini CLI befindet sich in der Pre-GA-Phase, mit möglicherweise eingeschränktem Support oder Fehlern.
- **Nicht vollständig Open-Source**: Nur die CLI-UI ist unter Apache-2.0-Lizenz; das Gemini-Modell ist proprietär.
- **Kontingentteilung**: Limits werden mit Gemini Code Assist geteilt, falls verwendet.
- **Zukünftige Preisgestaltung**: Die Preisgestaltung nach der Vorschauphase ist unklar; erweiterte Funktionen könnten kostenpflichtig werden.

---

### **Ressourcen**
- **Offizielles GitHub**: [github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
- **Dokumentation**: [gemini-cli.click](https://gemini-cli.click) oder GitHub-Docs
- **Blog-Ankündigung**: [blog.google](https://blog.google)
- **Feedback**: Melden Sie Bugs oder Vorschläge auf GitHub.

---

### **Beispiel-Workflow**
1. Installieren: `npm install -g @google/gemini-cli`
2. Ausführen: `cd mein-projekt && gemini`
3. Authentifizieren: Mit Google anmelden.
4. Prompt: `Schreibe ein Python-Skript für eine REST-API mit FastAPI`.
5. Generierten Code überprüfen und speichern.
6. Verwenden Sie `/tools`, um zusätzliche Funktionen wie GitHub-Integration zu erkunden.

---

Gemini CLI ist ein leistungsstarkes Tool für Entwickler, das nahtlose AI-Integration im Terminal bietet. Beginnen Sie einfach, nutzen Sie `GEMINI.md` für Kontext und erkunden Sie seine multimodalen Fähigkeiten, um die Produktivität zu steigern. Für weitere Beispiele sehen Sie sich die [GitHub-Tutorials](https://github.com/google-gemini/gemini-cli/docs/cli/tutorials.md) an.

Wenn Sie spezifische Beispiele benötigen oder Fragen zu einer bestimmten Funktion haben, lassen Sie es mich wissen!