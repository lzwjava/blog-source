---
audio: false
generated: false
lang: es
layout: post
title: Implementación del Modo Oscuro en Sitios Web
translated: true
---

Implementación del Modo Oscuro en mi blog de Jekyll.

## Alternar

```html
<script>
  const rootElement = document.documentElement;
  const themeToggleBtn = document.getElementById('themeToggle');
  const sunIcon = document.getElementById('sunIcon');
  const moonIcon = document.getElementById('moonIcon');
  const avatarImg = document.getElementById('avatarImg'); // referencia a la etiqueta <img>
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

actualizarIconosYAvatar();

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
  // Sobrescribe el color de fondo principal
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
    // Si necesitas un fondo más oscuro
    background-image: linear-gradient(120deg, $dark-main-bg-color, #222);
    background-color: #2f2f2f !important;
    // O elige un color oscuro diferente, por ejemplo, #1f1f1f, #3a3a3a, etc.
}
```

  // Color de fondo del bloque pre/code (antes era #e0d9cf)
  pre {
    background-color: #3a3a3a !important;
    // o #2f2f2f, etc.
  }

  // Sobrescribir el color de la fecha (era gris oscuro)
  .date {
    color: #aaa !important;
    // o #ccc, #bbb, etc.
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
// etc. - sobrescribir según sea necesario
}
```

## Sintaxis de Markdown

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

## Imagen en Markdown

```scss
.magnet-image {
  width: 300px;
  /* Ancho completo en pantallas pequeñas */
  min-height: 300px;
  /* Ajustar según sea necesario */
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
  <img src="/assets/images/magnet/magnet.jpg" alt="Imagen de Magnet">
</picture>
```