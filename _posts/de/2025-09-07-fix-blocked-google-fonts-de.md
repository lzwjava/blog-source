---
audio: false
date: 2025-09-07
generated: true
image: false
lang: de
layout: post
title: Behebung blockierter Google Fonts-Anfragen
translated: true
type: note
---

Diese Anfrage stammt von deiner Seite, die versucht, ein Webfont-Stylesheet von Google Fonts zu laden:

* **Was es ist:** `https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap` ist das CSS, das die **Open Sans** Schriftarten definiert. Dein Theme oder benutzerdefiniertes CSS bindet es ein, damit die Seite in Open Sans dargestellt werden kann.
* **Warum du "Status: — / 0 B / no headers" siehst:** DevTools zeigt das an, wenn die Anfrage **blockiert oder abgebrochen** wird (z.B. durch einen Ad-/Privacy-Blocker, eine strikte Content-Security-Policy, eine instabile Netzwerkverbindung oder eine Länderblockade). Die Seite *versucht* trotzdem, es anzufordern, daher die Zeile im Netzwerk-Tab.

### Woher es in einem Jekyll-Blog wahrscheinlich stammt

Normalerweise trifft einer dieser Punkte zu:

1. **Das Theme bindet es im `<head>` ein**
   Suche nach einer Zeile wie
   `<link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap" rel="stylesheet">`
   in `_layouts/default.html` oder `_includes/head.html` (oder dem entsprechenden File des Themes, wenn du `remote_theme` verwendest).

2. **SCSS importiert es**
   Überprüfe `/assets/css/*.scss` oder `/_sass/**` auf
   `@import url("https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap");`

3. **Remote-Theme** (z.B. jekyll-theme-cayman) bindet Google Fonts fest in seinem Head-Include ein. Wenn du das Head-Include/Layout des Themes in deinem Repository überschreibst, kannst du es entfernen.

### Wie du es schnell findest

Führe im Stammverzeichnis deines Site-Repos einen dieser Befehle aus:

```
rg -n "fonts.googleapis.com"
rg -n "Open Sans"
rg -n "display=swap"
```

### Optionen, um es zu beheben oder zu ändern

**A) Google Fonts entfernen und einen System Font Stack verwenden (schnellste & datenschutzfreundliche Methode)**

1. Lösche den `<link>` (oder den SCSS `@import`), der die Google Fonts lädt.
2. Setze in deinem Haupt-Stylesheet einen System Font Stack:

   ```css
   html, body {
     font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Ubuntu,
                  "Helvetica Neue", Arial, "Noto Sans", sans-serif,
                  "Apple Color Emoji", "Segoe UI Emoji";
   }
   ```

   (In Jekyll füge dies in `assets/css/style.scss` ein, mit Front-Matter `---` Zeilen oben.)

**B) Open Sans behalten, aber selbst hosten**

1. Lade die WOFF2-Dateien für Open Sans (400 & 700) herunter und lege sie unter `assets/fonts/` ab.
2. Füge deinem CSS hinzu:

   ```css
   @font-face {
     font-family: "Open Sans";
     font-style: normal;
     font-weight: 400;
     font-display: swap;
     src: url("/assets/fonts/OpenSans-400.woff2") format("woff2");
   }
   @font-face {
     font-family: "Open Sans";
     font-style: normal;
     font-weight: 700;
     font-display: swap;
     src: url("/assets/fonts/OpenSans-700.woff2") format("woff2");
   }
   body { font-family: "Open Sans", system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; }
   ```
3. Entferne den Google Fonts `<link>`/`@import`.

**C) Es belassen, aber verhindern, dass die Anfrage fehlschlägt**

* Deaktiviere die blockierende Erweiterung für deine Seite oder lockere deine CSP, um `https://fonts.googleapis.com` und `https://fonts.gstatic.com` zu erlauben.
* Wenn du dich in einer Region befindest, in der diese Domains blockiert sind, sind Option A oder B vorzuziehen.

### Jekyll-spezifische Überschreibungs-Tipps

* **Remote-Theme:** Kopiere das `/_includes/head.html` oder `/_layouts/default.html` des Themes mit demselben Pfad in dein Repository, entferne die Google Fonts Zeile, und Jekyll wird deine überschriebene Version verwenden.
* **Minified Head Include:** Manchmal fügt das Theme die Fonts über eine Variable ein. Setze in diesem Fall diese Variable auf leer oder überschreibe das Include, um die Fonts auszuschließen.

Wenn du deinen Theme-Namen (oder deinen `_config.yml` `theme` / `remote_theme` Eintrag) postest, kann ich dir die genaue Datei zum Überschreiben und den minimalen Diff zeigen.