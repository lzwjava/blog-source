---
audio: false
generated: true
image: false
lang: ja
layout: post
title: 言語別索引ページの事前コンパイル
translated: true
type: note
---

はい、パフォーマンスとユーザーエクスペリエンスを向上させるために、特にサイトに多数の投稿がある場合や、クライアントサイドのJavaScript処理を削減したい場合に、異なる言語用の個別のインデックスページ（例: `index-zh.html`、`index-en.html`）を事前コンパイルすることができます。このアプローチでは、クライアントサイドでJavaScriptを使用して投稿を動的にフィルタリングおよびソートするのではなく、ビルドプロセス中に各言語用の静的なHTMLファイルを生成します。

以下に、現在のセットアップの機能を維持しながら、Jekyllを使用して各言語用の個別のインデックスページ（`index-zh.html`、`index-en.html` など）を作成する方法について説明します。これにより、Jekyllのビルドシステムを活用して各言語用にフィルタリングされた投稿リストを事前計算し、複雑なクライアントサイドJavaScriptの必要性を減らすことができます。

---

### `index-zh.html`、`index-en.html` などを事前コンパイルするアプローチ

言語固有のインデックスページを事前コンパイルするには、各言語用に個別のJekyllページテンプレートを作成し、ビルドプロセス中にLiquidを使用して言語で投稿をフィルタリングします。これにより、各ページ（`index-en.html`、`index-zh.html` など）には関連する投稿のみが含まれ、ソート/フィルタリングロジックはブラウザではなくビルド時に処理されます。

以下の手順で実行できます。

---

#### 1. 言語固有のページテンプレートを作成する

Jekyllプロジェクトのルートディレクトリに、各言語用の個別のページファイルを作成します。例:

- `index-en.html`
- `index-zh.html`
- `index-ja.html`
- ...およびその他の言語（`es`、`hi`、`fr`、`de`、`ar`、`hant` など）についても同様。

各ファイルは、提供されたコードと同様の構造を使用しますが、Liquidを使用して特定の言語で投稿をフィルタリングします。以下は `index-en.html` の例です:

```html
---
layout: page
lang: en
permalink: /en/
---

<div class="sort-container">
  <span id="post-number" class="post-number">
    {% assign en_posts = site.posts | where: "lang", "en" %}
    {{ en_posts.size }} posts
    ({{ en_posts | where: "translated", true | size }} by <a href="https://mistral.ai">AI</a>)
  </span>

  <select id="sort-select">
    <option value="author-picks|en">Picks</option>
    <option value="date-desc|all">All</option>
    <option value="date-desc|original">Original</option>
    <option value="date-desc|en" selected>English</option>
    <option value="date-desc|zh">中文</option>
    <option value="date-desc|ja">日本語</option>
    <option value="date-desc|es">Español</option>
    <option value="date-desc|hi">हिंदी</option>
    <option value="date-desc|fr">Français</option>
    <option value="date-desc|de">Deutsch</option>
    <option value="date-desc|ar">العربية</option>
    <option value="date-desc|hant">繁體中文</option>
  </select>
</div>

<ul class="post-list">
  {% if en_posts.size > 0 %}
    {% for post in en_posts %}
      <li class="list-group-item post-item lang-en" data-top="{{ post.top | default: 0 }}" data-translated="{{ post.translated | default: false }}" data-generated="{{ post.generated | default: false }}">
        <a href="{{ post.url }}">
          <span class="date">{{ post.date | date: "%Y.%m.%d" }}</span>
          <span class="type">{% if post.image %}image{% else %}text{% endif %}</span>
          <span class="title">{{ post.title }}</span>
        </a>
      </li>
    {% endfor %}
  {% else %}
    <li class="list-group-item post-item">No posts available.</li>
  {% endif %}
</ul>

<footer class="site-footer">
  <span class="site-footer-credits">
    Powered by <a href="https://jekyllrb.com/">Jekyll</a><br>
    Ignited by <a href="https://mistral.ai">Mistral</a><br>
    Updated at <a href="https://github.com/lzwjava/lzwjava.github.io/commit/{{ site.release }}">{{ site.release | slice: 0, 6 }}</a><br>
    Copyright©{{ site.starting_year }}–{{ site.time | date: "%Y" }}
  </span>
</footer>
```

`index-zh.html` の場合、`lang` と `where` フィルタを置き換えます:

```html
---
layout: page
lang: zh
permalink: /zh/
---
<div class="sort-container">
  <span id="post-number" class="post-number">
    {% assign zh_posts = site.posts | where: "lang", "zh" %}
    {{ zh_posts.size }} posts
    ({{ zh_posts | where: "translated", true | size }} by <a href="https://mistral.ai">AI</a>)
  </span>
  <!-- Same sort-select as above -->
</div>

<ul class="post-list">
  {% if zh_posts.size > 0 %}
    {% for post in zh_posts %}
      <li class="list-group-item post-item lang-zh" data-top="{{ post.top | default: 0 }}" data-translated="{{ post.translated | default: false }}" data-generated="{{ post.generated | default: false }}">
        <a href="{{ post.url }}">
          <span class="date">{{ post.date | date: "%Y.%m.%d" }}</span>
          <span class="type">{% if post.image %}image{% else %}text{% endif %}</span>
          <span class="title">{{ post.title }}</span>
        </a>
      </li>
    {% endfor %}
  {% else %}
    <li class="list-group-item post-item">No posts available.</li>
  {% endif %}
</ul>

<!-- Same footer as above -->
```

各言語（`ja`、`es`、`hi`、`fr`、`de`、`ar`、`hant` など）についてこれを繰り返し、`lang` フロントマターと `where` フィルタを適宜調整します。

---

#### 2. 投稿のフロントマターを更新する

`_posts` ディレクトリ内の各投稿に、その言語に対応する `lang` フロントマター変数（例: `en`、`zh`、`ja` など）があることを確認してください。例:

```yaml
---
title: My English Post
lang: en
date: 2025-08-01
translated: true
generated: false
top: 1
---
```

これにより、`where` フィルタが言語ごとに投稿を正しく識別できます。

投稿が `_posts/en/`、`_posts/zh/` などのサブディレクトリに整理されている場合は、`lang` 変数を使用する代わりに、パスから言語を推測できます。例: `index-en.html` で:

```liquid
{% assign en_posts = site.posts | where_exp: "post", "post.path contains '_posts/en/'" %}
```

---

#### 3. JavaScriptを簡素化する

言語フィルタリングがビルド時に処理されるため、JavaScriptをソート（例: 日付順や作者のおすすめ）と言語ページ間のナビゲーションのみを処理するように簡素化できます。以下は更新されたJavaScriptのバージョンです:

```javascript
window.addEventListener('load', function () {
  const sortSelect = document.getElementById('sort-select');
  const postNumber = document.getElementById('post-number');
  const postList = document.querySelector('.post-list');

  function updatePosts() {
    const selectedValue = sortSelect.value;
    const [sortOption, langFilter] = selectedValue.split('|');

    // 選択された言語が現在のページと一致しない場合、リダイレクト
    const currentLang = '{{ page.lang }}';
    if (langFilter !== currentLang && langFilter !== 'all' && langFilter !== 'original' && sortOption !== 'author-picks') {
      window.location.href = `/${langFilter}/?sort=${selectedValue}`;
      return;
    }

    // すべての投稿を取得
    const posts = document.querySelectorAll('.post-list li.post-item');
    let processedPosts = [];

    if (sortOption === 'author-picks') {
      // 'data-top' > 0 の投稿をフィルタリング
      processedPosts = Array.from(posts)
        .filter(post => parseInt(post.dataset.top || 0, 10) > 0)
        .map(post => ({ element: post }));
    } else if (sortOption === 'date-desc' && langFilter === 'original') {
      // オリジナル（翻訳されていない、生成されていない）投稿をフィルタリング
      processedPosts = Array.from(posts)
        .filter(post => post.dataset.translated === 'false' && post.dataset.generated === 'false')
        .map(post => {
          const dateElement = post.querySelector('.date');
          const dateStr = dateElement ? dateElement.textContent.trim().replace(/\./g, '-') : null;
          return { element: post, date: dateStr ? new Date(dateStr) : null };
        })
        .filter(item => item.date)
        .sort((a, b) => b.date - a.date);
    } else {
      // 日付の降順でソート
      processedPosts = Array.from(posts)
        .map(post => {
          const dateElement = post.querySelector('.date');
          const dateStr = dateElement ? dateElement.textContent.trim().replace(/\./g, '-') : null;
          const aElement = post.querySelector('a');
          const href = aElement ? aElement.getAttribute('href') : '';
          const fileName = href ? href.split('/').pop() : '';
          return { element: post, date: dateStr ? new Date(dateStr) : null, fileName };
        })
        .filter(item => item.date)
        .sort((a, b) => {
          const dateComparison = b.date - a.date;
          return dateComparison !== 0 ? dateComparison : a.fileName.localeCompare(b.fileName);
        });
    }

    // 既存のリストをクリア
    postList.innerHTML = '';

    // 処理された投稿を追加するか、メッセージを表示
    if (processedPosts.length > 0) {
      processedPosts.forEach(item => {
        if (item.element) {
          postList.appendChild(item.element);
        }
      });
    } else {
      const noPostsMessage = document.createElement('li');
      noPostsMessage.className = 'list-group-item post-item';
      noPostsMessage.textContent = 'No posts available. Please refresh the page.';
      postList.appendChild(noPostsMessage);
    }

    // 投稿数を更新
    const translatedCount = processedPosts.filter(item => item.element && item.element.dataset.translated === 'true').length;
    postNumber.innerHTML = `${processedPosts.length} posts (${translatedCount} by <a href="https://mistral.ai">AI</a>)`;

    // リストを表示
    postList.style.display = 'block';
  }

  // localStorageから復元するか、デフォルトを設定
  const savedSort = localStorage.getItem('sortOption');
  if (savedSort) {
    sortSelect.value = savedSort;
  } else {
    sortSelect.value = 'date-desc|{{ page.lang }}';
  }

  updatePosts();

  // ドロップダウンの変更に対するイベントリスナー
  sortSelect.addEventListener('change', function () {
    localStorage.setItem('sortOption', sortSelect.value);
    updatePosts();
  });
});
```

主な変更点:
- スクリプトは、選択された言語が現在のページの言語（`{{ page.lang }}`）と一致するかどうかをチェックします。一致しない場合は、適切な言語ページ（例: 中国語の場合は `/zh/`）にリダイレクトします。
- 投稿はLiquidテンプレートによって事前にフィルタリングされているため、言語フィルタリングは不要になりました。

---

#### 4. パーマリンクとナビゲーションを設定する

各言語固有のページがフロントマターに一意のパーマリンク（例: `index-en.html` の場合は `permalink: /en/`）を持つことを確認してください。これにより、ユーザーは直接 `/en/`、`/zh/` などにナビゲートできます。

サイトのナビゲーションを更新して、これらの言語固有のページへのリンクを含めることもできます。例: レイアウトまたはヘッダー内で:

```html
<nav>
  <a href="/en/">English</a>
  <a href="/zh/">中文</a>
  <a href="/ja/">日本語</a>
  <!-- 他の言語を追加 -->
</nav>
```

---

#### 5. 「All」および「Original」フィルタを処理する

ドロップダウンの「All」および「Original」オプションについて:
- **All**: すべての投稿を含む `index.html` を作成する（元のセットアップと同様）か、言語固有のページのいずれかにリダイレクトできます。
- **Original**: `translated: false` および `generated: false` の投稿をフィルタリングする `index-original.html` を作成できます:

```html
---
layout: page
lang: original
permalink: /original/
---
<div class="sort-container">
  <span id="post-number" class="post-number">
    {% assign original_posts = site.posts | where: "translated", false | where: "generated", false %}
    {{ original_posts.size }} posts
    (0 by <a href="https://mistral.ai">AI</a>)
  </span>
  <!-- Same sort-select -->
</div>

<ul class="post-list">
  {% if original_posts.size > 0 %}
    {% for post in original_posts %}
      <li class="list-group-item post-item lang-{{ post.lang }}" data-top="{{ post.top | default: 0 }}" data-translated="false" data-generated="false">
        <a href="{{ post.url }}">
          <span class="date">{{ post.date | date: "%Y.%m.%d" }}</span>
          <span class="type">{% if post.image %}image{% else %}text{% endif %}</span>
          <span class="title">{{ post.title }}</span>
        </a>
      </li>
    {% endfor %}
  {% else %}
    <li class="list-group-item post-item">No posts available.</li>
  {% endif %}
</ul>

<!-- Same footer -->
```

---

#### 6. 事前コンパイルの利点

- **パフォーマンス**: ビルド時に投稿をフィルタリングすることで、クライアントサイドのJavaScript処理が削減され、特に低速なデバイスや接続のユーザーにとってサイトが高速化されます。
- **SEO**: 検索エンジンが言語固有のページ（`/en/`、`/zh/` など）をより適切にインデックスできるため、発見性が向上します。
- **よりシンプルなJavaScript**: JavaScriptはソートとナビゲーションのみを処理する必要があり、言語フィルタリングは不要です。
- **信頼性**: 事前コンパイルされたページは、クライアントサイドのバグ（例: 元のコードの「Known bug pending fix」メッセージ）を回避します。

---

#### 7. 考慮事項

- **ビルド時間**: 複数のインデックスページを事前コンパイルすると、特に多数の投稿や言語がある場合、ビルド時間が増加します。ただし、数千の投稿がない限り、通常は無視できます。
- **メンテナンス**: 複数のインデックスファイル（`index-en.html`、`index-zh.html` など）を維持する必要があります。重複を減らすために、Jekyllのインクルードやレイアウトを使用して共通コードを共有できます。
- **動的ソート**: JavaScriptは依然としてソート（例: 作者のおすすめ、日付の降順）を処理しますが、完全に静的な出力が必要な場合は、各ページのソート済みバージョンを事前計算することもできます（ただし、これによりより多くのファイル、例: `index-en-picks.html` が作成されます）。

---

#### 8. ディレクトリ構造の例

Jekyllプロジェクトは次のようになります:

```
├── _posts/
│   ├── en/
│   │   ├── 2025-08-01-post1.md
│   │   ├── 2025-08-02-post2.md
│   ├── zh/
│   │   ├── 2025-08-01-post1-zh.md
│   ├── ja/
│   └── ...
├── _layouts/
│   ├── page.html
├── index-en.html
├── index-zh.html
├── index-ja.html
├── index-original.html
├── _includes/
│   ├── header.html
│   ├── footer.html
├── assets/
│   ├── js/
│   │   ├── sort.js
```

---

#### 9. テストとデプロイ

- `jekyll serve` でローカルにテストし、各言語ページ（`/en/`、`/zh/` など）が正しい投稿を表示することを確認します。
- ドロップダウンナビゲーションが言語ページ間で正しくリダイレクトすることを確認します。
- ホスティングプラットフォーム（例: GitHub Pages）にデプロイし、パーマリンクが期待通りに機能することを確認します。

---

### 参考文献
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Mistral AI](https://mistral.ai)

実装の特定の部分についてさらに質問やヘルプが必要な場合は、お知らせください！