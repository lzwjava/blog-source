---
audio: false
generated: true
lang: fr
layout: post
title: Paramètres de proxy Maven
translated: true
type: note
---

D'après la sortie de votre commande `checkproxy`, vos proxys HTTP et HTTPS sont tous deux configurés sur `http://127.0.0.1:7890`. Voici l'extrait de configuration Maven `settings.xml` mis à jour pour configurer Maven afin d'utiliser ces paramètres de proxy.

### Extrait de configuration de proxy `settings.xml` mis à jour

Ajoutez ou mettez à jour la section `<proxies>` dans votre fichier Maven `settings.xml` (situé à `~/.m2/settings.xml` ou `/usr/share/maven/conf/settings.xml`) avec le contenu suivant :

```xml
<settings>
  <proxies>
    <proxy>
      <id>http-proxy</id>
      <active>true</active>
      <protocol>http</protocol>
      <host>127.0.0.1</host>
      <port>7890</port>
      <nonProxyHosts>localhost|127.0.0.1</nonProxyHosts>
    </proxy>
    <proxy>
      <id>https-proxy</id>
      <active>true</active>
      <protocol>https</protocol>
      <host>127.0.0.1</host>
      <port>7890</port>
      <nonProxyHosts>localhost|127.0.0.1</nonProxyHosts>
    </proxy>
  </proxies>
</settings>
```

### Explication de l'extrait
- **`<id>`** : Identifiants uniques (`http-proxy` et `https-proxy`) pour chaque configuration de proxy.
- **`<active>true</active>`** : Active le proxy.
- **`<protocol>`** : Défini sur `http` pour le proxy HTTP et `https` pour le proxy HTTPS, correspondant à la sortie de votre `checkproxy`.
- **`<host>127.0.0.1</host>`** : L'adresse IP du serveur proxy, comme indiqué dans vos paramètres de proxy.
- **`<port>7890</port>`** : Le numéro de port pour les deux proxys, comme spécifié.
- **`<nonProxyHosts>localhost|127.0.0.1</nonProxyHosts>`** : Exclut `localhost` et `127.0.0.1` d'être proxifiés, ce qui est standard pour éviter les problèmes avec les services locaux.
- **Pas de `<username>` ou `<password>`** : Étant donné que votre sortie de proxy n'indique pas d'authentification, ces champs sont omis. Si une authentification est requise, ajoutez-les avec vos identifiants.

### Étapes à appliquer
1. **Ouvrez `settings.xml`** :
   - Si `~/.m2/settings.xml` existe, modifiez-le (par exemple, `nano ~/.m2/settings.xml`).
   - S'il n'existe pas, créez-le ou modifiez le fichier global à `/usr/share/maven/conf/settings.xml` (nécessite `sudo`).

2. **Insérez ou mettez à jour la section `<proxies>`** :
   - Si `<proxies>` existe déjà, remplacez ou fusionnez les entrées `<proxy>` avec l'extrait ci-dessus.
   - Si `<settings>` est vide ou minimal, vous pouvez utiliser l'extrait entier comme contenu du fichier.

3. **Enregistrez et fermez** le fichier.

### Vérifiez la configuration
Exécutez une commande Maven qui nécessite un accès Internet pour confirmer que le proxy est utilisé :
```bash
cd ~/Projects/blog-server
mvn -X clean checkstyle:check
```

Dans la sortie de débogage (`-X`), recherchez les lignes indiquant que Maven utilise le proxy (par exemple, des connexions à `127.0.0.1:7890`). Si la commande télécharge des dépendances ou se termine sans erreurs réseau, le proxy fonctionne.

### Dépannage
- **Proxy ne fonctionne pas** :
  - Assurez-vous que le serveur proxy sur `127.0.0.1:7890` est en cours d'exécution (par exemple, testez avec `curl -x http://127.0.0.1:7890 https://repo.maven.apache.org`).
  - Vérifiez les fautes de frappe dans le fichier `settings.xml`.
- **Fichier de paramètres ignoré** :
  - Confirmez que Maven lit `~/.m2/settings.xml` en vérifiant le chemin du fichier dans la sortie de débogage.
  - Si vous utilisez le fichier global, assurez-vous d'avoir correctement modifié `/usr/share/maven/conf/settings.xml`.
- **Authentification requise** :
  - Si votre proxy nécessite un nom d'utilisateur et un mot de passe, ajoutez :
    ```xml
    <username>yourusername</username>
    <password>yourpassword</password>
    ```
    à chaque bloc `<proxy>`.

### Note sur le contexte précédent
Votre problème `checkstyle:check` dans le projet `blog-server` (lié à `checks.xml` et `SuppressWithNearbyTextFilter`) devrait être résolu séparément en mettant à jour le `pom.xml` comme suggéré précédemment (en utilisant `maven-checkstyle-plugin:3.3.1` avec Checkstyle `10.17.0` et `<configLocation>${project.basedir}/checks.xml</configLocation>`). Les paramètres de proxy ci-dessus garantiront que Maven peut télécharger tous les artefacts requis pour cette correction.

Faites-moi savoir si vous rencontrez des problèmes ou si vous avez besoin d'aide avec le `pom.xml` mis à jour ou pour un débogage supplémentaire du proxy !