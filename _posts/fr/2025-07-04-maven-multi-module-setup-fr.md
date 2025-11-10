---
audio: false
generated: true
lang: fr
layout: post
title: Convertir le dépôt en projet Maven multi-module
translated: true
type: note
---

Pour convertir votre dépôt `algorithm-solutions` en un projet Java multi-module géré par Maven, vous aurez besoin d'un `pom.xml` parent dans le répertoire racine et de fichiers `pom.xml` individuels pour chaque sous-module (`nowcoder` et `uva`). Le `pom.xml` parent définira les configurations communes et gérera les sous-modules, tandis que le `pom.xml` de chaque sous-module gérera ses paramètres spécifiques.

Ci-dessous, je fournirai les fichiers `pom.xml` pour le projet parent et les deux sous-modules. Je suppose :
- Le projet utilise Java 17 (une version courante pour les projets modernes ; ajustez si nécessaire).
- Les répertoires `nowcoder` et `uva` contiennent des fichiers source Java dans une structure Maven standard (`src/main/java`).
- Aucune dépendance externe n'est requise pour l'instant, mais la structure permet une ajout facile.
- Chaque sous-module sera empaqueté en tant que JAR (puisqu'il s'agit probablement de solutions d'algorithmes autonomes).

### Structure de répertoires
Après la configuration, votre structure de répertoires devrait ressembler à ceci :

```
algorithm-solutions/
├── pom.xml
├── nowcoder/
│   ├── pom.xml
│   └── src/
│       └── main/
│           └── java/
│               └── (vos fichiers Java, par ex. Main.java, nc140, etc.)
├── uva/
│   ├── pom.xml
│   └── src/
│       └── main/
│           └── java/
│               └── (vos fichiers Java, par ex. 100.java, 10000.java, etc.)
└── README.md
```

### `pom.xml` Parent
Ce fichier se place dans le répertoire racine (`algorithm-solutions/pom.xml`). Il définit le projet parent, liste les sous-modules et définit les configurations communes comme la version de Java et les paramètres du compilateur.

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

### `pom.xml` du Sous-module Nowcoder
Ce fichier se place dans le répertoire `nowcoder` (`nowcoder/pom.xml`). Il hérite du parent et spécifie ses propres détails d'artefact.

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

### `pom.xml` du Sous-module UVA
Ce fichier se place dans le répertoire `uva` (`uva/pom.xml`). Il hérite également du parent et spécifie ses propres détails d'artefact. Comme les solutions UVA n'ont généralement pas une seule classe `Main` (chaque problème peut être un programme autonome), je ne spécifierai pas de classe principale ici, mais vous pouvez en ajouter une si nécessaire.

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

### Étapes de configuration
1. **Créer la structure de répertoires Maven** :
   - Déplacez vos fichiers Java dans `nowcoder` vers `nowcoder/src/main/java/`.
   - Déplacez vos fichiers Java dans `uva` vers `uva/src/main/java/`.
   - Par exemple, `nowcoder/Main.java` devrait se trouver dans `nowcoder/src/main/java/Main.java`.

2. **Placer les fichiers `pom.xml`** :
   - Placez le `pom.xml` parent dans le répertoire racine `algorithm-solutions`.
   - Placez le `nowcoder/pom.xml` dans le répertoire `nowcoder`.
   - Placez le `uva/pom.xml` dans le répertoire `uva`.

3. **Construire le projet** :
   - Naviguez vers le répertoire racine `algorithm-solutions` dans un terminal.
   - Exécutez `mvn clean install` pour construire les deux sous-modules.

4. **Exécuter un programme spécifique** :
   - Pour `nowcoder`, si `Main.java` est le point d'entrée, vous pouvez l'exécuter avec :
     ```bash
     mvn -pl nowcoder exec:java -Dexec.mainClass="Main"
     ```
   - Pour les solutions UVA, comme chaque fichier peut être un programme autonome, vous pouvez exécuter une classe spécifique (par ex. `100.java`) avec :
     ```bash
     mvn -pl uva exec:java -Dexec.mainClass="100"
     ```

### Notes
- **Version de Java** : J'ai utilisé Java 17. Si vous avez besoin d'une version différente, mettez à jour les propriétés `<maven.compiler.source>` et `<maven.compiler.target>` dans le `pom.xml` parent.
- **Dépendances** : Si vos solutions nécessitent des bibliothèques (par ex. pour des utilitaires d'entrée/sortie), ajoutez-les dans la section `<dependencies>` du `pom.xml` du sous-module.
- **Nommage des fichiers** : Assurez-vous que vos fichiers Java correspondent aux noms de classe (par ex. `100.java` devrait contenir `public class 100`).
- **Autres répertoires** : Votre dépôt inclut `codeforces`, `hacker_rank`, etc. Si vous souhaitez les inclure en tant que sous-modules, ajoutez `<module>codeforces</module>` (etc.) au `pom.xml` parent et créez les fichiers `pom.xml` correspondants dans ces répertoires, similaires à `nowcoder` et `uva`.

Faites-moi savoir si vous avez besoin de sous-modules supplémentaires ou de configurations spécifiques !