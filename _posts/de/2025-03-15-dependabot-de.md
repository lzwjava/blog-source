---
audio: false
generated: true
lang: de
layout: post
title: Entfernen von Dependabot
translated: true
type: note
---

Um Dependabot aus GitHub Actions zu entfernen, musst du deaktivieren, dass es Pull Requests erstellen kann, die Workflows auslösen, und optional alle benutzerdefinierten Workflows entfernen, die speziell auf Dependabot ausgerichtet sind. Nachfolgend sind die Schritte dazu aufgeführt. Ich gehe davon aus, dass sich "dependant bot" in deiner Anfrage auf "Dependabot" bezieht, ein gängiges Tool in GitHub für die Abhängigkeitsverwaltung.

---

### Schritt 1: Dependabot-Versionsupdates deaktivieren
Dependabot-Versionsupdates erstellen automatisch Pull Requests, um deine Abhängigkeiten auf dem neuesten Stand zu halten. Diese Pull Requests können GitHub Actions-Workflows auslösen. Um diese Funktion zu deaktivieren:

- **Konfigurationsdatei finden**: Überprüfe dein Repository auf eine Datei namens `dependabot.yml` im Verzeichnis `.github`.
- **Datei entfernen**: Wenn sie existiert, lösche die Datei `dependabot.yml` und committe diese Änderung. Dies verhindert, dass Dependabot Pull Requests für Versionsupdates erstellt.
- **Überprüfen**: Wenn keine `dependabot.yml`-Datei existiert, sind Versionsupdates bereits deaktiviert.

---

### Schritt 2: Dependabot-Sicherheitsupdates deaktivieren
Dependabot-Sicherheitsupdates generieren Pull Requests, um Schwachstellen in deinen Abhängigkeiten zu beheben, die ebenfalls GitHub Actions-Workflows auslösen können. Um dies abzuschalten:

- **Gehe zu den Repository-Einstellungen**: Klicke in deinem GitHub-Repository auf den Tab **Settings**.
- **Navigiere zu den Sicherheitseinstellungen**: Scrolle zu **Security & analysis** (oder **Code security and analysis**, abhängig von deiner GitHub-Oberfläche).
- **Sicherheitsupdates deaktivieren**: Finde **Dependabot security updates** und klicke auf **Disable**.

Dies verhindert, dass Dependabot Pull Requests für Sicherheitskorrekturen erstellt.

---

### Schritt 3: (Optional) Benutzerdefinierte, Dependabot-bezogene Workflows entfernen
Falls du GitHub Actions-Workflows eingerichtet hast, die speziell für die Behandlung von Dependabot-Pull Requests gedacht sind (z. B. automatisches Mergen, Labeln oder die Verwendung von Dependabot-Metadaten), möchtest du diese möglicherweise bereinigen:

- **Workflow-Dateien prüfen**: Sieh im Verzeichnis `.github/workflows` nach YAML-Dateien.
- **Dependabot-Logik identifizieren**: Suche nach Bedingungen wie `if: github.event.pull_request.user.login == 'dependabot[bot]'` oder Aktionen wie `dependabot/fetch-metadata`.
- **Entfernen oder anpassen**: Lösche diese Workflows oder passe sie an, um die Dependabot-spezifische Logik zu entfernen, und committe die Änderungen.

Dieser Schritt ist optional, da das Deaktivieren von Dependabot in Schritt 1 und 2 verhindert, dass es neue Pull Requests erstellt, was bedeutet, dass bestehende Workflows nicht mehr von Dependabot ausgelöst werden. Das Entfernen dieser Workflows stellt jedoch eine vollständige Bereinigung sicher.

---

### Zusätzliche Hinweise
- **Bestehende Pull Requests**: Das Deaktivieren von Dependabot schließt keine bestehenden, von ihm erstellten Pull Requests. Diese können bei Aktualisierungen weiterhin Workflows auslösen. Du kannst sie bei Bedarf manuell schließen.
- **Dependabot-Warnungen**: Wenn du auch Schwachstellenbenachrichtigungen stoppen möchtest (die nicht direkt mit GitHub Actions verknüpft sind), gehe zu **Settings > Security & analysis** und deaktiviere **Dependabot alerts**. Dies ist optional und nicht mit Workflow-Auslösern verbunden.

---

### Ergebnis
Durch das Abschließen der Schritte 1 und 2 wird Dependabot keine Pull Requests mehr in deinem Repository erstellen, was seinen Einfluss auf GitHub Actions effektiv "entfernt". Falls du Workflows für Dependabot angepasst hast, stellt Schritt 3 sicher, dass die gesamte zugehörige Automatisierung entfernt wird. Deine GitHub Actions werden jetzt nur noch basierend auf anderen Ereignissen ausgeführt und sind nicht mehr von Dependabot betroffen.