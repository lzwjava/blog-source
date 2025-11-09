---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast:free
title: Ubicaciones de Código Fuente y Clases de JavaCC
translated: true
type: note
---

### Descripción general de JavaCC
JavaCC (Java Compiler Compiler) es una herramienta que genera código fuente Java (por ejemplo, clases de parser) a partir de archivos de especificación de gramática (archivos .jj). **No** compila código directamente a bytecode (archivos .class)—eso lo maneja un compilador de Java estándar como `javac`. Si estás usando JavaCC de manera programática (por ejemplo, en un IDE o entorno de ejecución) para generar y compilar código dinámico, las ubicaciones de salida dependen de cómo lo configures. Explicaré esto paso a paso, basándome en el comportamiento estándar de JavaCC y los patrones de uso comunes.

### Dónde genera JavaCC los archivos fuente
- **Ubicación de salida predeterminada**: JavaCC genera los archivos `.java` en el **directorio de trabajo actual** (o en un subdirectorio llamado "output" si no se especifica). Puedes anular esto con opciones de línea de comandos como `-OUTPUT_DIRECTORY=<ruta>` o programáticamente mediante la clase `JavaCCOptions` si lo invocas en código.
- **Ejemplo de uso en línea de comandos**:
  ```
  javacc -OUTPUT_DIRECTORY=/ruta/a/generado MiGramatica.jj
  ```
  Esto crearía archivos `.java` (por ejemplo, `Token`, `Parser`, `ParseException`) en `/ruta/a/generado`.
- **Uso programático**: Si estás llamando a JavaCC desde dentro de tu aplicación Java (por ejemplo, usando `org.javacc.JavaCC.main()` o APIs similares), puedes establecer opciones para especificar la ruta de salida. Los archivos fuente son simplemente archivos `.java` planos que necesitan compilación posterior.

Esto se alinea con la documentación oficial de JavaCC (por ejemplo, del proyecto heredado JavaCC en SourceForge o distribuciones basadas en Maven), que establece que las clases generadas se envían al directorio especificado como código fuente, no como bytecode.

### Dónde se almacenan las clases compiladas si compilas el código generado
JavaCC en sí mismo no compila a archivos `.class`—debes hacer esto manualmente o automatizarlo en tu código. Esto es lo que sucede a continuación:

- **Compilación manual**: Usa `javac` en los archivos `.java` generados:
  ```
  javac -d /ruta/a/clases MiParserGenerado.java
  ```
  - El flag `-d` especifica el directorio de salida para los archivos `.class`, a menudo una carpeta `classes/` o el destino de compilación de tu proyecto (por ejemplo, `target/classes/` en Maven/Gradle).
  - Ubicaciones comunes: `bin/`, `build/classes/`, o `target/classes/` dependiendo de tu sistema de compilación (por ejemplo, Ant, Maven).

- **Compilación dinámica en código**: Si estás usando JavaCC en tiempo de ejecución para generar parsers para código dinámico (por ejemplo, para interpretación de scripts o parsing sobre la marcha), normalmente harías:
  1. Generar los archivos `.java` programáticamente (por ejemplo, escribiendo en un directorio temporal como `System.getProperty("java.io.tmpdir")`).
  2. Compilarlos usando la API del Compilador de Java (javax.tools.JavaCompiler) o una biblioteca como Janino.
     - Ejemplo: Establecer la salida de compilación a un directorio personalizado, como `new File("generated/classes")`.
     - Los archivos `.class` compilados se almacenan en ese directorio. En tiempo de ejecución, usa un ClassLoader personalizado para cargarlos desde allí o desde búferes en memoria.
  - **Valor predeterminado de la JVM**: Sin rutas personalizadas, las clases podrían ir al `target/classes` predeterminado si se usan herramientas de compilación, o a cualquier directorio que especifiques en la tarea de compilación.

- **Escenarios dinámicos comunes**:
  - **Compilación en memoria**: Bibliotecas como la API del Compilador permiten compilar sin escribir en disco, almacenando el bytecode en memoria mediante `ClassLoader.defineClass()`. No ocurre almacenamiento físico.
  - **Almacenamiento temporal**: Si el código generado se compila y persiste, a menudo va a `/tmp/` en sistemas tipo Unix o a carpetas temporales. Para aplicaciones en producción, usa un directorio dedicado `generated/` o `cache/` en el sistema de archivos de tu proyecto.
  - **Frameworks**: Herramientas como ANTLR (alternativa a JavaCC) o ejecutores personalizados pueden automatizar esto, almacenando clases en la RAM o en una carpeta del classpath (por ejemplo, entradas de `CLASSPATH`).

### Consideraciones clave y mejores prácticas
- **Seguridad en tiempo de ejecución**: Compilar código dinámicamente conlleva riesgos (por ejemplo, problemas de seguridad). Asegúrate de que las gramáticas generadas por el usuario estén en un sandbox.
- **Integración con herramientas de compilación**: Si usas Maven o Gradle, los plugins de JavaCC (por ejemplo, `javcc-maven-plugin`) envían la salida a `target/generated-sources/javacc/` para las fuentes y a `target/classes/` para las clases compiladas, configurable en tu `pom.xml` o `build.gradle`.
- **Depuración**: Si la compilación falla, revisa la salida de error o los registros de JavaCC. Los archivos generados normalmente se almacenan donde se ejecuta tu aplicación, no globalmente.
- **Evidencia de la documentación**: Según la guía oficial de JavaCC (javacc.github.io o documentación heredada), la salida está basada en directorios y el manejo posterior a la compilación es responsabilidad del usuario. Ejemplos del mundo real en repositorios de GitHub (por ejemplo, busca usos de JavaCC) muestran directorios de salida personalizados como `src/main/generated/`.

Si esto no coincide con tu configuración (por ejemplo, un framework o IDE específico), ¡proporciona más detalles como tu fragmento de código o entorno, y puedo refinar la respuesta!