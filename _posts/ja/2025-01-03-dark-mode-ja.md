---
audio: false
generated: false
image: true
lang: ja
layout: post
title: ウェブサイトのダークモード実装
translated: true
type: post
---

私のJekyllブログでのダークモード実装。

## トグル

```html
<script>
  const rootElement = document.documentElement;
  const themeToggleBtn = document.getElementById('themeToggle');
  const sunIcon = document.getElementById('sunIcon');
  const moonIcon = document.getElementById('moonIcon');
  const avatarImg = document.getElementById('avatarImg'); // <img>要素への参照
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

この関数は、ダークモードが有効かどうかを確認し、それに応じてアイコンとアバター画像を更新します。ダークモードが有効な場合、太陽アイコンを表示し、月アイコンを非表示にします。また、アバター画像をダークモード用の画像に切り替えます。ダークモードが無効な場合は、その逆の動作を行います。

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
  // メインの背景色を上書き
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
    // より暗い背景が必要な場合
    background-image: linear-gradient(120deg, $dark-main-bg-color, #222);
    background-color: #2f2f2f !important;
    // または、別の暗い色を選択してください。例: #1f1f1f, #3a3a3a など
}
```

  // Pre/codeブロックの背景色（以前は#e0d9cf）
  pre {
    background-color: #3a3a3a !important;
    // または#2f2f2fなど
  }

```css
  // 日付の色を上書き（以前はdarkgray）
  .date {
    color: #aaa !important;
    // または #ccc, #bbb, など
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

このCSSコードは、`.main-content`クラス内のすべての見出し要素（`h1`から`h6`まで）のテキスト色を、変数`$dark-section-link-color`で定義された色に設定しています。

```javascript
// などなど - 必要に応じてオーバーライドする
}
```

## Markdown 構文

```scss
@import "syntax";
@import "syntax-dark";
```

このコードは、Sass（SCSS）ファイルで2つのスタイルシートをインポートしています。`syntax`と`syntax-dark`という名前のスタイルシートを読み込んでいます。これらのファイルは、おそらくコードのシンタックスハイライトに関連するスタイルを定義しているものと思われます。`syntax`は通常のシンタックスハイライト用で、`syntax-dark`はダークテーマ用のシンタックスハイライト用のスタイルを提供していると考えられます。

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

```scss
color: $color_1;
background-color: $background-color_1;
```

```css
.w {
  color: $color_1;
  background-color: $background-color_1;
}
```
```

## Markdown 画像

```scss
.magnet-image {
  width: 300px;
  /* 小さな画面では全幅表示 */
  min-height: 300px;
  /* 必要に応じて調整 */
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
  <img src="/assets/images/magnet/magnet.jpg" alt="磁石の画像">
</picture>
```