---
audio: false
generated: true
lang: fr
layout: post
title: 'Plugin Maven Shade : Créer des Uber-JARs'
translated: true
type: note
---

Le `maven-shade-plugin` est un plugin Maven utilisé pour créer un "uber-JAR" (un fichier JAR unique et autonome) en combinant le code compilé d'un projet avec ses dépendances. Il est couramment utilisé dans les projets Java pour empaqueter une application et toutes ses bibliothèques requises dans un seul fichier JAR exécutable, simplifiant ainsi la distribution et le déploiement.

### Détails clés :
- **Group ID** : `org.apache.maven.plugins` (indique qu'il s'agit d'un plugin Apache Maven officiel).
- **Artifact ID** : `maven-shade-plugin` (le nom spécifique du plugin).
- **Objectif** :
  - **Shading** : Déplace (renomme) les packages des dépendances pour éviter les conflits de classes (par exemple, lorsque plusieurs bibliothèques utilisent différentes versions de la même classe).
  - **Empaquetage** : Regroupe les dépendances dans le JAR final, le rendant autonome.
  - **Transformation des ressources** : Peut modifier les ressources (par exemple, fusionner des fichiers de configuration comme `MANIFEST.MF`).
- **Cas d'utilisation courants** :
  - Créer des JAR exécutables pour les applications en ligne de commande.
  - Résoudre les conflits de classpath dans les projets avec de multiples dépendances.
  - Simplifier le déploiement pour des applications comme les jobs Spark ou Hadoop.
- **Fonctionnement** :
  - Configuré dans le fichier `pom.xml` sous la section `<plugins>`.
  - Pendant le processus de build (généralement lors de la phase `package`), il combine les classes et les ressources, déplace éventuellement les packages et produit le JAR final.
- **Exemple de configuration** dans `pom.xml` :
  ```xml
  <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-shade-plugin</artifactId>
      <version>3.5.0</version> <!-- Utiliser la dernière version -->
      <executions>
          <execution>
              <phase>package</phase>
              <goals>
                  <goal>shade</goal>
              </goals>
              <configuration>
                  <transformers>
                      <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                          <mainClass>com.example.Main</mainClass>
                      </transformer>
                  </transformers>
              </configuration>
          </execution>
      </executions>
  </plugin>
  ```
  Cet exemple spécifie la classe principale pour un JAR exécutable et exécute le plugin pendant la phase `package`.

- **Fonctionnalités principales** :
  - **Inclusion des dépendances** : Intègre les dépendances dans le JAR.
  - **Relocalisation des packages** : Renomme les packages pour éviter les conflits (par exemple, `com.google.common` en `shaded.com.google.common`).
  - **Filtrage des ressources** : Fusionne ou transforme les fichiers de ressources.
  - **JAR exécutable** : Ajoute des entrées au manifeste pour rendre le JAR exécutable avec `java -jar`.

### Quand l'utiliser :
- Lorsque vous avez besoin d'un JAR unique pour une distribution facile.
- Lorsque vous devez gérer des conflits de dépendances (par exemple, différentes versions d'une même bibliothèque).
- Pour déployer des applications dans des environnements où les dépendances externes sont difficiles à gérer.

Si vous avez une question spécifique concernant sa configuration ou son cas d'utilisation, n'hésitez pas à me le demander !