---
audio: false
generated: true
image: false
lang: de
layout: post
title: 'Jekyll i18n: Polyglot-Plugin & Ordnermethode'
translated: true
type: note
---

Sie haben drei gute Wege für i18n in einem Jekyll-Blog, von „batteries-included“ bis „bare-bones“. So funktioniert jeder und so richten Sie ihn ein.

# 1) Am einfachsten: Ein Plugin verwenden (jekyll-polyglot)

**Am besten, wenn Sie lokal oder mit CI bauen können.** Der integrierte Builder von GitHub Pages erlaubt die meisten Third-Party-Plugins nicht. Bauen Sie also entweder lokal (`jekyll build`) und pushen Sie das generierte `_site/`-Verzeichnis, oder verwenden Sie GitHub Actions zum Bauen und Veröffentlichen.

**Installation**

```bash
gem install jekyll-polyglot
# oder zur Gemfile hinzufügen:
# gem 'jekyll-polyglot'
```

**\_config.yml**

```yml
plugins:
  - jekyll-polyglot

languages: ["en", "zh", "ja"]   # Ihre Sprachen
default_lang: "en"
exclude_from_localization: ["assets", "images", "CNAME"]  # Statische Pfade gemeinsam nutzen
parallel_localization: true
```

**Struktur der Inhalte**

```
_index.md               # Optionale Startseite
_posts/
  2024-05-01-hello.en.md
  2024-05-01-hello.zh.md
pages/
  about.en.md
  about.zh.md
```

Polyglot baut sprachspezifische URLs wie `/en/about/` und `/zh/about/`. Es stellt auch `site.active_lang` zur Verfügung.

**Sprachumschalter (in Ihrem Layout)**

```liquid
<nav class="lang-switch">
  {% for lang in site.languages %}
    {% if lang == site.active_lang %}
      <span>{{ lang }}</span>
    {% else %}
      <a href="{{ page.url | prepend:'/' | replace_first:'/' | prepend:'/' | absolute_url | replace: '/' | relative_url | prepend:'/' }}">
        {%- comment -%}
        Wir bauen die aktuelle URL für jede Sprache neu:
        {%- endcomment -%}
      </a>
    {% endif %}
  {% endfor %}
</nav>
```

Ein einfacherer Ansatz mit Polyglot ist:

```liquid
<nav>
  {% for lang in site.languages %}
    <a href="{{ site.baseurl_root }}/{{ lang }}{{ page.permalink | default: page.url }}">{{ lang }}</a>
  {% endfor %}
</nav>
```

**UI-Strings über Data-Dateien**
Erstellen Sie `_data/i18n.yml`:

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

Verwendung in Templates:

```liquid
{{ site.data.i18n[site.active_lang].nav.home }}
```

**SEO (hreflang)**
Im `<head>` Ihres Layouts:

```liquid
{% assign langs = site.languages %}
{% for l in langs %}
  <link rel="alternate" hreflang="{{ l }}" href="{{ site.url }}/{{ l }}{{ page.url }}" />
{% endfor %}
<link rel="alternate" hreflang="x-default" href="{{ site.url }}/{{ site.default_lang }}{{ page.url }}" />
```

# 2) Ohne Plugin: Sprachspezifische Ordner + Liquid

**Am besten, wenn Sie den integrierten Builder von GitHub Pages verwenden müssen.**

**Struktur**

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

**Aktuelle Sprache setzen**
In jedem Page Front Matter hinzufügen:

```yml
---
layout: default
lang: en
---
```

oder aus dem Pfad ableiten:

```liquid
{% assign current_lang = page.lang | default: page.path | split:'/' | first | remove:'_' %}
```

**Querverweise zwischen Übersetzungen**
Verwenden Sie eine gemeinsame ID im Front Matter:

```yml
---
layout: post
lang: en
ref: hello-post
---
```

In der chinesischen Version:

```yml
---
layout: post
lang: zh
ref: hello-post
---
```

Dann im Layout die zugehörigen Seiten finden:

```liquid
{% assign siblings = site.pages | concat: site.posts | where:"ref", page.ref %}
{% for s in siblings %}
  {% unless s.url == page.url %}
    <a href="{{ s.url }}">{{ s.lang }}</a>
  {% endunless %}
{% endfor %}
```

**UI-Strings ohne Plugins**
Verwenden Sie `_data/i18n.yml` wie oben und wählen Sie die Sprache über `current_lang`.

**Weiterleitung für Standardsprache (optional)**
Erstellen Sie `index.html` im Root-Verzeichnis:

```html
<!doctype html>
<meta charset="utf-8">
<script>
  const lang = (navigator.language || '').toLowerCase().startsWith('zh') ? 'zh' : 'en';
  location.replace('/' + lang + '/');
</script>
<noscript><a href="/en/">English</a> · <a href="/zh/">中文</a></noscript>
```

# 3) Hybrid: Ein Satz Posts, nur UI übersetzen

**Am besten, wenn Sie Artikel nicht übersetzen, sondern nur die Navigation/Footer.**
Behalten Sie einen einzigen Satz `/posts/`, fügen Sie `_data/i18n.yml` hinzu und rendern Sie die Beschriftungen nach Sprache. Bieten Sie sprachspezifische Indexseiten an, die dieselben Posts auflisten, aber mit lokalisierten Datumsangaben und UI.

**Lokalisierte Datumsangaben**

```liquid
{% assign locale = page.lang | default: site.default_lang %}
{{ page.date | date: "%B %-d, %Y" }}  {# oder Filter/Plugins verwenden, falls vorhanden #}
```

(Jekylls eingebaute `date`-Funktion ist nicht vollständig lokalisierungsfähig; für echte Lokalisierung benötigen Sie ein Plugin oder vorformatierte Strings in Data.)

---

## Praktische Tipps

* **Slugs:** Verwenden Sie denselben `ref` für Übersetzungen; lassen Sie die Titel je Sprache variieren.
* **Bilder:** Legen Sie gemeinsame Bilder in `/assets/` und schließen Sie sie von der Lokalisierung aus, damit die URLs stabil bleiben.
* **Sitemaps & SEO:** Generieren Sie sprachspezifische Sitemaps oder stellen Sie sicher, dass Ihre Sitemap alle Sprach-URLs auflistet; fügen Sie Canonical-Tags innerhalb jeder Sprachversion hinzu.
* **Feeds:** Erstellen Sie sprachspezifische Feeds, indem Sie Collections filtern: Filtern Sie Posts nach `lang` in Ihrem Feed-Template.

---

## Minimal funktionierendes Beispiel (ohne Plugin)

1.  `_data/i18n.yml` mit Strings.
2.  `_en/index.md` und `_zh/index.md` mit `lang` im Front Matter.
3.  Posts unter `_posts/en/` und `_posts/zh/` mit `lang` und gemeinsamem `ref`.
4.  Layout verwendet `site.data.i18n[current_lang]` und den oben gezeigten Snippet für die Suche nach zugehörigen Seiten.

Wenn Sie mir Ihre aktuelle Repo-Struktur mitteilen (und ob Sie direkt auf GitHub Pages oder über Actions bauen), kann ich eine passende Konfiguration und ein paar Starter-Layouts für Sie erstellen.