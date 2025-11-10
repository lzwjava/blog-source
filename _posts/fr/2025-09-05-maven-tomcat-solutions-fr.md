---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Solutions aux problèmes du plugin Maven Tomcat
translated: true
type: note
---

Vous avez trouvé l'indice clé directement dans vos propres logs :

> `[INFO] Skipping non-war project`

Rien ne s'est lancé parce que **le plugin tomcat7-maven-plugin ne fonctionne qu'avec les applications web packagées en WAR** avec la structure classique `src/main/webapp`. Votre projet est presque certainement packagé en JAR actuellement, donc le plugin se termine simplement après la construction.

Il y a un deuxième piège : vous utilisez **Tomcat 11** (APIs Jakarta `jakarta.*`), mais vos dépendances sont **Spring 5.2.x** (utilise `javax.*`). Cette incompatibilité signifie que même si Tomcat démarrait, un déploiement simple sur Tomcat 11 échouerait sans une migration. Utilisez Tomcat 9 (javax) pour Spring 5, ou mettez à jour l'application vers Spring 6/Jakarta pour Tomcat 10/11.

Voici des options propres parmi lesquelles choisir — choisissez-en une et cela fonctionnera :

### Option 1 — Garder Spring 5, exécuter localement avec le plugin Jetty (le plus rapide)

Pas besoin de WAR ; idéal pour du développement rapide.

1. Ajoutez le plugin :

   ```xml
   <plugin>
     <groupId>org.eclipse.jetty</groupId>
     <artifactId>jetty-maven-plugin</artifactId>
     <version>9.4.54.v20240208</version>
   </plugin>
   ```
2. Exécutez :

   ```bash
   mvn jetty:run -Djetty.port=8080
   ```

Ceci utilise `javax.*`, ce qui correspond à Spring 5.

### Option 2 — Garder Spring 5, construire un WAR, et utiliser le plugin Tomcat7

1. Dans `pom.xml`, définissez le packaging WAR :

   ```xml
   <packaging>war</packaging>
   ```
2. Assurez-vous que la structure webapp existe :

   ```
   src/main/webapp/
   src/main/webapp/WEB-INF/web.xml   # optionnel si vous avez un initializer Servlet 3
   ```
3. (Optionnel) Ajoutez la configuration du plugin :

   ```xml
   <plugin>
     <groupId>org.apache.tomcat.maven</groupId>
     <artifactId>tomcat7-maven-plugin</artifactId>
     <version>2.2</version>
     <configuration>
       <path>/</path>
       <port>8080</port>
     </configuration>
   </plugin>
   ```
4. Exécutez :

   ```bash
   mvn tomcat7:run            # pour une webapp déployée en mode exploré
   # ou
   mvn package && mvn tomcat7:run-war
   ```

### Option 3 — Garder Spring 5, déployer sur un Tomcat 9 autonome

Ceci correspond à `javax.*` sans changer le code.

```bash
brew install tomcat@9
/opt/homebrew/opt/tomcat@9/bin/catalina start
```

Construisez et déposez votre WAR dans `.../tomcat@9/libexec/webapps/`.

### Option 4 — Mettre à niveau l'application vers Spring 6/Jakarta, rester avec Tomcat 11

Si vous voulez un Tomcat moderne :

* Mettez à niveau vers Spring Framework 6.x / Spring Boot 3.x.
* Changez les imports de `javax.*` vers `jakarta.*`.
* Ensuite, Tomcat 10/11 convient.

---

#### Pourquoi `mvn tomcat7:run` a affiché un succès mais "rien ne s'est passé"

* Les phases Maven se sont terminées avec succès, mais le plugin a vu un **packaging non-WAR**, donc il **n'a pas démarré** un Tomcat embarqué. C'est exactement ce que signifie "Skipping non-war project".

---

Si vous me dites quelle option vous préférez, je vous donnerai le `pom.xml` exact et les fichiers minimaux pour cette configuration (y compris un petit contrôleur et comment l'atteindre à l'adresse `http://localhost:8080/hello`).