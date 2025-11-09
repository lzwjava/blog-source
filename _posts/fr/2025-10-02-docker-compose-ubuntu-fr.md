---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast:free
title: Installation de Docker Compose pour Ubuntu
translated: true
type: note
---

D'après les informations de votre système, vous utilisez **Ubuntu 24.04.2 LTS** sur une architecture **x86_64**. Pour télécharger le binaire **Docker Compose** approprié pour votre système à partir de la release GitHub fournie (v2.39.4), vous devez sélectionner le binaire compatible avec Linux sur x86_64.

### Téléchargement Recommandé
Vous devriez télécharger le binaire **docker-compose-linux-x86_64**, qui n'est pas explicitement listé dans les assets fournis mais qui est impliqué comme un binaire standard pour les systèmes Linux x86_64 dans les releases de Docker Compose. Cependant, parmi les assets listés, le plus proche pour votre système est :

- **docker-compose-linux-aarch64** n'est **pas** adapté car il est pour l'architecture ARM64 (aarch64), et votre système est x86_64.
- Les binaires **darwin** (par ex., `docker-compose-darwin-x86_64`) sont pour macOS, pas pour Linux.
- Les options de code source (`Source code (zip)` ou `Source code (tar.gz)`) nécessitent une compilation manuelle, ce qui est inutile puisqu'un binaire précompilé est typiquement disponible.

Puisque le binaire **docker-compose-linux-x86_64** n'est pas explicitement listé dans vos assets fournis mais est standard pour les releases de Docker Compose, vous pouvez probablement le trouver dans la liste complète des assets sur la page de release GitHub. S'il n'est pas disponible, vous pouvez utiliser le code source ou installer Docker Compose via une méthode alternative (par ex., gestionnaire de paquets ou pip).

### Étapes pour Télécharger et Installer
1.  **Confirmer le Binaire** : Visitez la page de release GitHub pour v2.39.4 pour confirmer la disponibilité de `docker-compose-linux-x86_64`. La page de release se trouve typiquement à l'adresse :
    [Docker Compose v2.39.4 Release](https://github.com/docker/compose/releases/tag/v2.39.4)

2.  **Télécharger le Binaire** :
    Si `docker-compose-linux-x86_64` est disponible, téléchargez-le. Par exemple :
    ```bash
    curl -L "https://github.com/docker/compose/releases/download/v2.39.4/docker-compose-linux-x86_64" -o docker-compose
    ```

3.  **Vérifier le Téléchargement** :
    Utilisez la checksum fournie pour vérifier l'intégrité du fichier téléchargé. Par exemple, si le fichier `docker-compose-linux-x86_64.sha256` est disponible :
    ```bash
    echo "<sha256> docker-compose" | sha256sum --check
    ```
    Remplacez `<sha256>` par le hash approprié provenant des assets de la release (par ex., `df7ff3dd8080134b851e1e49265028697d27de71f9bdc187e3d833357b934f36` pour `docker-compose-darwin-x86_64.sha256`, mais vous avez besoin de l'équivalent Linux).

4.  **Installer le Binaire** :
    Déplacez le binaire vers un répertoire dans votre PATH, comme `/usr/local/bin` :
    ```bash
    chmod +x docker-compose
    sudo mv docker-compose /usr/local/bin/docker-compose
    ```

5.  **Vérifier l'Installation** :
    Vérifiez la version installée :
    ```bash
    docker-compose --version
    ```
    Cela devrait afficher `Docker Compose version v2.39.4`.

### Méthode d'Installation Alternative
Si le binaire `docker-compose-linux-x86_64` n'est pas disponible ou si vous préférez une méthode plus simple, vous pouvez installer Docker Compose en utilisant le gestionnaire de paquets ou pip, car votre système a Python 3.13.4 installé :

#### Via le Gestionnaire de Paquets (Recommandé pour Ubuntu)
Docker Compose est souvent disponible dans les dépôts d'Ubuntu ou le dépôt officiel de Docker :
```bash
sudo apt update
sudo apt install docker-compose-plugin
```
Ceci installe le plugin Docker Compose, qui est la manière moderne d'utiliser Docker Compose (en tant que `docker compose` plutôt que `docker-compose`). Notez que la version dans le dépôt d'Ubuntu pourrait ne pas être exactement la v2.39.4, vérifiez avec :
```bash
docker compose version
```

#### Via pip (Python)
Puisque vous avez Python 3.13.4, vous pouvez installer Docker Compose via pip :
```bash
pip3 install docker-compose==2.39.4
```
Ceci installe la version spécifique. Vérifiez avec :
```bash
docker-compose --version
```

### Notes
- Le fichier `checksums.txt` (SHA256: `1a9c3370b88825ab2b229bb90eda6f703d84018ea1d56b5ba573f8893c9ab6b4`) peut être utilisé pour vérifier l'intégrité des fichiers téléchargés.
- Si vous choisissez de compiler à partir des sources (`Source code (zip)` ou `Source code (tar.gz)`), vous aurez besoin de Go (non listé dans les informations de votre système) et d'une configuration supplémentaire, ce qui est plus complexe et n'est pas recommandé sauf si nécessaire.
- La release inclut des améliorations et des correctifs (par ex., support pour `develop.watch.initial_sync`, volume ls sans projet, et TLS pour bake), qui sont pertinents si vous utilisez ces fonctionnalités.

Si vous avez besoin d'aide pour trouver le binaire exact `docker-compose-linux-x86_64` ou si vous rencontrez des problèmes, faites-le moi savoir et je vous guiderai davantage !

[Docker Compose v2.39.4 Release](https://github.com/docker/compose/releases/tag/v2.39.4)