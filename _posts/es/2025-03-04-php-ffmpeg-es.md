---
audio: false
generated: true
lang: es
layout: post
title: Usar ffmpeg en PHP
translated: true
type: note
---

### Puntos Clave
- Parece probable que para usar "php-ffmpeg/php-ffmpeg" versión ~0.5, primero necesitas instalar FFMpeg en tu sistema y luego usar Composer para instalar la librería PHP.
- La investigación sugiere incluir el archivo de autoload y crear una instancia de `FFMpeg\FFMpeg` para la manipulación de medios, con opciones para especificar rutas de binarios si es necesario.
- La evidencia apunta a usar métodos como `open()`, `save()`, y `frame()` para operaciones básicas, pero verifica la documentación en GitHub para obtener detalles completos debido a posibles diferencias específicas de la versión.

---

### Instalación
Primero, asegúrate de que FFMpeg esté instalado en tu sistema:
- En Ubuntu, usa `sudo apt-get install ffmpeg`.
- En macOS, usa `brew install ffmpeg`.
- En Windows, descarga desde [este sitio web](https://www.gyan.dev/ffmpeg/builds/) y sigue las instrucciones.

Luego, instala la librería php-FFMpeg via Composer con:
```
composer require php-FFMpeg/php-FFMpeg:~0.5
```

### Configuración y Uso
Incluye el archivo de autoload en tu script PHP:
```php
require_once 'vendor/autoload.php';
```

Crea una instancia de `FFMpeg\FFMpeg`, opcionalmente especificando rutas si los binarios de FFMpeg no están en el PATH del sistema:
```php
use FFMpeg\FFMpeg;
$ff = FFMpeg::create(array(
    'binary' => '/ruta/hacia/FFMpeg',
    'ffprobe' => '/ruta/hacia/FFprobe'
));
```

Abre un archivo multimedia y realiza operaciones, tales como:
- Transcodificación: `$video->save('output.mp4', new FFMpeg\Format\Video\X264());`
- Extraer un fotograma: `$frame = $video->frame(FFMpeg\Coordinate\TimeCode::fromSeconds(5)); $frame->save('frame.jpg');`
- Recortar: `$clip = $video->clip(FFMpeg\Coordinate\TimeCode::fromSeconds(10), FFMpeg\Coordinate\TimeCode::fromSeconds(20)); $clip->save('clip.mp4');`

Para más detalles, consulta la documentación de la librería en [GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg).

---

### Nota de Estudio: Guía Completa para Usar php-FFMpeg/php-FFMpeg Versión ~0.5

Esta nota proporciona una exploración en profundidad del uso de la librería "php-FFMpeg/php-FFMpeg", específicamente la versión aproximadamente 0.5, basada en la información disponible. Amplía la respuesta directa incluyendo todos los detalles relevantes de la investigación, asegurando una comprensión exhaustiva para los usuarios que buscan implementar esta librería PHP para la manipulación de medios.

#### Antecedentes y Contexto
La librería "php-FFMpeg/php-FFMpeg" es un wrapper de PHP para el binario FFMpeg, que permite la manipulación orientada a objetos de archivos de video y audio. Soporta tareas como transcodificación, extracción de fotogramas, recorte y más, lo que la hace valiosa para desarrolladores que trabajan en aplicaciones relacionadas con medios. La especificación de versión "~0.5" indica cualquier versión mayor o igual a 0.5 y menor a 1.0, lo que sugiere compatibilidad con versiones antiguas de PHP, probablemente encontrada en la rama 0.x del repositorio.

Dada la fecha actual, 3 de marzo de 2025, y la evolución de la librería, la versión 0.5 puede ser parte del soporte legacy, requiriendo la rama principal ahora PHP 8.0 o superior. Esta nota asume que el usuario está trabajando dentro de las limitaciones de esta versión, reconociendo posibles diferencias en la funcionalidad en comparación con lanzamientos más nuevos.

#### Proceso de Instalación
Para comenzar, FFMpeg debe estar instalado en el sistema, ya que la librería depende de sus binarios para las operaciones. Los métodos de instalación varían según el sistema operativo:
- **Ubuntu**: Usa el comando `sudo apt-get install ffmpeg` para instalar a través del gestor de paquetes.
- **macOS**: Utiliza Homebrew con `brew install ffmpeg` para una instalación sencilla.
- **Windows**: Descarga los binarios de FFMpeg desde [este sitio web](https://www.gyan.dev/ffmpeg/builds/) y sigue las instrucciones proporcionadas, asegurándote de que los ejecutables sean accesibles en el PATH del sistema o se especifiquen manualmente.

Tras la instalación de FFMpeg, la librería php-FFMpeg se instala a través de Composer, el gestor de paquetes de PHP. El comando `composer require php-FFMpeg/php-FFMpeg:~0.5` asegura que se obtenga la versión correcta. Este proceso crea un directorio `vendor` en el proyecto, que aloja la librería y sus dependencias, con Composer gestionando el autoloading para una integración perfecta.

#### Configuración e Inicialización
Después de la instalación, incluye el archivo de autoload en tu script PHP para permitir el acceso a las clases de la librería:
```php
require_once 'vendor/autoload.php';
```

Crea una instancia de `FFMpeg\FFMpeg` para comenzar a usar la librería. El método de creación permite la configuración, particularmente importante si los binarios de FFMpeg no están en el PATH del sistema:
```php
use FFMpeg\FFMpeg;
$ff = FFMpeg::create(array(
    'timeout' => 0,
    'thread_count' => 12,
    'binary' => '/ruta/hacia/tu/propio/FFMpeg',
    'ffprobe' => '/ruta/hacia/tu/propio/FFprobe'
));
```
Esta configuración permite establecer tiempos de espera, recuentos de hilos y rutas de binarios explícitas, mejorando la flexibilidad para diferentes configuraciones del sistema. La configuración predeterminada busca los binarios en el PATH, pero la especificación manual garantiza la compatibilidad, especialmente en entornos personalizados.

#### Uso Principal y Operaciones
La librería proporciona una interfaz fluida y orientada a objetos para la manipulación de medios. Comienza abriendo un archivo multimedia:
```php
$video = $ff->open('input.mp4');
```
Esto soporta rutas del sistema de archivos local, recursos HTTP y otros protocolos soportados por FFMpeg, con una lista de tipos soportados disponible a través del comando `ffmpeg -protocols`.

##### Transcodificación
La transcodificación implica convertir medios a diferentes formatos. Usa el método `save` con una instancia de formato:
```php
$format = new FFMpeg\Format\Video\X264();
$video->save('output.mp4', $format);
```
El formato `X264` es un ejemplo; la librería soporta varios formatos de video y audio, implementables a través de `FFMpeg\Format\FormatInterface`, con interfaces específicas como `VideoInterface` y `AudioInterface` para los respectivos tipos de medios.

##### Extracción de Fotogramas
Extraer fotogramas es útil para miniaturas o análisis. El siguiente código extrae un fotograma a los 5 segundos:
```php
$frame = $video->frame(FFMpeg\Coordinate\TimeCode::fromSeconds(5));
$frame->save('frame.jpg');
```
La clase `TimeCode`, parte de `FFMpeg\Coordinate`, asegura una sincronización precisa, con opciones para la precisión en la extracción de imágenes.

##### Recorte
Para recortar una porción del video, especifica los tiempos de inicio y fin:
```php
$clip = $video->clip(FFMpeg\Coordinate\TimeCode::fromSeconds(10), FFMpeg\Coordinate\TimeCode::fromSeconds(20));
$clip->save('clip.mp4');
```
Esto crea un nuevo segmento de video, manteniendo la calidad y el formato original, con la capacidad de aplicar filtros adicionales si es necesario.

#### Características Avanzadas y Consideraciones
La librería soporta características adicionales, como se describe en la documentación:
- **Manipulación de Audio**: Similar al video, el audio puede ser transcodificado con `FFMpeg\Media\Audio::save`, aplicando filtros, añadiendo metadatos y remuestreando.
- **Creación de GIF**: Los GIFs animados se pueden guardar usando `FFMpeg\Media\Gif::save`, con parámetros de duración opcionales.
- **Concatenación**: Combina múltiples archivos multimedia usando `FFMpeg\Media\Concatenate::saveFromSameCodecs` para los mismos códecs o `saveFromDifferentCodecs` para códecs variados, con recursos para más lectura en [este enlace](https://trac.ffmpeg.org/wiki/Concatenate), [este enlace](https://ffmpeg.org/ffmpeg-formats.html#concat-1), y [este enlace](https://ffmpeg.org/ffmpeg.html#Stream-copy).
- **Manejo Avanzado de Medios**: Soporta múltiples entradas/salidas con `-filter_complex`, útil para filtrado y mapeo complejos, con soporte de filtros incorporados.
- **Extracción de Metadatos**: Usa `FFMpeg\FFProbe::create` para metadatos, validando archivos con `FFMpeg\FFProbe::isValid` (disponible desde v0.10.0, notando que la versión 0.5 puede carecer de esto).

Las coordenadas, como `FFMpeg\Coordinate\AspectRatio`, `Dimension`, `FrameRate`, `Point` (dinámico desde v0.10.0), y `TimeCode`, proporcionan un control preciso sobre las propiedades de los medios, aunque algunas características como los puntos dinámicos pueden no estar disponibles en la versión 0.5.

#### Notas Específicas de la Versión
Dada la especificación "~0.5", es probable que la librería se alinee con la rama 0.x, soportando versiones antiguas de PHP. El repositorio de GitHub indica PHP 8.0 o superior para la rama principal, con 0.x para soporte legacy. Sin embargo, los detalles exactos de la versión 0.5 no se encontraron explícitamente en los lanzamientos, lo que sugiere que puede ser parte del historial de commits o de los commits de la rama. Los usuarios deben verificar la compatibilidad, ya que características más nuevas como ciertos tipos de coordenadas (por ejemplo, puntos dinámicos) pueden requerir versiones posteriores a la 0.5.

#### Documentación y Lectura Adicional
Mientras que la página de Read the Docs ([Read the Docs](https://FFMpeg-PHP.readthedocs.io/en/latest/)) apareció vacía, el repositorio de GitHub ([GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg)) contiene documentación exhaustiva dentro del README, cubriendo el uso de la API, formatos y ejemplos. Este es el recurso principal para la versión 0.5, dada la falta de documentación en línea específica para esta versión legacy.

#### Tabla: Resumen de Operaciones y Métodos Clave

| Operación               | Ejemplo de Método                                      | Descripción                                      |
|-------------------------|----------------------------------------------------|-------------------------------------------------|
| Abrir Archivo Multimedia| `$ff->open('input.mp4')`                           | Carga un archivo multimedia para manipulación   |
| Transcodificar Video    | `$video->save('output.mp4', new X264())`           | Convierte al formato especificado               |
| Extraer Fotograma       | `$video->frame(TimeCode::fromSeconds(5))->save('frame.jpg')` | Extrae fotograma en el tiempo especificado, guarda como imagen |
| Recortar Video          | `$video->clip(TimeCode::fromSeconds(10), TimeCode::fromSeconds(20))->save('clip.mp4')` | Crea un recorte entre tiempos, guarda como nuevo archivo |
| Configurar Instancia    | `FFMpeg::create(array('binary' => '/ruta/hacia/FFMpeg'))` | Establece rutas de binarios personalizadas y opciones |

Esta tabla encapsula la funcionalidad principal, ayudando a los usuarios en una referencia rápida mientras implementan la librería.

#### Detalle Inesperado: Implicaciones de la Versión Legacy
Un aspecto inesperado es la posible limitación de la versión 0.5, dada su ubicación en la rama 0.x para soporte de PHP antiguo. Esto puede restringir el acceso a características modernas, como los puntos de coordenadas dinámicas introducidos en v0.10.0, requiriendo que los usuarios verifiquen los commits de la rama para conocer las capacidades exactas, añadiendo una capa de complejidad no inmediatamente aparente en versiones más nuevas.

#### Conclusión
Usar "php-FFMpeg/php-FFMpeg" versión ~0.5 implica instalar FFMpeg, configurar a través de Composer y aprovechar una API orientada a objetos para tareas multimedia. Si bien operaciones básicas como la transcodificación y la extracción de fotogramas son sencillas, las diferencias específicas de la versión pueden requerir consultar la documentación de la rama 0.x en [GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg). Este enfoque integral asegura que los usuarios puedan utilizar la librería de manera efectiva, reconociendo tanto su potencia como sus posibles limitaciones legacy.

---

### Citas Clave
- [FFMpeg PHP Object Oriented Library Packagist](https://packagist.org/products/php-FFMpeg/php-FFMpeg)
- [PHP-FFMpeg GitHub Repository Documentation](https://github.com/PHP-FFMpeg/PHP-FFMpeg)
- [FFMpeg PHP Read the Docs Documentation](https://FFMpeg-PHP.readthedocs.io/en/latest/)
- [FFMpeg Download and Builds Website](https://www.gyan.dev/ffmpeg/builds/)
- [FFMpeg Concatenation Wiki Page](https://trac.ffmpeg.org/wiki/Concatenate)
- [FFMpeg Formats Documentation Page](https://ffmpeg.org/ffmpeg-formats.html#concat-1)
- [FFMpeg Command Line Tool Documentation](https://ffmpeg.org/ffmpeg.html#Stream-copy)