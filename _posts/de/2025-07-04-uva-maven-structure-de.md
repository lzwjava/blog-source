---
audio: false
generated: true
lang: de
layout: post
title: Maven-Struktur für UVA-Probleme
translated: true
type: note
---

Danke, dass Sie die spezifische Verzeichnisstruktur für Ihr `uva/106`-Unterverzeichnis geteilt haben. Es scheint, dass Ihr Projekt eine granularere Struktur hat, bei der jedes UVA-Problem (z.B. `106`) ein separates Verzeichnis mit seinem eigenen `src`-Ordner ist, der eine `Main.java`-Datei und möglicherweise Eingabedateien wie `1.in` enthält. Dies deutet darauf hin, dass jedes Problem möglicherweise als separates Unterprojekt oder Modul behandelt wird. Um dies in einem Maven-Multi-Module-Setup unterzubringen, können wir entweder:
1. Jedes Problemverzeichnis (z.B. `uva/106`) als eigenes Maven-Submodul behandeln.
2. `uva` als ein einzelnes Modul beibehalten und die Problemdateien innerhalb seines `src/main/java`-Verzeichnisses organisieren.

Angesichts der Anzahl der UVA-Probleme (wie in Ihrer früheren Liste zu sehen: `100`, `10000`, etc.) könnte die Erstellung eines separaten Maven-Moduls für jedes Problem zu einer großen Anzahl von Modulen führen, was umständlich sein könnte. Stattdessen schlage ich eine Struktur vor, bei der `uva` ein einzelnes Modul ist und die `Main.java` jedes Problems innerhalb von `uva/src/main/java` unter einer Paketstruktur (z.B. `com.algorithm.solutions.uva.p106` für Problem 106) organisiert wird. Dies hält das Projekt handhabbar und bewahrt gleichzeitig die Vorteile von Maven.

Ich werde jedoch auch einen alternativen Ansatz bereitstellen, bei dem jedes Problem ein separates Submodul ist, falls Sie diese Granularität bevorzugen. Im Folgenden werde ich die `pom.xml`-Dateien basierend auf Ihrer Struktur aktualisieren und Schritte zur Neuorganisation Ihrer Dateien bereitstellen.

---

### Option 1: Einzelnes `uva`-Modul mit Problem-Paketen

#### Aktualisierte Verzeichnisstruktur
```
algorithm-solutions/
├── pom.xml
├── nowcoder/
│   ├── pom.xml
│   └── src/
│       └── main/
│           └── java/
│               └── com/algorithm/solutions/nowcoder/
│                   ├── Main.java
│                   ├── nc140.java
│                   ├── nc45.java
│                   ├── nc78.java
│                   └── nc93.java
├── uva/
│   ├── pom.xml
│   ├── src/
│   │   └── main/
│   │       └── java/
│   │           └── com/algorithm/solutions/uva/
│   │               ├── p100/
│   │               │   └── Main.java
│   │               ├── p106/
│   │               │   └── Main.java
│   │               ├── p10000/
│   │               │   └── Main.java
│   │               └── (etc.)
│   └── resources/
│       └── uva/
│           ├── p100/
│           │   └── 1.in
│           ├── p106/
│           │   └── 1.in
│           └── (etc.)
└── README.md
```

#### Eltern-`pom.xml` (Stammverzeichnis: `algorithm-solutions/pom.xml`)
Dies bleibt weitgehend unverändert gegenüber vorher und definiert `nowcoder` und `uva` als Module.

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

#### Nowcoder-Submodul `pom.xml` (`nowcoder/pom.xml`)
Dies ist unverändert gegenüber der vorherigen Antwort, unter der Annahme, dass `nowcoder`-Dateien nach `src/main/java/com/algorithm/solutions/nowcoder/` verschoben wurden.

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
                            <mainClass>com.algorithm.solutions.nowcoder.Main</mainClass>
                        </manifest>
                    </archive>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

#### UVA-Submodul `pom.xml` (`uva/pom.xml`)
Dieses Modul enthält ein `resources`-Verzeichnis für Eingabedateien wie `1.in`. Die `Main.java`-Dateien für jedes Problem sind in Paketen organisiert.

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
        <resources>
            <resource>
                <directory>src/main/resources</directory>
                <includes>
                    <include>**/*.in</include>
                </includes>
            </resource>
        </resources>
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

#### Dateiorganisation
- **Java-Dateien verschieben**:
  - Für jedes Problem (z.B. `uva/106/src/Main.java`), verschieben Sie `Main.java` nach `uva/src/main/java/com/algorithm/solutions/uva/p106/Main.java`.
  - Aktualisieren Sie die `Main.java`-Datei, um die Paketdeklaration einzufügen:
    ```java
    package com.algorithm.solutions.uva.p106;
    public class Main {
        // ... existing code ...
    }
    ```
  - Führen Sie dies für alle Probleme durch (z.B. `p100`, `p10000`, etc.).

- **Eingabedateien verschieben**:
  - Verschieben Sie Eingabedateien wie `uva/106/1.in` nach `uva/src/main/resources/uva/p106/1.in`.
  - Dies ermöglicht es Maven, diese Dateien in das JAR aufzunehmen, auf das über `ClassLoader.getResource()` oder ähnliches in Ihrem Java-Code zugegriffen werden kann.

#### Ausführen eines Programms
Um ein bestimmtes UVA-Problem auszuführen (z.B. Problem 106):
```bash
mvn -pl uva exec:java -Dexec.mainClass="com.algorithm.solutions.uva.p106.Main"
```

---

### Option 2: Jedes UVA-Problem als Submodul
Wenn Sie bevorzugen, dass jedes UVA-Problem (z.B. `106`, `100`) sein eigenes Maven-Modul ist, hier ist die Einrichtung. Dies ist granularer, erhöht aber die Anzahl der `pom.xml`-Dateien.

#### Aktualisierte Verzeichnisstruktur
```
algorithm-solutions/
├── pom.xml
├── nowcoder/
│   ├── pom.xml
│   └── src/
│       └── main/
│           └── java/
│               └── com/algorithm/solutions/nowcoder/
│                   ├── Main.java
│                   ├── nc140.java
│                   ├── nc45.java
│                   ├── nc78.java
│                   └── nc93.java
├── uva/
│   ├── 106/
│   │   ├── pom.xml
│   │   ├── src/
│   │   │   └── main/
│   │   │       └── java/
│   │   │           └── com/algorithm/solutions/uva/p106/
│   │   │               └── Main.java
│   │   └── resources/
│   │       └── 1.in
│   ├── 100/
│   │   ├── pom.xml
│   │   ├── src/
│   │   │   └── main/
│   │   │       └── java/
│   │   │           └── com/algorithm/solutions/uva/p100/
│   │   │               └── Main.java
│   │   └── resources/
│   │       └── (input files, if any)
│   └── (other problem directories)
└── README.md
```

#### Eltern-`pom.xml` (Stammverzeichnis: `algorithm-solutions/pom.xml`)
Fügen Sie jedes Problem als Modul hinzu.

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
        <module>uva/106</module>
        <module>uva/100</module>
        <module>uva/10000</module>
        <module>uva/10006</module>
        <module>uva/10008</module>
        <module>uva/10009</module>
        <module>uva/10012</module>
        <module>uva/10013</module>
        <module>uva/10018</module>
        <module>uva/10019</module>
        <module>uva/10026</module>
        <module>uva/10033</module>
        <module>uva/10034</module>
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

#### Nowcoder-Submodul `pom.xml` (`nowcoder/pom.xml`)
Wie oben (unverändert).

#### UVA-Problem 106 Submodul `pom.xml` (`uva/106/pom.xml`)
Jedes Problem hat seine eigene `pom.xml`. Hier ist ein Beispiel für `uva/106`:

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

    <artifactId>uva-106</artifactId>
    <name>UVA Problem 106</name>
    <description>Solution for UVA problem 106</description>

    <build>
        <resources>
            <resource>
                <directory>resources</directory>
                <includes>
                    <include>**/*.in</include>
                </includes>
            </resource>
        </resources>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <version>3.4.2</version>
                <configuration>
                    <archive>
                        <manifest>
                            <mainClass>com.algorithm.solutions.uva.p106.Main</mainClass>
                        </manifest>
                    </archive>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

- **Für andere Probleme wiederholen**: Erstellen Sie ähnliche `pom.xml`-Dateien für `uva/100`, `uva/10000`, etc., passen Sie dabei die `artifactId` (z.B. `uva-100`), `name` und `mainClass` (z.B. `com.algorithm.solutions.uva.p100.Main`) an.

#### Dateiorganisation
- **Java-Dateien verschieben**:
  - Für `uva/106/src/Main.java`, verschieben nach `uva/106/src/main/java/com/algorithm/solutions/uva/p106/Main.java`.
  - Paketdeklaration hinzufügen:
    ```java
    package com.algorithm.solutions.uva.p106;
    public class Main {
        // ... existing code ...
    }
    ```
- **Eingabedateien verschieben**:
  - Verschieben Sie `uva/106/1.in` nach `uva/106/resources/1.in`.

#### Ausführen eines Programms
Um Problem 106 auszuführen:
```bash
mvn -pl uva/106 exec:java -Dexec.mainClass="com.algorithm.solutions.uva.p106.Main"
```

---

### Empfehlung
- **Option 1 (Einzelnes `uva`-Modul)** ist einfacher und besser skalierbar, insbesondere wenn Sie viele UVA-Probleme haben. Es vermeidet die Erstellung zahlreicher `pom.xml`-Dateien und hält die Projektstruktur sauber. Verwenden Sie Pakete, um Probleme logisch zu organisieren.
- **Option 2 (Pro-Problem-Module)** ist besser, wenn Sie möchten, dass jedes Problem vollständig unabhängig ist (z.B. für separate Bereitstellung oder Tests). Es erfordert jedoch mehr Wartungsaufwand aufgrund der Anzahl der Module.

### Schritte zur Implementierung von Option 1
1. **Verzeichnisstruktur erstellen**:
   - Führen Sie diese Befehle im Stammverzeichnis `algorithm-solutions` aus:
     ```bash
     mkdir -p uva/src/main/java/com/algorithm/solutions/uva
     mkdir -p uva/src/main/resources/uva
     mkdir -p nowcoder/src/main/java/com/algorithm/solutions/nowcoder
     ```
2. **Dateien verschieben**:
   - Für jedes UVA-Problem (z.B. `106`):
     ```bash
     mkdir -p uva/src/main/java/com/algorithm/solutions/uva/p106
     mv uva/106/src/Main.java uva/src/main/java/com/algorithm/solutions/uva/p106/Main.java
     mkdir -p uva/src/main/resources/uva/p106
     mv uva/106/1.in uva/src/main/resources/uva/p106/1.in
     ```
   - Für `nowcoder`:
     ```bash
     mv nowcoder/*.java nowcoder/src/main/java/com/algorithm/solutions/nowcoder/
     ```
3. **Java-Dateien aktualisieren**:
   - Fügen Sie entsprechende Paketdeklarationen hinzu (z.B. `package com.algorithm.solutions.uva.p106;` für `uva/106/Main.java`).
4. **`pom.xml`-Dateien hinzufügen**:
   - Platzieren Sie die Eltern-`pom.xml` in `algorithm-solutions/`.
   - Platzieren Sie die `nowcoder/pom.xml` und `uva/pom.xml` wie gezeigt.
5. **Build**:
   ```bash
   mvn clean install
   ```

### Hinweise
- **Eingabedateien**: Wenn Ihre `Main.java` Eingabedateien wie `1.in` liest, aktualisieren Sie den Code, um über `getClass().getResource("/uva/p106/1.in")` oder ähnliches darauf zuzugreifen, da sie sich jetzt in `src/main/resources` befinden.
- **Ignorieren von `.iml`-Dateien**: Fügen Sie eine `.gitignore`-Datei mit `*.iml` hinzu, um IntelliJ-Projektdateien von der Versionskontrolle auszuschließen.
- **Andere Verzeichnisse**: Für `codeforces`, `hacker_rank`, etc. können Sie ähnliche Module erstellen, wenn Sie bereit sind. Lassen Sie mich wissen, wenn Sie `pom.xml`-Dateien dafür benötigen.
- **Java-Version**: Passen Sie `<maven.compiler.source>` und `<maven.compiler.target>` an, wenn Sie eine andere Java-Version verwenden.

Wenn Sie Option 2 bevorzugen oder Hilfe bei spezifischen Problemen benötigen (z.B. Anpassen von `Main.java` für Ressourcenladen), lassen Sie es mich wissen!