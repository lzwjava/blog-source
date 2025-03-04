---
audio: true
generated: true
lang: fr
layout: post
title: Déploiement d'EAR dans WebSphere Liberty Profile
translated: true
---

On dirait que vous avez réussi à créer un fichier EAR (Enterprise Archive) en utilisant `mvn package` avec Maven, et le processus de construction s'est terminé sans aucune erreur. Cependant, lorsque vous déployez cet EAR sur WebSphere Liberty Profile (WLP) et démarrez le serveur, vous rencontrez l'erreur "no module found." Cela est déroutant car une construction fluide suggère généralement que tout est en ordre, mais le serveur ne reconnaît pas votre application comme prévu. Décomposons cela et essayons de comprendre ce qui pourrait se passer, ainsi que les étapes pour résoudre le problème.

### Compréhension du Problème
Un fichier EAR est une archive Java EE standard qui emballe votre application, contenant généralement un ou plusieurs modules tels que des fichiers WAR (pour les applications web), des fichiers JAR (pour les EJBs ou les bibliothèques), et un descripteur de déploiement (`application.xml`). Lorsque vous déployez un EAR sur WLP, le serveur devrait détecter ces modules et démarrer l'application. Le message "no module found" suggère que WLP ne trouve pas de modules dans votre EAR ou ne les reconnaît pas, empêchant le démarrage de l'application.

Puisque votre construction Maven a été réussie ("tout est fluide"), le problème pourrait se situer dans l'une des trois zones suivantes :
1. **Le contenu du fichier EAR** : L'EAR pourrait ne pas contenir les modules attendus, ou le descripteur de déploiement pourrait être manquant ou incorrect.
2. **Le processus de déploiement** : La manière dont vous déployez l'EAR sur WLP pourrait ne pas correspondre à la manière dont le serveur s'attend à le trouver et à le traiter.
3. **La configuration du serveur** : WLP pourrait ne pas être configuré pour reconnaître les modules dans votre EAR en raison de fonctionnalités manquantes ou d'une mauvaise configuration.

Explorons ces possibilités et fournissons des étapes concrètes pour diagnostiquer et résoudre le problème.

---

### Causes Possibles et Solutions

#### 1. Le Fichier EAR Pourrait Être Vide ou Incorrectement Emballé
Même si la construction a été réussie, il est possible que votre EAR ne contienne aucun module (par exemple, des fichiers WAR ou JAR) ou que le fichier `application.xml`, qui indique au serveur quels modules sont inclus, soit manquant ou mal configuré.

- **Pourquoi cela se produit** : Dans un projet EAR Maven, le plugin `maven-ear-plugin` est responsable de l'assemblage de l'EAR. Il inclut des modules en fonction de votre configuration `pom.xml` ou des dépendances. Si aucun module n'est spécifié, ou si les dépendances (comme un WAR) ne sont pas correctement définies ou résolues, l'EAR pourrait être vide ou manquer d'un `application.xml` approprié.
- **Comment vérifier** :
  - Ouvrez votre fichier EAR (c'est une archive ZIP) à l'aide d'un outil comme `unzip` ou exécutez `jar tf myApp.ear` dans le terminal pour lister son contenu.
  - Recherchez :
    - Les fichiers de modules (par exemple, `my-web.war`, `my-ejb.jar`) à la racine de l'EAR.
    - Un fichier `META-INF/application.xml`.
  - À l'intérieur de `application.xml`, vous devriez voir des entrées définissant vos modules, comme :
    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <application>
        <module>
            <web>
                <web-uri>my-web.war</web-uri>
                <context-root>/myapp</context-root>
            </web>
        </module>
    </application>
    ```
- **Comment corriger** :
  - Vérifiez votre `pom.xml` pour le module EAR. Assurez-vous d'avoir spécifié les dépendances pour les modules que vous souhaitez inclure, par exemple :
    ```xml
    <dependencies>
        <dependency>
            <groupId>com.example</groupId>
            <artifactId>my-web</artifactId>
            <type>war</type>
        </dependency>
    </dependencies>
    ```
  - Configurez le plugin `maven-ear-plugin` si nécessaire :
    ```xml
    <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-ear-plugin</artifactId>
        <version>3.3.0</version>
        <configuration>
            <modules>
                <webModule>
                    <groupId>com.example</groupId>
                    <artifactId>my-web</artifactId>
                    <contextRoot>/myapp</contextRoot>
                </webModule>
            </modules>
        </configuration>
    </plugin>
    ```
  - Reconstruisez avec `mvn clean package` et revérifiez le contenu de l'EAR.

Si l'EAR est vide ou `application.xml` est manquant/incorrect, c'est probablement la cause principale. Corriger la configuration Maven devrait résoudre le problème.

---

#### 2. Problème de Méthode de Déploiement
La manière dont vous déployez l'EAR sur WLP pourrait également être le problème. WLP prend en charge deux méthodes de déploiement principales : le répertoire `dropins` et la configuration explicite dans `server.xml`.

- **Utilisation du répertoire `dropins`** :
  - Si vous avez placé l'EAR dans le répertoire `wlp/usr/servers/<serverName>/dropins/`, WLP devrait automatiquement le détecter et le déployer.
  - Cependant, pour les fichiers EAR, le déploiement automatique ne fonctionne pas toujours comme prévu, surtout si une configuration supplémentaire (comme les racines de contexte) est nécessaire.
- **Utilisation de `server.xml`** :
  - Pour les fichiers EAR, il est souvent préférable de configurer explicitement l'application dans `wlp/usr/servers/<serverName>/server.xml` :
    ```xml
    <server>
        <featureManager>
            <feature>servlet-3.1</feature> <!-- Assurez-vous que les fonctionnalités requises sont activées -->
        </featureManager>
        <application id="myApp" name="myApp" type="ear" location="${server.config.dir}/apps/myApp.ear"/>
    </server>
    ```
  - Placez l'EAR dans `wlp/usr/servers/<serverName>/apps/` (ou ajustez le chemin `location` en conséquence).
- **Comment vérifier** :
  - Confirmez où vous avez placé l'EAR et comment vous démarrez le serveur (par exemple, `./bin/server run <serverName>`).
  - Vérifiez les journaux du serveur (par exemple, `wlp/usr/servers/<serverName>/logs/console.log` ou `messages.log`) pour les messages de déploiement.
- **Comment corriger** :
  - Essayez de configurer l'EAR dans `server.xml` comme montré ci-dessus au lieu de compter sur `dropins`.
  - Redémarrez le serveur après avoir apporté des modifications : `./bin/server stop <serverName>` suivi de `./bin/server start <serverName>`.

Si l'EAR n'a pas été correctement enregistré avec le serveur, cela pourrait expliquer l'erreur.

---

#### 3. Fonctionnalités Serveur Manquantes
WLP est un serveur léger qui ne charge que les fonctionnalités que vous activez dans `server.xml`. Si votre EAR contient des modules nécessitant des fonctionnalités spécifiques (par exemple, des servlets, des EJBs), et que ces fonctionnalités ne sont pas activées, WLP pourrait ne pas reconnaître ou charger les modules.

- **Pourquoi cela se produit** : Par exemple, un fichier WAR a besoin de la fonctionnalité `servlet-3.1` (ou supérieure), tandis qu'un module EJB a besoin de `ejbLite-3.2`. Sans celles-ci, le serveur pourrait échouer à traiter les modules.
- **Comment vérifier** :
  - Regardez votre `server.xml` et vérifiez la section `<featureManager>`.
  - Les fonctionnalités courantes incluent :
    - `<feature>servlet-3.1</feature>` pour les modules web.
    - `<feature>ejbLite-3.2</feature>` pour les modules EJB.
  - Passez en revue les journaux du serveur pour des messages concernant des fonctionnalités manquantes (par exemple, "la fonctionnalité requise n'est pas installée").
- **Comment corriger** :
  - Ajoutez les fonctionnalités nécessaires à `server.xml` en fonction des besoins de votre application :
    ```xml
    <featureManager>
        <feature>servlet-3.1</feature>
        <!-- Ajoutez d'autres fonctionnalités si nécessaire -->
    </featureManager>
    ```
  - Redémarrez le serveur pour appliquer les modifications.

Si les fonctionnalités sont manquantes, les activer devrait permettre à WLP de reconnaître les modules.

---

### Étapes de Diagnostic
Pour identifier le problème, suivez ces étapes :

1. **Inspecter le Fichier EAR** :
   - Exécutez `jar tf myApp.ear` ou décompressez-le.
   - Assurez-vous qu'il contient vos modules (par exemple, `my-web.war`) et un `META-INF/application.xml` valide.

2. **Vérifier la Construction Maven** :
   - Passez en revue le `pom.xml` de votre module EAR pour confirmer les dépendances et la configuration du plugin `maven-ear-plugin`.
   - Exécutez `mvn clean package` à nouveau et vérifiez la sortie de la construction pour des messages concernant l'inclusion de modules (par exemple, "Ajout du module my-web.war").

3. **Vérifier le Déploiement** :
   - Confirmez l'emplacement de l'EAR (par exemple, `dropins` ou `apps`).
   - Si vous utilisez `dropins`, essayez de le déplacer vers `apps` et de l'ajouter à `server.xml`.

4. **Examiner les Journaux du Serveur** :
   - Démarrez le serveur et vérifiez `console.log` ou `messages.log` pour des messages d'erreur détaillés au-delà de "no module found."
   - Recherchez des indices comme "l'application ne contient aucun module" ou des erreurs liées aux fonctionnalités.

5. **Tester avec un EAR Simple** :
   - Créez un EAR de base avec un seul fichier WAR en utilisant un `pom.xml` connu pour fonctionner et déployez-le sur WLP. Si cela fonctionne, le problème est spécifique à l'emballage de votre EAR d'origine.

---

### Cause la Plus Probable
Étant donné que votre construction était fluide mais que WLP signale "no module found," la cause la plus probable est que **le fichier EAR ne contient aucun module** ou **le `application.xml` est manquant/incorrect**. Cela pourrait se produire si votre `pom.xml` ne spécifie pas correctement les modules à inclure, même si Maven n'a pas signalé d'erreur. Alternativement, si l'EAR est correct, le problème pourrait être lié au déploiement (par exemple, non configuré dans `server.xml`) ou à des fonctionnalités serveur manquantes.

### Recommandation Finale
- Commencez par vérifier le contenu de l'EAR (`jar tf myApp.ear`) et la configuration de votre `pom.xml`.
- Si l'EAR est vide ou manque de `application.xml`, corrigez la configuration Maven et reconstruisez.
- Si l'EAR semble correct, configurez-le dans `server.xml`, assurez-vous que les fonctionnalités requises sont activées, et redeployez.
- Vérifiez les journaux du serveur pour un contexte supplémentaire.

En suivant ces étapes, vous devriez être en mesure d'identifier si le problème se situe dans la construction, le déploiement ou la configuration du serveur et de faire fonctionner votre application sur WLP avec succès. Faites-moi savoir si vous avez besoin d'aide pour des configurations spécifiques !