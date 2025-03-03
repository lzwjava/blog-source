---
audio: false
generated: true
lang: es
layout: post
title: Usando ffmpeg en PHP
translated: true
---

### Puntos Clave
- Parece probable que para usar la versión "php-ffmpeg/php-ffmpeg" ~0.5, primero necesite instalar FFMpeg en su sistema y luego usar Composer para instalar la biblioteca PHP.
- La investigación sugiere incluir el archivo de autocarga y crear una instancia de `FFMpeg\FFMpeg` para la manipulación de medios, con opciones para especificar rutas binarias si es necesario.
- La evidencia apunta a usar métodos como `open()`, `save()` y `frame()` para operaciones básicas, pero consulte la documentación de GitHub para obtener todos los detalles debido a posibles diferencias específicas de la versión.

---

### Instalación
Primero, asegúrese de que FFMpeg esté instalado en su sistema:
- En Ubuntu, use `sudo apt-get install ffmpeg`.
- En macOS, use `brew install ffmpeg`.
- En Windows, descargue desde [este sitio web](https://www.gyan.dev/ffmpeg/builds/) y siga las instrucciones.

A continuación, instale la biblioteca php-FFMpeg a través de Composer con:
```
composer require php-FFMpeg/php-FFMpeg:~0.5
```

### Configuración y Uso
Incluya el archivo de autocarga en su script PHP:
```php
require_once 'vendor/autoload.php';
```

Cree una instancia de `FFMpeg\FFMpeg`, opcionalmente especificando rutas si los binarios de FFMpeg no están en el PATH del sistema:
```php
use FFMpeg\FFMpeg;
$ff = FFMpeg::create(array(
    'binary' => '/ruta/a/FFMpeg',
    'ffprobe' => '/ruta/a/FFprobe'
));
```

Abra un archivo de medios y realice operaciones, como:
- Transcodificación: `$video->save('output.mp4', new FFMpeg\Format\Video\X264());`
- Extracción de un fotograma: `$frame = $video->frame(FFMpeg\Coordinate\TimeCode::fromSeconds(5)); $frame->save('frame.jpg');`
- Recorte: `$clip = $video->clip(FFMpeg\Coordinate\TimeCode::fromSeconds(10), FFMpeg\Coordinate\TimeCode::fromSeconds(20)); $clip->save('clip.mp4');`

Para más detalles, consulte la documentación de la biblioteca en [GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg).

---

### Nota de Encuesta: Guía Completa para Usar php-FFMpeg/php-FFMpeg Versión ~0.5

Esta nota proporciona una exploración exhaustiva del uso de la biblioteca "php-FFMpeg/php-FFMpeg", específicamente la versión aproximadamente 0.5, basada en la información disponible. Amplía la respuesta directa incluyendo todos los detalles relevantes de la investigación, asegurando una comprensión exhaustiva para los usuarios que buscan implementar esta biblioteca PHP para la manipulación de medios.

#### Antecedentes y Contexto
La biblioteca "php-FFMpeg/php-FFMpeg" es un wrapper PHP para el binario FFMpeg, habilitando la manipulación orientada a objetos de archivos de video y audio. Soporta tareas como transcodificación, extracción de fotogramas, recorte y más, lo que la hace valiosa para los desarrolladores que trabajan en aplicaciones relacionadas con medios. La especificación de versión "~0.5" indica cualquier versión mayor o igual a 0.5 y menor que 1.0, sugiriendo compatibilidad con versiones más antiguas de PHP, probablemente encontradas en la rama 0.x del repositorio.

Dada la fecha actual, 3 de marzo de 2025, y la evolución de la biblioteca, la versión 0.5 puede ser parte del soporte legado, con la rama principal ahora requiriendo PHP 8.0 o superior. Esta nota asume que el usuario está trabajando dentro de las limitaciones de esta versión, reconociendo posibles diferencias en la funcionalidad en comparación con los lanzamientos más recientes.

#### Proceso de Instalación
Para comenzar, FFMpeg debe estar instalado en el sistema, ya que la biblioteca depende de sus binarios para las operaciones. Los métodos de instalación varían según el sistema operativo:
- **Ubuntu**: Use el comando `sudo apt-get install ffmpeg` para instalar a través del administrador de paquetes.
- **macOS**: Utilice Homebrew con `brew install ffmpeg` para una instalación sencilla.
- **Windows**: Descargue los binarios de FFMpeg desde [este sitio web](https://www.gyan.dev/ffmpeg/builds/) y siga las instrucciones proporcionadas, asegurándose de que los ejecutables sean accesibles en el PATH del sistema o especifíquelos manualmente.

Después de la instalación de FFMpeg, la biblioteca php-FFMpeg se instala a través de Composer, el administrador de paquetes PHP. El comando `composer require php-FFMpeg/php-FFMpeg:~0.5` asegura que se obtenga la versión correcta. Este proceso crea un directorio `vendor` en el proyecto, alojando la biblioteca y sus dependencias, con Composer gestionando la autocarga para una integración sin problemas.

#### Configuración e Inicialización
Después de la instalación, incluya el archivo de autocarga en su script PHP para habilitar el acceso a las clases de la biblioteca:
```php
require_once 'vendor/autoload.php';
```

Cree una instancia de `FFMpeg\FFMpeg` para comenzar a usar la biblioteca. El método de creación permite la configuración, especialmente importante si los binarios de FFMpeg no están en el PATH del sistema:
```php
use FFMpeg\FFMpeg;
$ff = FFMpeg::create(array(
    'timeout' => 0,
    'thread_count' => 12,
    'binary' => '/ruta/a/FFMpeg',
    'ffprobe' => '/ruta/a/FFprobe'
));
```
Esta configuración soporta la configuración de temporizadores, recuentos de hilos y rutas binarias explícitas, mejorando la flexibilidad para diferentes configuraciones del sistema. La configuración predeterminada busca binarios en el PATH, pero la especificación manual asegura la compatibilidad, especialmente en entornos personalizados.

#### Uso Principal y Operaciones
La biblioteca proporciona una interfaz fluida y orientada a objetos para la manipulación de medios. Comience abriendo un archivo de medios:
```php
$video = $ff->open('input.mp4');
```
Esto soporta rutas del sistema de archivos locales, recursos HTTP y otros protocolos soportados por FFMpeg, con una lista de tipos soportados disponible a través del comando `ffmpeg -protocols`.

##### Transcodificación
La transcodificación implica convertir medios a diferentes formatos. Use el método `save` con una instancia de formato:
```php
$format = new FFMpeg\Format\Video\X264();
$video->save('output.mp4', $format);
```
El formato `X264` es solo un ejemplo; la biblioteca soporta varios formatos de video y audio, implementables a través de `FFMpeg\Format\FormatInterface`, con interfaces específicas como `VideoInterface` y `AudioInterface` para los tipos de medios respectivos.

##### Extracción de Fotogramas
La extracción de fotogramas es útil para miniaturas o análisis. El siguiente código extrae un fotograma a los 5 segundos:
```php
$frame = $video->frame(FFMpeg\Coordinate\TimeCode::fromSeconds(5));
$frame->save('frame.jpg');
```
La clase `TimeCode`, parte de `FFMpeg\Coordinate`, asegura un tiempo preciso, con opciones para la precisión en la extracción de imágenes.

##### Recorte
Para recortar una parte del video, especifique los tiempos de inicio y fin:
```php
$clip = $video->clip(FFMpeg\Coordinate\TimeCode::fromSeconds(10), FFMpeg\Coordinate\TimeCode::fromSeconds(20));
$clip->save('clip.mp4');
```
Esto crea un nuevo segmento de video, manteniendo la calidad y el formato originales, con la capacidad de aplicar filtros adicionales si es necesario.

#### Características Avanzadas y Consideraciones
La biblioteca soporta características adicionales, como se describe en la documentación:
- **Manipulación de Audio**: Similar al video, el audio puede transcodificarse con `FFMpeg\Media\Audio::save`, aplicando filtros, agregando metadatos y remuestreando.
- **Creación de GIF**: Los GIF animados pueden guardarse usando `FFMpeg\Media\Gif::save`, con parámetros opcionales de duración.
- **Concatenación**: Combine múltiples archivos de medios usando `FFMpeg\Media\Concatenate::saveFromSameCodecs` para los mismos codecs o `saveFromDifferentCodecs` para codecs variados, con recursos para lectura adicional en [este enlace](https://trac.ffmpeg.org/wiki/Concatenate), [este enlace](https://ffmpeg.org/ffmpeg-formats.html#concat-1) y [este enlace](https://ffmpeg.org/ffmpeg.html#Stream-copy).
- **Manejo Avanzado de Medios**: Soporta múltiples entradas/salidas con `-filter_complex`, útil para filtros y mapeos complejos, con soporte de filtros integrados.
- **Extracción de Metadatos**: Use `FFMpeg\FFProbe::create` para metadatos, validando archivos con `FFMpeg\FFProbe::isValid` (disponible desde v0.10.0, notando que la versión 0.5 puede carecer de esto).

Las coordenadas, como `FFMpeg\Coordinate\AspectRatio`, `Dimension`, `FrameRate`, `Point` (dinámico desde v0.10.0) y `TimeCode`, proporcionan un control preciso sobre las propiedades de los medios, aunque algunas características como puntos dinámicos pueden no estar disponibles en la versión 0.5.

#### Notas Específicas de la Versión
Dada la especificación "~0.5", la biblioteca probablemente se alinea con la rama 0.x, soportando versiones más antiguas de PHP. El repositorio de GitHub indica PHP 8.0 o superior para la rama principal, con 0.x para soporte legado. Sin embargo, los detalles exactos de la versión 0.5 no se encontraron explícitamente en los lanzamientos, sugiriendo que puede ser parte del historial de commits o commits de ramas. Los usuarios deben verificar la compatibilidad, ya que características más nuevas como ciertos tipos de coordenadas (por ejemplo, puntos dinámicos) pueden requerir versiones más allá de 0.5.

#### Documentación y Lectura Adicional
Aunque la página de Read the Docs ([Read the Docs](https://FFMpeg-PHP.readthedocs.io/en/latest/)) apareció vacía, el repositorio de GitHub ([GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg)) contiene documentación exhaustiva dentro del README, cubriendo el uso de la API, formatos y ejemplos. Este es el recurso principal para la versión 0.5, dado la falta de documentación en línea específica para esta versión de legado.

#### Tabla: Resumen de Operaciones y Métodos Clave

| Operación               | Ejemplo de Método                                      | Descripción                                      |
|-------------------------|----------------------------------------------------|-------------------------------------------------|
| Abrir Archivo de Medios  | `$ff->open('input.mp4')`                           | Carga un archivo de medios para manipulación             |
| Transcodificar Video     | `$video->save('output.mp4', new X264())`           | Convierte al formato especificado                    |
| Extraer Fotograma        | `$video->frame(TimeCode::fromSeconds(5))->save('frame.jpg')` | Extrae fotograma en el tiempo especificado, guarda como imagen |
| Recortar Video           | `$video->clip(TimeCode::fromSeconds(10), TimeCode::fromSeconds(20))->save('clip.mp4')` | Crea recorte entre tiempos, guarda como nuevo archivo   |
| Configurar Instancia     | `FFMpeg::create(array('binary' => '/ruta/a/FFMpeg'))` | Establece rutas binarias y opciones personalizadas            |

Esta tabla encapsula la funcionalidad principal, ayudando a los usuarios en la referencia rápida mientras implementan la biblioteca.

#### Detalle Inesperado: Implicaciones de la Versión de Legado
Un aspecto inesperado es la posible limitación de la versión 0.5, dada su colocación en la rama 0.x para el soporte de versiones más antiguas de PHP. Esto puede restringir el acceso a características modernas, como puntos de coordenadas dinámicos introducidos en v0.10.0, requiriendo que los usuarios verifiquen los commits de la rama para las capacidades exactas, añadiendo una capa de complejidad no inmediatamente aparente en las versiones más recientes.

#### Conclusión
Usar "php-FFMpeg/php-FFMpeg" versión ~0.5 implica instalar FFMpeg, configurar a través de Composer y aprovechar una API orientada a objetos para tareas de medios. Aunque las operaciones básicas como la transcodificación y la extracción de fotogramas son sencillas, las diferencias específicas de la versión pueden requerir consultar la documentación de la rama 0.x en [GitHub](https://github.com/PHP-FFMpeg/PHP-FFMpeg). Este enfoque exhaustivo asegura que los usuarios puedan utilizar la biblioteca de manera efectiva, reconociendo tanto su poder como las posibles restricciones de legado.

---

### Citaciones Clave
- [FFMpeg PHP Object Oriented Library Packagist](https://packagist.org/products/php-FFMpeg/php-FFMpeg)
- [PHP-FFMpeg GitHub Repository Documentation](https://github.com/PHP-FFMpeg/PHP-FFMpeg)
- [FFMpeg PHP Read the Docs Documentation](https://FFMpeg-PHP.readthedocs.io/en/latest/)
- [FFMpeg Download and Builds Website](https://www.gyan.dev/ffmpeg/builds/)
- [FFMpeg Concatenation Wiki Page](https://trac.ffmpeg.org/wiki/Concatenate)
- [FFMpeg Formats Documentation Page](https://ffmpeg.org/ffmpeg-formats.html#concat-1)
- [FFMpeg Command Line Tool Documentation](https://ffmpeg.org/ffmpeg.html#Stream-copy)