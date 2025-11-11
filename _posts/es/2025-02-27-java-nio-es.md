---
audio: false
generated: true
lang: es
layout: post
title: Uso de NIO en Java
translated: true
type: note
---

Permíteme explicar cómo usar NIO (New Input/Output) en Java con algunos ejemplos prácticos. Java NIO es una API de E/S no bloqueante que proporciona una forma más eficiente de manejar operaciones de E/S en comparación con el paquete tradicional java.io.

Aquí tienes un desglose de los componentes clave y un ejemplo simple:

### Componentes Clave de NIO
1.  **Buffers**: Contenedores para datos (por ejemplo, `ByteBuffer`).
2.  **Channels**: Flujos para leer/escribir datos (por ejemplo, `FileChannel`, `SocketChannel`).
3.  **Selectors**: Para multiplexar múltiples canales en modo no bloqueante.

### Ejemplo Básico: Leer un Archivo con NIO
Aquí se muestra cómo puedes leer un archivo usando `FileChannel` y `ByteBuffer`:

```java
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

public class NIOFileReader {
    public static void main(String[] args) {
        try {
            // Abrir un canal de archivo
            FileChannel fileChannel = FileChannel.open(
                Paths.get("example.txt"), 
                StandardOpenOption.READ
            );

            // Asignar un buffer
            ByteBuffer buffer = ByteBuffer.allocate(1024);

            // Leer datos en el buffer
            while (fileChannel.read(buffer) > 0) {
                // Voltear el buffer para prepararlo para la lectura
                buffer.flip();

                // Procesar los datos
                while (buffer.hasRemaining()) {
                    System.out.print((char) buffer.get());
                }

                // Limpiar el buffer para la siguiente lectura
                buffer.clear();
            }

            // Cerrar el canal
            fileChannel.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### Cómo Funciona
1.  **FileChannel**: Abre una conexión al archivo.
2.  **ByteBuffer**: Actúa como un almacenamiento temporal para los datos. Asignas su tamaño (por ejemplo, 1024 bytes).
3.  **Operaciones del Buffer**:
    - `flip()`: Prepara el buffer para ser leído después de escribir datos en él.
    - `clear()`: Reinicia el buffer para el siguiente fragmento de datos.
4.  **Lectura**: El método `read()` llena el buffer y extraes los datos byte a byte.

---

### Escribir a un Archivo con NIO
Aquí tienes un ejemplo de cómo escribir datos en un archivo:

```java
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

public class NIOFileWriter {
    public static void main(String[] args) {
        try {
            // Abrir un canal de archivo para escribir
            FileChannel fileChannel = FileChannel.open(
                Paths.get("output.txt"), 
                StandardOpenOption.CREATE, 
                StandardOpenOption.WRITE
            );

            // Datos a escribir
            String data = "Hello, NIO!";
            ByteBuffer buffer = ByteBuffer.allocate(1024);

            // Poner datos en el buffer
            buffer.put(data.getBytes());

            // Voltear el buffer para prepararlo para la escritura
            buffer.flip();

            // Escribir el buffer en el archivo
            fileChannel.write(buffer);

            // Cerrar el canal
            fileChannel.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

---

### Ejemplo No Bloqueante con Selector
Para programación de red (por ejemplo, un servidor), puedes usar `Selector` con `SocketChannel`:

```java
import java.nio.ByteBuffer;
import java.nio.channels.SelectionKey;
import java.nio.channels.Selector;
import java.nio.channels.ServerSocketChannel;
import java.nio.channels.SocketChannel;
import java.net.InetSocketAddress;
import java.util.Iterator;

public class NIOServer {
    public static void main(String[] args) throws Exception {
        // Abrir un selector
        Selector selector = Selector.open();

        // Abrir un canal de socket de servidor
        ServerSocketChannel serverChannel = ServerSocketChannel.open();
        serverChannel.bind(new InetSocketAddress(8080));
        serverChannel.configureBlocking(false);

        // Registrar el canal con el selector
        serverChannel.register(selector, SelectionKey.OP_ACCEPT);

        System.out.println("Server started on port 8080");

        while (true) {
            selector.select(); // Bloquea hasta que ocurran eventos
            Iterator<SelectionKey> keys = selector.selectedKeys().iterator();

            while (keys.hasNext()) {
                SelectionKey key = keys.next();
                keys.remove();

                if (key.isAcceptable()) {
                    // Aceptar nueva conexión
                    SocketChannel client = serverChannel.accept();
                    client.configureBlocking(false);
                    client.register(selector, SelectionKey.OP_READ);
                    System.out.println("Client connected");
                } else if (key.isReadable()) {
                    // Leer datos del cliente
                    SocketChannel client = (SocketChannel) key.channel();
                    ByteBuffer buffer = ByteBuffer.allocate(1024);
                    int bytesRead = client.read(buffer);
                    if (bytesRead == -1) {
                        client.close();
                    } else {
                        buffer.flip();
                        System.out.println("Received: " + new String(buffer.array(), 0, bytesRead));
                        buffer.clear();
                    }
                }
            }
        }
    }
}
```

### Consejos para Usar NIO
-   **Gestión del Buffer**: Siempre usa `flip()` después de escribir en un buffer y antes de leerlo, y `clear()` cuando lo reutilices.
-   **No Bloqueante**: Usa `configureBlocking(false)` y `Selector` para aplicaciones de red escalables.
-   **Rendimiento**: NIO brilla en escenarios con muchas conexiones concurrentes o transferencias de datos grandes.

¡Házme saber si te gustaría una inmersión más profunda en alguna parte específica!