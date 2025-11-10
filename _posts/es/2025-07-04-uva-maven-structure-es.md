---
audio: false
generated: true
lang: es
layout: post
title: Estructura Maven para Problemas de UVA
translated: true
type: note
---

Gracias por compartir la estructura de directorios específica para tu subdirectorio `uva/106`. Parece que tu proyecto tiene una estructura más granular donde cada problema de UVA (por ejemplo, `106`) es un directorio separado con su propia carpeta `src` que contiene un archivo `Main.java` y posiblemente archivos de entrada como `1.in`. Esto sugiere que cada problema podría tratarse como un subproyecto o módulo separado. Para acomodar esto en una configuración multi-módulo de Maven, podemos:

1.  Tratar cada directorio de problema (por ejemplo, `uva/106`) como su propio submódulo de Maven.
2.  Mantener `uva` como un solo módulo y organizar los archivos de problemas dentro de su directorio `src/main/java`.

Dada la cantidad de problemas de UVA (como se ve en tu lista anterior: `100`, `10000`, etc.), crear un módulo de Maven separado para cada problema podría generar una gran cantidad de módulos, lo que podría ser engorroso. En su lugar, propondré una estructura donde `uva` es un solo módulo, y el `Main.java` de cada problema se organiza dentro de `uva/src/main/java` bajo una estructura de paquetes (por ejemplo, `com.algorithm.solutions.uva.p106` para el problema 106). Esto mantiene el proyecto manejable mientras conserva los beneficios de Maven.

Sin embargo, también proporcionaré un enfoque alternativo donde cada problema es un submódulo separado si prefieres esa granularidad. A continuación, actualizaré los archivos `pom.xml` según tu estructura y proporcionaré pasos para reorganizar tus archivos.

---

### Opción 1: Módulo único `uva` con Paquetes por Problema

#### Estructura de Directorios Actualizada
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

#### `pom.xml` Padre (Raíz: `algorithm-solutions/pom.xml`)
Esto permanece prácticamente igual que antes, definiendo `nowcoder` y `uva` como módulos.

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

#### `pom.xml` del Submódulo Nowcoder (`nowcoder/pom.xml`)
Este es igual a la respuesta anterior, asumiendo que los archivos de `nowcoder` se movieron a `src/main/java/com/algorithm/solutions/nowcoder/`.

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

#### `pom.xml` del Submódulo UVA (`uva/pom.xml`)
Este módulo incluye un directorio `resources` para archivos de entrada como `1.in`. Los archivos `Main.java` para cada problema se organizan en paquetes.

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

#### Organización de Archivos
- **Mover Archivos Java**:
  - Para cada problema (por ejemplo, `uva/106/src/Main.java`), mueve `Main.java` a `uva/src/main/java/com/algorithm/solutions/uva/p106/Main.java`.
  - Actualiza el archivo `Main.java` para incluir la declaración del paquete:
    ```java
    package com.algorithm.solutions.uva.p106;
    public class Main {
        // ... código existente ...
    }
    ```
  - Haz esto para todos los problemas (por ejemplo, `p100`, `p10000`, etc.).

- **Mover Archivos de Entrada**:
  - Mueve archivos de entrada como `uva/106/1.in` a `uva/src/main/resources/uva/p106/1.in`.
  - Esto permite que Maven incluya estos archivos en el JAR, accesibles mediante `ClassLoader.getResource()` o similar en tu código Java.

#### Ejecutar un Programa
Para ejecutar un problema específico de UVA (por ejemplo, problema 106):
```bash
mvn -pl uva exec:java -Dexec.mainClass="com.algorithm.solutions.uva.p106.Main"
```

---

### Opción 2: Cada Problema UVA como un Submódulo
Si prefieres que cada problema de UVA (por ejemplo, `106`, `100`) sea su propio módulo de Maven, así es como se configura. Esto es más granular pero aumenta el número de archivos `pom.xml`.

#### Estructura de Directorios Actualizada
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
│   │       └── (archivos de entrada, si los hay)
│   └── (otros directorios de problemas)
└── README.md
```

#### `pom.xml` Padre (Raíz: `algorithm-solutions/pom.xml`)
Añade cada problema como un módulo.

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

#### `pom.xml` del Submódulo Nowcoder (`nowcoder/pom.xml`)
Igual que arriba (sin cambios).

#### `pom.xml` del Submódulo UVA Problema 106 (`uva/106/pom.xml`)
Cada problema tiene su propio `pom.xml`. Aquí hay un ejemplo para `uva/106`:

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

- **Repetir para Otros Problemas**: Crea archivos `pom.xml` similares para `uva/100`, `uva/10000`, etc., ajustando el `artifactId` (por ejemplo, `uva-100`), `name`, y `mainClass` (por ejemplo, `com.algorithm.solutions.uva.p100.Main`).

#### Organización de Archivos
- **Mover Archivos Java**:
  - Para `uva/106/src/Main.java`, muévelo a `uva/106/src/main/java/com/algorithm/solutions/uva/p106/Main.java`.
  - Añade la declaración del paquete:
    ```java
    package com.algorithm.solutions.uva.p106;
    public class Main {
        // ... código existente ...
    }
    ```
- **Mover Archivos de Entrada**:
  - Mueve `uva/106/1.in` a `uva/106/resources/1.in`.

#### Ejecutar un Programa
Para ejecutar el problema 106:
```bash
mvn -pl uva/106 exec:java -Dexec.mainClass="com.algorithm.solutions.uva.p106.Main"
```

---

### Recomendación
- **Opción 1 (Módulo único `uva`)** es más simple y más escalable, especialmente si tienes muchos problemas de UVA. Evita crear numerosos archivos `pom.xml` y mantiene la estructura del proyecto limpia. Usa paquetes para organizar los problemas lógicamente.
- **Opción 2 (Módulos por Problema)** es mejor si quieres que cada problema sea completamente independiente (por ejemplo, para implementación o prueba separada). Sin embargo, requiere más mantenimiento debido al número de módulos.

### Pasos para Implementar la Opción 1
1.  **Crear Estructura de Directorios**:
    - Ejecuta estos comandos en la raíz de `algorithm-solutions`:
      ```bash
      mkdir -p uva/src/main/java/com/algorithm/solutions/uva
      mkdir -p uva/src/main/resources/uva
      mkdir -p nowcoder/src/main/java/com/algorithm/solutions/nowcoder
      ```
2.  **Mover Archivos**:
    - Para cada problema de UVA (por ejemplo, `106`):
      ```bash
      mkdir -p uva/src/main/java/com/algorithm/solutions/uva/p106
      mv uva/106/src/Main.java uva/src/main/java/com/algorithm/solutions/uva/p106/Main.java
      mkdir -p uva/src/main/resources/uva/p106
      mv uva/106/1.in uva/src/main/resources/uva/p106/1.in
      ```
    - Para `nowcoder`:
      ```bash
      mv nowcoder/*.java nowcoder/src/main/java/com/algorithm/solutions/nowcoder/
      ```
3.  **Actualizar Archivos Java**:
    - Añade las declaraciones de paquete apropiadas (por ejemplo, `package com.algorithm.solutions.uva.p106;` para `uva/106/Main.java`).
4.  **Añadir Archivos `pom.xml`**:
    - Coloca el `pom.xml` padre en `algorithm-solutions/`.
    - Coloca los `nowcoder/pom.xml` y `uva/pom.xml` como se muestra.
5.  **Compilar**:
    ```bash
    mvn clean install
    ```

### Notas
- **Archivos de Entrada**: Si tu `Main.java` lee archivos de entrada como `1.in`, actualiza el código para acceder a ellos mediante `getClass().getResource("/uva/p106/1.in")` o similar, ya que ahora están en `src/main/resources`.
- **Ignorar Archivos `.iml`**: Añade un archivo `.gitignore` con `*.iml` para excluir los archivos de proyecto de IntelliJ del control de versiones.
- **Otros Directorios**: Para `codeforces`, `hacker_rank`, etc., puedes crear módulos similares cuando estés listo. Avísame si necesitas archivos `pom.xml` para esos.
- **Versión de Java**: Ajusta `<maven.compiler.source>` y `<maven.compiler.target>` si usas una versión diferente de Java.

Si prefieres la Opción 2 o necesitas ayuda con problemas específicos (por ejemplo, ajustar `Main.java` para la carga de recursos), ¡avísame!