---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Corriger l'Erreur Bundler Command Not Found
translated: true
type: note
---

### Comprendre le problème
Votre commande `gem install jekyll bundler` a réussi (elle a installé 30 gems, incluant Bundler 2.7.2), mais la commande `bundle` n'est pas trouvée. C'est un problème courant de PATH/environnement sur les systèmes Ubuntu/Debian après une installation système avec `sudo gem install`. Les gems installent les binaires dans `/usr/local/bin` (ou similaire), mais le `$PATH` de votre shell pourrait ne pas l'inclure, ou le changement ne s'est pas propagé (par exemple, nécessité de recharger votre profil).

La suggestion du système d'`apt install ruby-bundler` installerait une version plus ancienne (2.4.20) via apt, ce qui pourrait entrer en conflit avec votre Bundler 2.7.2 installé via gem — évitez cela pour l'instant. Idem pour snap ; cela pourrait isoler Ruby d'une manière qui rompt les chemins des gems.

### Correction rapide : Vérifier et utiliser le Bundler installé
1. **Vérifiez où `bundle` est installé** :
   ```
   gem environment
   ```
   - Cherchez "EXECUTABLE DIRECTORY" (probablement `/usr/local/bin`). Notez ce chemin.

2. **Localisez et testez `bundle` directement** :
   ```
   which bundle  # Si rien, essayez : find /usr/local -name bundle 2>/dev/null
   /usr/local/bin/bundle --version  # Devrait afficher "Bundler version 2.7.2"
   ```
   - Si cela fonctionne, parfait ! Utilisez le chemin complet pour l'instant : `/usr/local/bin/bundle install`

3. **Exécutez votre configuration Jekyll avec le chemin complet** :
   - Dans `~/projects/blog-source` (en supposant qu'il y ait un `Gemfile`) :
     ```
     /usr/local/bin/bundle install
     /usr/local/bin/bundle exec jekyll serve
     ```
   - Cela devrait installer les dépendances de Jekyll et démarrer le serveur (généralement à http://127.0.0.1:4000).

### Correction permanente : Mettre à jour votre PATH
Si `/usr/local/bin` n'est pas dans votre `$PATH`, ajoutez-le :
1. Éditez `~/.bashrc` (ou `~/.profile` pour les shells de connexion) :
   ```
   nano ~/.bashrc
   ```
   Ajoutez cette ligne à la fin :
   ```
   export PATH="/usr/local/bin:$PATH"
   ```

2. Rechargez votre shell :
   ```
   source ~/.bashrc
   ```

3. Vérifiez :
   ```
   echo $PATH  # Devrait maintenant inclure /usr/local/bin
   bundle --version  # Devrait fonctionner sans le chemin complet
   ```

Maintenant, réessayez :
```
bundle install
bundle exec jekyll serve
```

### Si cela ne fonctionne pas
- **Problèmes de permissions ?** (Rare, mais sudo peut les causer.) Réinstallez sans sudo (installation utilisateur locale) :
  ```
  gem install --user-install bundler jekyll
  ```
  Puis ajoutez `export PATH="$HOME/.local/share/gem/ruby/*/bin:$PATH"` à `~/.bashrc` (ajustez le chemin à partir de `gem environment`).

- **Incompatibilité de version de Ruby ?** Vérifiez avec `ruby --version`. Si c'est la version système de Ruby (par exemple, 2.7.x), envisagez des gestionnaires de version de Ruby comme `rbenv` (installez via `curl -fsSL https://github.com/rbenv/rbenv-installer/raw/HEAD/bin/rbenv-installer | bash`, puis suivez la configuration). Cela évite les conflits système à long terme.

- **Le proxy est-il toujours actif ?** Si vos variables d'environnement (`http_proxy`, etc.) sont définies, Bundler devrait les hériter — assurez-vous simplement qu'elles sont exportées avant l'exécution.

Votre configuration devrait fonctionner correctement après l'ajustement du PATH. Si vous rencontrez des erreurs (par exemple, partagez la sortie de `gem environment`), collez-les pour une aide plus ciblée !