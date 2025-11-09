---
audio: false
date: 2025-09-09
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 為 Jekyll 生成網站地圖檔案
translated: true
type: note
---

**sitemap.xml** 是一個 XML 檔案，用於告知 Google 和 Bing 等搜尋引擎您網站上的頁面。它能協助爬蟲程式更有效地探索和索引您的網站結構。對於 Jekyll 部落格而言，這意味著搜尋引擎可以找到您所有的文章、頁面和翻譯版本（例如您的 `index-zh.html`、`index-fr.html` 等），即使這些內容並未在網站各處都有連結。

### Sitemap 的功能

* 列出您網站的所有重要 URL。
* 提供後設資料，例如最後修改日期 (`<lastmod>`)、更新頻率 (`<changefreq>`) 和優先順序 (`<priority>`)。
* 透過確保爬蟲程式不會遺漏頁面來提升 SEO。

### 如何為 Jekyll 生成 Sitemap

您有幾種方法可以選擇：

#### 1. 使用 `jekyll-sitemap` 外掛（推薦）

1. 在您的 Jekyll 專案 `Gemfile` 中，新增：

   ```ruby
   gem 'jekyll-sitemap'
   ```
2. 在您的 `_config.yml` 中，新增：

   ```yaml
   plugins:
     - jekyll-sitemap
   ```

   （如果您使用 GitHub Pages，`jekyll-sitemap` 已在白名單中，因此可以直接使用。）
3. 當您建置時（透過 `jekyll build` 或若您已設定則透過 `make`），Jekyll 會自動在您的 `_site/` 資料夾中生成 `sitemap.xml`。

#### 2. 手動建立 sitemap 模板

若您偏好更多控制權：

1. 在專案根目錄建立檔案：`/sitemap.xml`。
2. 加入此 Liquid 模板：

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
3. 確保您的 `_config.yml` 中包含 `url: "https://yourdomain.com"`，以便正確生成連結。

#### 3. 驗證

* 建置後，檢查 `_site/sitemap.xml`。
* 將其提交至 Google Search Console 以獲得更好的索引效果。

---

👉 既然您已經有 `_config.yml` 和 `_plugins/`，最簡單的方法就是直接啟用 `jekyll-sitemap`。這樣您就不需要手動維護 XML。

您是否需要我根據您目前的檔案，為您的儲存庫草擬確切的 `_config.yml` 新增內容，以便您直接貼上使用？