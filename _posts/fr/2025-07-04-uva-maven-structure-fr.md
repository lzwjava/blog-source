---
audio: false
generated: true
lang: fr
layout: post
title: Structure Maven pour les problèmes UVA
translated: true
type: note
---

Merci d'avoir partagé la structure spécifique de votre sous-répertoire `uva/106`. Il semble que votre projet ait une structure plus granulaire où chaque problème UVA (par exemple, `106`) est un répertoire séparé avec son propre dossier `src` contenant un fichier `Main.java` et éventuellement des fichiers d'entrée comme `1.in`. Cela suggère que chaque problème pourrait être traité comme un sous-projet ou module distinct. Pour accommoder cela dans une configuration Maven multi-modules, nous pouvons soit :
1. Traiter chaque répertoire de problème (par exemple, `uva/106`) comme son propre sous-module Maven.
2. Conserver `uva` comme un seul module et organiser les fichiers de problème dans son répertoire `src/main/java`.

Étant donné le nombre de problèmes UVA (comme vu dans votre liste précédente : `100`, `10000`, etc.), créer un module Maven séparé pour chaque problème pourrait conduire à un grand nombre de modules, ce qui pourrait être encombrant. Je propose plutôt une structure où `uva` est un module unique, et chaque `Main.java` de problème est organisé dans `uva/src/main/java` sous une structure de package (par exemple, `com.algorithm.solutions.uva.p106` pour le problème 106). Cela garde le projet gérable tout en conservant les avantages de Maven.

Cependant, je fournirai également une approche alternative où chaque problème est un sous-module séparé si vous préférez cette granularité. Ci-dessous, je mettrai à jour les fichiers `pom.xml` basés sur votre structure et fournirai les étapes pour réorganiser vos fichiers.

---

### Option 1 : Module `uva` unique avec des packages par problème

#### Structure de répertoire mise à jour
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

#### `pom.xml` parent (Racine : `algorithm-solutions/pom.xml`)
Celui-ci reste largement le même qu'avant, définissant `nowcoder` et `uva` comme modules.

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

#### Sous-module Nowcoder `pom.xml` (`nowcoder/pom.xml`)
Celui-ci est inchangé par rapport à la réponse précédente, en supposant que les fichiers `nowcoder` sont déplacés vers `src/main/java/com/algorithm/solutions/nowcoder/`.

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

#### Sous-module UVA `pom.xml` (`uva/pom.xml`)
Ce module inclut un répertoire `resources` pour les fichiers d'entrée comme `1.in`. Les fichiers `Main.java` pour chaque problème sont organisés en packages.

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

#### Organisation des fichiers
- **Déplacer les fichiers Java** :
  - Pour chaque problème (par exemple, `uva/106/src/Main.java`), déplacez `Main.java` vers `uva/src/main/java/com/algorithm/solutions/uva/p106/Main.java`.
  - Mettez à jour le fichier `Main.java` pour inclure la déclaration de package :
    ```java
    package com.algorithm.solutions.uva.p106;
    public class Main {
        // ... code existant ...
    }
    ```
  - Faites cela pour tous les problèmes (par exemple, `p100`, `p10000`, etc.).

- **Déplacer les fichiers d'entrée** :
  - Déplacez les fichiers d'entrée comme `uva/106/1.in` vers `uva/src/main/resources/uva/p106/1.in`.
  - Cela permet à Maven d'inclure ces fichiers dans le JAR, accessibles via `ClassLoader.getResource()` ou similaire dans votre code Java.

#### Exécution d'un programme
Pour exécuter un problème UVA spécifique (par exemple, le problème 106) :
```bash
mvn -pl uva exec:java -Dexec.mainClass="com.algorithm.solutions.uva.p106.Main"
```

---

### Option 2 : Chaque problème UVA comme sous-module
Si vous préférez que chaque problème UVA (par exemple, `106`, `100`) soit son propre module Maven, voici comment le configurer. C'est plus granulaire mais augmente le nombre de fichiers `pom.xml`.

#### Structure de répertoire mise à jour
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
│   │       └── (fichiers d'entrée, s'il y en a)
│   └── (autres répertoires de problèmes)
└── README.md
```

#### `pom.xml` parent (Racine : `algorithm-solutions/pom.xml`)
Ajoutez chaque problème comme module.

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

#### Sous-module Nowcoder `pom.xml` (`nowcoder/pom.xml`)
Identique à ci-dessus (inchangé).

#### Sous-module UVA Problème 106 `pom.xml` (`uva/106/pom.xml`)
Chaque problème a son propre `pom.xml`. Voici un exemple pour `uva/106` :

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

- **Répéter pour les autres problèmes** : Créez des fichiers `pom.xml` similaires pour `uva/100`, `uva/10000`, etc., en ajustant l'`artifactId` (par exemple, `uva-100`), le `name`, et le `mainClass` (par exemple, `com.algorithm.solutions.uva.p100.Main`).

#### Organisation des fichiers
- **Déplacer les fichiers Java** :
  - Pour `uva/106/src/Main.java`, déplacez vers `uva/106/src/main/java/com/algorithm/solutions/uva/p106/Main.java`.
  - Ajoutez la déclaration de package :
    ```java
    package com.algorithm.solutions.uva.p106;
    public class Main {
        // ... code existant ...
    }
    ```
- **Déplacer les fichiers d'entrée** :
  - Déplacez `uva/106/1.in` vers `uva/106/resources/1.in`.

#### Exécution d'un programme
Pour exécuter le problème 106 :
```bash
mvn -pl uva/106 exec:java -Dexec.mainClass="com.algorithm.solutions.uva.p106.Main"
```

---

### Recommandation
- **Option 1 (Module `uva` unique)** est plus simple et plus évolutive, surtout si vous avez beaucoup de problèmes UVA. Elle évite de créer de nombreux fichiers `pom.xml` et garde la structure du projet propre. Utilisez des packages pour organiser les problèmes logiquement.
- **Option 2 (Modules par problème)** est meilleure si vous voulez que chaque problème soit complètement indépendant (par exemple, pour un déploiement ou des tests séparés). Cependant, elle nécessite plus de maintenance en raison du nombre de modules.

### Étapes pour mettre en œuvre l'Option 1
1. **Créer la structure de répertoire** :
   - Exécutez ces commandes à la racine de `algorithm-solutions` :
     ```bash
     mkdir -p uva/src/main/java/com/algorithm/solutions/uva
     mkdir -p uva/src/main/resources/uva
     mkdir -p nowcoder/src/main/java/com/algorithm/solutions/nowcoder
     ```
2. **Déplacer les fichiers** :
   - Pour chaque problème UVA (par exemple, `106`) :
     ```bash
     mkdir -p uva/src/main/java/com/algorithm/solutions/uva/p106
     mv uva/106/src/Main.java uva/src/main/java/com/algorithm/solutions/uva/p106/Main.java
     mkdir -p uva/src/main/resources/uva/p106
     mv uva/106/1.in uva/src/main/resources/uva/p106/1.in
     ```
   - Pour `nowcoder` :
     ```bash
     mv nowcoder/*.java nowcoder/src/main/java/com/algorithm/solutions/nowcoder/
     ```
3. **Mettre à jour les fichiers Java** :
   - Ajoutez les déclarations de package appropriées (par exemple, `package com.algorithm.solutions.uva.p106;` pour `uva/106/Main.java`).
4. **Ajouter les fichiers `pom.xml`** :
   - Placez le `pom.xml` parent dans `algorithm-solutions/`.
   - Placez les `nowcoder/pom.xml` et `uva/pom.xml` comme indiqué.
5. **Construire** :
   ```bash
   mvn clean install
   ```

### Notes
- **Fichiers d'entrée** : Si votre `Main.java` lit des fichiers d'entrée comme `1.in`, mettez à jour le code pour y accéder via `getClass().getResource("/uva/p106/1.in")` ou similaire, car ils sont maintenant dans `src/main/resources`.
- **Ignorer les fichiers `.iml`** : Ajoutez un fichier `.gitignore` avec `*.iml` pour exclure les fichiers de projet IntelliJ du contrôle de version.
- **Autres répertoires** : Pour `codeforces`, `hacker_rank`, etc., vous pouvez créer des modules similaires quand vous serez prêt. Faites-moi savoir si vous avez besoin de fichiers `pom.xml` pour ceux-ci.
- **Version Java** : Ajustez `<maven.compiler.source>` et `<maven.compiler.target>` si vous utilisez une version Java différente.

Si vous préférez l'Option 2 ou avez besoin d'aide pour des problèmes spécifiques (par exemple, ajuster `Main.java` pour le chargement des ressources), faites-le-moi savoir !