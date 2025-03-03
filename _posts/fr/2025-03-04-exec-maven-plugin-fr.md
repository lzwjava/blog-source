---
audio: false
generated: true
lang: fr
layout: post
title: Plugin Maven Exec
translated: true
---

Pour utiliser le plugin Maven `org.codehaus.mojo` Exec dans votre projet Maven, vous devez le configurer dans votre fichier `pom.xml` et décider comment vous souhaitez exécuter des programmes—soit des commandes externes, soit des programmes Java—durant votre processus de build. Le plugin fournit deux objectifs principaux : `exec:exec` pour exécuter des programmes externes et `exec:java` pour exécuter des classes Java. Ci-dessous, je vais vous guider à travers les étapes pour le configurer et l'utiliser efficacement.

### Étape 1 : Ajouter le Plugin à votre `pom.xml`
Tout d'abord, incluez le plugin Exec Maven dans la section `<build><plugins>` de votre `pom.xml`. Spécifiez le `groupId`, `artifactId` et une version (la plus récente à ce jour est `3.1.0`) :

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
        </plugin>
    </plugins>
</build>
```

Cela ajoute le plugin à votre projet, mais il ne fera rien tant que vous ne l'aurez pas configuré ou exécuté manuellement.

### Étape 2 : Choisir votre Objectif
Le plugin offre deux objectifs principaux :
- **`exec:exec`** : Exécute tout programme externe (par exemple, des scripts shell, des binaires, ou même la commande `java`).
- **`exec:java`** : Exécute une classe Java avec une méthode `main` de votre projet dans la même JVM que Maven.

Vous pouvez utiliser ces objectifs soit en les exécutant manuellement depuis la ligne de commande (par exemple, `mvn exec:exec`), soit en les liant à une phase spécifique du cycle de vie de build Maven.

### Option 1 : Exécuter un Programme Java avec `exec:java`
Si vous souhaitez exécuter une classe Java de votre projet, utilisez l'objectif `exec:java`. Cela est idéal pour exécuter une méthode `main` dans une classe qui fait partie de votre projet, en utilisant automatiquement le classpath d'exécution du projet (y compris les dépendances).

#### Exécution Manuelle
Ajoutez une configuration pour spécifier la classe principale :

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <configuration>
                <mainClass>com.example.Main</mainClass>
            </configuration>
        </plugin>
    </plugins>
</build>
```

Ensuite, exécutez-le depuis la ligne de commande :

```bash
mvn exec:java
```

Cela exécute `com.example.Main` dans la même JVM que Maven, en héritant des paramètres JVM de Maven.

#### Exécution Automatique Pendant le Build
Pour l'exécuter automatiquement pendant une phase de build (par exemple, `test`), utilisez la section `<executions>` :

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <executions>
                <execution>
                    <id>run-my-java</id>
                    <phase>test</phase>
                    <goals>
                        <goal>java</goal>
                    </goals>
                    <configuration>
                        <mainClass>com.example.Main</mainClass>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

Maintenant, lorsque vous exécutez `mvn test`, la classe `com.example.Main` s'exécutera pendant la phase `test`.

#### Passer des Arguments ou des Propriétés Système
Vous pouvez passer des arguments à la méthode `main` ou définir des propriétés système :

```xml
<configuration>
    <mainClass>com.example.Main</mainClass>
    <arguments>
        <argument>arg1</argument>
        <argument>arg2</argument>
    </arguments>
    <systemProperties>
        <systemProperty>
            <key>propertyName</key>
            <value>propertyValue</value>
        </systemProperty>
    </systemProperties>
</configuration>
```

Notez que `exec:java` s'exécute dans la même JVM que Maven, donc les options JVM (par exemple, `-Xmx`) sont héritées de la manière dont Maven est invoqué (par exemple, `mvn -Xmx512m exec:java`).

### Option 2 : Exécuter un Programme Externe avec `exec:exec`
Pour exécuter des programmes externes comme des scripts shell ou des commandes, utilisez l'objectif `exec:exec`.

#### Exécution Manuelle
Configurez le plugin pour exécuter un script :

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <configuration>
                <executable>myScript.sh</executable>
                <workingDirectory>/path/to/dir</workingDirectory>
                <arguments>
                    <argument>param1</argument>
                    <argument>param2</argument>
                </arguments>
            </configuration>
        </plugin>
    </plugins>
</build>
```

Exécutez-le avec :

```bash
mvn exec:exec
```

Cela exécute `myScript.sh` avec les arguments spécifiés dans le répertoire de travail donné.

#### Exécution Automatique Pendant le Build
Liez-le à une phase, comme démarrer et arrêter un serveur pour des tests d'intégration :

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <executions>
                <execution>
                    <id>start-server</id>
                    <phase>pre-integration-test</phase>
                    <goals>
                        <goal>exec</goal>
                    </goals>
                    <configuration>
                        <executable>startServer.sh</executable>
                    </configuration>
                </execution>
                <execution>
                    <id>stop-server</id>
                    <phase>post-integration-test</phase>
                    <goals>
                        <goal>exec</goal>
                    </goals>
                    <configuration>
                        <executable>stopServer.sh</executable>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

L'exécution de `mvn integration-test` démarrera le serveur avant les tests et l'arrêtera ensuite.

#### Exécuter Java avec des Options JVM Personnalisées
Si vous avez besoin d'une JVM séparée avec des options spécifiques (contrairement à `exec:java`), utilisez `exec:exec` avec l'exécutable `java`. Vous devrez gérer le classpath manuellement. Voici un exemple :

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <configuration>
                <executable>java</executable>
                <arguments>
                    <argument>-Xmx512m</argument>
                    <argument>-classpath</argument>
                    <argument>${project.build.outputDirectory}</argument>
                    <argument>com.example.Main</argument>
                </arguments>
            </configuration>
        </plugin>
    </plugins>
</build>
```

Pour inclure les dépendances dans le classpath, vous pouvez utiliser le plugin `maven-dependency-plugin` pour le générer :

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-dependency-plugin</artifactId>
            <version>3.2.0</version>
            <executions>
                <execution>
                    <id>build-classpath</id>
                    <phase>generate-resources</phase>
                    <goals>
                        <goal>build-classpath</goal>
                    </goals>
                    <configuration>
                        <outputProperty>project.classpath</outputProperty>
                    </configuration>
                </execution>
            </executions>
        </plugin>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <executions>
                <execution>
                    <id>run-java</id>
                    <phase>test</phase>
                    <goals>
                        <goal>exec</goal>
                    </goals>
                    <configuration>
                        <executable>java</executable>
                        <arguments>
                            <argument>-Xmx512m</argument>
                            <argument>-classpath</argument>
                            <argument>${project.classpath}:${project.build.outputDirectory}</argument>
                            <argument>com.example.Main</argument>
                        </arguments>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

Ajustez le séparateur de classpath (`:` pour Unix, `;` pour Windows) selon les besoins.

### Options de Configuration Supplémentaires
- **Variables d'Environnement** (pour `exec:exec`) :
  ```xml
  <configuration>
      <executable>myScript.sh</executable>
      <environmentVariables>
          <MY_VAR>value</MY_VAR>
      </environmentVariables>
  </configuration>
  ```
- **Répertoire de Travail** : Utilisez `<workingDirectory>` pour définir où la commande s'exécute.

### Résumé
Le plugin Exec Maven est polyvalent :
- Utilisez `exec:java` pour exécuter facilement des classes Java de votre projet, en utilisant le classpath du projet, mais il s'exécute dans la JVM de Maven.
- Utilisez `exec:exec` pour des programmes externes ou Java avec des options JVM personnalisées, nécessitant une gestion manuelle du classpath si nécessaire.
- Configurez-le dans `pom.xml` et exécutez-le manuellement (`mvn exec:java` ou `mvn exec:exec`) ou liez-le aux phases de build avec `<executions>`.

Cette configuration vous permet d'intégrer des exécutions personnalisées de manière transparente dans votre processus de build Maven !