---
audio: false
generated: false
lang: ja
layout: post
title: スタイル付けされたコードレビュープラットフォーム
translated: true
---

モダンなウェブアプリケーションを構築する際、スタイリングは見た目を良くするだけでなく、直感的でレスポンシブで魅力的なユーザーエクスペリエンスを作り出すことです。最近、Vue.jsで動作するコードレビュープラットフォームのStylusベースのスタイルシートを探索しましたが、そのCSSアーキテクチャは、解きほぐす価値のあるテクニックの宝庫です。このアプリがStylusを使ってポリッシュされたUIを作り上げる方法、レイアウトの構造からホバー効果まで、コードを保守しやすくスケーラブルに保つ方法について、深掘りしてみましょう。

## Stylusの理由：簡単な概要

Stylusは、伝統的なCSSの冗長さを取り除き（カッコやセミコロンが不要）、変数、ミックスイン、ネストなどの強力な機能を追加するCSSプレプロセッサです。提供されたコードは、`variables.styl`から変数を、`base.styl`からベーススタイルシートをインポートしており、一貫性のある再利用可能なスタイルを設定する準備が整っています。例えば、主要な色 `#1CB2EF` は `variables.styl` で定義され、ボタンや背景で再利用されています。

## レイアウトの構造：セクションとコンテナ

アプリのホームページは、`.slide`、`.feature`、`.reviewer`、`.example`、`.contact` など、それぞれ独自のスタイリング戦略を持つセクションに分かれています。以下に、`.slide`（ヒーロー）セクションのスタイルが示されています。

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

### 主要なテクニック：
- **フルスクリーンヒーロー**：`height 800px` と `width 100%` は、太いフルウィドスバナーを作成し、`overflow hidden` はコンテンツが溢れないようにします。
- **背景画像**：`.bg` クラスは `background-size cover` を使ってヒーロー画像を比例的にスケーリングし、`background-position-y 40%` は視覚的な影響を高めるために垂直方向のアライメントを微調整します。
- **ネスト**：Stylusのネストは関連するスタイルをグループ化し、フラットなCSSに比べて可読性を向上させます。

## レスポンシブグリッド：Flexboxとclearfix

`.feature` セクションは、3列レイアウトを展示しています。

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

### ハイライト：
- **Flexbox**：`display flex` と `flex-direction row` はリストアイテムを水平に配置し、`flex-grow 1` はコンテナを均等に広げて填めます。
- **センタリング**：`width 1160px` と `margin 0 auto` はコンテンツを中央に配置し、固定幅レイアウトの古典的なテクニックです。
- **Pseudo-Classの魔法**：`&:first-child` セレクターは最初のアイテムのパディングを削除し、不自然なスペースを防ぎます。

`.example` セクションは、レビューカードのグリッドをさらに進化させ、`clearfix()` ミックスインを使用しています。

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

- **Clearfix**：このミックスイン（おそらく `base.styl` で定義されている）は、古いブラウザやカスタムレイアウトで行が適切にスタックするようにフロートをクリアします。
- **フロートベースのグリッド**：`pull-left()`（他のユーティリティミックスイン）はアイテムを左にフロートさせ、`margin-left 48px` はギャップを追加します。このアプローチは、より広範な互換性を持つFlexboxと相互に補完します。

## インタラクティブスタイリング：ホバー効果とトランジション

`.example` のレビューカードは、スムーズなホバーインタラクションで輝きます。

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
- **ホバー効果**：ホバー時に画像が拡大 (`transform scale(1.2,1.2)`) して明るくなり (`-webkit-filter brightness(0.6)`)、テキスト要素は `translate` で上にシフトし、不透明度を調整します。
- **トランジション**：`transition all 0.35s ease 0s` は、すべてのプロパティに対してスムーズなアニメーションを確保し、350msの期間とイージングカーブを持っています。
- **レイヤリング**：`.text` の `position absolute` は画像の上に配置し、`z-index 2` は可視性を確保します。

`.author` ボタンも反応します。

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

ホバー時にブランドカラー `#1CB2EF` に色を変えるシンプルな色のスワップは、素晴らしいタッチです。

## ビジュアルポリッシュ：シャドウ、ボタン、アイコン

シャドウは深さを強調し、`.info` の `box-shadow 0 4px 4px 1px rgba(135,135,135,.1)` で見られます。ボタン、例えば `.contact` のものも、細心の注意を払ってスタイル付けられています。

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

- **インセットシャドウ**：内側のシャドウ (`inset`) と外側のドロップシャドウを組み合わせることで、押されたボタンの効果が得られます。
- **一貫性**：ボーダーカラー `#00A3E6` はブランドパレットに一致しています。

アイコン、例えば `.icon_crown` は背景画像を使用します。

```stylus
.icon_crown
  background url("../img/icon/crown@2x.png") no-repeat
  background-size contain
  width 49px
  height 52px
```

`@2x` 接尾辞はレティナ対応のアセットを示し、`background-size contain` は適切なスケーリングを確保します。

## ベストプラクティスと学び

このStylusの実装は、どのCSSプロジェクトにも役立つ教訓を提供します：
1. **プレプロセッサを使用**：Stylusのネストとミックスイン（例えば `clearfix()`）は複雑なレイアウトを簡素化します。
2. **レイアウトのバランス**：Flexboxをモダンブラウザで、フロートベースのフォールバックを使用して、堅牢性を確保します。
3. **UXを向上**：スムーズなトランジションとホバー効果はUIを生き生きとさせます。
4. **保守性を保つ**：変数とインポートを活用して、大きなコードベースでの一貫性を保ちます。

コードレビュープラットフォームや個人のポートフォリオをスタイル付けする際でも、これらのテクニックはCSSのスキルを向上させることができます。次回スタイルシートを書く際には、ネスト、トランジション、そしてシャドウの少しのタッチがデザインを変える方法を考えてみてください！