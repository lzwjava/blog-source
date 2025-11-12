---
audio: false
generated: true
lang: de
layout: post
title: Erste Schritte mit GitHub Copilot in VS Code
translated: true
type: note
---

Die Verwendung von GitHub Copilot in Visual Studio Code (VS Code) ist unkompliziert, sobald es eingerichtet ist. Nachfolgend finden Sie eine Schritt-für-Schritt-Anleitung für den Einstieg, Stand 20. März 2025:

---

### Schritt 1: VS Code installieren
- Stellen Sie sicher, dass Visual Studio Code installiert ist. Laden Sie es von [code.visualstudio.com](https://code.visualstudio.com/) herunter, falls noch nicht geschehen.
- Aktualisieren Sie VS Code auf die neueste Version für optimale Kompatibilität (gehen Sie zu `Hilfe > Nach Updates suchen`).

---

### Schritt 2: Die GitHub Copilot-Erweiterung installieren
1. **Öffnen Sie VS Code**.
2. **Gehen Sie zum Extensions Marketplace**:
   - Klicken Sie auf das Erweiterungen-Symbol in der Aktivitätsleiste links (oder drücken Sie `Strg+Umschalt+X` / `Cmd+Umschalt+X` auf dem Mac).
3. **Suchen Sie nach "GitHub Copilot"**:
   - Geben Sie "GitHub Copilot" in die Suchleiste ein.
   - Suchen Sie nach der offiziellen Erweiterung von GitHub (sie hat ein verifiziertes Abzeichen).
4. **Installieren Sie die Erweiterung**:
   - Klicken Sie auf die Schaltfläche `Installieren` neben "GitHub Copilot".
5. **Optional: Copilot Chat installieren (Empfohlen)**:
   - Suchen Sie nach "GitHub Copilot Chat" und installieren Sie es ebenfalls. Dies fügt konversationelle KI-Funktionen hinzu, wie das Stellen von Fragen oder das Generieren von Code per Chat.

---

### Schritt 3: Bei GitHub Copilot anmelden
1. **Bei GitHub authentifizieren**:
   - Nach der Installation erscheint eine Aufforderung zur Anmeldung.
   - Klicken Sie im Pop-up auf `Bei GitHub anmelden` oder gehen Sie zum Copilot-Status-Symbol (rechte untere Ecke von VS Code) und wählen Sie "Anmelden".
2. **Im Browser autorisieren**:
   - Ein Browserfenster öffnet sich und fordert Sie auf, sich in Ihr GitHub-Konto einzuloggen.
   - Genehmigen Sie die Autorisierungsanfrage, indem Sie auf `Authorize Git hypoxia` klicken.
3. **Code kopieren**:
   - GitHub stellt einen Einmal-Code bereit. Kopieren Sie ihn und fügen Sie ihn zurück in VS Code ein, wenn Sie dazu aufgefordert werden.
4. **Aktivierung überprüfen**:
   - Sobald Sie angemeldet sind, sollte das Copilot-Symbol in der Statusleiste grün werden, was seine Aktivität anzeigt. Sie erhalten auch eine Benachrichtigung, die Ihren Zugriff bestätigt.

---

### Schritt 4: Copilot konfigurieren (Optional)
- **Vorschläge aktivieren/deaktivieren**:
  - Gehen Sie zu `Datei > Einstellungen > Einstellungen` (oder `Strg+,` / `Cmd+,`).
  - Suchen Sie nach "Copilot", um Einstellungen wie das Aktivieren von Inline-Vorschlägen oder das Deaktivieren für bestimmte Sprachen anzupassen.
- **Abonnement überprüfen**:
  - Copilot erfordert nach einer 30-tägigen Testphase ein Abonnement (10 $/Monat oder 100 $/Jahr). Studierende, Lehrkräfte und Maintainer von Open-Source-Projekten können über [GitHub Education](https://education.github.com/) oder die Copilot-Einstellungen kostenlosen Zugang beantragen.

---

### Schritt 5: Copilot verwenden
So nutzen Sie Copilot in Ihrem Codierungs-Workflow:

#### 1. **Code-Vorschläge**
- **Inline-Autovervollständigung**:
  - Beginnen Sie mit der Eingabe in einer Datei (z. B. `def calculate_sum(` in Python), und Copilot schlägt Vervollständigungen in grauem Text vor.
  - Drücken Sie `Tab`, um den Vorschlag zu akzeptieren, oder tippen Sie weiter, um ihn zu ignorieren.
- **Mehrzeilige Vorschläge**:
  - Schreiben Sie einen Kommentar wie `// Function to sort an array` und drücken Sie Enter. Copilot könnte eine gesamte Implementierung vorschlagen (z. B. einen Sortieralgorithmus).
  - Verwenden Sie `Alt+]` (oder `Option+]` auf dem Mac), um durch mehrere Vorschläge zu blättern.

#### 2. **Code-Generierung aus Kommentaren**
- Geben Sie einen beschreibenden Kommentar ein, wie:
  ```javascript
  // Fetch data from an API and handle errors
  ```
  Drücken Sie Enter, und Copilot könnte generieren:
  ```javascript
  async function fetchData(url) {
    try {
      const response = await fetch(url);
      if (!response.ok) throw new Error('Network response was not ok');
      return await response.json();
    } catch (error) {
      console.error('Fetch error:', error);
    }
  }
  ```
- Akzeptieren Sie mit `Tab` oder passen Sie ihn nach Bedarf an.

#### 3. **Copilot Chat (falls installiert)**
- **Chat öffnen**:
  - Klicken Sie auf das Chat-Symbol in der Seitenleiste oder verwenden Sie `Strg+Alt+C` (anpassbar).
- **Fragen stellen**:
  - Geben Sie etwas ein wie "Explain how Promises work in JavaScript" oder "Write a Python script to read a CSV file."
  - Copilot antwortet im Chat-Bereich und kann Code direkt in Ihren Editor einfügen.
- **Kontextbezogene Hilfe**:
  - Markieren Sie Code, klicken Sie mit der rechten Maustaste und wählen Sie "Ask Copilot", um ihn erklären oder umstrukturieren zu lassen.

#### 4. **Debugging und Testing**
- Schreiben Sie einen Kommentar wie `// Write unit tests for this function`, und Copilot kann Testfälle mit Frameworks wie Jest oder PyTest generieren.

---

### Tipps für eine effektive Nutzung
- **Seien Sie spezifisch**: Je mehr Kontext Sie bieten (z. B. Kommentare, Variablennamen), desto besser sind die Vorschläge von Copilot.
- **Vorschläge überprüfen**: Copilot ist nicht perfekt – überprüfen Sie seinen Code immer auf Richtigkeit und Sicherheit.
- **Sprachunterstützung**: Es funktioniert am besten mit gängigen Sprachen (Python, JavaScript, Java usw.), unterstützt aber Dutzende weitere.
- **Tastenkürzel**:
  - `Alt+\` (oder `Option+\` auf dem Mac): Zeigen Sie alle Vorschläge manuell an.
  - `Strg+Eingabe`: Öffnen Sie das Vorschlagsfenster.

---

### Problembehandlung
- **Funktioniert nicht?**:
  - Stellen Sie sicher, dass Sie angemeldet sind (überprüfen Sie die Statusleiste).
  - Vergewissern Sie sich, dass Ihr Abonnement in Ihren GitHub-Kontoeinstellungen aktiv ist.
  - Starten Sie VS Code neu oder installieren Sie die Erweiterung neu, falls die Probleme bestehen bleiben.
- **Keine Vorschläge?**:
  - Überprüfen Sie, ob Copilot für die aktuelle Sprache aktiviert ist (`editor.inlineSuggest.enabled` sollte in den Einstellungen auf "true" stehen).

---

Das war's! Sie sind nun bereit, GitHub Copilot in VS Code zu verwenden. Beginnen Sie, indem Sie eine Datei öffnen, etwas Code oder einen Kommentar eingeben und sich von Copilot unterstützen lassen. Viel Spaß beim smarten Coden!