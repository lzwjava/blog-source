---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Jekyll i18n：多言語対応プラグインとフォルダ方式
translated: true
type: note
---

Jekyllブログでのi18n実装には、「バッテリー内蔵」から「ベアボーン」まで3つの優れた方法があります。それぞれの仕組みと設定方法をご紹介します。

# 1) 最も簡単: プラグインを使用 (jekyll-polyglot)

**ローカルまたはCIでビルドできる場合に最適。** GitHub Pagesの組み込みビルダーはほとんどのサードパーティプラグインを許可しないため、ローカルでビルド(`jekyll build`)して生成された`_site/`をプッシュするか、GitHub Actionsを使用してビルドと公開を行います。

**インストール**

```bash
gem install jekyll-polyglot
# またはGemfileに追加:
# gem 'jekyll-polyglot'
```

**\_config.yml**

```yml
plugins:
  - jekyll-polyglot

languages: ["en", "zh", "ja"]   # 使用言語
default_lang: "en"
exclude_from_localization: ["assets", "images", "CNAME"]  # 静的パスを共有維持
parallel_localization: true
```

**コンテンツ構造**

```
_index.md               # オプションのランディングページ
_posts/
  2024-05-01-hello.en.md
  2024-05-01-hello.zh.md
pages/
  about.en.md
  about.zh.md
```

Polyglotは`/en/about/`や`/zh/about/`のような言語スコープのURLを構築します。また、`site.active_lang`も公開します。

**言語切替（レイアウト内）**

```liquid
<nav class="lang-switch">
  {% for lang in site.languages %}
    {% if lang == site.active_lang %}
      <span>{{ lang }}</span>
    {% else %}
      <a href="{{ page.url | prepend:'/' | replace_first:'/' | prepend:'/' | absolute_url | replace: '/' | relative_url | prepend:'/' }}">
        {%- comment -%}
        各言語用に現在のURLを再構築します:
        {%- endcomment -%}
      </a>
    {% endif %}
  {% endfor %}
</nav>
```

Polyglotを使用したより簡単な方法:

```liquid
<nav>
  {% for lang in site.languages %}
    <a href="{{ site.baseurl_root }}/{{ lang }}{{ page.permalink | default: page.url }}">{{ lang }}</a>
  {% endfor %}
</nav>
```

**UI文字列はデータファイル経由**
`_data/i18n.yml`を作成:

```yml
en:
  nav:
    home: "Home"
    posts: "Posts"
zh:
  nav:
    home: "主页"
    posts: "文章"
```

テンプレート内で使用:

```liquid
{{ site.data.i18n[site.active_lang].nav.home }}
```

**SEO (hreflang)**
レイアウトの`<head>`内に:

```liquid
{% assign langs = site.languages %}
{% for l in langs %}
  <link rel="alternate" hreflang="{{ l }}" href="{{ site.url }}/{{ l }}{{ page.url }}" />
{% endfor %}
<link rel="alternate" hreflang="x-default" href="{{ site.url }}/{{ site.default_lang }}{{ page.url }}" />
```

# 2) プラグインなし: 言語別フォルダ + Liquid

**GitHub Pagesの組み込みビルダーを使用する必要がある場合に最適。**

**構造**

```
_en/
  index.md
  about.md
_zh/
  index.md
  about.md
_posts/
  en/
    2024-05-01-hello.md
  zh/
    2024-05-01-hello.md
```

**\_config.yml**

```yml
defaults:
  - scope: { path: "_posts/en" }
    values: { lang: "en", permalink: "/en/:categories/:year/:month/:day/:title/" }
  - scope: { path: "_posts/zh" }
    values: { lang: "zh", permalink: "/zh/:categories/:year/:month/:day/:title/" }
  - scope: { path: "_en" }
    values: { lang: "en", permalink: "/en/:path/" }
  - scope: { path: "_zh" }
    values: { lang: "zh", permalink: "/zh/:path/" }
```

**現在の言語を設定**
各ページのフロントマターに追加:

```yml
---
layout: default
lang: en
---
```

またはパスから推測:

```liquid
{% assign current_lang = page.lang | default: page.path | split:'/' | first | remove:'_' %}
```

**翻訳間の相互リンク**
フロントマターで共有識別子を使用:

```yml
---
layout: post
lang: en
ref: hello-post
---
```

中国語版では:

```yml
---
layout: post
lang: zh
ref: hello-post
---
```

レイアウト内で兄弟ページを検索:

```liquid
{% assign siblings = site.pages | concat: site.posts | where:"ref", page.ref %}
{% for s in siblings %}
  {% unless s.url == page.url %}
    <a href="{{ s.url }}">{{ s.lang }}</a>
  {% endunless %}
{% endfor %}
```

**プラグインなしでのUI文字列**
上記のように`_data/i18n.yml`を使用し、`current_lang`経由で言語を選択。

**デフォルト言語リダイレクト（オプション）**
ルートに`index.html`を作成:

```html
<!doctype html>
<meta charset="utf-8">
<script>
  const lang = (navigator.language || '').toLowerCase().startsWith('zh') ? 'zh' : 'en';
  location.replace('/' + lang + '/');
</script>
<noscript><a href="/en/">English</a> · <a href="/zh/">中文</a></noscript>
```

# 3) ハイブリッド: 投稿は1セット、UIのみ翻訳

**記事自体は翻訳せず、ナビゲーションやフッターなどのクロームのみ翻訳する場合に最適。**
単一の`/posts/`セットを維持し、`_data/i18n.yml`を追加して、言語ごとにラベルをレンダリングします。同じ投稿をリスト表示するが、ローカライズされた日付とUIを持つ言語別インデックスページを提供します。

**ローカライズされた日付**

```liquid
{% assign locale = page.lang | default: site.default_lang %}
{{ page.date | date: "%B %-d, %Y" }}  {# または、フィルター/プラグインがある場合はそれを使用 #}
```

(Jekyllの組み込み`date`は完全にロケール対応ではありません。真のロケールフォーマットには、プラグインまたはデータ内の事前フォーマット済み文字列が必要です。)

---

## 実用的なヒント

* **スラッグ:** 翻訳対応版には同じ`ref`を維持し、タイトルは言語ごとに変更可能にします。
* **画像:** 共有画像は`/assets/`に配置し、ローカライズから除外してURLを安定させます。
* **サイトマップとSEO:** 言語別サイトマップを生成するか、サイトマップにすべての言語URLがリストされていることを確認します。各言語バージョン内にcanonicalタグを追加します。
* **フィード:** コレクションをスコープすることで言語別フィードを作成: フィードテンプレートで`lang`によって投稿をフィルタリングします。

---

## 最小動作例（プラグインなし）

1. 文字列を含む`_data/i18n.yml`
2. `lang`フロントマターを含む`_en/index.md`と`_zh/index.md`
3. `lang`と共有`ref`を含む`_posts/en/`と`_posts/zh/`下の投稿
4. レイアウトは`site.data.i18n[current_lang]`と上記の兄弟ルックアップスニペットを使用

現在のリポジトリ構造（およびGitHub Pagesを直接ビルドしているかActions経由か）を教えていただければ、すぐに使用できる設定といくつかのスターターレイアウトを調整できます。