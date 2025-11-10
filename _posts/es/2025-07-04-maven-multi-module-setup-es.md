---
audio: false
generated: true
lang: es
layout: post
title: Convertir Repositorio a Maven Multi-Módulo
translated: true
type: note
---

Para convertir tu repositorio `algorithm-solutions` en un proyecto multi-módulo de Java gestionado por Maven, necesitarás un `pom.xml` principal en el directorio raíz y archivos `pom.xml` individuales para cada submódulo (`nowcoder` y `uva`). El `pom.xml` principal definirá las configuraciones comunes y gestionará los submódulos, mientras que el `pom.xml` de cada submódulo manejará sus configuraciones específicas.

A continuación, proporcionaré los archivos `pom.xml` para el proyecto principal y los dos submódulos. Asumiré que:
- El proyecto utiliza Java 17 (una versión común para proyectos modernos; ajústala si es necesario).
- Los directorios `nowcoder` y `uva` contienen archivos fuente Java en una estructura estándar de Maven (`src/main/java`).
- No se requieren dependencias externas por ahora, pero la estructura permite agregarlas fácilmente.
- Cada submódulo se empaquetará como un JAR (ya que probablemente sean soluciones de algoritmos independientes).

### Estructura de Directorios
Después de la configuración, la estructura de tus directorios debería verse así:

```
algorithm-solutions/
├── pom.xml
├── nowcoder/
│   ├── pom.xml
│   └── src/
│       └── main/
│           └── java/
│               └── (tus archivos Java, p.ej., Main.java, nc140, etc.)
├── uva/
│   ├── pom.xml
│   └── src/
│       └── main/
│           └── java/
│               └── (tus archivos Java, p.ej., 100.java, 10000.java, etc.)
└── README.md
```

### `pom.xml` Principal
Este archivo va en el directorio raíz (`algorithm-solutions/pom.xml`). Define el proyecto principal, enumera los submódulos y establece configuraciones comunes como la versión de Java y la configuración del compilador.

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
    <description>Proyecto principal para las soluciones de algoritmos</description>

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

### `pom.xml` del Submódulo Nowcoder
Este archivo va en el directorio `nowcoder` (`nowcoder/pom.xml`). Hereda del proyecto principal y especifica sus propios detalles del artifact.

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
    <description>Soluciones para problemas de algoritmos de Nowcoder</description>

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

### `pom.xml` del Submódulo UVA
Este archivo va en el directorio `uva` (`uva/pom.xml`). También hereda del proyecto principal y especifica sus propios detalles del artifact. Dado que las soluciones de UVA típicamente no tienen una única clase `Main` (cada problema podría ser un programa independiente), no especificaré una clase principal aquí, pero puedes agregar una si es necesario.

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
    <description>Soluciones para problemas de algoritmos de UVA</description>

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

### Pasos para Configurar
1.  **Crear la Estructura de Directorios de Maven**:
    - Mueve tus archivos Java en `nowcoder` a `nowcoder/src/main/java/`.
    - Mueve tus archivos Java en `uva` a `uva/src/main/java/`.
    - Por ejemplo, `nowcoder/Main.java` debería estar en `nowcoder/src/main/java/Main.java`.

2.  **Colocar los Archivos `pom.xml`**:
    - Coloca el `pom.xml` principal en el directorio raíz `algorithm-solutions`.
    - Coloca el `nowcoder/pom.xml` en el directorio `nowcoder`.
    - Coloca el `uva/pom.xml` en el directorio `uva`.

3.  **Compilar el Proyecto**:
    - Navega al directorio raíz `algorithm-solutions` en una terminal.
    - Ejecuta `mvn clean install` para compilar ambos submódulos.

4.  **Ejecutar un Programa Específico**:
    - Para `nowcoder`, si `Main.java` es el punto de entrada, puedes ejecutarlo con:
      ```bash
      mvn -pl nowcoder exec:java -Dexec.mainClass="Main"
      ```
    - Para las soluciones de UVA, dado que cada archivo podría ser un programa independiente, puedes ejecutar una clase específica (p.ej., `100.java`) con:
      ```bash
      mvn -pl uva exec:java -Dexec.mainClass="100"
      ```

### Notas
- **Versión de Java**: Utilicé Java 17. Si necesitas una versión diferente, actualiza las propiedades `<maven.compiler.source>` y `<maven.compiler.target>` en el `pom.xml` principal.
- **Dependencias**: Si tus soluciones requieren librerías (p.ej., para utilidades de entrada/salida), agrégalas al `pom.xml` del submódulo en una sección `<dependencies>`.
- **Nomenclatura de Archivos**: Asegúrate de que tus archivos Java coincidan con los nombres de las clases (p.ej., `100.java` debe contener `public class 100`).
- **Otros Directorios**: Tu repositorio incluye `codeforces`, `hacker_rank`, etc. Si deseas incluirlos como submódulos, agrega `<module>codeforces</module>` (etc.) al `pom.xml` principal y crea archivos `pom.xml` correspondientes en esos directorios, similares a `nowcoder` y `uva`.

¡Avísame si necesitas submódulos adicionales o configuraciones específicas!