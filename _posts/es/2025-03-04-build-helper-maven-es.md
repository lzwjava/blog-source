---
audio: false
generated: true
lang: es
layout: post
title: Plugin de Ayuda de Construcción Maven
translated: true
---

El `builder-helper-maven-plugin`, ahora conocido como el **Build Helper Maven Plugin**, es una herramienta versátil diseñada para asistir con diversas tareas en el ciclo de vida de construcción de Maven. Originalmente alojado bajo Codehaus, ahora es mantenido por MojoHaus, aunque sus coordenadas de Maven aún utilizan el grupo ID `org.codehaus.mojo`. Este plugin proporciona un conjunto de objetivos para ayudar con operaciones como agregar directorios de origen adicionales, adjuntar artefactos adicionales, analizar información de versión y más. A continuación, te guiaré sobre cómo usar este plugin en tu proyecto Maven.

### ¿Qué es Maven?
Antes de sumergirnos en el plugin, establezcamos el contexto. Maven es una herramienta de automatización de construcción ampliamente utilizada, principalmente para proyectos Java. Simplifica y estandariza el proceso de construcción al gestionar dependencias, compilar código, empaquetar aplicaciones y más, todo configurado a través de un archivo central llamado `pom.xml`.

### Paso 1: Incluir el Plugin en tu `pom.xml`
Para usar el Build Helper Maven Plugin, necesitas agregarlo al archivo `pom.xml` de tu proyecto Maven dentro de la sección `<build><plugins>`. Aquí te muestro cómo hacerlo:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>build-helper-maven-plugin</artifactId>
            <version>3.6.0</version>
            <!-- Ejecuciones para objetivos específicos se agregarán aquí -->
        </plugin>
    </plugins>
</build>
```

- **Group ID**: `org.codehaus.mojo` (reflejando sus orígenes, aunque ahora está bajo MojoHaus).
- **Artifact ID**: `build-helper-maven-plugin`.
- **Versión**: Hasta mi última actualización, `3.6.0` es la versión más reciente, pero deberías verificar [Maven Central](https://mvnrepository.com/artifact/org.codehaus.mojo/build-helper-maven-plugin) para la versión más reciente.

Esta declaración hace que el plugin esté disponible en tu proyecto, pero no hará nada hasta que configures objetivos específicos.

### Paso 2: Configurar Ejecuciones para Objetivos Específicos
El Build Helper Maven Plugin ofrece múltiples objetivos, cada uno diseñado para una tarea particular. Configuras estos objetivos agregando bloques `<executions>` dentro de la declaración del plugin, especificando cuándo deben ejecutarse (a través de una fase del ciclo de vida de Maven) y cómo deben comportarse.

Aquí tienes algunos objetivos comúnmente utilizados y sus propósitos:

- **`add-source`**: Agrega directorios de origen adicionales a tu proyecto.
- **`add-test-source`**: Agrega directorios de origen de pruebas adicionales.
- **`add-resource`**: Agrega directorios de recursos adicionales.
- **`attach-artifact`**: Adjunta artefactos adicionales (por ejemplo, archivos) a tu proyecto para instalación y despliegue.
- **`parse-version`**: Analiza la versión del proyecto y establece propiedades (por ejemplo, versiones principales, menores, incrementales).

Cada objetivo requiere su propia configuración, que defines dentro de un bloque `<execution>`.

### Paso 3: Ejemplo – Agregar un Directorio de Origen Extra
Un caso de uso frecuente para este plugin es agregar un directorio de origen extra, ya que Maven generalmente solo admite uno por defecto (`src/main/java`). Aquí te muestro cómo configurar el objetivo `add-source` para incluir un directorio de origen adicional:

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
                            <source>path/to/your/extra/source/directory</source>
                        </sources>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

- **`<id>`**: Un identificador único para esta ejecución (por ejemplo, `add-source`).
- **`<phase>`**: La fase del ciclo de vida de Maven cuando se ejecuta el objetivo (por ejemplo, `generate-sources` asegura que el directorio se agregue temprano en la construcción).
- **`<goals>`**: Especifica el objetivo a ejecutar (`add-source` en este caso).
- **`<configuration>`**: Define el directorio de origen extra (reemplaza `path/to/your/extra/source/directory` con tu ruta real, por ejemplo, `src/main/generated`).

Cuando ejecutes un comando Maven como `mvn compile`, Maven incluirá este directorio adicional como una carpeta de origen.

### Notas Adicionales
- **Compatibilidad de Versiones**: Desde la versión 3.0.0, el plugin requiere Maven 3 o superior. Si estás usando una versión anterior de Maven, necesitarás usar la versión 1.12 o anterior del plugin.
- **Múltiples Objetivos**: Puedes definir múltiples bloques `<execution>` dentro del mismo plugin para ejecutar diferentes objetivos. Por ejemplo, podrías agregar tanto directorios de origen como de origen de pruebas incluyendo ejecuciones para `add-source` y `add-test-source`.
- **Ejecutar el Plugin**: Una vez configurado, ejecutar un comando Maven (por ejemplo, `mvn clean install`) desencadenará los objetivos del plugin durante las fases especificadas.

### Recursos Adicionales
Para más detalles y ejemplos de otros objetivos, consulta la [página de uso oficial](https://www.mojohaus.org/build-helper-maven-plugin/usage.html). Esta página proporciona documentación completa y configuraciones de ejemplo para todos los objetivos disponibles.

### Pensamientos Finales
El Build Helper Maven Plugin es una poderosa adición a tu kit de herramientas Maven, especialmente para proyectos que requieren configuraciones de construcción no estándar. Al incluirlo en tu `pom.xml` y configurar los objetivos apropiados, puedes personalizar tu proceso de construcción para satisfacer necesidades específicas. Aunque tuvo sus orígenes en Codehaus, su hogar actual es MojoHaus, y sigue siendo una opción confiable para mejorar las construcciones de Maven.