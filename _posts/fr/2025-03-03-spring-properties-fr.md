---
audio: false
generated: true
lang: fr
layout: post
title: Sélection de fichiers de propriété dans Spring Boot
translated: true
---

Dans un projet Spring Boot Maven, vous avez deux fichiers de propriétés, `appProperties.properties` et `appProperties-hk.properties`, situés sous `src/main/resources`. Pour contrôler quel fichier de propriétés est utilisé, en particulier pour spécifier l'utilisation des propriétés `-hk`, vous pouvez utiliser les mécanismes de configuration de Spring Boot. Voici comment faire :

### Solution

1. **Créer un fichier `application.properties`**
   - Par défaut, Spring Boot recherche `application.properties` ou `application.yml` dans `src/main/resources` pour charger les paramètres de configuration.
   - Pour utiliser vos fichiers de propriétés personnalisés (`appProperties.properties` et `appProperties-hk.properties`), vous devez informer Spring Boot de rechercher des fichiers avec le nom de base `appProperties` au lieu du `application` par défaut.
   - Ajoutez la ligne suivante à un nouveau fichier `application.properties` dans `src/main/resources` :

     ```properties
     spring.config.name=appProperties
     ```

   - Ce paramètre indique à Spring Boot de charger `appProperties.properties` comme fichier de configuration de base, et il recherchera également automatiquement des variantes spécifiques aux profils comme `appProperties-{profile}.properties` lorsqu'un profil est actif.

2. **Utiliser les profils Spring pour spécifier les propriétés `-hk`**
   - Spring Boot prend en charge les profils, qui permettent de charger des fichiers de propriétés supplémentaires ou de substitution en fonction du profil actif.
   - Puisque votre fichier est nommé `appProperties-hk.properties`, il suit le modèle `appProperties-{profile}.properties`. Ici, "hk" peut être traité comme un nom de profil.
   - Pour utiliser `appProperties-hk.properties`, activez le profil "hk" lors de l'exécution de votre application. Spring Boot chargera alors à la fois `appProperties.properties` et `appProperties-hk.properties`, les propriétés dans `appProperties-hk.properties` remplaçant toute propriété correspondante dans `appProperties.properties`.

3. **Comment activer le profil "hk"**
   - **Via la ligne de commande** : Lors de l'exécution de votre application Spring Boot, spécifiez le profil actif en utilisant l'argument `--spring.profiles.active`. Par exemple :
     ```bash
     java -jar target/myapp.jar --spring.profiles.active=hk
     ```
     Remplacez `myapp.jar` par le nom du fichier JAR de votre application généré par Maven.

   - **Via Maven** : Si vous exécutez l'application en utilisant la cible `spring-boot:run`, configurez le profil dans votre `pom.xml` :
     ```xml
     <plugin>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-maven-plugin</artifactId>
         <configuration>
             <profiles>
                 <profile>hk</profile>
             </profiles>
         </configuration>
     </plugin>
     ```
     Ensuite, exécutez :
     ```bash
     mvn spring-boot:run
     ```

   - **Via la propriété système** : Définissez le profil comme argument JVM :
     ```bash
     java -Dspring.profiles.active=hk -jar target/myapp.jar
     ```

   - **Via la variable d'environnement** : Exportez le profil dans votre environnement (par exemple, dans un système de type Unix) :
     ```bash
     export SPRING_PROFILES_ACTIVE=hk
     java -jar target/myapp.jar
     ```

### Fonctionnement
- Avec `spring.config.name=appProperties` défini dans `application.properties`, Spring Boot utilise `appProperties` comme nom de base pour les fichiers de configuration.
- Lorsque aucun profil n'est actif, seul `appProperties.properties` est chargé.
- Lorsque le profil "hk" est activé (par exemple, via `--spring.profiles.active=hk`), Spring Boot charge à la fois `appProperties.properties` et `appProperties-hk.properties`. Les propriétés définies dans `appProperties-hk.properties` prennent le pas sur celles dans `appProperties.properties` s'il y a des doublons.

### Étapes finales
- Assurez-vous que `appProperties.properties` et `appProperties-hk.properties` sont dans `src/main/resources`.
- Ajoutez `application.properties` avec `spring.config.name=appProperties` à `src/main/resources`.
- Exécutez votre application avec le profil "hk" activé pour utiliser les propriétés `-hk`.

Cette approche est conforme aux conventions de Spring Boot, ce qui en fait une méthode typique et simple pour contrôler quel fichier de propriétés est utilisé dans votre projet. Pour utiliser spécifiquement les propriétés `-hk`, activez simplement le profil "hk" comme décrit ci-dessus.