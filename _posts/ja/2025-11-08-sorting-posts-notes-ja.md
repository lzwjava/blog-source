---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 投稿とノートの並べ替え
translated: true
type: note
---

### 修正された `_includes/sort.html`

既存の `sort.html` は9つのオプションを持つ言語選択機能を備えており、これは完璧です。大きな変更は必要ありませんが、`<span id="post-number">` をより汎用的な表現（例：「投稿」ではなく「エントリー」）に微調整しました。これは、ノートも含まれるようになったためです。必要に応じて、あなたのJSで動的に更新できます。以下が調整後のバージョンです：

```html
<div class="sort-container">
  <span id="post-number" class="post-number">
    {{ site.posts.size | plus: site.notes.size }} エントリー
    ({{ site.posts.size | plus: site.notes.size | divided_by: 7 | times: 6 }} Translated by <a href="https://openrouter.ai">AI</a>)
  </span>
  <select id="sort-select">
    <option value="en" selected>English</option>
    <option value="zh">中文</option>
    <option value="ja">日本語</option>
    <option value="es">Español</option>
    <option value="hi">हिंदी</option>
    <option value="fr">Français</option>
    <option value="de">Deutsch</option>
    <option value="ar">العربية</option>
    <option value="hant">繁體中文</option>
  </select>
</div>
```

**主な変更点**: カウントを `site.notes.size` を含むように更新しました（これについては後述します）。計算式は同じですが、ノートも考慮するようになりました。もしあなたのJS (`index.js`) が、表示されているアイテムに基づいてこの span を動的に更新するようになっていれば、言語固有のカウントも自動的に処理するでしょう。

### Step 1: Jekyll コレクションとしてのノートを設定 (`_config.yml` 内)

`_notes` を `_posts` と同様に扱う（つまり、Jekyll が Markdown ファイルを処理し、`site.notes` を通じて公開する）ために、これを `_config.yml` に追加します。これは必須です。これがないと、ノートは投稿のように `url`、`title`、`date` などを持ちません。

```yaml
collections:
  notes:
    output: true
    permalink: /notes/:path/
```

- `output: true` はノートのページを生成します（データのみが必要な場合はオプション）。
- `permalink` は `/notes/es/2025-11-07-tidb-vs-cockroachdb-es/` のようなURLを保証します（必要に応じて調整してください）。
- これを追加した後は、Jekyll サーバーを再起動してください。

これで `site.notes` は `site.posts` と同様に機能します。ただし、ノートファイル（例: `_notes/es/2025-11-07-tidb-vs-cockroachdb-es.md`）が同様の frontmatter (`title:`、`date:`、`image:`、`top:`、`translated:`、`generated:`) を持っていることを前提としています。

### Step 2: 修正されたページレイアウト (例: `index.md` または `<ul class="post-list">` がある場所)

現在のループは英語の投稿のみを表示しています。ノートを追加し、9つの言語すべてをサポートするには：

- 言語リストを一度定義します。
- **すべての**言語をループ処理します。
- 各言語について、一致する**投稿**（`_posts/{lang}/` から）と**ノート**（`_notes/{lang}/` から）を `<li>` アイテムとして追加します。
- 各 `<li>` に `class="... lang-{lang}"` を付与し、あなたのJSがそれらをフィルタリングできるようにします（例: `#sort-select` の値に基づいて表示/非表示）。
- これによりリスト全体が事前に構築され（JSによって非表示）、その後、言語が動的に切り替わります。
- 日付でソートしますか？新しい順にしたい場合は、ループに `| sort: 'date' | reverse` を追加してください（日付が比較可能であることを前提としています）。

以下が完全に更新されたレイアウトです：

```html
---
layout: page
---
{% include sort.html %}

<ul class="post-list">
  {% if site.posts.size == 0 and site.notes.size == 0 %}
    <li class="list-group-item post-item">利用可能なエントリーはありません。</li>
  {% else %}
    {% assign langs = "en,zh,ja,es,hi,fr,de,ar,hant" | split: "," %}
    {% for lang in langs %}
      {% comment %} この言語の投稿 {% endcomment %}
      {% for post in site.posts | sort: 'date' | reverse %}
        {% if post.path contains "_posts/{{ lang }}/" %}
          {% assign translated = post.translated %}
          {% assign generated = post.generated %}
          {% if translated == nil %}{% assign translated = false %}{% endif %}
          {% if generated == nil %}{% assign generated = false %}{% endif %}
          <li class="list-group-item post-item lang-{{ lang }}" data-top="{{ post.top }}" data-translated="{{ translated }}" data-generated="{{ generated }}">
            <a href="{{ post.url }}">
              <span class="date">{{ post.date | date: "%Y.%m.%d" }}</span>
              <span class="type">{% if post.image %}image{% else %}text{% endif %}</span>
              <span class="title">{{ post.title }}</span>
            </a>
          </li>
        {% endif %}
      {% endfor %}

      {% comment %} この言語のノート (投稿と同様) {% endcomment %}
      {% for note in site.notes | sort: 'date' | reverse %}
        {% if note.path contains "_notes/{{ lang }}/" %}
          {% assign translated = note.translated %}
          {% assign generated = note.generated %}
          {% if translated == nil %}{% assign translated = false %}{% endif %}
          {% if generated == nil %}{% assign generated = false %}{% endif %}
          <li class="list-group-item post-item lang-{{ lang }}" data-top="{{ note.top }}" data-translated="{{ translated }}" data-generated="{{ generated }}">
            <a href="{{ note.url }}">
              <span class="date">{{ note.date | date: "%Y.%m.%d" }}</span>
              <span class="type">{% if note.image %}image{% else %}text{% endif %}</span>
              <span class="title">{{ note.title }}</span>
            </a>
          </li>
        {% endif %}
      {% endfor %}
    {% endfor %}
  {% endif %}
</ul>

{% include footer.html %}
<script src="/assets/js/index.js"></script>
```

**主な変更点**:
- **言語配列**: `{% assign langs = "en,zh,ja,es,hi,fr,de,ar,hant" | split: "," %}` — あなたのセレクトボックスのオプションと一致します。メンテナンスが容易です。
- **投稿ループ**: ハードコードされた `en` フィルターを削除し、各言語に対して `post.path contains "_posts/{{ lang }}/"` をチェックするようにしました。
- **ノートループ**: 同様に追加し、`note.path contains "_notes/{{ lang }}/"` をチェックします。ノートを投稿と全く同様に扱います（同じクラス、属性、構造）。
- **ソート**: 両方のループに `| sort: 'date' | reverse` を追加し、時系列順（新しい順）にしました。不要であれば削除してください。
- **空チェック**: `site.notes.size` を含むように更新しました。
- **パフォーマンス**: これはビルド時に約9言語分のコンテンツをすべて生成します。小規模サイトでは問題ありませんが、大規模な場合はページネーションやJSフェッチを検討してください。

### オプション: タイプ切り替えの追加 (投稿/ノート/両方)

「セレクト/スイッチ、2つのオプションセレクトか何かを追加」とおっしゃっていたので、もし**2つ目のドロップダウン**を追加してタイプ（例: 投稿のみ、ノートのみ、または両方）でフィルタリングしたい場合は、言語セレクトの後にこれを `sort.html` に追加してください：

```html
<select id="type-select">
  <option value="both" selected>Posts & Notes</option>
  <option value="posts">Posts Only</option>
  <option value="notes">Notes Only</option>
</select>
```

その後、各 `<li>` に `data-type` 属性を追加します：
- 投稿の場合: `data-type="posts"`
- ノートの場合: `data-type="notes"`

あなたの `index.js` を更新して `#type-select` の変更を処理するようにします（例: `.post-item[data-type="notes"]` をフィルタリングして表示/非表示）。これにより、Liquid を変更することなくシンプルに保てます。

### 次のステップ
- **テスト**: `_notes/es/2025-11-07-tidb-vs-cockroachdb-es.md` のようなサンプルノートを frontmatter (title, date など) 付きで追加し、リビルド後、ドロップダウンで「Español」に切り替えてみてください — 表示されるはずです。
- **JS調整**: `index.js` が `.lang-{value}` でフィルタリングし、`#post-number` を（例: 表示されている `<li>` の数を数えて）更新することを確認してください。もしノートをまだ処理していない場合は、上記のように `data-type` を追加してください。
- もしパスが異なる場合（例: ディレクトリに末尾の `/` がない）、`contains` チェックを調整してください。

これは、あなたの9言語セットアップを維持しながら、ノートをシームレスに統合します。JSスニペットやさらなる調整が必要でしたらお知らせください！