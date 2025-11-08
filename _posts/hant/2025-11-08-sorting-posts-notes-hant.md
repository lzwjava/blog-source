---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 帖子與筆記排序
translated: true
type: note
---

### 修改後的 `_includes/sort.html`

你現有的 `sort.html` 已經包含了 9 種語言的選擇器，這非常完美。這裡不需要重大更改，但我在 `<span id="post-number">` 中添加了一個小註解，使其更通用（例如，使用「entries」而不是「posts」），因為我們現在包含了筆記。如果需要，這可以通過你的 JS 動態更新。以下是調整後的版本：

```html
<div class="sort-container">
  <span id="post-number" class="post-number">
    {{ site.posts.size | plus: site.notes.size }} 個條目
    ({{ site.posts.size | plus: site.notes.size | divided_by: 7 | times: 6 }} 由 <a href="https://openrouter.ai">AI</a> 翻譯)
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

**關鍵更改**：更新了計數以包含 `site.notes.size`（我們將在下面定義這個）。公式保持不變，但現在考慮了筆記。如果你的 JS (`index.js`) 已經根據可見項目動態更新此 span，它將自動處理特定語言的計數。

### 步驟 1：將筆記配置為 Jekyll 集合（在 `_config.yml` 中）

要將 `_notes` 視為 `_posts`（以便 Jekyll 處理 Markdown 文件並通過 `site.notes` 公開它們），請將以下內容添加到你的 `_config.yml` 中。這至關重要——沒有它，筆記將不會像文章那樣擁有 `url`、`title`、`date` 等屬性。

```yaml
collections:
  notes:
    output: true
    permalink: /notes/:path/
```

- `output: true` 為筆記生成頁面（如果只需要數據，則為可選）。
- `permalink` 確保 URL 如 `/notes/es/2025-11-07-tidb-vs-cockroachdb-es/`（如果需要，請調整）。
- 添加此內容後，請重啟你的 Jekyll 伺服器。

現在 `site.notes` 就像 `site.posts` 一樣工作，假設你的筆記文件（例如 `_notes/es/2025-11-07-tidb-vs-cockroachdb-es.md`）具有類似的 frontmatter：`title:`、`date:`、`image:`、`top:`、`translated:`、`generated:`。

### 步驟 2：修改後的頁面佈局（例如 `index.md` 或你的 `<ul class="post-list">` 所在的位置）

你當前的循環僅顯示英文文章。要添加筆記並支持所有 9 種語言：

- 定義一次語言列表。
- 遍歷**所有**語言。
- 對於每種語言，添加匹配的**文章**（來自 `_posts/{lang}/`）和**筆記**（來自 `_notes/{lang}/`）作為 `<li>` 項目。
- 每個 `<li>` 獲得 `class="... lang-{lang}"`，以便你的 JS 可以過濾它們（例如，根據 `#sort-select` 值隱藏/顯示）。
- 這會預先填充整個列表（由 JS 隱藏），然後動態切換語言。
- 按日期排序？如果你希望最新的在前，請在循環中添加 `| sort: 'date' | reverse`（假設日期是可比較的）。

以下是完整的更新後佈局：

```html
---
layout: page
---
{% include sort.html %}

<ul class="post-list">
  {% if site.posts.size == 0 and site.notes.size == 0 %}
    <li class="list-group-item post-item">暫無可用條目。</li>
  {% else %}
    {% assign langs = "en,zh,ja,es,hi,fr,de,ar,hant" | split: "," %}
    {% for lang in langs %}
      {% comment %} 此語言的貼文 {% endcomment %}
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

      {% comment %} 此語言的筆記（與貼文相同） {% endcomment %}
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

**關鍵更改**：
- **語言陣列**：`{% assign langs = "en,zh,ja,es,hi,fr,de,ar,hant" | split: "," %}`—與你的選擇選項匹配。易於維護。
- **貼文循環**：移除了硬編碼的 `en` 過濾器；現在檢查每個語言的 `post.path contains "_posts/{{ lang }}/"`。
- **筆記循環**：以相同方式添加，檢查 `note.path contains "_notes/{{ lang }}/"`。將筆記視為與貼文完全相同（相同的類別、屬性、結構）。
- **排序**：在兩個循環中添加了 `| sort: 'date' | reverse` 以按時間順序排列（最新的在前）。如果不需要，請移除。
- **空檢查**：更新以包含 `site.notes.size`。
- **效能**：這在構建時生成所有約 9 種語言的內容。對於小型站點來說沒問題；如果內容龐大，請考慮分頁或 JS 獲取。

### 可選：添加類型切換（貼文/筆記/兩者）

你提到「添加一個選擇/切換，兩個選項選擇或其他」。如果你想要**第二個下拉選單**來按類型過濾（例如，僅貼文、僅筆記或兩者），請在語言選擇器之後將以下內容添加到 `sort.html`：

```html
<select id="type-select">
  <option value="both" selected>Posts & Notes</option>
  <option value="posts">Posts Only</option>
  <option value="notes">Notes Only</option>
</select>
```

然後，為每個 `<li>` 添加一個 `data-type` 屬性：
- 對於貼文：`data-type="posts"`
- 對於筆記：`data-type="notes"`

更新你的 `index.js` 以處理 `#type-select` 的更改（例如，過濾 `.post-item[data-type="notes"]` 以隱藏/顯示）。這使得它在不更改 Liquid 的情況下保持簡單。

### 後續步驟
- 測試：添加一個示例筆記，如 `_notes/es/2025-11-07-tidb-vs-cockroachdb-es.md`，並帶有 frontmatter（標題、日期等），重新構建，然後在下拉選單中切換到「Español」—它應該會出現。
- JS 調整：確保 `index.js` 通過 `.lang-{value}` 過濾並更新 `#post-number`（例如，計算可見的 `<li>`）。如果它尚未處理筆記，請如上所述添加 `data-type`。
- 如果路徑不同（例如，目錄中沒有尾隨 `/`），請調整 `contains` 檢查。

這將無縫集成筆記，同時保持你的 9 種語言設置。如果你需要 JS 片段或進一步調整，請告訴我！