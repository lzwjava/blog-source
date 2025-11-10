---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Jekyll 國際化：多語言插件與文件夾方法
translated: true
type: note
---

為你的 Jekyll 博客實現國際化 (i18n)，有三種不錯的方案，從「開箱即用」到「高度自訂」任君選擇。以下是每種方案的運作方式與設定步驟。

# 1) 最簡易方案：使用外掛 (jekyll-polyglot)

**若你能在本地或透過 CI 構建，此為最佳選擇。** GitHub Pages 的內建建置器不允許大多數第三方外掛，因此你需要在本地執行 `jekyll build` 後推送生成的 `_site/` 目錄，或是使用 GitHub Actions 進行建置與發布。

**安裝**

```bash
gem install jekyll-polyglot
# 或將其加入 Gemfile：
# gem 'jekyll-polyglot'
```

**\_config.yml**

```yml
plugins:
  - jekyll-polyglot

languages: ["en", "zh", "ja"]   # 你的目標語言
default_lang: "en"
exclude_from_localization: ["assets", "images", "CNAME"]  # 保持靜態路徑共享
parallel_localization: true
```

**內容結構**

```
_index.md               # 可選的 landing 頁面
_posts/
  2024-05-01-hello.en.md
  2024-05-01-hello.zh.md
pages/
  about.en.md
  about.zh.md
```

Polyglot 會建立語言限定的 URL，例如 `/en/about/` 和 `/zh/about/`。它同時也提供了 `site.active_lang` 變數。

**語言切換器 (置於你的版面配置中)**

```liquid
<nav class="lang-switch">
  {% for lang in site.languages %}
    {% if lang == site.active_lang %}
      <span>{{ lang }}</span>
    {% else %}
      <a href="{{ page.url | prepend:'/' | replace_first:'/' | prepend:'/' | absolute_url | replace: '/' | relative_url | prepend:'/' }}">
        {%- comment -%}
        我們將為每種語言重建當前 URL：
        {%- endcomment -%}
      </a>
    {% endif %}
  {% endfor %}
</nav>
```

使用 Polyglot 時，一個更簡單的方法是：

```liquid
<nav>
  {% for lang in site.languages %}
    <a href="{{ site.baseurl_root }}/{{ lang }}{{ page.permalink | default: page.url }}">{{ lang }}</a>
  {% endfor %}
</nav>
```

**透過資料檔案管理 UI 字串**
建立 `_data/i18n.yml`：

```yml
en:
  nav:
    home: "Home"
    posts: "Posts"
zh:
  nav:
    home: "主頁"
    posts: "文章"
```

在模板中使用：

```liquid
{{ site.data.i18n[site.active_lang].nav.home }}
```

**SEO (hreflang)**
在版面配置的 `<head>` 區塊中加入：

```liquid
{% assign langs = site.languages %}
{% for l in langs %}
  <link rel="alternate" hreflang="{{ l }}" href="{{ site.url }}/{{ l }}{{ page.url }}" />
{% endfor %}
<link rel="alternate" hreflang="x-default" href="{{ site.url }}/{{ site.default_lang }}{{ page.url }}" />
```

# 2) 無外掛方案：各語言獨立資料夾 + Liquid

**若你必須使用 GitHub Pages 的內建建置器，此為最佳選擇。**

**結構**

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

**設定當前語言**
在每個頁面的 front matter 中加入：

```yml
---
layout: default
lang: en
---
```

或從路徑推斷：

```liquid
{% assign current_lang = page.lang | default: page.path | split:'/' | first | remove:'_' %}
```

**翻譯版本間的跨鏈結**
在 front matter 中使用共享識別符：

```yml
---
layout: post
lang: en
ref: hello-post
---
```

在中文版本中：

```yml
---
layout: post
lang: zh
ref: hello-post
---
```

然後在版面配置中，尋找對應的翻譯頁面：

```liquid
{% assign siblings = site.pages | concat: site.posts | where:"ref", page.ref %}
{% for s in siblings %}
  {% unless s.url == page.url %}
    <a href="{{ s.url }}">{{ s.lang }}</a>
  {% endunless %}
{% endfor %}
```

**無外掛的 UI 字串管理**
如上所述使用 `_data/i18n.yml`，並透過 `current_lang` 選擇語言。

**預設語言重定向 (可選)**
在根目錄建立 `index.html`：

```html
<!doctype html>
<meta charset="utf-8">
<script>
  const lang = (navigator.language || '').toLowerCase().startsWith('zh') ? 'zh' : 'en';
  location.replace('/' + lang + '/');
</script>
<noscript><a href="/en/">English</a> · <a href="/zh/">中文</a></noscript>
```

# 3) 混合方案：單一文稿集，僅翻譯 UI

**若你不需要翻譯文章內容，只需翻譯導覽列、頁尾等框架元素，此為最佳選擇。**
保持單一的 `/posts/` 文稿集，加入 `_data/i18n.yml`，並根據語言渲染標籤。提供各語言的索引頁面，這些頁面列出相同的文稿，但使用本地化的日期和 UI。

**本地化日期**

```liquid
{% assign locale = page.lang | default: site.default_lang %}
{{ page.date | date: "%B %-d, %Y" }}  {# 或者，如果你有過濾器或外掛，可以使用它們 #}
```

(Jekyll 內建的 `date` 並非完全支援本地化；要實現真正的本地化日期格式，你需要使用外掛或在資料中預先格式化字串。)

---

## 實用技巧

* **Slugs:** 翻譯對應的頁面保持相同的 `ref`；標題則可按語言不同。
* **圖片:** 將共享圖片置於 `/assets/` 並將其排除在本地化之外，以保持 URL 穩定。
* **Sitemaps & SEO:** 生成各語言的網站地圖，或確保你的網站地圖列出了所有語言版本的 URL；在每個語言版本中加入 canonical 標籤。
* **Feeds:** 透過限定集合範圍來建立各語言的訂閱源：在你的訂閱源模板中，按 `lang` 過濾文稿。

---

## 最小可行範例 (無外掛)

1.  準備包含字串的 `_data/i18n.yml`。
2.  準備帶有 `lang` front matter 的 `_en/index.md` 和 `_zh/index.md`。
3.  將帶有 `lang` 和共享 `ref` 的文稿分別置於 `_posts/en/` 和 `_posts/zh/` 目錄下。
4.  版面配置使用 `site.data.i18n[current_lang]` 以及上述尋找對應翻譯頁面的程式碼片段。

如果你能告訴我你目前的儲存庫結構（以及你是直接透過 GitHub Pages 建置還是使用 Actions），我可以為你量身訂製一個可直接使用的配置和一些入門版面配置。