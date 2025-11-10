---
audio: false
generated: true
lang: de
layout: post
title: Optimierung der gtag.js-Leistung auf Jekyll GitHub Pages
translated: true
type: note
---

Die Verwendung von `gtag.js` auf einer mit Jekyll erstellten GitHub Pages-Seite bringt einige besondere Einschränkungen mit sich, da GitHub Pages nur begrenzte serverseitige Kontrolle bietet und keinen direkten Zugriff auf Caching-Header oder serverseitiges Scripting ermöglicht. Dennoch können Sie die Abrufgeschwindigkeit von `https://www.googletagmanager.com/gtag/js?id=UA-66656236-1` mit clientseitigen Techniken und Jekyll-spezifischen Konfigurationen optimieren. Im Folgenden finden Sie gezielte Strategien zur Verbesserung der Leistung in diesem Kontext:

---

### 1. **`gtag.js` Asynchron Laden**
Stellen Sie sicher, dass das `gtag.js`-Skript asynchron geladen wird, um das Blockieren des Seitenrenderns zu vermeiden. In Ihrer Jekyll-Seite:
- Fügen Sie das Skript zu Ihrem Jekyll-Layout oder Include-File hinzu (z.B. `_includes/analytics.html` oder direkt in Ihr `default.html`-Layout).
- Verwenden Sie das `async`-Attribut:
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-66656236-1"></script>
```
- Platzieren Sie dies im `<head>` oder direkt vor `</body>` in Ihrer Jekyll-Vorlage (z.B. `_layouts/default.html`):
```html
<head>
  <script async src="https://www.googletagmanager.com/gtag/js?id=UA-66656236-1"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-66656236-1');
  </script>
</head>
```
- **Warum es hilft**: `async` stellt sicher, dass das Skript das HTML-Parsing nicht blockiert und reduziert so die wahrgenommene Ladezeit.

---

### 2. **Preconnect für Googles Domain hinzufügen**
Reduzieren Sie DNS-Lookup- und Verbindungslatenz, indem Sie einen `preconnect`-Hint für `googletagmanager.com` hinzufügen. In Ihrem Jekyll-Layout (`_layouts/default.html` oder `_includes/head.html`):
```html
<link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
```
- Platzieren Sie dies im `<head>` vor dem `gtag.js`-Skript.
- **Warum es hilft**: Initiiert die DNS-Auflösung und TCP-Verbindung frühzeitig und beschleunigt so den Abruf von `gtag.js`.

---

### 3. **`gtag.js` Lazy-Loaden**
Da GitHub Pages statisch ist, können Sie `gtag.js` lazy-loaden, um kritische Inhalte zu priorisieren. Fügen Sie der Jekyll-Vorlage oder einer separaten JS-Datei (z.B. `assets/js/analytics.js`) das folgende JavaScript hinzu:
```javascript
window.addEventListener('load', () => {
  const script = document.createElement('script');
  script.src = 'https://www.googletagmanager.com/gtag/js?id=UA-66656236-1';
  script.async = true;
  document.head.appendChild(script);
  script.onload = () => {
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-66656236-1');
  };
});
```
- Binden Sie dieses Skript in Ihr Jekyll-Layout ein:
```html
<script src="{{ '/assets/js/analytics.js' | relative_url }}"></script>
```
- **Warum es hilft**: Verzögert das Laden von `gtag.js` bis nach dem Laden der kritischen Ressourcen der Seite (z.B. HTML, CSS) und verbessert so die anfängliche Seiten Geschwindigkeit.

---

### 4. **Verwenden eines CDN-Proxys über Cloudflare**
GitHub Pages erlaubt keine benutzerdefinierten Caching-Header, aber Sie können `gtag.js` über ein CDN wie Cloudflare proxyen, um es näher an Ihren Benutzern zu cachen:
1. **Cloudflare einrichten**:
   - Fügen Sie Ihre GitHub Pages-Seite zu Cloudflare hinzu (z.B. `username.github.io`).
   - Aktivieren Sie Cloudflares DNS und Proxying für Ihre Domain.
2. **`gtag.js` proxyen**:
   - Erstellen Sie eine Page Rule in Cloudflare, um das `gtag.js`-Skript zu cachen, oder hosten Sie eine lokale Kopie im `_site`-Ordner Ihrer Jekyll-Seite (z.B. `assets/js/gtag.js`).
   - Aktualisieren Sie Ihren Script-Tag:
```html
<script async src="{{ '/assets/js/gtag.js' | relative_url }}"></script>
```
   - Synchronisieren Sie die lokale Kopie periodisch mit Googles `gtag.js`, um Aktualität sicherzustellen (manueller Prozess oder via CI/CD-Skript).
3. **Cache-Einstellungen**:
   - Setzen Sie in Cloudflare eine Cache-Regel für das Skript (z.B. `Cache Everything` mit einem TTL von 1 Stunde).
- **Warum es hilft**: Cloudflares Edge-Server reduzieren die Latenz, indem sie das Skript von einem Standort näher an Ihren Benutzern ausliefern.
- **Hinweis**: Seien Sie vorsichtig beim Proxyen von Google-Skripten, da diese häufig aktualisiert werden können. Testen Sie gründlich, um sicherzustellen, dass das Tracking funktioniert.

---

### 5. **Jekyll-Build und -Auslieferung optimieren**
Stellen Sie sicher, dass Ihre Jekyll-Seite optimiert ist, um die gesamte Seitenladezeit zu minimieren, was indirekt der `gtag.js`-Leistung hilft:
- **Assets minifizieren**:
  - Verwenden Sie ein Jekyll-Plugin wie `jekyll-compress` oder `jekyll-minifier`, um HTML, CSS und JS zu minifizieren.
  - Fügen Sie zu Ihrer `_config.yml` hinzu:
```yaml
plugins:
  - jekyll-compress
```
- **Gzip-Komprimierung aktivieren**:
  - GitHub Pages aktiviert Gzip automatisch für unterstützte Dateien, aber überprüfen Sie in den Browser-Dev-Tools im Header `Content-Encoding`, ob Ihre CSS/JS-Dateien komprimiert sind.
- **Blockierende Ressourcen reduzieren**:
  - Minimieren Sie die Anzahl der render-blockierenden CSS/JS-Dateien, die vor `gtag.js` geladen werden.
  - Verwenden Sie `jekyll-assets` oder ähnliches, um die Asset-Auslieferung zu optimieren:
```yaml
plugins:
  - jekyll-assets
```
- **Kritisches CSS Inlinen**:
  - Inlinen Sie kritisches CSS im `<head>` und verschieben Sie nicht-kritisches CSS, um die Render-Blocking-Zeit zu reduzieren, was das Laden von `gtag.js` scheinbar beschleunigen kann.
- **Bildoptimierung**:
  - Komprimieren Sie Bilder mit `jekyll-picture-tag` oder einem ähnlichen Plugin, um das gesamte Seitengewicht zu reduzieren und Bandbreite für `gtag.js` freizugeben.

---

### 6. **Zu Minimal Analytics wechseln**
Falls `gtag.js` weiterhin langsam ist oder Analytics nicht kritisch ist:
- Erwägen Sie leichtere Alternativen wie Plausible oder Fathom, die kleinere Skripte verwenden (~1 KB vs. ~50 KB für `gtag.js`).
- Beispiel für Plausible:
```html
<script defer data-domain="yourdomain.com" src="https://plausible.io/js/plausible.js"></script>
```
- Fügen Sie dies zu Ihrer Jekyll-`_includes/analytics.html` hinzu und binden Sie es in Ihr Layout ein.
- **Warum es hilft**: Kleinere Skripte laden schneller, besonders auf der statischen Infrastruktur von GitHub Pages.

---

### 7. **Leistung testen und überwachen**
- **Abrufzeit messen**:
  - Verwenden Sie Chrome DevTools (Network-Tab), um die Ladezeit von `gtag.js` zu überprüfen.
  - Testen Sie mit Tools wie Lighthouse oder WebPageTest, um die allgemeine Seitenleistung zu bewerten.
- **Benutzerstandorte simulieren**:
  - Verwenden Sie ein Tool wie Pingdom, um Ladezeiten aus Regionen zu testen, in denen sich Ihr Publikum befindet, da die Leistung von GitHub Pages und Googles CDN geografisch variiert.
- **Real User Metrics überwachen**:
  - Wenn Sie Google Analytics verwenden, prüfen Sie den Site Speed Report, um die Auswirkung von `gtag.js` zu verfolgen.
- **Jekyll-spezifisches Debugging**:
  - Führen Sie `jekyll build --profile` aus, um langsam buildende Komponenten Ihrer Seite zu identifizieren, die die Leistung indirekt beeinflussen könnten.

---

### 8. **Einschränkungen bei GitHub Pages**
- **Keine serverseitige Kontrolle**: GitHub Pages ist ein statischer Host, daher können Sie kein serverseitiges Tagging oder benutzerdefinierte Cache-Header für `gtag.js` implementieren.
- **Kein HTTP/3**: GitHub Pages verwendet HTTP/2, das schnell, aber nicht so optimiert wie HTTP/3 ist. Ein CDN wie Cloudflare kann auf HTTP/3 upgraden.
- **Geografische Latenz**: Die GitHub Pages-Server befinden sich hauptsächlich in den USA, daher können Benutzer fernab der USA langsamere Ladezeiten erfahren. Ein CDN mildert dies ab.

---

### Beispiel-Jekyll-Setup
Hier ist ein Beispiel für `_includes/analytics.html` für Ihre Jekyll-Seite, das `preconnect` und `async` kombiniert:
```html
<link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-66656236-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-66656236-1');
</script>
```
Binden Sie es in Ihr Layout ein (`_layouts/default.html`):
```html
<head>
</head>
```

---

### Nächste Schritte
- **Aktuelle Leistung testen**: Teilen Sie die aktuelle Abrufzeit für `gtag.js` (aus den Browser-Dev-Tools) oder die URL Ihrer Seite, und ich kann sie weiter analysieren.
- **Geografischer Kontext**: Lassen Sie mich den primären Standort Ihres Publikums wissen (z.B. USA, Europa, Asien), um CDN- oder Proxy-Empfehlungen anzupassen.
- **Cloudflare-Setup**: Wenn Sie Cloudflare verwenden möchten, kann ich detaillierte Schritte zum Proxyen von `gtag.js` bereitstellen.
- **Alternative Analytics**: Wenn Sie einen Wechsel von Google Analytics in Erwägung ziehen, kann ich spezifische, schlanke Tools und deren Jekyll-Integration empfehlen.

Möchten Sie, dass ich mich auf einen dieser Aspekte konzentriere oder eine spezifische Analyse durchführe (z.B. die Leistung Ihrer Seite teste oder eine Cloudflare-Setup-Anleitung bereitstelle)?