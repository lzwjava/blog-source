---
audio: false
generated: true
lang: de
layout: post
title: Exec Maven Plugin
translated: true
type: note
---

Um den `org.codehaus.mojo` Exec Maven Plugin in Ihrem Maven-Projekt zu verwenden, müssen Sie ihn in Ihrer `pom.xml`-Datei konfigurieren und entscheiden, wie Sie Programme – entweder externe Befehle oder Java-Programme – während Ihres Build-Prozesses ausführen möchten. Das Plugin bietet zwei Haupt-Goals: `exec:exec` zum Ausführen externer Programme und `exec:java` zum Ausführen von Java-Klassen. Im Folgenden zeige ich Ihnen die Schritte zur Einrichtung und effektiven Nutzung.

### Schritt 1: Fügen Sie das Plugin zu Ihrer `pom.xml` hinzu
Fügen Sie zunächst das Exec Maven Plugin im Abschnitt `<build><plugins>` Ihrer `pom.xml` hinzu. Geben Sie `groupId`, `artifactId` und eine Version an (die aktuellste ist `3.1.0`):

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

Dies fügt das Plugin zu Ihrem Projekt hinzu, aber es wird noch nichts tun, bis Sie es konfigurieren oder seine Goals manuell ausführen.

### Schritt 2: Wählen Sie Ihr Goal
Das Plugin bietet zwei primäre Goals:
- **`exec:exec`**: Führt ein beliebiges externes Programm aus (z.B. Shell-Skripte, Binärdateien oder sogar den `java`-Befehl).
- **`exec:java`**: Führt eine Java-Klasse mit einer `main`-Methode aus Ihrem Projekt in derselben JVM wie Maven aus.

Sie können diese Goals entweder manuell über die Kommandozeile ausführen (z.B. `mvn exec:exec`) oder sie an eine bestimmte Phase im Maven Build-Lifecycle binden.

### Option 1: Ausführen eines Java-Programms mit `exec:java`
Wenn Sie eine Java-Klasse aus Ihrem Projekt ausführen möchten, verwenden Sie das Goal `exec:java`. Dies ist ideal, um eine `main`-Methode in einer Klasse auszuführen, die Teil Ihres Projekts ist, und automatisch den Runtime-Classpath des Projekts (einschließlich Abhängigkeiten) zu nutzen.

#### Manuelle Ausführung
Fügen Sie eine Konfiguration hinzu, um die Hauptklasse anzugeben:

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

Führen Sie es dann über die Kommandozeile aus:

```bash
mvn exec:java
```

Dies führt `com.example.Main` in derselben JVM wie Maven aus und erbt die JVM-Einstellungen von Maven.

#### Automatische Ausführung während des Builds
Um es automatisch während einer Build-Phase (z.B. `test`) auszuführen, verwenden Sie den Abschnitt `<executions>`:

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

Wenn Sie nun `mvn test` ausführen, wird die Klasse `com.example.Main` während der `test`-Phase ausgeführt.

#### Übergeben von Argumenten oder Systemeigenschaften
Sie können Argumente an die `main`-Methode übergeben oder Systemeigenschaften setzen:

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

Beachten Sie, dass `exec:java` in derselben JVM wie Maven läuft, daher werden JVM-Optionen (z.B. `-Xmx`) von der Art geerbt, wie Maven aufgerufen wurde (z.B. `mvn -Xmx512m exec:java`).

### Option 2: Ausführen eines externen Programms mit `exec:exec`
Um externe Programme wie Shell-Skripte oder Befehle auszuführen, verwenden Sie das Goal `exec:exec`.

#### Manuelle Ausführung
Konfigurieren Sie das Plugin, um ein Skript auszuführen:

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

Führen Sie es mit folgendem Befehl aus:

```bash
mvn exec:exec
```

Dies führt `myScript.sh` mit den angegebenen Argumenten im angegebenen Arbeitsverzeichnis aus.

#### Automatische Ausführung während des Builds
Binden Sie es an eine Phase, z.B. zum Starten und Stoppen eines Servers für Integrationstests:

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

Die Ausführung von `mvn integration-test` startet den Server vor den Tests und stoppt ihn danach.

#### Ausführen von Java mit benutzerdefinierten JVM-Optionen
Wenn Sie eine separate JVM mit spezifischen Optionen benötigen (im Gegensatz zu `exec:java`), verwenden Sie `exec:exec` mit dem `java`-Executable. Sie müssen den Classpath manuell verwalten. Hier ein Beispiel:

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

Um Abhängigkeiten in den Classpath aufzunehmen, können Sie das `maven-dependency-plugin` verwenden, um ihn zu generieren:

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

Passen Sie den Classpath-Separator (`:` für Unix, `;` für Windows) nach Bedarf an.

### Zusätzliche Konfigurationsoptionen
- **Umgebungsvariablen** (für `exec:exec`):
  ```xml
  <configuration>
      <executable>myScript.sh</executable>
      <environmentVariables>
          <MY_VAR>value</MY_VAR>
      </environmentVariables>
  </configuration>
  ```
- **Arbeitsverzeichnis**: Verwenden Sie `<workingDirectory>`, um festzulegen, wo der Befehl ausgeführt wird.

### Zusammenfassung
Der Exec Maven Plugin ist vielseitig:
- Verwenden Sie `exec:java`, um Java-Klassen aus Ihrem Projekt einfach auszuführen und den Classpath des Projekts zu nutzen, aber es läuft in Mavens JVM.
- Verwenden Sie `exec:exec` für externe Programme oder Java mit benutzerdefinierten JVM-Optionen, was bei Bedarf eine manuelle Classpath-Verwaltung erfordert.
- Konfigurieren Sie es in `pom.xml` und führen Sie es entweder manuell aus (`mvn exec:java` oder `mvn exec:exec`) oder binden Sie es mit `<executions>` an Build-Phasen.

Dieser Aufbau ermöglicht es Ihnen, benutzerdefinierte Ausführungen nahtlos in Ihren Maven Build-Prozess zu integrieren!