---
audio: false
generated: true
lang: fr
layout: post
title: Solutions algorithmiques consolidées dans Maven
translated: true
type: note
---

Pour consolider toutes vos solutions d'algorithmes (`nowcoder`, `uva`, etc.) dans un seul module Maven géré par un fichier `pom.xml` dans le répertoire racine `algorithm-solutions`, nous traiterons l'ensemble du projet comme un seul module. Les fichiers Java de `nowcoder` et `uva` (et d'autres répertoires comme `codeforces`, `hacker_rank`, etc.) seront organisés sous `src/main/java` avec des structures de package appropriées (par exemple, `com.algorithm.solutions.nowcoder`, `com.algorithm.solutions.uva`). Les fichiers d'entrée (par exemple, `1.in`) iront dans `src/main/resources`.

### Hypothèses
- Tous les fichiers Java (par exemple, `nowcoder/Main.java`, `uva/106/src/Main.java`) seront déplacés vers `src/main/java/com/algorithm/solutions/<platform>` (par exemple, `nowcoder`, `uva/p106`).
- Les fichiers d'entrée (par exemple, `uva/106/1.in`) seront déplacés vers `src/main/resources/<platform>` (par exemple, `uva/p106`).
- Le projet utilise Java 17 (ajustable dans le `pom.xml`).
- Le `pom.xml` sera dans le répertoire racine `algorithm-solutions`, et aucun sous-module ne sera utilisé.

### Structure de répertoires
Après réorganisation (en supposant que vous exécutiez le script Python de la réponse précédente pour `uva` et un script similaire pour `nowcoder`), la structure sera :

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
│   │       │   └── (fichiers d'entrée, s'il y en a)
│   │       ├── uva/
│   │       │   ├── p106/
│   │       │   │   └── 1.in
│   │       │   ├── p100/
│   │       │   └── (etc.)
│   │       ├── codeforces/
│   │       └── hacker_rank/
└── README.md
```

### `pom.xml` parent
Ce `pom.xml` va dans le répertoire racine `algorithm-solutions`. Il configure le projet comme un seul module, inclut les ressources pour les fichiers d'entrée et configure le compilateur Maven pour Java 17.

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
    <description>Projet consolidé pour les solutions d'algorithmes de multiples plateformes</description>

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

### Notes sur le `pom.xml`
- **Packaging** : Défini sur `jar` car il s'agit d'un seul module exécutable.
- **Ressources** : Inclut les fichiers `*.in` de `src/main/resources` pour les fichiers d'entrée.
- **Classe principale** : Définie sur `com.algorithm.solutions.nowcoder.Main` par défaut. Comme chaque problème peut avoir sa propre classe `Main`, vous exécuterez généralement des classes spécifiques en utilisant `mvn exec:java`.
- **Version Java** : Utilise Java 17 ; ajustez `<maven.compiler.source>` et `<maven.compiler.target>` si nécessaire.

### Étapes de configuration
1. **Créer la structure de répertoires** :
   ```bash
   mkdir -p src/main/java/com/algorithm/solutions/{nowcoder,uva,codeforces,hacker_rank}
   mkdir -p src/main/resources/{nowcoder,uva,codeforces,hacker_rank}
   ```

2. **Déplacer les fichiers** :
   - Pour `nowcoder` :
     ```bash
     mkdir -p src/main/java/com/algorithm/solutions/nowcoder
     mv nowcoder/*.java src/main/java/com/algorithm/solutions/nowcoder/
     ```
     Ajoutez la déclaration de package à chaque fichier Java (par exemple, `Main.java`) :
     ```java
     package com.algorithm.solutions.nowcoder;
     // ... reste du code ...
     ```
   - Pour `uva`, utilisez le script Python de la réponse précédente, ou manuellement :
     ```bash
     mkdir -p src/main/java/com/algorithm/solutions/uva/p106
     mv uva/106/src/Main.java src/main/java/com/algorithm/solutions/uva/p106/Main.java
     mkdir -p src/main/resources/uva/p106
     mv uva/106/1.in src/main/resources/uva/p106/1.in
     ```
     Ajoutez la déclaration de package à `Main.java` :
     ```java
     package com.algorithm.solutions.uva.p106;
     // ... reste du code ...
     ```
     Répétez pour les autres problèmes UVA (`100`, `10000`, etc.).

3. **Placer le `pom.xml`** :
   - Enregistrez le `pom.xml` ci-dessus dans le répertoire racine `algorithm-solutions`.

4. **Construire le projet** :
   ```bash
   mvn clean install
   ```

5. **Exécuter un programme spécifique** :
   - Pour un problème `nowcoder` :
     ```bash
     mvn exec:java -Dexec.mainClass="com.algorithm.solutions.nowcoder.Main"
     ```
   - Pour un problème UVA (par exemple, problème 106) :
     ```bash
     mvn exec:java -Dexec.mainClass="com.algorithm.solutions.uva.p106.Main"
     ```

### Script Python pour `nowcoder`
Pour compléter le script `uva` précédent, voici un script Python pour déplacer les fichiers `nowcoder` vers `src/main/java/com/algorithm/solutions/nowcoder/` et ajouter les déclarations de package. Exécutez-le depuis le répertoire racine `algorithm-solutions`.

```python
import os
from pathlib import Path

def add_package_declaration(java_file, package):
    """Ajouter une déclaration de package en haut d'un fichier Java si elle n'est pas déjà présente."""
    with open(java_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not content.strip().startswith('package '):
        new_content = f'package {package};\n\n{content}'
        with open(java_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Added package declaration to {java_file}')

def reorganize_nowcoder():
    # Définir les chemins
    nowcoder_root = Path('nowcoder')
    target_dir = Path('src/main/java/com/algorithm/solutions/nowcoder')

    # Créer le répertoire cible
    target_dir.mkdir(parents=True, exist_ok=True)

    if not nowcoder_root.exists():
        print('Error: nowcoder directory not found.')
        return

    # Déplacer les fichiers Java
    for java_file in nowcoder_root.glob('*.java'):
        target_file = target_dir / java_file.name
        shutil.move(str(java_file), str(target_file))
        print(f'Moved {java_file} to {target_file}')
        
        # Ajouter la déclaration de package
        add_package_declaration(target_file, 'com.algorithm.solutions.nowcoder')

    # Supprimer le répertoire nowcoder vide
    if not any(nowcoder_root.iterdir()):
        nowcoder_root.rmdir()
        print(f'Removed empty directory {nowcoder_root}')

if __name__ == '__main__':
    reorganize_nowcoder()
    print('Nowcoder reorganization complete.')
```

### Notes
- **Exécution des scripts** : Exécutez les scripts `reorganize_uva.py` (de la réponse précédente) et `reorganize_nowcoder.py` pour déplacer les fichiers :
  ```bash
  python reorganize_uva.py
  python reorganize_nowcoder.py
  ```
- **Fichiers d'entrée** : Si `nowcoder` a des fichiers d'entrée, modifiez le script pour déplacer les fichiers `*.in` vers `src/main/resources/nowcoder/`.
- **Autres répertoires** : Pour `codeforces`, `hacker_rank`, etc., vous pouvez adapter le script `nowcoder` en changeant le répertoire source et le nom du package.
- **Accès aux ressources** : Mettez à jour votre code Java pour lire les fichiers d'entrée depuis `src/main/resources` (par exemple, `getClass().getResource("/uva/p106/1.in")`).
- **Ignorer les fichiers** : Ajoutez `*.iml` à un fichier `.gitignore` pour exclure les fichiers de projet IntelliJ.

Faites-moi savoir si vous avez besoin de scripts pour d'autres répertoires ou d'ajustements supplémentaires au `pom.xml` !