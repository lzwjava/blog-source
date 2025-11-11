---
audio: false
generated: true
lang: es
layout: post
title: Análisis de Argumentos de Línea de Comandos en Java
translated: true
type: note
---

Para usar `net.sourceforge.argparse4j`, una biblioteca Java para analizar argumentos de línea de comandos inspirada en `argparse` de Python, sigue estos pasos:

---

### 1. **Agregar la Dependencia**
Para incluir `argparse4j` en tu proyecto, agrégalo como una dependencia. Si usas Maven, actualiza tu `pom.xml` con lo siguiente:

```xml
<dependency>
    <groupId>net.sourceforge.argparse4j</groupId>
    <artifactId>argparse4j</artifactId>
    <version>0.9.0</version>
</dependency>
```

Para otras herramientas de build como Gradle, consulta el [Maven Central Repository](https://central.sonatype.com/artifact/net.sourceforge.argparse4j/argparse4j) para la configuración equivalente.

---

### 2. **Crear un Objeto `ArgumentParser`**
Comienza creando una instancia de `ArgumentParser` usando `ArgumentParsers.newFor("prog").build()`, donde `"prog"` es el nombre de tu programa. También puedes agregar una descripción y habilitar la generación automática de ayuda.

**Ejemplo:**
```java
import net.sourceforge.argparse4j.ArgumentParsers;
import net.sourceforge.argparse4j.inf.ArgumentParser;

ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
    .defaultHelp(true)  // Habilita la opción -h/--help
    .description("Calcular el checksum de los archivos dados.");
```

---

### 3. **Agregar Argumentos**
Define los argumentos de línea de comandos que tu programa aceptará usando `parser.addArgument()`. Puedes especificar:
- **Argumentos opcionales** (ej., `-t`, `--type`) con flags, opciones, valores por defecto y texto de ayuda.
- **Argumentos posicionales** (ej., `file`) con soporte opcional de longitud variable usando `.nargs("*")`.

**Ejemplo:**
```java
parser.addArgument("-t", "--type")
    .choices("SHA-256", "SHA-512", "SHA1")  // Restringir a estas opciones
    .setDefault("SHA-256")                  // Valor por defecto si no se proporciona
    .help("Especificar la función hash a usar");  // Descripción para el mensaje de ayuda

parser.addArgument("file")
    .nargs("*")                             // Acepta cero o más argumentos
    .help("Archivo para calcular el checksum");    // Descripción para el mensaje de ayuda
```

---

### 4. **Analizar los Argumentos de Línea de Comandos**
Analiza los argumentos de línea de comandos (normalmente pasados como `String[] args` desde tu método `main`) usando `parser.parseArgs()`. Envuelve esto en un bloque try-catch para manejar los errores de análisis correctamente.

**Ejemplo:**
```java
import net.sourceforge.argparse4j.inf.Namespace;
import net.sourceforge.argparse4j.inf.ArgumentParserException;

public class Checksum {
    public static void main(String[] args) {
        ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
            .defaultHelp(true)
            .description("Calcular el checksum de los archivos dados.");
        
        parser.addArgument("-t", "--type")
            .choices("SHA-256", "SHA-512", "SHA1").setDefault("SHA-256")
            .help("Especificar la función hash a usar");
        parser.addArgument("file").nargs("*")
            .help("Archivo para calcular el checksum");

        Namespace ns = null;
        try {
            ns = parser.parseArgs(args);  // Analizar los argumentos
        } catch (ArgumentParserException e) {
            parser.handleError(e);        // Imprimir error y mensaje de ayuda
            System.exit(1);               // Salir en caso de error
        }
    }
}
```

---

### 5. **Acceder a los Valores Analizados**
El método `parseArgs()` devuelve un objeto `Namespace` que contiene los valores de los argumentos analizados. Usa métodos como `getString()` o `getList()` para recuperarlos.

**Ejemplo:**
```java
String hashType = ns.getString("type");  // ej., "SHA-256"
List<String> files = ns.getList("file"); // Lista de nombres de archivo

System.out.println("Tipo de Hash: " + hashType);
System.out.println("Archivos: " + files);
```

---

### Uniendo Todo
Aquí tienes un ejemplo completo:

```java
import net.sourceforge.argparse4j.ArgumentParsers;
import net.sourceforge.argparse4j.inf.ArgumentParser;
import net.sourceforge.argparse4j.inf.ArgumentParserException;
import net.sourceforge.argparse4j.inf.Namespace;
import java.util.List;

public class Checksum {
    public static void main(String[] args) {
        // Paso 2: Crear el analizador
        ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
            .defaultHelp(true)
            .description("Calcular el checksum de los archivos dados.");

        // Paso 3: Agregar argumentos
        parser.addArgument("-t", "--type")
            .choices("SHA-256", "SHA-512", "SHA1").setDefault("SHA-256")
            .help("Especificar la función hash a usar");
        parser.addArgument("file").nargs("*")
            .help("Archivo para calcular el checksum");

        // Paso 4: Analizar argumentos
        Namespace ns = null;
        try {
            ns = parser.parseArgs(args);
        } catch (ArgumentParserException e) {
            parser.handleError(e);
            System.exit(1);
        }

        // Paso 5: Acceder a los valores analizados
        String hashType = ns.getString("type");
        List<String> files = ns.getList("file");

        // Ejemplo de salida
        System.out.println("Tipo de Hash: " + hashType);
        System.out.println("Archivos: " + files);
    }
}
```

---

### Características Adicionales
- **Ayuda Automática**: Ejecuta tu programa con `-h` o `--help` para ver un mensaje de ayuda generado automáticamente.
- **Subcomandos**: Usa `parser.addSubparsers()` para comandos complejos (ej., `git commit`, `git push`).
- **Anotaciones**: Vincula argumentos a campos de clase usando anotaciones (consulta el manual de usuario para más detalles).

Para un uso más avanzado, consulta el [Manual de Usuario de Argparse4j](https://argparse4j.github.io/userguide.html).

---

Este flujo de trabajo te permite analizar y manejar fácilmente los argumentos de línea de comandos en tu aplicación Java usando `net.sourceforge.argparse4j`.