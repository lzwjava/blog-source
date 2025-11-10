---
audio: false
generated: true
lang: fr
layout: post
title: Exécuter des classes Java avec Maven Exec
translated: true
type: note
---

Le but `exec:java` du Maven Exec Plugin est un moyen puissant d'exécuter une classe Java avec une méthode `main` directement depuis votre build Maven. Il exécute la classe Java spécifiée **dans la même JVM** que votre build Maven, en utilisant les dépendances du projet comme classpath.

Voici comment l'utiliser, avec des scénarios et exemples courants :

## 1. Utilisation de base depuis la ligne de commande

La façon la plus simple d'utiliser `exec:java` est directement depuis la ligne de commande, surtout pour des tests rapides ou pour exécuter une classe utilitaire spécifique.

**Commande :**

```bash
mvn exec:java -Dexec.mainClass="com.yourcompany.YourMainClass"
```

**Explication :**

  * `mvn exec:java` : Invoke le but `java` de l'`exec-maven-plugin`.
  * `-Dexec.mainClass="com.yourcompany.YourMainClass"` : Cette propriété système spécifie le nom qualifié complet de la classe Java qui contient la méthode `public static void main(String[] args)` que vous souhaitez exécuter.

**Exemple :**

Supposons que vous ayez une classe `com.example.myapp.HelloWorld` avec une méthode `main` :

```java
package com.example.myapp;

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello from Maven exec:java!");
    }
}
```

Vous l'exécuteriez en utilisant :

```bash
mvn compile exec:java -Dexec.mainClass="com.example.myapp.HelloWorld"
```

**Remarque :** Il est recommandé d'exécuter d'abord `mvn compile` pour s'assurer que vos classes sont compilées avant que `exec:java` tente de les exécuter.

## 2. Passage d'arguments à votre programme Java

Vous pouvez passer des arguments à la méthode `main` de votre programme Java en utilisant la propriété système `exec.args` :

**Commande :**

```bash
mvn exec:java -Dexec.mainClass="com.yourcompany.YourMainClass" -Dexec.args="arg1 arg2 \"arg with spaces\""
```

**Exemple :**

Si votre classe `HelloWorld` était :

```java
package com.example.myapp;

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello from Maven exec:java!");
        if (args.length > 0) {
            System.out.println("Arguments reçus : ");
            for (String arg : args) {
                System.out.println("- " + arg);
            }
        }
    }
}
```

Vous l'exécuteriez comme ceci :

```bash
mvn compile exec:java -Dexec.mainClass="com.example.myapp.HelloWorld" -Dexec.args="FirstArgument SecondArgument"
```

Pour les arguments contenant des espaces, encadrez-les de guillemets :

```bash
mvn compile exec:java -Dexec.mainClass="com.example.myapp.HelloWorld" -Dexec.args="\"Hello World\" AnotherArg"
```

## 3. Configuration de `exec:java` dans `pom.xml`

Pour des configurations plus permanentes ou par défaut, vous pouvez ajouter l'`exec-maven-plugin` à votre `pom.xml`. Cela vous permet de définir une `mainClass` par défaut et d'autres paramètres, afin de ne pas avoir à les spécifier à chaque fois sur la ligne de commande.

**Configuration `pom.xml` :**

```xml
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.yourcompany</groupId>
    <artifactId>my-maven-app</artifactId>
    <version>1.0-SNAPSHOT</modelVersion>

    <build>
        <plugins>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>3.2.0</version> <executions>
                    <execution>
                        <goals>
                            <goal>java</goal>
                        </goals>
                    </execution>
                </executions>
                <configuration>
                    <mainClass>com.example.myapp.HelloWorld</mainClass>
                    <arguments>
                        <argument>defaultArg1</argument>
                        <argument>defaultArg2</argument>
                    </arguments>
                    <systemProperties>
                        <systemProperty>
                            <key>my.custom.property</key>
                            <value>someValue</value>
                        </systemProperty>
                    </systemProperties>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
    </properties>

</project>
```

**Explication des options de configuration :**

  * `<groupId>org.codehaus.mojo</groupId>` et `<artifactId>exec-maven-plugin</artifactId>` : Coordonnées standard du plugin.
  * `<version>3.2.0</version>` : Spécifiez toujours une version récente du plugin.
  * `<goals><goal>java</goal></goals>` : Cela lie le but `java`. Si vous ne le liez pas à une phase spécifique, il sera exécuté lorsque vous appellerez explicitement `mvn exec:java`.
  * `<mainClass>com.example.myapp.HelloWorld</mainClass>` : Définit la classe principale par défaut à exécuter. Si vous exécutez `mvn exec:java` sans `-Dexec.mainClass` sur la ligne de commande, cette classe sera utilisée.
  * `<arguments>` : Une liste d'arguments à passer à la méthode `main`. Ce sont des arguments par défaut qui peuvent être remplacés par `exec.args` sur la ligne de commande.
  * `<systemProperties>` : Vous permet de définir des propriétés système (`-Dkey=value`) qui seront disponibles pour votre application Java lors de l'exécution de `exec:java`.

**Exécution avec la configuration `pom.xml` :**

Une fois configuré dans `pom.xml` :

  * Pour exécuter avec la classe principale et les arguments par défaut :
    ```bash
    mvn compile exec:java
    ```
  * Pour remplacer la classe principale depuis la ligne de commande :
    ```bash
    mvn compile exec:java -Dexec.mainClass="com.example.myapp.AnotherMainClass"
    ```
  * Pour remplacer/ajouter des arguments depuis la ligne de commande :
    ```bash
    mvn compile exec:java -Dexec.args="commandLineArg1 commandLineArg2"
    ```
    (Remarque : `exec.args` remplacera généralement les `arguments` définis dans `pom.xml` s'il est fourni sur la ligne de commande.)

## 4. Différences clés avec `exec:exec`

Il est important de comprendre la distinction entre `exec:java` et `exec:exec` :

  * **`exec:java`** : Exécute le programme Java **dans la même JVM** que Maven. C'est généralement plus rapide car cela évite de lancer un nouveau processus. Il configure automatiquement les dépendances du projet dans le classpath.
  * **`exec:exec`** : Exécute un programme externe arbitraire (y compris `java` lui-même) **dans un processus séparé**. C'est utile lorsque vous devez spécifier un exécutable Java différent, passer des arguments JVM (comme `-Xmx`), ou exécuter des exécutables non-Java. Si vous utilisez `exec:exec` pour exécuter un programme Java, vous devez généralement construire manuellement le classpath en utilisant `%classpath` dans les arguments.

Pour l'exécution standard de la plupart des applications Java dans un build Maven, `exec:java` est le choix le plus pratique.

## 5. Considérations importantes

  * **Classpath :** `exec:java` inclut automatiquement les classes compilées de votre projet et ses dépendances dans le classpath.
  * **Arguments JVM :** Parce que `exec:java` s'exécute dans la *même* JVM que Maven, vous ne pouvez pas passer d'arguments JVM (comme `-Xmx`, `-XX:MaxPermSize`) directement à `exec:java` via sa configuration ou `exec.args`. Ces arguments doivent être passés à la JVM Maven elle-même, généralement via la variable d'environnement `MAVEN_OPTS` :
    ```bash
    export MAVEN_OPTS="-Xmx1024m -Dsome.jvm.property=value"
    mvn exec:java ...
    ```
  * **System.exit()** : Si votre programme Java appelle `System.exit()`, cela terminera l'intégralité du processus de build Maven, pas seulement votre programme. Soyez conscient de cela lorsque vous utilisez `exec:java`. Le plugin a une option `blockSystemExit` (depuis la version 3.2.0) qui tente d'empêcher cela, mais il est préférable de concevoir votre méthode main pour qu'elle se termine correctement sans appeler `System.exit()`.
  * **Dépendances :** `exec:java` repose sur les dépendances du projet. Si vous devez exécuter une classe provenant d'une dépendance qui ne fait pas partie de la construction de votre projet, vous devrez peut-être ajuster la configuration du plugin ou envisager d'utiliser `exec:exec` avec une définition explicite du classpath.
  * **Version du Plugin :** Utilisez toujours une version récente de l'`exec-maven-plugin` pour bénéficier des dernières fonctionnalités et corrections de bogues. Consultez le site web de MojoHaus pour les informations les plus à jour.