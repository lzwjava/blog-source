---
audio: false
generated: true
lang: de
layout: post
title: Verwendung von Google Analytics
translated: true
---

Um Google Analytics zu verwenden, integrieren Sie es in Ihr Frontend-Projekt und überprüfen Sie die Daten sowohl über die App als auch über die Website. Diese Anleitung geht davon aus, dass Ihr Frontend-Projekt entweder eine Website oder eine mobile App ist und **Google Analytics 4 (GA4)** verwendet, den aktuellen Standard ab 2023, da Universal Analytics keine neue Datenerfassung mehr unterstützt.

---

### 1. Google Analytics einrichten
Bevor Sie Google Analytics in Ihr Projekt integrieren, müssen Sie ein Konto erstellen und es konfigurieren:

- **Konto erstellen**: Gehen Sie zu [analytics.google.com](https://analytics.google.com) und melden Sie sich mit Ihrem Google-Konto an, falls Sie noch keines haben.
- **GA4-Eigenschaft erstellen**:
  - Klicken Sie auf "Admin" in der unteren linken Ecke.
  - Unter "Eigenschaft" klicken Sie auf "Eigenschaft erstellen", füllen Sie Ihre Projektdetails aus und wählen Sie **Google Analytics 4**.
- **Datenstrom hinzufügen**: Abhängig von Ihrem Frontend-Projekttyp:
  - **Für eine Website**: Wählen Sie "Web", geben Sie die URL Ihrer Website ein und benennen Sie den Stream (z. B. "Meine Website").
  - **Für eine mobile App**: Wählen Sie "App", wählen Sie iOS oder Android und geben Sie Ihre App-Details ein (z. B. Paketname).

Nach dem Einrichten des Datenstroms erhalten Sie eine **Messungs-ID** (z. B. `G-XXXXXXXXXX`), die Sie für die Integration verwenden.

---

### 2. Google Analytics in Ihr Frontend-Projekt integrieren
Der Integrationsprozess hängt davon ab, ob Ihr Frontend-Projekt eine Website oder eine mobile App ist.

#### Für eine Website
- **Google-Tag hinzufügen**:
  - Gehen Sie in Ihrer GA4-Eigenschaft zu "Datenströme", wählen Sie Ihren Webstream aus und finden Sie die "Tagging-Anweisungen".
  - Kopieren Sie das bereitgestellte **Google-Tag**-Skript, das so aussieht:
    ```html
    <!-- Google-Tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=YOUR_MEASUREMENT_ID"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'YOUR_MEASUREMENT_ID');
    </script>
    ```
  - Fügen Sie diesen Code in den `<head>`-Bereich des HTML Ihrer Website ein und ersetzen Sie `YOUR_MEASUREMENT_ID` durch Ihre tatsächliche Messungs-ID.
- **Für Single-Page-Anwendungen (SPAs)** (z. B. React, Angular, Vue):
  - Das Standard-Skript verfolgt nur das initiale Laden der Seite. Für SPAs, bei denen Seiten nicht beim Routenwechsel neu geladen werden, verwenden Sie eine Bibliothek, um die Navigation zu verfolgen. Zum Beispiel in **React**:
    1. Installieren Sie die `react-ga4`-Bibliothek:
       ```bash
       npm install react-ga4
       ```
    2. Initialisieren Sie sie in Ihrer App (z. B. in `index.js` oder `App.js`):
       ```javascript
       import ReactGA from 'react-ga4';
       ReactGA.initialize('YOUR_MEASUREMENT_ID');
       ```
    3. Verfolgen Sie Seitenaufrufe bei Routenänderungen (z. B. mit React Router):
       ```javascript
       ReactGA.send({ hitType: "pageview", page: window.location.pathname });
       ```
       Rufen Sie dies auf, wenn sich die Route ändert, z. B. in einem `useEffect`-Hook, der an den Standort des Routers gebunden ist.
  - Ähnliche Bibliotheken gibt es für andere Frameworks (z. B. `ngx-analytics` für Angular, `vue-ga` für Vue – überprüfen Sie die Kompatibilität mit GA4).
- **Optional**: Verwenden Sie **Google Tag Manager** (GTM) anstelle des direkten Einbettens des Tags für eine einfachere Verwaltung der Tracking-Skripte.

#### Für eine mobile App
- **Mit Firebase (Empfohlen)**:
  - Wenn Ihre App Firebase verwendet, aktivieren Sie **Google Analytics for Firebase**:
    1. Erstellen Sie ein Firebase-Projekt unter [console.firebase.google.com](https://console.firebase.google.com).
    2. Fügen Sie Ihre App dem Projekt hinzu (iOS oder Android).
    3. Folgen Sie den Anweisungen, um die Konfigurationsdatei herunterzuladen (z. B. `GoogleService-Info.plist` für iOS, `google-services.json` für Android) und fügen Sie sie zu Ihrer App hinzu.
    4. Installieren Sie das Firebase SDK:
       - **iOS**: Verwenden Sie CocoaPods (`pod 'Firebase/Analytics'`) und initialisieren Sie in `AppDelegate`.
       - **Android**: Fügen Sie Abhängigkeiten in `build.gradle` hinzu und initialisieren Sie in Ihrer App.
    5. Firebase verbindet sich automatisch mit Ihrer GA4-Eigenschaft und beginnt mit der Datenerfassung.
- **Ohne Firebase**:
  - Verwenden Sie das eigenständige **Google Analytics SDK** für iOS oder Android (weniger üblich mit der GA4-Firebase-Integration). Beziehen Sie sich auf die offizielle Dokumentation für die Einrichtung, da diese je nach Plattform variiert.

---

### 3. Integration überprüfen
- **Für Websites**: Nach dem Hinzufügen des Tracking-Codes:
  - Besuchen Sie Ihre Website und öffnen Sie den **Echtzeit**-Bericht in Google Analytics (unter "Berichte" > "Echtzeit").
  - Wenn Sie Ihren Besuch protokolliert sehen, funktioniert die Integration.
  - Alternativ können Sie ein Browser-Tool wie **GA Checker** oder die Chrome DevTools-Konsole verwenden, um `gtag`-Aufrufe zu bestätigen.
- **Für Apps**: Überprüfen Sie die Firebase-Konsole oder den GA4-Echtzeit-Bericht nach dem Starten Ihrer App mit dem installierten SDK. Es kann einige Minuten dauern, bis Daten angezeigt werden.

---

### 4. Daten über die App und Website überprüfen
Sobald Google Analytics mit der Datenerfassung beginnt, können Sie diese auf zwei Arten anzeigen:
- **Google Analytics Web-Oberfläche**:
  - Melden Sie sich bei [analytics.google.com](https://analytics.google.com) an.
  - Wählen Sie Ihre GA4-Eigenschaft.
  - Erkunden Sie Berichte wie:
    - **Echtzeit**: Live-Nutzeraktivität sehen.
    - **Zielgruppe**: Nutzerdemografien verstehen.
    - **Erwerb**: Nachverfolgen, woher die Nutzer kommen.
    - **Verhalten**: Nutzerinteraktionen analysieren (z. B. Seitenaufrufe, Ereignisse).
- **Google Analytics Mobile App**:
  - Laden Sie die offizielle **Google Analytics App** aus dem App Store (iOS) oder Google Play Store (Android) herunter.
  - Melden Sie sich mit Ihrem Google-Konto an und wählen Sie Ihre Eigenschaft.
  - Zeigen Sie eine Teilmenge von Berichten (z. B. Echtzeit, Zielgruppe) unterwegs an.

---

### Zusätzliche Hinweise
- **Wenn Ihr Projekt sowohl eine Website als auch eine App enthält**: Sie können mehrere Datenströme (z. B. einen für die Website, einen für die App) unter derselben GA4-Eigenschaft hinzufügen. Dies ermöglicht es Ihnen, kombinierte oder separate Analysen in derselben Oberfläche anzuzeigen.
- **Ereignisse verfolgen**: Neben Seitenaufrufen können Sie benutzerdefinierte Ereignisse (z. B. Klicks auf Schaltflächen) mit `gtag('event', ...)` für Websites oder Firebase’s `logEvent` für Apps verfolgen. Beispiel für eine Website:
  ```javascript
  gtag('event', 'click', {
    'event_category': 'Button',
    'event_label': 'Submit'
  });
  ```
- **GA4 vs. Universal Analytics**: Verwenden Sie GA4 für neue Projekte, da Universal Analytics keine Daten mehr verarbeitet, nachdem es am 1. Juli 2023 eingestellt wurde.

Durch die Befolgung dieser Schritte integrieren Sie Google Analytics erfolgreich in Ihr Frontend-Projekt und können Nutzerdaten sowohl über die Google Analytics-Website als auch über die mobile App überwachen. Wenn Ihr Projekttyp (Website oder App) spezifische Klarstellungen erfordert, passen Sie die Integrationsschritte entsprechend an!