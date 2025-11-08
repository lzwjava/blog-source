---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 風格化代碼審查平台
translated: true
type: post
---

當建立現代化的網頁應用程式時，樣式設計不僅僅是讓東西看起來好看——它關乎於創造直觀、響應式和引人入勝的用戶體驗。我最近探索了一個基於 Vue.js 的代碼審查平台的 Stylus 樣式表，其 CSS 架構是技術的寶庫，值得深入探討。讓我們深入了解這個應用如何使用 Stylus 來打造其精緻的 UI，從佈局結構到懸停效果，同時保持代碼的可維護性和可擴展性。

## 為什麼選擇 Stylus？快速入門

Stylus 是一個 CSS 預處理器，它去除了傳統 CSS 的冗長（不需要大括號或分號），並添加了強大的功能，如變量、混合（mixins）和嵌套。提供的代碼從 `variables.styl` 導入變量，從 `base.styl` 導入基礎樣式表，為一致且可重用的樣式打下基礎。例如，主色 `#1CB2EF` 可能在 `variables.styl` 中定義，並在按鈕和背景中重複使用。

## 佈局結構：區段和容器

應用的首頁分為不同的區段——`.slide`、`.feature`、`.reviewer`、`.example` 和 `.contact`，每個區段都有自己的樣式策略。以下是 `.slide`（英雄區段）的樣式：

```stylus
.slide
  height 800px
  position relative
  color #fff
  width 100%
  overflow hidden
  .bg
    background url("../img/home/hero.jpg") no-repeat
    background-size cover
    background-position-y 40%
    position 200% 200%
    width 100%
    height 100%
    padding-top 280px
```

### 關鍵技術：
- **全屏英雄區段**：`height 800px` 和 `width 100%` 創建了一個大膽的全寬橫幅。`overflow hidden` 確保沒有內容溢出。
- **背景圖片**：`.bg` 類使用 `background-size cover` 將英雄圖片按比例縮放，而 `background-position-y 40%` 微調其垂直對齊以達到視覺效果。
- **嵌套**：Stylus 的嵌套將相關樣式分組，提高了可讀性，比平面 CSS 更好。

## 响應式網格：Flexbox 和 clearfix

`.feature` 區段展示了一個三列佈局：

```stylus
.feature
  height 450px
  padding 125px 0
  background white
  .list
    width 1160px
    margin 0 auto
    display flex
    flex-direction row
    li
      height 200px
      padding-left 50px
      flex-grow 1
      &:first-child
        padding-left 0
      .short
        width 235px
        height 200px
        margin 0 auto
```

### 亮點：
- **Flexbox**：`display flex` 和 `flex-direction row` 將列表項目水平對齊，而 `flex-grow 1` 確保它們均勻擴展以填充容器。
- **居中**：`width 1160px` 配合 `margin 0 auto` 將內容居中，這是固定寬度佈局的經典技術。
- **偽類魔法**：`&:first-child` 選擇器從第一個項目中移除填充，防止不合適的間距。

`.example` 區段進一步使用了審查卡片的網格，使用 `clearfix()` 混合：

```stylus
.example
  .list
    clearfix()
    .row
      clearfix()
      li:first-child
        margin-left 0
    li
      height 354px
      margin-left 48px
      pull-left()
      margin-bottom 48px
```

- **Clearfix**：這個混合（可能在 `base.styl` 中定義）處理浮動清除，確保行在舊瀏覽器或自定義佈局中正確堆疊。
- **浮動網格**：`pull-left()`（另一個實用混合）將項目浮動到左邊，`margin-left 48px` 添加間距。這種方法與 Flexbox 相輔相成，以實現更廣泛的兼容性。

## 互動樣式：懸停效果和過渡

`.example` 中的審查卡片在平滑的懸停交互中閃耀：

```stylus
li
  .info
    position relative
    height 354px
    width 100%
    color white
    box-shadow 0 4px 4px 1px rgba(135,135,135,.1)
    overflow hidden
    cursor pointer
    &:hover
      img
        transform scale(1.2,1.2)
        -webkit-filter brightness(0.6)
      .title
        -webkit-transform translate(0, -20px)
        opacity 1.0
      .tips
        -webkit-transform translate(0, -10px)
        opacity 0.8
    img
      height 100%
      -webkit-filter brightness(0.4)
      transition all 0.35s ease 0s
```

### 分解：
- **懸停效果**：懸停時，圖片放大（`transform scale(1.2,1.2)`）並變亮（`-webkit-filter brightness(0.6)`），而文本元素向上移動並調整不透明度。
- **過渡**：`transition all 0.35s ease 0s` 確保所有屬性的平滑動畫，持續時間為 350 毫秒，帶有緩動曲線。
- **分層**：`.text` 的 `position absolute` 將其定位在圖片上方，`z-index 2` 確保其可見性。

`.author` 按鈕也有反應：

```stylus
.author
  position absolute
  background black
  margin-left 30px
  margin-top 30px
  height 30px
  padding-left 20px
  padding-right 20px
  transition all 0.35s ease 0s
  &:hover
    background #1cb2ef
```

簡單的顏色從黑色變為品牌色 `#1CB2EF` 的懸停效果，增加了愉快的觸感。

## 視覺精緻：陰影、按鈕和圖標

陰影增強了深度，如 `.info` 的 `box-shadow 0 4px 4px 1px rgba(135,135,135,.1)`。按鈕，如 `.contact` 中的按鈕，經過精心設計：

```stylus
.contact
  .rightbtn
    .more
      width 127px
      height 50px
      color #1CB2EF
      background white
      border-radius 3px
      border 1px solid #00A3E6
      -webkit-box-shadow 0px 1px 0px rgba(255,255,255,0.15) inset, 0px 1px 2px rgba(0,0,0,0.15)
```

- **內陰影**：微妙的內陰影（`inset`）與外陰影相結合，創建了一個按下按鈕的效果。
- **一致性**：邊框顏色 `#00A3E6` 與品牌調色板相一致。

圖標，如 `.icon_crown`，使用背景圖片：

```stylus
.icon_crown
  background url("../img/icon/crown@2x.png") no-repeat
  background-size contain
  width 49px
  height 52px
```

`@2x` 後綴表示 Retina 友好的資產，`background-size contain` 確保適當縮放。

## 最佳實踐和心得

這個 Stylus 實現為任何 CSS 項目提供了教訓：
1. **使用預處理器**：Stylus 的嵌套和混合（例如 `clearfix()`）簡化了複雜的佈局。
2. **平衡佈局**：結合 Flexbox 以適應現代瀏覽器，並使用浮動作為備用方案，以實現穩健性。
3. **增強 UX**：平滑的過渡和懸停效果使 UI 看起來更生動。
4. **保持可維護性**：利用變量和導入以在大型代碼庫中保持一致性。

無論你是為代碼審查平台還是個人作品集進行樣式設計，這些技術都可以提升你的 CSS 水平。下次寫樣式表時，考慮如何使用嵌套、過渡和一點陰影來轉變你的設計！