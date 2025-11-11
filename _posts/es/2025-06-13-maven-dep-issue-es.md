---
audio: false
generated: true
lang: es
layout: post
title: Problema de Dependencia de Maven
translated: true
type: note
---

### Resumen del Problema

El usuario está experimentando un fallo de compilación al ejecutar una aplicación Spring Boot con Maven. El mensaje de error indica una `IllegalArgumentException` causada por `NoClassDefFoundError: org/springframework/beans/factory/aot/BeanRegistrationExcludeFilter`. Esto sugiere un problema de incompatibilidad de versiones en las dependencias del proyecto, lo que impide que la aplicación se inicie correctamente. El archivo `pom.xml` proporcionado y la salida de Maven nos dan el contexto necesario para diagnosticar y resolver el problema.

### Causa Raíz

El error ocurre porque la aplicación Spring Boot no puede instanciar `SharedMetadataReaderFactoryContextInitializer`, una clase involucrada en el proceso de auto-configuración de Spring Boot. La causa subyacente es una clase faltante, `BeanRegistrationExcludeFilter`, que es parte de Spring Framework 6.0 y versiones posteriores. El proyecto utiliza Spring Boot 3.4.2, que depende de Spring Framework 6.1.14. Sin embargo, el `pom.xml` especifica versiones antiguas e incompatibles de las dependencias de Spring Framework, lo que genera un conflicto en el classpath.

Estos son los problemas clave identificados en el `pom.xml`:

1.  **Versión Incompatible del Plugin Maven de Spring Boot:**
    *   El `spring-boot-maven-plugin` está configurado en la versión `2.7.0`, que está diseñada para Spring Boot 2.x, no para Spring Boot 3.4.2 (una versión 3.x). Esta discrepancia puede causar problemas durante las fases de compilación y ejecución.

2.  **Dependencias Explícitas e Incompatibles de Spring Framework:**
    *   El `pom.xml` declara explícitamente `spring-aop` y `spring-aspects` con la versión `5.3.23` (Spring Framework 5.x), mientras que Spring Boot 3.4.2 requiere Spring Framework 6.1.14. Maven prioriza estas versiones declaradas explícitamente sobre las versiones gestionadas por Spring Boot, lo que resulta en una mezcla de Spring Framework 5.x y 6.x en el classpath. Esta mezcla causa el `NoClassDefFoundError` porque `BeanRegistrationExcludeFilter` (de Spring Framework 6.x) no está disponible cuando se cargan los jars antiguos de la versión 5.x.

### Solución

Para resolver el problema, debemos asegurarnos de que todos los componentes del proyecto sean compatibles con Spring Boot 3.4.2 y que Spring Boot gestione las versiones de sus dependencias para evitar conflictos. Se deben realizar los siguientes cambios en el `pom.xml`:

1.  **Actualizar la Versión del Plugin Maven de Spring Boot:**
    *   Cambiar la versión del `spring-boot-maven-plugin` de `2.7.0` a `3.4.2` para alinearla con la versión de Spring Boot utilizada en el proyecto.

2.  **Eliminar las Dependencias Explícitas de Spring Framework:**
    *   Eliminar las declaraciones explícitas de `spring-aop` y `spring-aspects` con la versión `5.3.23`. Spring Boot 3.4.2 gestiona estas dependencias a través de sus starters (por ejemplo, `spring-boot-starter-web` incluye `spring-aop` con la versión correcta, 6.1.14). Al eliminarlas, evitamos que Maven anule la gestión de dependencias de Spring Boot.

### `pom.xml` Actualizado

A continuación se muestra el archivo `pom.xml` corregido con los cambios necesarios aplicados:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>org.lzwjava</groupId>
    <artifactId>blog-server</artifactId>
    <version>1.0</version>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
            <version>3.4.2</version>
        </dependency>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-api</artifactId>
            <version>5.9.3</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-engine</artifactId>
            <version>5.9.3</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.mockito</groupId>
            <artifactId>mockito-core</artifactId>
            <version>5.3.1</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <version>3.4.2</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.aspectj</groupId>
            <artifactId>aspectjrt</artifactId>
            <version>1.9.22</version>
        </dependency>
        <dependency>
            <groupId>org.aspectj</groupId>
            <artifactId>aspectjweaver</artifactId>
            <version>1.9.22</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>3.4.2</version>
                <executions>
                    <execution>
                        <goals>
                            <goal>repackage</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.0.0-M8</version>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-checkstyle-plugin</artifactId>
                <version>3.1.1</version>
                <configuration>
                    <configLocation>google_checks.xml</configLocation>
                </configuration>
                <executions>
                    <execution>
                        <goals>
                            <goal>check</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

### Explicación de los Cambios

-   **Actualización del Plugin Maven de Spring Boot:**
    *   Se cambió `<version>2.7.0</version>` a `<version>3.4.2</version>` en la configuración del `spring-boot-maven-plugin`. Esto asegura que el plugin sea compatible con Spring Boot 3.4.2, admitiendo características y configuraciones específicas de la serie 3.x.

-   **Eliminación de `spring-aop` y `spring-aspects`:**
    *   Se eliminaron las siguientes dependencias:
        ```xml
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-aop</artifactId>
            <version>5.3.23</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-aspects</artifactId>
            <version>5.3.23</version>
        </dependency>
        ```
    *   `spring-aop` ya está incluido en `spring-boot-starter-web` (a través de `spring-web`), y Spring Boot gestiona su versión a la 6.1.14, que es compatible con 3.4.2.
    *   `spring-aspects` no es una dependencia estándar en los starters de Spring Boot. Si el proyecto la requiere explícitamente (por ejemplo, para aspectos personalizados), se puede volver a agregar sin una versión (dejando que la gestión de dependencias de Spring Boot la maneje) o establecerla en `6.1.14`. Sin embargo, dado que el error ocurre durante el inicio y está relacionado con la auto-configuración y no con aspectos faltantes, es probable que no sea necesaria aquí y se pueda eliminar de forma segura.

### Notas Adicionales

-   **Dependencias de AspectJ:**
    *   Las dependencias `aspectjrt` y `aspectjweaver` (versión 1.9.22) permanecen en el `pom.xml` ya que son compatibles con Spring Framework 6.1.14 y pueden ser necesarias si el proyecto utiliza características de AspectJ. Estas no entran en conflicto con Spring Boot 3.4.2.

-   **Mejores Prácticas:**
    *   Para proyectos Spring Boot, se recomienda usar `spring-boot-starter-parent` como POM padre o importar el BOM `spring-boot-dependencies` para gestionar las versiones de las dependencias automáticamente. El `pom.xml` actual no hace ninguna de las dos cosas, pero la solución funciona sin requerir este cambio ya que `spring-boot-starter-web` y otros starters aún imponen la coherencia de versiones cuando se eliminan las anulaciones explícitas.

-   **Verificación:**
    *   Después de aplicar estos cambios, ejecuta `mvn clean spring-boot:run` para verificar que la aplicación se inicie sin errores. Si el proyecto depende de `spring-aspects` (por ejemplo, para una funcionalidad AOP específica) y su eliminación causa problemas, agrégala de nuevo con `<version>6.1.14</version>` u omite la versión y asegura una gestión de dependencias adecuada.

### Conclusión

Al actualizar el `spring-boot-maven-plugin` a la versión 3.4.2 y eliminar las dependencias explícitas `spring-aop` y `spring-aspects`, el proyecto utilizará versiones consistentes de Spring Boot (3.4.2) y Spring Framework (6.1.14). Esto resuelve el conflicto de classpath que causaba el `NoClassDefFoundError` y permite que la aplicación se inicie exitosamente.