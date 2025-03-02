---
audio: false
generated: false
lang: hant
layout: post
title: 網站深色模式實施
translated: true
---

在我的Jekyll博客中實現暗黑模式。

## 切換按鈕

```html
<script>
  const rootElement = document.documentElement;
  const themeToggleBtn = document.getElementById('themeToggle');
  const sunIcon = document.getElementById('sunIcon');
  const moonIcon = document.getElementById('moonIcon');
  const avatarImg = document.getElementById('avatarImg'); // 引用<img>元素

  const savedTheme = localStorage.getItem('theme');
  if (savedTheme === 'dark') {
    rootElement.classList.add('dark-mode');
  }

  function updateIconsAndAvatar() {
    const isDark = rootElement.classList.contains('dark-mode');
    sunIcon.style.display = isDark ? 'inline-block' : 'none';
    moonIcon.style.display = isDark ? 'none' : 'inline-block';
    avatarImg.src = isDark
      ? '/assets/images/avatar_dark.png'
      : '/assets/images/avatar.jpg';
  }

  updateIconsAndAvatar();

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
  // 覆蓋主要背景顏色
  body {
    background-color: $dark-main-bg-color;
    color: white;
  }

  .main-content {
    background-color: $dark-main-bg-color;

    h6,
    blockquote {
      color: $dark-section-headings-color;
    }

    a {
      color: white !important;
    }
  }

  .page-header {
    // 如果需要更暗的背景
    background-image: linear-gradient(120deg, $dark-main-bg-color, #222);
    background-color: #2f2f2f !important;
    // 或者選擇不同的暗色，例如 #1f1f1f, #3a3a3a, 等等
  }

  // 預格式/代碼塊背景顏色（原為 #e0d9cf）
  pre {
    background-color: #3a3a3a !important;
    // 或者 #2f2f2f, 等等
  }

  // 日期顏色覆蓋（原為 darkgray）
  .date {
    color: #aaa !important;
    // 或者 #ccc, #bbb, 等等
  }

  .main-content h1,
  .main-content h2,
  .main-content h3,
  .main-content h4,
  .main-content h5,
  .main-content h6 {
    color: $dark-section-link-color;
  }

  // 等等 - 根據需要覆蓋
}
```

## Markdown 語法

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

      pre {
        margin: 0;
      }
    }

    color: $color_1;
    background-color: $background-color_1;

    .w {
      color: $color_1;
      background-color: $background-color_1;
    }
  }
}
```

## Markdown 圖片

```scss
.magnet-image {
  width: 300px;
  /* 小屏幕上全寬 */
  min-height: 300px;
  /* 根據需要調整 */
  background-image: url('/assets/images/magnet/magnet.jpg');
  background-size: cover;
}

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