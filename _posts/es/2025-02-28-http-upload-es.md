---
audio: false
generated: true
lang: es
layout: post
title: Cargas de Archivos HTTP
translated: true
type: note
---

### Puntos Clave
- La investigación sugiere que las subidas de archivos HTTP suelen utilizar el método POST con multipart/form-data para formularios web, permitiendo múltiples archivos y datos adicionales.
- Parece probable que el método PUT también pueda subir archivos, enviando el contenido en bruto directamente, y se utiliza a menudo en APIs RESTful por su simplicidad.
- La evidencia se inclina hacia que ambos métodos son válidos, siendo la configuración del servidor y el caso de uso los que determinan la elección.

### Descripción General
Subir archivos mediante HTTP es una tarea común para compartir datos en línea, como enviar fotos o documentos a un sitio web. Puedes hacerlo de dos formas principales: usando el método POST con un formato especial llamado multipart/form-data, que es ideal para formularios web, o usando el método PUT, que es más simple y se usa a menudo en APIs modernas. Cada método tiene su propia configuración, y la elección correcta depende de cómo esté configurado el servidor y lo que intentes hacer.

### Cómo Funciona
- **POST con Multipart/Form-Data**: Esto es como empaquetar tu archivo y cualquier información adicional (como una descripción) en partes separadas, marcadas por una cadena límite única. Es común para formularios web donde seleccionas archivos para subir.
- **Método PUT**: Esto envía el contenido del archivo directamente a una URL específica, como actualizar un archivo en el servidor. Es más simple pero requiere que el servidor lo admita.

### Detalle Inesperado
Puede que no esperes que el método PUT, usualmente para actualizar datos, también pueda manejar subidas de archivos, especialmente en APIs, convirtiéndolo en una opción versátil más allá de los formularios tradicionales.

---

### Nota de la Encuesta: Explicación Detallada de las Subidas de Archivos HTTP

Subir archivos mediante HTTP es una operación fundamental en el desarrollo web, que permite a los usuarios compartir datos como imágenes, documentos o medios con los servidores. Este proceso se puede lograr mediante dos métodos principales: el método POST con codificación multipart/form-data, comúnmente utilizado para formularios web, y el método PUT, a menudo utilizado en APIs RESTful para la transmisión directa del contenido del archivo. A continuación, exploramos estos métodos en profundidad, incluyendo su estructura, implementación y consideraciones, para proporcionar una comprensión integral tanto para audiencias técnicas como no técnicas.

#### Multipart/Form-Data: El Estándar para Formularios Web

El tipo de contenido multipart/form-data es la opción predeterminada para las subidas de archivos HTTP, especialmente cuando se trata de formularios HTML. Este método permite la transmisión simultánea de múltiples archivos y datos de formulario adicionales, como campos de texto, dentro de una sola solicitud. El proceso implica construir un cuerpo de solicitud dividido en partes, cada una separada por una cadena límite única, lo que garantiza que el servidor pueda distinguir entre las diferentes piezas de datos.

##### Estructura y Ejemplo
La solicitud comienza estableciendo la cabecera `Content-Type` en `multipart/form-data; boundary=cadena_límite`, donde `cadena_límite` es una cadena elegida aleatoriamente para evitar conflictos con el contenido del archivo. Cada parte del cuerpo incluye cabeceras como `Content-Disposition`, que especifica el nombre del campo del formulario y, para los archivos, el nombre del archivo, y `Content-Type`, que indica el tipo de datos (por ejemplo, `text/plain` para archivos de texto, `image/jpeg` para imágenes JPEG). La parte termina con la cadena límite, y la parte final se marca con el límite seguido de dos guiones.

Considera subir un archivo llamado `example.txt` con el contenido "Hello, world!" a [este endpoint](https://example.com/upload), con el nombre del campo del formulario "file". La solicitud HTTP se vería así:

```
POST /upload HTTP/1.1
Host: example.com
Content-Type: multipart/form-data; boundary=abc123
Content-Length: 101

--abc123
Content-Disposition: form-data; name="file"; filename="example.txt"
Content-Type: text/plain

Hello, world!
--abc123--
```

Aquí, el `Content-Length` se calcula como 101 bytes, teniendo en cuenta el límite, las cabeceras y el contenido del archivo, con los finales de línea usando típicamente CRLF (`\r\n`) para un formato HTTP correcto.

##### Manejo de Múltiples Archivos y Campos de Formulario
Este método sobresale en escenarios que requieren metadatos adicionales. Por ejemplo, si se sube un archivo con una descripción, el cuerpo de la solicitud puede incluir múltiples partes:

```
--abc123
Content-Disposition: form-data; name="description"

Este es mi archivo
--abc123
Content-Disposition: form-data; name="file"; filename="example.txt"
Content-Type: text/plain

Hello, world!
--abc123--
```

El contenido de cada parte se conserva, incluyendo cualquier salto de línea, y el límite garantiza la separación. Esta flexibilidad lo hace ideal para formularios web con elementos `<input type="file">`.

#### Método PUT: Subida Directa de Archivos para APIs RESTful

El método PUT ofrece una alternativa más simple, particularmente en contextos de APIs RESTful, donde el objetivo es actualizar o crear un recurso con el contenido del archivo. A diferencia de multipart/form-data, PUT envía los datos en bruto del archivo directamente en el cuerpo de la solicitud, reduciendo la sobrecarga y simplificando el procesamiento en el servidor.

##### Estructura y Ejemplo
Para subir `example.txt` a [esta URL](https://example.com/files/123), la solicitud sería:

```
PUT /files/123 HTTP/1.1
Host: example.com
Content-Type: text/plain
Content-Length: 13

Hello, world!
```

Aquí, `Content-Type` especifica el tipo MIME del archivo (por ejemplo, `text/plain`), y `Content-Length` es el tamaño del archivo en bytes. Este método es eficiente para archivos grandes, ya que evita la sobrecarga de codificación de multipart/form-data, pero requiere que el servidor esté configurado para manejar solicitudes PUT para subidas de archivos.

##### Casos de Uso y Consideraciones
PUT se usa a menudo en escenarios como actualizar avatares de usuario o subir archivos a un recurso específico en una API. Sin embargo, no todos los servidores admiten PUT para subidas de archivos por defecto, especialmente en entornos de hosting compartido, donde POST con multipart/form-data es más universalmente aceptado. Puede ser necesaria una configuración del servidor, como habilitar el verbo PUT en Apache, como se señala en el [Manual de PHP sobre soporte del método PUT](https://www.php.net/manual/en/features.file-upload.put-method.php).

#### Análisis Comparativo

Para ilustrar las diferencias, considera la siguiente tabla que compara los dos métodos:

| Aspecto                  | POST con Multipart/Form-Data          | PUT con Contenido en Bruto          |
|-------------------------|----------------------------------------|---------------------------------------|
| **Caso de Uso**          | Formularios web, múltiples archivos, metadatos | APIs RESTful, actualizaciones de un solo archivo |
| **Complejidad**          | Mayor (manejo de límites, múltiples partes) | Menor (contenido directo)               |
| **Eficiencia**           | Moderada (sobrecarga de codificación) | Mayor (sin codificación)                 |
| **Soporte del Servidor** | Ampliamente admitido                   | Puede requerir configuración            |
| **Ejemplo de Cabeceras** | `Content-Type: multipart/form-data; boundary=abc123` | `Content-Type: text/plain`           |
| **Cuerpo de la Solicitud** | Partes separadas por límites          | Contenido en bruto del archivo                     |

Esta tabla destaca que, mientras multipart/form-data es más versátil para interacciones web, PUT es más eficiente para subidas impulsadas por API, dependiendo de las capacidades del servidor.

#### Detalles de Implementación y Problemas Potenciales

##### Selección del Límite y Contenido del Archivo
En multipart/form-data, elegir una cadena límite es crucial para evitar conflictos con el contenido del archivo. Si el límite aparece dentro del archivo, puede causar errores de análisis. Las bibliotecas modernas manejan esto generando límites aleatorios, pero la implementación manual requiere cuidado. Para archivos binarios, el contenido se transmite tal cual, preservando todos los bytes, lo que es esencial para mantener la integridad del archivo.

##### Tamaño del Archivo y Rendimiento
Ambos métodos deben considerar los límites de tamaño de archivo impuestos por los servidores. Las solicitudes multipart/form-data pueden volverse grandes con múltiples archivos, potencialmente excediendo los límites del servidor o causando problemas de memoria. PUT, aunque más simple, también requiere streaming para archivos grandes para evitar cargar todo el contenido en la memoria, como se discute en la [documentación de HTTPie sobre subidas de archivos](https://httpie.io/docs/cli/file-upload-forms).

##### Manejo de Errores y Seguridad
Después de enviar la solicitud, los clientes deben verificar el código de estado HTTP. El éxito se indica típicamente con 200 (OK) o 201 (Creado), mientras que errores como 400 (Solicitud Incorrecta) o 403 (Prohibido) señalan problemas. La seguridad es primordial, ya que las subidas de archivos pueden ser explotadas para ataques como subir ejecutables maliciosos. Los servidores deben validar los tipos de archivo, escanear en busca de malware y restringir los directorios de subida, como se describe en los [debates de Stack Overflow sobre seguridad en subidas de archivos HTTP](https://stackoverflow.com/questions/8659808/how-does-http-file-upload-work).

#### Ejemplos Prácticos en Diferentes Lenguajes

Varios lenguajes de programación proporcionan bibliotecas para simplificar las subidas de archivos HTTP. Por ejemplo, la biblioteca `requests` de Python maneja multipart/form-data con:

```python
import requests
files = {'file': open('example.txt', 'rb')}
response = requests.post('https://example.com/upload', files=files)
```

Para PUT, se puede usar curl como se muestra en [Stack Overflow sobre probar subidas PUT](https://stackoverflow.com/questions/5143915/test-file-upload-using-http-put-method):

```bash
curl -X PUT "https://example.com/files/123" --upload-file example.txt
```

Estos ejemplos demuestran abstracción, pero entender la estructura HTTP subyacente es crucial para la resolución de problemas y las implementaciones personalizadas.

#### Conclusión

En resumen, las subidas de archivos HTTP se pueden lograr mediante POST con multipart/form-data para interacciones versátiles en formularios web o PUT para actualizaciones eficientes en API, cada uno con ventajas y requisitos distintos. La configuración del servidor, el tamaño del archivo y las consideraciones de seguridad son críticas para garantizar una implementación robusta. Para más lectura, explora la [guía de Medium sobre subidas de archivos POST](https://medium.com/@API4AI/post-a-file-via-http-request-the-ultimate-guide-b23fb70a3f73) para ver ejemplos prácticos en diferentes lenguajes.

### Citas Clave
- [How do you upload your files to a web server Learn web development MDN](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Tools_and_setup/Upload_files_to_a_web_server)
- [How does HTTP file upload work Stack Overflow](https://stackoverflow.com/questions/8659808/how-does-http-file-upload-work)
- [POST a File via HTTP Request The Ultimate Guide by API4AI Medium](https://medium.com/@API4AI/post-a-file-via-http-request-the-ultimate-guide-b23fb70a3f73)
- [HTTP REST API File Uploads Phil Sturgeon](https://philsturgeon.com/http-rest-api-file-uploads/)
- [PHP PUT method support Manual](https://www.php.net/manual/en/features.file-upload.put-method.php)
- [curl Test file upload using HTTP PUT method Stack Overflow](https://stackoverflow.com/questions/5143915/test-file-upload-using-http-put-method)
- [File upload forms HTTPie 3.2.4 latest docs](https://httpie.io/docs/cli/file-upload-forms)