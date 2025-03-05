---
audio: false
generated: true
lang: fr
layout: post
title: Fichiers JAR manquants dans WebSphere Liberty
translated: true
---

Dans WebSphere Liberty, vous avez remarqué des avertissements dans le fichier `console.log` qui ressemblent à ceci : *"le chemin de classe du manifeste : grpc-protobuf.jar ne peut pas être trouvé dans le fichier jar ..ear/war ou son parent"*. Ces avertissements indiquent que le serveur ne peut pas localiser le fichier `grpc-protobuf.jar`, qui est référencé dans le chemin de classe du manifeste d'un fichier EAR ou WAR dans votre application. Ci-dessous, je vais répondre à vos questions : savoir si ces avertissements sont importants, s'ils affecteront le fonctionnement de votre application, et comment les supprimer.

---

### Ces avertissements sont-ils importants ?

Oui et non—cela dépend de savoir si le JAR manquant est nécessaire pour votre application :

- **Si le JAR est nécessaire :**
  Si `grpc-protobuf.jar` contient des classes ou des ressources dont votre application a besoin au moment de l'exécution, cet avertissement est significatif. Sans le JAR, votre application pourrait rencontrer des erreurs d'exécution comme `ClassNotFoundException`, ce qui pourrait entraîner des échecs partiels ou un comportement incorrect de certaines parties de l'application.

- **Si le JAR n'est pas nécessaire :**
  Si le JAR n'est pas réellement nécessaire—peut-être qu'il s'agit d'une référence obsolète provenant d'une ancienne configuration ou d'une dépendance optionnelle—l'avertissement est inoffensif et n'affectera pas le fonctionnement de votre application. Cependant, il continuera à encombrer vos journaux.

En résumé, ces avertissements sont importants si le JAR manquant est crucial pour votre application. Vous devrez enquêter pour déterminer son importance.

---

### Cela affectera-t-il le fonctionnement de l'application ?

L'impact sur le temps d'exécution de votre application dépend du rôle du JAR manquant :

- **Oui, si le JAR est requis :**
  Si votre application tente d'utiliser des classes ou des ressources de `grpc-protobuf.jar` et qu'il est manquant, vous verrez probablement des erreurs d'exécution. Cela pourrait empêcher votre application de fonctionner correctement ou la faire échouer complètement.

- **Non, si le JAR est superflu :**
  Si le JAR n'est pas nécessaire, votre application fonctionnera bien malgré l'avertissement. Le message restera simplement dans les journaux comme une nuisance.

Pour confirmer, vérifiez le comportement de votre application et les journaux pour des erreurs au-delà de l'avertissement lui-même. Si tout fonctionne comme prévu, le JAR peut ne pas être essentiel.

---

### Comment supprimer l'avertissement ?

Pour éliminer l'avertissement, vous devez soit vous assurer que le JAR est correctement inclus dans votre application, soit supprimer la référence inutile. Voici une approche étape par étape :

1. **Vérifiez si le JAR est nécessaire :**
   - Passez en revue la documentation de votre application, le code source ou la liste des dépendances (par exemple, `pom.xml` si vous utilisez Maven) pour déterminer si `grpc-protobuf.jar` est requis.
   - Si ce n'est pas nécessaire, passez à l'étape 3 pour supprimer la référence. Si c'est nécessaire, continuez à l'étape 2.

2. **Corrigez l'emballage (si le JAR est nécessaire) :**
   - Assurez-vous que `grpc-protobuf.jar` est inclus à l'emplacement correct dans votre package d'application :
     - **Pour un fichier WAR :** Placez-le dans le répertoire `WEB-INF/lib`.
     - **Pour un fichier EAR :** Placez-le à la racine de l'EAR ou dans un répertoire de bibliothèque désigné (par exemple, `lib/`).
   - Reconstruisez et redéployez votre application pour confirmer que le JAR est maintenant trouvé par WebSphere Liberty.
   - Vérifiez le fichier `console.log` pour voir si l'avertissement disparaît.

3. **Mettez à jour le manifeste (si le JAR n'est pas nécessaire) :**
   - Ouvrez le fichier `MANIFEST.MF` dans votre EAR ou WAR, situé dans le répertoire `META-INF/`.
   - Recherchez l'attribut `Class-Path`, qui pourrait ressembler à ceci :
     ```
     Class-Path: grpc-protobuf.jar some-other-lib.jar
     ```
   - Supprimez la référence à `grpc-protobuf.jar` pour qu'elle n'apparaisse plus dans la liste.
   - Enregistrez le fichier, reconstruisez votre application et redéployez-la. L'avertissement ne devrait plus apparaître.

4. **Vérifiez la configuration du classpath :**
   - Si votre application utilise des bibliothèques partagées ou des chargeurs de classes personnalisés dans WebSphere Liberty, vérifiez que la configuration du serveur (par exemple, `server.xml`) inclut les JAR nécessaires ou ne fait pas référence incorrectement à `grpc-protobuf.jar`.
   - Ajustez la configuration si nécessaire et redémarrez le serveur.

---

### Conseils généraux

- **Enquêtez sur les avertissements :** Même si l'application semble fonctionner correctement, il est bon de comprendre la cause des avertissements pour éviter les surprises ultérieures.
- **Testez après les modifications :** Après avoir ajouté le JAR ou mis à jour le manifeste, testez votre application en profondeur pour vous assurer qu'elle se comporte comme prévu.
- **Maintenez les journaux propres :** Résoudre les avertissements inutiles garde vos journaux clairs, facilitant ainsi la détection des problèmes réels à l'avenir.

En suivant ces étapes, vous pouvez déterminer si l'avertissement `grpc-protobuf.jar` est critique, traiter tout impact potentiel sur le temps d'exécution et supprimer l'avertissement de votre fichier `console.log` dans WebSphere Liberty.

---

Lorsque vous exécutez `mvn package` pour construire un fichier EAR et que vous rencontrez des avertissements concernant des JAR manquants (comme `grpc-protobuf.jar`) dans le chemin de classe du manifeste, il est peu probable que le problème provienne d'arguments de ligne de commande manquants. La commande `mvn package` elle-même est suffisante pour déclencher le cycle de vie de construction de Maven jusqu'à la phase `package`, qui inclut la compilation, les tests et l'emballage de votre EAR. Cependant, l'avertissement suggère un problème de configuration dans votre projet Maven plutôt qu'un problème avec la commande ou ses arguments. Explorons cela étape par étape.

---

### Que signifie l'avertissement ?

L'avertissement indique que le fichier `MANIFEST.MF` dans votre EAR fait référence à `grpc-protobuf.jar` dans son attribut `Class-Path`, mais ce JAR n'est pas trouvé à l'emplacement attendu dans l'EAR (par exemple, le répertoire `lib/`). L'attribut `Class-Path` liste les JAR dont votre application a besoin au moment de l'exécution, et un JAR manquant pourrait entraîner des erreurs d'exécution comme `ClassNotFoundException`.

---

### S'agit-il d'arguments manquants ?

Non, vous n'avez pas besoin d'arguments supplémentaires avec `mvn package` pour résoudre ce problème. Maven s'appuie sur les fichiers `pom.xml` de votre projet et les configurations des plugins (comme le `maven-ear-plugin`) pour déterminer ce qui est inclus dans l'EAR et comment le manifeste est généré. Ajouter des arguments comme `-DskipTests` ou `-U` pourrait modifier le processus de construction, mais ils n'aborderont pas directement cet avertissement. La cause profonde réside dans la configuration de votre projet, pas dans la commande elle-même.

---

### Causes courantes de l'avertissement

Voici les raisons probables de l'avertissement :

1. **Déclaration de dépendance manquante**
   Si `grpc-protobuf.jar` est requis par votre application, il pourrait ne pas être déclaré comme dépendance dans le `pom.xml` du module EAR ou de ses sous-modules (par exemple, un module WAR ou JAR).

2. **Portée de dépendance incorrecte**
   Si `grpc-protobuf.jar` est déclaré avec une portée comme `provided`, Maven suppose qu'il est fourni par l'environnement d'exécution (par exemple, WebSphere Liberty) et ne l'inclura pas dans l'EAR.

3. **Entrée de manifeste indésirable**
   Le `maven-ear-plugin` pourrait être configuré pour ajouter `grpc-protobuf.jar` au `Class-Path` dans le manifeste, même s'il n'est pas inclus dans l'EAR.

4. **Problème de dépendance transitive**
   Le JAR pourrait être une dépendance transitive (une dépendance d'une autre dépendance) qui est soit exclue, soit pas correctement incluse dans l'EAR.

---

### Comment enquêter

Pour identifier le problème, essayez ces étapes :

1. **Vérifiez le fichier manifeste**
   Après avoir exécuté `mvn package`, décompressez l'EAR généré et consultez `META-INF/MANIFEST.MF`. Vérifiez si `grpc-protobuf.jar` est listé dans le `Class-Path`. Cela confirme si l'avertissement correspond au contenu du manifeste.

2. **Passez en revue le `pom.xml` de l'EAR**
   Consultez la configuration du `maven-ear-plugin`. Par exemple :
   ```xml
   <plugin>
       <groupId>org.apache.maven.plugins</groupId>
       <artifactId>maven-ear-plugin</artifactId>
       <version>3.2.0</version>
       <configuration>
           <version>7</version> <!-- Correspond à votre version Java EE -->
           <defaultLibBundleDir>lib</defaultLibBundleDir>
       </configuration>
   </plugin>
   ```
   Assurez-vous qu'il est configuré pour inclure les dépendances dans le répertoire `lib/` (ou là où vos JARs doivent aller).

3. **Inspectez les dépendances**
   Exécutez `mvn dependency:tree` sur votre module EAR pour voir si `grpc-protobuf.jar` apparaît. S'il est manquant, il n'est déclaré nulle part dans votre arbre de dépendances.

4. **Consultez les sous-modules**
   Si votre EAR inclut des WARs ou des JARs, vérifiez leurs fichiers `pom.xml` pour les dépendances sur `grpc-protobuf.jar`.

---

### Comment le réparer

Selon ce que vous trouvez, appliquez l'une de ces solutions :

1. **Si le JAR est nécessaire**
   Ajoutez `grpc-protobuf.jar` comme dépendance dans le `pom.xml` de votre EAR :
   ```xml
   <dependency>
       <groupId>io.grpc</groupId>
       <artifactId>grpc-protobuf</artifactId>
       <version>1.39.0</version> <!-- Utilisez la version correcte -->
   </dependency>
   ```
   Assurez-vous que le `maven-ear-plugin` l'inclut dans l'EAR (par exemple, dans le répertoire `lib/`).

2. **Si la portée est incorrecte**
   Si elle est déclarée comme `<scope>provided</scope>` mais doit être empaquetée, changez-la en `<scope>compile</scope>` (la portée par défaut).

3. **Si le JAR n'est pas nécessaire**
   Si `grpc-protobuf.jar` ne devrait pas être dans le manifeste, vérifiez les configurations de manifeste personnalisées dans le `maven-ear-plugin` :
   ```xml
   <configuration>
       <manifestFile>META-INF/MANIFEST.MF</manifestFile>
   </configuration>
   ```
   Supprimez toutes les entrées manuelles pour `grpc-protobuf.jar`, ou laissez Maven générer le manifeste automatiquement.

4. **Gérez les dépendances transitives**
   Si c'est une dépendance transitive que vous n'avez pas besoin, excluez-la :
   ```xml
   <dependency>
       <groupId>some.group</groupId>
       <artifactId>some-artifact</artifactId>
       <exclusions>
           <exclusion>
               <groupId>io.grpc</groupId>
               <artifactId>grpc-protobuf</artifactId>
           </exclusion>
       </exclusions>
   </dependency>
   ```

5. **Reconstruisez et vérifiez**
   Exécutez `mvn clean package` pour reconstruire l'EAR, puis vérifiez le fichier EAR de sortie pour vous assurer que l'avertissement a disparu et que la structure est correcte.

---

### Conclusion

La commande `mvn package` elle-même n'a pas besoin d'arguments supplémentaires pour résoudre cet avertissement. Au lieu de cela, le problème est probablement dû à une mauvaise configuration dans votre `pom.xml` ou le `maven-ear-plugin`. En vous assurant que `grpc-protobuf.jar` est soit correctement inclus (si nécessaire) soit supprimé du manifeste (si non nécessaire), vous pouvez éliminer l'avertissement. Commencez par inspecter votre manifeste et vos dépendances, puis ajustez votre configuration en conséquence. Cela devrait résoudre le problème sans changer votre commande de construction.