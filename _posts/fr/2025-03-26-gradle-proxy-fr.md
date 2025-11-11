---
audio: false
generated: true
lang: fr
layout: post
title: Configurer le proxy pour Gradle dans VSCode
translated: true
type: note
---

Pour configurer un proxy pour Gradle dans Visual Studio Code (VSCode) afin qu'il puisse télécharger les dépendances via un proxy, vous devez configurer les paramètres du proxy dans la configuration de Gradle. Gradle utilise un fichier properties pour gérer ces paramètres, et VSCode s'appuie sur le système de build de Gradle pour les projets Gradle. Voici comment procéder :

### Étapes pour configurer le proxy pour Gradle dans VSCode

1. **Localiser ou créer le fichier Properties de Gradle**
   - Gradle utilise un fichier appelé `gradle.properties` pour stocker les paramètres de configuration globaux.
   - Ce fichier se trouve généralement dans le répertoire utilisateur de Gradle :
     - Sur Windows : `C:\Users\<VotreNomUtilisateur>\.gradle\gradle.properties`
     - Sur macOS/Linux : `~/.gradle/gradle.properties`
   - Si le fichier n'existe pas, créez-le à l'emplacement indiqué ci-dessus.

2. **Ajouter les paramètres de proxy à `gradle.properties`**
   - Ouvrez le fichier `gradle.properties` dans un éditeur de texte.
   - Ajoutez les lignes suivantes en remplaçant les espaces réservés (`<proxyHost>`, `<proxyPort>`, `<username>`, `<password>`) par vos détails de proxy réels :
     ```
     systemProp.http.proxyHost=<proxyHost>
     systemProp.http.proxyPort=<proxyPort>
     systemProp.http.proxyUser=<username>
     systemProp.http.proxyPassword=<password>
     systemProp.https.proxyHost=<proxyHost>
     systemProp.https.proxyPort=<proxyPort>
     systemProp.https.proxyUser=<username>
     systemProp.https.proxyPassword=<password>
     ```
   - Exemple avec des valeurs réelles :
     ```
     systemProp.http.proxyHost=proxy.example.com
     systemProp.http.proxyPort=8080
     systemProp.http.proxyUser=myuser
     systemProp.http.proxyPassword=mypassword
     systemProp.https.proxyHost=proxy.example.com
     systemProp.https.proxyPort=8080
     systemProp.https.proxyUser=myuser
     systemProp.https.proxyPassword=mypassword
     ```
   - Si votre proxy ne nécessite pas d'authentification (nom d'utilisateur/mot de passe), vous pouvez omettre les lignes `proxyUser` et `proxyPassword`.

3. **Optionnel : Configurer le proxy par projet**
   - Si vous souhaitez que les paramètres de proxy s'appliquent uniquement à un projet spécifique (au lieu de globalement), vous pouvez ajouter le fichier `gradle.properties` au répertoire racine de votre projet (par exemple, `<racine-du-projet>/gradle.properties`) avec le même contenu que ci-dessus.

4. **Vérifier que Gradle utilise le proxy**
   - Ouvrez votre projet Gradle dans VSCode.
   - Exécutez une tâche de build (par exemple, `gradle build`) via le terminal de VSCode ou l'extension Gradle.
   - Gradle devrait maintenant router ses téléchargements (comme les dépendances depuis le site officiel) via le proxy spécifié.

5. **Notes spécifiques à VSCode**
   - Assurez-vous que le **Java Extension Pack** et l'extension **Gradle for Java** sont installés dans VSCode, car ils améliorent la prise en charge des projets Gradle.
   - Si VSCode rencontre encore des problèmes, vérifiez que votre runtime Java (utilisé par Gradle) respecte également le proxy. Vous devrez peut-être définir des arguments de proxy JVM :
     - Dans VSCode, allez dans `File > Preferences > Settings`.
     - Recherchez `java.gradle.build.jvmArguments`.
     - Ajoutez quelque chose comme :
       ```
       -Dhttp.proxyHost=<proxyHost> -Dhttp.proxyPort=<proxyPort> -Dhttps.proxyHost=<proxyHost> -Dhttps.proxyPort=<proxyPort>
       ```

6. **Tester la configuration**
   - Rechargez votre projet dans VSCode (par exemple, fermez et rouvrez-le ou utilisez le bouton "Refresh" dans la barre latérale Gradle).
   - Exécutez une tâche Gradle (par exemple, `gradle build` ou `gradle dependencies`) pour confirmer qu'il télécharge les fichiers via le proxy.

### Dépannage
- **Vérifier les détails du proxy** : Assurez-vous que l'hôte, le port et les identifiants de votre proxy sont corrects.
- **Pare-feu ou réseau** : Si cela échoue encore, votre proxy ou votre réseau pourrait bloquer des URL Gradle spécifiques (par exemple, `https://services.gradle.org`). Testez avec une commande comme `curl` ou consultez votre administrateur réseau.
- **Sortie détaillée** : Exécutez Gradle avec `--debug` ou `--info` (par exemple, `gradle build --debug`) dans le terminal VSCode pour voir les journaux détaillés des requêtes réseau.

Cette configuration devrait permettre à Gradle dans VSCode de télécharger les dépendances via votre proxy avec succès. Faites-moi savoir si vous rencontrez des problèmes !