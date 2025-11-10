---
audio: false
generated: true
lang: de
layout: post
title: Ausführen von Java-Klassen mit Maven Exec
translated: true
type: note
---

Das `exec:java`-Ziel des Maven Exec Plugins ist eine leistungsstarke Methode, um eine Java-Klasse mit einer `main`-Methode direkt aus Ihrem Maven-Build heraus auszuführen. Es führt die angegebene Java-Klasse **in derselben JVM** wie Ihr Maven-Build aus und verwendet die Abhängigkeiten des Projekts als Classpath.

So verwenden Sie es, mit gängigen Szenarien und Beispielen:

## 1. Grundlegende Verwendung von der Kommandozeile

Der einfachste Weg, `exec:java` zu verwenden, ist direkt von der Kommandozeile, besonders für schnelle Tests oder zum Ausführen einer bestimmten Utility-Klasse.

**Befehl:**

```bash
mvn exec:java -Dexec.mainClass="com.yourcompany.YourMainClass"
```

**Erklärung:**

*   `mvn exec:java`: Ruft das `java`-Ziel des `exec-maven-plugin` auf.
*   `-Dexec.mainClass="com.yourcompany.YourMainClass"`: Diese Systemeigenschaft spezifiziert den vollqualifizierten Namen der Java-Klasse, die die `public static void main(String[] args)`-Methode enthält, die Sie ausführen möchten.

**Beispiel:**

Angenommen, Sie haben eine Klasse `com.example.myapp.HelloWorld` mit einer `main`-Methode:

```java
package com.example.myapp;

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello from Maven exec:java!");
    }
}
```

Sie würden sie ausführen mit:

```bash
mvn compile exec:java -Dexec.mainClass="com.example.myapp.HelloWorld"
```

**Hinweis:** Es ist gute Praxis, zuerst `mvn compile` auszuführen, um sicherzustellen, dass Ihre Klassen kompiliert sind, bevor `exec:java` versucht, sie auszuführen.

## 2. Übergeben von Argumenten an Ihr Java-Programm

Sie können Argumente an die `main`-Methode Ihres Java-Programms mit der `exec.args`-Systemeigenschaft übergeben:

**Befehl:**

```bash
mvn exec:java -Dexec.mainClass="com.yourcompany.YourMainClass" -Dexec.args="arg1 arg2 \"arg with spaces\""
```

**Beispiel:**

Wenn Ihre `HelloWorld`-Klasse wie folgt wäre:

```java
package com.example.myapp;

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello from Maven exec:java!");
        if (args.length > 0) {
            System.out.println("Arguments received: ");
            for (String arg : args) {
                System.out.println("- " + arg);
            }
        }
    }
}
```

Sie würden sie so ausführen:

```bash
mvn compile exec:java -Dexec.mainClass="com.example.myapp.HelloWorld" -Dexec.args="FirstArgument SecondArgument"
```

Für Argumente mit Leerzeichen schließen Sie sie in Anführungszeichen ein:

```bash
mvn compile exec:java -Dexec.mainClass="com.example.myapp.HelloWorld" -Dexec.args="\"Hello World\" AnotherArg"
```

## 3. Konfigurieren von `exec:java` in `pom.xml`

Für dauerhaftere oder Standard-Konfigurationen können Sie den `exec-maven-plugin` zu Ihrer `pom.xml` hinzufügen. Dies erlaubt es Ihnen, eine Standard-`mainClass` und andere Parameter zu definieren, sodass Sie sie nicht jedes Mal auf der Kommandozeile angeben müssen.

**`pom.xml`-Konfiguration:**

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

**Erklärung der Konfigurationsoptionen:**

*   `<groupId>org.codehaus.mojo</groupId>` und `<artifactId>exec-maven-plugin</artifactId>`: Standard-Koordinaten für das Plugin.
*   `<version>3.2.0</version>`: Geben Sie immer eine aktuelle Version des Plugins an.
*   `<goals><goal>java</goal></goals>`: Dies bindet das `java`-Ziel. Wenn Sie es nicht an eine bestimmte Phase binden, wird es ausgeführt, wenn Sie explizit `mvn exec:java` aufrufen.
*   `<mainClass>com.example.myapp.HelloWorld</mainClass>`: Setzt die Standard-Hauptklasse zur Ausführung. Wenn Sie `mvn exec:java` ohne `-Dexec.mainClass` auf der Kommandozeile ausführen, wird diese Klasse verwendet.
*   `<arguments>`: Eine Liste von Argumenten, die an die `main`-Methode übergeben werden. Dies sind Standardargumente, die durch `exec.args` auf der Kommandozeile überschrieben werden können.
*   `<systemProperties>`: Erlaubt es Ihnen, Systemeigenschaften (`-Dkey=value`) zu definieren, die für Ihre Java-Anwendung verfügbar sind, wenn `exec:java` läuft.

**Ausführen mit `pom.xml`-Konfiguration:**

Einmal in `pom.xml` konfiguriert:

*   Um mit der Standard-Hauptklasse und -Argumenten auszuführen:
    ```bash
    mvn compile exec:java
    ```
*   Um die Hauptklasse von der Kommandozeile zu überschreiben:
    ```bash
    mvn compile exec:java -Dexec.mainClass="com.example.myapp.AnotherMainClass"
    ```
*   Um Argumente von der Kommandozeile zu überschreiben/hinzuzufügen:
    ```bash
    mvn compile exec:java -Dexec.args="commandLineArg1 commandLineArg2"
    ```
    (Hinweis: `exec.args` wird typischerweise die in `pom.xml` definierten `arguments` *ersetzen*, wenn es auf der Kommandozeile angegeben wird.)

## 4. Wichtige Unterschiede zu `exec:exec`

Es ist wichtig, den Unterschied zwischen `exec:java` und `exec:exec` zu verstehen:

*   **`exec:java`**: Führt das Java-Programm **in derselben JVM** wie Maven aus. Dies ist generell schneller, da das Starten eines neuen Prozesses vermieden wird. Es richtet automatisch die Abhängigkeiten des Projekts im Classpath ein.
*   **`exec:exec`**: Führt ein beliebiges externes Programm (einschließlich `java` selbst) **in einem separaten Prozess** aus. Dies ist nützlich, wenn Sie einen anderen Java-Executable angeben, JVM-Argumente (wie `-Xmx`) übergeben oder Nicht-Java-Executables ausführen müssen. Wenn Sie `exec:exec` verwenden, um ein Java-Programm auszuführen, müssen Sie typischerweise den Classpath manuell mit `%classpath` in den Argumenten konstruieren.

Für die meisten Standard-Java-Anwendungsausführungen innerhalb eines Maven-Builds ist `exec:java` die bequemere Wahl.

## 5. Wichtige Überlegungen

*   **Classpath:** `exec:java` schließt automatisch die kompilierten Klassen Ihres Projekts und seine Abhängigkeiten in den Classpath ein.
*   **JVM-Argumente:** Da `exec:java` in der *gleichen* JVM wie Maven läuft, können Sie JVM-Argumente (wie `-Xmx`, `-XX:MaxPermSize`) nicht direkt an `exec:java` über seine Konfiguration oder `exec.args` übergeben. Diese Argumente müssen der Maven-JVM selbst übergeben werden, typischerweise über die Umgebungsvariable `MAVEN_OPTS`:
    ```bash
    export MAVEN_OPTS="-Xmx1024m -Dsome.jvm.property=value"
    mvn exec:java ...
    ```
*   **System.exit():** Wenn Ihr Java-Programm `System.exit()` aufruft, wird es den gesamten Maven-Build-Prozess beenden, nicht nur Ihr Programm. Seien Sie sich dessen bewusst, wenn Sie `exec:java` verwenden. Das Plugin hat eine Option `blockSystemExit` (seit Version 3.2.0), die dies zu verhindern versucht, aber es ist am besten, Ihre `main`-Methode so zu gestalten, dass sie ordnungsgemäß beendet wird, ohne `System.exit()` aufzurufen.
*   **Abhängigkeiten:** `exec:java` verlässt sich auf die Abhängigkeiten des Projekts. Wenn Sie eine Klasse aus einer Abhängigkeit ausführen müssen, die nicht Teil des Projekt-Builds ist, müssen Sie möglicherweise die Plugin-Konfiguration anpassen oder die Verwendung von `exec:exec` mit expliziter Classpath-Definition in Betracht ziehen.
*   **Plugin-Version:** Verwenden Sie immer eine aktuelle Version des `exec-maven-plugin` für die neuesten Features und Bugfixes. Prüfen Sie die MojoHaus-Website auf die aktuellsten Informationen.