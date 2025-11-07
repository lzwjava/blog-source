---
audio: false
generated: true
image: false
lang: zh
layout: post
model: x-ai/grok-4-fast
title: 文章与笔记排序
translated: true
---

### 修改后的 `_includes/sort.html`

您现有的 `sort.html` 已包含带有9个选项的语言选择器，这非常完美。此处无需重大更改，但我在 `<span id="post-number">` 中添加了一个小注释，使其更通用（例如，使用"entries"而不是"posts"），因为我们现在包含了笔记。如果需要，这可以通过您的JS动态更新。以下是调整后的版本：

```html
<div class="sort-container">
  <span id="post-number" class="post-number">
    {{ site.posts.size | plus: site.notes.size }} 个条目
    ({{ site.posts.size | plus: site.notes.size | divided_by: 7 | times: 6 }} 由 <a href="https://openrouter.ai">AI</a> 翻译)
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

**关键更改**：更新了计数以包含 `site.notes.size`（我们将在下面定义这个）。公式保持不变，但现在考虑了笔记。如果您的JS（`index.js`）已经根据可见项动态更新此span，它将自动处理特定语言的计数。

### 步骤 1：将笔记配置为 Jekyll 集合（在 `_config.yml` 中）

要将 `_notes` 像 `_posts` 一样对待（以便 Jekyll 处理 Markdown 文件并通过 `site.notes` 公开它们），请将此添加到您的 `_config.yml` 中。这至关重要——没有它，笔记将无法像文章一样拥有 `url`、`title`、`date` 等属性。

```yaml
collections:
  notes:
    output: true
    permalink: /notes/:path/
```

- `output: true` 为笔记生成页面（如果只需要数据，则为可选）。
- `permalink` 确保 URL 如 `/notes/es/2025-11-07-tidb-vs-cockroachdb-es/`（如果需要，请调整）。
- 添加此配置后，请重新启动 Jekyll 服务器。

现在 `site.notes` 就像 `site.posts` 一样工作，前提是您的笔记文件（例如 `_notes/es/2025-11-07-tidb-vs-cockroachdb-es.md`）具有类似的前言数据：`title:`、`date:`、`image:`、`top:`、`translated:`、`generated:`。

### 步骤 2：修改后的页面布局（例如 `index.md` 或您的 `<ul class="post-list">` 所在的位置）

您当前的循环仅显示英文文章。要添加笔记并支持所有9种语言：

- 定义一次语言列表。
- 循环遍历**所有**语言。
- 对于每种语言，添加匹配的**文章**（来自 `_posts/{lang}/`）和**笔记**（来自 `_notes/{lang}/`）作为 `<li>` 项。
- 每个 `<li>` 获得 `class="... lang-{lang}"`，以便您的JS可以过滤它们（例如，根据 `#sort-select` 值隐藏/显示）。
- 这将预先填充整个列表（由JS隐藏），然后动态切换语言。
- 按日期排序？如果您希望最新的在前（假设日期是可比较的），请在循环中添加 `| sort: 'date' | reverse`。

以下是完整的更新后布局：

```html
---
layout: page
---
{% include sort.html %}

<ul class="post-list">
  {% if site.posts.size == 0 and site.notes.size == 0 %}
    <li class="list-group-item post-item">暂无可用条目。</li>
  {% else %}
    {% assign langs = "en,zh,ja,es,hi,fr,de,ar,hant" | split: "," %}
    {% for lang in langs %}
      {% comment %} 此语言的文章 {% endcomment %}
      {% for post in site.posts | sort: 'date'