---
audio: false
generated: true
lang: es
layout: post
title: Configurar Palantir Java Format con Spotless
translated: true
type: note
---

Para configurar **Palantir Java Format** con el **Spotless Maven Plugin** en un archivo `pom.xml`, debe configurar el plugin para usar `palantirJavaFormat` y especificar opciones de formato como tabulaciones, sangría, orden de importaciones y otras configuraciones. A continuación se presenta una guía detallada sobre cómo configurar estas opciones y las opciones disponibles basadas en el plugin Spotless y Palantir Java Format.

### Agregar Spotless Maven Plugin con Palantir Java Format

Incluya el Spotless Maven Plugin en su `pom.xml` y configúrelo para usar `palantirJavaFormat`. Aquí hay una configuración básica con configuraciones comunes para tabulaciones, sangría, orden de importaciones y otras opciones:

```xml
<plugin>
    <groupId>com.diffplug.spotless</groupId>
    <artifactId>spotless-maven-plugin</artifactId>
    <version>2.43.0</version> <!-- Usa la versión más reciente -->
    <configuration>
        <java>
            <!-- Especificar archivos a formatear (opcional, por defecto todos los archivos .java) -->
            <includes>
                <include>src/main/java/**/*.java</include>
                <include>src/test/java/**/*.java</include>
            </includes>
            <!-- Palantir Java Format -->
            <palantirJavaFormat>
                <version>2.53.0</version> <!-- Especificar la versión deseada -->
                <style>GOOGLE</style> <!-- Opciones: GOOGLE, AOSP, o PALANTIR -->
                <formatJavadoc>true</formatJavadoc> <!-- Opcional: Formatear Javadoc -->
            </palantirJavaFormat>
            <!-- Configuración de sangría -->
            <indent>
                <tabs>true</tabs> <!-- Usar tabulaciones en lugar de espacios -->
                <spacesPerTab>4</spacesPerTab> <!-- Número de espacios por tabulación -->
            </indent>
            <!-- Configuración del orden de importaciones -->
            <importOrder>
                <order>java,javax,org,com,\\#</order> <!-- Orden de importaciones personalizado -->
            </importOrder>
            <!-- Remover importaciones no utilizadas -->
            <removeUnusedImports/>
            <!-- Otras configuraciones opcionales -->
            <trimTrailingWhitespace/>
            <endWithNewline/>
            <toggleOffOn/> <!-- Habilita las etiquetas spotless:off y spotless:on -->
        </java>
    </configuration>
    <executions>
        <execution>
            <goals>
                <goal>apply</goal> <!-- Formatea el código automáticamente -->
            </goals>
            <phase>validate</phase> <!-- Se ejecuta durante la fase de validación -->
        </execution>
    </executions>
</plugin>
```

### Explicación de las Opciones de Configuración

Aquí se desglosan las opciones clave de configuración para la sección `java` en Spotless con `palantirJavaFormat`, centrándose en tabulaciones, sangría, orden de importaciones y otras configuraciones relevantes:

#### 1. **Palantir Java Format (`<palantirJavaFormat>`)**

- **`<version>`**: Especifica la versión de `palantir-java-format` a usar. Consulte la última versión en [Maven Repository](https://mvnrepository.com/artifact/com.palantir.java-format/palantir-java-format) o [GitHub](https://github.com/palantir/palantir-java-format/releases). Ejemplo: `<version>2.53.0</version>`.
- **`<style>`**: Define el estilo de formato. Las opciones son:
  - `GOOGLE`: Usa Google Java Style (sangría de 2 espacios, límite de línea de 100 caracteres).
  - `AOSP`: Usa el estilo Android Open Source Project (sangría de 4 espacios, límite de línea de 100 caracteres).
  - `PALANTIR`: Usa el estilo de Palantir (sangría de 4 espacios, límite de línea de 120 caracteres, formato amigable con lambdas).[](https://github.com/palantir/palantir-java-format)
- **`<formatJavadoc>`**: Booleano para habilitar/deshabilitar el formateo de Javadoc (requiere Palantir Java Format versión ≥ 2.39.0). Ejemplo: `<formatJavadoc>true</formatJavadoc>`.[](https://github.com/diffplug/spotless/blob/main/plugin-gradle/README.md)
- **Group Artifact Personalizado**: Raramente necesario, pero puede especificar un group y artifact personalizado para el formateador. Ejemplo: `<groupArtifact>com.palantir.java-format:palantir-java-format</groupArtifact>`.

#### 2. **Sangría (`<indent>`)**

- **`<tabs>`**: Booleano para usar tabulaciones (`true`) o espacios (`false`) para la sangría. Ejemplo: `<tabs>true</tabs>`.[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
- **`<spacesPerTab>`**: Número de espacios por tabulación (se usa cuando `<tabs>` es `false` o para sangría mixta). Los valores comunes son `2` o `4`. Ejemplo: `<spacesPerTab>4</spacesPerTab>`.[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
  - **Nota**: El estilo de Palantir Java Format (por ejemplo, `GOOGLE`, `AOSP`, `PALANTIR`) puede influir en el comportamiento de la sangría. Por ejemplo, `GOOGLE` usa por defecto 2 espacios, mientras que `AOSP` y `PALANTIR` usan 4 espacios. Las configuraciones `<indent>` en Spotless pueden anular o complementar estos valores por defecto, pero asegúrese de mantener la consistencia para evitar conflictos.[](https://stackoverflow.com/questions/50027892/override-google-java-format-with-spotless-maven-plugin)

#### 3. **Orden de Importaciones (`<importOrder>`)**

- **`<order>`**: Especifica el orden de los grupos de importación, separados por comas. Use `\\#` para importaciones estáticas y una cadena vacía (`""`) para importaciones no especificadas. Ejemplo: `<order>java,javax,org,com,\\#</order>` ordena las importaciones comenzando con `java`, luego `javax`, etc., con las importaciones estáticas al final.[](https://stackoverflow.com/questions/71339562/spotless-java-google-format-vs-intellij-import-file)
- **`<file>`**: Alternativamente, especifique un archivo que contenga el orden de importación. Ejemplo: `<file>${project.basedir}/eclipse.importorder</file>`. El formato del archivo coincide con la configuración del orden de importación de Eclipse (por ejemplo, `java|javax|org|com|\\#`).[](https://stackoverflow.com/questions/71339562/spotless-java-google-format-vs-intellij-import-file)
  - Contenido de archivo de ejemplo:
    ```
    #sort
    java
    javax
    org
    com
    \#
    ```

#### 4. **Otras Configuraciones Útiles**

- **`<removeUnusedImports>`**: Elimina las importaciones no utilizadas. Opcionalmente, especifique el motor:
  - Por defecto: Usa `google-java-format` para la eliminación.
  - Alternativa: `<engine>cleanthat-javaparser-unnecessaryimport</engine>` para compatibilidad con JDK8+ y nuevas características de Java (por ejemplo, Java 17).[](https://stackoverflow.com/questions/77126927/spotless-eclipse-formatter-java-17-error-on-string-literals-removing-unu)
- **`<trimTrailingWhitespace>`**: Elimina los espacios en blanco al final de las líneas. Ejemplo: `<trimTrailingWhitespace/>`.[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
- **`<endWithNewline>`**: Asegura que los archivos terminen con una nueva línea. Ejemplo: `<endWithNewline/>`.[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
- **`<toggleOffOn>`**: Habilita los comentarios `// spotless:off` y `// spotless:on` para excluir secciones de código del formateo. Ejemplo: `<toggleOffOn/>`.[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
- **`<licenseHeader>`**: Agrega un encabezado de licencia a los archivos. Ejemplo:
  ```xml
  <licenseHeader>
      <content>/* (C) $YEAR */</content>
  </licenseHeader>
  ```
  También puede usar un archivo: `<file>${project.basedir}/license.txt</file>`.[](https://www.baeldung.com/java-maven-spotless-plugin)
- **`<formatAnnotations>`**: Asegura que las anotaciones de tipo estén en la misma línea que los campos que describen. Ejemplo: `<formatAnnotations/>`.[](https://www.baeldung.com/java-maven-spotless-plugin)
- **`<ratchetFrom>`**: Limita el formateo a los archivos cambiados en relación con una rama de Git (por ejemplo, `origin/main`). Ejemplo: `<ratchetFrom>origin/main</ratchetFrom>`.[](https://github.com/diffplug/spotless/blob/main/plugin-maven/README.md)

#### 5. **Formateo Específico de POM (`<pom>`)**

Para formatear el archivo `pom.xml` en sí, use la sección `<pom>` con `sortPom`:
```xml
<pom>
    <sortPom>
        <nrOfIndentSpace>2</nrOfIndentSpace> <!-- Sangría para el POM -->
        <predefinedSortOrder>recommended_2008_06</predefinedSortOrder> <!-- Orden estándar de POM -->
        <sortDependencies>groupId,artifactId</sortDependencies> <!-- Ordenar dependencias -->
        <sortPlugins>groupId,artifactId</sortPlugins> <!-- Ordenar plugins -->
        <endWithNewline>true</endWithNewline>
    </sortPom>
</pom>
```
- **Opciones para `sortPom`**:
  - `<nrOfIndentSpace>`: Número de espacios para la sangría (por ejemplo, `2` o `4`).
  - `<predefinedSortOrder>`: Opciones como `recommended_2008_06` o `custom_1` para el orden de elementos.[](https://github.com/diffplug/spotless/blob/main/plugin-gradle/README.md)
  - `<sortDependencies>`: Ordenar por `groupId`, `artifactId`, u otros criterios.
  - `<sortPlugins>`: Ordenar plugins de manera similar.
  - `<endWithNewline>`: Asegurar que el POM termine con una nueva línea.
  - `<expandEmptyElements>`: Expandir etiquetas XML vacías (por ejemplo, `<tag></tag>` vs `<tag/>`).[](https://github.com/diffplug/spotless/blob/main/plugin-gradle/README.md)

### Ejecutar Spotless

- **Verificar formato**: `mvn spotless:check` – Valida el código contra las reglas configuradas, fallando la compilación si se encuentran violaciones.
- **Aplicar formato**: `mvn spotless:apply` – Formatea automáticamente el código para cumplir con las reglas.

### Notas y Mejores Prácticas

- **Consistencia con el IDE**: Para alinear IntelliJ o Eclipse con Spotless, instale el plugin `palantir-java-format` para IntelliJ o use un archivo XML del formateador de Eclipse. Para IntelliJ, importe un archivo de estilo compatible (por ejemplo, `intellij-java-google-style.xml` para el estilo Google) o configure manualmente para que coincida con la configuración de Palantir.[](https://plugins.jetbrains.com/plugin/13180-palantir-java-format)
- **Compatibilidad de Versiones**: Asegúrese de que la versión de `palantir-java-format` sea compatible con su versión de Java. Para Java 17+, use una versión reciente (por ejemplo, 2.53.0). Algunas características como pattern matching pueden tener soporte limitado.[](https://www.reddit.com/r/java/comments/1g8zu8c/codestyle_and_formatters/)
- **Formateo Personalizado**: Para personalización avanzada, use un archivo XML del formateador de Eclipse con `<eclipse>` en lugar de `<palantirJavaFormat>`:
  ```xml
  <eclipse>
      <file>${project.basedir}/custom-style.xml</file>
  </eclipse>
  ```
  Ejemplo de `custom-style.xml`:
  ```xml
  <?xml version="1.0" encoding="utf-8"?>
  <profiles version="21">
      <profile kind="CodeFormatterProfile" name="custom" version="21">
          <setting id="org.eclipse.jdt.core.formatter.tabulation.char" value="space"/>
          <setting id="org.eclipse.jdt.core.formatter.indentation.size" value="4"/>
          <setting id="org.eclipse.jdt.core.formatter.tabulation.size" value="4"/>
      </profile>
  </profiles>
  ```
  [](https://www.baeldung.com/java-maven-spotless-plugin)
- **Limitaciones**: Palantir Java Format es menos configurable que el formateador de Eclipse, pero está diseñado para la consistencia y características modernas de Java (por ejemplo, lambdas). Puede que no maneje todos los casos extremos (por ejemplo, lambdas profundamente anidadas).[](https://www.reddit.com/r/java/comments/18z151f/strict_code_formatter/)

### Resumen de Opciones Disponibles

| **Opción**                  | **Descripción**                                                                 | **Valores de Ejemplo**                              |
|-----------------------------|---------------------------------------------------------------------------------|------------------------------------------------|
| `<palantirJavaFormat>`      | Configura Palantir Java Format.                                                | `<version>2.53.0</version>`, `<style>PALANTIR</style>` |
| `<indent>`                  | Establece el estilo de sangría (tabs o espacios) y tamaño.                     | `<tabs>true</tabs>`, `<spacesPerTab>4</spacesPerTab>` |
| `<importOrder>`             | Define el orden de grupos de importación o usa un archivo.                     | `<order>java,javax,org,com,\\#</order>`        |
| `<removeUnusedImports>`     | Elimina importaciones no utilizadas, con motor opcional.                       | `<engine>cleanthat-javaparser-unnecessaryimport</engine>` |
| `<trimTrailingWhitespace>`  | Elimina espacios en blanco al final de la línea.                              | `<trimTrailingWhitespace/>`                    |
| `<endWithNewline>`         | Asegura que los archivos terminen con una nueva línea.                        | `<endWithNewline/>`                           |
| `<toggleOffOn>`            | Habilita las etiquetas `spotless:off`/`spotless:on`.                          | `<toggleOffOn/>`                              |
| `<licenseHeader>`          | Agrega un encabezado de licencia.                                              | `<content>/* (C) $YEAR */</content>`           |
| `<formatAnnotations>`       | Formatea anotaciones para que estén en la misma línea que los campos.         | `<formatAnnotations/>`                         |
| `<sortPom>`                | Formatea `pom.xml` con ordenamiento y sangría.                                | `<nrOfIndentSpace>2</nrOfIndentSpace>`        |

### Fuentes

- Documentación de Spotless Maven Plugin: [GitHub](https://github.com/diffplug/spotless/tree/main/plugin-maven)[](https://github.com/diffplug/spotless/blob/main/plugin-maven/README.md)
- Palantir Java Format: [GitHub](https://github.com/palantir/palantir-java-format)[](https://github.com/palantir/palantir-java-format)
- Ejemplos de Stack Overflow y la comunidad para la configuración de Spotless[](https://stackoverflow.com/questions/50027892/override-google-java-format-with-spotless-maven-plugin)[](https://stackoverflow.com/questions/71339562/spotless-java-google-format-vs-intellij-import-file)[](https://stackoverflow.com/questions/77126927/spotless-eclipse-formatter-java-17-error-on-string-literals-removing-unu)

Esta configuración asegura un formateo de código consistente con Palantir Java Format, adaptado a sus preferencias para tabulaciones, sangría y orden de importaciones. ¡Avíseme si necesita más aclaraciones u opciones adicionales!