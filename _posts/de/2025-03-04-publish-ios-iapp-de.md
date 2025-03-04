---
audio: false
generated: true
lang: de
layout: post
title: Veröffentlichung einer iOS-App im App Store
translated: true
---

Um das Apple Developer Program zum Hochladen einer iOS-App, sei es für persönliche oder Unternehmenszwecke, zu nutzen, müssen Sie sich im Programm anmelden, Ihre App vorbereiten und verpacken, sie hochladen und Updates verwalten. Im Folgenden finden Sie eine Schritt-für-Schritt-Anleitung, die alle Aspekte Ihrer Anfrage abdeckt, einschließlich der D-U-N-S-Nummer-Anforderung von Dun & Bradstreet für Unternehmenszwecke, der Verpackung der App, des Hochladens des Archivs und des Aktualisierens von Apps über die Apple-Website.

---

### 1. Anmeldung im Apple Developer Program

#### Für Einzelpersonen (Persönliche Nutzung)
- **Apple ID erstellen**:
  Wenn Sie noch keine haben, gehen Sie zu [appleid.apple.com](https://appleid.apple.com) und melden Sie sich mit einer persönlichen E-Mail-Adresse an.
- **Programm beitreten**:
  - Besuchen Sie [developer.apple.com/programs/](https://developer.apple.com/programs/) und klicken Sie auf "Beitreten."
  - Melden Sie sich mit Ihrer Apple ID an.
  - Akzeptieren Sie die Bedingungen, geben Sie Ihren persönlichen rechtlichen Namen und Ihre Adresse an und zahlen Sie die jährliche Gebühr von 99 USD.
- **Wichtiger Hinweis**: Ihr persönlicher Name wird als Verkäufer im App Store angezeigt.

#### Für Unternehmen (Organisatorische Nutzung)
- **D-U-N-S-Nummer erhalten**:
  - Eine D-U-N-S-Nummer ist eine eindeutige neunstellige Kennung, die von Dun & Bradstreet zugewiesen wird, um den rechtlichen Status Ihrer Organisation zu überprüfen. Apple erfordert dies für Unternehmenskonten.
  - Überprüfen Sie, ob Ihre Organisation bereits eine hat, unter [dnb.com](https://www.dnb.com). Wenn nicht, fordern Sie sie kostenlos über deren Website an—die Bearbeitung kann bis zu zwei Wochen dauern.
- **Programm beitreten**:
  - Verwenden Sie eine Apple ID, die mit Ihrer Organisation verbunden ist (z.B. eine Geschäfts-E-Mail).
  - Gehen Sie zu [developer.apple.com/programs/](https://developer.apple.com/programs/) und klicken Sie auf "Beitreten."
  - Wählen Sie "Organisation" und geben Sie an:
    - Name der rechtlichen Einheit
    - Hauptsitzadresse
    - D-U-N-S-Nummer
  - Die Person, die sich anmeldet, muss die rechtliche Befugnis haben, Apple’s Bedingungen im Namen der Organisation zu akzeptieren.
  - Zahlen Sie die jährliche Gebühr von 99 USD.
- **Wichtiger Hinweis**: Der Name Ihrer Organisation wird als Verkäufer im App Store angezeigt.

---

### 2. Vorbereitung und Verpackung der App
- **App in Xcode entwickeln**:
  - Verwenden Sie Xcode, das offizielle Entwicklertool von Apple, um Ihre iOS-App zu erstellen.
  - Stellen Sie sicher, dass sie den [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) entspricht.
  - Legen Sie das Bereitstellungsziel fest und aktualisieren Sie die Versions- und Buildnummern der App in den Projekteinstellungen.
- **App archivieren**:
  - Öffnen Sie Ihr Projekt in Xcode.
  - Wählen Sie "Generic iOS Device" (oder einen beliebigen Simulator) als Buildziel aus.
  - Gehen Sie zu **Produkt** > **Archiv** in der Menüleiste.
  - Xcode wird Ihre App kompilieren und ein Archiv erstellen, das eine verpackte Version zur Verteilung einschließlich Code, Ressourcen und Signaturinformationen ist.

---

### 3. Hochladen des App-Archivs
- **Mit Xcode**:
  - Nach dem Archivieren öffnet sich das Organizer-Fenster automatisch in Xcode.
  - Wählen Sie Ihr Archiv aus und klicken Sie auf **App verteilen**.
  - Wählen Sie **App Store Connect** als Verteilungsmethode.
  - Folgen Sie den Anweisungen, um das Archiv zu validieren und zu App Store Connect hochzuladen.
- **Mit Transporter (Alternative)**:
  - Laden Sie die [Transporter-App](https://apps.apple.com/us/app/transporter/id1450874784) aus dem Mac App Store herunter.
  - Melden Sie sich mit Ihrer Apple ID an.
  - Fügen Sie die archivierte App-Datei (als `.ipa`-Datei aus Xcode exportiert) hinzu und laden Sie sie zu App Store Connect hoch.
  - Diese Option ist nützlich für fortgeschrittene Benutzer oder Massenuploads.

---

### 4. Apps mit Apple’s Website (App Store Connect) aktualisieren
- **App Store Connect aufrufen**:
  - Gehen Sie zu [appstoreconnect.apple.com](https://appstoreconnect.apple.com) und melden Sie sich mit Ihrer Apple ID an.
- **Ihre App verwalten**:
  - Wählen Sie Ihre App aus dem Dashboard aus.
  - Navigieren Sie zur Registerkarte **App Store**.
  - Aktualisieren Sie die Metadaten (z.B. App-Beschreibung, Screenshots, Schlüsselwörter).
  - Unter "Versions," wählen Sie das neue Build, das Sie hochgeladen haben.
- **Zur Überprüfung einreichen**:
  - Klicken Sie auf **Zur Überprüfung einreichen**, um das Update an das Apple-Überprüfungsteam zu senden.
  - Nach der Genehmigung können Sie es manuell freigeben oder eine automatische Freigabe planen.

---

### Zusätzliche Hinweise
- **Unternehmensspezifische Details**:
  - Stellen Sie sicher, dass Ihre D-U-N-S-Nummer und die organisatorischen Informationen korrekt sind, um Verzögerungen bei der Anmeldung zu vermeiden.
  - Sie können Teammitglieder (z.B. Entwickler, Tester) zu Ihrem Konto über App Store Connect einladen und Rollen wie "Entwickler" oder "Admin" zuweisen.
- **Häufige Herausforderungen und Tipps**:
  - **Code-Signing-Probleme**: Überprüfen Sie Ihre Zertifikate und Bereitstellungsprofile in Xcode unter **Signing & Capabilities**. Verwenden Sie die Option "Automatisch Signatur verwalten", wenn Sie sich unsicher sind.
  - **App-Überprüfungsablehnungen**: Testen Sie Ihre App gründlich, um den Richtlinien von Apple zu entsprechen und Verzögerungen zu vermeiden.
  - **D-U-N-S-Verzögerungen**: Beantragen Sie Ihre D-U-N-S-Nummer frühzeitig, wenn Sie ein Unternehmen sind, da dies eine Voraussetzung für die Anmeldung ist.

---

Mit diesen Schritten können Sie das Apple Developer Program erfolgreich nutzen, um Ihre iOS-App hochzuladen und zu aktualisieren, sei es als Einzelperson oder als Unternehmen. Für weitere Details besuchen Sie die offizielle Dokumentation von Apple unter [developer.apple.com](https://developer.apple.com).