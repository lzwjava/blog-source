---
audio: true
lang: hant
layout: post
title: 网站暗黑模式实现
---

我的Jekyll博客中的暗黑模式实现。

## 切换

```html
<script>
  const rootElement = document.documentElement;
  const themeToggleBtn = document.getElementById('themeToggle');
  const sunIcon = document.getElementById('sunIcon');
  const moonIcon = document.getElementById('moonIcon');
  const avatarImg = document.getElementById('avatarImg'); // 引用到 <img> 元素
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

更新图标和头像();

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
  // 覆蓋你的主要背景顏色
  body {
    background-color: $dark-main-bg-color;
    color: white;
  }
```

.main-content {
    background-color: $dark-main-bg-color;
}

h6,
blockquote {
  color: $dark-section-headings-color;
}

```css
a {
  color: white !important;
}
```

```css
.page-header {
    // 如果需要更暗的背景
    background-image: linear-gradient(120deg, $dark-main-bg-color, #222);
    background-color: #2f2f2f !important;
    // 或者选择其他深色，例如 #1f1f1f, #3a3a3a 等
}
```

  // 代码块背景颜色（原为 #e0d9cf）
  pre {
    background-color: #3a3a3a !important;
    // 或者 #2f2f2f 等
  }

  // 日期颜色覆盖（原为深灰色）
  .date {
    color: #aaa !important;
    // 或者 #ccc, #bbb, 等等
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

这段代码的意思是，所有位于 `.main-content` 类下的标题元素（`h1` 到 `h6`）的文本颜色将被设置为变量 `$dark-section-link-color` 所定义的颜色值。

```csharp
// 等等 - 根据需要重写
}
```

## Markdown 语法

```scss
@import "語法";
@import "暗色語法";
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
```
```

## Markdown 图片

```scss
.magnet-image {
  width: 300px;
  /* 在小屏幕上全宽显示 */
  min-height: 300px;
  /* 根据需要调整 */
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
  <img src="/assets/images/magnet/magnet.jpg" alt="磁鐵圖片">
</picture>
```