---
audio: false
generated: true
lang: es
layout: post
title: Solucionar descargas con curl
translated: true
type: note
---

Al intentar descargar un archivo ZIP de Eclipse desde eclipse.org usando `curl -O`, puedes encontrarte con que descarga un archivo HTML en lugar del archivo ZIP deseado, acompañado de un error "301 Movido Permanentemente". Esto sucede porque la URL que estás usando redirige a otra ubicación, y `curl` no está siguiendo automáticamente esa redirección hasta el archivo real. Aquí se explica cómo solucionarlo:

### Entendiendo el Problema

- **301 Movido Permanentemente**: Este código de estado HTTP significa que el recurso (el archivo ZIP) se ha movido permanentemente a una nueva URL. Los servidores a menudo usan redirecciones para los enlaces de descarga para apuntar a sitios espejo o ubicaciones actualizadas.
- **Comportamiento de `curl -O`**: La opción `-O` le dice a `curl` que guarde el contenido descargado en un archivo con el nombre del archivo remoto. Sin embargo, sin manejar explícitamente las redirecciones, `curl` podría guardar el contenido de la respuesta de redirección intermedia (a menudo una página HTML) en lugar de seguirla hasta el archivo ZIP.

### Solución

Para asegurarse de que `curl` siga la redirección y descargue el archivo ZIP de Eclipse, usa la opción `-L` junto con `-O`. La bandera `-L` instruye a `curl` a seguir cualquier redirección hasta que llegue al destino final.

#### Comando

```bash
curl -L -O <URL>
```

- **`-L`**: Sigue las redirecciones, como la redirección 301, a la nueva ubicación.
- **`-O`**: Guarda el archivo con el nombre original de la URL final.
- **`<URL>`**: Reemplaza esto con la URL de descarga específica de Eclipse, como `https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip`.

### Instrucciones Paso a Paso

1. **Encuentra la URL Correcta**:
   - Visita el sitio web de Eclipse (por ejemplo, `https://www.eclipse.org/downloads/`).
   - Selecciona el paquete deseado (por ejemplo, Eclipse IDE for Java Developers).
   - Haz clic derecho en el enlace o botón de descarga y copia la URL. Alternativamente, usa las herramientas de desarrollador de tu navegador (F12, pestaña Red/Network) para capturar la URL exacta cuando hagas clic en descargar.

2. **Ejecuta el Comando**:
   - Abre tu terminal.
   - Ejecuta el comando `curl` con las opciones `-L` y `-O`, usando la URL que copiaste:
     ```bash
     curl -L -O https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip
     ```
   - Esto debería descargar el archivo ZIP (por ejemplo, `eclipse-java-2023-03-R-win32-x86_64.zip`) en tu directorio actual.

### Resolución de Problemas

Si aún encuentras problemas, intenta estos pasos adicionales:

- **Comprueba las Redirecciones con Salida Detallada**:
  - Usa la opción `-v` para ver información detallada sobre la solicitud y las redirecciones:
    ```bash
    curl -v -L -O <URL>
    ```
  - Busca el encabezado `Location` en la respuesta 301 para ver a dónde redirige. Si está apuntando a una página HTML en lugar de a un archivo ZIP, es posible que la URL no sea el enlace de descarga directo.

- **Verifica la URL**:
  - Eclipse a menudo usa un script `download.php` que puede redirigir a un espejo. Asegúrate de que tu URL sea el enlace directo al archivo ZIP o un enlace de redirección que resuelva en el archivo. Por ejemplo, un enlace directo a un espejo podría verse así:
    ```bash
    curl -L -O https://mirror.its.dal.ca/eclipse/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip
    ```

- **Establece un Encabezado User-Agent**:
  - Algunos servidores se comportan de manera diferente según el cliente. Si el servidor devuelve HTML porque detecta `curl`, imita un navegador añadiendo un User-Agent:
    ```bash
    curl -L -O -A "Mozilla/5.0" <URL>
    ```

### Por Qué Esto Funciona

El sitio web de Eclipse puede redirigir las solicitudes de descarga a un espejo o a una URL actualizada. Sin `-L`, `curl -O` guarda la respuesta de redirección (una página HTML) en lugar de seguirla. Añadir `-L` asegura que `curl` rastree la redirección 301 hasta el archivo ZIP real, resolviendo el problema.

Siguiendo estos pasos, deberías descargar exitosamente el archivo ZIP de Eclipse desde eclipse.org usando `curl`.