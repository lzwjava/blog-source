---
audio: false
date: 2025-09-09
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: Jekyllのサイトマップファイル生成
translated: true
type: note
---

**sitemap.xml** は、Google や Bing などの検索エンジンに対して、あなたのウェブサイト上のページについて伝える XML ファイルです。これは、クローラーがあなたのサイトの構造をより効率的に発見し、インデックスするのに役立ちます。Jekyll ブログの場合、これは、あなたのすべての投稿、ページ、翻訳ページ（`index-zh.html`、`index-fr.html` など）が、どこにもリンクされていなくても、検索エンジンが見つけられることを意味します。

### Sitemap の役割

*   サイトのすべての重要な URL をリストアップします。
*   最終更新日 (`<lastmod>`)、変更頻度 (`<changefreq>`)、優先度 (`<priority>`) などのメタデータを提供します。
*   クローラーがページを見逃さないようにすることで、SEO を改善します。

### Jekyll での生成方法

いくつかの方法があります:

#### 1. `jekyll-sitemap` プラグインを使用する (推奨)

1.  Jekyll プロジェクトの `Gemfile` に以下を追加します:

    ```ruby
    gem 'jekyll-sitemap'
    ```
2.  `_config.yml` に以下を追加します:

    ```yaml
    plugins:
      - jekyll-sitemap
    ```

    (GitHub Pages を使用している場合、`jekyll-sitemap` はすでにホワイトリストに登録されているため、直接動作します。)
3.  ビルド時 (`jekyll build` または、設定している場合は `make` 経由) に、Jekyll は `_site/` フォルダ内に `sitemap.xml` を自動生成します。

#### 2. 手動で Sitemap テンプレートを作成する

より細かい制御を希望する場合:

1.  プロジェクトルートに `/sitemap.xml` ファイルを作成します。
2.  以下の Liquid テンプレートを追加します:

    ```xml
    ---
    layout: nil
    ---
    <?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
      {% for page in site.pages %}
        {% if page.sitemap != false %}
          <url>
            <loc>{{ site.url }}{{ page.url | replace:'index.html','' }}</loc>
            <lastmod>{{ page.date | date_to_xmlschema }}</lastmod>
          </url>
        {% endif %}
      {% endfor %}
      {% for post in site.posts %}
        <url>
          <loc>{{ site.url }}{{ post.url }}</loc>
          <lastmod>{{ post.date | date_to_xmlschema }}</lastmod>
        </url>
      {% endfor %}
    </urlset>
    ```
3.  リンクが正しく生成されるように、`_config.yml` に `url: "https://yourdomain.com"` が設定されていることを確認してください。

#### 3. 検証

*   ビルド後、`_site/sitemap.xml` を確認してください。
*   より良いインデックス登録のために、Google Search Console に送信してください。

---

👉 あなたはすでに `_config.yml` と `_plugins/` をお持ちなので、最も簡単な方法は `jekyll-sitemap` を有効にすることです。そうすれば、XML を手動でメンテナンスする必要はありません。

現在のファイルに基づいて、リポジトリに直接貼り付けできるように、正確な `_config.yml` への追加部分を草案してほしいですか？