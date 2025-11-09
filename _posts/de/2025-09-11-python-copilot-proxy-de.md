---
audio: false
date: 2025-09-11
generated: true
image: false
lang: de
layout: post
model: mistralai/mistral-medium-3.1
title: Implementierung Eines Python Copilot Proxy Servers
translated: true
type: note
---

Dieses Python-Skript ist ein **lokaler Proxy-Server**, der mit **GitHub Copilot** interagiert, um Code-Vervollständigungen zu generieren. Es imitiert das Verhalten des offiziellen GitHub Copilot-Plugins (z.B. für Neovim), indem es die Authentifizierung handhabt und Anfragen an die Copilot-API weiterleitet.

---

### **Wichtige Komponenten & Arbeitsablauf**
1. **Authentifizierung (`setup()` und `get_token()`)**
   - Verwendet **OAuth Device Flow** für die Authentifizierung bei GitHub.
   - Fordert einen **Device Code** und **User Code** von GitHub an.
   - Bittet den Benutzer, eine URL (`verification_uri`) zu besuchen und den `user_code` einzugeben.
   - Fragt GitHub wiederholt ab, bis ein **Access Token** empfangen wird.
   - Speichert das Token in `.copilot_token` für die zukünftige Verwendung.
   - Tauscht das Access Token gegen ein **Copilot Session Token** aus (erforderlich für API-Aufrufe).

2. **Token-Aktualisierung (`token_thread()`)**
   - Läuft in einem Hintergrund-Thread.
   - Aktualisiert das Copilot-Token alle **25 Minuten** (da Token ablaufen).

3. **Copilot-API-Interaktion (`copilot()`)**
   - Sendet einen **Prompt** (Code-Snippet) an die Copilot-API.
   - Gibt generierte Vervollständigungen im **Streaming-Modus** (zeilenweise) zurück.
   - Behandelt Fehler (z.B. ungültige/abgelaufene Token).

4. **HTTP-Server (`HTTPRequestHandler`)**
   - Lauscht auf **POST-Anfragen** (z.B. von einem lokalen Editor).
   - Extrahiert den `prompt` und die `language` aus der Anfrage.
   - Ruft `copilot()` auf und gibt die Vervollständigung als Klartext zurück.

5. **Hauptfunktion (`main()`)**
   - Startet den **Token-Aktualisierungs-Thread**.
   - Startet einen **HTTP-Server** auf einem bestimmten Port (Standard: `8080`).

---

### **So funktioniert es Schritt für Schritt**
1. **Erster Start (Kein Token vorhanden)**
   - Das Skript ruft `setup()` auf, um sich über OAuth zu authentifizieren.
   - Der Benutzer besucht GitHub, gibt einen Code ein und erteilt Zugriff.
   - Das Skript speichert das Access Token in `.copilot_token`.

2. **Folgestarts (Token existiert)**
   - Das Skript liest `.copilot_token` und holt sich ein Copilot Session Token.
   - Wenn das Token abläuft, wird es automatisch aktualisiert.

3. **Anfragen bearbeiten**
   - Ein lokaler Editor (z.B. Neovim) sendet eine **POST-Anfrage** mit einem Code-Snippet.
   - Das Skript leitet den Prompt an die Copilot-API weiter.
   - Die Vervollständigung wird an den Editor zurückgegeben.

4. **Token-Verwaltung**
   - Ein Hintergrund-Thread aktualisiert das Token alle **25 Minuten**, um ein Ablaufen zu vermeiden.

---

### **Warum dies existiert**
- **Umgeht offizielle Plugins**: Einige Editoren (z.B. Neovim) haben keine offizielle Copilot-Unterstützung. Dieses Skript dient als Brücke.
- **Lokaler Proxy**: Umgeht Rate Limits, indem Token lokal verwaltet werden.
- **Anpassbarkeit**: Kann für die Arbeit mit verschiedenen Editoren oder APIs modifiziert werden.

---

### **Sicherheits- und ethische Überlegungen**
- **Feste Client-ID**: Das Skript verwendet die offizielle `client_id` von GitHub Copilot (`Iv1.b507a08c87ecfe98`), was gegen die GitHub-ToS verstoßen kann, wenn es außerhalb genehmigter Plugins verwendet wird.
- **Token-Speicherung**: Das Access Token wird im Klartext (`.copilot_token`) gespeichert, was ein Sicherheitsrisiko darstellt.
- **Rate Limits**: Häufige Anfragen können die Missbrauchserkennung von GitHub auslösen.

---
### **Verwendung**
1. Führen Sie das Skript aus:
   ```sh
   python copilot_proxy.py [PORT]
   ```
   (Standard-Port: `8080`)

2. Konfigurieren Sie Ihren Editor so, dass er Anfragen an `http://localhost:8080` mit einer JSON-Nutzlast wie dieser sendet:
   ```json
   {
     "prompt": "def hello_world():",
     "language": "python"
   }
   ```

3. Das Skript gibt die Copilot-Vervollständigung zurück.

---
### **Mögliche Verbesserungen**
- **Bessere Fehlerbehandlung**: Wiederholen fehlgeschlagener Anfragen, Behandlung von Netzwerkproblemen.
- **Sichere Token-Speicherung**: Verwendung von verschlüsselter Speicherung oder Umgebungsvariablen.
- **Konfigurationsdatei**: Ermöglicht das Anpassen von `client_id`, `port`, etc.
- **Protokollierung**: Hinzufügen von Debug-Protokollen zur Fehlerbehebung.

---
### **Alternativen**
- Verwenden Sie **offizielle Copilot-Plugins** (VS Code, JetBrains, etc.).
- Probieren Sie **Open-Source-Alternativen** wie **Codeium** oder **Tabby** aus.

Dieses Skript ist eine clevere Problemumgehung, sollte aber aufgrund möglicher ToS-Verstöße mit Vorsicht verwendet werden.