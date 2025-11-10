---
audio: false
generated: true
lang: de
layout: post
title: Erkennung der Benutzersprache
translated: true
type: note
---

### Erkennung der Länder- oder Spracheinstellung des Benutzers

Da Ihr Jekyll-Blog statisch ist (generiertes HTML/JS), ist eine serverseitige Erkennung ohne Integration einer Hosting-Plattform, die diese unterstützt (z.B. Netlify Functions oder GitHub Pages mit Einschränkungen), nicht einfach möglich. Der beste Ansatz ist die clientseitige JavaScript-Erkennung beim Laden der Seite. Sie haben zwei Hauptoptionen:

1.  **Browser-Spracheinstellung** (Empfohlen für Ihren Anwendungsfall): Dies erkennt die bevorzugte Sprache des Benutzers aus seinen Browser-Einstellungen (über `navigator.language` oder `navigator.languages`). Es ist schnell, erfordert keine externen APIs, respektiert die Privatsphäre der Benutzer (keine IP-Weitergabe) und bezieht sich direkt auf die Sprache rather than das Land. Länder haben oft mehrere Sprachen (z.B. wird in Indien weitläufig Englisch neben Hindi verwendet), daher ist dies genauer für die automatische Einstellung der Dropdown-Liste.

2.  **IP-basierte Landerkennung**: Dies verwendet eine kostenlose Geolocation-API, um das Land aus der IP-Adresse des Benutzers abzurufen und es dann einer Sprache zuzuordnen. Es ist nützlich, wenn Sie spezifisch Länderinformationen benötigen (z.B. für Analysen), erfordert aber einen externen Abruf, kann datenschutzrechtliche Bedenken haben und ist nicht immer präzise (VPNs, Proxys). Die Zuordnung von Land zu Sprache ist ungenau.

Ihr Ziel scheint die automatische Auswahl der Sprache in der `<select id="sort-select">` Dropdown-Liste zu sein (z.B. 'date-desc|en' für Englisch). Ich stelle Code für beide Methoden bereit, den Sie innerhalb Ihres `<script>` Tags, direkt nach `const sortSelect = document.getElementById('sort-select');`, hinzufügen können.

Priorisieren Sie die Überprüfung von `localStorage` (wie Ihr Code bereits tut), und greifen Sie nur dann auf die Erkennung zurück, wenn keine gespeicherte Präferenz vorhanden ist.

#### Option 1: Browser-Sprache verwenden (Einfacher und Bevorzugt)
Fügen Sie diesen Code-Ausschnitt hinzu. Er überprüft den primären Sprachcode von `navigator.language` (z.B. 'en-US' -> 'en', 'zh-CN' -> 'zh') und ordnet ihn Ihren Dropdown-Werten zu. Standardmäßig wird Englisch verwendet, wenn keine Übereinstimmung gefunden wird.

```javascript
// Inside window.addEventListener('load', function () { ... });

// After const sortSelect = ...;

// Restore from localStorage if available
const savedSort = localStorage.getItem('sortOption');
if (savedSort) {
  sortSelect.value = savedSort;
} else {
  // Detect browser language if no saved preference
  let lang = navigator.language.toLowerCase().split('-')[0]; // e.g., 'en-US' -> 'en'
  
  // Special handling for Chinese variants (zh-Hant for traditional)
  if (lang === 'zh') {
    const fullLang = navigator.language.toLowerCase();
    if (fullLang.includes('tw') || fullLang.includes('hk') || fullLang.includes('hant')) {
      lang = 'hant';
    } else {
      lang = 'zh'; // Simplified Chinese
    }
  }

  // Map to your dropdown options (add more if needed)
  const langMap = {
    'en': 'date-desc|en',
    'zh': 'date-desc|zh',
    'ja': 'date-desc|ja',
    'es': 'date-desc|es',
    'hi': 'date-desc|hi',
    'fr': 'date-desc|fr',
    'de': 'date-desc|de',
    'ar': 'date-desc|ar',
    'hant': 'date-desc|hant'
  };

  sortSelect.value = langMap[lang] || 'date-desc|en'; // Default to English
}

updatePosts();
```

Dies läuft synchron beim Laden, also ohne Verzögerungen. Testen Sie es, indem Sie Ihre Browser-Spracheinstellungen ändern (z.B. in Chrome: Einstellungen > Sprachen).

#### Option 2: IP-basierte Landerkennung verwenden
Dies erfordert einen asynchronen Abruf (Fetch) von einer kostenlosen API. Ich empfehle `country.is`, da es einfach ist und nur den Ländercode zurückgibt (z.B. {country: 'US'}). Es ist kostenlos, benötigt keinen API-Schlüssel und ist Open-Source.

Fügen Sie diesen Code hinzu. Hinweis: Es ist asynchron, daher verwenden wir `await` und packen es in eine async-Funktion, um die Benutzeroberfläche nicht zu blockieren. Wenn der Fetch fehlschlägt (z.B. durch Ad-Blocker), wird standardmäßig Englisch verwendet.

```javascript
// Inside window.addEventListener('load', async function () { ... });  // Make the load handler async

// After const sortSelect = ...;

// Restore from localStorage if available
const savedSort = localStorage.getItem('sortOption');
if (savedSort) {
  sortSelect.value = savedSort;
  updatePosts();
} else {
  try {
    // Fetch country code
    const response = await fetch('https://country.is/');
    const data = await response.json();
    const country = data.country.toUpperCase(); // e.g., 'US'

    // Map country codes to your languages (ISO 3166-1 alpha-2 codes)
    // This is approximate; expand as needed (e.g., multiple countries per language)
    const countryLangMap = {
      'US': 'date-desc|en',  // USA -> English
      'GB': 'date-desc|en',  // UK -> English
      'CN': 'date-desc|zh',  // China -> Simplified Chinese
      'TW': 'date-desc|hant', // Taiwan -> Traditional Chinese
      'HK': 'date-desc|hant', // Hong Kong -> Traditional Chinese
      'JP': 'date-desc|ja',  // Japan -> Japanese
      'ES': 'date-desc|es',  // Spain -> Spanish
      'MX': 'date-desc|es',  // Mexico -> Spanish (example for Latin America)
      'IN': 'date-desc|hi',  // India -> Hindi
      'FR': 'date-desc|fr',  // France -> French
      'DE': 'date-desc|de',  // Germany -> German
      'SA': 'date-desc|ar',  // Saudi Arabia -> Arabic
      'AE': 'date-desc|ar'   // UAE -> Arabic
    };

    sortSelect.value = countryLangMap[country] || 'date-desc|en'; // Default to English
  } catch (error) {
    console.warn('Country detection failed:', error);
    sortSelect.value = 'date-desc|en'; // Fallback
  }

  updatePosts();
}
```

-   **Hinweise**:
    -   Aktualisieren Sie das `window.addEventListener` wie gezeigt auf `async function ()`.
    -   Für den Datenschutz: Informieren Sie die Benutzer bei Bedarf (DSGVO in der EU). Einige Browser/APIs können Cross-Origin-Requests blockieren; testen Sie gründlich.
    -   Wenn Sie eine andere API bevorzugen, sind Alternativen `https://ip-api.com/json/` (gibt mehr Daten zurück wie `{ "countryCode": "US" }`) oder `https://ipgeolocation.io/ip_location/` (für Free Tier anmelden).
    -   Ratenbegrenzungen: Diese sind für persönliche Blogs großzügig, sollten aber überwacht werden, wenn der Traffic steigt.

#### Zusätzliche Überlegungen

-   **Fallback und Benutzerüberschreibung**: Benutzer können die Dropdown-Liste immer ändern, und sie wird im localStorage gespeichert. Sie könnten einen "Sprache erkennen" Button hinzufügen, wenn die automatische Erkennung nicht immer gewünscht ist.
-   **Testen**: Verwenden Sie VPNs, um verschiedene Länder zu simulieren, oder Browser-Erweiterungen, um Sprachen vorzutäuschen.
-   **Datenschutz**: Die Browser-Sprache ist risikoarm. Für IP-Methoden sollten Sie eine Einwilligungsabfrage in Betracht ziehen, wenn Ihr Publikum sensibel ist.
-   **Kombination beider Methoden**: Verwenden Sie zuerst die Browser-Sprache, dann die IP, wenn sie nicht mit Ihren unterstützten Sprachen übereinstimmt (aber halten Sie es einfach).
-   **Jekyll-spezifisch**: Keine Änderungen an der Jekyll-Konfiguration erforderlich. Wenn Sie auf Netlify/Vercel hosten, könnten Sie Edge Functions für die serverseitige Erkennung verwenden, aber das ist hier übertrieben.

Wenn dies nicht funktioniert oder Sie Fehler teilen können, geben Sie bitte mehr Details an!

[Country.is API](https://country.is/)  
[IP-API Geolocation](https://ip-api.com/)  
[ipgeolocation.io](https://ipgeolocation.io/)