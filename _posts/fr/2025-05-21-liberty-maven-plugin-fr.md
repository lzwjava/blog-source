---
audio: false
generated: true
lang: fr
layout: post
title: Plugin Maven Liberty
translated: true
type: note
---

Pour atteindre votre objectif d'exécuter un script dans IntelliJ IDEA sur Windows qui gère rapidement votre serveur Liberty et construit votre programme, tout en garantissant que le serveur est arrêté avant de remplacer le fichier EAR, je recommande d'utiliser le **Liberty Maven Plugin**. Cette approche est simple, s'intègre bien avec votre processus de build Maven et évite les problèmes que vous avez rencontrés avec le formatage des commandes et les fichiers batch.

Voici comment la configurer :

---

### Solution : Utilisation du Liberty Maven Plugin

#### Étape 1 : Ajouter le Liberty Maven Plugin à votre `pom.xml`
Le Liberty Maven Plugin vous permet de contrôler le serveur Liberty (démarrer, arrêter, déployer, etc.) directement depuis Maven, ce qui élimine le besoin de scripts complexes ou de fichiers batch.

- Ouvrez le fichier `pom.xml` de votre projet.
- Ajoutez la configuration de plugin suivante dans la section `<build>` :

```xml
<build>
    <plugins>
        <plugin>
            <groupId>io.openliberty.tools</groupId>
            <artifactId>liberty-maven-plugin</artifactId>
            <version>3.3.4</version>
            <configuration>
                <serverName>default</serverName>
                <installDirectory>C:\chemin\vers\liberty</installDirectory>
            </configuration>
        </plugin>
    </plugins>
</build>
```

- **Remplacez** `C:\chemin\vers\liberty` par le chemin réel vers votre répertoire d'installation de Liberty (par exemple, `C:\Program Files\IBM\WebSphere\Liberty`).
- Le `<serverName>default</serverName>` correspond à votre utilisation de `default` dans les commandes `server start default` et `server stop default`.

#### Étape 2 : Créer une configuration d'exécution Maven dans IntelliJ IDEA
Au lieu d'utiliser un script ou un fichier batch, vous pouvez configurer IntelliJ IDEA pour exécuter une séquence de goals Maven qui arrête le serveur, construit votre projet et redémarre le serveur.

- Dans IntelliJ IDEA, allez dans **Run > Edit Configurations...**.
- Cliquez sur le bouton **+** et sélectionnez **Maven** dans la liste.
- Configurez la configuration d'exécution :
  - **Name :** Donnez-lui un nom significatif, par exemple `Run Liberty`.
  - **Working directory :** Assurez-vous qu'il est défini sur le répertoire de votre projet (généralement détecté automatiquement).
  - **Command line :** Entrez la séquence de goals Maven suivante :
    ```
    liberty:stop package liberty:start
    ```
- Cliquez sur **Apply** puis sur **OK**.

#### Étape 3 : Exécuter la configuration
- Utilisez le bouton **Run** (triangle vert) dans IntelliJ IDEA pour exécuter cette configuration.
- Cela va :
  1. **Arrêter le serveur Liberty** (`liberty:stop`) : Garantit que le serveur ne fonctionne pas lors du remplacement du fichier EAR.
  2. **Construire votre projet** (`package`) : Exécute `mvn package` pour générer le fichier EAR.
  3. **Démarrer le serveur Liberty** (`liberty:start`) : Redémarre le serveur avec le fichier EAR mis à jour.

---

### Pourquoi cette solution fonctionne pour vous
- **Corrige les problèmes de format de commande :** Vous avez mentionné que l'utilisation de "Script text" dans la configuration d'exécution divise `server start default` en arguments séparés (`server`, `start`, `default`). L'approche Maven évite cela complètement en utilisant des goals de plugin bien définis.
- **Évite la complexité des fichiers batch :** Vous avez trouvé difficile de faire fonctionner correctement un fichier `.bat` (par exemple, à cause des chemins ou des paramètres d'environnement). Le Liberty Maven Plugin gère la gestion du serveur en interne, vous n'avez donc pas besoin de déboguer les commandes ou les chemins des fichiers batch.
- **Répond à votre exigence :** Vous avez besoin que le serveur soit arrêté lors du remplacement du fichier EAR pour éviter les problèmes de démarrage. Cette solution arrête explicitement le serveur avant la construction et le redémarre ensuite, garantissant un processus propre.

---

### Alternative : Utilisation d'un fichier batch (si préféré)
Si vous préférez rester avec un fichier batch, voici un exemple fonctionnel, bien qu'il soit moins recommandé en raison des problèmes que vous avez rencontrés :

1. Créez un fichier nommé `runLiberty.bat` dans votre répertoire de projet avec le contenu suivant :

```bat
@echo off
set LIBERTY_BIN=C:\chemin\vers\liberty\bin
set MAVEN_HOME=C:\chemin\vers\maven
set PATH=%PATH%;%LIBERTY_BIN%;%MAVEN_HOME%\bin

"%LIBERTY_BIN%\server" stop default
mvn package
"%LIBERTY_BIN%\server" start default
```

- Remplacez `C:\chemin\vers\liberty` et `C:\chemin\vers\maven` par les chemins réels vers vos installations Liberty et Maven.

2. Dans IntelliJ IDEA :
   - Allez dans **Run > Edit Configurations...**.
   - Cliquez sur **+** et sélectionnez **Batch file**.
   - Définissez le **Path to batch file** sur l'emplacement de `runLiberty.bat`.
   - Définissez le **Working directory** sur votre répertoire de projet.
   - Cliquez sur **Apply** et **OK**.

3. Exécutez-le en utilisant le bouton **Run**.

Cependant, cette méthode vous oblige à vous assurer manuellement que les chemins et les variables d'environnement sont corrects, ce que vous avez trouvé difficile. L'approche par plugin Maven est plus simple et plus fiable.

---

### Recommandation
Utilisez la méthode **Liberty Maven Plugin** décrite ci-dessus. Elle est :
- **Intégrée :** S'insère dans votre processus de build Maven existant.
- **Simple :** Pas besoin de lutter avec la syntaxe des fichiers batch ou les chemins.
- **Fiable :** Gère correctement l'arrêt et le démarrage du serveur, évitant les problèmes de remplacement du fichier EAR.

Cette configuration vous permettra d'exécuter votre programme rapidement et de manière cohérente dans IntelliJ IDEA sur votre serveur Liberty !