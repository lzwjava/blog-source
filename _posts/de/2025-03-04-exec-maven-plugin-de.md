---
audio: false
generated: true
lang: de
layout: post
title: Maven Exec Plugin
translated: true
---

Um das `org.codehaus.mojo` Exec Maven Plugin in deinem Maven-Projekt zu verwenden, musst du es in deiner `pom.xml`-Datei konfigurieren und entscheiden, wie du Programme während des Build-Prozesses ausführen möchtest—entweder externe Befehle oder Java-Programme. Das Plugin bietet zwei Hauptziele: `exec:exec` zum Ausführen externer Programme und `exec:java` zum Ausführen von Java-Klassen. Im Folgenden werde ich dich durch die Schritte zur Einrichtung und effektiven Nutzung führen.

### Schritt 1: Plugin zur `pom.xml` hinzufügen
Zunächst fügst du das Exec Maven Plugin im `<build><plugins>`-Bereich deiner `pom.xml` hinzu. Gib die `groupId`, `artifactId` und eine Version an (die neueste Version ist derzeit `3.1.0`):

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

Dies fügt das Plugin zu deinem Projekt hinzu, aber es wird noch nichts tun, bis du es konfigurierst oder seine Ziele manuell ausführst.

### Schritt 2: Ziel auswählen
Das Plugin bietet zwei Hauptziele:
- **`exec:exec`**: Führt jedes externe Programm aus (z.B. Shell-Skripte, Binärdateien oder sogar den `java`-Befehl).
- **`exec:java`**: Führt eine Java-Klasse mit einer `main`-Methode aus deinem Projekt im selben JVM wie Maven aus.

Du kannst diese Ziele entweder manuell von der Befehlszeile ausführen (z.B. `mvn exec:exec`) oder sie an eine bestimmte Phase im Maven-Build-Lebenszyklus binden.

### Option 1: Ausführen eines Java-Programms mit `exec:java`
Wenn du eine Java-Klasse aus deinem Projekt ausführen möchtest, verwende das Ziel `exec:java`. Dies ist ideal, um eine `main`-Methode in einer Klasse auszuführen, die Teil deines Projekts ist, und dabei automatisch die Laufzeit-Klassenpfade des Projekts (einschließlich Abhängigkeiten) zu nutzen.

#### Manuelle Ausführung
Füge eine Konfiguration hinzu, um die Hauptklasse anzugeben:

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

Führe es dann von der Befehlszeile aus:

```bash
mvn exec:java
```

Dies führt `com.example.Main` im selben JVM wie Maven aus und erbt die JVM-Einstellungen von Maven.

#### Automatische Ausführung während des Builds
Um es automatisch während einer Build-Phase (z.B. `test`) auszuführen, verwende den `<executions>`-Bereich:

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

Wenn du nun `mvn test` ausführst, wird die Klasse `com.example.Main` während der `test`-Phase ausgeführt.

#### Übergeben von Argumenten oder Systemeigenschaften
Du kannst Argumente an die `main`-Methode übergeben oder Systemeigenschaften festlegen:

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

Beachte, dass `exec:java` im selben JVM wie Maven ausgeführt wird, sodass JVM-Optionen (z.B. `-Xmx`) von der Art und Weise, wie Maven aufgerufen wird (z.B. `mvn -Xmx512m exec:java`), geerbt werden.

### Option 2: Ausführen eines externen Programms mit `exec:exec`
Zum Ausführen externer Programme wie Shell-Skripte oder Befehle verwende das Ziel `exec:exec`.

#### Manuelle Ausführung
Konfiguriere das Plugin, um ein Skript auszuführen:

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

Führe es mit aus:

```bash
mvn exec:exec
```

Dies führt `myScript.sh` mit den angegebenen Argumenten im angegebenen Arbeitsverzeichnis aus.

#### Automatische Ausführung während des Builds
Binde es an eine Phase, wie z.B. das Starten und Stoppen eines Servers für Integrationstests:

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

Das Ausführen von `mvn integration-test` startet den Server vor den Tests und stoppt ihn danach.

#### Ausführen von Java mit benutzerdefinierten JVM-Optionen
Wenn du einen separaten JVM mit spezifischen Optionen benötigst (im Gegensatz zu `exec:java`), verwende `exec:exec` mit dem `java`-Ausführbaren. Du musst den Klassenpfad manuell verwalten. Hier ist ein Beispiel:

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

Um Abhängigkeiten in den Klassenpfad einzubeziehen, kannst du das `maven-dependency-plugin` verwenden, um ihn zu generieren:

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

Passe den Klassenpfad-Trennzeichen (`:` für Unix, `;` für Windows) nach Bedarf an.

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
- **Arbeitsverzeichnis**: Verwende `<workingDirectory>`, um festzulegen, wo der Befehl ausgeführt wird.

### Zusammenfassung
Das Exec Maven Plugin ist vielseitig:
- Verwende `exec:java`, um Java-Klassen aus deinem Projekt einfach auszuführen und dabei den Klassenpfad des Projekts zu nutzen, aber es wird im JVM von Maven ausgeführt.
- Verwende `exec:exec` für externe Programme oder Java mit benutzerdefinierten JVM-Optionen, wobei eine manuelle Verwaltung des Klassenpfads erforderlich sein kann.
- Konfiguriere es in der `pom.xml` und führe es entweder manuell (`mvn exec:java` oder `mvn exec:exec`) aus oder binde es an Build-Phasen mit `<executions>`.

Diese Einrichtung ermöglicht es dir, benutzerdefinierte Ausführungen nahtlos in deinen Maven-Build-Prozess zu integrieren!