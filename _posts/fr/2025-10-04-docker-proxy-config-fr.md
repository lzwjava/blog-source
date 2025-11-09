---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Configuration du proxy du démon Docker
translated: true
type: note
---

### Configuration du démon Docker pour les paramètres de proxy

Le démon Docker peut être configuré pour utiliser un proxy HTTP/HTTPS pour des opérations comme le téléchargement d'images ou la construction de conteneurs derrière un pare-feu d'entreprise. Cela se fait en modifiant (ou en créant) le fichier `/etc/docker/daemon.json`. Notez que cette configuration s'applique au démon lui-même (par exemple, pour `docker pull` ou `docker build`), et non pas aux conteneurs individuels (qui utiliseraient des variables d'environnement ou des arguments de build Docker).

#### Prérequis
- Vous avez besoin d'un accès root ou sudo sur un système Linux (c'est le système d'exploitation principal pour la configuration du démon Docker ; sur Windows/Mac avec Docker Desktop, utilisez plutôt les paramètres de l'interface graphique).
- Docker installé et en cours d'exécution.
- Connaître les détails de votre serveur proxy (par exemple, `http://proxy.company.com:8080` pour un proxy HTTP/HTTPS, et toutes les exceptions no-proxy).

#### Configuration étape par étape

1. **Localiser ou créer le fichier de configuration du démon** :
   - Ouvrez un terminal et naviguez vers `/etc/docker/` (créez le répertoire s'il n'existe pas : `sudo mkdir -p /etc/docker`).
   - Modifiez le fichier `daemon.json` en utilisant un éditeur de texte (par exemple, `sudo nano /etc/docker/daemon.json` ou `sudo vim /etc/docker/daemon.json`).
   - Si le fichier n'existe pas, créez-le. Commencez avec un objet JSON vide `{}` s'il est nouveau.

2. **Ajouter la configuration du proxy** :
   - Ajoutez une section `"proxies"` au fichier JSON. Voici un exemple basique :

     ```json
     {
       "proxies": {
         "http-proxy": "http://proxy.company.com:8080",
         "https-proxy": "http://proxy.company.com:8080",
         "no-proxy": "localhost,127.0.0.1,*.company.com,10.0.0.0/8"
       }
     }
     ```

     - **Explications** :
       - `"http-proxy"` : L'URL pour le proxy HTTP (requise pour les requêtes non-HTTPS).
       - `"https-proxy"` : L'URL pour le proxy HTTPS (souvent la même que le proxy HTTP).
       - `"no-proxy"` : Une liste séparée par des virgules des hôtes/domaines/plages d'adresses IP qui doivent contourner le proxy (par exemple, les adresses locales ou les domaines internes). Cela évite les boucles infinies.
       - Si une authentification est nécessaire, utilisez le format `http://username:password@proxy.company.com:8080`.
       - Pour les proxies SOCKS, utilisez `"http-proxy": "socks5://proxy.company.com:1080"`.

     - Si `daemon.json` a déjà un contenu existant (par exemple, d'autres paramètres comme `"log-driver": "json-file"`), fusionnez la section `"proxies"` dedans sans dupliquer les clés. Assurez une syntaxe JSON valide (utilisez un outil comme `jsonlint` pour valider si nécessaire).

3. **Sauvegarder et redémarrer le démon Docker** :
   - Sauvegardez le fichier.
   - Redémarrez le service Docker pour appliquer les changements :
     ```
     sudo systemctl restart docker
     ```
     - Sur les systèmes plus anciens ou sans systemd, utilisez `sudo service docker restart`.
   - Vérifiez que le démon est en cours d'exécution :
     ```
     sudo systemctl status docker
     ```
     - Vérifiez les logs en cas de problème : `sudo journalctl -u docker.service`.

4. **Vérifier la configuration** :
   - Testez en téléchargeant une image (qui devrait maintenant passer par votre proxy) :
     ```
     docker pull hello-world
     ```
   - Vérifiez si les paramètres de proxy sont appliqués en inspectant la configuration du démon :
     ```
     docker info | grep -i proxy
     ```
     - Vous devriez voir une sortie comme :
       ```
       HTTP Proxy: http://proxy.company.com:8080
       HTTPS Proxy: http://proxy.company.com:8080
       No Proxy: localhost,127.0.0.1,*.company.com,10.0.0.0/8
       ```
   - Si vous utilisez Docker dans un contexte de build, testez avec :
     ```
     docker build -t test-proxy .
     ```
     (En supposant un Dockerfile simple qui télécharge une image de base.)

#### Notes supplémentaires
- **Sécurité** : Évitez de coder en dur les identifiants dans `daemon.json` sur les systèmes partagés. Utilisez des variables d'environnement si possible, ou des outils comme `docker config` pour des configurations plus avancées.
- **Problèmes courants** :
  - **Erreurs de syntaxe** : Un JSON invalide empêchera le démon de démarrer. Vérifiez avec `cat /etc/docker/daemon.json` et un validateur JSON.
  - **Pare-feu/SELinux** : Assurez-vous que votre proxy est accessible et qu'aucun module de sécurité ne le bloque.
  - **Version de Docker** : Cela fonctionne sur Docker 20.10+ (les versions antérieures utilisaient des variables d'environnement différentes comme `HTTP_PROXY`). Vérifiez votre version avec `docker --version` et mettez à niveau si nécessaire.
  - **Proxies spécifiques au registre** : Pour les registres privés, vous pourriez avoir besoin d'une configuration supplémentaire sous `"registry-mirrors"` ou de registres non sécurisés dans `daemon.json`.
- **Pour les conteneurs** : Si vous avez besoin des paramètres de proxy *à l'intérieur* des conteneurs en cours d'exécution (pas le démon), définissez les variables d'environnement dans le Dockerfile (par exemple, `ENV http_proxy=http://proxy.company.com:8080`) ou via `docker run -e http_proxy=...`.
- **Docker Desktop (Windows/Mac)** : Allez dans Paramètres > Ressources > Proxies, et activez/configurez là-bas—aucune modification JSON n'est nécessaire.

Pour plus de détails, reportez-vous à la documentation officielle de Docker : [Configure the Docker daemon](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file). Si vous rencontrez des erreurs, partagez la sortie exacte pour le dépannage !