---
audio: false
generated: true
lang: es
layout: post
title: Maven Plugin de Dependencia
translated: true
---

El **Maven Dependency Plugin** es una herramienta poderosa en Maven, una herramienta de automatización de compilación ampliamente utilizada para proyectos de Java, que te ayuda a gestionar y manipular las dependencias del proyecto. Las dependencias en un proyecto de Maven son bibliotecas o módulos externos declarados en el archivo `pom.xml`, que Maven descarga de los repositorios y hace disponibles durante la compilación, la ejecución o las pruebas. El Plugin de Dependencia amplía esta funcionalidad proporcionando diversos objetivos (tareas) para analizar, copiar, listar o manejar de otra manera estas dependencias. Aquí te mostramos cómo usarlo de manera efectiva:

---

#### **1. Descripción del uso**
Puedes usar el Maven Dependency Plugin de dos maneras principales:
- **Configúralo en el archivo `pom.xml`**: Esto te permite vincular objetivos específicos del plugin a fases del ciclo de vida de construcción de Maven (por ejemplo, `package`, `install`) para su ejecución automática durante el proceso de construcción.
- **Ejecutar objetivos directamente desde la línea de comandos**: Esto es ideal para tareas puntuales o cuando no deseas modificar el `pom.xml`.

El plugin se identifica por sus coordenadas: `groupId: org.apache.maven.plugins`, `artifactId: maven-dependency-plugin`. Necesitarás especificar una versión (por ejemplo, `3.2.0`) al configurarlo, aunque Maven puede resolver la última versión si se omite en el uso de la línea de comandos.

---

#### **2. Agregar el Plugin a `pom.xml`**
Para usar el plugin como parte de tu proceso de construcción, agrégalo a la sección `<build><plugins>` de tu `pom.xml`. Aquí tienes un ejemplo básico:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-dependency-plugin</artifactId>
            <version>3.2.0</version>
        </plugin>
    </plugins>
</build>
```

Con esta configuración, puedes configurar objetivos específicos para que se ejecuten durante el ciclo de vida de la construcción agregando bloques `<executions>`.

---

#### **3. Objetivos comunes y cómo usarlos**
El plugin proporciona varios objetivos para gestionar dependencias. A continuación, se muestran algunos de los más comúnmente utilizados, junto con ejemplos de cómo usarlos:

##### **a. `copy-dependencies`**
- **Propósito**: Copia las dependencias del proyecto a un directorio especificado (por ejemplo, para empaquetarlas en una carpeta `lib`).
- **Configurado en `pom.xml`**:
  Vincula este objetivo a la fase `package` para copiar dependencias durante `mvn package`:

  ```xml
  <build>
      <plugins>
          <plugin>
              <groupId>org.apache.maven.plugins</groupId>
              <artifactId>maven-dependency-plugin</artifactId>
              <version>3.2.0</version>
              <executions>
                  <execution>
                      <id>copy-dependencies</id>
                      <phase>package</phase>
                      <goals>
                          <goal>copy-dependencies</goal>
                      </goals>
                      <configuration>
                          <outputDirectory>${project.build.directory}/lib</outputDirectory>
                          <includeScope>runtime</includeScope>
                      </configuration>
                  </execution>
              </executions>
          </plugin>
      </plugins>
  </build>
  ```

  - `${project.build.directory}/lib` se resuelve a `target/lib` en tu proyecto.
  - `<includeScope>runtime</includeScope>` limita la copia a las dependencias con los alcances `compile` y `runtime`, excluyendo `test` y `provided`.

- **Línea de comandos**:
  Ejecútalo directamente sin modificar el `pom.xml`:

  ```bash
  mvn dependency:copy-dependencies -DoutputDirectory=lib
  ```

##### **b. `tree`**
- **Propósito**: Muestra el árbol de dependencias, mostrando todas las dependencias directas y transitivas y sus versiones. Esto es útil para identificar conflictos de versiones.
- **Línea de comandos**:
  Simplemente ejecuta:

  ```bash
  mvn dependency:tree
  ```

  Esto muestra una vista jerárquica de las dependencias en la consola.
- **Configurado en `pom.xml`** (opcional):
  Si deseas que esto se ejecute durante una fase de construcción (por ejemplo, `verify`), configúralo de manera similar a `copy-dependencies`.

##### **c. `analyze`**
- **Propósito**: Analiza las dependencias para identificar problemas, como:
  - Dependencias utilizadas pero no declaradas.
  - Dependencias declaradas pero no utilizadas.
- **Línea de comandos**:
  Ejecuta:

  ```bash
  mvn dependency:analyze
  ```

  Esto genera un informe en la consola.
- **Nota**: Este objetivo puede requerir configuración adicional para proyectos complejos para afinar su análisis.

##### **d. `list`**
- **Propósito**: Lista todas las dependencias resueltas del proyecto.
- **Línea de comandos**:
  Ejecuta:

  ```bash
  mvn dependency:list
  ```

  Esto proporciona una lista plana de dependencias, útil para referencia rápida.

##### **e. `unpack`**
- **Propósito**: Extrae el contenido de una dependencia específica (por ejemplo, un archivo JAR) a un directorio.
- **Línea de comandos**:
  Ejemplo para descomprimir una dependencia específica:

  ```bash
  mvn dependency:unpack -Dartifact=groupId:artifactId:version -DoutputDirectory=target/unpacked
  ```

  Reemplaza `groupId:artifactId:version` con las coordenadas de la dependencia (por ejemplo, `org.apache.commons:commons-lang3:3.12.0`).

##### **f. `purge-local-repository`**
- **Propósito**: Elimina dependencias especificadas de tu repositorio local de Maven (`~/.m2/repository`), forzando una descarga fresca desde los repositorios remotos.
- **Línea de comandos**:
  Ejecuta:

  ```bash
  mvn dependency:purge-local-repository
  ```

  Esto es útil para solucionar problemas con archivos de dependencia corruptos.

---

#### **4. Opciones de personalización**
Muchos objetivos admiten parámetros de configuración para adaptar su comportamiento:
- **`outputDirectory`**: Especifica dónde copiar o descomprimir archivos (por ejemplo, `target/lib`).
- **`includeScope` o `excludeScope`**: Filtra dependencias por alcance (por ejemplo, `runtime`, `test`).
- **`artifact`**: Objetivo de una dependencia específica para objetivos como `unpack`.

Estos se pueden establecer en la sección `<configuration>` del `pom.xml` o pasarse como argumentos de la línea de comandos con `-D` (por ejemplo, `-DincludeScope=runtime`).

---

#### **5. Ejemplos prácticos**
- **Escenario 1: Empaquetar una aplicación independiente**
  Usa `copy-dependencies` para recopilar todas las dependencias de tiempo de ejecución en una carpeta `lib`:

  ```bash
  mvn dependency:copy-dependencies -DoutputDirectory=lib -DincludeScope=runtime
  ```

- **Escenario 2: Depurar conflictos de dependencias**
  Ejecuta `dependency:tree` para inspeccionar dependencias transitivas:

  ```bash
  mvn dependency:tree
  ```

  Si encuentras múltiples versiones de una biblioteca (por ejemplo, `commons-logging`), resuelve el conflicto agregando una sección `<dependencyManagement>` en `pom.xml`.

- **Escenario 3: Extraer recursos**
  Descomprime una dependencia para acceder a su contenido:

  ```bash
  mvn dependency:unpack -Dartifact=org.example:my-lib:1.0.0 -DoutputDirectory=target/resources
  ```

---

#### **6. Resumen**
Para usar el Maven Dependency Plugin:
- Agrégalo a tu `pom.xml` con objetivos y configuraciones específicos si deseas que se integre en tu proceso de construcción.
- Ejecuta objetivos como `copy-dependencies`, `tree`, `analyze`, `list` o `unpack` directamente desde la línea de comandos para tareas ad-hoc.
- Personaliza el comportamiento con opciones de configuración para adaptarlo a las necesidades de tu proyecto.

Este plugin es una herramienta versátil para gestionar dependencias más allá de la simple declaración, lo que lo hace invaluable para construir, depurar y distribuir proyectos de Maven.