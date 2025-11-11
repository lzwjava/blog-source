---
audio: false
generated: true
lang: de
layout: post
title: Veröffentlichung einer Chrome-Erweiterung
translated: true
type: note
---

Die Veröffentlichung eines Chrome-Plugins (Extensions) im Chrome Web Store ist ein unkomplizierter Prozess, wenn Sie die notwendigen Schritte sorgfältig befolgen. Im Folgenden finden Sie eine vollständige, schrittweise Anleitung, die Ihnen hilft, Ihre Extension im Chrome Web Store live zu schalten.

---

### Schritt 1: Bereiten Sie Ihre Chrome-Extension vor
Bevor Sie mit dem Veröffentlichungsprozess beginnen, stellen Sie sicher, dass Ihre Extension für die Öffentlichkeit bereit ist:

- **Testen Sie gründlich**: Testen Sie Ihre Extension auf verschiedenen Chrome-Versionen, um sicherzustellen, dass sie wie beabsichtigt funktioniert. Verwenden Sie die Funktion "Entpackt laden" von Chrome (zu finden unter `chrome://extensions/`), um sie lokal zu testen.
- **Bereinigen Sie den Code**: Entfernen Sie jeglichen Debug-Code, `console.log`-Anweisungen oder unnötige Kommentare, die sensible Informationen preisgeben oder die Leistung beeinträchtigen könnten.
- **Überprüfen Sie die Leistung**: Stellen Sie sicher, dass Ihre Extension den Browser nicht verlangsamt oder übermäßige Ressourcen verbraucht.
- **Überprüfen Sie manifest.json**: Diese Datei ist das Rückgrat Ihrer Extension. Stellen Sie sicher, dass sie Folgendes enthält:
  - Einen beschreibenden `name`.
  - Eine `version`-Nummer (z. B. "1.0.0" für Ihre erste Veröffentlichung).
  - Erforderliche `permissions` (z. B. "activeTab", "storage"), die Sie minimal und gerechtfertigt halten.
  - Ein `icons`-Feld, das auf Ihre Icon-Datei verweist (z. B. ein 128x128 Pixel großes `icon.png`).
  - Alle anderen notwendigen Felder wie `background`, `content_scripts` oder `action`, abhängig von der Funktionalität Ihrer Extension.

---

### Schritt 2: Packen Sie Ihre Extension zusammen
Um Ihre Extension im Chrome Web Store hochzuladen, müssen Sie sie korrekt verpacken:

- **Sammeln Sie die Dateien**: Stellen Sie sicher, dass Ihr Extension-Verzeichnis alle erforderlichen Dateien enthält:
  - `manifest.json`
  - HTML-, CSS-, JavaScript-Dateien
  - Bilder (einschließlich Ihres Icons)
- **Erstellen Sie eine ZIP-Datei**: Komprimieren Sie das gesamte Extension-Verzeichnis in eine `.zip`-Datei. Laden Sie keine `.crx`-Datei hoch, da der Chrome Web Store jetzt direkt `.zip`-Dateien akzeptiert.

---

### Schritt 3: Richten Sie ein Entwicklerkonto ein
Sie benötigen ein Chrome Web Store-Entwicklerkonto, um Ihre Extension zu veröffentlichen:

- **Melden Sie sich an**: Gehen Sie zum [Chrome Developer Dashboard](https://chrome.google.com/webstore/devconsole) und melden Sie sich mit Ihrem Google-Konto an.
- **Zahlen Sie die Gebühr**: Wenn Sie sich noch nicht registriert haben, zahlen Sie eine einmalige Anmeldegebühr von 5 US-Dollar. Dies ist eine einmalige Kosten, nicht pro Extension.

---

### Schritt 4: Bereiten Sie die Assets für die Store-Listung vor
Für die Store-Listung Ihrer Extension werden bestimmte Assets und Informationen benötigt, um Benutzer anzuziehen:

- **Icon**: Ein 128x128 Pixel großes Icon (z. B. `icon.png`), das in Ihrer `manifest.json` angegeben ist. Dieses erscheint in der Chrome-Symbolleiste und der Store-Listung.
- **Screenshots**: Mindestens einen Screenshot, der Ihre Extension in Aktion zeigt. Empfohlene Größen sind 1280x800 oder 640x400 Pixel. Mehrere Screenshots sind besser, um die Funktionalität zu präsentieren.
- **Optionale Werbebilder**: Ein Marquee-Bild (1400x560 Pixel) kann Ihre Listung verbessern, ist jedoch nicht erforderlich.
- **Beschreibung**:
  - **Kurzbeschreibung**: Eine prägnante Zusammenfassung (z. B. "Ein einfaches Tool zum [Zweck Ihrer Extension]").
  - **Detaillierte Beschreibung**: Eine längere Erklärung, was Ihre Extension tut, ihre Hauptfunktionen und warum Benutzer sie installieren sollten. Vermeiden Sie Rechtschreib- oder Grammatikfehler.
- **Datenschutzerklärung** (falls zutreffend): Wenn Ihre Extension persönliche oder sensible Benutzerdaten sammelt, erstellen Sie eine Datenschutzerklärung und hosten Sie diese online (z. B. auf einer persönlichen Website oder GitHub-Seite). Verlinken Sie sie in Ihrer Listung. Wenn keine Daten gesammelt werden, kann eine einfache Aussage wie "Diese Extension sammelt oder überträgt keine persönlichen Benutzerdaten" Vertrauen aufbauen.

---

### Schritt 5: Laden Sie Ihre Extension hoch
Jetzt sind Sie bereit, Ihre Extension einzureichen:

1. **Zugriff auf das Dashboard**: Melden Sie sich beim [Chrome Developer Dashboard](https://chrome.google.com/webstore/devconsole) an.
2. **Neues Element hinzufügen**: Klicken Sie auf "Add new item" oder einen ähnlichen Button, um den Upload-Prozess zu starten.
3. **ZIP-Datei hochladen**: Wählen Sie Ihre `.zip`-Datei aus und laden Sie sie hoch.
4. **Listung ausfüllen**:
   - Geben Sie Ihre Kurz- und detaillierte Beschreibung ein.
   - Laden Sie Ihr Icon, Screenshots und optionale Werbebilder hoch.
   - Wählen Sie passende **Kategorien** (z. B. "Productivity") und fügen Sie **Tags** hinzu (z. B. "time management"), um die Auffindbarkeit zu verbessern.
   - Verlinken Sie Ihre Datenschutzerklärung (falls zutreffend).
   - Legen Sie die **Sichtbarkeit** fest: Wählen Sie, ob Sie sofort nach der Genehmigung veröffentlichen oder einen späteren Zeitpunkt planen möchten. Für Ihre erste Veröffentlichung ist "publish after approval" typisch.
5. **Preisgestaltung**: Entscheiden Sie, ob Ihre Extension kostenlos (empfohlen für eine erste Veröffentlichung) oder kostenpflichtig ist. Die meisten Chrome-Extensions sind kostenlos, eine Monetarisierung ist später über In-App-Käufe oder Abonnements möglich (was jedoch zusätzliche Einrichtung erfordert).

---

### Schritt 6: Zur Überprüfung einreichen
- **Einreichen**: Sobald alle Felder ausgefüllt sind, reichen Sie Ihre Extension zur Überprüfung ein.
- **Überprüfungsprozess**: Das Chrome Web Store-Team wird Ihre Extension auf Einhaltung der [Program Policies](https://developer.chrome.com/docs/webstore/program-policies/) überprüfen. Dies dauert in der Regel einige Stunden bis wenige Tage.
- **Richtlinienkonformität**:
  - Stellen Sie sicher, dass Ihre Extension einen einzigen, klaren Zweck hat.
  - Begründen Sie alle Berechtigungen in Ihrer Beschreibung (z. B. warum "activeTab" oder "storage" benötigt wird).
  - Vermeiden Sie verbotene Verhaltensweisen wie Malware, übermäßige Datensammlung oder irreführende Behauptungen.

---

### Schritt 7: Nach der Genehmigung
- **Live gehen**: Sobald genehmigt, ist Ihre Extension im Chrome Web Store für Benutzer zur Installation verfügbar.
- **Feedback überwachen**: Überprüfen Sie Benutzerbewertungen und -rezensionen im Developer Dashboard, um Probleme oder Vorschläge zu adressieren.
- **Updates**: Für zukünftige Updates erhöhen Sie die `version` in `manifest.json`, erstellen eine neue `.zip`-Datei und laden sie über das Dashboard hoch. Sie wird erneut überprüft, bevor sie für Benutzer aktualisiert wird.

---

### Zusätzliche Tipps
- **Wählen Sie einen eindeutigen Namen**: Durchsuchen Sie den Chrome Web Store, um sicherzustellen, dass der Name Ihrer Extension nicht bereits vergeben ist. Machen Sie ihn beschreibend und einprägsam.
- **Fangen Sie einfach an**: Halten Sie Ihre erste Veröffentlichung kostenlos und nur auf Englisch. Sie können später kostenpflichtige Funktionen oder Übersetzungen hinzufügen.
- **Bewerben Sie sie**: Teilen Sie Ihre Extension in sozialen Medien oder auf anderen Plattformen, um die Sichtbarkeit zu erhöhen (optional).

---

Indem Sie diese Schritte befolgen – Vorbereiten Ihrer Extension, Verpacken, Einrichten eines Entwicklerkontos, Erstellen einer ansprechenden Store-Listung und Einreichen zur Überprüfung – werden Sie Ihr Chrome-Plugin erfolgreich im Chrome Web Store veröffentlichen. Viel Erfolg bei Ihrem Launch!