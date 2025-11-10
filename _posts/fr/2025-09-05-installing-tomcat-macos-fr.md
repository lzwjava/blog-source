---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Installation d'Apache Tomcat sur macOS
translated: true
type: note
---

Voici un guide étape par étape pour installer et exécuter **Apache Tomcat sur macOS** :

---

### 1. Vérifier Java

Tomcat nécessite Java. Vérifiez qu'il est installé :

```bash
java -version
```

Si vous ne voyez pas de version de Java (par exemple `1.8` ou `11` ou supérieure), installez-en une. Sur macOS, le moyen le plus simple est via [Homebrew](https://brew.sh) :

```bash
brew install openjdk@11
```

Puis liez-la :

```bash
brew link --force --overwrite openjdk@11
```

---

### 2. Installer Tomcat (Option A : Homebrew – le plus simple)

Avec Homebrew, vous pouvez installer Tomcat rapidement :

```bash
brew install tomcat
```

Cela installe généralement la dernière version (par exemple, Tomcat 10).

Vous la trouverez dans :

```
/usr/local/Cellar/tomcat/<version>/libexec
```

Ou si vous utilisez Apple Silicon :

```
/opt/homebrew/Cellar/tomcat/<version>/libexec
```

Exécutez-la avec :

```bash
catalina run
```

---

### 3. Installer Tomcat (Option B : Téléchargement manuel – méthode officielle)

1. Allez sur le [site web d'Apache Tomcat](https://tomcat.apache.org/download-10.cgi) et téléchargez la dernière version stable (choisissez le fichier `.tar.gz`).

2. Extrayez-le dans un répertoire, par exemple :

   ```bash
   tar xvf apache-tomcat-10.*.tar.gz
   mv apache-tomcat-10.* ~/tomcat
   ```

3. Démarrez Tomcat :

   ```bash
   cd ~/tomcat/bin
   ./startup.sh
   ```

4. Pour l'arrêter :

   ```bash
   ./shutdown.sh
   ```

---

### 4. Vérifier l'installation

Ouvrez votre navigateur et allez à l'adresse :

```
http://localhost:8080
```

Vous devriez voir la page d'accueil de Tomcat.

---

### 5. (Optionnel) Ajouter au PATH

Pour pouvoir exécuter `startup.sh` de n'importe où, ajoutez ceci à votre `~/.zshrc` ou `~/.bashrc` :

```bash
export CATALINA_HOME=~/tomcat
export PATH=$CATALINA_HOME/bin:$PATH
```

Rechargez :

```bash
source ~/.zshrc
```

---

👉 C'est terminé. Vous avez maintenant Tomcat qui fonctionne localement sur macOS.

Voulez-vous que je vous montre aussi **comment déployer un fichier WAR sur Tomcat sur macOS** après l'installation ?