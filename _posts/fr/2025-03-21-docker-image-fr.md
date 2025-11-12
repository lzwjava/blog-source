---
audio: false
generated: true
lang: fr
layout: post
title: Construction et Déploiement d'une Image Docker
translated: true
type: note
---

Voici un guide étape par étape pour construire une applications Spring Boot en une image Docker et la déployer sur un serveur :

### Prérequis
1. **Java** (par exemple, JDK 17 ou une version compatible) installé localement.
2. **Maven** ou **Gradle** (selon la configuration de votre projet Spring Boot).
3. **Docker** installé sur votre machine locale et sur le serveur.
4. **Un projet Spring Boot** prêt à être conteneurisé.
5. **Un accès au serveur** (par exemple, via SSH) avec Docker installé.

---

### Étape 1 : Préparer votre application Spring Boot
Assurez-vous que votre application Spring Boot fonctionne localement. Testez-la avec :
```bash
mvn spring-boot:run  # Si vous utilisez Maven
# OU
gradle bootRun       # Si vous utilisez Gradle
```

Assurez-vous que l'application se construit avec succès :
```bash
mvn clean package    # Maven
# OU
gradle build         # Gradle
```
Cela génère un fichier `.jar` (par exemple, `target/myapp-1.0.0.jar`).

---

### Étape 2 : Créer un Dockerfile
Dans le répertoire racine de votre projet (où se trouve le fichier `.jar`), créez un fichier nommé `Dockerfile` avec le contenu suivant :

```dockerfile
# Utiliser une image OpenJDK officielle comme image de base
FROM openjdk:17-jdk-slim

# Définir le répertoire de travail à l'intérieur du conteneur
WORKDIR /app

# Copier le fichier JAR Spring Boot dans le conteneur
COPY target/myapp-1.0.0.jar app.jar

# Exposer le port sur lequel votre application Spring Boot s'exécute (par défaut 8080)
EXPOSE 8080

# Exécuter le fichier JAR
ENTRYPOINT ["java", "-jar", "app.jar"]
```

**Notes :**
- Remplacez `myapp-1.0.0.jar` par le nom réel de votre fichier JAR.
- Ajustez la version de Java (`openjdk:17-jdk-slim`) si votre application utilise une version différente.

---

### Étape 3 : Construire l'image Docker
Depuis le répertoire contenant le `Dockerfile`, exécutez :
```bash
docker build -t myapp:latest .
```
- `-t myapp:latest` tag l'image comme `myapp` avec la version `latest`.
- Le `.` indique à Docker d'utiliser le répertoire courant comme contexte de build.

Vérifiez que l'image a été créée :
```bash
docker images
```

---

### Étape 4 : Tester l'image Docker localement
Exécutez le conteneur localement pour vous assurer qu'il fonctionne :
```bash
docker run -p 8080:8080 myapp:latest
```
- `-p 8080:8080` mappe le port 8080 de votre machine sur le port 8080 du conteneur.
- Ouvrez un navigateur ou utilisez `curl` pour tester (par exemple, `curl http://localhost:8080`).

Arrêtez le conteneur avec `Ctrl+C` ou trouvez son ID avec `docker ps` et arrêtez-le :
```bash
docker stop <container-id>
```

---

### Étape 5 : Pousser l'image vers un registre Docker (Optionnel)
Pour déployer sur un serveur, vous devrez pousser l'image vers un registre comme Docker Hub (ou un registre privé). Si vous ignorez cette étape, vous devrez transférer l'image manuellement.

1. Connectez-vous à Docker Hub :
   ```bash
   docker login
   ```
2. Taguez votre image :
   ```bash
   docker tag myapp:latest yourusername/myapp:latest
   ```
3. Poussez l'image :
   ```bash
   docker push yourusername/myapp:latest
   ```

---

### Étape 6 : Déployer sur le serveur
#### Option 1 : Utilisation d'un registre
1. SSH dans votre serveur :
   ```bash
   ssh user@server-ip
   ```
2. Tirez l'image :
   ```bash
   docker pull yourusername/myapp:latest
   ```
3. Exécutez le conteneur :
   ```bash
   docker run -d -p 8080:8080 yourusername/myapp:latest
   ```
   - `-d` exécute le conteneur en mode détaché (arrière-plan).

#### Option 2 : Transfert manuel
Si vous n'avez pas utilisé de registre :
1. Sauvegardez l'image localement en tant que fichier `.tar` :
   ```bash
   docker save -o myapp.tar myapp:latest
   ```
2. Transférez-la vers le serveur (par exemple, via SCP) :
   ```bash
   scp myapp.tar user@server-ip:/path/to/destination
   ```
3. SSH dans le serveur :
   ```bash
   ssh user@server-ip
   ```
4. Chargez l'image :
   ```bash
   docker load -i myapp.tar
   ```
5. Exécutez le conteneur :
   ```bash
   docker run -d -p 8080:8080 myapp:latest
   ```

---

### Étape 7 : Vérifier le déploiement
Vérifiez si le conteneur est en cours d'exécution :
```bash
docker ps
```

Testez l'application depuis le serveur ou de manière externe :
- Si sur le serveur : `curl http://localhost:8080`
- Si externe : Utilisez l'IP du serveur (par exemple, `http://server-ip:8080`), en vous assurant que le port est ouvert dans le firewall du serveur.

---

### Optionnel : Améliorations
- **Variables d'environnement** : Passez des configurations à votre application :
  ```bash
  docker run -d -p 8080:8080 -e "SPRING_PROFILES_ACTIVE=prod" myapp:latest
  ```
- **Docker Compose** : Pour les configurations multi-conteneurs, utilisez un fichier `docker-compose.yml`.
- **Politique de redémarrage** : Ajoutez `--restart unless-stopped` pour garantir que le conteneur redémarre en cas de reboot du serveur.

Faites-moi savoir si vous avez besoin d'aide pour une partie spécifique !

---

D'après la sortie d'erreur que vous avez fournie, il y a quelques problèmes qui empêchent votre commande `docker build` de réussir. Décomposons-les et résolvons-les étape par étape.

---

### Problèmes identifiés
1. **Plugin `docker-buildx` manquant**
   Erreur : `fork/exec /Users/lzwjava/.docker/cli-plugins/docker-buildx: no such file or directory`
   Cela suggère que Docker essaie d'utiliser le plugin `buildx` (un outil de build moderne), mais il n'est pas installé ou configuré correctement.

2. **Avertissement de dépréciation de l'ancien builder**
   Avertissement : `DEPRECATED: The legacy builder is deprecated...`
   Docker recommande de passer à BuildKit (`buildx`), mais il revient à l'ancien builder, qui échoue.

3. **Docker Daemon non exécuté**
   Erreur : `Cannot connect to the Docker daemon at unix:///Users/lzwjava/.docker/run/docker.sock. Is the docker daemon running?`
   Le démon Docker (le service en arrière-plan qui gère les conteneurs) ne fonctionne pas sur votre système.

4. **Erreurs d'accès aux fichiers**
   Erreurs : `Can't add file ... to tar: io: read/write on closed pipe` et `Can't close tar writer...`
   Ce sont des problèmes secondaires causés par l'échec du processus de build dû au démon non exécuté.

5. **Paramètres de proxy détectés**
   Votre système utilise des proxys (`HTTP_PROXY` et `HTTPS_PROXY`). Cela pourrait interférer avec Docker s'il n'est pas configuré correctement.

---

### Correction étape par étape

#### 1. Vérifier que le Docker Daemon est en cours d'exécution
Le problème principal est que le démon Docker ne fonctionne pas. Voici comment le corriger :

- **Sur macOS** (en supposant que vous utilisez Docker Desktop) :
  1. Ouvrez Docker Desktop depuis votre dossier Applications ou Spotlight.
  2. Assurez-vous qu'il fonctionne (vous verrez l'icône de la baleine Docker dans la barre de menus devenir verte).
  3. S'il ne démarre pas :
     - Quittez Docker Desktop et redémarrez-le.
     - Vérifiez les mises à jour : Docker Desktop > Check for Updates.
     - S'il échoue toujours, réinstallez Docker Desktop depuis [docker.com](https://www.docker.com/products/docker-desktop/).

- **Vérifier via le Terminal** :
  Exécutez :
  ```bash
  docker info
  ```
  Si le démon est en cours d'exécution, vous verrez les informations système. Sinon, vous obtiendrez la même erreur "Cannot connect".

- **Redémarrer le démon manuellement** (si nécessaire) :
  ```bash
  sudo launchctl stop com.docker.docker
  sudo launchctl start com.docker.docker
  ```

Une fois le démon en cours d'exécution, passez aux étapes suivantes.

---

#### 2. Installer le plugin `buildx` (Optionnel mais recommandé)
Étant donné que l'ancien builder est déprécié, configurons `buildx` :

1. **Installer `buildx`** :
   - Téléchargez le binaire manuellement ou suivez les instructions de Docker :
     ```bash
     mkdir -p ~/.docker/cli-plugins
     curl -SL https://github.com/docker/buildx/releases/download/v0.13.0/buildx-v0.13.0.darwin-amd64 -o ~/.docker/cli-plugins/docker-buildx
     chmod +x ~/.docker/cli-plugins/docker-buildx
     ```
     (Vérifiez la [dernière release](https://github.com/docker/buildx/releases) pour votre OS/architecture, par exemple, `darwin-arm64` pour les Macs M1/M2.)

2. **Vérifier l'installation** :
   ```bash
   docker buildx version
   ```

3. **Définir BuildKit par défaut** (optionnel) :
   Ajoutez ceci à `~/.docker/config.json` :
   ```json
   {
     "features": { "buildkit": true }
   }
   ```

Alternativement, vous pouvez ignorer cela et utiliser l'ancien builder pour l'instant (voir Étape 4).

---

#### 3. Gérer les paramètres de proxy
Vos paramètres de proxy (`http://127.0.0.1:7890`) pourraient interférer avec la capacité de Docker à récupérer les images. Configurez Docker pour les utiliser :

1. **Via Docker Desktop** :
   - Ouvrez Docker Desktop > Settings > Resources > Proxies.
   - Activez "Manual proxy configuration" et entrez :
     - HTTP Proxy: `http://127.0.0.1:7890`
     - HTTPS Proxy: `http://127.0.0.1:7890`
   - Appliquez & Redémarrez.

2. **Via CLI** (si vous n'utilisez pas Desktop) :
   Créez ou modifiez `~/.docker/config.json` :
   ```json
   {
     "proxies": {
       "default": {
         "httpProxy": "http://127.0.0.1:7890",
         "httpsProxy": "http://127.0.0.1:7890"
       }
     }
   }
   ```
   Redémarrez Docker après l'édition.

---

#### 4. Réessayer le build
Maintenant que le démon est en cours d'exécution et que les proxys sont configurés, essayez de construire à nouveau :

```bash
docker build -t myapp:latest .
```

- Si vous avez installé `buildx`, il utilisera BuildKit par défaut.
- Si vous avez ignoré `buildx`, ajoutez `--progress=plain` pour forcer l'ancien builder :
  ```bash
  docker build --progress=plain -t myapp:latest .
  ```

---

#### 5. Dépanner l'erreur `.git/hooks` (Si elle persiste)
L'erreur `.git/hooks/pre-rebase.sample` suggère que Docker essaie d'inclure des fichiers inutiles dans le contexte de build. Excluez-les avec un fichier `.dockerignore` :

1. Créez `.dockerignore` dans le même répertoire que votre `Dockerfile` :
   ```
   .git
   .gitignore
   *.md
   target/*
   !target/*.jar
   ```
2. Cela indique à Docker d'ignorer le dossier `.git` et tout ce qui se trouve dans `target/` sauf votre fichier JAR.

3. Réessayez le build :
   ```bash
   docker build -t myapp:latest .
   ```

---

### Vérification finale
- Vérifiez l'image :
  ```bash
  docker images
  ```
- Exécutez-la localement :
  ```bash
  docker run -p 8080:8080 myapp:latest
  ```
- Testez avec `curl http://localhost:8080`.

---

### Prochaines étapes
Une fois que l'image est construite avec succès, suivez les étapes de déploiement de ma réponse précédente (par exemple, poussez vers un registre ou transférez vers un serveur). Faites-moi savoir si vous rencontrez d'autres problèmes !