---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Impecable en Proyectos Maven Multi-Módulo
translated: true
type: note
---

### Spotless en Proyectos Maven Multi-Módulo

Spotless es un plugin de formato de código disponible tanto para Maven como para Gradle. Basándome en tu mención del flag `-pl` (lista de proyectos) de Maven, asumiré que estás usando el **plugin Spotless para Maven** en un proyecto Java multi-módulo. Esto te permite ejecutar verificaciones de formato (por ejemplo, mediante `spotless:check`) o aplicar correcciones (por ejemplo, mediante `spotless:apply`) de forma selectiva en módulos específicos, lo cual es eficiente para proyectos grandes donde quizás solo necesites formatear ciertos módulos (por ejemplo, durante el desarrollo en un submódulo específico).

#### Prerrequisitos
- Tu proyecto usa Maven con una estructura multi-módulo (definida en un `pom.xml` padre con `<modules>...</modules>`).
- El plugin Spotless para Maven está configurado en tu proyecto (típicamente en el POM padre o en los POMs de módulos individuales). Si no, agrégalo a tu POM:
  ```xml
  <build>
    <plugins>
      <plugin>
        <groupId>com.diffplug.spotless</groupId>
        <artifactId>spotless-maven-plugin</artifactId>
        <version>2.43.0</version>  <!-- Usa la última versión -->
        <configuration>
          <!-- Tus reglas de formato aquí, p.ej., para Java, Groovy -->
        </configuration>
      </plugin>
    </plugins>
  </build>
  ```
  - Las reglas comunes incluyen Google Java Format, Eclipse JDT para Java, o personalizaciones para imports, espaciado, etc.
  - Spotless soporta muchos tipos de archivo (Java, Kotlin, XML, etc.) y se integra bien con herramientas de CI para hooks pre-commit (mediante el goal `spotless:check`, que falla las builds con código sin formatear).

#### Usando `-pl` para Controlar el Formato por Módulo
El flag `-pl` (lista de proyectos) de Maven te permite especificar una lista separada por comas de módulos a incluir en la ejecución de la build/plugin. Por defecto, Maven se ejecuta en todos los módulos, pero `-pl` lo restringe, ahorrando tiempo y evitando trabajo innecesario en módulos no afectados.

- **Estructura Básica del Comando**:
  - Para verificar el formato (sin aplicar cambios): `mvn spotless:check -pl modulo1,modulo2`
  - Para aplicar correcciones de formato: `mvn spotless:apply -pl modulo1,modulo2`
  - Reemplaza `modulo1,modulo2` con los nombres reales de los módulos (por ejemplo, rutas relativas desde la raíz, como `core,api`).

- **Ejemplos**:
  1. **Verificar el formato solo en el módulo `core`**:
     ```
     mvn spotless:check -pl core
     ```
     - Esto escanea y valida solo los archivos fuente de `core`. Si existen problemas de formato, la build falla con detalles (por ejemplo, "Ejecuta `spotless:apply` para corregir").

  2. **Aplicar formato a múltiples módulos (`api` y `utils`)**:
     ```
     mvn spotless:apply -pl api,utils
     ```
     - Esto modifica los archivos in-place para que coincidan con tus reglas de Spotless. Siempre confirma los cambios después para evitar sorpresas en el control de versiones.

  3. **Excluir módulos específicos durante una ejecución completa del proyecto**: Usa `-pl !moduloAExcluir` para ejecutar en todo *excepto* en ciertos módulos (Maven 3.2.1+ soporta negación con `!`).
     - Ejemplo: `mvn spotless:check -pl !legacy` (se ejecuta en todos los módulos excepto en `legacy`).

- **Consejos para Eficiencia**:
  - **Ejecución en Paralelo**: Añade `-T 4` para builds multi-hilo (por ejemplo, `mvn spotless:check -pl core,api -T 4`).
  - **Ejecución de Prueba**: Usa `spotless:check` primero para previsualizar problemas sin realizar cambios—es idempotente y seguro.
  - **Integración con IDE/Control de Versiones**: Configura Spotless para que se ejecute al guardar/confirmar en tu IDE (por ejemplo, IntelliJ mediante el plugin Spotless) o úsalo como un hook pre-commit (mediante herramientas como pre-commit o hooks de Git) para verificaciones automatizadas.
  - **Manejo de Resolución del Reactor**: Si las dependencias de los módulos son complejas, Maven las resuelve automáticamente al usar `-pl`, asegurando que los módulos dependientes se procesen primero si es necesario.
  - **Problemas Comunes**:
    - Si `-pl` no funciona, asegúrate de que los módulos estén definidos en `<modules>` y usa rutas completamente calificadas si hay ambigüedades (por ejemplo, `-pl :core` para configuraciones multi-repositorio).
    - Para usuarios de Gradle (si te referías al plugin Spotless para Gradle), el equivalente es `-p` para rutas de proyecto, pero tu consulta especifica `-pl`, por lo que se asume Maven. Si es Gradle, cambia a plugins como `gradle task -p submodulo`.

Para la documentación completa, consulta la [documentación del Plugin Spotless para Maven](https://github.com/diffplug/spotless/tree/v2.43.0/plugin-maven). Si tu configuración es diferente (por ejemplo, Gradle), proporciona más detalles para un consejo más específico.