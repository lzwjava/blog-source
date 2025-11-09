---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Configuration des modules WAR et EAR Maven
translated: true
type: note
---

### Configuration de projet multi-module Maven pour WAR vers EAR

Dans Maven, pour qu'un module produise un WAR (par exemple, une application web) et qu'un autre module l'assemble dans un EAR (Enterprise Archive), utilisez une structure de projet multi-module. Le module EAR dépend du module WAR via le `maven-ear-plugin`. Cela garantit que le WAR est inclus dans l'EAR lors de la construction.

#### Étape 1 : Créer le POM parent
Le POM parent définit les modules et gère les configurations partagées. Définissez son packaging sur `pom`.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>parent</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <modules>
        <module>web-module</module>  <!-- Construire celui-ci en premier -->
        <module>ear-module</module>
    </modules>

    <!-- Optionnel : Dépendances partagées et versions de plugins -->
    <dependencyManagement>
        <dependencies>
            <!-- Définir les versions pour les modules enfants ici -->
        </dependencies>
    </dependencyManagement>

    <build>
        <pluginManagement>
            <plugins>
                <!-- Gérer les versions des plugins -->
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-ear-plugin</artifactId>
                    <version>3.3.0</version>
                </plugin>
            </plugins>
        </pluginManagement>
    </build>
</project>
```

#### Étape 2 : Configurer le module WAR
Ce module construit l'application web en tant que WAR. Définissez son packaging sur `war`. Aucune configuration EAR spéciale n'est nécessaire ici—il a juste besoin d'être construit en premier.

Structure de répertoire : `web-module/pom.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.example</groupId>
        <artifactId>parent</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>web-module</artifactId>
    <packaging>war</packaging>

    <dependencies>
        <!-- Ajoutez vos dépendances web, par exemple servlet-api -->
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>4.0.1</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>3.3.2</version>
            </plugin>
        </plugins>
    </build>
</project>
```

#### Étape 3 : Configurer le module EAR
Ce module assemble l'EAR. Définissez son packaging sur `ear` et utilisez le `maven-ear-plugin` pour référencer le module WAR. Le plugin récupérera l'artefact WAR et l'inclura dans l'EAR.

Structure de répertoire : `ear-module/pom.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.example</groupId>
        <artifactId>parent</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>ear-module</artifactId>
    <packaging>ear</packaging>

    <dependencies>
        <!-- Dépendre du module WAR pour l'inclure dans la construction -->
        <dependency>
            <groupId>com.example</groupId>
            <artifactId>web-module</artifactId>
            <version>${project.version}</version>
            <type>war</type>
        </dependency>
        <!-- Optionnel : Ajouter des modules EJB ou autres si nécessaire -->
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-ear-plugin</artifactId>
                <version>3.3.0</version>
                <configuration>
                    <!-- Version EAR (par exemple, pour Java EE) -->
                    <version>8</version>
                    
                    <!-- Répertoire pour les bibliothèques dans l'EAR -->
                    <defaultLibBundleDir>lib</defaultLibBundleDir>
                    
                    <!-- WARs légers (exclure les dépendances déjà dans les libs de l'EAR) -->
                    <skinnyWars>true</skinnyWars>
                    
                    <!-- Définir les modules à inclure -->
                    <modules>
                        <webModule>
                            <groupId>com.example</groupId>
                            <artifactId>web-module</artifactId>
                            <bundleDir>/</bundleDir>  <!-- Racine de l'EAR -->
                            <contextRoot>/mywebapp</contextRoot>  <!-- Contexte de déploiement -->
                        </webModule>
                        <!-- Ajouter plus de <ejbModule> ou <jarModule> si nécessaire -->
                    </modules>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

#### Étape 4 : Construire le projet
- Exécutez depuis le **répertoire parent** : `mvn clean install`
  - Cela construit les modules dans l'ordre (WAR d'abord, puis EAR).
- L'EAR sera dans `ear-module/target/ear-module-1.0-SNAPSHOT.ear`.
- Pour construire seulement l'EAR (en supposant que le WAR est déjà construit) : `cd ear-module && mvn clean package`.

#### Notes importantes
- **Ordre de construction** : Listez le module WAR avant l'EAR dans les `<modules>` du parent pour garantir que Maven construise le WAR en premier.
- **Dépendances** : La `<dependency>` du module EAR sur le WAR garantit qu'il est résolu pendant le packaging.
- **Personnalisation** : Ajustez le `<contextRoot>` pour le chemin URL de l'application web. Ajoutez plus de modules (par exemple, des JAR EJB) dans `<modules>`.
- **Dépannage** : Si le WAR n'est pas inclus, vérifiez que les coordonnées de l'artefact correspondent exactement. Utilisez `mvn dependency:tree` dans le module EAR pour vérifier.

Pour plus de détails, consultez la documentation officielle du plugin Maven EAR.

[Apache Maven EAR Plugin](https://maven.apache.org/plugins/maven-ear-plugin/)  
[Maven Multi-Module Projects](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html#Multi-module_Projects)