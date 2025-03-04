---
audio: false
generated: true
lang: de
layout: post
title: Veröffentlichung einer Chrome-Erweiterung
translated: true
---

Das Veröffentlichen eines Chrome-Plugins (Erweiterung) im Chrome Web Store ist ein einfacher Prozess, wenn Sie die notwendigen Schritte sorgfältig befolgen. Hier ist eine vollständige Schritt-für-Schritt-Anleitung, die Ihnen hilft, Ihre Erweiterung im Chrome Web Store live zu schalten.

---

### Schritt 1: Vorbereitung Ihrer Chrome-Erweiterung
Bevor Sie den Veröffentlichungsprozess beginnen, stellen Sie sicher, dass Ihre Erweiterung für die Öffentlichkeit bereit ist:

- **Gründlich Testen**: Testen Sie Ihre Erweiterung auf verschiedenen Versionen von Chrome, um sicherzustellen, dass sie wie beabsichtigt funktioniert. Verwenden Sie die Funktion "Load unpacked" von Chrome (zu finden unter `chrome://extensions/`), um sie lokal zu testen.
- **Code Bereinigen**: Entfernen Sie alle Debug-Code, `console.log`-Anweisungen oder unnötige Kommentare, die sensible Informationen preisgeben oder die Leistung beeinträchtigen könnten.
- **Leistung Überprüfen**: Stellen Sie sicher, dass Ihre Erweiterung den Browser nicht verlangsamt oder übermäßige Ressourcen verwendet.
- **manifest.json Überprüfen**: Diese Datei ist das Rückgrat Ihrer Erweiterung. Stellen Sie sicher, dass sie Folgendes enthält:
  - Einen beschreibenden `name`.
  - Eine `version` (z.B. "1.0.0" für Ihre erste Veröffentlichung).
  - Erforderliche `permissions` (z.B. "activeTab", "storage"), halten Sie sie minimal und gerechtfertigt.
  - Ein `icons`-Feld, das auf Ihre Symboldatei zeigt (z.B. ein 128x128 Pixel großes `icon.png`).
  - Alle anderen notwendigen Felder wie `background`, `content_scripts` oder `action`, je nach Funktionalität Ihrer Erweiterung.

---

### Schritt 2: Verpacken Ihrer Erweiterung
Um Ihre Erweiterung im Chrome Web Store hochzuladen, müssen Sie sie korrekt verpacken:

- **Dateien Zusammenstellen**: Stellen Sie sicher, dass Ihr Erweiterungsverzeichnis alle erforderlichen Dateien enthält:
  - `manifest.json`
  - HTML-, CSS- und JavaScript-Dateien
  - Bilder (einschließlich Ihres Symbols)
- **ZIP-Datei Erstellen**: Komprimieren Sie das gesamte Erweiterungsverzeichnis in eine `.zip`-Datei. Laden Sie keine `.crx`-Datei hoch, da der Chrome Web Store jetzt `.zip`-Dateien direkt akzeptiert.

---

### Schritt 3: Einrichten eines Entwicklerkontos
Sie benötigen ein Chrome Web Store Entwicklerkonto, um Ihre Erweiterung zu veröffentlichen:

- **Anmelden**: Gehen Sie zum [Chrome Developer Dashboard](https://chrome.google.com/webstore/devconsole) und melden Sie sich mit Ihrem Google-Konto an.
- **Gebühr Bezahlen**: Wenn Sie sich noch nicht registriert haben, zahlen Sie eine einmalige Entwickleranmeldegebühr von 5 USD. Dies ist eine einmalige Gebühr, nicht pro Erweiterung.

---

### Schritt 4: Vorbereitung der Store-Listing-Assets
Ihr Erweiterungs-Store-Listing benötigt spezifische Assets und Informationen, um Benutzer anzuziehen:

- **Symbol**: Ein 128x128 Pixel großes Symbol (z.B. `icon.png`), das in Ihrem `manifest.json` angegeben ist. Dies erscheint in der Chrome-Symbolleiste und im Store-Listing.
- **Screenshots**: Mindestens ein Screenshot, der Ihre Erweiterung in Aktion zeigt. Empfohlene Größen sind 1280x800 oder 640x400 Pixel. Mehrere Screenshots sind besser, um die Funktionalität zu präsentieren.
- **Optionale Werbebilder**: Ein Marquee-Bild (1400x560 Pixel) kann Ihr Listing verbessern, ist aber nicht erforderlich.
- **Beschreibung**:
  - **Kurze Beschreibung**: Eine prägnante Zusammenfassung (z.B. "Ein einfaches Werkzeug für [Zweck Ihrer Erweiterung]").
  - **Detaillierte Beschreibung**: Eine längere Erklärung, was Ihre Erweiterung tut, ihre Hauptmerkmale und warum Benutzer sie installieren sollten. Vermeiden Sie Rechtschreib- oder Grammatikfehler.
- **Datenschutzrichtlinie** (falls zutreffend): Wenn Ihre Erweiterung persönliche oder sensible Benutzerdaten sammelt, erstellen Sie eine Datenschutzrichtlinie und hosten Sie sie online (z.B. auf einer persönlichen Website oder GitHub-Seite). Verlinken Sie darauf in Ihrem Listing. Wenn sie keine Daten sammelt, kann eine einfache Aussage wie "Diese Erweiterung sammelt oder überträgt keine persönlichen Benutzerdaten" Vertrauen schaffen.

---

### Schritt 5: Hochladen Ihrer Erweiterung
Jetzt sind Sie bereit, Ihre Erweiterung einzureichen:

1. **Dashboard Zugriff**: Melden Sie sich im [Chrome Developer Dashboard](https://chrome.google.com/webstore/devconsole) an.
2. **Neues Element Hinzufügen**: Klicken Sie auf "Add new item" oder eine ähnliche Schaltfläche, um den Upload-Prozess zu starten.
3. **ZIP-Datei Hochladen**: Wählen Sie Ihre `.zip`-Datei aus und laden Sie sie hoch.
4. **Listing Ausfüllen**:
   - Geben Sie Ihre kurze und detaillierte Beschreibung ein.
   - Laden Sie Ihr Symbol, Screenshots und optionale Werbebilder hoch.
   - Wählen Sie geeignete **Kategorien** (z.B. "Produktivität") und fügen Sie **Tags** (z.B. "Zeitmanagement") hinzu, um die Auffindbarkeit zu verbessern.
   - Verlinken Sie Ihre Datenschutzrichtlinie (falls zutreffend).
   - Legen Sie die **Sichtbarkeit** fest: Wählen Sie, ob Sie die Erweiterung sofort nach der Genehmigung veröffentlichen oder einen späteren Zeitpunkt planen. Für Ihre erste Veröffentlichung ist "nach Genehmigung veröffentlichen" typisch.
5. **Preisgestaltung**: Entscheiden Sie, ob Ihre Erweiterung kostenlos (empfohlen für eine erste Veröffentlichung) oder kostenpflichtig ist. Die meisten Chrome-Erweiterungen sind kostenlos, mit späteren Monetarisierungsmöglichkeiten durch In-App-Käufe oder Abonnements (dies erfordert zusätzliche Einstellungen).

---

### Schritt 6: Einreichen zur Überprüfung
- **Einreichen**: Sobald alle Felder ausgefüllt sind, reichen Sie Ihre Erweiterung zur Überprüfung ein.
- **Überprüfungsprozess**: Das Chrome Web Store-Team wird Ihre Erweiterung auf Einhaltung der [Programmrichtlinien](https://developer.chrome.com/docs/webstore/program-policies/) überprüfen. Dies dauert in der Regel einige Stunden bis einige Tage.
- **Einhaltung der Richtlinien**:
  - Stellen Sie sicher, dass Ihre Erweiterung einen einzigen, klaren Zweck hat.
  - Begründen Sie alle Berechtigungen in Ihrer Beschreibung (z.B., warum "activeTab" oder "storage" benötigt wird).
  - Vermeiden Sie verbotene Verhaltensweisen wie Malware, übermäßige Datensammlung oder irreführende Behauptungen.

---

### Schritt 7: Nach der Genehmigung
- **Live Schalten**: Sobald genehmigt, steht Ihre Erweiterung im Chrome Web Store für Benutzer zur Installation bereit.
- **Feedback Überwachen**: Überprüfen Sie Benutzerbewertungen und -bewertungen im Entwickler-Dashboard, um Probleme oder Vorschläge zu beheben.
- **Aktualisierungen**: Für zukünftige Aktualisierungen erhöhen Sie die `version` in `manifest.json`, erstellen Sie eine neue `.zip`-Datei und laden Sie sie über das Dashboard hoch. Sie wird erneut überprüft, bevor sie für Benutzer aktualisiert wird.

---

### Zusätzliche Tipps
- **Einzigartigen Namen Wählen**: Durchsuchen Sie den Chrome Web Store, um sicherzustellen, dass der Name Ihrer Erweiterung noch nicht vergeben ist. Machen Sie ihn beschreibend und einprägsam.
- **Einfach Beginnen**: Für Ihre erste Veröffentlichung sollten Sie es kostenlos und nur auf Englisch lassen. Sie können später bezahlte Funktionen oder Übersetzungen hinzufügen.
- **Promotion**: Teilen Sie Ihre Erweiterung in sozialen Medien oder auf anderen Plattformen, um die Sichtbarkeit zu erhöhen (optional).

---

Indem Sie diese Schritte befolgen – Vorbereitung Ihrer Erweiterung, Verpacken, Einrichten eines Entwicklerkontos, Erstellen eines ansprechenden Store-Listings und Einreichen zur Überprüfung – werden Sie Ihre Chrome-Erweiterung erfolgreich im Chrome Web Store veröffentlichen. Viel Erfolg bei Ihrem Launch!