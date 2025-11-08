---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Configuration des paramètres de proxy RubyGems
translated: true
type: note
---

Pour vous assurer que `gem` (RubyGems) utilise votre proxy (par exemple, à `http://127.0.0.1:7890`) pendant l'installation, suivez ces étapes. D'après la sortie verbeuse que vous avez partagée, il *semble déjà utiliser le proxy* — la ligne "Connecting to 127.0.0.1:7890... connected" est un indicateur fort provenant du client HTTP sous-jacent (probablement `net/http` ou un comportement similaire à `curl` en mode verbeux).

### 1. **Configurer le Proxy (si ce n'est pas déjà fait)**
   - **Option A : Utiliser les variables d'environnement (recommandé pour des commandes ponctuelles ou avec `sudo`)**  
     Celles-ci indiquent à `gem` de router le trafic via le proxy. Exécutez ceci avant votre installation :
     ```
     export http_proxy=http://127.0.0.1:7890
     export https_proxy=http://127.0.0.1:7890
     sudo -E gem install jekyll bundler --verbose
     ```
     - Le drapeau `-E` préserve vos variables d'environnement lors de l'utilisation de `sudo`.
     - Pour une configuration persistante, ajoutez les lignes `export` à votre `~/.bashrc` ou `~/.profile`.

   - **Option B : Configurer dans `~/.gemrc` (au niveau de l'utilisateur, `sudo` non nécessaire pour les installations futures)**  
     Créez ou modifiez `~/.gemrc` :
     ```
     echo 'http_proxy: http://127.0.0.1:7890' >> ~/.gemrc
     echo 'https_proxy: http://127.0.0.1:7890' >> ~/.gemrc
     ```
     Exécutez ensuite `gem install jekyll bundler --verbose` (sans `sudo` si possible — `sudo` peut ignorer les configurations utilisateur). Si vous utilisez `sudo`, utilisez l'Option A.

### 2. **Vérifier que le Proxy est Utilisé**
   - **Exécuter avec `--verbose` (comme vous l'avez fait)** : Cherchez des lignes comme :
     - `HEAD https://index.rubygems.org/` suivie des détails de connexion au proxy.
     - `Connecting to 127.0.0.1:7890... connected.` (ceci confirme l'utilisation du proxy).
     - Si cela montre des connexions directes à `rubygems.org` (par exemple, des adresses IP sans mention du proxy), il contourne le proxy.
   
   - **Tester avec un dry-run ou une récupération d'information** :
     ```
     gem fetch jekyll --verbose --platform=ruby
     ```
     Ou simplement interroger l'index :
     ```
     gem search jekyll --verbose
     ```
     Vérifiez la sortie pour les connexions proxy.

   - **Vérifier les variables d'environnement** :
     ```
     echo $http_proxy $https_proxy
     ```
     Si elles sont correctement définies, `gem` devrait les hériter.

   - **Déboguer avec `gem env`** :
     ```
     gem env
     ```
     Cherchez sous les sections "HTTP Proxy" ou "HTTPS Proxy" l'URL de votre proxy.

### Dépannage
- **Si `sudo` ignore le proxy** : Utilisez `sudo -E` ou exécutez sans `sudo` (installez dans le répertoire utilisateur : `gem install --user-install jekyll bundler`).
- **Aucune ligne de connexion ?** Votre proxy n'est peut-être pas configuré pour être verbeux, ou les variables d'environnement ne sont pas définies. Testez le proxy séparément : `curl -v https://rubygems.org/` (devrait montrer les sauts proxy).
- **Proxy d'entreprise/strict ?** S'il nécessite une authentification, utilisez `http://user:pass@127.0.0.1:7890`.
- **Ça ne fonctionne toujours pas ?** Désactivez temporairement le proxy (`unset http_proxy https_proxy`) et réessayez — si cela fonctionne sans, le problème est la configuration ; sinon, vérifiez votre serveur proxy (par exemple, les logs Clash/V2Ray).

Votre installation a réussi (réponses 200 OK), donc vous êtes probablement bon — confirmez simplement que la prochaine exécution montre la connexion proxy pour être tranquille. Si vous partagez plus de sortie, je peux déboguer davantage !