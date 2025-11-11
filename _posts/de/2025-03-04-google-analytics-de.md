---
audio: false
generated: true
lang: de
layout: post
title: Nutzung von Google Analytics
translated: true
type: note
---

Um Google Analytics zu nutzen, integriere es in dein Frontend-Projekt und überprüfe die Daten sowohl über die App als auch die Website, indem du diese Schritte befolgst. Diese Anleitung geht davon aus, dass dein Frontend-Projekt entweder eine Website oder eine Mobile App ist und **Google Analytics 4 (GA4)** verwendet, den aktuellen Standard seit 2023, da Universal Analytics für neue Datenerfassung nicht mehr unterstützt wird.

---

### 1. Google Analytics einrichten
Bevor du Google Analytics in dein Projekt integrieren kannst, musst du ein Konto erstellen und es konfigurieren:

- **Konto erstellen**: Gehe zu [analytics.google.com](https://analytics.google.com) und registriere dich mit deinem Google-Konto, falls du noch keines hast.
- **Eine GA4-Property erstellen**:
  - Klicke unten links auf "Admin".
  - Klicke unter "Property" auf "Create Property", fülle die Details deines Projekts aus und wähle **Google Analytics 4**.
- **Einen Datenstrom hinzufügen**: Abhängig von deinem Frontend-Projekttyp:
  - **Für eine Website**: Wähle "Web", gib die URL deiner Website ein und benenne den Strom (z. B. "Meine Website").
  - **Für eine Mobile App**: Wähle "App", wähle iOS oder Android und gib deine App-Details an (z. B. Paketname).

Nachdem du den Datenstrom eingerichtet hast, erhältst du eine **Mess-ID** (z. B. `G-XXXXXXXXXX`), die du für die Integration verwendest.

---

### 2. Google Analytics in dein Frontend-Projekt integrieren
Der Integrationsprozess hängt davon ab, ob dein Frontend-Projekt eine Website oder eine Mobile App ist.

#### Für eine Website
- **Den Google Tag hinzufügen**:
  - Gehe in deiner GA4-Property zu "Datenströme", wähle deinen Web-Datenstrom aus und finde die "Tagging-Anweisungen".
  - Kopiere den bereitgestellten **Google Tag**-Script, der so aussieht:
    ```html
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=YOUR_MEASUREMENT_ID"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'YOUR_MEASUREMENT_ID');
    </script>
    ```
  - Füge diesen Code in den `<head>`-Bereich des HTML-Codes deiner Website ein und ersetze `YOUR_MEASUREMENT_ID` durch deine tatsächliche Mess-ID.
- **Für Single-Page Applications (SPAs)** (z. B. React, Angular, Vue):
  - Das Standard-Script erfasst nur den anfänglichen Seitenaufruf. Für SPAs, bei denen sich Seiten bei Routenänderungen nicht neu laden, verwende eine Bibliothek, um die Navigation zu verfolgen. Zum Beispiel in **React**:
    1. Installiere die `react-ga4`-Bibliothek:
       ```bash
       npm install react-ga4
       ```
    2. Initialisiere sie in deiner App (z. B. in `index.js` oder `App.js`):
       ```javascript
       import ReactGA from 'react-ga4';
       ReactGA.initialize('YOUR_MEASUREMENT_ID');
       ```
    3. Verfolge Seitenaufrufe bei Routenänderungen (z. B. mit React Router):
       ```javascript
       ReactGA.send({ hitType: "pageview", page: window.location.pathname });
       ```
       Rufe dies auf, wenn sich die Route ändert, z. B. in einem `useEffect`-Hook, der an den Ort des Routers gebunden ist.
  - Ähnliche Bibliotheken gibt es für andere Frameworks (z. B. `ngx-analytics` für Angular, `vue-ga` für Vue – prüfe die GA4-Kompatibilität).
- **Optional**: Verwende **Google Tag Manager** (GTM) anstelle des direkten Einbettens des Tags, um Tracking-Scripts einfacher zu verwalten.

#### Für eine Mobile App
- **Firebase verwenden (Empfohlen)**:
  - Wenn deine App Firebase verwendet, aktiviere **Google Analytics for Firebase**:
    1. Erstelle ein Firebase-Projekt unter [console.firebase.google.com](https://console.firebase.google.com).
    2. Füge deine App zum Projekt hinzu (iOS oder Android).
    3. Befolge die Anweisungen, um die Konfigurationsdatei herunterzuladen (z. B. `GoogleService-Info.plist` für iOS, `google-services.json` für Android) und füge sie deiner App hinzu.
    4. Installiere das Firebase SDK:
       - **iOS**: Verwende CocoaPods (`pod 'Firebase/Analytics'`) und initialisiere in `AppDelegate`.
       - **Android**: Füge Abhängigkeiten in `build.gradle` hinzu und initialisiere in deiner App.
    5. Firebase verknüpft automatisch mit deiner GA4-Property und beginnt mit der Datenerfassung.
- **Ohne Firebase**:
  - Verwende das eigenständige **Google Analytics SDK** für iOS oder Android (jetzt weniger verbreitet aufgrund der Firebase-Integration von GA4). Siehe die offizielle Dokumentation für das Setup, da es je nach Plattform variiert.

---

### 3. Die Integration überprüfen
- **Für Websites**: Nachdem du den Tracking-Code hinzugefügt hast:
  - Besuche deine Website und öffne den **Echtzeit**-Bericht in Google Analytics (unter "Berichte" > "Echtzeit").
  - Wenn dein Besuch erfasst wird, funktioniert die Integration.
  - Alternativ kannst du ein Browser-Tool wie **GA Checker** oder die Chrome DevTools-Konsole verwenden, um `gtag`-Aufrufe zu bestätigen.
- **Für Apps**: Überprüfe die Firebase Console oder den GA4-Echtzeitbericht, nachdem du deine App mit dem installierten SDK gestartet hast. Es kann einige Minuten dauern, bis Daten erscheinen.

---

### 4. Die Daten über die App und Website überprüfen
Sobald Google Analytics Daten sammelt, kannst du sie auf zwei Arten einsehen:
- **Google Analytics Web-Oberfläche**:
  - Melde dich bei [analytics.google.com](https://analytics.google.com) an.
  - Wähle deine GA4-Property aus.
  - Erkunde Berichte wie:
    - **Echtzeit**: Siehe Live-Benutzeraktivität.
    - **Zielgruppe**: Verstehe die Benutzerdemografie.
    - **Akquise**: Verfolge, woher die Benutzer kommen.
    - **Verhalten**: Analysiere Benutzerinteraktionen (z. B. Seitenaufrufe, Events).
- **Google Analytics Mobile App**:
  - Lade die offizielle **Google Analytics App** aus dem App Store (iOS) oder Google Play Store (Android) herunter.
  - Melde dich mit deinem Google-Konto an und wähle deine Property aus.
  - Sieh dir eine Auswahl von Berichten (z. B. Echtzeit, Zielgruppe) unterwegs an.

---

### Zusätzliche Hinweise
- **Wenn dein Projekt sowohl eine Website als auch eine App umfasst**: Du kannst mehrere Datenströme (z. B. einen für die Website, einen für die App) unter derselben GA4-Property hinzufügen. So kannst du kombinierte oder separate Analysen in derselben Oberfläche einsehen.
- **Events verfolgen**: Zusätzlich zu Seitenaufrufen kannst du benutzerdefinierte Events (z. B. Button-Klicks) mit `gtag('event', ...)` für Websites oder Firebase's `logEvent` für Apps verfolgen. Beispiel für eine Website:
  ```javascript
  gtag('event', 'click', {
    'event_category': 'Button',
    'event_label': 'Submit'
  });
  ```
- **GA4 vs. Universal Analytics**: Verwende GA4 für neue Projekte, da Universal Analytics nach dem 1. Juli 2023 keine Daten mehr verarbeitet hat.

Indem du diese Schritte befolgst, integrierst du Google Analytics erfolgreich in dein Frontend-Projekt und kannst Benutzerdaten sowohl über die Google Analytics Website als auch die Mobile App überwachen. Wenn dein Projekttyp (Website oder App) spezifischere Erklärungen erfordert, passe die Integrationsschritte entsprechend an!