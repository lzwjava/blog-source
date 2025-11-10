---
audio: false
generated: true
lang: fr
layout: post
title: Outils de Développement Spring Boot pour le Redémarrage Automatique
translated: true
type: note
---

Lorsque vous exécutez une application Spring Boot avec `mvn spring-boot:run`, les surveillances de fichiers et les capacités de redémarrage automatique ou de rechargement à chaud ne sont pas activées par défaut. Cependant, vous pouvez les activer en ajoutant la dépendance `spring-boot-devtools` à votre projet. Ce module fournit des fonctionnalités comme les redémarrages automatiques et LiveReload pour un développement plus rapide.

### Détails
1. **Comportement par défaut sans DevTools** :
   - Exécuter `mvn spring-boot:run` sans `spring-boot-devtools` n'inclut pas les surveillances de fichiers ou le redémarrage automatique. Vous devez arrêter et redémarrer manuellement l'application pour appliquer les modifications aux classes Java, aux ressources statiques ou aux templates.
   - Les ressources statiques (par exemple, HTML, CSS, JS) peuvent nécessiter une reconstruction complète ou un redémarrage, sauf configuration contraire.

2. **Avec `spring-boot-devtools`** :
   - **Surveillances de fichiers** : DevTools surveille le classpath pour détecter les changements dans les fichiers Java, les propriétés et certaines ressources (par exemple, `/resources`, `/static`, `/templates`).
   - **Redémarrage automatique** : Lorsqu'un fichier sur le classpath change (par exemple, une classe Java ou un fichier de propriétés), DevTools déclenche un redémarrage automatique de l'application. Celui-ci est plus rapide qu'un démarrage à froid car il utilise deux chargeurs de classe : un pour les bibliothèques tierces inchangées (chargeur de classe de base) et un autre pour le code de votre application (chargeur de classe de redémarrage).[](https://docs.spring.io/spring-boot/reference/using/devtools.html)[](https://docs.spring.io/spring-boot/docs/1.5.16.RELEASE/reference/html/using-boot-devtools.html)
   - **LiveReload** : Les modifications apportées aux ressources statiques (par exemple, HTML, CSS, JS dans `/static`, `/public` ou `/templates`) ou aux templates (par exemple, Thymeleaf) déclenchent un rafraîchissement du navigateur au lieu d'un redémarrage complet, à condition que vous ayez une extension de navigateur LiveReload installée (prise en charge pour Chrome, Firefox, Safari).[](https://www.concretepage.com/spring-boot/spring-boot-automatic-restart-using-developer-tools-with-maven)[](https://www.codejava.net/frameworks/spring-boot/spring-boot-auto-reload-changes-using-livereload-and-devtools)
   - **Exclusions** : Par défaut, les ressources dans `/META-INF/maven`, `/META-INF/resources`, `/resources`, `/static`, `/public` et `/templates` ne déclenchent pas de redémarrage mais déclenchent un LiveReload. Vous pouvez personnaliser cela avec `spring.devtools.restart.exclude`.[](https://docs.spring.io/spring-boot/reference/using/devtools.html)

3. **Configuration pour DevTools** :
   Ajoutez la dépendance suivante à votre `pom.xml` :
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-devtools</artifactId>
       <scope>runtime</scope>
       <optional>true</optional>
   </dependency>
   ```
   - Le `<optional>true</optional>` garantit que DevTools n'est pas inclus dans les builds de production.[](https://www.concretepage.com/spring-boot/spring-boot-automatic-restart-using-developer-tools-with-maven)
   - Exécutez l'application avec `mvn spring-boot:run`. DevTools activera automatiquement la surveillance des fichiers et le redémarrage automatique.

4. **Comportement dans les IDE** :
   - **Eclipse** : Sauvegarder les modifications (Ctrl+S) déclenche automatiquement une build, que DevTools détecte et redémarre l'application.[](https://docs.spring.io/spring-boot/docs/1.5.7.RELEASE/reference/html/howto-hotswapping.html)
   - **IntelliJ IDEA** : Vous devez déclencher manuellement une build (Ctrl+F9 ou "Make Project") pour que DevTools détecte les changements, sauf si vous configurez la construction automatique. Alternativement, activez "Build project automatically" dans les paramètres d'IntelliJ pour des redémarrages transparents.[](https://www.codejava.net/frameworks/spring-boot/spring-boot-auto-restart-and-live-reload-in-intellij-idea)
   - Pour LiveReload, installez l'extension de navigateur depuis http://livereload.com/extensions/ et activez-la.[](https://www.codejava.net/frameworks/spring-boot/spring-boot-auto-reload-changes-using-livereload-and-devtools)

5. **Alternative : Spring Loaded** :
   - Au lieu de DevTools, vous pouvez utiliser Spring Loaded pour un échange à chaud plus avancé (par exemple, changements de signature de méthode). Ajoutez-le au `spring-boot-maven-plugin` :
     ```xml
     <plugin>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-maven-plugin</artifactId>
         <dependencies>
             <dependency>
                 <groupId>org.springframework</groupId>
                 <artifactId>springloaded</artifactId>
                 <version>1.2.8.RELEASE</version>
             </dependency>
         </dependencies>
     </plugin>
     ```
   - Spring Loaded est moins recommandé que DevTools, car il n'est pas aussi activement maintenu et pourrait ne pas prendre en charge tous les frameworks.[](https://docs.spring.io/spring-boot/docs/1.5.7.RELEASE/reference/html/howto-hotswapping.html)[](https://docs.spring.io/spring-boot/docs/1.5.16.RELEASE/reference/html/howto-hotswapping.html)

6. **Rechargement à chaud des ressources statiques** :
   - Sans DevTools, vous pouvez activer le rechargement à chaud des ressources statiques en définissant la propriété `addResources` du `spring-boot-maven-plugin` :
     ```xml
     <plugin>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-maven-plugin</artifactId>
         <configuration>
             <addResources>true</addResources>
         </configuration>
     </plugin>
     ```
   - Cela ajoute `src/main/resources` au classpath, permettant l'édition sur place des fichiers statiques, mais c'est moins complet que DevTools.[](https://docs.spring.io/spring-boot/maven-plugin/run.html)

7. **Mises en garde** :
   - DevTools peut causer des problèmes de chargement de classe dans les projets multi-modules. Si cela se produit, essayez de désactiver le redémarrage avec `spring.devtools.restart.enabled=false` ou utilisez JRebel pour un rechargement avancé.[](https://docs.spring.io/spring-boot/reference/using/devtools.html)
   - Pour les fichiers hors classpath, utilisez `spring.devtools.restart.additional-paths` pour surveiller des répertoires supplémentaires.[](https://docs.spring.io/spring-boot/docs/1.5.16.RELEASE/reference/html/using-boot-devtools.html)
   - LiveReload nécessite une extension de navigateur et peut ne pas fonctionner pour toutes les configurations front-end (par exemple, React avec Webpack).[](https://stackoverflow.com/questions/49888724/hot-reload-for-spring-boot-backend-frontend)
   - Si les redémarrages sont lents, ajustez `spring.devtools.restart.poll-interval` et `spring.devtools.restart.quiet-period` pour optimiser la surveillance des fichiers.[](https://docs.spring.io/spring-boot/reference/using/devtools.html)

### Étapes pour une application simple
1. Créez une application Spring Boot basique (par exemple, en utilisant Spring Initializr avec `spring-boot-starter-web`).
2. Ajoutez la dépendance `spring-boot-devtools` au `pom.xml`.
3. Exécutez `mvn spring-boot:run`.
4. Modifiez un fichier Java, un fichier de propriétés ou une ressource statique (par exemple, HTML dans `src/main/resources/static`).
5. Observez le redémarrage automatique (pour Java/propriétés) ou le rafraîchissement du navigateur (pour les ressources statiques avec LiveReload activé).

### Exemple
Pour une application simple avec un contrôleur REST :
```java
@RestController
public class HelloController {
    @GetMapping("/hello")
    public String hello() {
        return "Hello, World!";
    }
}
```
- Ajoutez DevTools, exécutez `mvn spring-boot:run`, et changez la valeur de retour de la méthode `hello()`. L'application redémarrera automatiquement.
- Ajoutez un `index.html` dans `src/main/resources/static`, installez l'extension LiveReload, et modifiez le HTML. Le navigateur se rafraîchira sans redémarrage.

### Conclusion
Pour une application Spring Boot simple, l'ajout de `spring-boot-devtools` est le moyen le plus simple d'activer les surveillances de fichiers, le redémarrage automatique et le rechargement à chaud. Utilisez `mvn spring-boot:run` avec DevTools pour une expérience de développement transparente. Si vous avez besoin d'un échange à chaud plus avancé, envisagez Spring Loaded ou JRebel, mais DevTools est suffisant pour la plupart des cas.[](https://www.geeksforgeeks.org/hot-reload-with-spring-boot-devtools/)[](https://docs.spring.io/spring-boot/how-to/hotswapping.html)

---

Voici un exemple de configuration de `spring-boot-devtools` pour la surveillance de fichiers, le redémarrage automatique et le rechargement à chaud dans votre application Spring Boot en utilisant un fichier `application.yml`. Cette configuration est adaptée à votre projet `blog-server`, basée sur les logs que vous avez fournis, qui montrent que DevTools est actif et surveille `target/classes`.

### Configuration `application.yml`
```yaml
spring:
  devtools:
    restart:
      # Activer le redémarrage automatique (par défaut : true)
      enabled: true
      # Répertoires supplémentaires à surveiller pour les redémarrages (ex. : dossier config personnalisé)
      additional-paths:
        - /home/lzw/Projects/blog-server/config
      # Fichiers/répertoires à exclure du déclenchement des redémarrages (exclusions par défaut conservées)
      exclude: static/**,public/**,templates/**,logs/**,generated/**
      # Intervalle de vérification des changements de fichiers (en millisecondes, défaut : 1000)
      poll-interval: 1000
      # Période d'inactivité après les changements de fichiers avant redémarrage (en millisecondes, défaut : 400)
      quiet-period: 400
      # Optionnel : Fichier pour déclencher manuellement les redémarrages
      trigger-file: .restart
    livereload:
      # Activer LiveReload pour le rafraîchissement du navigateur sur les changements de ressources statiques (défaut : true)
      enabled: true
```

### Explication des paramètres
- **`spring.devtools.restart.enabled`** : Active le redémarrage automatique lorsque les fichiers du classpath changent (par exemple, `target/classes`, comme vu dans votre log : `file:/home/lzw/Projects/blog-server/target/classes/`).
- **`spring.devtools.restart.additional-paths`** : Surveille des répertoires supplémentaires (par exemple, `/home/lzw/Projects/blog-server/config`) pour les changements déclenchant des redémarrages.
- **`spring.devtools.restart.exclude`** : Empêche les redémarrages pour les changements dans les répertoires `static/`, `public/`, `templates/`, `logs/` ou `generated/`, tout en permettant LiveReload pour les ressources statiques (par exemple, HTML, CSS, JS).
- **`spring.devtools.restart.poll-interval`** : Définit la fréquence à laquelle DevTools vérifie les changements de fichiers (1000ms = 1 seconde).
- **`spring.devtools.restart.quiet-period`** : Attend 400ms après la détection d'un changement pour s'assurer qu'aucun autre changement n'est en attente avant de redémarrer.
- **`spring.devtools.restart.trigger-file`** : Permet les redémarrages manuels en mettant à jour `.restart` (par exemple, `touch /home/lzw/Projects/blog-server/.restart`).
- **`spring.devtools.livereload.enabled`** : Active le serveur LiveReload, qui déclenche les rafraîchissements du navigateur pour les changements dans `static/` ou `templates/` (nécessite une extension de navigateur LiveReload).

### Étapes à appliquer
1. Créez ou mettez à jour `src/main/resources/application.yml` avec la configuration ci-dessus.
2. Assurez-vous que `spring-boot-devtools` est dans votre `pom.xml` :
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-devtools</artifactId>
       <scope>runtime</scope>
       <optional>true</optional>
   </dependency>
   ```
3. Exécutez `mvn spring-boot:run`. DevTools surveillera `target/classes` et `/home/lzw/Projects/blog-server/config` (s'il est ajouté), en redémarrant l'application lors de changements de fichiers Java ou de propriétés et en rafraîchissant le navigateur lors de changements de ressources statiques.
4. Pour LiveReload, installez une extension de navigateur (par exemple, depuis http://livereload.com/extensions/) ou intégrez un client LiveReload dans votre front-end.

### Notes
- Vos logs montrent un démarrage rapide (0,8 seconde), donc l'`poll-interval` et le `quiet-period` par défaut devraient convenir. Ajustez-les (par exemple, `poll-interval: 500`) si les redémarrages semblent lents dans un projet plus volumineux.
- Si vous n'avez pas besoin de LiveReload (par exemple, en utilisant un serveur de développement front-end séparé), définissez `livereload.enabled: false`.
- Pour les redémarrages manuels, créez `.restart` à la racine de votre projet et mettez-le à jour si nécessaire.

Cette configuration YAML devrait fonctionner parfaitement avec votre configuration, en améliorant les fonctionnalités de surveillance de fichiers et de redémarrage automatique que vous voyez déjà.