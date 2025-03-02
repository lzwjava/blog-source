---
audio: false
generated: false
lang: de
layout: post
title: Implementierung des Dunkelmodus auf der Website
translated: true
---

Implementierung des Dark Mode in meinem Jekyll-Blog.

## Umschalten

```html
<script>
  const rootElement = document.documentElement;
  const themeToggleBtn = document.getElementById('themeToggle');
  const sunIcon = document.getElementById('sunIcon');
  const moonIcon = document.getElementById('moonIcon');
  const avatarImg = document.getElementById('avatarImg'); // Referenz auf das <img>-Element
```

  const savedTheme = localStorage.getItem('theme');
  if (savedTheme === 'dark') {
    rootElement.classList.add('dark-mode');
  }

```javascript
function updateIconsAndAvatar() {
    const isDark = rootElement.classList.contains('dark-mode');
    sunIcon.style.display = isDark ? 'inline-block' : 'none';
    moonIcon.style.display = isDark ? 'none' : 'inline-block';
    avatarImg.src = isDark
      ? '/assets/images/avatar_dark.png'
      : '/assets/images/avatar.jpg';
}
```

Übersetzung:

```javascript
function updateIconsAndAvatar() {
    const isDark = rootElement.classList.contains('dark-mode');
    sunIcon.style.display = isDark ? 'inline-block' : 'none';
    moonIcon.style.display = isDark ? 'none' : 'inline-block';
    avatarImg.src = isDark
      ? '/assets/images/avatar_dark.png'
      : '/assets/images/avatar.jpg';
}
```

Die Funktion `updateIconsAndAvatar` überprüft, ob das `rootElement` die Klasse `dark-mode` enthält. Abhängig davon, ob der Dark Mode aktiviert ist oder nicht, werden das Sonnen- und Mond-Icon sowie das Avatar-Bild entsprechend angepasst.

  updateIconsAndAvatar();

```javascript
themeToggleBtn.addEventListener('click', function () {
    rootElement.classList.toggle('dark-mode');
    if (rootElement.classList.contains('dark-mode')) {
      localStorage.setItem('theme', 'dark');
    } else {
      localStorage.setItem('theme', 'light');
    }
    updateIconsAndAvatar();
  });
</script>
```

## CSS

```scss
.dark-mode {
  // Überschreiben Sie Ihre Haupt-Hintergrundfarbe
  body {
    background-color: $dark-main-bg-color;
    color: white;
  }
```

```css
.main-content {
    background-color: $dark-main-bg-color;
}
```

```css
    h6,
    blockquote {
      color: $dark-section-headings-color;
    }
```

```css
a {
  color: white !important;
}
```

```css
.page-header {
    // Wenn Sie einen dunkleren Hintergrund benötigen
    background-image: linear-gradient(120deg, $dark-main-bg-color, #222);
    background-color: #2f2f2f !important;
    // Oder wählen Sie eine andere dunkle Farbe, z.B. #1f1f1f, #3a3a3a, usw.
}
```

  // Hintergrundfarbe für Pre/Code-Blöcke (war #e0d9cf)
  pre {
    background-color: #3a3a3a !important;
    // oder #2f2f2f, etc.
  }

  // Überschreiben der Datumsfarbe (war dunkelgrau)
  .date {
    color: #aaa !important;
    // oder #ccc, #bbb, etc.
  }

```css
.main-content h1,
.main-content h2,
.main-content h3,
.main-content h4,
.main-content h5,
.main-content h6 {
  color: $dark-section-link-color;
}
```

  // usw. - nach Bedarf überschreiben
}
```

## Markdown-Syntax

```scss
@import "syntax";
@import "syntax-dark";
```

```scss
.dark-mode {
  .highlight {
    table {
      td {
        padding: 5px;
      }
```

```css
pre {
  margin: 0;
}
```

```css
color: $color_1;
background-color: $background-color_1;
```

```css
.w {
  color: $color_1;
  background-color: $background-color_1;
}
}
}
```

## Markdown-Bild

```scss
.magnet-image {
  width: 300px;
  /* Volle Breite auf kleinen Bildschirmen */
  min-height: 300px;
  /* Nach Bedarf anpassen */
  background-image: url('/assets/images/magnet/magnet.jpg');
  background-size: cover;
}
```

```css
.dark-mode .magnet-image {
  background-image: url('/assets/images/magnet/magnet_dark.jpg');
}
```

```html
<picture>
  <source srcset="/assets/images/magnet/magnet_dark.jpg" media="(prefers-color-scheme: dark)">
  <img src="/assets/images/magnet/magnet.jpg" alt="Magnet Bild">
</picture>
```