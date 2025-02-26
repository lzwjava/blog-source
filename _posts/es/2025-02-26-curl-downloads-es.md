---
audio: false
lang: es
layout: post
title: Solucionar problemas de descargas con curl
translated: true
---

Cuando intentas descargar un archivo ZIP de Eclipse desde eclipse.org utilizando `curl -O`, es posible que encuentres un problema en el que se descarga un archivo HTML en lugar del archivo ZIP deseado, acompañado de un error "301 Moved Permanently". Esto ocurre porque la URL que estás utilizando redirige a otra ubicación y `curl` no sigue automáticamente esa redirección al archivo real. Aquí tienes cómo solucionarlo:

### Comprender el Problema

- **301 Moved Permanently**: Este código de estado HTTP significa que el recurso (el archivo ZIP) se ha movido permanentemente a una nueva URL. Los servidores a menudo utilizan redirecciones para enlaces de descarga que apuntan a sitios espejo o ubicaciones actualizadas.
- **Comportamiento de `curl -O`**: La opción `-O` le indica a `curl` que guarde el contenido descargado en un archivo con el nombre del archivo remoto. Sin embargo, sin manejar explícitamente las redirecciones, `curl` podría guardar el contenido de la respuesta de redirección intermedia (a menudo una página HTML) en lugar de seguirla hasta el archivo ZIP.

### Solución

Para asegurarte de que `curl` siga la redirección y descargue el archivo ZIP de Eclipse, usa la opción `-L` junto con `-O`. La bandera `-L` instruye a `curl` a seguir cualquier redirección hasta que alcance el destino final.

#### Comando

```bash
curl -L -O <URL>
```

- **`-L`**: Sigue las redirecciones, como la redirección 301, a la nueva ubicación.
- **`-O`**: Guarda el archivo con el nombre original de la URL final.
- **`<URL>`**: Reemplaza esto con la URL específica de descarga de Eclipse, como `https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip`.

### Instrucciones Paso a Paso

1. **Encontrar la URL Correcta**:
   - Visita el sitio web de Eclipse (por ejemplo, `https://www.eclipse.org/downloads/`).
   - Selecciona el paquete deseado (por ejemplo, Eclipse IDE for Java Developers).
   - Haz clic derecho en el enlace o botón de descarga y copia la URL. Alternativamente, usa las herramientas de desarrollo de tu navegador (F12, pestaña Network) para capturar la URL exacta cuando hagas clic en descargar.

2. **Ejecutar el Comando**:
   - Abre tu terminal.
   - Ejecuta el comando `curl` con las opciones `-L` y `-O`, usando la URL que copiaste:
     ```bash
     curl -L -O https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip
     ```
   - Esto debería descargar el archivo ZIP (por ejemplo, `eclipse-java-2023-03-R-win32-x86_64.zip`) a tu directorio actual.

### Solución de Problemas

Si aún encuentras problemas, intenta estos pasos adicionales:

- **Verificar Redirecciones con Salida Verbosa**:
  - Usa la opción `-v` para ver información detallada sobre la solicitud y las redirecciones:
    ```bash
    curl -v -L -O <URL>
    ```
  - Mira el encabezado `Location` en la respuesta 301 para ver a dónde se redirige. Si apunta a una página HTML en lugar de un archivo ZIP, la URL podría no ser el enlace de descarga directo.

- **Verificar la URL**:
  - Eclipse a menudo usa un script `download.php` que puede redirigir a un espejo. Asegúrate de que tu URL sea el enlace directo al archivo ZIP o un enlace de redirección que se resuelva al archivo. Por ejemplo, un enlace de espejo directo podría verse así:
    ```bash
    curl -L -O https://mirror.its.dal.ca/eclipse/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip
    ```

- **Establecer un Encabezado User-Agent**:
  - Algunos servidores se comportan de manera diferente según el cliente. Si el servidor devuelve HTML porque detecta `curl`, simula un navegador agregando un User-Agent:
    ```bash
    curl -L -O -A "Mozilla/5.0" <URL>
    ```

### Por Qué Funciona

El sitio web de Eclipse puede redirigir las solicitudes de descarga a un espejo o una URL actualizada. Sin `-L`, `curl -O` guarda la respuesta de redirección (una página HTML) en lugar de seguirla. Agregar `-L` asegura que `curl` rastree la redirección 301 hasta el archivo ZIP real, resolviendo el problema.

Siguiendo estos pasos, deberías poder descargar el archivo ZIP de Eclipse desde eclipse.org utilizando `curl`.