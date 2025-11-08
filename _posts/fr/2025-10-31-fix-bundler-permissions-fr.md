---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Résoudre les erreurs d'autorisation de Bundler
translated: true
type: note
---

### Comprendre l'erreur

Il s'agit d'un problème d'autorisation courant lors de l'utilisation de Bundler (le gestionnaire de dépendances de Ruby) avec une installation système de Ruby (version 3.2.0 ici). L'erreur se produit car Bundler tente de télécharger et de mettre en cache la gemme `rake` (et potentiellement d'autres) dans le répertoire système des gemmes à l'emplacement `/var/lib/gems/3.2.0/cache/`, ce qui nécessite un accès en écriture au niveau root. Votre installation de Bundler elle-même est locale à l'utilisateur (dans `~/.local/share/gem/`), mais elle utilise par défaut les chemins système des gemmes pour les installations.

Cette chaîne dans votre `Gemfile` (Jekyll + dépendances comme `minima`, `jekyll-feed`, etc.) déclenche simplement l'installation de `rake` en tant que dépendance profonde—rien de mal avec votre configuration, seulement des problèmes de permissions.

### Correctifs rapides (par ordre de recommandation)

1. **Installer les gemmes localement (Recommandé - Aucun Sudo nécessaire)**
   Cela garde tout dans votre répertoire personnel, évitant entièrement les chemins système. Exécutez :
   ```
   bundle config set --local path 'vendor/bundle'
   bundle install
   ```
   - Cela crée un dossier `vendor/bundle` dans votre projet pour les gemmes.
   - Pour exécuter votre site Jekyll plus tard, utilisez `bundle exec jekyll serve` (le `exec` garantit l'utilisation des gemmes locales).
   - Si vous voulez que ce soit global pour tous les projets : Remplacez `--local` par `--global` et utilisez `~/.bundle` comme chemin.

2. **Utiliser Sudo (Rapide mais pas idéal)**
   Si vous avez besoin d'une installation ponctuelle et que les gemmes système ne vous dérangent pas :
   ```
   sudo bundle install
   ```
   - **Avertissement** : Cela installe les gemmes globalement en tant que root, ce qui peut entraîner des problèmes de propriété plus tard (par exemple, vous auriez besoin de `sudo` pour les mises à jour futures). À éviter si possible.

3. **Corriger les permissions système (Avancé - À utiliser avec prudence)**
   Si vous souhaitez continuer à utiliser le répertoire système des gemmes sans sudo :
   ```
   sudo chown -R $USER:$USER /var/lib/gems/3.2.0/
   ```
   - Puis réessayez `bundle install`.
   - **Avertissement** : Cela modifie la propriété des gemmes système, ce qui pourrait casser les paquets gérés par votre distribution (par exemple, Ubuntu). Ne faites cela que si vous êtes à l'aise pour résoudre les problèmes.

### Recommandation à long terme
Pour le développement Ruby/Jekyll, passez à un gestionnaire d'installation Ruby géré par l'utilisateur comme [rbenv](https://github.com/rbenv/rbenv) ou [RVM](https://rvm.io/). Cela évite tous les maux de tête liés aux permissions en installant Ruby et les gemmes entièrement dans votre répertoire personnel :
- Installez rbenv : Suivez le [guide officiel](https://github.com/rbenv/rbenv#installation).
- Puis : `rbenv install 3.2.0 && rbenv global 3.2.0 && gem install bundler`.
- Réessayez `bundle install`—cela fonctionnera sans problème.

Si aucune de ces solutions ne fonctionne ou si vous rencontrez une autre erreur, partagez le résultat de `ruby -v`, `gem env`, et votre `Gemfile.lock` (s'il existe) pour une aide plus personnalisée !