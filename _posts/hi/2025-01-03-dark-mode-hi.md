---
audio: false
generated: false
lang: hi
layout: post
title: वेबसाइट डार्क मोड कार्यान्वयन
translated: true
---

मेरे Jekyll ब्लॉग में डार्क मोड का कार्यान्वयन।

## टॉगल

```html
<script>
  const rootElement = document.documentElement;
  const themeToggleBtn = document.getElementById('themeToggle');
  const sunIcon = document.getElementById('sunIcon');
  const moonIcon = document.getElementById('moonIcon');
  const avatarImg = document.getElementById('avatarImg'); // <img> का संदर्भ
```

```javascript
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme === 'dark') {
    rootElement.classList.add('dark-mode');
  }
```

  function updateIconsAndAvatar() {
    const isDark = rootElement.classList.contains('dark-mode');
    sunIcon.style.display = isDark ? 'inline-block' : 'none';
    moonIcon.style.display = isDark ? 'none' : 'inline-block';
    avatarImg.src = isDark
      ? '/assets/images/avatar_dark.png'
      : '/assets/images/avatar.jpg';
  }

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
  // अपने मुख्य बैकग्राउंड रंग को ओवरराइड करें
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
    // यदि आपको गहरा पृष्ठभूमि चाहिए
    background-image: linear-gradient(120deg, $dark-main-bg-color, #222);
    background-color: #2f2f2f !important;
    // या कोई अन्य गहरा रंग चुनें, जैसे #1f1f1f, #3a3a3a, आदि।
}
```

```css
  // Pre/code block की पृष्ठभूमि रंग (पहले #e0d9cf था)
  pre {
    background-color: #3a3a3a !important;
    // या #2f2f2f, आदि।
  }
```

  // दिनांक रंग ओवरराइड (पहले darkgray था)
  .date {
    color: #aaa !important;
    // या #ccc, #bbb, आदि।
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

यह CSS कोड `.main-content` क्लास के अंदर सभी हेडिंग टैग्स (`h1`, `h2`, `h3`, `h4`, `h5`, `h6`) के टेक्स्ट का रंग `$dark-section-link-color` वेरिएबल द्वारा निर्धारित करता है।

```javascript
// आदि - आवश्यकतानुसार ओवरराइड करें
}
```

## मार्कडाउन सिंटैक्स

```scss
@import "syntax";
@import "syntax-dark";
```

(यह कोड ब्लॉक है, इसे अनुवादित नहीं किया जाना चाहिए।)

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

## मार्कडाउन इमेज

```scss
.magnet-image {
  width: 300px;
  /* छोटे स्क्रीन पर पूरी चौड़ाई */
  min-height: 300px;
  /* आवश्यकतानुसार समायोजित करें */
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
  <img src="/assets/images/magnet/magnet.jpg" alt="चुंबक छवि">
</picture>
```