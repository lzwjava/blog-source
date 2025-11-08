---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Sortieren von Beiträgen und Notizen
translated: true
type: note
---

### Modifiziertes `_includes/sort.html`

Deine bestehende `sort.html` hat bereits die Sprachauswahl mit 9 Optionen, was perfekt ist. Hier sind keine größeren Änderungen nötig, aber ich habe eine kleine Anpassung im `<span id="post-number">` vorgenommen, um es generischer zu gestalten (z.B. "Einträge" statt "Beiträge"), da wir jetzt Notizen einschließen. Dies kann bei Bedarf dynamisch von deinem JS aktualisiert werden. Hier ist die angepasste Version:

```html
<div class="sort-container">
  <span id="post-number" class="post-number">
    {{ site.posts.size | plus: site.notes.size }} Einträge
    ({{ site.posts.size | plus: site.notes.size | divided_by: 7 | times: 6 }} Übersetzt von <a href="https://openrouter.ai">KI</a>)
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

**Wichtige Änderung**: Die Zählung wurde aktualisiert, um `site.notes.size` einzubeziehen (dies definieren wir weiter unten). Die Formel bleibt gleich, berücksichtigt jetzt aber auch Notizen. Falls dein JS (`index.js`) diesen Span bereits dynamisch basierend auf sichtbaren Elementen aktualisiert, wird es sprachspezifische Zählungen automatisch handhaben.

### Schritt 1: Konfiguriere Notizen als Jekyll-Collection (in `_config.yml`)

Um `_notes` wie `_posts` zu behandeln (damit Jekyll die Markdown-Dateien verarbeitet und sie via `site.notes` verfügbar macht), füge dies deiner `_config.yml` hinzu. Dies ist essentiell – ohne dies haben Notizen keine `url`, `title`, `date` etc. wie Beiträge.

```yaml
collections:
  notes:
    output: true
    permalink: /notes/:path/
```

- `output: true` erzeugt Seiten für Notizen (optional, wenn du nur Daten benötigst).
- `permalink` stellt URLs wie `/notes/es/2025-11-07-tidb-vs-cockroachdb-es/` sicher (anpassen falls nötig).
- Starte deinen Jekyll-Server nach dieser Änderung neu.

Jetzt funktioniert `site.notes` genauso wie `site.posts`, vorausgesetzt deine Notizdateien (z.B. `_notes/es/2025-11-07-tidb-vs-cockroachdb-es.md`) haben ähnliches Frontmatter: `title:`, `date:`, `image:`, `top:`, `translated:`, `generated:`.

### Schritt 2: Modifiziertes Seiten-Layout (z.B. `index.md` oder wo auch immer dein `<ul class="post-list">` steht)

Deine aktuelle Schleife zeigt nur englische Beiträge. Um Notizen hinzuzufügen und alle 9 Sprachen zu unterstützen:

- Definiere einmalig eine Liste der Sprachen.
- Durchlaufe **alle** Sprachen.
- Füge für jede Sprache passende **Beiträge** (aus `_posts/{lang}/`) und **Notizen** (aus `_notes/{lang}/`) als `<li>`-Elemente hinzu.
- Jedes `<li>` erhält `class="... lang-{lang}"`, damit dein JS sie filtern kann (z.B. Ein-/Ausblenden basierend auf dem `#sort-select`-Wert).
- Dies füllt die gesamte Liste im Voraus (versteckt durch JS) und schaltet dann dynamisch zwischen Sprachen um.
- Nach Datum sortieren? Füge `| sort: 'date' | reverse` zu den Schleifen hinzu, wenn du die neuesten zuerst willst (vorausgesetzt Daten sind vergleichbar).

Hier ist das vollständig aktualisierte Layout:

```html
---
layout: page
---
{% include sort.html %}

<ul class="post-list">
  {% if site.posts.size == 0 and site.notes.size == 0 %}
    <li class="list-group-item post-item">Keine Einträge verfügbar.</li>
  {% else %}
    {% assign langs = "en,zh,ja,es,hi,fr,de,ar,hant" | split: "," %}
    {% for lang in langs %}
      {% comment %} Beiträge für diese Sprache {% endcomment %}
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

      {% comment %} Notizen für diese Sprache (genau wie Beiträge) {% endcomment %}
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

**Wichtige Änderungen**:
- **Sprachen-Array**: `{% assign langs = "en,zh,ja,es,hi,fr,de,ar,hant" | split: "," %}` – stimmt mit deinen Select-Optionen überein. Einfach zu pflegen.
- **Beitrags-Schleife**: Entfernte den fest kodierten `en`-Filter; prüft jetzt `post.path contains "_posts/{{ lang }}/"` für jede Sprache.
- **Notiz-Schleife**: Identisch hinzugefügt, prüft `note.path contains "_notes/{{ lang }}/"`. Behandelt Notizen genau wie Beiträge (gleiche Klassen, Attribute, Struktur).
- **Sortierung**: Fügte `| sort: 'date' | reverse` zu beiden Schleifen für chronologische Reihenfolge hinzu (neueste zuerst). Entfernen falls nicht benötigt.
- **Leere-Prüfung**: Aktualisiert, um `site.notes.size` einzubeziehen.
- **Performance**: Dies erzeugt den gesamten Inhalt von ~9 Sprachen zur Build-Zeit. Gut für kleine Seiten; bei großen Seiten ggf. Paginierung oder JS-Fetching in Betracht ziehen.

### Optional: Füge eine Typ-Umschaltung hinzu (Beiträge/Notizen/Beides)

Du erwähntest "add a select/switch , two options select or whatever". Wenn du eine **zweite Dropdown**-Auswahl zum Filtern nach Typ möchtest (z.B. Nur Beiträge, Nur Notizen, oder Beides), füge dies nach der Sprachauswahl in `sort.html` hinzu:

```html
<select id="type-select">
  <option value="both" selected>Beiträge & Notizen</option>
  <option value="posts">Nur Beiträge</option>
  <option value="notes">Nur Notizen</option>
</select>
```

Füge dann ein `data-type`-Attribut zu jedem `<li>` hinzu:
- Für Beiträge: `data-type="posts"`
- Für Notizen: `data-type="notes"`

Aktualisiere dein `index.js`, um Änderungen an `#type-select` zu handhaben (z.B. filtere `.post-item[data-type="notes"]` zum Ein-/Ausblenden). Dies hält es einfach ohne Änderungen an Liquid.

### Nächste Schritte
- Test: Füge eine Beispiel-Notiz wie `_notes/es/2025-11-07-tidb-vs-cockroachdb-es.md` mit Frontmatter (Titel, Datum, etc.) hinzu, baue neu und wechsle zu "Español" in der Dropdown-Auswahl – sie sollte erscheinen.
- JS-Anpassungen: Stelle sicher, dass `index.js` nach `.lang-{value}` filtert und `#post-number` aktualisiert (z.B. zähle sichtbare `<li>`). Falls es Notizen noch nicht handhabt, füge `data-type` wie oben hinzu.
- Falls Pfade abweichen (z.B. kein nachgestelltes `/` in Verzeichnissen), passe die `contains`-Prüfungen an.

Dies integriert Notizen nahtlos und behält dein 9-Sprachen-Setup bei. Lass mich wissen, wenn du JS-Snippets oder weitere Anpassungen benötigst!