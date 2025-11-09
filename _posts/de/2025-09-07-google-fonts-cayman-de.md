---
audio: false
date: 2025-09-07
generated: true
image: false
lang: de
layout: post
title: Google Fonts Import im Cayman-Theme
translated: true
type: note
---

Ja — das ist sehr wahrscheinlich der Grund.

Wenn du schreibst:

```scss
@import "jekyll-theme-cayman";
```

importierst du nicht nur lokales SCSS — du importierst das gesamte **Stylesheet des Themes**, welches selbst den Google Fonts Import enthält (oder darauf verweist). Cayman verwendet **Open Sans** als Standard-Schriftart und lädt sie von `https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap`.

Der Ablauf sieht also so aus:

1. Dein SCSS enthält `@import "jekyll-theme-cayman";`.
2. Jekyll erweitert dies in die `_sass`-Dateien des Themes.
3. In Caymans SCSS gibt es eine Zeile wie:

   ```scss
   @import url("https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap");
   ```
4. Das ist die Netzwerkanfrage, die du in den DevTools siehst.

---

### So entfernst oder überschreibst du es

* **Überschreibe den Font-Import**: Kopiere das Haupt-SCSS des Themes in dein Projekt (z.B. `assets/css/style.scss`), entferne die Google Fonts Zeile und weise Jekyll an, sie nicht zu importieren.

* **Überschreibe nur die Schriftartenfamilie**: Behalte den Rest von Cayman bei, erzwinge aber einen System Font Stack in deinem eigenen CSS:

  ```css
  html, body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Ubuntu,
                 "Helvetica Neue", Arial, "Noto Sans", sans-serif;
  }
  ```

  Selbst wenn die Google Fonts Anfrage stattfindet, wird der Browser sie nicht verwenden.

* **Open Sans selbst hosten**: Wenn dir Open Sans gefällt, du aber den externen Aufruf vermeiden willst, lade die Font-Dateien herunter und definiere sie mit `@font-face` in deinem eigenen CSS. Entferne dann den `@import url(...)` aus Cayman.

---

👉 Falls du möchtest, kann ich dir genau zeigen, welche Cayman SCSS-Datei die Google Fonts Zeile enthält und wie du sie in deinem Jekyll-Setup sauber überschreiben kannst. Soll ich das Schritt für Schritt durchgehen?