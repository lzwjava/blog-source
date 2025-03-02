---
audio: true
generated: true
lang: fr
layout: post
title: Résoudre les problèmes de déploiement dans WebSphere Liberty Profile
translated: true
---

Lorsque vous essayez d'accéder à votre application Spring Boot à l'adresse `http://localhost:9080/myapp/` et que vous rencontrez une erreur "context root not found" sur WebSphere Liberty Profile (WLP), cela indique que WLP n'a pas déployé votre application sous la racine de contexte attendue (`/myapp`). Ce problème survient généralement en raison de problèmes de configuration de déploiement, de configuration du serveur ou du fichier WAR lui-même. Voici un guide complet pour diagnostiquer et résoudre ce problème.

---

### Compréhension du Problème
L'erreur "context root not found" signifie que WLP ne trouve pas d'application déployée à `/myapp`. Normalement, lorsque vous placez un fichier WAR nommé `myapp.war` dans le répertoire `dropins` de WLP, il devrait se déployer automatiquement avec la racine de contexte `/myapp`, le rendant accessible à `http://localhost:9080/myapp/`. Comme ce n'est pas le cas, nous devons investiguer pourquoi le déploiement a échoué.

---

### Étapes de Dépannage

#### 1. **Vérifier les Journaux du Serveur pour les Messages de Déploiement**
La première étape consiste à confirmer si WLP a déployé votre application.

- **Localiser les Journaux :**
  - Si votre serveur s'appelle `myServer`, vérifiez les journaux à :
    ```
    /opt/ibm/wlp/usr/servers/myServer/logs/messages.log
    ```
    ou
    ```
    /opt/ibm/wlp/usr/servers/myServer/logs/console.log
    ```
  - Si vous utilisez le serveur par défaut, remplacez `myServer` par `defaultServer`.

- **Rechercher la Confirmation de Déploiement :**
  - Vous devriez voir un message comme :
    ```
    [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myapp/
    ```
    Cela indique que l'application est déployée et disponible.
  - De plus, recherchez :
    ```
    CWWKZ0001I: Application myapp started in X.XXX seconds.
    ```
    Cela confirme que l'application a démarré avec succès.

- **Que Faire :**
  - Si ces messages sont absents, l'application n'a pas été déployée. Recherchez tout message `ERROR` ou `WARNING` dans les journaux qui pourrait indiquer pourquoi (par exemple, des fonctionnalités manquantes, des permissions de fichiers ou des échecs de démarrage).
  - Si vous voyez les journaux de démarrage de Spring Boot (par exemple, la bannière Spring Boot), l'application se charge, et le problème pourrait être lié à la racine de contexte ou au mappage d'URL.

#### 2. **Vérifier l'Emplacement et les Permissions du Fichier WAR**
Assurez-vous que le fichier WAR est correctement placé dans le répertoire `dropins` et est accessible par WLP.

- **Vérifier le Chemin :**
  - Pour un serveur nommé `myServer`, le fichier WAR devrait être à :
    ```
    /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war
    ```
  - Si vous utilisez `defaultServer`, ajustez en conséquence :
    ```
    /opt/ibm/wlp/usr/servers/defaultServer/dropins/myapp.war
    ```

- **Vérifier les Permissions :**
  - Assurez-vous que le processus WLP a des permissions de lecture pour le fichier. Sur un système de type Unix, exécutez :
    ```bash
    ls -l /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war
    ```
    Le fichier devrait être lisible par l'utilisateur exécutant WLP (par exemple, `rw-r--r--`).

- **Que Faire :**
  - Si le fichier est manquant ou mal placé, copiez-le dans le répertoire `dropins` correct :
    ```bash
    cp target/myapp.war /opt/ibm/wlp/usr/servers/myServer/dropins/
    ```
  - Corrigez les permissions si nécessaire :
    ```bash
    chmod 644 /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war
    ```

#### 3. **Confirmer la Surveillance des `dropins` dans `server.xml`**
Le répertoire `dropins` de WLP est activé par défaut, mais des configurations personnalisées pourraient le désactiver.

- **Vérifier `server.xml` :**
  - Ouvrez le fichier de configuration du serveur :
    ```
    /opt/ibm/wlp/usr/servers/myServer/server.xml
    ```
  - Recherchez l'élément `applicationMonitor` :
    ```xml
    <applicationMonitor updateTrigger="polled" pollingRate="5s" dropins="dropins" />
    ```
    Cela confirme que WLP surveille le répertoire `dropins` toutes les 5 secondes pour de nouvelles applications.

- **Que Faire :**
  - S'il est absent, ajoutez la ligne ci-dessus dans les balises `<server>` ou assurez-vous qu'aucune configuration de substitution ne désactive `dropins`.
  - Redémarrez le serveur après les modifications :
    ```bash
    /opt/ibm/wlp/bin/server stop myServer
    /opt/ibm/wlp/bin/server start myServer
    ```

#### 4. **Assurez-vous que les Fonctionnalités Nécessaires sont Activées**
WLP nécessite des fonctionnalités spécifiques pour déployer un fichier WAR Spring Boot, telles que le support Servlet.

- **Vérifier `server.xml` :**
  - Vérifiez la section `featureManager` pour inclure :
    ```xml
    <featureManager>
        <feature>javaee-8.0</feature>
    </featureManager>
    ```
    La fonctionnalité `javaee-8.0` inclut Servlet 4.0, qui est compatible avec Spring Boot. Alternativement, au moins `servlet-4.0` devrait être présent.

- **Que Faire :**
  - Si elle est manquante, ajoutez la fonctionnalité et redémarrez le serveur.

#### 5. **Valider la Structure du Fichier WAR**
Un fichier WAR corrompu ou mal structuré pourrait empêcher le déploiement.

- **Inspecter le WAR :**
  - Dézippez le fichier WAR pour vérifier son contenu :
    ```bash
    unzip -l myapp.war
    ```
  - Recherchez :
    - `WEB-INF/classes/com/example/demo/HelloController.class` (votre classe de contrôleur).
    - `WEB-INF/lib/` contenant les dépendances Spring Boot (par exemple, `spring-web-x.x.x.jar`).

- **Que Faire :**
  - Si la structure est incorrecte, reconstruisez le WAR :
    ```bash
    mvn clean package
    ```
    Assurez-vous que votre `pom.xml` définit `<packaging>war</packaging>` et marque `spring-boot-starter-tomcat` comme `<scope>provided</scope>`.

#### 6. **Déploiement Alternatif via le Répertoire `apps`**
Si `dropins` échoue, essayez de déployer l'application explicitement via le répertoire `apps`.

- **Étapes :**
  - Déplacez le fichier WAR :
    ```bash
    mv /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war /opt/ibm/wlp/usr/servers/myServer/apps/
    ```
  - Éditez `server.xml` pour ajouter :
    ```xml
    <application id="myapp" name="myapp" type="war" location="${server.config.dir}/apps/myapp.war">
        <context-root>/myapp</context-root>
    </application>
    ```
  - Redémarrez le serveur :
    ```bash
    /opt/ibm/wlp/bin/server restart myServer
    ```

- **Tester à Nouveau :**
  - Accédez à `http://localhost:9080/myapp/`. Si cela fonctionne, le problème était avec `dropins`.

#### 7. **Vérifier l'État du Serveur**
Assurez-vous que le serveur fonctionne correctement.

- **Vérifier l'État :**
  ```bash
  /opt/ibm/wlp/bin/server status myServer
  ```
  - S'il est arrêté, démarrez-le :
    ```bash
    /opt/ibm/wlp/bin/server start myServer
    ```

- **Tester WLP Lui-Même :**
  - Visitez `http://localhost:9080/`. Si WLP fonctionne, vous verrez une page d'accueil (sauf si elle est remplacée). Si cela échoue, il y a un problème plus large au niveau du serveur.

---

### Résolution
Pour corriger l'erreur "context root not found" :

1. **Commencez Ici :**
   - Vérifiez les journaux du serveur (`messages.log` ou `console.log`) pour les messages ou erreurs de déploiement.
   - Assurez-vous que `myapp.war` est dans le répertoire `dropins` avec les permissions appropriées.

2. **Étapes Suivantes :**
   - Vérifiez que `server.xml` active la fonctionnalité `javaee-8.0` et surveille `dropins`.
   - Si non résolu, déployez via le répertoire `apps` avec une configuration `<application>` explicite dans `server.xml`.

3. **Vérification Finale :**
   - Après avoir apporté des modifications, redémarrez WLP et accédez à `http://localhost:9080/myapp/`. Vous devriez voir "Hello World!" si le déploiement réussit.

En suivant ces étapes, vous identifierez si le problème est lié à la configuration du serveur, à l'emplacement du WAR ou au fichier WAR lui-même, et vous le résoudrez en conséquence.