---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Deaktiviere Claude Code-Bearbeitungsbestätigungs-Popup
translated: true
type: note
---

Um das Bearbeitungsbestätigungs-Popup in Claude Code zu deaktivieren (damit Änderungen direkt auf Dateien wie `sync_githook.py` angewendet werden, ohne Nachfrage), müssen Sie die Berechtigungen in Ihrer `settings.json`-Datei konfigurieren. Dies ist der "Claude Code JSON", den Sie meinen – es ist die Hauptkonfigurationsdatei von Claude Code für Benutzereinstellungen.

### Einrichtungsschritte

1. **Datei finden oder erstellen**:
   - Die Datei befindet sich unter `~/.claude/settings.json` (auf macOS/Linux) oder `%USERPROFILE%\.claude\settings.json` (auf Windows). Der `.claude`-Ordner ist versteckt, verwenden Sie also Ihr Terminal/Datei-Explorer, um dorthin zu navigieren.
   - Wenn die Datei oder der Ordner nicht existiert, erstellen Sie sie. Dies können Sie durch Ausführen des `/config`-Befehls von Claude Code in seinem interaktiven REPL tun (es führt Sie zur Einstellungsoberfläche).

2. **JSON bearbeiten**:
   - Öffnen Sie `settings.json` in einem Texteditor (z.B. VS Code).
   - Fügen Sie den `permissions`-Abschnitt hinzu oder aktualisieren Sie ihn, um Bearbeitungen automatisch zu genehmigen. Hier eine einfache Konfiguration, um Abfragen für alle Bearbeitungsaktionen zu deaktivieren:

     ```json:disable-run
     {
       "permissions": {
         "defaultMode": "acceptEdits",
         "allow": [
           "Edit(*)",
           "Write(*)",
           "MultiEdit(*)"
         ],
         "ask": []
       }
     }
     ```

     - **Was dies bewirkt**:
       - `"defaultMode": "acceptEdits"`: Setzt den globalen Standard, Bearbeitungen ohne Nachfrage zu akzeptieren.
       - `"allow"`: Genehmigt vorab spezifische Tools wie `Edit` (für Einzeldatei-Bearbeitungen), `Write` (für das Schreiben von Inhalten) und `MultiEdit` (für Stapeländerungen) für beliebige Dateien (`*` Wildcard).
       - `"ask": []`: Stellt sicher, dass keine Aktionen eine Abfrage auslösen, es sei denn, sie werden explizit anderswo verweigert.
     - Speichern Sie die Datei. Änderungen werden in Ihrer nächsten Claude Code-Sitzung sofort übernommen.

3. **Testen**:
   - Starten Sie Claude Code neu oder laden Sie die Sitzung neu.
   - Bitten Sie es, eine Datei zu bearbeiten (z.B. "Bearbeite sync_githook.py, um einen Kommentar hinzuzufügen"). Es sollte die Änderung ohne Popup anwenden.
   - Wenn Sie projektspezifische Einstellungen möchten (z.B. nur für dieses Repo), erstellen Sie `.claude/settings.json` im Stammverzeichnis Ihres Projekts statt im Benutzerverzeichnis.

4. **Optionale Anpassungen**:
   - Für feinere Kontrolle (z.B. nur Bearbeitungen in bestimmten Verzeichnissen erlauben): Ändern Sie `"Edit(*)"` zu `"Edit(./src/**)"`.
   - Wenn Abfragen weiterhin auftreten, führen Sie `/allowed-tools` im REPL aus, um die aktuellen Regeln zu prüfen, oder verwenden Sie `/config`, um über die UI anzupassen.
   - Aus Sicherheitsgründen: Vermeiden Sie zu breite `allow`-Regeln – beginnen Sie einfach und erweitern Sie sie.

Dies sollte Ihren Workflow ohne Unterbrechungen beschleunigen. Wenn Sie sich in einer Enterprise-Umgebung befinden, prüfen Sie bei Ihrem Administrator, da verwaltete Richtlinien Benutzereinstellungen überschreiben können.

[Claude Code Settings Docs](https://docs.claude.com/en/docs/claude-code/settings)  
[Disable Claude Code Permission Prompts Guide](https://www.arsturn.com/blog/how-to-disable-claude-code-permission-prompts)