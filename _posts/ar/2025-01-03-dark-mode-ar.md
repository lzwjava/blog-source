---
audio: false
generated: false
lang: ar
layout: post
title: تنفيذ الوضع الداكن للموقع
translated: true
---

تنفيذ الوضع الداكن في مدونتي Jekyll.

## تبديل

```html
<script>
  const rootElement = document.documentElement;
  const themeToggleBtn = document.getElementById('themeToggle');
  const sunIcon = document.getElementById('sunIcon');
  const moonIcon = document.getElementById('moonIcon');
  const avatarImg = document.getElementById('avatarImg'); // مرجع إلى العنصر <img>
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
  // تجاوز لون الخلفية الرئيسي
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
    // إذا كنت بحاجة إلى خلفية أغمق
    background-image: linear-gradient(120deg, $dark-main-bg-color, #222);
    background-color: #2f2f2f !important;
    // أو اختر لونًا داكنًا مختلفًا، مثل #1f1f1f، #3a3a3a، إلخ.
}
```

```css
  // لون خلفية كتلة الكود (كان #e0d9cf)
  pre {
    background-color: #3a3a3a !important;
    // أو #2f2f2f، إلخ.
  }
```

```css
  // تجاوز لون التاريخ (كان رمادي داكن)
  .date {
    color: #aaa !important;
    // أو #ccc، #bbb، إلخ.
  }
```

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

```arabic
  // إلخ. - قم بتجاوزها حسب الحاجة
}
```

## بناء جملة Markdown

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

## صورة Markdown

```scss
.magnet-image {
  width: 300px;
  /* العرض الكامل على الشاشات الصغيرة */
  min-height: 300px;
  /* تعديل حسب الحاجة */
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
  <img src="/assets/images/magnet/magnet.jpg" alt="صورة المغناطيس">
</picture>
```