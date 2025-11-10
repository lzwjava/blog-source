---
audio: false
generated: true
lang: de
layout: post
title: 'Beschleunigung von Jekyll-Builds: Untersuchung von Multithreading-Ansätzen'
translated: true
type: note
---

Jekylls Build-Prozess ist standardmäßig single-threaded, was bei großen Sites langsam sein kann. Obwohl es keine integrierte Konfigurationsoption in Jekyll gibt, um multithreaded Builds zu aktivieren, können Sie einige Ansätze erkunden, um Parallelität zu erreichen. Im Folgenden skizziere ich die Möglichkeiten, Herausforderungen und praktischen Schritte auf der Grundlage verfügbarer Informationen und technischer Überlegungen.

### Warum Jekyll-Builds Single-Threaded sind
Jekyll verarbeitet Seiten sequentiell, um sicherzustellen, dass Abhängigkeiten (wie `site.related_posts` oder Liquid-Templates) korrekt behandelt werden. Einige Komponenten, wie Liquid und bestimmte Plugins, sind möglicherweise nicht thread-sicher, was Multithreading erschwert (). Dieses Design priorisiert Korrektheit über Geschwindigkeit, aber bei großen Sites kann dies zu Build-Zeiten von mehreren Minuten führen (,).[](https://github.com/jekyll/jekyll/issues/9485)[](https://github.com/jekyll/jekyll/issues/1855)[](https://github.com/jekyll/jekyll/issues/4297)

### Ansätze für Multithreaded Jekyll-Builds
Hier sind potenzielle Möglichkeiten, Parallelität in Jekyll-Builds einzuführen, insbesondere im Kontext eines GitHub Actions Workflows wie dem von Ihnen bereitgestellten:

#### 1. **Verwenden eines benutzerdefinierten Plugins für Multithreaded Rendering**
Ein Proof-of-Concept-Plugin für multithreaded Rendering wurde vorgeschlagen (). Es reduzierte die Build-Zeit in einem Testfall von 45 Sekunden auf 10 Sekunden, hatte jedoch Probleme mit Thread-Safety, was zu falschen Seiteninhalten führte. Das Plugin kollidierte auch mit Plugins wie `jekyll-feed`, die auf sequentiellem Rendering angewiesen sind.[](https://github.com/jekyll/jekyll/issues/9485)

**Schritte zum Ausprobieren eines benutzerdefinierten Plugins:**
- **Plugin erstellen**: Implementieren Sie ein Ruby-Plugin, das die `Site`-Klasse von Jekyll erweitert, um das Seitenrendering zu parallelisieren. Sie könnten beispielsweise die `render_pages`-Methode modifizieren, um Rubys `Thread`-Klasse oder einen Thread-Pool zu verwenden ().[](https://github.com/jekyll/jekyll/issues/9485)
  ```ruby
  module Jekyll
    module UlyssesZhan::MultithreadRendering
      def render_pages(*args)
        @rendering_threads = []
        super # Ursprüngliche Methode aufrufen
        @rendering_threads.each(&:join) # Auf Abschluss der Threads warten
      end
    end
  end
  Jekyll::Site.prepend(Jekyll::UlyssesZhan::MultithreadRendering)
  ```
- **Zur Gemfile hinzufügen**: Platzieren Sie das Plugin in Ihrem `_plugins`-Verzeichnis und stellen Sie sicher, dass es von Jekyll geladen wird.
- **Auf Thread-Safety testen**: Da Liquid und einige Plugins (z.B. `jekyll-feed`) brechen könnten, testen Sie gründlich. Möglicherweise müssen Sie Liquid patchen oder Multithreading für bestimmte Funktionen vermeiden ().[](https://github.com/jekyll/jekyll/issues/9485)
- **Mit GitHub Actions integrieren**: Aktualisieren Sie Ihren Workflow, um das Plugin in Ihrem Repository einzubinden. Stellen Sie sicher, dass die `jekyll-build-pages`-Aktion Ihr benutzerdefiniertes Jekyll-Setup verwendet:
  ```yaml
  - name: Build with Jekyll
    uses: actions/jekyll-build-pages@v1
    with:
      source: ./
      destination: ./_site
    env:
      BUNDLE_GEMFILE: ./Gemfile # Stellen Sie sicher, dass Ihre benutzerdefinierte Gemfile mit dem Plugin verwendet wird
  ```

**Herausforderungen**:
- Thread-Safety-Probleme mit Liquid und Plugins wie `jekyll-feed` ().[](https://github.com/jekyll/jekyll/issues/9485)
- Potenzial für falsches Seitenrendering (z.B. erscheint der Inhalt einer Seite in einer anderen).
- Erfordert Ruby-Expertise zum Debuggen und Warten.

#### 2. **Parallelisieren von Builds mit mehreren Konfigurationen**
Anstatt einen einzelnen Build zu multithreaden, können Sie Ihre Site in kleinere Teile aufteilen (z.B. nach Collection oder Verzeichnis) und sie mit mehreren Jekyll-Prozessen parallel bauen. Dieser Ansatz vermeidet Thread-Safety-Probleme, erfordert aber mehr Setup.

**Schritte**:
- **Site aufteilen**: Organisieren Sie Ihre Site in Collections (z.B. `posts`, `pages`, `docs`) oder Verzeichnisse und erstellen Sie separate `_config.yml`-Dateien für jede (,).[](https://amcrouch.medium.com/configuring-environments-when-building-sites-with-jekyll-dd6eb2603c39)[](https://coderwall.com/p/tfcj2g/using-different-build-configuration-in-jekyll-site)
  ```yaml
  # _config_posts.yml
  collections:
    posts:
      output: true
  destination: ./_site/posts

  # _config_pages.yml
  collections:
    pages:
      output: true
  destination: ./_site/pages
  ```
- **GitHub Actions Workflow aktualisieren**: Modifizieren Sie Ihren Workflow, um mehrere Jekyll-Builds parallel auszuführen, jeder mit einer anderen Konfigurationsdatei.
  ```yaml
  name: Build Jekyll Site
  on:
    push:
      branches: [main]
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
        - name: Setup Ruby
          uses: ruby/setup-ruby@v1
          with:
            ruby-version: '3.1'
            bundler-cache: true
        - name: Build Posts
          run: bundle exec jekyll build --config _config_posts.yml
        - name: Build Pages
          run: bundle exec jekyll build --config _config_pages.yml
        - name: Combine Outputs
          run: |
            mkdir -p ./_site
            cp -r ./_site/posts/* ./_site/
            cp -r ./_site/pages/* ./_site/
        - name: Deploy
          uses: actions/upload-artifact@v4
          with:
            name: site
            path: ./_site
  ```
- **Ausgaben kombinieren**: Nach den parallelen Builds führen Sie die Ausgabeverzeichnisse in einem einzigen `_site`-Ordner für das Deployment zusammen.

**Herausforderungen**:
- Verwalten von Abhängigkeiten zwischen Collections (z.B. `site.related_posts`).
- Erhöhte Komplexität in Konfiguration und Deployment.
- Skaliert möglicherweise nicht gut für Sites mit stark gekoppelten Inhalten.

#### 3. **Verwenden eines Thread-Pools für große Sites**
Ein Pull Request für das `amp-jekyll`-Plugin schlug die Verwendung eines Thread-Pools vor, um Seiten zu verarbeiten, mit einer konfigurierbaren Anzahl von Threads, um das System nicht zu überlasten (). Dieser Ansatz balanciert Leistung und Ressourcennutzung.[](https://github.com/juusaw/amp-jekyll/pull/26)

**Schritte**:
- **Thread-Pool implementieren**: Modifizieren oder erstellen Sie ein Plugin, das `Thread::Queue` von Ruby verwendet, um eine feste Anzahl von Worker-Threads zu verwalten (z.B. 4 oder 8, abhängig von Ihrem System).
  ```ruby
  require 'thread'

  module Jekyll
    module ThreadPoolRendering
      def render_pages(*args)
        queue = Queue.new
        site.pages.each { |page| queue << page }
        threads = (1..4).map do # 4 Threads
          Thread.new do
            until queue.empty?
              page = queue.pop(true) rescue nil
              page&.render_with_liquid(site)
            end
          end
        end
        threads.each(&:join)
        super
      end
    end
  end
  Jekyll::Site.prepend(Jekyll::ThreadPoolRendering)
  ```
- **Konfigurationsoption hinzufügen**: Erlauben Sie Benutzern, Multithreading zu aktivieren/deaktivieren oder die Anzahl der Threads in `_config.yml` festzulegen:
  ```yaml
  multithreading:
    enabled: true
    thread_count: 4
  ```
- **Mit Workflow integrieren**: Stellen Sie sicher, dass das Plugin in Ihrem Repository enthalten ist und während des GitHub Actions Builds geladen wird.

**Herausforderungen**:
- Ähnliche Thread-Safety-Probleme wie beim ersten Ansatz.
- Context-Switching-Overhead für große Sites mit vielen kurzen Tasks ().[](https://github.com/juusaw/amp-jekyll/pull/26)
- Erfordert Tests, um Kompatibilität mit allen Plugins sicherzustellen.

#### 4. **Optimieren ohne Multithreading**
Wenn sich Multithreading als zu komplex oder riskant erweist, können Sie den single-threaded Build-Prozess optimieren:
- **Inkrementelle Builds aktivieren**: Verwenden Sie `jekyll build --incremental`, um nur geänderte Dateien neu zu bauen (,). Fügen Sie dies Ihrem Workflow hinzu:[](https://github.com/jekyll/jekyll/blob/master/lib/jekyll/commands/build.rb)[](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)
  ```yaml
  - name: Build with Jekyll
    uses: actions/jekyll-build-pages@v1
    with:
      source: ./
      destination: ./_site
      incremental: true
  ```
- **Plugin-Nutzung reduzieren**: Benutzerdefinierte Plugins können Builds erheblich verlangsamen (). Überprüfen und entfernen Sie unnötige Plugins.[](https://github.com/jekyll/jekyll/issues/4297)
- **Schnellere Converter verwenden**: Wechseln Sie von Kramdown zu einem schnelleren Markdown-Prozessor wie CommonMark, oder testen Sie Pandoc für spezifische Anwendungsfälle ().[](https://github.com/jekyll/jekyll/issues/9485)
- **Abhängigkeiten cachen**: Stellen Sie `bundler-cache: true` in Ihrem GitHub Actions Workflow sicher, um die Neuinstallation von Gems zu vermeiden ().[](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)

### Empfehlungen
- **Beginnen Sie mit inkrementellen Builds**: Dies ist der einfachste Weg, Builds zu beschleunigen, ohne Thread-Safety-Probleme zu riskieren. Fügen Sie `--incremental` zu Ihrem Workflow hinzu und testen Sie die Auswirkung.
- **Experimentieren Sie mit einem Thread-Pool-Plugin**: Wenn Sie Ruby-Expertise haben, versuchen Sie, ein Thread-Pool-Plugin mit einer konfigurierbaren Anzahl von Threads zu implementieren (Option 3). Beginnen Sie mit einer kleinen Site, um Thread-Safety zu testen.
- **Vermeiden Sie vorerst vollständiges Multithreading**: Angesichts der Thread-Safety-Bedenken mit Liquid und Plugins () könnte vollständiges Multithreading signifikante Refaktorierung oder einen benutzerdefinierten Liquid-Fork erfordern, was unpraktisch sein könnte, es sei denn, Sie tragen zur Kernentwicklung von Jekyll bei.[](https://github.com/jekyll/jekyll/issues/9485)
- **Build-Zeiten überwachen**: Verwenden Sie GitHub Actions Logs, um Build-Zeiten zu messen und Engpässe zu identifizieren. Beispielsweise deutet eine Site, die 6 Minuten zum Bauen braucht (), darauf hin, dass Plugins oder die Verarbeitung großer Assets das Problem sein könnten.[](https://github.com/jekyll/jekyll/issues/1855)

### GitHub Actions Beispiel mit inkrementellen Builds
Hier ist eine aktualisierte Version Ihres Workflows mit aktivierten inkrementellen Builds:
```yaml
name: Build Jekyll Site
on:
  push:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.1'
          bundler-cache: true
      - name: Build with Jekyll
        uses: actions/jekyll-build-pages@v1
        with:
          source: ./
          destination: ./_site
          incremental: true
      - name: Deploy
        uses: actions/upload-artifact@v4
        with:
          name: site
          path: ./_site
```

### Caveats
- **Thread Safety**: Multithreading in Jekyll ist experimentell und kann Plugins brechen oder falsche Ausgaben produzieren (). Testen Sie es gründlich zuerst an einer kleinen Site.[](https://github.com/jekyll/jekyll/issues/9485)
- **GitHub Actions Limits**: Parallele Builds (Option 2) erhöhen die Ressourcennutzung, stellen Sie also sicher, dass Ihr Workflow innerhalb der Limits des Free-Tiers von GitHub bleibt.
- **Jekyll 5 Potenzial**: Zukünftige Versionen von Jekyll könnten Multithreading nativ adressieren, da es diskutiert wurde (). Vorerst sind benutzerdefinierte Lösungen nötig.[](https://github.com/jekyll/jekyll/issues/9485)

Wenn Sie Hilfe bei der Implementierung eines spezifischen Ansatzes benötigen (z.B. Schreiben eines Plugins oder Aufteilen von Builds), lassen Sie es mich wissen, und ich kann detailliertere Anleitung oder Code bereitstellen!