---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 預編譯語言特定索引頁面
translated: true
type: note
---

是的，你可以為不同語言預編譯獨立的首頁檔案（例如 `index-zh.html`、`index-en.html`），以提升效能和使用者體驗，特別是當你的網站擁有大量文章，或希望減少客戶端 JavaScript 處理時。這種方法會在建置過程中為每種語言生成靜態 HTML 檔案，而非依賴 JavaScript 在客戶端動態篩選和排序文章。

以下我將說明如何透過 Jekyll 實現此功能，重點在建立各語言獨立首頁（`index-zh.html`、`index-en.html` 等）的同時，維持現有設定的功能性。這將利用 Jekyll 的建置系統預先計算每種語言的篩選後文章列表，減少複雜的客戶端 JavaScript 處理需求。

---

### 預編譯 `index-zh.html`、`index-en.html` 等檔案的實現方法

要預編譯語言專屬的首頁，你可以為每種語言建立獨立的 Jekyll 頁面模板，並在建置過程中透過 Liquid 語法按語言篩選文章。如此一來，每個頁面（`index-en.html`、`index-zh.html` 等）將僅包含相關語言的文章，而排序/篩選邏輯會在建置時處理，而非在瀏覽器中執行。

具體操作方式如下：

---

#### 1. 建立語言專屬頁面模板

在 Jekyll 專案的根目錄中為每種語言建立獨立頁面檔案，例如：

- `index-en.html`
- `index-zh.html`
- `index-ja.html`
- ...以及其他語言版本（`es`、`hi`、`fr`、`de`、`ar`、`hant` 等）。

每個檔案將採用與你提供程式碼相似的結構，但會使用 Liquid 語法篩選特定語言的文章。以下是 `index-en.html` 的範例：

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

至於 `index-zh.html`，你需要替換 `lang` 和 `where` 篩選器：

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

請為每種語言（`ja`、`es`、`hi`、`fr`、`de`、`ar`、`hant` 等）重複此步驟，並相應調整 `lang` 前置資料和 `where` 篩選器。

---

#### 2. 更新文章前置資料

確保 `_posts` 目錄中的每篇文章都設有 `lang` 前置資料變數，對應其語言（例如 `en`、`zh`、`ja` 等）。範例：

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

這讓 `where` 篩選器能正確按語言識別文章。

若你的文章組織在子目錄中（如 `_posts/en/`、`_posts/zh/` 等），你可以從路徑推斷語言，而無需使用 `lang` 變數。例如在 `index-en.html` 中：

```liquid
{% assign en_posts = site.posts | where_exp: "post", "post.path contains '_posts/en/'" %}
```

---

#### 3. 簡化 JavaScript

由於語言篩選現已於建置時處理，你可以簡化 JavaScript 僅處理排序（例如按日期或作者精選）和語言頁面間的導航。以下是更新後的 JavaScript 範例：

```javascript
window.addEventListener('load', function () {
  const sortSelect = document.getElementById('sort-select');
  const postNumber = document.getElementById('post-number');
  const postList = document.querySelector('.post-list');

  function updatePosts() {
    const selectedValue = sortSelect.value;
    const [sortOption, langFilter] = selectedValue.split('|');

    // If the selected language doesn't match the current page, redirect
    const currentLang = '{{ page.lang }}';
    if (langFilter !== currentLang && langFilter !== 'all' && langFilter !== 'original' && sortOption !== 'author-picks') {
      window.location.href = `/${langFilter}/?sort=${selectedValue}`;
      return;
    }

    // Grab all posts
    const posts = document.querySelectorAll('.post-list li.post-item');
    let processedPosts = [];

    if (sortOption === 'author-picks') {
      // Filter posts with 'data-top' > 0
      processedPosts = Array.from(posts)
        .filter(post => parseInt(post.dataset.top || 0, 10) > 0)
        .map(post => ({ element: post }));
    } else if (sortOption === 'date-desc' && langFilter === 'original') {
      // Filter original (non-translated, non-generated) posts
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
      // Sort by date descending
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

    // Clear existing list
    postList.innerHTML = '';

    // Append processed posts or show a message
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

    // Update the post count
    const translatedCount = processedPosts.filter(item => item.element && item.element.dataset.translated === 'true').length;
    postNumber.innerHTML = `${processedPosts.length} posts (${translatedCount} by <a href="https://mistral.ai">AI</a>)`;

    // Show the list
    postList.style.display = 'block';
  }

  // Restore from localStorage or set default
  const savedSort = localStorage.getItem('sortOption');
  if (savedSort) {
    sortSelect.value = savedSort;
  } else {
    sortSelect.value = 'date-desc|{{ page.lang }}';
  }

  updatePosts();

  // Event listener for dropdown changes
  sortSelect.addEventListener('change', function () {
    localStorage.setItem('sortOption', sortSelect.value);
    updatePosts();
  });
});
```

主要變更：
- 腳本會檢查選取的語言是否與當前頁面語言（`{{ page.lang }}`）匹配。若不匹配，則重新導向至相應語言頁面（例如中文頁面 `/zh/`）。
- 由於文章已透過 Liquid 模板預先篩選，不再需要語言篩選功能。

---

#### 4. 設定固定鏈結與導航

確保每個語言專屬頁面在其前置資料中設有獨特的固定鏈結（例如 `index-en.html` 設為 `permalink: /en/`）。這讓使用者能直接導航至 `/en/`、`/zh/` 等路徑。

你可能也需要更新網站的導航選單，加入這些語言專屬頁面的連結。例如在版型或頂部欄位中：

```html
<nav>
  <a href="/en/">English</a>
  <a href="/zh/">中文</a>
  <a href="/ja/">日本語</a>
  <!-- 加入其他語言 -->
</nav>
```

---

#### 5. 處理「全部」與「原創」篩選器

針對下拉選單中的「全部」和「原創」選項：
- **全部**：你可以建立包含所有文章的 `index.html`（類似原始設定），或重新導向至某個語言專屬頁面。
- **原創**：你可以建立 `index-original.html` 來篩選 `translated: false` 且 `generated: false` 的文章：

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

#### 6. 預編譯的優勢

- **效能**：在建置時篩選文章可減少客戶端 JavaScript 處理，提升網站速度，對裝置或連線速度較慢的使用者尤其明顯。
- **SEO**：搜尋引擎能更好地索引語言專屬頁面（`/en/`、`/zh/` 等），提升可發現性。
- **簡化 JavaScript**：JavaScript 僅需處理排序和導航，無需處理語言篩選。
- **可靠性**：預編譯頁面可避免客戶端錯誤（例如原始程式碼中的「已知錯誤待修復」訊息）。

---

#### 7. 注意事項

- **建置時間**：預編譯多個首頁會增加建置時間，特別當你擁有大量文章或多種語言時。但除非文章數以千計，否則影響通常可忽略不計。
- **維護**：你需要維護多個索引檔案（`index-en.html`、`index-zh.html` 等）。為減少重複，可使用 Jekyll includes 或版型來共享通用程式碼。
- **動態排序**：JavaScript 仍負責處理排序（例如作者精選、日期降冪），但若你希望實現完全靜態輸出，也可以預先計算每個頁面的排序版本（不過這會產生更多檔案，例如 `index-en-picks.html`）。

---

#### 8. 範例目錄結構

你的 Jekyll 專案結構可能如下：

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

#### 9. 測試與部署

- 使用 `jekyll serve` 在本機測試，確保每個語言頁面（`/en/`、`/zh/` 等）正確顯示對應文章。
- 驗證下拉選單的導航能否正確在語言頁面間重新導向。
- 部署至你的託管平台（例如 GitHub Pages），並檢查固定鏈結是否如預期運作。

---

### 參考資源
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Mistral AI](https://mistral.ai)

若你有進一步問題或需要協助實作特定部分，請隨時告知！