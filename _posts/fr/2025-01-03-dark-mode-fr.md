---
audio: false
generated: false
lang: fr
layout: post
title: Implémentation du Mode Sombre sur un Site Web
translated: true
---

Implémentation du mode sombre sur mon blog Jekyll.

## Basculer

```html
<script>
  const rootElement = document.documentElement;
  const themeToggleBtn = document.getElementById('themeToggle');
  const sunIcon = document.getElementById('sunIcon');
  const moonIcon = document.getElementById('moonIcon');
  const avatarImg = document.getElementById('avatarImg'); // référence à l'élément <img>
```

```javascript
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'dark') {
  rootElement.classList.add('dark-mode');
}
```

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
  // Remplacez votre couleur de fond principale
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
  }
```

```css
.page-header {
    // Si vous avez besoin d'un fond plus sombre
    background-image: linear-gradient(120deg, $dark-main-bg-color, #222);
    background-color: #2f2f2f !important;
    // Ou choisissez une autre couleur sombre, par exemple, #1f1f1f, #3a3a3a, etc.
}
```

  // Couleur de fond du bloc pre/code (était #e0d9cf)
  pre {
    background-color: #3a3a3a !important;
    // ou #2f2f2f, etc.
  }

  // Remplacement de la couleur de la date (était darkgray)
  .date {
    color: #aaa !important;
    // ou #ccc, #bbb, etc.
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

```javascript
// etc. - à remplacer selon les besoins
}
```

## Syntaxe Markdown

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

## Image en Markdown

```scss
.magnet-image {
  width: 300px;
  /* Pleine largeur sur les petits écrans */
  min-height: 300px;
  /* Ajustez selon les besoins */
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
  <img src="/assets/images/magnet/magnet.jpg" alt="Image de Magnet">
</picture>
```