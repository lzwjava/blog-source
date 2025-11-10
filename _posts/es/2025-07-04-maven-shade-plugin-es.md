---
audio: false
generated: true
lang: es
layout: post
title: 'Plugin Maven Shade: Crear Uber-JARs'
translated: true
type: note
---

El `maven-shade-plugin` es un plugin de Maven utilizado para crear un "uber-JAR" (un único archivo JAR autocontenido) combinando el código compilado de un proyecto con sus dependencias. Se usa comúnmente en proyectos Java para empaquetar una aplicación y todas sus librerías requeridas en un único archivo JAR ejecutable, simplificando la distribución y el despliegue.

### Detalles Clave:
- **Group ID**: `org.apache.maven.plugins` (indica que es un plugin oficial de Apache Maven).
- **Artifact ID**: `maven-shade-plugin` (el nombre específico del plugin).
- **Propósito**:
  - **Shading (Ocultación)**: Reubica (renombra) paquetes de dependencias para evitar conflictos de clases (por ejemplo, cuando múltiples librerías usan diferentes versiones de la misma clase).
  - **Empaquetado**: Agrupa las dependencias en el JAR final, haciéndolo independiente.
  - **Transformación de Recursos**: Puede modificar recursos (por ejemplo, fusionar archivos de configuración como `MANIFEST.MF`).
- **Casos de Uso Comunes**:
  - Crear JARs ejecutables para aplicaciones de línea de comandos.
  - Resolver conflictos en el classpath en proyectos con múltiples dependencias.
  - Simplificar el despliegue para aplicaciones como trabajos de Spark o Hadoop.
- **Cómo Funciona**:
  - Se configura en el archivo `pom.xml` dentro de la sección `<plugins>`.
  - Durante el proceso de construcción (típicamente en la fase `package`), combina clases y recursos, reubica opcionalmente paquetes y produce el JAR final.
- **Configuración de Ejemplo** en `pom.xml`:
  ```xml
  <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-shade-plugin</artifactId>
      <version>3.5.0</version> <!-- Usa la última versión -->
      <executions>
          <execution>
              <phase>package</phase>
              <goals>
                  <goal>shade</goal>
              </goals>
              <configuration>
                  <transformers>
                      <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                          <mainClass>com.example.Main</mainClass>
                      </transformer>
                  </transformers>
              </configuration>
          </execution>
      </executions>
  </plugin>
  ```
  Este ejemplo especifica la clase principal para un JAR ejecutable y ejecuta el plugin durante la fase `package`.

- **Características Principales**:
  - **Inclusión de Dependencias**: Incrusta las dependencias en el JAR.
  - **Reubicación de Paquetes**: Renombra paquetes para evitar conflictos (por ejemplo, `com.google.common` a `shaded.com.google.common`).
  - **Filtrado de Recursos**: Fusiona o transforma archivos de recursos.
  - **JAR Ejecutable**: Añade entradas al manifiesto para hacer el JAR ejecutable con `java -jar`.

### Cuándo Usarlo:
- Cuando necesitas un único JAR para una distribución sencilla.
- Cuando manejas conflictos de dependencias (por ejemplo, diferentes versiones de la misma librería).
- Para desplegar aplicaciones en entornos donde las dependencias externas son difíciles de gestionar.

Si tienes una pregunta específica sobre su configuración o caso de uso, ¡házmelo saber!