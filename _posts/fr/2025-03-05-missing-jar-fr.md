---
audio: false
generated: true
lang: fr
layout: post
title: Fichiers JAR manquants dans WebSphere Liberty
translated: true
type: note
---

Dans WebSphere Liberty, vous avez remarqué des avertissements dans le fichier `console.log` qui ressemblent à ceci : *"the manifest class path: grpc-protobuf.jar cannot be found in jar file ..ear/war or its parent"*. Ces avertissements indiquent que le serveur ne peut pas localiser le fichier `grpc-protobuf.jar`, qui est référencé dans le chemin de classe (class path) du manifeste d'un fichier EAR ou WAR de votre application. Ci-dessous, je répondrai à vos questions : est-ce que ces avertissements sont importants, est-ce qu'ils auront un impact sur l'exécution de votre application, et comment les supprimer.

---

### Ces avertissements sont-ils importants ?

Oui et non — cela dépend si le JAR manquant est requis par votre application :

- **Si le JAR est nécessaire :**  
  Si `grpc-protobuf.jar` contient des classes ou des ressources dont votre application a besoin au moment de l'exécution, cet avertissement est significatif. Sans ce JAR, votre application pourrait rencontrer des erreurs d'exécution comme `ClassNotFoundException`, ce qui pourrait entraîner l'échec ou un comportement incorrect de certaines de ses parties.

- **Si le JAR n'est pas nécessaire :**  
  Si le JAR n'est pas réellement requis — peut-être s'agit-il d'une référence résiduelle d'une ancienne configuration ou d'une dépendance optionnelle — l'avertissement est inoffensif et n'affectera pas la fonctionnalité de votre application. Cependant, il encombrera toujours vos journaux.

En résumé, ces avertissements sont importants si le JAR manquant est critique pour votre application. Vous devrez enquêter pour déterminer son importance.

---

### Est-ce que cela impactera l'exécution de l'application ?

L'impact sur l'exécution de votre application dépend du rôle du JAR manquant :

- **Oui, si le JAR est requis :**  
  Si votre application tente d'utiliser des classes ou des ressources de `grpc-protobuf.jar` et qu'il est manquant, vous verrez probablement des erreurs d'exécution. Cela pourrait empêcher votre application de fonctionner correctement ou la faire échouer complètement.

- **Non, si le JAR est inutile :**  
  Si le JAR n'est pas nécessaire, votre application fonctionnera bien malgré l'avertissement. Le message restera simplement dans les journaux comme une nuisance.

Pour confirmer, vérifiez le comportement de votre application et les journaux pour des erreurs au-delà de l'avertissement lui-même. Si tout fonctionne comme prévu, le JAR n'est peut-être pas essentiel.

---

### Comment supprimer l'avertissement ?

Pour éliminer l'avertissement, vous devez soit vous assurer que le JAR est correctement inclus dans votre application, soit supprimer la référence inutile à celui-ci. Voici une approche étape par étape :

1. **Vérifiez si le JAR est nécessaire :**  
   - Consultez la documentation, le code source ou la liste des dépendances de votre application (par exemple, `pom.xml` si vous utilisez Maven) pour déterminer si `grpc-protobuf.jar` est requis.  
   - S'il n'est pas nécessaire, passez à l'étape 3 pour supprimer la référence. S'il est nécessaire, poursuivez à l'étape 2.

2. **Corrigez le packaging (si le JAR est nécessaire) :**  
   - Assurez-vous que `grpc-protobuf.jar` est inclus à l'emplacement correct dans votre package d'application :  
     - **Pour un fichier WAR :** Placez-le dans le répertoire `WEB-INF/lib`.  
     - **Pour un fichier EAR :** Placez-le à la racine de l'EAR ou dans un répertoire de bibliothèque désigné (par exemple, `lib/`).  
   - Recompilez et redéployez votre application pour confirmer que le JAR est maintenant trouvé par WebSphere Liberty.  
   - Vérifiez le `console.log` pour voir si l'avertissement disparaît.

3. **Mettez à jour le manifeste (si le JAR n'est pas nécessaire) :**  
   - Ouvrez le fichier `MANIFEST.MF` dans votre EAR ou WAR, situé dans le répertoire `META-INF/`.  
   - Recherchez l'attribut `Class-Path`, qui pourrait ressembler à ceci :  
     ```
     Class-Path: grpc-protobuf.jar some-other-lib.jar
     ```  
   - Supprimez la référence à `grpc-protobuf.jar` afin qu'elle n'apparaisse plus dans la liste.  
   - Enregistrez le fichier, recompilez votre application et redéployez-la. L'avertissement ne devrait plus apparaître.

4. **Vérifiez la configuration du classpath :**  
   - Si votre application utilise des bibliothèques partagées ou des chargeurs de classes personnalisés dans WebSphere Liberty, vérifiez que la configuration du serveur (par exemple, `server.xml`) inclut les JARs nécessaires ou ne référence pas incorrectement `grpc-protobuf.jar`.  
   - Ajustez la configuration si nécessaire et redémarrez le serveur.

---

### Conseils généraux

- **Étudiez les avertissements :** Même si l'application semble fonctionner correctement, il est bon de comprendre la cause des avertissements pour éviter des surprises plus tard.  
- **Testez après les modifications :** Après avoir ajouté le JAR ou mis à jour le manifeste, testez votre application minutieusement pour vous assurer qu'elle se comporte comme prévu.  
- **Maintenez les journaux propres :** Résoudre les avertissements inutiles garde vos journaux clairs, ce qui facilite la détection des vrais problèmes à l'avenir.

En suivant ces étapes, vous pouvez déterminer si l'avertissement concernant `grpc-protobuf.jar` est critique, traiter tout impact potentiel sur l'exécution et supprimer l'avertissement de votre `console.log` dans WebSphere Liberty.

---

Lorsque vous exécutez `mvn package` pour construire un fichier EAR et que vous rencontrez des avertissements concernant des JARs manquants (comme `grpc-protobuf.jar`) dans le chemin de classe du manifeste, il est peu probable que le problème provienne d'arguments de ligne de commande manquants. La commande `mvn package` elle-même est suffisante pour déclencher le cycle de vie de construction Maven jusqu'à la phase `package`, qui inclut la compilation, les tests et le packaging de votre EAR. Cependant, l'avertissement suggère un problème de configuration dans votre projet Maven plutôt qu'un problème avec la commande ou ses arguments. Examinons cela étape par étape.

---

### Que signifie l'avertissement ?

L'avertissement indique que le fichier `MANIFEST.MF` dans votre EAR référence `grpc-protobuf.jar` dans son attribut `Class-Path`, mais ce JAR n'est pas trouvé à l'emplacement attendu dans l'EAR (par exemple, le répertoire `lib/`). L'attribut `Class-Path` liste les JARs dont votre application a besoin au moment de l'exécution, et un JAR manquant pourrait entraîner des erreurs d'exécution comme `ClassNotFoundException`.

---

### S'agit-il d'arguments manquants ?

Non, vous n'avez pas besoin d'arguments supplémentaires avec `mvn package` pour résoudre ceci. Maven s'appuie sur les fichiers `pom.xml` de votre projet et les configurations de plugins (comme `maven-ear-plugin`) pour déterminer ce qui est inclus dans l'EAR et comment le manifeste est généré. Ajouter des arguments comme `-DskipTests` ou `-U` peut modifier le processus de construction, mais ils ne résoudront pas directement cet avertissement. La cause racine se trouve dans la configuration de votre projet, pas dans la commande elle-même.

---

### Causes courantes de l'avertissement

Voici les raisons probables de l'avertissement :

1. **Déclaration de dépendance manquante**  
   Si `grpc-protobuf.jar` est requis par votre application, il se peut qu'il ne soit pas déclaré comme dépendance dans le `pom.xml` de votre module EAR ou de ses sous-modules (par exemple, un module WAR ou JAR).

2. **Portée de dépendance incorrecte**  
   Si `grpc-protobuf.jar` est déclaré avec une portée comme `provided`, Maven suppose qu'il est fourni par l'environnement d'exécution (par exemple, WebSphere Liberty) et ne l'inclura pas dans l'EAR.

3. **Entrée de manifeste non souhaitée**  
   Le `maven-ear-plugin` pourrait être configuré pour ajouter `grpc-protobuf.jar` au `Class-Path` dans le manifeste, même s'il n'est pas inclus dans l'EAR.

4. **Problème de dépendance transitive**  
   Le JAR pourrait être une dépendance transitive (une dépendance d'une autre dépendance) qui est soit exclue, soit non correctement incluse dans l'EAR.

---

### Comment enquêter

Pour identifier le problème, essayez ces étapes :

1. **Vérifiez le fichier manifeste**  
   Après avoir exécuté `mvn package`, décompressez l'EAR généré et regardez `META-INF/MANIFEST.MF`. Vérifiez si `grpc-protobuf.jar` est listé dans le `Class-Path`. Cela confirme si l'avertissement correspond au contenu du manifeste.

2. **Revoyez le `pom.xml` de l'EAR**  
   Regardez la configuration du `maven-ear-plugin`. Par exemple :
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
   Assurez-vous qu'il est configuré pour inclure les dépendances dans le répertoire `lib/` (ou là où vos JARs devraient se trouver).

3. **Inspectez les dépendances**  
   Exécutez `mvn dependency:tree` sur votre module EAR pour voir si `grpc-protobuf.jar` apparaît. S'il est manquant, il n'est déclaré nulle part dans votre arborescence de dépendances.

4. **Examinez les sous-modules**  
   Si votre EAR inclut des WARs ou des JARs, vérifiez leurs fichiers `pom.xml` pour des dépendances sur `grpc-protobuf.jar`.

---

### Comment le corriger

En fonction de ce que vous trouvez, appliquez l'une de ces solutions :

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
   S'il est déclaré comme `<scope>provided</scope>` mais doit être packagé, changez-le pour `<scope>compile</scope>` (la portée par défaut).

3. **Si le JAR n'est pas nécessaire**  
   Si `grpc-protobuf.jar` ne devrait pas être dans le manifeste, vérifiez les configurations de manifeste personnalisées dans le `maven-ear-plugin` :
   ```xml
   <configuration>
       <manifestFile>META-INF/MANIFEST.MF</manifestFile>
   </configuration>
   ```
   Supprimez toute entrée manuelle pour `grpc-protobuf.jar`, ou laissez Maven générer le manifeste automatiquement.

4. **Gérez les dépendances transitives**  
   S'il s'agit d'une dépendance transitive dont vous n'avez pas besoin, excluez-la :
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

5. **Recompilez et vérifiez**  
   Exécutez `mvn clean package` pour reconstruire l'EAR, puis vérifiez le fichier EAR généré pour vous assurer que l'avertissement a disparu et que la structure est correcte.

---

### Conclusion

La commande `mvn package` elle-même ne nécessite pas d'arguments supplémentaires pour corriger cet avertissement. Au lieu de cela, le problème est probablement dû à une mauvaise configuration dans votre `pom.xml` ou le `maven-ear-plugin`. En vous assurant que `grpc-protobuf.jar` est soit correctement inclus (si nécessaire), soit supprimé du manifeste (s'il n'est pas nécessaire), vous pouvez éliminer l'avertissement. Commencez par inspecter votre manifeste et vos dépendances, puis ajustez votre configuration en conséquence. Cela devrait résoudre le problème sans changer votre commande de construction.