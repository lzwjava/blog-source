---
audio: false
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: Jekyll CSSキャッシュ防止対策
translated: true
type: note
---

現在表示されているのは、Jekyll（テーマまたは`jekyll-assets`/`jekyll-feed`/`minima`パイプライン経由）がキャッシュ対策として、スタイルシートのURLに自動的に**フィンガープリント（ハッシュ）**を追加しているためです。これが、同じCSSファイルがリビルドされるたびに異なる`?v=...`クエリ文字列で表示される理由です。

Jekyllがビルドのたびにこのクエリ文字列を変更しないようにしたい場合は、「キャッシュ対策」/「ダイジェスト」動作を無効化または上書きできます：

### オプション1. 固定リンクを使用する

Jekyllのヘルパータグ（例：`{{ "/assets/css/style.css" | relative_url }}` または `{{ "/assets/css/style.css" | asset_path }}`）の代わりに、直接ハードコードします：

```html
<link rel="stylesheet" href="/assets/css/style.css">
```

この方法では、フィンガープリントは注入されません。

### オプション2. アセットダイジェストを無効にする

**jekyll-assets**またはファイルのフィンガープリントを行うテーマを使用している場合は、`_config.yml`でダイジェストを無効にできます：

```yml
assets:
  digest: false
```

### オプション3. ダイジェストなしで`relative_url`を使用する

テーマが以下のようなコードを使用している場合：

```liquid
<link rel="stylesheet" href="{{ '/assets/css/style.css' | relative_url }}">
```

ダイジェストが有効な`asset_path`や`absolute_url`を通してパイプしていないことを確認してください。単に`relative_url`を使用します。

---

👉 要約：

* **絶対に変更されたくない**場合は、パスをハードコードしてください。
* 設定で制御したい場合は、`assets.digest: false`を設定してください。
* バージョニングは維持したいが安定させたい場合は、自身で`?v=...`を手動で管理する必要があります。

**完全に静的**（決して変更されない）にしたいですか？それとも、Jekyllが**ビルドのたびに新しいハッシュを生成するのを止め**たいだけですか？