---
audio: false
generated: true
lang: fr
layout: post
title: Corriger l'Erreur Commande Go Introuvable sur macOS
translated: true
type: note
---

Le message d'erreur `/bin/sh: go: command not found` indique que le langage de programmation Go n'est pas installé sur votre système macOS, ou qu'il n'est pas correctement configuré dans votre PATH. La commande `make` tente d'exécuter un processus de compilation Go, ce qui nécessite le compilateur Go (`go`). Voici les étapes pour installer Go sur macOS et résoudre ce problème.

### Étapes pour installer Go sur macOS

Il existe deux méthodes principales pour installer Go sur macOS : utiliser le programme d'installation officiel de Go ou utiliser Homebrew. Je vais décrire les deux méthodes, mais Homebrew est souvent plus simple pour les utilisateurs de macOS. Choisissez une méthode en fonction de votre préférence.

#### Prérequis
- Assurez-vous que votre version de macOS est 10.10 ou ultérieure pour la compatibilité avec les versions récentes de Go.
- Vous devez avoir un accès administrateur pour installer Go et modifier les fichiers système.
- Une application terminal (se trouve dans Applications > Utilitaires > Terminal).

#### Méthode 1 : Installer Go avec Homebrew (Recommandé)
Homebrew est un gestionnaire de paquets populaire pour macOS qui simplifie l'installation des logiciels.

1. **Installer Homebrew (s'il n'est pas déjà installé)** :
   - Ouvrez Terminal et exécutez :
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - Suivez les instructions à l'écran pour terminer l'installation.

2. **Installer Go** :
   - Exécutez la commande suivante pour installer la dernière version de Go :
     ```bash
     brew install go
     ```
   - Ceci installe Go dans `/usr/local/Cellar/go` (ou un chemin similaire) et ajoute le binaire Go à `/usr/local/bin`.

3. **Vérifier l'installation** :
   - Vérifiez la version installée de Go en exécutant :
     ```bash
     go version
     ```
   - Vous devriez voir une sortie comme `go version go1.23.x darwin/amd64`, confirmant que Go est installé.

4. **Configurer les variables d'environnement** (si nécessaire) :
   - Homebrew ajoute généralement Go à votre PATH automatiquement, mais si les commandes `go` ne fonctionnent pas, ajoutez le chemin du binaire Go à votre profil shell :
     - Ouvrez ou créez le fichier de configuration de shell approprié (par exemple, `~/.zshrc` pour Zsh, qui est l'option par défaut sur macOS depuis Catalina, ou `~/.bash_profile` pour Bash) :
       ```bash
       nano ~/.zshrc
       ```
     - Ajoutez les lignes suivantes :
       ```bash
       export PATH=$PATH:/usr/local/go/bin
       ```
     - Enregistrez le fichier (Ctrl+X, puis Y, puis Entrée dans nano) et appliquez les modifications :
       ```bash
       source ~/.zshrc
       ```
     - Si vous souhaitez utiliser un espace de travail personnalisé, définissez `GOPATH` (optionnel, car les modules Go éliminent souvent le besoin de cela) :
       ```bash
       export GOPATH=$HOME/go
       export PATH=$PATH:$GOPATH/bin
       ```
     - Rechargez le fichier :
       ```bash
       source ~/.zshrc
       ```

5. **Tester l'installation de Go** :
   - Exécutez `go version` à nouveau pour vous assurer que la commande est reconnue.
   - Optionnellement, créez un programme Go simple pour confirmer que tout fonctionne :
     ```bash
     mkdir -p ~/go/src/hello
     nano ~/go/src/hello/main.go
     ```
     - Ajoutez le code suivant :
       ```go
       package main
       import "fmt"
       func main() {
           fmt.Println("Hello, World!")
       }
       ```
     - Enregistrez et quittez (Ctrl+X, Y, Entrée), puis compilez et exécutez :
       ```bash
       cd ~/go/src/hello
       go run main.go
       ```
     - Vous devriez voir `Hello, World!` comme sortie.

#### Méthode 2 : Installer Go en utilisant le programme d'installation officiel
Si vous préférez ne pas utiliser Homebrew, vous pouvez installer Go en utilisant le package macOS officiel.

1. **Télécharger le programme d'installation de Go** :
   - Visitez la page de téléchargement officielle de Go : https://go.dev/dl/
   - Téléchargez le package macOS (`.pkg`) pour votre architecture système (par exemple, `go1.23.x.darwin-amd64.pkg` pour les Macs Intel ou `go1.23.x.darwin-arm64.pkg` pour les Apple Silicon).

2. **Exécuter le programme d'installation** :
   - Double-cliquez sur le fichier `.pkg` téléchargé dans le Finder.
   - Suivez les instructions à l'écran pour installer Go. Il sera installé par défaut dans `/usr/local/go`.
   - Vous devrez peut-être entrer votre mot de passe administrateur.

3. **Configurer les variables d'environnement** :
   - Ouvrez Terminal et modifiez votre fichier de configuration de shell (par exemple, `~/.zshrc` ou `~/.bash_profile`) :
     ```bash
     nano ~/.zshrc
     ```
   - Ajoutez les lignes suivantes :
     ```bash
     export GOROOT=/usr/local/go
     export GOPATH=$HOME/go
     export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
     ```
   - Enregistrez et appliquez les modifications :
     ```bash
     source ~/.zshrc
     ```
   - Remarque : `GOROOT` est optionnel sauf si vous développez Go lui-même ou avez besoin d'un chemin d'installation non standard. Les versions modernes de Go ne nécessitent souvent pas que `GOROOT` soit défini.

4. **Vérifier l'installation** :
   - Exécutez :
     ```bash
     go version
     ```
   - Vous devriez voir la version installée de Go (par exemple, `go version go1.23.x darwin/amd64`).

5. **Tester l'installation de Go** :
   - Suivez les mêmes étapes que dans la Méthode 1, Étape 5 pour créer et exécuter un programme "Hello, World!".

#### Dépannage du problème initial
Après avoir installé Go, retournez dans votre répertoire `clash-core` et réessayez la commande `make` :
```bash
cd /path/to/clash-core
make
```

Si vous rencontrez des problèmes :
- **Paramètres de proxy** : Votre sortie de terminal montre que `HTTP_PROXY` et `HTTPS_PROXY` sont définis sur `http://127.0.0.1:7890`. Assurez-vous que votre proxy est actif et n'interfère pas avec l'accès réseau de Go (par exemple, le téléchargement des dépendances). Vous pouvez désactiver temporairement le proxy pour tester :
  ```bash
  unset HTTP_PROXY HTTPS_PROXY
  make
  ```
- **Permissions** : Si vous obtenez des erreurs de permission, assurez-vous d'avoir un accès en écriture au répertoire du projet et à l'espace de travail Go (`$GOPATH` ou `$HOME/go`).
- **Modules Go** : Le projet `clash-core` utilise probablement les modules Go. Assurez-vous d'être dans le bon répertoire contenant `go.mod`, et exécutez `go mod tidy` pour récupérer les dépendances avant `make` :
  ```bash
  go mod tidy
  make
  ```
- **Incompatibilité d'architecture** : La commande `make` compile pour `linux-amd64` (`GOOS=linux GOARCH=amd64`). Si vous prévoyez d'exécuter le binaire sur macOS, vous devrez peut-être modifier le Makefile ou la commande de compilation pour cibler `darwin-amd64` (pour les Macs Intel) ou `darwin-arm64` (pour les Apple Silicon). Vérifiez le Makefile pour la cible `linux-amd64` et ajustez-la, ou exécutez :
  ```bash
  GOARCH=amd64 GOOS=darwin CGO_ENABLED=0 go build -trimpath -ldflags '-X "github.com/Dreamacro/clash/constant.Version=1.18" -X "github.com/Dreamacro/clash/constant.BuildTime=Sat Jun 28 12:24:27 UTC 2025" -w -s -buildid=' -o bin/clash-darwin-amd64
  ```
  Remplacez `amd64` par `arm64` si vous êtes sur Apple Silicon.

#### Notes supplémentaires
- **Désinstaller les versions précédentes de Go** : Si Go était précédemment installé, supprimez-le pour éviter les conflits :
  ```bash
  sudo rm -rf /usr/local/go
  sudo rm -f /etc/paths.d/go
  ```
  Puis réinstallez en utilisant l'une des méthodes ci-dessus.
- **Espace de travail Go** : Si vous définissez `GOPATH`, créez le répertoire :
  ```bash
  mkdir -p $HOME/go/{bin,src,pkg}
  ```
  Cependant, avec les modules Go (utilisés par la plupart des projets modernes comme `clash-core`), `GOPATH` est moins critique.
- **Outils de ligne de commande Xcode** : Certains projets Go nécessitent des dépendances C (par exemple, `CGO_ENABLED=1`). Installez les outils de ligne de commande Xcode si nécessaire :
  ```bash
  xcode-select --install
  ```
- **Versions multiples de Go** : Si vous avez besoin de plusieurs versions de Go, envisagez d'utiliser un gestionnaire de version comme `gvm` (installez via Homebrew ou un script).

#### Vérification
Une fois Go installé et la commande `make` réussie, le binaire `clash-core` devrait apparaître dans le répertoire `bin/` (par exemple, `bin/clash-linux-amd64` ou `bin/clash-darwin-amd64`). Vérifiez qu'il fonctionne en exécutant :
```bash
./bin/clash-darwin-amd64 --version
```

Si vous avez besoin d'une aide supplémentaire ou si vous rencontrez des erreurs spécifiques, faites-moi savoir le message d'erreur exact ou le contexte, et je pourrai fournir une aide plus ciblée !