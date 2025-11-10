---
audio: false
generated: true
lang: es
layout: post
title: Soluciones de Algoritmo Consolidadas en Maven
translated: true
type: note
---

Para consolidar todas tus soluciones de algoritmos (`nowcoder`, `uva`, etc.) en un único módulo Maven gestionado por un archivo `pom.xml` en el directorio raíz `algorithm-solutions`, trataremos el proyecto completo como un módulo. Los archivos Java de `nowcoder` y `uva` (y otros directorios como `codeforces`, `hacker_rank`, etc.) se organizarán bajo `src/main/java` con estructuras de paquetes apropiadas (por ejemplo, `com.algorithm.solutions.nowcoder`, `com.algorithm.solutions.uva`). Los archivos de entrada (por ejemplo, `1.in`) irán en `src/main/resources`.

### Suposiciones
- Todos los archivos Java (por ejemplo, `nowcoder/Main.java`, `uva/106/src/Main.java`) se moverán a `src/main/java/com/algorithm/solutions/<plataforma>` (por ejemplo, `nowcoder`, `uva/p106`).
- Los archivos de entrada (por ejemplo, `uva/106/1.in`) se moverán a `src/main/resources/<plataforma>` (por ejemplo, `uva/p106`).
- El proyecto usa Java 17 (ajustable en el `pom.xml`).
- El `pom.xml` estará en el directorio raíz `algorithm-solutions`, y no se usarán submódulos.

### Estructura de Directorios
Después de la reorganización (asumiendo que ejecutas el script de Python de la respuesta anterior para `uva` y uno similar para `nowcoder`), la estructura será:

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
│   │       │   └── (archivos de entrada, si los hay)
│   │       ├── uva/
│   │       │   ├── p106/
│   │       │   │   └── 1.in
│   │       │   ├── p100/
│   │       │   └── (etc.)
│   │       ├── codeforces/
│   │       └── hacker_rank/
└── README.md
```

### `pom.xml` Padre
Este `pom.xml` va en el directorio raíz `algorithm-solutions`. Configura el proyecto como un módulo único, incluye recursos para los archivos de entrada y configura el compilador de Maven para Java 17.

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
    <description>Proyecto consolidado para soluciones de algoritmos de múltiples plataformas</description>

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

### Notas sobre el `pom.xml`
- **Empaquetado**: Configurado como `jar` ya que es un módulo ejecutable único.
- **Recursos**: Incluye archivos `*.in` de `src/main/resources` para los archivos de entrada.
- **Clase Principal**: Configurada como `com.algorithm.solutions.nowcoder.Main` por defecto. Dado que cada problema puede tener su propia clase `Main`, normalmente ejecutarás clases específicas usando `mvn exec:java`.
- **Versión de Java**: Usa Java 17; ajusta `<maven.compiler.source>` y `<maven.compiler.target>` si es necesario.

### Pasos para Configurar
1. **Crear la Estructura de Directorios**:
   ```bash
   mkdir -p src/main/java/com/algorithm/solutions/{nowcoder,uva,codeforces,hacker_rank}
   mkdir -p src/main/resources/{nowcoder,uva,codeforces,hacker_rank}
   ```

2. **Mover Archivos**:
   - Para `nowcoder`:
     ```bash
     mkdir -p src/main/java/com/algorithm/solutions/nowcoder
     mv nowcoder/*.java src/main/java/com/algorithm/solutions/nowcoder/
     ```
     Añade la declaración del paquete a cada archivo Java (por ejemplo, `Main.java`):
     ```java
     package com.algorithm.solutions.nowcoder;
     // ... resto del código ...
     ```
   - Para `uva`, usa el script de Python de la respuesta anterior, o manualmente:
     ```bash
     mkdir -p src/main/java/com/algorithm/solutions/uva/p106
     mv uva/106/src/Main.java src/main/java/com/algorithm/solutions/uva/p106/Main.java
     mkdir -p src/main/resources/uva/p106
     mv uva/106/1.in src/main/resources/uva/p106/1.in
     ```
     Añade la declaración del paquete a `Main.java`:
     ```java
     package com.algorithm.solutions.uva.p106;
     // ... resto del código ...
     ```
     Repite para otros problemas de UVA (`100`, `10000`, etc.).

3. **Colocar el `pom.xml`**:
   - Guarda el `pom.xml` anterior en el directorio raíz `algorithm-solutions`.

4. **Compilar el Proyecto**:
   ```bash
   mvn clean install
   ```

5. **Ejecutar un Programa Específico**:
   - Para un problema de `nowcoder`:
     ```bash
     mvn exec:java -Dexec.mainClass="com.algorithm.solutions.nowcoder.Main"
     ```
   - Para un problema de UVA (por ejemplo, problema 106):
     ```bash
     mvn exec:java -Dexec.mainClass="com.algorithm.solutions.uva.p106.Main"
     ```

### Script de Python para `nowcoder`
Para complementar el script anterior de `uva`, aquí hay un script de Python para mover los archivos de `nowcoder` a `src/main/java/com/algorithm/solutions/nowcoder/` y añadir declaraciones de paquete. Ejecuta esto desde el directorio raíz `algorithm-solutions`.

```python
import os
from pathlib import Path

def add_package_declaration(java_file, package):
    """Añade la declaración del paquete al inicio de un archivo Java si no está ya presente."""
    with open(java_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not content.strip().startswith('package '):
        new_content = f'package {package};\n\n{content}'
        with open(java_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Se añadió la declaración del paquete a {java_file}')

def reorganize_nowcoder():
    # Definir rutas
    nowcoder_root = Path('nowcoder')
    target_dir = Path('src/main/java/com/algorithm/solutions/nowcoder')

    # Crear directorio destino
    target_dir.mkdir(parents=True, exist_ok=True)

    if not nowcoder_root.exists():
        print('Error: No se encontró el directorio nowcoder.')
        return

    # Mover archivos Java
    for java_file in nowcoder_root.glob('*.java'):
        target_file = target_dir / java_file.name
        shutil.move(str(java_file), str(target_file))
        print(f'Se movió {java_file} a {target_file}')
        
        # Añadir declaración del paquete
        add_package_declaration(target_file, 'com.algorithm.solutions.nowcoder')

    # Eliminar directorio nowcoder si está vacío
    if not any(nowcoder_root.iterdir()):
        nowcoder_root.rmdir()
        print(f'Se eliminó el directorio vacío {nowcoder_root}')

if __name__ == '__main__':
    reorganize_nowcoder()
    print('Reorganización de Nowcoder completada.')
```

### Notas
- **Ejecutar Scripts**: Ejecuta los scripts `reorganize_uva.py` (de la respuesta anterior) y `reorganize_nowcoder.py` para mover los archivos:
  ```bash
  python reorganize_uva.py
  python reorganize_nowcoder.py
  ```
- **Archivos de Entrada**: Si `nowcoder` tiene archivos de entrada, modifica el script para mover los archivos `*.in` a `src/main/resources/nowcoder/`.
- **Otros Directorios**: Para `codeforces`, `hacker_rank`, etc., puedes adaptar el script de `nowcoder` cambiando el directorio fuente y el nombre del paquete.
- **Acceso a Recursos**: Actualiza tu código Java para leer los archivos de entrada desde `src/main/resources` (por ejemplo, `getClass().getResource("/uva/p106/1.in")`).
- **Ignorar Archivos**: Añade `*.iml` a un archivo `.gitignore` para excluir los archivos de proyecto de IntelliJ.

¡Avísame si necesitas scripts para otros directorios o más ajustes al `pom.xml`!