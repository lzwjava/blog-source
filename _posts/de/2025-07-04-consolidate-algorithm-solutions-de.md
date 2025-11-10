---
audio: false
generated: true
lang: de
layout: post
title: Konsolidierte Algorithmuslösungen in Maven
translated: true
type: note
---

Um alle Ihre Algorithmus-Lösungen (`nowcoder`, `uva` usw.) in einem einzigen Maven-Modul zu konsolidieren, das durch eine `pom.xml`-Datei im `algorithm-solutions`-Stammverzeichnis verwaltet wird, behandeln wir das gesamte Projekt als ein Modul. Die Java-Dateien aus `nowcoder` und `uva` (und anderen Verzeichnissen wie `codeforces`, `hacker_rank` usw.) werden unter `src/main/java` mit entsprechenden Paketstrukturen organisiert (z.B. `com.algorithm.solutions.nowcoder`, `com.algorithm.solutions.uva`). Eingabedateien (z.B. `1.in`) kommen in `src/main/resources`.

### Annahmen
- Alle Java-Dateien (z.B. `nowcoder/Main.java`, `uva/106/src/Main.java`) werden nach `src/main/java/com/algorithm/solutions/<Plattform>` verschoben (z.B. `nowcoder`, `uva/p106`).
- Eingabedateien (z.B. `uva/106/1.in`) werden nach `src/main/resources/<Plattform>` verschoben (z.B. `uva/p106`).
- Das Projekt verwendet Java 17 (in der `pom.xml` anpassbar).
- Die `pom.xml` befindet sich im `algorithm-solutions`-Stammverzeichnis, und es werden keine Untermodule verwendet.

### Verzeichnisstruktur
Nach der Reorganisation (unter der Annahme, dass Sie das Python-Skript aus der vorherigen Antwort für `uva` und ein ähnliches für `nowcoder` ausführen), sieht die Struktur wie folgt aus:

```
algorithm-solutions/
├── pom.xml
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/algorithm/solutions/
│   │   │       ├── nowcoder/
│   │   │       │   ├── Main.java
│   │   │       │   ├── nc140.java
│   │   │       │   ├── nc45.java
│   │   │       │   ├── nc78.java
│   │   │       │   └── nc93.java
│   │   │       ├── uva/
│   │   │       │   ├── p100/
│   │   │       │   │   └── Main.java
│   │   │       │   ├── p106/
│   │   │       │   │   └── Main.java
│   │   │       │   ├── p10000/
│   │   │       │   │   └── Main.java
│   │   │       │   └── (etc.)
│   │   │       ├── codeforces/
│   │   │       └── hacker_rank/
│   │   └── resources/
│   │       ├── nowcoder/
│   │       │   └── (Eingabedateien, falls vorhanden)
│   │       ├── uva/
│   │       │   ├── p106/
│   │       │   │   └── 1.in
│   │       │   ├── p100/
│   │       │   └── (etc.)
│   │       ├── codeforces/
│   │       └── hacker_rank/
└── README.md
```

### Übergeordnete `pom.xml`
Diese `pom.xml` kommt in das `algorithm-solutions`-Stammverzeichnis. Sie konfiguriert das Projekt als ein einzelnes Modul, bindet Ressourcen für Eingabedateien ein und richtet den Maven-Compiler für Java 17 ein.

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.algorithm.solutions</groupId>
    <artifactId>algorithm-solutions</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <name>Algorithm Solutions</name>
    <description>Konsolidiertes Projekt für Algorithmus-Lösungen von mehreren Plattformen</description>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

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
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.13.0</version>
                <configuration>
                    <source>${maven.compiler.source}</source>
                    <target>${maven.compiler.target}</target>
                </configuration>
            </plugin>
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

### Anmerkungen zur `pom.xml`
- **Packaging**: Auf `jar` gesetzt, da es sich um ein einziges ausführbares Modul handelt.
- **Ressourcen**: Bindet `*.in`-Dateien aus `src/main/resources` für Eingabedateien ein.
- **Hauptklasse**: Auf `com.algorithm.solutions.nowcoder.Main` als Standard gesetzt. Da jedes Problem seine eigene `Main`-Klasse haben kann, werden Sie typischerweise spezifische Klassen mit `mvn exec:java` ausführen.
- **Java-Version**: Verwendet Java 17; passen Sie `<maven.compiler.source>` und `<maven.compiler.target>` bei Bedarf an.

### Schritte zur Einrichtung
1. **Verzeichnisstruktur erstellen**:
   ```bash
   mkdir -p src/main/java/com/algorithm/solutions/{nowcoder,uva,codeforces,hacker_rank}
   mkdir -p src/main/resources/{nowcoder,uva,codeforces,hacker_rank}
   ```

2. **Dateien verschieben**:
   - Für `nowcoder`:
     ```bash
     mkdir -p src/main/java/com/algorithm/solutions/nowcoder
     mv nowcoder/*.java src/main/java/com/algorithm/solutions/nowcoder/
     ```
     Fügen Sie jede Java-Datei eine Paketdeklaration hinzu (z.B. `Main.java`):
     ```java
     package com.algorithm.solutions.nowcoder;
     // ... rest of the code ...
     ```
   - Für `uva`, verwenden Sie das Python-Skript aus der vorherigen Antwort, oder manuell:
     ```bash
     mkdir -p src/main/java/com/algorithm/solutions/uva/p106
     mv uva/106/src/Main.java src/main/java/com/algorithm/solutions/uva/p106/Main.java
     mkdir -p src/main/resources/uva/p106
     mv uva/106/1.in src/main/resources/uva/p106/1.in
     ```
     Fügen Sie `Main.java` eine Paketdeklaration hinzu:
     ```java
     package com.algorithm.solutions.uva.p106;
     // ... rest of the code ...
     ```
     Wiederholen Sie dies für andere UVA-Probleme (`100`, `10000` usw.).

3. **Die `pom.xml` platzieren**:
   - Speichern Sie die obige `pom.xml` im `algorithm-solutions`-Stammverzeichnis.

4. **Das Projekt bauen**:
   ```bash
   mvn clean install
   ```

5. **Ein bestimmtes Programm ausführen**:
   - Für ein `nowcoder`-Problem:
     ```bash
     mvn exec:java -Dexec.mainClass="com.algorithm.solutions.nowcoder.Main"
     ```
   - Für ein UVA-Problem (z.B. Problem 106):
     ```bash
     mvn exec:java -Dexec.mainClass="com.algorithm.solutions.uva.p106.Main"
     ```

### Python-Skript für `nowcoder`
Als Ergänzung zum vorherigen `uva`-Skript, hier ein Python-Skript, um `nowcoder`-Dateien nach `src/main/java/com/algorithm/solutions/nowcoder/` zu verschieben und Paketdeklarationen hinzuzufügen. Führen Sie dies aus dem `algorithm-solutions`-Stammverzeichnis aus.

```python
import os
from pathlib import Path

def add_package_declaration(java_file, package):
    """Add package declaration to the top of a Java file if not already present."""
    with open(java_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not content.strip().startswith('package '):
        new_content = f'package {package};\n\n{content}'
        with open(java_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Added package declaration to {java_file}')

def reorganize_nowcoder():
    # Define paths
    nowcoder_root = Path('nowcoder')
    target_dir = Path('src/main/java/com/algorithm/solutions/nowcoder')

    # Create target directory
    target_dir.mkdir(parents=True, exist_ok=True)

    if not nowcoder_root.exists():
        print('Error: nowcoder directory not found.')
        return

    # Move Java files
    for java_file in nowcoder_root.glob('*.java'):
        target_file = target_dir / java_file.name
        shutil.move(str(java_file), str(target_file))
        print(f'Moved {java_file} to {target_file}')
        
        # Add package declaration
        add_package_declaration(target_file, 'com.algorithm.solutions.nowcoder')

    # Remove empty nowcoder directory
    if not any(nowcoder_root.iterdir()):
        nowcoder_root.rmdir()
        print(f'Removed empty directory {nowcoder_root}')

if __name__ == '__main__':
    reorganize_nowcoder()
    print('Nowcoder reorganization complete.')
```

### Anmerkungen
- **Skripte ausführen**: Führen Sie die Skripte `reorganize_uva.py` (aus der vorherigen Antwort) und `reorganize_nowcoder.py` aus, um Dateien zu verschieben:
  ```bash
  python reorganize_uva.py
  python reorganize_nowcoder.py
  ```
- **Eingabedateien**: Wenn `nowcoder` Eingabedateien hat, modifizieren Sie das Skript, um `*.in`-Dateien nach `src/main/resources/nowcoder/` zu verschieben.
- **Andere Verzeichnisse**: Für `codeforces`, `hacker_rank` usw. können Sie das `nowcoder`-Skript anpassen, indem Sie das Quellverzeichnis und den Paketnamen ändern.
- **Ressourcenzugriff**: Aktualisieren Sie Ihren Java-Code, um Eingabedateien aus `src/main/resources` zu lesen (z.B. `getClass().getResource("/uva/p106/1.in")`).
- **Dateien ignorieren**: Fügen Sie `*.iml` zu einer `.gitignore`-Datei hinzu, um IntelliJ-Projektdateien auszuschließen.

Lassen Sie mich wissen, wenn Sie Skripte für andere Verzeichnisse benötigen oder weitere Anpassungen an der `pom.xml`!