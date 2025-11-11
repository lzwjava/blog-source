---
audio: false
generated: true
lang: es
layout: post
title: Complemento Maven de Ayuda de Construcción
translated: true
type: note
---

El `builder-helper-maven-plugin`, ahora conocido como **Build Helper Maven Plugin**, es una herramienta versátil diseñada para ayudar con diversas tareas en el ciclo de vida de compilación de Maven. Originalmente alojado bajo Codehaus, ahora es mantenido por MojoHaus, aunque sus coordenadas de Maven aún utilizan el group ID `org.codehaus.mojo`. Este plugin proporciona un conjunto de metas (goals) para ayudar con operaciones como agregar directorios de origen adicionales, adjuntar artefactos adicionales, analizar información de versión y más. A continuación, te guiaré sobre cómo usar este plugin en tu proyecto de Maven.

### ¿Qué es Maven?
Antes de profundizar en el plugin, establezcamos el contexto. Maven es una herramienta de automatización de compilación ampliamente utilizada, principalmente para proyectos Java. Simplifica y estandariza el proceso de compilación gestionando dependencias, compilando código, empaquetando aplicaciones y más, todo configurado a través de un archivo central llamado `pom.xml`.

### Paso 1: Incluir el Plugin en Tu `pom.xml`
Para usar el Build Helper Maven Plugin, debes agregarlo a la sección `<build><plugins>` del archivo `pom.xml` de tu proyecto Maven. Así es cómo se hace:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>build-helper-maven-plugin</artifactId>
            <version>3.6.0</version>
            <!-- Aquí se agregarán las ejecuciones para metas específicas -->
        </plugin>
    </plugins>
</build>
```

- **Group ID**: `org.codehaus.mojo` (refleja sus orígenes, aunque ahora esté bajo MojoHaus).
- **Artifact ID**: `build-helper-maven-plugin`.
- **Versión**: Según mi última actualización, `3.6.0` es la versión más reciente, pero debes verificar [Maven Central](https://mvnrepository.com/artifact/org.codehaus.mojo/build-helper-maven-plugin) para obtener la versión más actualizada.

Esta declaración hace que el plugin esté disponible en tu proyecto, pero no hará nada hasta que configures metas específicas.

### Paso 2: Configurar Ejecuciones para Metas Específicas
El Build Helper Maven Plugin ofrece múltiples metas, cada una diseñada para una tarea particular. Configuras estas metas agregando bloques `<executions>` dentro de la declaración del plugin, especificando cuándo deben ejecutarse (a través de una fase del ciclo de vida de Maven) y cómo deben comportarse.

Aquí hay algunas metas comúnmente utilizadas y sus propósitos:

- **`add-source`**: Agrega directorios de origen adicionales a tu proyecto.
- **`add-test-source`**: Agrega directorios de origen de prueba adicionales.
- **`add-resource`**: Agrega directorios de recursos adicionales.
- **`attach-artifact`**: Adjunta artefactos adicionales (por ejemplo, archivos) a tu proyecto para su instalación y despliegue.
- **`parse-version`**: Analiza la versión del proyecto y establece propiedades (por ejemplo, versiones mayor, menor, incremental).

Cada meta requiere su propia configuración, que defines dentro de un bloque `<execution>`.

### Paso 3: Ejemplo – Agregar un Directorio de Origen Extra
Un caso de uso frecuente para este plugin es agregar un directorio de origen adicional, ya que Maven normalmente solo admite uno por defecto (`src/main/java`). Así es como configuras la meta `add-source` para incluir un directorio de origen adicional:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>build-helper-maven-plugin</artifactId>
            <version>3.6.0</version>
            <executions>
                <execution>
                    <id>add-source</id>
                    <phase>generate-sources</phase>
                    <goals>
                        <goal>add-source</goal>
                    </goals>
                    <configuration>
                        <sources>
                            <source>ruta/a/tu/directorio/fuente/extra</source>
                        </sources>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

- **`<id>`**: Un identificador único para esta ejecución (por ejemplo, `add-source`).
- **`<phase>`**: La fase del ciclo de vida de Maven en la que se ejecuta la meta (por ejemplo, `generate-sources` asegura que el directorio se agregue temprano en la compilación).
- **`<goals>`**: Especifica la meta a ejecutar (`add-source` en este caso).
- **`<configuration>`**: Define el directorio de origen adicional (reemplaza `ruta/a/tu/directorio/fuente/extra` con tu ruta real, por ejemplo, `src/main/generated`).

Cuando ejecutes un comando de Maven como `mvn compile`, Maven incluirá este directorio adicional como una carpeta de origen.

### Notas Adicionales
- **Compatibilidad de Versiones**: Desde la versión 3.0.0, el plugin requiere Maven 3 o superior. Si estás usando una versión anterior de Maven, necesitarás usar la versión 1.12 o anterior del plugin.
- **Múltiples Metas**: Puedes definir múltiples bloques `<execution>` dentro del mismo plugin para ejecutar diferentes metas. Por ejemplo, podrías agregar directorios de origen y de origen de prueba incluyendo ejecuciones para `add-source` y `add-test-source`.
- **Ejecutando el Plugin**: Una vez configurado, ejecutar un comando de Maven (por ejemplo, `mvn clean install`) activará las metas del plugin durante las fases especificadas.

### Recursos Adicionales
Para más detalles y ejemplos de otras metas, consulta la [página de uso oficial](https://www.mojohaus.org/build-helper-maven-plugin/usage.html). Esta página proporciona documentación completa y configuraciones de ejemplo para todas las metas disponibles.

### Reflexiones Finales
El Build Helper Maven Plugin es una adición poderosa a tu kit de herramientas de Maven, especialmente para proyectos que requieren configuraciones de compilación no estándar. Al incluirlo en tu `pom.xml` y configurar las metas apropiadas, puedes adaptar tu proceso de compilación para satisfacer necesidades específicas. Si bien se originó bajo Codehaus, su hogar actual es MojoHaus, y sigue siendo una opción confiable para mejorar las compilaciones de Maven.