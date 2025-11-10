---
audio: false
generated: true
lang: de
layout: post
title: Repository in Maven-Multi-Module umwandeln
translated: true
type: note
---

Um Ihr `algorithm-solutions`-Repository in ein Multi-Modul-Java-Projekt zu konvertieren, das von Maven verwaltet wird, benötigen Sie eine übergeordnete `pom.xml` im Stammverzeichnis und individuelle `pom.xml`-Dateien für jedes Untermodul (`nowcoder` und `uva`). Die übergeordnete `pom.xml` definiert gemeinsame Konfigurationen und verwaltet die Untermodule, während die `pom.xml` jedes Untermoduls dessen spezifische Einstellungen handhabt.

Im Folgenden stelle ich die `pom.xml`-Dateien für das Elternprojekt und die beiden Untermodule bereit. Ich gehe davon aus:
- Das Projekt verwendet Java 17 (eine gängige Version für moderne Projekte; bei Bedarf anpassen).
- Die Verzeichnisse `nowcoder` und `uva` enthalten Java-Quelldateien in einer standardmäßigen Maven-Struktur (`src/main/java`).
- Derzeit sind keine externen Abhängigkeiten erforderlich, aber die Struktur ermöglicht eine einfache Ergänzung.
- Jedes Untermodul wird als JAR gepackt (da es sich wahrscheinlich um eigenständige Algorithmus-Lösungen handelt).

### Verzeichnisstruktur
Nach dem Einrichten sollte Ihre Verzeichnisstruktur wie folgt aussehen:

```
algorithm-solutions/
├── pom.xml
├── nowcoder/
│   ├── pom.xml
│   └── src/
│       └── main/
│           └── java/
│               └── (Ihre Java-Dateien, z.B. Main.java, nc140, etc.)
├── uva/
│   ├── pom.xml
│   └── src/
│       └── main/
│           └── java/
│               └── (Ihre Java-Dateien, z.B. 100.java, 10000.java, etc.)
└── README.md
```

### Übergeordnete `pom.xml`
Diese Datei kommt in das Stammverzeichnis (`algorithm-solutions/pom.xml`). Sie definiert das Elternprojekt, listet die Untermodule auf und legt gemeinsame Konfigurationen wie die Java-Version und Compiler-Einstellungen fest.

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.algorithm.solutions</groupId>
    <artifactId>algorithm-solutions</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <name>Algorithm Solutions Parent</name>
    <description>Parent project for algorithm solutions</description>

    <modules>
        <module>nowcoder</module>
        <module>uva</module>
    </modules>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.13.0</version>
                <configuration>
                    <source>${maven.compiler.source}</source>
                    <target>${maven.compiler.target}</target>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

### Nowcoder-Untermodul `pom.xml`
Diese Datei kommt in das `nowcoder`-Verzeichnis (`nowcoder/pom.xml`). Sie erbt vom Eltern-Projekt und gibt ihre eigenen Artefakt-Details an.

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.algorithm.solutions</groupId>
        <artifactId>algorithm-solutions</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>nowcoder</artifactId>
    <name>Nowcoder Solutions</name>
    <description>Solutions for Nowcoder algorithm problems</description>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <version>3.4.2</version>
                <configuration>
                    <archive>
                        <manifest>
                            <mainClass>Main</mainClass>
                        </manifest>
                    </archive>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

### UVA-Untermodul `pom.xml`
Diese Datei kommt in das `uva`-Verzeichnis (`uva/pom.xml`). Sie erbt ebenfalls vom Eltern-Projekt und gibt ihre eigenen Artefakt-Details an. Da UVA-Lösungen typischerweise keine einzelne `Main`-Klasse haben (jedes Problem könnte ein eigenständiges Programm sein), werde ich hier keine Hauptklasse angeben, aber Sie können bei Bedarf eine hinzufügen.

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.algorithm.solutions</groupId>
        <artifactId>algorithm-solutions</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>uva</artifactId>
    <name>UVA Solutions</name>
    <description>Solutions for UVA algorithm problems</description>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <version>3.4.2</version>
            </plugin>
        </plugins>
    </build>
</project>
```

### Schritte zur Einrichtung
1. **Maven-Verzeichnisstruktur erstellen**:
   - Verschieben Sie Ihre Java-Dateien in `nowcoder` nach `nowcoder/src/main/java/`.
   - Verschieben Sie Ihre Java-Dateien in `uva` nach `uva/src/main/java/`.
   - Beispiel: `nowcoder/Main.java` sollte in `nowcoder/src/main/java/Main.java` liegen.

2. **Die `pom.xml`-Dateien platzieren**:
   - Platzieren Sie die übergeordnete `pom.xml` im `algorithm-solutions`-Stammverzeichnis.
   - Platzieren Sie die `nowcoder/pom.xml` im `nowcoder`-Verzeichnis.
   - Platzieren Sie die `uva/pom.xml` im `uva`-Verzeichnis.

3. **Das Projekt erstellen**:
   - Navigieren Sie in einem Terminal zum `algorithm-solutions`-Stammverzeichnis.
   - Führen Sie `mvn clean install` aus, um beide Untermodule zu erstellen.

4. **Ein bestimmtes Programm ausführen**:
   - Für `nowcoder`, falls `Main.java` der Einstiegspunkt ist, können Sie es ausführen mit:
     ```bash
     mvn -pl nowcoder exec:java -Dexec.mainClass="Main"
     ```
   - Für UVA-Lösungen, da jede Datei ein eigenständiges Programm sein könnte, können Sie eine bestimmte Klasse (z.B. `100.java`) ausführen mit:
     ```bash
     mvn -pl uva exec:java -Dexec.mainClass="100"
     ```

### Hinweise
- **Java-Version**: Ich habe Java 17 verwendet. Wenn Sie eine andere Version benötigen, aktualisieren Sie die Eigenschaften `<maven.compiler.source>` und `<maven.compiler.target>` in der übergeordneten `pom.xml`.
- **Abhängigkeiten**: Wenn Ihre Lösungen Bibliotheken erfordern (z.B. für Eingabe-/Ausgabe-Hilfsprogramme), fügen Sie diese im Abschnitt `<dependencies>` der `pom.xml` des Untermoduls hinzu.
- **Dateinamen**: Stellen Sie sicher, dass Ihre Java-Dateien den Klassennamen entsprechen (z.B. sollte `100.java` `public class 100` enthalten).
- **Andere Verzeichnisse**: Ihr Repo enthält `codeforces`, `hacker_rank`, etc. Wenn Sie diese als Untermodule einbinden möchten, fügen Sie `<module>codeforces</module>` (usw.) zur übergeordneten `pom.xml` hinzu und erstellen Sie entsprechende `pom.xml`-Dateien in diesen Verzeichnissen, ähnlich wie bei `nowcoder` und `uva`.

Lassen Sie mich wissen, wenn Sie zusätzliche Untermodule oder spezifische Konfigurationen benötigen!