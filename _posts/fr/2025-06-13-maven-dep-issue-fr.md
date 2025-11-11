---
audio: false
generated: true
lang: fr
layout: post
title: Problème de Dépendance Maven
translated: true
type: note
---

### Aperçu du problème

L'utilisateur rencontre un échec de build lors de l'exécution d'une application Spring Boot avec Maven. Le message d'erreur indique une `IllegalArgumentException` causée par `NoClassDefFoundError: org/springframework/beans/factory/aot/BeanRegistrationExcludeFilter`. Cela suggère un problème d'incompatibilité de version parmi les dépendances du projet, empêchant le démarrage correct de l'application. Le fichier `pom.xml` fourni et la sortie Maven nous donnent le contexte nécessaire pour diagnostiquer et résoudre le problème.

### Cause Racine

L'erreur se produit car l'application Spring Boot est incapable d'instancier `SharedMetadataReaderFactoryContextInitializer`, une classe impliquée dans le processus d'auto-configuration de Spring Boot. La cause sous-jacente est une classe manquante, `BeanRegistrationExcludeFilter`, qui fait partie de Spring Framework 6.0 et ultérieur. Le projet utilise Spring Boot 3.4.2, qui dépend de Spring Framework 6.1.14. Cependant, le `pom.xml` spécifie des versions plus anciennes et incompatibles des dépendances de Spring Framework, conduisant à un conflit dans le classpath.

Voici les problèmes clés identifiés dans le `pom.xml` :

1. **Version Incompatible du Plugin Maven Spring Boot :**
   - Le `spring-boot-maven-plugin` est défini en version `2.7.0`, qui est conçue pour Spring Boot 2.x, et non pour Spring Boot 3.4.2 (une version 3.x). Cette incohérence peut causer des problèmes pendant les phases de build et d'exécution.

2. **Dépendances Explicites Incompatibles de Spring Framework :**
   - Le `pom.xml` déclare explicitement `spring-aop` et `spring-aspects` avec la version `5.3.23` (Spring Framework 5.x), alors que Spring Boot 3.4.2 requiert Spring Framework 6.1.14. Maven priorise ces versions explicitement déclarées par rapport aux versions gérées par Spring Boot, résultant en un mélange de Spring Framework 5.x et 6.x dans le classpath. Ce mélange provoque le `NoClassDefFoundError` car `BeanRegistrationExcludeFilter` (provenant de Spring Framework 6.x) est indisponible lorsque les jars plus anciens 5.x sont chargés.

### Solution

Pour résoudre le problème, nous devons nous assurer que tous les composants du projet sont compatibles avec Spring Boot 3.4.2 et que Spring Boot gère les versions de ses dépendances pour éviter les conflits. Les modifications suivantes doivent être apportées au `pom.xml` :

1. **Mettre à Jour la Version du Plugin Maven Spring Boot :**
   - Changez la version du `spring-boot-maven-plugin` de `2.7.0` à `3.4.2` pour l'aligner avec la version de Spring Boot utilisée dans le projet.

2. **Supprimer les Dépendances Explicites de Spring Framework :**
   - Supprimez les déclarations explicites de `spring-aop` et `spring-aspects` avec la version `5.3.23`. Spring Boot 3.4.2 gère ces dépendances via ses starters (par exemple, `spring-boot-starter-web` inclut `spring-aop` avec la version correcte, 6.1.14). En les supprimant, nous empêchons Maven de remplacer la gestion des dépendances de Spring Boot.

### `pom.xml` Mis à Jour

Voici le fichier `pom.xml` corrigé avec les changements nécessaires appliqués :

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>org.lzwjava</groupId>
    <artifactId>blog-server</artifactId>
    <version>1.0</version>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
            <version>3.4.2</version>
        </dependency>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-api</artifactId>
            <version>5.9.3</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-engine</artifactId>
            <version>5.9.3</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.mockito</groupId>
            <artifactId>mockito-core</artifactId>
            <version>5.3.1</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <version>3.4.2</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.aspectj</groupId>
            <artifactId>aspectjrt</artifactId>
            <version>1.9.22</version>
        </dependency>
        <dependency>
            <groupId>org.aspectj</groupId>
            <artifactId>aspectjweaver</artifactId>
            <version>1.9.22</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>3.4.2</version>
                <executions>
                    <execution>
                        <goals>
                            <goal>repackage</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.0.0-M8</version>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-checkstyle-plugin</artifactId>
                <version>3.1.1</version>
                <configuration>
                    <configLocation>google_checks.xml</configLocation>
                </configuration>
                <executions>
                    <execution>
                        <goals>
                            <goal>check</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

### Explication des Changements

- **Mise à Jour du Plugin Maven Spring Boot :**
  - Changé `<version>2.7.0</version>` en `<version>3.4.2</version>` dans la configuration du `spring-boot-maven-plugin`. Cela garantit que le plugin est compatible avec Spring Boot 3.4.2, supportant les fonctionnalités et configurations spécifiques à la série 3.x.

- **Suppression de `spring-aop` et `spring-aspects` :**
  - Supprimé les dépendances suivantes :
    ```xml
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-aop</artifactId>
        <version>5.3.23</version>
    </dependency>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-aspects</artifactId>
        <version>5.3.23</version>
    </dependency>
    ```
  - `spring-aop` est déjà inclus dans `spring-boot-starter-web` (via `spring-web`), et Spring Boot gère sa version en 6.1.14, qui est compatible avec 3.4.2.
  - `spring-aspects` n'est pas une dépendance standard dans les starters Spring Boot. Si le projet en a explicitement besoin (par exemple, pour des aspects personnalisés), il peut être réajouté sans version (en laissant la gestion des dépendances de Spring Boot s'en charger) ou défini à `6.1.14`. Cependant, puisque l'erreur se produit au démarrage et concerne l'auto-configuration plutôt que des aspects manquants, il est probable qu'elle soit inutile ici et peut être supprimée en toute sécurité.

### Notes Supplémentaires

- **Dépendances AspectJ :**
  - Les dépendances `aspectjrt` et `aspectjweaver` (version 1.9.22) restent dans le `pom.xml` car elles sont compatibles avec Spring Framework 6.1.14 et peuvent être requises si le projet utilise des fonctionnalités AspectJ. Elles n'entrent pas en conflit avec Spring Boot 3.4.2.

- **Bonnes Pratiques :**
  - Pour les projets Spring Boot, il est recommandé d'utiliser `spring-boot-starter-parent` comme POM parent ou d'importer le BOM `spring-boot-dependencies` pour gérer automatiquement les versions des dépendances. Le `pom.xml` actuel ne fait ni l'un ni l'autre, mais la solution fonctionne sans nécessiter ce changement puisque `spring-boot-starter-web` et les autres starters imposent toujours une cohérence de version lorsque les surcharges explicites sont supprimées.

- **Vérification :**
  - Après avoir appliqué ces changements, exécutez `mvn clean spring-boot:run` pour vérifier que l'application démarre sans erreurs. Si le projet dépend de `spring-aspects` (par exemple, pour une fonctionnalité AOP spécifique), et que sa suppression cause des problèmes, réajoutez-le avec `<version>6.1.14</version>` ou omettez la version et assurez une gestion correcte des dépendances.

### Conclusion

En mettant à jour le `spring-boot-maven-plugin` en version 3.4.2 et en supprimant les dépendances explicites `spring-aop` et `spring-aspects`, le projet utilisera des versions cohérentes de Spring Boot (3.4.2) et de Spring Framework (6.1.14). Cela résout le conflit de classpath causant le `NoClassDefFoundError` et permet à l'application de démarrer avec succès.