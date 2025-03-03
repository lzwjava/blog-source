---
audio: false
generated: true
lang: es
layout: post
title: Biblioteca en la Nube de Streaming Pili para PHP
translated: true
---

### Puntos Clave
- Parece probable que para usar "pili-engineering/pili-sdk-php": "dev-master", necesites instalarlo a través de Composer y configurar las credenciales de Qiniu.
- La investigación sugiere que el paquete requiere PHP 5.3.0 o superior y es para Pili Streaming Cloud, relacionado con Qiniu.
- La evidencia apunta a la creación de un objeto Hub y el uso de operaciones de transmisión como la generación de URLs RTMP, pero los métodos exactos pueden variar.

### Instalación
Primero, asegúrate de tener Composer instalado. Agrega el paquete a tu archivo `composer.json` con:
```json
"require": {
    "pili-engineering/pili-sdk-php": "dev-master"
}
```
Luego, ejecuta `composer install` o `composer update`. En tu script de PHP, incluye:
```php
require 'vendor/autoload.php';
```

### Configuración y Uso
Necesitarás una cuenta de Qiniu y un Hub de Pili. Configura tu clave de acceso, clave secreta y nombre del hub, luego crea un objeto Hub:
```php
use Qiniu\Credentials;
use Pili\Hub;

$credentials = new Credentials('your_access_key', 'your_secret_key');
$hub = new Hub($credentials, 'your_hub_name');
```
Crea o obtén una transmisión, por ejemplo, `$stream = $hub->createStream('your_stream_key');`, y usa métodos como `$stream->rtmpPublishUrl(60)` para operaciones.

### Detalle Inesperado
Ten en cuenta que "dev-master" es una versión de desarrollo, potencialmente inestable, con versiones etiquetadas como 1.5.5 disponibles para producción.

---

### Guía Completa sobre el Uso de "pili-engineering/pili-sdk-php": "dev-master"

Esta guía proporciona una exploración detallada de cómo usar el paquete "pili-engineering/pili-sdk-php" con la versión "dev-master", basada en la documentación y ejemplos disponibles. Cubre la instalación, configuración, uso y consideraciones adicionales, asegurando una comprensión exhaustiva para los desarrolladores que trabajan con los servicios de Pili Streaming Cloud.

#### Antecedentes y Contexto
El paquete "pili-engineering/pili-sdk-php" es una biblioteca del lado del servidor para PHP, diseñada para interactuar con Pili Streaming Cloud, un servicio asociado con Qiniu, un proveedor de almacenamiento en la nube y CDN. La versión "dev-master" se refiere a la rama de desarrollo más reciente, que puede incluir características recientes pero podría ser menos estable que las versiones etiquetadas. El paquete requiere PHP 5.3.0 o superior, haciéndolo accesible para muchos entornos de PHP hasta marzo 3, 2025.

#### Proceso de Instalación
Para comenzar, debes tener Composer instalado, un gestor de dependencias para PHP. La instalación implica agregar el paquete a tu archivo `composer.json` del proyecto y ejecutar un comando de Composer para descargarlo. Específicamente:

- Agrega lo siguiente a tu `composer.json` bajo la sección "require":
  ```json
  "require": {
      "pili-engineering/pili-sdk-php": "dev-master"
  }
  ```
- Ejecuta `composer install` o `composer update` en tu terminal para obtener el paquete y sus dependencias. Esto creará un directorio `vendor` con los archivos necesarios.
- En tu script de PHP, incluye el autocargador para acceder a las clases del paquete:
  ```php
  require 'vendor/autoload.php';
  ```

Este proceso asegura que el paquete esté integrado en tu proyecto, aprovechando el autocargador de Composer para un acceso fácil a las clases.

#### Prerrequisitos y Configuración
Antes de usar el SDK, necesitas una cuenta de Qiniu y debes configurar un Hub de Pili, ya que el SDK interactúa con los servicios de Pili Streaming Cloud. Esto implica obtener una Clave de Acceso y una Clave Secreta de Qiniu y crear un hub dentro de su plataforma. La documentación sugiere que estas credenciales son esenciales para la autenticación.

Para configurar, define tus credenciales en tu script de PHP:
- Clave de Acceso: Tu Clave de Acceso de Qiniu.
- Clave Secreta: Tu Clave Secreta de Qiniu.
- Nombre del Hub: El nombre de tu Hub de Pili, que debe existir antes de su uso.

Un ejemplo de configuración se ve así:
```php
$accessKey = 'your_access_key';
$secretKey = 'your_secret_key';
$hubName = 'your_hub_name';
```

#### Creación y Uso del Objeto Hub
El núcleo del SDK es el objeto Hub, que facilita la gestión de transmisiones. Primero, crea un objeto Credentials usando tus claves de Qiniu:
```php
use Qiniu\Credentials;

$credentials = new Credentials($accessKey, $secretKey);
```
Luego, instancia un objeto Hub con estas credenciales y tu nombre de hub:
```php
use Pili\Hub;

$hub = new Hub($credentials, $hubName);
```
Este objeto Hub te permite realizar diversas operaciones relacionadas con transmisiones, como crear, recuperar o listar transmisiones.

#### Trabajando con Transmisiones
Las transmisiones son centrales en Pili Streaming Cloud, y el SDK proporciona métodos para gestionarlas a través del objeto Hub. Para crear una nueva transmisión:
```php
$streamKey = 'your_stream_key'; // Debe ser único dentro del hub
$stream = $hub->createStream($streamKey);
```
Para recuperar una transmisión existente:
```php
$stream = $hub->getStream($streamKey);
```
El objeto de transmisión luego ofrece varios métodos para operaciones, detallados en la siguiente tabla basada en la documentación disponible:

| **Operación**          | **Método**                     | **Descripción**                                      |
|-------------------------|--------------------------------|------------------------------------------------------|
| Crear Transmisión      | `$hub->createStream($key)`     | Crea una nueva transmisión con la clave dada.       |
| Obtener Transmisión    | `$hub->getStream($key)`        | Recupera una transmisión existente por clave.        |
| Listar Transmisiones   | `$hub->listStreams($marker, $limit, $prefix)` | Lista transmisiones con opciones de paginación.       |
| URL de Publicación RTMP| `$stream->rtmpPublishUrl($expire)` | Genera una URL de publicación RTMP con tiempo de expiración.  |
| URL de Reproducción RTMP| `$stream->rtmpPlayUrl()`       | Genera una URL de reproducción RTMP para la transmisión. |
| URL de Reproducción HLS | `$stream->hlsPlayUrl()`        | Genera una URL de reproducción HLS para la transmisión. |
| Deshabilitar Transmisión | `$stream->disable()`           | Deshabilita la transmisión.                         |
| Habilitar Transmisión  | `$stream->enable()`            | Habilita la transmisión.                            |
| Estado de la Transmisión | `$stream->status()`            | Recupera el estado actual de la transmisión.        |

Por ejemplo, para generar una URL de publicación RTMP con un tiempo de expiración de 60 segundos:
```php
$expire = 60;
$url = $stream->rtmpPublishUrl($expire);
echo $url;
```
Esta URL se puede usar para publicar transmisiones en Pili Streaming Cloud, con la expiración asegurando acceso temporal.

#### Consideraciones Adicionales
- **Estabilidad de la Versión**: La versión "dev-master" es la rama de desarrollo, potencialmente inestable. Para producción, considera usar una versión etiquetada, como 1.5.5, disponible en Packagist [pili-engineering/pili-sdk-php versions](https://packagist.org/p/pili-engineering/pili-sdk-php). El historial muestra actualizaciones como adiciones de API y refinamientos de métodos, con versiones que datan de 2016.
- **Manejo de Errores**: La documentación sugiere usar bloques try-catch para operaciones, como se ve en ejemplos para la creación y recuperación de transmisiones, para manejar posibles excepciones.
- **Documentación y Ejemplos**: Aunque los ejemplos específicos no se detallaron extensamente, el repositorio de GitHub [Pili Streaming Cloud server-side library for PHP](https://github.com/pili-engineering/pili-sdk-php) proporciona instrucciones de instalación y listas de características, y comparaciones con otros SDK de lenguajes (por ejemplo, Python) indican funcionalidad similar, como la generación de URLs.

#### Insights Comparativos
Comparando con otros SDK de Pili, como la versión de Python, se revelan patrones similares: ambos requieren credenciales, configuración de hub y operaciones de transmisión. La versión de PHP, sin embargo, usa un enfoque orientado a objetos con clases Hub y Stream, contrastando con el estilo más funcional de Python. Esto se alinea con las prácticas típicas de desarrollo de PHP, ofreciendo seguridad de tipos e integración con IDE.

#### Conclusión
Usar "pili-engineering/pili-sdk-php": "dev-master" implica instalarlo a través de Composer, configurar las credenciales de Qiniu, crear un objeto Hub y gestionar transmisiones con métodos como `rtmpPublishUrl`. Asegúrate de que tu entorno cumpla con los requisitos de PHP 5.3.0+ y considera la estabilidad para el uso en producción. Esta guía proporciona un punto de partida completo, con más detalles disponibles en la documentación oficial y el repositorio.

### Citaciones Clave
- [Pili Streaming Cloud server-side library for PHP GitHub](https://github.com/pili-engineering/pili-sdk-php)
- [pili-engineering/pili-sdk-php versions Packagist](https://packagist.org/p/pili-engineering/pili-sdk-php)