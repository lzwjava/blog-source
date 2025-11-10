---
audio: false
generated: true
lang: de
layout: post
title: Umleiten der Eingabe in Maven-Java-Programmen
translated: true
type: note
---

Die Umleitung der Eingabe für `exec:java`-Programme kann etwas knifflig sein, da `exec:java` den Java-Prozess in *derselben JVM* wie Maven ausführt. Das bedeutet, dass Sie die standardmäßigen Shell-Umleitungsoperatoren (`<`, `>`) nicht auf die gleiche Weise verwenden können wie für einen separaten Prozess.

Sie haben jedoch weiterhin einige Möglichkeiten, um Ihrem `exec:java`-Programm Eingaben bereitzustellen:

## 1. Programmatische Eingabe (Standard `System.in`)

Der direkteste Weg besteht darin, Ihr Java-Programm so zu gestalten, dass es wie üblich von `System.in` liest. Wenn Sie `mvn exec:java` ausführen, wird alles, was Sie in Ihrer Konsole eingeben, an `System.in` Ihres Java-Programms weitergeleitet.

**Beispiel-Java-Programm (`MyInputProgram.java`):**

```java
package com.example.app;

import java.util.Scanner;

public class MyInputProgram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        System.out.println("Hello, " + name + "!");

        System.out.print("Enter your age: ");
        int age = scanner.nextInt();
        System.out.println("You are " + age + " years old.");

        scanner.close();
    }
}
```

**Ausführung von der Kommandozeile:**

```bash
mvn compile exec:java -Dexec.mainClass="com.example.app.MyInputProgram"
```

Wenn Sie dies ausführen, startet Maven und Ihr Programm fordert Sie dann zur Eingabe auf. Sie tippen direkt in die Konsole.

## 2. Verwenden der `exec.args`-Eigenschaft für Eingaben (für einfache Fälle)

Wenn Ihr Programm sehr einfache, nicht-interaktive Eingaben erwartet, *könnten* Sie diese als Argument übergeben. Ihr Programm liest dann dieses Argument anstelle von `System.in`. Dies ist keine echte Standard-Eingabeumleitung, erfüllt aber für einfache Daten einen ähnlichen Zweck.

**Beispiel-Java-Programm (`MyArgProgram.java`):**

```java
package com.example.app;

public class MyArgProgram {
    public static void main(String[] args) {
        if (args.length > 0) {
            String inputData = args[0];
            System.out.println("Received input from argument: " + inputData);
        } else {
            System.out.println("No input argument provided.");
        }
    }
}
```

**Ausführung von der Kommandozeile:**

```bash
mvn compile exec:java -Dexec.mainClass="com.example.app.MyArgProgram" -Dexec.args="MyCustomInputString"
```

Oder mit Leerzeichen:

```bash
mvn compile exec:java -Dexec.mainClass="com.example.app.MyArgProgram" -Dexec.args="\"Input with spaces\""
```

Dieser Ansatz ist nur geeignet, wenn Ihr Programm so modifiziert werden kann, dass es seine "Eingabe" als Kommandozeilenargumente akzeptiert.

## 3. Umleiten der Eingabe mit Shell-Umleitung (mit `exec:exec`)

Wenn Sie unbedingt eine Eingabe von einer Datei oder einer Pipe umleiten müssen, **müssen** Sie das Ziel `exec:exec` anstelle von `exec:java` verwenden. Das Ziel `exec:exec` startet einen separaten Prozess, was es der Shell ermöglicht, die Standard-Eingabe-/Ausgabeumleitung zu handhaben.

**`pom.xml`-Konfiguration für `exec:exec`:**

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

**Beispiel-Java-Programm (dasselbe `MyInputProgram.java` wie oben):**

```java
package com.example.app;

import java.util.Scanner;

public class MyInputProgram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        System.out.println("Hello, " + name + "!");

        // Angenommen, Sie möchten nach dem Namen eine weitere Zeile für das Alter lesen
        System.out.print("Enter your age: ");
        int age = scanner.nextInt();
        System.out.println("You are " + age + " years old.");

        scanner.close();
    }
}
```

**Eingabedatei (`input.txt`):**

```
Alice
30
```

**Ausführung mit `exec:exec` und Eingabeumleitung:**

Kompilieren Sie zunächst Ihr Projekt:

```bash
mvn compile
```

Führen Sie dann das Ziel `exec:exec` aus und leiten Sie die Eingabe über Ihre Shell um:

```bash
mvn exec:exec@run-my-java-app < input.txt
```

**Erklärung:**

  * `mvn exec:exec@run-my-java-app`: Führt das Ziel `exec` des `exec-maven-plugin` mit der `id` "run-my-java-app" aus.
  * `< input.txt`: Dies ist ein standardmäßiger Shell-Umleitungsoperator. Er weist Ihre Shell an, den Inhalt von `input.txt` zu nehmen und ihn als Standardeingabe an den ausgeführten Befehl (`java com.example.app.MyInputProgram`) zu senden.

**Wichtige Hinweise für `exec:exec`:**

  * **`executable`:** Sie geben explizit `java` als ausführbare Datei an.
  * **`arguments`:** Sie müssen die Argumente des `java`-Befehls manuell konstruieren, einschließlich `-classpath` und der `mainClass`. Das Tag `<classpath/>` ist ein spezieller Wert, den das `exec-maven-plugin` durch den tatsächlich berechneten Classpath Ihres Projekts ersetzt.
  * **`workingDirectory`:** Es ist oft hilfreich, das `workingDirectory` auf `${project.build.directory}/classes` zu setzen, damit Java Ihre kompilierten `.class`-Dateien finden kann.
  * **`outputFile` (Optional):** Das `exec-maven-plugin` für `exec:exec` bietet auch eine `<outputFile>`-Konfigurationsoption an, um die Standardausgabe und Fehlerausgabe des Programms direkt innerhalb der Plugin-Konfiguration in eine Datei umzuleiten, anstatt sich auf die Shell-Umleitung zu verlassen. Dies kann für Protokollierungszwecke nützlich sein.

**Zusammenfassend:**

  * Für interaktive Eingaben, bei denen ein Benutzer direkt tippt, funktionieren `exec:java` und `System.in` einwandfrei.
  * Um Eingaben aus einer Datei oder einer Pipe bereitzustellen, müssen Sie zu `exec:exec` wechseln und die Eingabeumleitungsfähigkeiten Ihrer Shell (`<`) nutzen.