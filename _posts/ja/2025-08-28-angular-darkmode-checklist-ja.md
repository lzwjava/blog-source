---
audio: false
generated: true
image: false
lang: ja
layout: post
title: アンギュラーダークモード要素チェックリスト
translated: true
type: note
---

Angularフロントエンドでダークモードを実装する際、通常は`body`、`select`、`option`から始めますが、テーマの一貫性を保つためにスタイルを変更すべき一般的なHTML要素は他にも数多くあります。以下は実践的なチェックリストです：

### ページレベルとコンテナ

* `html`、`body` → 背景色と文字色
* `div`、`section`、`article`、`aside`、`header`、`footer`、`main`、`nav` → 背景色と文字色の設定（特にデフォルトで白背景を持つ場合）

### テキストと見出し

* `h1, h2, h3, h4, h5, h6` → ダーク背景に対して文字が可視であることを確認
* `p`、`span`、`a` → 文字色、リンクのホバー色、訪問済みリンクの状態を調整

### フォームと入力要素

* `input[type="text"]`、`input[type="password"]`、`input[type="email"]`、`textarea` → 背景、文字色、ボーダー
* `input[type="checkbox"]`、`input[type="radio"]` → 可視性のために特別な処理が必要な場合あり
* `select`、`option` → 前述の通り、背景色と文字色の両方
* `button` → 背景、ボーダー、文字色、さらにホバー/アクティブ状態
* `label` → ダーク背景と対比する文字色を確保
* `fieldset`、`legend` → 背景とボーダー

### リストとテーブル

* `ul`、`ol`、`li` → 文字色
* `table` → 背景、ボーダー色、文字色
* `thead`、`tbody`、`tr`、`th`、`td` → 背景とボーダーの個別調整

### インタラクティブ要素

* `details`、`summary` → 背景と文字
* `dialog` → 背景と文字
* `mark` → ダーク背景でも機能するハイライト色（デフォルトの黄色は明るすぎる場合あり）

### メディアとその他

* `hr` → ボーダー色（デフォルトはダーク背景では明るすぎることが多い）
* `code`、`pre` → 可読性のための背景と文字色
* `blockquote` → 背景とボーダー色
* `progress`、`meter` → トラックと値の色

---

💡 **ベストプラクティス**: すべてに`!important`を使用する代わりに、色用のCSS変数（`--bg-color`、`--text-color`など）を定義し、ダークモードがアクティブになったときにそれらを交換します（例：`body`に`.dark-mode`クラスを追加）。これにより、Angularコンポーネントやカスタム要素もテーマにクリーンに組み込むことができます。

**ベースCSSスニペット**（変数付き）を草案して、Angularプロジェクトの開始点として使用できるようにしましょうか？