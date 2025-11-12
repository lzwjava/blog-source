---
audio: false
generated: true
lang: es
layout: post
title: Biblioteca de Nube de Transmisión Pili para PHP
translated: true
type: note
---

### Puntos Clave
- Parece probable que para usar "pili-engineering/pili-sdk-php": "dev-master", necesites instalarlo vía Composer y configurar las credenciales de Qiniu.
- La investigación sugiere que el paquete requiere PHP 5.3.0 o superior y es para Pili Streaming Cloud, relacionado con Qiniu.
- La evidencia apunta a crear un objeto Hub y usar operaciones de stream como generar URLs RTMP, pero los métodos exactos pueden variar.

### Instalación
Primero, asegúrate de tener Composer instalado. Añade el paquete a tu archivo `composer.json` con:
```json
"require": {
    "pili-engineering/pili-sdk-php": "dev-master"
}
```
Luego, ejecuta `composer install` o `composer update`. En tu script PHP, incluye:
```php
require 'vendor/autoload.php';
```

### Configuración y Uso
Necesitarás una cuenta de Qiniu y un Pili Hub. Establece tu access key, secret key y hub name, luego crea un objeto Hub:
```php
use Qiniu\Credentials;
use Pili\Hub;

$credentials = new Credentials('your_access_key', 'your_secret_key');
$hub = new Hub($credentials, 'your_hub_name');
```
Crea u obtén un stream, por ejemplo, `$stream = $hub->createStream('your_stream_key');`, y usa métodos como `$stream->rtmpPublishUrl(60)` para operaciones.

### Detalle Inesperado
Ten en cuenta que "dev-master" es una versión de desarrollo, potencialmente inestable, con versiones etiquetadas como 1.5.5 disponibles para producción.

---

### Guía Completa sobre el Uso de "pili-engineering/pili-sdk-php": "dev-master"

Esta guía proporciona una exploración detallada de cómo usar el paquete "pili-engineering/pili-sdk-php" con la versión "dev-master", basada en la documentación y ejemplos disponibles. Cubre la instalación, configuración, uso y consideraciones adicionales, asegurando una comprensión exhaustiva para los desarrolladores que trabajan con los servicios de Pili Streaming Cloud.

#### Antecedentes y Contexto
El paquete "pili-engineering/pili-sdk-php" es una librería del lado del servidor para PHP, diseñada para interactuar con Pili Streaming Cloud, un servicio asociado con Qiniu, un proveedor de almacenamiento en la nube y CDN. La versión "dev-master" se refiere a la rama de desarrollo más reciente, que puede incluir características nuevas pero podría ser menos estable que las versiones etiquetadas. El paquete requiere PHP 5.3.0 o superior, haciéndolo accesible para muchos entornos PHP a partir del 3 de marzo de 2025.

#### Proceso de Instalación
Para comenzar, debes tener Composer instalado, un gestor de dependencias para PHP. La instalación implica añadir el paquete al archivo `composer.json` de tu proyecto y ejecutar un comando de Composer para descargarlo. Específicamente:

- Añade lo siguiente a tu `composer.json` en la sección "require":
  ```json
  "require": {
      "pili-engineering/pili-sdk-php": "dev-master"
  }
  ```
- Ejecuta `composer install` o `composer update` en tu terminal para obtener el paquete y sus dependencias. Esto creará un directorio `vendor` con los archivos necesarios.
- En tu script PHP, incluye el autoloader para acceder a las clases del paquete:
  ```php
  require 'vendor/autoload.php';
  ```

Este proceso asegura que el paquete esté integrado en tu proyecto, aprovechando el autoloading de Composer para un acceso fácil a las clases.

#### Prerrequisitos y Configuración
Antes de usar el SDK, necesitas una cuenta de Qiniu y debes configurar un Pili Hub, ya que el SDK interactúa con los servicios de Pili Streaming Cloud. Esto implica obtener una Access Key y una Secret Key de Qiniu y crear un hub dentro de su plataforma. La documentación sugiere que estas credenciales son esenciales para la autenticación.

Para configurar, define tus credenciales en tu script PHP:
- Access Key: Tu Access Key de Qiniu.
- Secret Key: Tu Secret Key de Qiniu.
- Hub Name: El nombre de tu Pili Hub, que debe existir previamente.

Una configuración de ejemplo se ve así:
```php
$accessKey = 'your_access_key';
$secretKey = 'your_secret_key';
$hubName = 'your_hub_name';
```

#### Creación y Uso del Objeto Hub
El núcleo del SDK es el objeto Hub, que facilita la gestión de streams. Primero, crea un objeto Credentials usando tus keys de Qiniu:
```php
use Qiniu\Credentials;

$credentials = new Credentials($accessKey, $secretKey);
```
Luego, instancia un objeto Hub con estas credenciales y el nombre de tu hub:
```php
use Pili\Hub;

$hub = new Hub($credentials, $hubName);
```
Este objeto Hub te permite realizar varias operaciones relacionadas con streams, como crear, recuperar o listar streams.

#### Trabajando con Streams
Los streams son centrales en Pili Streaming Cloud, y el SDK proporciona métodos para gestionarlos a través del objeto Hub. Para crear un nuevo stream:
```php
$streamKey = 'your_stream_key'; // Debe ser único dentro del hub
$stream = $hub->createStream($streamKey);
```
Para recuperar un stream existente:
```php
$stream = $hub->getStream($streamKey);
```
El objeto stream luego ofrece varios métodos para operaciones, detallados en la siguiente tabla basada en la documentación disponible:

| **Operación**          | **Método**                     | **Descripción**                                      |
|-------------------------|--------------------------------|------------------------------------------------------|
| Crear Stream           | `$hub->createStream($key)`     | Crea un nuevo stream con la key dada.               |
| Obtener Stream         | `$hub->getStream($key)`        | Recupera un stream existente por su key.            |
| Listar Streams         | `$hub->listStreams($marker, $limit, $prefix)` | Lista streams con opciones de paginación.           |
| URL RTMP de Publicación| `$stream->rtmpPublishUrl($expire)` | Genera una URL RTMP de publicación con tiempo de expiración. |
| URL RTMP de Reproducción| `$stream->rtmpPlayUrl()`       | Genera una URL RTMP de reproducción para el stream. |
| URL HLS de Reproducción| `$stream->hlsPlayUrl()`        | Genera una URL HLS de reproducción para streaming.  |
| Deshabilitar Stream    | `$stream->disable()`           | Deshabilita el stream.                              |
| Habilitar Stream       | `$stream->enable()`            | Habilita el stream.                                 |
| Obtener Estado del Stream| `$stream->status()`           | Recupera el estado actual del stream.               |

Por ejemplo, para generar una URL RTMP de publicación con una expiración de 60 segundos:
```php
$expire = 60;
$url = $stream->rtmpPublishUrl($expire);
echo $url;
```
Esta URL puede usarse para publicar streams en Pili Streaming Cloud, con la expiración asegurando acceso temporal.

#### Consideraciones Adicionales
- **Estabilidad de la Versión**: La versión "dev-master" es la rama de desarrollo, potencialmente inestable. Para producción, considera usar una versión etiquetada, como la 1.5.5, disponible en Packagist [versiones de pili-engineering/pili-sdk-php](https://packagist.org/p/pili-engineering/pili-sdk-php). El historial muestra actualizaciones como adiciones de API y refinamientos de métodos, con versiones que se remontan a 2016.
- **Manejo de Errores**: La documentación sugiere usar bloques try-catch para las operaciones, como se ve en ejemplos para la creación y recuperación de streams, para manejar posibles excepciones.
- **Documentación y Ejemplos**: Aunque los ejemplos específicos no fueron extensamente detallados, el repositorio de GitHub [Librería del lado del servidor de Pili Streaming Cloud para PHP](https://github.com/pili-engineering/pili-sdk-php) proporciona instrucciones de instalación y listas de características, y las comparaciones con otros SDKs de lenguaje (por ejemplo, Python) indican una funcionalidad similar, como la generación de URLs.

#### Perspectivas Comparativas
La comparación con otros SDKs de Pili, como la versión Python, revela patrones similares: ambos requieren credenciales, configuración del hub y operaciones de stream. Sin embargo, la versión PHP usa un enfoque orientado a objetos con clases Hub y Stream, contrastando con el estilo más funcional de Python. Esto se alinea con las prácticas típicas de desarrollo en PHP, ofreciendo seguridad de tipos y soporte para IDE.

#### Conclusión
Usar "pili-engineering/pili-sdk-php": "dev-master" implica instalar vía Composer, configurar las credenciales de Qiniu, crear un objeto Hub y gestionar streams con métodos como `rtmpPublishUrl`. Asegúrate de que tu entorno cumpla con los requisitos de PHP 5.3.0+ y considera la estabilidad para uso en producción. Esta guía proporciona un punto de partida exhaustivo, con más detalles disponibles en la documentación oficial y el repositorio.

### Citas Clave
- [Librería del lado del servidor de Pili Streaming Cloud para PHP GitHub](https://github.com/pili-engineering/pili-sdk-php)
- [versiones de pili-engineering/pili-sdk-php Packagist](https://packagist.org/p/pili-engineering/pili-sdk-php)