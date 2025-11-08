---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Installation de Jekyll sur Ubuntu
translated: true
type: note
---

### Configuration et exécution de Jekyll sur Ubuntu

D'après votre erreur ("Commande 'bundle' introuvable") et les commandes que vous essayez d'exécuter, il semble que vous ayez d'abord besoin d'installer Ruby, Bundler et Jekyll correctement. Ubuntu ne les inclut pas par défaut, mais c'est simple en utilisant le guide officiel de Jekyll. Je vais vous guider à travers la configuration complète étape par étape, puis comment exécuter vos commandes spécifiques.

#### Étape 1 : Installer les dépendances système
Ouvrez votre terminal et exécutez cette commande pour installer Ruby et les outils de compilation (cela inclut Ruby 3.x via `ruby-full`) :

```bash
sudo apt update
sudo apt install ruby-full build-essential zlib1g-dev
```

- Cela configure Ruby (vérifiez avec `ruby -v`—cela devrait afficher quelque chose comme 3.0+).
- Si vous êtes sur une Ubuntu récente (par exemple, 22.04+), cela fonctionne directement. Évitez Snap pour Ruby si possible, car cela peut causer des problèmes de chemin.

#### Étape 2 : Configurer un répertoire Gem utilisateur (recommandé pour éviter Sudo)
Pour installer des gems sans privilèges root (évite les erreurs de permission plus tard) :

```bash
echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

- Vérifiez : Exécutez `gem env`—cela devrait afficher votre `GEM_HOME` comme `~/gems`.

#### Étape 3 : Installer Jekyll et Bundler
Maintenant, installez les outils :

```bash
gem install jekyll bundler
```

- Cela ajoute les commandes `gem`, `jekyll` et `bundle` à votre chemin.
- Si vous obtenez des erreurs de permission, revérifiez l'Étape 2 ou utilisez temporairement `sudo` (mais évitez-le à long terme).

#### Étape 4 : Créer et exécuter votre blog
Maintenant, vous pouvez exécuter les commandes de votre extrait. Je vais expliquer chacune :

1. **Créer un nouveau site Jekyll** :
   ```bash
   jekyll new myblog
   ```
   - Cela génère un site basique dans un dossier `myblog`.

2. **Entrer dans le répertoire** :
   ```bash
   cd myblog
   ```

3. **Installer les dépendances** (c'est là que votre `bundle install` original a échoué—maintenant cela devrait fonctionner) :
   ```bash
   bundle install
   ```
   - Récupère les gems comme les plugins Jekyll.

4. **Servir le site** (démarre un serveur local à http://127.0.0.1:4000) :
   ```bash
   bundle exec jekyll serve
   ```
   - Ouvrez votre navigateur à cette URL pour voir votre site.

5. **Servir avec reconstructions incrémentielles** (plus rapide pour le développement, ne reconstruit que les fichiers modifiés) :
   ```bash
   bundle exec jekyll serve --incremental
   ```

6. **Servir incluant les brouillons** (affiche les articles non publiés) :
   ```bash
   bundle exec jekyll serve --draft
   ```

7. **Si vous obtenez une erreur "webrick"** (courant sur Ruby 3+, car il n'est pas inclus par défaut) :
   ```bash
   bundle add webrick
   ```
   - Puis redémarrez la commande serve : `bundle exec jekyll serve`.
   - Alternativement, ajoutez `gem "webrick"` à votre `Gemfile` et exécutez `bundle install`.

8. **Servir rapidement sans Bundler** (si vous ignorez `bundle exec`) :
   ```bash
   jekyll serve
   ```
   - Mais utilisez `bundle exec` pour la cohérence dans les projets.

#### Dépannage
- **Toujours "bundle not found" ?** Assurez-vous que l'Étape 2 a correctement sourcé votre `~/.bashrc` (`source ~/.bashrc`), puis redémarrez votre terminal ou exécutez `hash -r`. Vérifiez avec `which bundle`.
- **Problèmes de permission avec les gems ?** Tenez-vous à la configuration du répertoire utilisateur de l'Étape 2.
- **Version de Ruby trop ancienne ?** Si `ruby -v` est <3.0, envisagez d'utiliser rbenv pour une version plus récente (installez via `curl -fsSL https://github.com/rbenv/rbenv-installer/raw/HEAD/bin/rbenv-installer | bash`, puis `rbenv install 3.2.0`).
- **Le pare-feu bloque le port 4000 ?** Ubuntu généralement non, mais testez avec `curl http://127.0.0.1:4000`.
- Votre projet est dans `~/projects/blog-source`—exécutez ces commandes à partir de là ou ajustez les chemins.

Une fois servi, modifiez les fichiers dans `_posts/` ou `_config.yml` et enregistrez—Jekyll se reconstruit automatiquement. Pour la production, construisez avec `jekyll build` et déployez sur GitHub Pages ou Netlify.

[Jekyll Ubuntu Installation Guide](https://jekyllrb.com/docs/installation/ubuntu/)