---
audio: false
generated: true
lang: fr
layout: post
title: Sélection du Fichier de Propriétés dans Spring Boot
translated: true
type: note
---

Dans un projet Maven Spring Boot, vous avez deux fichiers de propriétés, `appProperties.properties` et `appProperties-hk.properties`, situés dans `src/main/resources`. Pour contrôler quel fichier de propriétés est utilisé, en particulier pour spécifier l'utilisation des propriétés `-hk`, vous pouvez tirer parti des mécanismes de configuration de Spring Boot. Voici comment procéder :

### Solution

1. **Créer un fichier `application.properties`**
   - Par défaut, Spring Boot recherche `application.properties` ou `application.yml` dans `src/main/resources` pour charger les paramètres de configuration.
   - Pour utiliser vos fichiers de propriétés personnalisés (`appProperties.properties` et `appProperties-hk.properties`), vous devez indiquer à Spring Boot de rechercher des fichiers avec le nom de base `appProperties` au lieu du nom par défaut `application`.
   - Ajoutez la ligne suivante dans un nouveau fichier `application.properties` dans `src/main/resources` :

     ```properties
     spring.config.name=appProperties
     ```

   - Ce paramètre indique à Spring Boot de charger `appProperties.properties` comme fichier de configuration de base, et il recherchera automatiquement les variantes spécifiques au profil comme `appProperties-{profile}.properties` lorsqu'un profil est actif.

2. **Utiliser les profils Spring pour spécifier les propriétés `-hk`**
   - Spring Boot prend en charge les profils, qui vous permettent de charger des fichiers de propriétés supplémentaires ou de remplacement en fonction du profil actif.
   - Étant donné que votre fichier est nommé `appProperties-hk.properties`, il suit le modèle `appProperties-{profile}.properties`. Ici, "hk" peut être traité comme un nom de profil.
   - Pour utiliser `appProperties-hk.properties`, activez le profil "hk" lors de l'exécution de votre application. Spring Boot chargera alors à la fois `appProperties.properties` et `appProperties-hk.properties`, les propriétés dans `appProperties-hk.properties` écrasant toute propriété correspondante dans `appProperties.properties`.

3. **Comment activer le profil "hk"**
   - **Via la ligne de commande** : Lors de l'exécution de votre application Spring Boot, spécifiez le profil actif en utilisant l'argument `--spring.profiles.active`. Par exemple :
     ```bash
     java -jar target/myapp.jar --spring.profiles.active=hk
     ```
     Remplacez `myapp.jar` par le nom du fichier JAR de votre application généré par Maven.

   - **Via Maven** : Si vous exécutez l'application en utilisant le goal `spring-boot:run`, configurez le profil dans votre `pom.xml` :
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
     Puis exécutez :
     ```bash
     mvn spring-boot:run
     ```

   - **Via une propriété système** : Définissez le profil comme argument JVM :
     ```bash
     java -Dspring.profiles.active=hk -jar target/myapp.jar
     ```

   - **Via une variable d'environnement** : Exportez le profil dans votre environnement (par exemple, dans un système de type Unix) :
     ```bash
     export SPRING_PROFILES_ACTIVE=hk
     java -jar target/myapp.jar
     ```

### Comment cela fonctionne
- Avec `spring.config.name=appProperties` défini dans `application.properties`, Spring Boot utilise `appProperties` comme nom de base pour les fichiers de configuration.
- Lorsqu'aucun profil n'est actif, seul `appProperties.properties` est chargé.
- Lorsque le profil "hk" est activé (par exemple, via `--spring.profiles.active=hk`), Spring Boot charge à la fois `appProperties.properties` et `appProperties-hk.properties`. Les propriétés définies dans `appProperties-hk.properties` prennent le pas sur celles de `appProperties.properties` s'il y a des doublons.

### Étapes finales
- Assurez-vous que `appProperties.properties` et `appProperties-hk.properties` se trouvent dans `src/main/resources`.
- Ajoutez `application.properties` avec `spring.config.name=appProperties` dans `src/main/resources`.
- Exécutez votre application avec le profil "hk" activé pour utiliser les propriétés `-hk`.

Cette approche est conforme aux conventions de Spring Boot, ce qui en fait un moyen typique et simple de contrôler quel fichier de propriétés est utilisé dans votre projet. Pour utiliser spécifiquement les propriétés `-hk`, activez simplement le profil "hk" comme décrit ci-dessus.