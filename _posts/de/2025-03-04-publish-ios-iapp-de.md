---
audio: false
generated: true
lang: de
layout: post
title: Veröffentlichung einer iOS-App im App Store
translated: true
type: note
---

Um das Apple Developer Program zum Hochladen einer iOS-App zu nutzen, egal ob für den persönlichen oder unternehmerischen Gebrauch, müssen Sie sich für das Programm anmelden, Ihre App vorbereiten und paketieren, sie hochladen und Updates verwalten. Im Folgenden finden Sie eine Schritt-für-Schritt-Anleitung, die alle Aspekte Ihrer Anfrage behandelt, einschließlich der Anforderung einer Dun & Bradstreet (D-U-N-S) Nummer für die Unternehmensnutzung, dem Paketieren der App, dem Hochladen des Archivs und dem Aktualisieren von Apps über die Website von Apple.

---

### 1. Anmeldung beim Apple Developer Program

#### Für Einzelpersonen (Persönliche Nutzung)
- **Apple ID erstellen**:  
  Falls Sie noch keine haben, gehen Sie zu [appleid.apple.com](https://appleid.apple.com) und registrieren Sie sich mit einer persönlichen E-Mail-Adresse.
- **Für das Programm anmelden**:  
  - Besuchen Sie [developer.apple.com/programs/](https://developer.apple.com/programs/) und klicken Sie auf "Enroll".
  - Melden Sie sich mit Ihrer Apple ID an.
  - Stimmen Sie den Bedingungen zu, geben Sie Ihren persönlichen, rechtlichen Namen und Ihre Adresse an und zahlen Sie die jährliche Gebühr von 99 USD.
- **Wichtiger Hinweis**: Ihr persönlicher Name wird als Verkäufer im App Store angezeigt.

#### Für Unternehmen (Unternehmerische Nutzung)
- **D-U-N-S Nummer beschaffen**:  
  - Eine D-U-N-S Nummer ist eine eindeutige neunstellige Kennung, die von Dun & Bradstreet vergeben wird, um den rechtlichen Status Ihrer Organisation zu verifizieren. Apple verlangt diese für Unternehmenskonten.
  - Prüfen Sie auf [dnb.com](https://www.dnb.com), ob Ihre Organisation bereits eine besitzt. Falls nicht, können Sie diese kostenlos über deren Website beantragen – die Bearbeitung kann bis zu zwei Wochen dauern.
- **Für das Programm anmelden**:  
  - Verwenden Sie eine Apple ID, die mit Ihrer Organisation verknüpft ist (z. B. eine Geschäfts-E-Mail).
  - Gehen Sie zu [developer.apple.com/programs/](https://developer.apple.com/programs/) und klicken Sie auf "Enroll".
  - Wählen Sie "Organization" und geben Sie an:
    - Rechtlicher Firmenname
    - Adresse der Hauptniederlassung
    - D-U-N-S Nummer
  - Die Person, die die Anmeldung vornimmt, muss die rechtliche Befugnis haben, den Bedingungen von Apple im Namen der Organisation zuzustimmen.
  - Zahlen Sie die jährliche Gebühr von 99 USD.
- **Wichtiger Hinweis**: Der Name Ihrer Organisation wird als Verkäufer im App Store angezeigt.

---

### 2. Vorbereitung und Paketierung der App
- **Entwickeln Sie Ihre App in Xcode**:  
  - Verwenden Sie Xcode, das offizielle Entwicklungstool von Apple, um Ihre iOS-App zu erstellen.
  - Stellen Sie sicher, dass sie die [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) erfüllt.
  - Legen Sie das Deployment Target fest und aktualisieren Sie die Versions- und Build-Nummern der App in den Projekteinstellungen.
- **Archivieren Sie die App**:  
  - Öffnen Sie Ihr Projekt in Xcode.
  - Wählen Sie "Generic iOS Device" (oder einen Simulator) als Build-Ziel.
  - Gehen Sie in der Menüleiste zu **Product** > **Archive**.
  - Xcode kompiliert Ihre App und erstellt ein Archiv, eine paketierte Version, die zur Distribution bereit ist, einschließlich Code, Ressourcen und Signierinformationen.

---

### 3. Hochladen des App-Archivs
- **Verwendung von Xcode**:  
  - Nach dem Archivieren öffnet sich das Organizer-Fenster automatisch in Xcode.
  - Wählen Sie Ihr Archiv aus und klicken Sie auf **Distribute App**.
  - Wählen Sie **App Store Connect** als Distributionsmethode.
  - Folgen Sie den Anweisungen, um das Archiv zu validieren und in App Store Connect hochzuladen.
- **Verwendung von Transporter (Alternative)**:  
  - Laden Sie die [Transporter-App](https://apps.apple.com/us/app/transporter/id1450874784) aus dem Mac App Store herunter.
  - Melden Sie sich mit Ihrer Apple ID an.
  - Fügen Sie die archivierte App-Datei (aus Xcode als `.ipa`-Datei exportiert) hinzu und laden Sie sie in App Store Connect hoch.
  - Diese Option ist nützlich für fortgeschrittene Benutzer oder Bulk-Uploads.

---

### 4. Aktualisieren von Apps über die Website von Apple (App Store Connect)
- **Auf App Store Connect zugreifen**:  
  - Gehen Sie zu [appstoreconnect.apple.com](https://appstoreconnect.apple.com) und melden Sie sich mit Ihrer Apple ID an.
- **Verwalten Sie Ihre App**:  
  - Wählen Sie Ihre App aus dem Dashboard aus.
  - Navigieren Sie zum Tab **App Store**.
  - Aktualisieren Sie die Metadaten (z. B. App-Beschreibung, Screenshots, Keywords).
  - Wählen Sie unter "Versions" den neuen Build aus, den Sie hochgeladen haben.
- **Zur Überprüfung einreichen**:  
  - Klicken Sie auf **Submit for Review**, um das Update an das Review-Team von Apple zu senden.
  - Nach der Freigabe können Sie es manuell veröffentlichen oder eine automatische Veröffentlichung planen.

---

### Zusätzliche Hinweise
- **Unternehmensspezifische Details**:  
  - Stellen Sie sicher, dass Ihre D-U-N-S Nummer und Ihre Organisationsinformationen korrekt sind, um Verzögerungen bei der Anmeldung zu vermeiden.
  - Sie können Teammitglieder (z. B. Entwickler, Tester) über App Store Connect zu Ihrem Konto einladen und Rollen wie "Developer" oder "Admin" zuweisen.
- **Häufige Herausforderungen und Tipps**:  
  - **Code Signing Probleme**: Überprüfen Sie Ihre Zertifikate und Provisioning Profiles in Xcode unter **Signing & Capabilities**. Verwenden Sie die Option "Automatically manage signing", wenn Sie unsicher sind.
  - **App Review Ablehnungen**: Testen Sie Ihre App gründlich, um die Richtlinien von Apple einzuhalten und Verzögerungen zu vermeiden.
  - **D-U-N-S Verzögerungen**: Beantragen Sie Ihre D-U-N-S Nummer frühzeitig, wenn Sie ein Unternehmen sind, da sie eine Voraussetzung für die Anmeldung ist.

---

Mit diesen Schritten können Sie das Apple Developer Program erfolgreich nutzen, um Ihre iOS-App hochzuladen und zu aktualisieren, egal ob als Einzelperson oder Unternehmen. Weitere Details finden Sie in der offiziellen Dokumentation von Apple unter [developer.apple.com](https://developer.apple.com).