---
audio: false
generated: true
lang: fr
layout: post
title: 'Accélérer les Compilations Jekyll : Explorer les Approches Multithread'
translated: true
type: note
---

Le processus de construction de Jekyll est mono-thread par défaut, ce qui peut être lent pour les sites volumineux. Bien qu'il n'y ait pas d'option de configuration intégrée dans Jekyll pour activer les builds multithreads, vous pouvez explorer certaines approches pour obtenir du parallélisme. Ci-dessous, je décris les possibilités, les défis et les étapes pratiques basées sur les informations disponibles et les considérations techniques.

### Pourquoi les builds Jekyll sont mono-threads
Jekyll traite les pages séquentiellement pour garantir que les dépendances (comme `site.related_posts` ou les templates Liquid) sont gérées correctement. Certains composants, comme Liquid et certaines extensions, pourraient ne pas être thread-safe, ce qui complique le multithreading (). Cette conception privilégie l'exactitude sur la vitesse, mais pour les sites volumineux, cela peut entraîner des temps de build de plusieurs minutes (,).[](https://github.com/jekyll/jekyll/issues/9485)[](https://github.com/jekyll/jekyll/issues/1855)[](https://github.com/jekyll/jekyll/issues/4297)

### Approches pour des builds Jekyll multithreads
Voici des moyens potentiels d'introduire le parallélisme dans les builds Jekyll, particulièrement dans le contexte d'un workflow GitHub Actions comme celui que vous avez fourni :

#### 1. **Utiliser une extension personnalisée pour le rendu multithread**
Une extension de preuve de concept pour le rendu multithread a été proposée (). Elle a réduit le temps de build de 45 secondes à 10 secondes dans un cas de test mais avait des problèmes de thread safety, conduisant à un contenu de page incorrect. L'extension entrait également en conflit avec des extensions comme `jekyll-feed`, qui dépendent d'un rendu séquentiel.[](https://github.com/jekyll/jekyll/issues/9485)

**Étapes pour essayer une extension personnalisée :**
- **Créer une extension** : Implémentez une extension Ruby qui étend la classe `Site` de Jekyll pour paralléliser le rendu des pages. Par exemple, vous pourriez modifier la méthode `render_pages` pour utiliser la classe `Thread` de Ruby ou un pool de threads ().[](https://github.com/jekyll/jekyll/issues/9485)
  ```ruby
  module Jekyll
    module UlyssesZhan::MultithreadRendering
      def render_pages(*args)
        @rendering_threads = []
        super # Appeler la méthode originale
        @rendering_threads.each(&:join) # Attendre que les threads se terminent
      end
    end
  end
  Jekyll::Site.prepend(Jekyll::UlyssesZhan::MultithreadRendering)
  ```
- **Ajouter au Gemfile** : Placez l'extension dans votre répertoire `_plugins` et assurez-vous qu'elle est chargée par Jekyll.
- **Tester la thread safety** : Étant donné que Liquid et certaines extensions (par exemple, `jekyll-feed`) peuvent casser, testez minutieusement. Vous pourriez avoir besoin de patcher Liquid ou d'éviter le multithreading pour certaines fonctionnalités ().[](https://github.com/jekyll/jekyll/issues/9485)
- **Intégrer avec GitHub Actions** : Mettez à jour votre workflow pour inclure l'extension dans votre dépôt. Assurez-vous que l'action `jekyll-build-pages` utilise votre configuration Jekyll personnalisée :
  ```yaml
  - name: Build with Jekyll
    uses: actions/jekyll-build-pages@v1
    with:
      source: ./
      destination: ./_site
    env:
      BUNDLE_GEMFILE: ./Gemfile # S'assurer que votre Gemfile personnalisé avec l'extension est utilisé
  ```

**Défis** :
- Problèmes de thread safety avec Liquid et des extensions comme `jekyll-feed` ().[](https://github.com/jekyll/jekyll/issues/9485)
- Risque de rendu de page incorrect (par exemple, le contenu d'une page apparaissant dans une autre).
- Nécessite une expertise en Ruby pour déboguer et maintenir.

#### 2. **Paralléliser les builds avec des configurations multiples**
Au lieu de multithreader un seul build, vous pouvez diviser votre site en parties plus petites (par exemple, par collection ou répertoire) et les construire en parallèle en utilisant plusieurs processus Jekyll. Cette approche évite les problèmes de thread safety mais nécessite plus de configuration.

**Étapes** :
- **Diviser le site** : Organisez votre site en collections (par exemple, `posts`, `pages`, `docs`) ou répertoires et créez des fichiers `_config.yml` séparés pour chacun (,).[](https://amcrouch.medium.com/configuring-environments-when-building-sites-with-jekyll-dd6eb2603c39)[](https://coderwall.com/p/tfcj2g/using-different-build-configuration-in-jekyll-site)
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
- **Mettre à jour le workflow GitHub Actions** : Modifiez votre workflow pour exécuter plusieurs builds Jekyll en parallèle, chacun avec un fichier de configuration différent.
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
- **Combiner les sorties** : Après les builds parallèles, fusionnez les répertoires de sortie en un seul dossier `_site` pour le déploiement.

**Défis** :
- Gérer les interdépendances entre les collections (par exemple, `site.related_posts`).
- Complexité accrue de la configuration et du déploiement.
- Peut ne pas bien évoluer pour les sites avec un contenu fortement couplé.

#### 3. **Utiliser un pool de threads pour les sites volumineux**
Une pull request pour l'extension `amp-jekyll` a suggéré d'utiliser un pool de threads pour traiter les pages, avec un nombre configurable de threads pour éviter de submerger le système (). Cette approche équilibre performance et utilisation des ressources.[](https://github.com/juusaw/amp-jekyll/pull/26)

**Étapes** :
- **Implémenter un pool de threads** : Modifiez ou créez une extension pour utiliser `Thread::Queue` de Ruby afin de gérer un nombre fixe de threads de travail (par exemple, 4 ou 8, selon votre système).
  ```ruby
  require 'thread'

  module Jekyll
    module ThreadPoolRendering
      def render_pages(*args)
        queue = Queue.new
        site.pages.each { |page| queue << page }
        threads = (1..4).map do # 4 threads
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
- **Ajouter une option de configuration** : Permettez aux utilisateurs d'activer/désactiver le multithreading ou de définir le nombre de threads dans `_config.yml` :
  ```yaml
  multithreading:
    enabled: true
    thread_count: 4
  ```
- **Intégrer avec le workflow** : Assurez-vous que l'extension est incluse dans votre dépôt et chargée pendant le build GitHub Actions.

**Défis** :
- Problèmes de thread safety similaires à la première approche.
- Surcharge de changement de contexte pour les sites volumineux avec de nombreuses tâches courtes ().[](https://github.com/juusaw/amp-jekyll/pull/26)
- Nécessite des tests pour garantir la compatibilité avec toutes les extensions.

#### 4. **Optimiser sans multithreading**
Si le multithreading s'avère trop complexe ou risqué, vous pouvez optimiser le processus de build mono-thread :
- **Activer les builds incrémentiels** : Utilisez `jekyll build --incremental` pour ne reconstruire que les fichiers modifiés (,). Ajoutez à votre workflow :[](https://github.com/jekyll/jekyll/blob/master/lib/jekyll/commands/build.rb)[](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)
  ```yaml
  - name: Build with Jekyll
    uses: actions/jekyll-build-pages@v1
    with:
      source: ./
      destination: ./_site
      incremental: true
  ```
- **Réduire l'utilisation des extensions** : Les extensions personnalisées peuvent ralentir considérablement les builds (). Auditez et supprimez les extensions inutiles.[](https://github.com/jekyll/jekyll/issues/4297)
- **Utiliser des convertisseurs plus rapides** : Passez de Kramdown à un processeur markdown plus rapide comme CommonMark, ou testez Pandoc pour des cas d'utilisation spécifiques ().[](https://github.com/jekyll/jekyll/issues/9485)
- **Mettre en cache les dépendances** : Assurez-vous que `bundler-cache: true` est présent dans votre workflow GitHub Actions pour éviter de réinstaller les gems ().[](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)

### Recommandations
- **Commencer par les builds incrémentiels** : C'est le moyen le plus simple d'accélérer les builds sans risquer de problèmes de thread safety. Ajoutez `--incremental` à votre workflow et testez son impact.
- **Expérimenter avec une extension de pool de threads** : Si vous avez de l'expertise en Ruby, essayez d'implémenter une extension de pool de threads avec un nombre configurable de threads (Option 3). Commencez avec un petit site pour tester la thread safety.
- **Éviter le multithreading complet pour l'instant** : Compte tenu des préoccupations de thread safety avec Liquid et les extensions (), le multithreading complet pourrait nécessiter une refonte importante ou un fork personnalisé de Liquid, ce qui pourrait ne pas être pratique à moins que vous ne contribuiez au développement core de Jekyll.[](https://github.com/jekyll/jekyll/issues/9485)
- **Surveiller les temps de build** : Utilisez les logs GitHub Actions pour mesurer les temps de build et identifier les goulots d'étranglement. Par exemple, un site prenant 6 minutes à build () suggère que les extensions ou le traitement d'assets volumineux pourraient être le problème.[](https://github.com/jekyll/jekyll/issues/1855)

### Exemple GitHub Actions avec builds incrémentiels
Voici une version mise à jour de votre workflow avec les builds incrémentiels activés :
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

### Mises en garde
- **Thread Safety** : Le multithreading dans Jekyll est expérimental et peut casser les extensions ou produire une sortie incorrecte (). Testez minutieusement sur un petit site en premier.[](https://github.com/jekyll/jekyll/issues/9485)
- **Limites de GitHub Actions** : Les builds parallèles (Option 2) augmentent l'utilisation des ressources, assurez-vous donc que votre workflow reste dans les limites du niveau gratuit de GitHub.
- **Potentiel de Jekyll 5** : Les futures versions de Jekyll pourraient aborder le multithreading nativement, comme cela a été discuté (). Pour l'instant, des solutions personnalisées sont nécessaires.[](https://github.com/jekyll/jekyll/issues/9485)

Si vous avez besoin d'aide pour implémenter une approche spécifique (par exemple, écrire une extension ou diviser les builds), faites-le moi savoir et je pourrai fournir des conseils ou du code plus détaillés !