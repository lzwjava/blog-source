---
audio: false
date: 2025-09-09
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Erstellen von Sitemap-Dateien für Jekyll
translated: true
type: note
---

Eine **sitemap.xml** ist eine XML-Datei, die Suchmaschinen wie Google und Bing über die Seiten Ihrer Website informiert. Sie hilft Crawlern, die Struktur Ihrer Website effizienter zu entdecken und zu indexieren. Für einen Jekyll-Blog bedeutet das, dass Suchmaschine alle Ihre Beiträge, Seiten und Übersetzungen (wie Ihre `index-zh.html`, `index-fr.html`, etc.) finden können, selbst wenn diese nicht überall verlinkt sind.

### Was eine Sitemap bewirkt

* Listet alle wichtigen URLs Ihrer Website auf.
* Stellt Metadaten wie das letzte Änderungsdatum (`<lastmod>`), die Änderungshäufigkeit (`<changefreq>`) und die Priorität (`<priority>`) bereit.
* Verbessert die SEO, indem sichergestellt wird, dass Crawler keine Seiten übersehen.

### Generierung für Jekyll

Sie haben mehrere Möglichkeiten:

#### 1. Verwenden des `jekyll-sitemap` Plugins (empfohlen)

1. Fügen Sie in der `Gemfile` Ihres Jekyll-Projekts hinzu:

   ```ruby
   gem 'jekyll-sitemap'
   ```
2. Fügen Sie in Ihrer `_config.yml` hinzu:

   ```yaml
   plugins:
     - jekyll-sitemap
   ```

   (Wenn Sie GitHub Pages verwenden, ist `jekyll-sitemap` bereits auf der Whitelist und funktioniert direkt.)
3. Wenn Sie builden (`jekyll build` oder via `make`, falls eingerichtet), generiert Jekyll automatisch eine `sitemap.xml` in Ihrem `_site/`-Ordner.

#### 2. Manuelles Erstellen einer Sitemap-Vorlage

Wenn Sie mehr Kontrolle bevorzugen:

1. Erstellen Sie eine Datei im Projekt-Root: `/sitemap.xml`.
2. Fügen Sie diese Liquid-Vorlage hinzu:

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
3. Stellen Sie sicher, dass Ihre `_config.yml` `url: "https://ihredomain.com"` enthält, damit die Links korrekt generiert werden.

#### 3. Verifizieren

* Überprüfen Sie nach dem Builden die `_site/sitemap.xml`.
* Reichen Sie sie in der Google Search Console für eine bessere Indexierung ein.

---

👉 Da Sie bereits `_config.yml` und `_plugins/` haben, ist der einfachste Weg, `jekyll-sitemap` zu aktivieren. So müssen Sie die XML-Datei nicht manuell pflegen.

Möchten Sie, dass ich den genauen `_config.yml`-Zusatz für Ihr Repository (basierend auf Ihren aktuellen Dateien) formuliere, damit Sie ihn direkt einfügen können?