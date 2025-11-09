---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 現代網頁風格與版面設計
translated: true
type: note
---

### 概述
這是一段使用 SCSS (Sass) 語法編寫的 CSS 代碼，具有嵌套結構、用於偽類的 & 選擇器以及 @extend 指令。它定義了基本網頁佈局、表單、按鈕和實用工具的樣式，呈現出簡潔現代的視覺效果（例如圓角、柔和陰影、懸停過渡效果）。不帶單位的屬性（如 `font-size 16px`）是 SCSS 的簡寫形式。我將按部分進行解析，說明選擇器及其效果。

### 全域樣式 (html, body)
```css
html, body
  font-family Verdana
  font-size 16px
  height 100%
  background-color #D2D2D2
```
- 應用簡單的字體堆疊（Verdana 作為備選字體），大小為 16px。
- 設定 100% 高度以實現全頁面佈局，通常用於居中或覆蓋整個視口。
- 背景為淺灰色 (#D2D2D2)，作為中性基調色。

### 列表與連結樣式 (ul, a)
```css
ul
  list-style-type none
  padding 0
  margin 0

a
  color #000
  cursor pointer
  text-decoration none
```
- 移除無序列表的預設項目符號、內邊距和外邊距，實現更簡潔的自定義樣式。
- 連結為黑色 (#000)，懸停時顯示指標游標，且無底線，使其外觀類似按鈕。

### 顏色與文字實用工具 (.a-blue)
```css
.a-blue
  color #00BDEF
```
- 用於藍色文字 (#00BDEF，一種淺藍色) 的類別，通常用於強調。

### 按鈕樣式 (.btn, .btn-blue, .btn-gray, .btn-gray-2)
```css
.btn
  border-radius 3px
  padding 10px

.btn-blue
  background #00BDEF
  color #fff
  -webkit-box-shadow 0px 1px 0px rgba(255,255,255,0.15) inset,0px 1px 2px rgba(0,0,0,0.15)
  box-shadow 0px 1px 0px rgba(255,255,255,0.15) inset,0px 1px 2px rgba(0,0,0,0.15)
  &:hover
    background #00ABD8
    transition .5s

.btn-gray
  background #eee
  color #333
  border 1px solid #d5d5d5
  border-radius 3px
  -webkit-box-shadow 0px 1px 0px rgba(255,255,255,0.15) inset,0px 1px 2px rgba(0,0,0,0.15)
  box-shadow 0px 1px 0px rgba(255,255,255,0.15) inset,0px 1px 2px rgba(0,0,0,0.15)
  &:hover
    background #ddd
    transition 0.5s

.btn-gray-2
  background #eee
  color #333
  border 1px solid #d5d5d5
  border-radius 3px
  &:hover
    background #ddd
    transition 0.5s
```
- `.btn` 是基礎類別，用於設定 3px 圓角和 10px 內邊距。
- `.btn-blue`：藍色按鈕（背景 #00BDEF，白色文字），具有內嵌高光和投影以增加立體感。懸停時藍色變深，並帶有流暢的 0.5 秒過渡效果。
- `.btn-gray` 和 `.btn-gray-2`：灰色按鈕（淺背景 #eee，深色文字 #333，細邊框 #d5d5d5），具有類似的陰影效果。`.btn-gray-2` 沒有明確的 box-shadow，但具有相同的懸停效果（變亮為 #ddd）。適用於次要操作。

### 定位實用工具 (.absolute-center, .full-space)
```css
.absolute-center
    margin auto
    position absolute
    top 0
    left 0
    bottom 0
    right 0

.full-space
    position absolute
    top 0
    left 0
    bottom 0
    right 0
```
- `.absolute-center`：將元素在其父容器中絕對居中（上下左右均為 0，並使用自動外邊距）。
- `.full-space`：使元素絕對定位並填滿其父容器的整個空間。

### 表單樣式 (.base-form, input/textarea/select, button)
```css
.base-form
  @extend .absolute-center
  max-width 350px
  height 400px
  background #fff
  border-radius 20px
  text-align center
  padding 20px 10px

input, textarea, select
  box-sizing border-box
  border none
  outline none
  &:focus
    border none
    outline none
    box-shadow 0px 1px 4px 0px rgba(0,0,0,.06)
    -webkit-box-shadow 0px 1px 4px 0px rgba(0,0,0,.06)

button
  border-style none
  outline none
```
- `.base-form`：繼承 `.absolute-center` 以居中顯示模態表單（最大寬度 350px，高度 400px，白色背景，20px 圓角，文字居中，內部內邊距）。適合用於登入/註冊表單。
- 輸入框、文字區域、下拉選單：無邊框，並使用 box-sizing 將內邊距包含在寬度內；聚焦時無外框線，但添加細微的灰色陰影以提升使用者體驗。
- 按鈕：移除預設邊框和外框線，假設使用 `.btn` 樣式來美化外觀。

此代碼建立了一個響應式、居中的表單頁面，並具有風格化的按鈕和輸入框。若使用 SCSS，請編譯為標準 CSS。如需自定義，可根據需要調整顏色或尺寸。