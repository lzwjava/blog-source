---
audio: false
generated: true
lang: es
layout: post
title: Lectura de Entrada de Consola en Java
translated: true
type: note
---

Para usar el paquete `org.jline.reader` en Java, que es parte de la biblioteca JLine para manejar la entrada de consola con funciones avanzadas como edición de línea, historial y completado, sigue estos pasos. Esta guía proporciona un enfoque completo y práctico para comenzar.

### Prerrequisitos
Asegúrate de tener la biblioteca JLine agregada a tu proyecto. Si estás usando Maven, incluye la siguiente dependencia en tu `pom.xml`:

```xml
<dependency>
    <groupId>org.jline</groupId>
    <artifactId>jline</artifactId>
    <version>3.21.0</version> <!-- Usa la última versión -->
</dependency>
```

### Pasos Básicos para Usar `org.jline.reader`

1. **Crear una Instancia de Terminal**
   - Usa la clase `TerminalBuilder` de `org.jline.terminal` para crear un objeto `Terminal`. Este representa el entorno de consola donde se leerá la entrada.
   - Ejemplo:
     ```java
     import org.jline.terminal.Terminal;
     import org.jline.terminal.TerminalBuilder;

     Terminal terminal = TerminalBuilder.builder().build();
     ```
   - El método `build()` crea un terminal predeterminado adecuado para la mayoría de los entornos. Puedes personalizarlo más (por ejemplo, estableciendo el tipo de terminal), pero el predeterminado suele ser suficiente.

2. **Crear una Instancia de LineReader**
   - Usa la clase `LineReaderBuilder` de `org.jline.reader` para crear un objeto `LineReader`, pasándole la instancia de `Terminal`.
   - El `LineReader` es la interfaz principal para leer la entrada del usuario con las características de JLine.
   - Ejemplo:
     ```java
     import org.jline.reader.LineReader;
     import org.jline.reader.LineReaderBuilder;

     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .build();
     ```

3. **Leer la Entrada del Usuario**
   - Usa el método `readLine()` de `LineReader` para leer una línea de texto ingresada por el usuario. Opcionalmente, puedes especificar un prompt para mostrar.
   - Ejemplo:
     ```java
     String line = reader.readLine("> ");
     ```
   - Esto muestra `> ` como un prompt, espera la entrada del usuario y devuelve la cadena ingresada cuando el usuario presiona Enter.

### Ejemplo Simple
Aquí tienes un ejemplo completo y mínimo que lee la entrada del usuario en un bucle hasta que el usuario escribe "exit":

```java
import org.jline.reader.LineReader;
import org.jline.reader.LineReaderBuilder;
import org.jline.terminal.Terminal;
import org.jline.terminal.TerminalBuilder;

public class ConsoleExample {
    public static void main(String[] args) throws Exception {
        // Crear Terminal
        Terminal terminal = TerminalBuilder.builder().build();
        
        // Crear LineReader
        LineReader reader = LineReaderBuilder.builder()
            .terminal(terminal)
            .build();
        
        // Leer entrada en un bucle
        String line;
        while ((line = reader.readLine("> ")) != null) {
            System.out.println("Ingresaste: " + line);
            if (line.equals("exit")) {
                break;
            }
        }
    }
}
```

- **Salida**: Cuando ejecutas esto, muestra un prompt `> `. Puedes escribir texto, usar la tecla de retroceso o las flechas para editar (características no fácilmente disponibles con `System.in`), y presionar Enter. Escribir "exit" termina el programa.

### Características Opcionales
Puedes mejorar el `LineReader` con funcionalidad adicional:

#### 1. **Habilitar el Historial de Comandos**
   - Agrega un objeto `History` para almacenar y recordar entradas anteriores (por ejemplo, usando las teclas de flecha arriba/abajo).
   - Ejemplo:
     ```java
     import org.jline.reader.impl.history.DefaultHistory;
     import org.jline.reader.History;

     History history = new DefaultHistory();
     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .history(history)
         .build();
     ```
   - Ahora, el usuario puede navegar a través de su historial de entradas.

#### 2. **Agregar Autocompletado**
   - Implementa un `Completer` para sugerir completados cuando el usuario presiona Tab.
   - Ejemplo con un completer de cadenas simple:
     ```java
     import org.jline.reader.Completer;
     import org.jline.reader.impl.completer.StringsCompleter;

     Completer completer = new StringsCompleter("foo", "bar", "baz");
     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .completer(completer)
         .build();
     ```
   - Escribir "f" y presionar Tab sugiere "foo".

#### 3. **Leer Contraseñas (Entrada Enmascarada)**
   - Usa `readLine()` con un carácter de enmascaramiento para ocultar la entrada (por ejemplo, para contraseñas).
   - Ejemplo:
     ```java
     String password = reader.readLine("Ingresa la contraseña: ", '*');
     ```
   - Muestra asteriscos (`*`) en lugar de los caracteres escritos.

### Gestión de Recursos
Para aplicaciones robustas, cierra el `Terminal` cuando termines para liberar recursos. Dado que `Terminal` implementa `Closeable`, usa un bloque try-with-resources:

```java
try (Terminal terminal = TerminalBuilder.builder().build()) {
    LineReader reader = LineReaderBuilder.builder()
        .terminal(terminal)
        .build();
    String line = reader.readLine("> ");
    System.out.println("Ingresaste: " + line);
}
```

### ¿Por Qué Usar `org.jline.reader`?
A diferencia de la entrada básica con `System.in` y `BufferedReader`, `org.jline.reader` proporciona:
- **Edición de Línea**: Retroceso, movimiento del cursor, etc.
- **Historial**: Recordar entradas anteriores.
- **Completado**: Auto-sugerir opciones.
- **Manejo de Terminal Multiplataforma**: Funciona de manera consistente en diferentes entornos.

### Notas
- Si no especificas un `Terminal` en `LineReaderBuilder`, crea uno predeterminado internamente, por lo que `LineReader reader = LineReaderBuilder.builder().build();` funciona para casos simples.
- Evita llamar a `readLine()` desde múltiples hilos simultáneamente, ya que `LineReader` no es seguro para hilos para lecturas concurrentes.
- Para casos de uso avanzados (por ejemplo, entrada multilínea, enlaces de teclas personalizados), explora características adicionales de JLine como parsers o mapas de teclas.

Esto cubre lo esencial del uso de `org.jline.reader` para leer la entrada de consola en Java de manera efectiva. ¡Comienza con la configuración básica y agrega características como historial o completado según sea necesario para tu aplicación