---
audio: false
generated: true
lang: fr
layout: post
title: Redirection des entrées dans les programmes Java Maven
translated: true
type: note
---

La redirection de l'entrée pour les programmes `exec:java` peut être un peu délicate car `exec:java` exécute le processus Java dans *la même JVM* que Maven. Cela signifie que vous ne pouvez pas utiliser les opérateurs de redirection shell standard (`<`, `>`) de la même manière que vous le feriez pour un processus séparé.

Cependant, vous avez encore quelques options pour fournir une entrée à votre programme `exec:java` :

## 1. Entrée programmatique (`System.in` standard)

La manière la plus simple est de concevoir votre programme Java pour qu'il lise depuis `System.in` comme d'habitude. Lorsque vous exécutez `mvn exec:java`, tout ce que vous tapez dans votre console sera dirigé vers `System.in` de votre programme Java.

**Exemple de programme Java (`MyInputProgram.java`) :**

```java
package com.example.app;

import java.util.Scanner;

public class MyInputProgram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Entrez votre nom : ");
        String name = scanner.nextLine();
        System.out.println("Bonjour, " + name + " !");

        System.out.print("Entrez votre âge : ");
        int age = scanner.nextInt();
        System.out.println("Vous avez " + age + " ans.");

        scanner.close();
    }
}
```

**Exécution depuis la ligne de commande :**

```bash
mvn compile exec:java -Dexec.mainClass="com.example.app.MyInputProgram"
```

Lorsque vous exécutez ceci, Maven démarrera, puis votre programme vous demandera une entrée. Vous tapez directement dans la console.

## 2. Utilisation de la propriété `exec.args` pour l'entrée (pour les cas simples)

Si votre programme attend une entrée très simple et non interactive, vous *pourriez* peut-être la passer comme argument, et votre programme lit alors cet argument au lieu de `System.in`. Ce n'est pas une véritable redirection d'entrée standard, mais cela remplit un objectif similaire pour des données simples.

**Exemple de programme Java (`MyArgProgram.java`) :**

```java
package com.example.app;

public class MyArgProgram {
    public static void main(String[] args) {
        if (args.length > 0) {
            String inputData = args[0];
            System.out.println("Entrée reçue depuis l'argument : " + inputData);
        } else {
            System.out.println("Aucun argument d'entrée fourni.");
        }
    }
}
```

**Exécution depuis la ligne de commande :**

```bash
mvn compile exec:java -Dexec.mainClass="com.example.app.MyArgProgram" -Dexec.args="MyCustomInputString"
```

Ou avec des espaces :

```bash
mvn compile exec:java -Dexec.mainClass="com.example.app.MyArgProgram" -Dexec.args="\"Input with spaces\""
```

Cette approche n'est envisageable que si votre programme peut être modifié pour accepter son "entrée" comme arguments de ligne de commande.

## 3. Redirection de l'entrée en utilisant la redirection shell (avec `exec:exec`)

Si vous avez absolument besoin de rediriger l'entrée depuis un fichier ou un pipe, vous **devez** utiliser le goal `exec:exec` au lieu de `exec:java`. Le goal `exec:exec` génère un processus séparé, ce qui permet au shell de gérer la redirection de l'entrée/sortie standard.

**Configuration `pom.xml` pour `exec:exec` :**

```xml
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.yourcompany</groupId>
    <artifactId>my-maven-app</artifactId>
    <version>1.0-SNAPSHOT</version>

    <build>
        <plugins>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>3.2.0</version> <executions>
                    <execution>
                        <id>run-my-java-app</id>
                        <phase>package</phase> <goals>
                            <goal>exec</goal>
                        </goals>
                        <configuration>
                            <executable>java</executable>
                            <arguments>
                                <argument>-classpath</argument>
                                <classpath/> <argument>com.example.app.MyInputProgram</argument>
                                </arguments>
                            <workingDirectory>${project.build.directory}/classes</workingDirectory>
                            </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
    </properties>

</project>
```

**Exemple de programme Java (le même `MyInputProgram.java` que ci-dessus) :**

```java
package com.example.app;

import java.util.Scanner;

public class MyInputProgram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Entrez votre nom : ");
        String name = scanner.nextLine();
        System.out.println("Bonjour, " + name + " !");

        // En supposant que vous voulez lire une autre ligne pour l'âge après le nom
        System.out.print("Entrez votre âge : ");
        int age = scanner.nextInt();
        System.out.println("Vous avez " + age + " ans.");

        scanner.close();
    }
}
```

**Fichier d'entrée (`input.txt`) :**

```
Alice
30
```

**Exécution avec `exec:exec` et redirection d'entrée :**

D'abord, compilez votre projet :

```bash
mvn compile
```

Ensuite, exécutez le goal `exec:exec` et redirigez l'entrée en utilisant votre shell :

```bash
mvn exec:exec@run-my-java-app < input.txt
```

**Explication :**

  * `mvn exec:exec@run-my-java-app` : Exécute le goal `exec` du `exec-maven-plugin` avec l'`id` "run-my-java-app".
  * `< input.txt` : C'est un opérateur de redirection shell standard. Il indique à votre shell de prendre le contenu de `input.txt` et de l'envoyer comme entrée standard à la commande exécutée (`java com.example.app.MyInputProgram`).

**Notes importantes pour `exec:exec` :**

  * **`executable` :** Vous spécifiez explicitement `java` comme exécutable.
  * **`arguments` :** Vous devez construire manuellement les arguments de la commande `java`, y compris `-classpath` et la `mainClass`. La balise `<classpath/>` est une valeur spéciale que le `exec-maven-plugin` remplace par le classpath réel calculé de votre projet.
  * **`workingDirectory` :** Il est souvent utile de définir le `workingDirectory` sur `${project.build.directory}/classes` afin que Java puisse trouver vos fichiers `.class` compilés.
  * **`outputFile` (Optionnel) :** Le `exec-maven-plugin` pour `exec:exec` fournit également une option de configuration `<outputFile>` pour rediriger la sortie standard et l'erreur du programme vers un fichier directement dans la configuration du plugin, plutôt que de dépendre de la redirection shell. Cela peut être utile pour la journalisation.

**En résumé :**

  * Pour une entrée interactive où un utilisateur tape directement, `exec:java` et `System.in` fonctionnent correctement.
  * Pour fournir une entrée depuis un fichier ou un pipe, vous devrez passer à `exec:exec` et tirer parti des capacités de redirection d'entrée de votre shell (`<`).