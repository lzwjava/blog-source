---
audio: false
generated: true
image: false
lang: de
layout: post
title: Vorkompilierte sprachspezifische Indexseiten
translated: true
type: note
---

Ja, Sie können separate Indexseiten für verschiedene Sprachen vorübersetzen (z. B. `index-zh.html`, `index-en.html`), um die Leistung und Benutzererfahrung zu verbessern, insbesondere wenn Ihre Site eine große Anzahl von Beiträgen hat oder Sie die clientseitige JavaScript-Verarbeitung reduzieren möchten. Dieser Ansatz beinhaltet die Generierung statischer HTML-Dateien für jede Sprache während des Build-Prozesses, anstatt sich darauf zu verlassen, dass JavaScript die Beiträge dynamisch auf der Client-Seite filtert und sortiert.

Im Folgenden werde ich skizzieren, wie Sie dies mit Jekyll erreichen können, mit Schwerpunkt auf der Erstellung separater Indexseiten für jede Sprache (`index-zh.html`, `index-en.html`, usw.) unter Beibehaltung der Funktionalität Ihres aktuellen Setups. Dies nutzt das Build-System von Jekyll, um die gefilterten Beitragslisten für jede Sprache vorab zu berechnen, was den Bedarf an komplexem clientseitigem JavaScript reduziert.

---

### Vorgehensweise zum Vorübersetzen von `index-zh.html`, `index-en.html`, etc.

Um sprachspezifische Indexseiten vorzuübersetzen, können Sie separate Jekyll-Seitenvorlagen für jede Sprache erstellen und Liquid verwenden, um Beiträge während des Build-Prozesses nach Sprache zu filtern. Auf diese Weise enthält jede Seite (`index-en.html`, `index-zh.html`, usw.) nur die relevanten Beiträge, und die Sortier-/Filterlogik wird zur Build-Zeit und nicht im Browser abgehandelt.

So können Sie es machen:

---

#### 1. Erstellen Sie sprachspezifische Seitenvorlagen

Erstellen Sie separate Seiten-Dateien im Stammverzeichnis Ihres Jekyll-Projekts für jede Sprache, wie z.B.:

- `index-en.html`
- `index-zh.html`
- `index-ja.html`
- ...und so weiter für andere Sprachen (`es`, `hi`, `fr`, `de`, `ar`, `hant`, etc.).

Jede Datei verwendet eine ähnliche Struktur wie Ihr bereitgestellter Code, filtert aber Beiträge für eine bestimmte Sprache mit Liquid. Hier ist ein Beispiel für `index-en.html`:

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

Für `index-zh.html` würden Sie das `lang`-Frontmatter und den `where`-Filter ersetzen:

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
  <!-- Gleicher sort-select wie oben -->
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

<!-- Gleicher Footer wie oben -->
```

Wiederholen Sie dies für jede Sprache (`ja`, `es`, `hi`, `fr`, `de`, `ar`, `hant`, etc.) und passen Sie das `lang`-Frontmatter und den `where`-Filter entsprechend an.

---

#### 2. Aktualisieren Sie das Post-Frontmatter

Stellen Sie sicher, dass jeder Beitrag in Ihrem `_posts`-Verzeichnis eine Frontmatter-Variable `lang` hat, die seiner Sprache entspricht (z.B. `en`, `zh`, `ja`, etc.). Zum Beispiel:

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

Dies ermöglicht es dem `where`-Filter, Beiträge korrekt nach Sprache zu identifizieren.

Wenn Ihre Beiträge in Unterverzeichnissen wie `_posts/en/`, `_posts/zh/`, etc. organisiert sind, können Sie die Sprache aus dem Pfad ableiten, anstatt eine `lang`-Variable zu verwenden. Zum Beispiel in `index-en.html`:

```liquid
{% assign en_posts = site.posts | where_exp: "post", "post.path contains '_posts/en/'" %}
```

---

#### 3. Vereinfachen Sie das JavaScript

Da die Sprachfilterung nun zur Build-Zeit erfolgt, können Sie das JavaScript so vereinfachen, dass es nur die Sortierung (z.B. nach Datum oder Author Picks) und die Navigation zwischen den Sprachseiten behandelt. Hier ist eine aktualisierte Version des JavaScript:

```javascript
window.addEventListener('load', function () {
  const sortSelect = document.getElementById('sort-select');
  const postNumber = document.getElementById('post-number');
  const postList = document.querySelector('.post-list');

  function updatePosts() {
    const selectedValue = sortSelect.value;
    const [sortOption, langFilter] = selectedValue.split('|');

    // Wenn die gewählte Sprache nicht der aktuellen Seite entspricht, umleiten
    const currentLang = '{{ page.lang }}';
    if (langFilter !== currentLang && langFilter !== 'all' && langFilter !== 'original' && sortOption !== 'author-picks') {
      window.location.href = `/${langFilter}/?sort=${selectedValue}`;
      return;
    }

    // Alle Beiträge erfassen
    const posts = document.querySelectorAll('.post-list li.post-item');
    let processedPosts = [];

    if (sortOption === 'author-picks') {
      // Filtere Beiträge mit 'data-top' > 0
      processedPosts = Array.from(posts)
        .filter(post => parseInt(post.dataset.top || 0, 10) > 0)
        .map(post => ({ element: post }));
    } else if (sortOption === 'date-desc' && langFilter === 'original') {
      // Filtere originale (nicht übersetzte, nicht generierte) Beiträge
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
      // Sortiere absteigend nach Datum
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

    // Bestehende Liste leeren
    postList.innerHTML = '';

    // Verarbeitete Beiträge anhängen oder eine Nachricht anzeigen
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

    // Beitragszahl aktualisieren
    const translatedCount = processedPosts.filter(item => item.element && item.element.dataset.translated === 'true').length;
    postNumber.innerHTML = `${processedPosts.length} posts (${translatedCount} by <a href="https://mistral.ai">AI</a>)`;

    // Liste anzeigen
    postList.style.display = 'block';
  }

  // Aus localStorage wiederherstellen oder Standard setzen
  const savedSort = localStorage.getItem('sortOption');
  if (savedSort) {
    sortSelect.value = savedSort;
  } else {
    sortSelect.value = 'date-desc|{{ page.lang }}';
  }

  updatePosts();

  // Event-Listener für Dropdown-Änderungen
  sortSelect.addEventListener('change', function () {
    localStorage.setItem('sortOption', sortSelect.value);
    updatePosts();
  });
});
```

Wichtige Änderungen:
- Das Skript prüft, ob die gewählte Sprache der Sprache der aktuellen Seite (`{{ page.lang }}`) entspricht. Wenn nicht, leitet es zur entsprechenden Sprachseite um (z.B. `/zh/` für Chinesisch).
- Die Sprachfilterung ist nicht mehr nötig, da die Beiträge bereits durch die Liquid-Vorlage vorgefiltert sind.

---

#### 4. Konfigurieren Sie Permalinks und Navigation

Stellen Sie sicher, dass jede sprachspezifische Seite einen eindeutigen Permalink in ihrem Frontmatter hat (z.B. `permalink: /en/` für `index-en.html`). Dies ermöglicht es Benutzern, direkt auf `/en/`, `/zh/`, usw. zuzugreifen.

Sie sollten möglicherweise auch die Navigation Ihrer Site aktualisieren, um Links zu diesen sprachspezifischen Seiten einzufügen. Zum Beispiel in Ihrem Layout oder Header:

```html
<nav>
  <a href="/en/">English</a>
  <a href="/zh/">中文</a>
  <a href="/ja/">日本語</a>
  <!-- Fügen Sie andere Sprachen hinzu -->
</nav>
```

---

#### 5. Behandeln Sie die "All" und "Original" Filter

Für die Optionen "All" und "Original" im Dropdown:
- **All**: Sie können eine `index.html` erstellen, die alle Beiträge enthält (ähnlich Ihrem ursprünglichen Setup), oder zu einer der sprachspezifischen Seiten weiterleiten.
- **Original**: Sie können eine `index-original.html` erstellen, die Beiträge mit `translated: false` und `generated: false` filtert:

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
  <!-- Gleicher sort-select -->
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

<!-- Gleicher Footer -->
```

---

#### 6. Vorteile des Vorübersetzens

- **Leistung**: Das Filtern von Beiträgen zur Build-Zeit reduziert die clientseitige JavaScript-Verarbeitung, was die Site schneller macht, insbesondere für Benutzer mit langsameren Geräten oder Verbindungen.
- **SEO**: Suchmaschinen können sprachspezifische Seiten (`/en/`, `/zh/`, usw.) besser indexieren, was die Auffindbarkeit verbessert.
- **Einfacheres JavaScript**: Das JavaScript muss nur die Sortierung und Navigation behandeln, nicht die Sprachfilterung.
- **Zuverlässigkeit**: Vorübersetzte Seiten vermeiden clientseitige Fehler (z.B. die "Known bug pending fix"-Meldung in Ihrem ursprünglichen Code).

---

#### 7. Überlegungen

- **Build-Zeit**: Das Vorübersetzen mehrerer Indexseiten erhöht die Build-Zeit, insbesondere wenn Sie viele Beiträge oder Sprachen haben. Dies ist jedoch normalerweise vernachlässigbar, es sei denn, Sie haben Tausende von Beiträgen.
- **Wartung**: Sie müssen mehrere Index-Dateien (`index-en.html`, `index-zh.html`, usw.) pflegen. Um Duplizierung zu reduzieren, können Sie Jekyll-Includes oder Layouts verwenden, um gemeinsamen Code zu teilen.
- **Dynamische Sortierung**: Das JavaScript behandelt weiterhin die Sortierung (z.B. Author Picks, date-desc), aber Sie könnten vorsortierte Versionen jeder Seite vorab berechnen, wenn Sie eine vollständig statische Ausgabe wünschen (dies würde jedoch mehr Dateien erzeugen, z.B. `index-en-picks.html`).

---

#### 8. Beispiel-Verzeichnisstruktur

Ihr Jekyll-Projekt könnte so aussehen:

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

#### 9. Testen und Bereitstellen

- Testen Sie lokal mit `jekyll serve`, um sicherzustellen, dass jede Sprachseite (`/en/`, `/zh/`, usw.) die korrekten Beiträge anzeigt.
- Verifizieren Sie, dass die Dropdown-Navigation korrekt zwischen den Sprachseiten weiterleitet.
- Stellen Sie auf Ihrer Hosting-Plattform (z.B. GitHub Pages) bereit und prüfen Sie, ob die Permalinks wie erwartet funktionieren.

---

### Referenzen
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Mistral AI](https://mistral.ai)

Wenn Sie weitere Fragen haben oder Hilfe bei bestimmten Teilen der Implementierung benötigen, lassen Sie es mich wissen!