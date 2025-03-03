---
audio: false
generated: true
lang: es
layout: post
title: Herramienta de PHP para Generar Códigos QR
translated: true
---

### Puntos Clave
- Parece probable que para usar "endroid/qr-code" versión 2.2.2, necesites instalarlo a través de Composer y asegurarte de que la extensión GD esté habilitada.
- La investigación sugiere que puedes generar códigos QR utilizando la clase Builder, configurando parámetros como datos, tamaño y escritor, y luego guardando o mostrando el resultado.
- La evidencia indica que la biblioteca soporta PNG, SVG y otros formatos, con opciones para logotipos y etiquetas, pero verifica para la versión 2.2.2.

### Instalación
Primero, instala la biblioteca usando Composer con el siguiente comando:
```
composer require endroid/qr-code:2.2.2
```
Asegúrate de que tu configuración de PHP tenga la extensión GD habilitada, ya que es requerida para la generación de imágenes.

### Ejemplo de Uso
Aquí tienes un ejemplo básico utilizando la clase Builder, que probablemente es compatible con la versión 2.2.2:
```php
use Endroid\QrCode\Builder\Builder;
use Endroid\QrCode\Encoding\Encoding;
use Endroid\QrCode\ErrorCorrectionLevel\ErrorCorrectionLevelHigh;
use Endroid\QrCode\Writer\PngWriter;

$url = 'https://example.com';
$qrCode = Builder::create()
    ->writer(new PngWriter())
    ->data($url)
    ->encoding(new Encoding('ISO-8859-1'))
    ->errorCorrectionLevel(new ErrorCorrectionLevelHigh())
    ->build();
$qrCode->saveToFile('qr_code.png');
```
Esto crea un código QR para una URL y lo guarda como un archivo PNG. También puedes mostrarlo como un URI de datos para su visualización en la web.

### Notas Adicionales
La biblioteca soporta varios escritores (por ejemplo, PNG, SVG) y permite personalizaciones como agregar logotipos o etiquetas. Sin embargo, dado que la versión 2.2.2 es antigua, algunas características en la documentación actual (como opciones avanzadas de logotipos) pueden no estar disponibles, así que verifica la documentación para esa versión específica en [GitHub](https://github.com/endroid/qr-code).

---

### Nota de Encuesta: Guía Detallada sobre el Uso de "endroid/qr-code" Versión 2.2.2

Esta nota proporciona una guía completa sobre el uso de la biblioteca "endroid/qr-code", versión 2.2.2, para generar códigos QR en aplicaciones PHP. Expande la respuesta directa incluyendo todos los detalles relevantes de la investigación, asegurando una comprensión exhaustiva para los desarrolladores, especialmente aquellos nuevos en la biblioteca. El contenido está estructurado para imitar un artículo profesional, con tablas para claridad y URLs en línea para referencia adicional.

#### Introducción
La biblioteca "endroid/qr-code" es una herramienta PHP para generar códigos QR, ampliamente utilizada para aplicaciones como el seguimiento de productos, la gestión de documentos y el marketing. La versión 2.2.2, especificada en la consulta, es un lanzamiento antiguo, y aunque la biblioteca está marcada como abandonada en [Packagist](https://packagist.org/packages/endroid/qr-code), sigue siendo funcional para la generación básica de códigos QR. Esta guía detalla la instalación y el uso, con un enfoque en asegurar la compatibilidad con la versión 2.2.2, reconociendo las posibles diferencias con versiones más nuevas.

#### Proceso de Instalación
Para comenzar, debes instalar la biblioteca a través de Composer, el gestor de paquetes de PHP. El comando es:
```
composer require endroid/qr-code:2.2.2
```
Esto asegura que obtendrás exactamente la versión 2.2.2. Un requisito crítico es la extensión GD para PHP, que debe estar habilitada y configurada, ya que es esencial para la generación de imágenes. Sin ella, la biblioteca no puede producir códigos QR visuales.

| Paso                  | Detalles                                                                 |
|-----------------------|-------------------------------------------------------------------------|
| Comando de Instalación | `composer require endroid/qr-code:2.2.2`                                |
| Requisito de PHP      | Asegúrate de que la extensión GD esté habilitada (verifica `phpinfo()` para confirmación)     |

La investigación indica que el repositorio de GitHub ([GitHub](https://github.com/endroid/qr-code)) y las páginas de [Packagist](https://packagist.org/packages/endroid/qr-code) confirman este método de instalación, sin encontrar documentación específica para la versión 2.2.2, lo que sugiere depender de patrones de uso generales.

#### Detalles de Uso
La biblioteca ofrece dos métodos principales para la generación de códigos QR: utilizando la clase Builder o directamente con la clase QrCode. Dado el enfoque de la consulta en el uso, se recomienda el enfoque Builder por su simplicidad, aunque ambos se detallan aquí para completitud.

##### Usando la Clase Builder
La clase Builder proporciona una interfaz fluida para configurar códigos QR. Basado en ejemplos de la documentación reciente, una implementación básica es:
```php
use Endroid\QrCode\Builder\Builder;
use Endroid\QrCode\Encoding\Encoding;
use Endroid\QrCode\ErrorCorrectionLevel\ErrorCorrectionLevelHigh;
use Endroid\QrCode\Writer\PngWriter;

$url = 'https://example.com';
$qrCode = Builder::create()
    ->writer(new PngWriter())
    ->data($url)
    ->encoding(new Encoding('ISO-8859-1'))
    ->errorCorrectionLevel(new ErrorCorrectionLevelHigh())
    ->build();
$qrCode->saveToFile('qr_code.png');
```
Este código crea un código QR para la URL, utilizando el formato PNG, con codificación ISO-8859-1 para mejor compatibilidad con los escáneres y alta corrección de errores. También puedes mostrarlo como un URI de datos:
```php
$qrCodeDataUri = $qrCode->getDataUri();
```
Esto es útil para incrustarlo en HTML, por ejemplo, `<img src="<?php echo $qrCodeDataUri; ?>">`.

Sin embargo, dado la antigüedad de la versión 2.2.2, algunas clases como `ErrorCorrectionLevelHigh` pueden tener nombres diferentes (por ejemplo, `ErrorCorrectionLevel::HIGH` en versiones más antiguas). La investigación de publicaciones en Stack Overflow ([Stack Overflow](https://stackoverflow.com/questions/40777377/endroid-qr-code)) sugiere que versiones más antiguas utilizaban métodos como `setErrorCorrection('high')`, así que verifica la API para 2.2.2.

##### Usando la Clase QrCode Directamente
Para más control, puedes usar la clase QrCode, como se ve en ejemplos:
```php
use Endroid\QrCode\QrCode;
use Endroid\QrCode\Writer\PngWriter;

$qrCode = new QrCode('Life is too short to be generating QR codes');
$qrCode->setSize(300);
$qrCode->setMargin(10);
$writer = new PngWriter();
$result = $writer->write($qrCode);
$result->saveToFile('qrcode.png');
```
Este método es más verboso pero permite ajustes finos, como establecer colores de primer plano y fondo, que podrían ser relevantes para la versión 2.2.2. Nuevamente, verifica la documentación para la disponibilidad de métodos.

#### Opciones de Configuración
La biblioteca soporta varios escritores para diferentes formatos de salida, como se detalla en la tabla a continuación, basada en la documentación actual, con una nota para verificar para la versión 2.2.2:

| Clase de Escritor       | Formato   | Notas                                                                 |
|-----------------------|----------|----------------------------------------------------------------------|
| PngWriter             | PNG      | Nivel de compresión configurable, predeterminado -1                           |
| SvgWriter             | SVG      | Adecuado para gráficos vectoriales, sin opciones de compresión                 |
| WebPWriter            | WebP     | Calidad 0-100, predeterminado 80, buena para uso web                          |
| PdfWriter             | PDF      | Unidad en mm, predeterminado, buena para impresión                                 |

Las opciones de codificación incluyen UTF-8 (predeterminado) e ISO-8859-1, con esta última recomendada para la compatibilidad con escáneres de códigos de barras. Los modos de tamaño de bloque redondo (margen, agrandar, reducir, ninguno) pueden mejorar la legibilidad, pero su disponibilidad en 2.2.2 necesita confirmación.

#### Características Avanzadas y Consideraciones
Para uso avanzado, como incrustar logotipos, la clase Builder soporta métodos como `logoPath()` y `logoResizeToWidth()`, como se ve en un artículo de Medium ([Medium](https://johnrix.medium.com/creating-qr-codes-with-embedded-images-in-php-d926e4546b31)). Sin embargo, estos podrían ser adiciones posteriores a 2.2.2, así que prueba la compatibilidad. La validación de los códigos QR generados es posible pero afecta el rendimiento y está deshabilitada por defecto, un detalle de [GitHub](https://github.com/endroid/qr-code).

Dado el aviso de abandono de la biblioteca en [Packagist](https://packagist.org/packages/endroid/qr-code), es importante tener en cuenta posibles preocupaciones de seguridad o mantenimiento, aunque para uso básico sigue siendo viable. Para usuarios de Symfony, hay un paquete ([GitHub](https://github.com/endroid/qr-code-bundle)), pero eso está fuera del uso general de PHP.

#### Notas Específicas de la Versión
La investigación no mostró documentación directa para la versión 2.2.2, con las etiquetas de GitHub no listándola, lo que sugiere que podría ser un lanzamiento antiguo o un error tipográfico. El repositorio actual muestra versiones hasta 6.0.0, y [Packagist](https://packagist.org/packages/endroid/qr-code) lo lista como abandonado, recomendando endroid/qr-code, lo que es confuso ya que es el mismo paquete. Esto indica posibles problemas de renombrado o versionado, por lo que los usuarios deben bloquear dependencias y probar actualizaciones.

#### Conclusión
Usar "endroid/qr-code" versión 2.2.2 implica instalarlo a través de Composer, asegurarse de que la extensión GD esté habilitada y generar códigos QR con la clase Builder o QrCode. Aunque los ejemplos se basan en la documentación actual, verifica las diferencias de API para 2.2.2, especialmente para características avanzadas. Para más detalles, consulta la página de GitHub de la biblioteca y las discusiones relacionadas en Stack Overflow.

#### Citaciones Clave
- [Repositorio de Generador de Código QR en GitHub](https://github.com/endroid/qr-code)
- [Página de endroid/qr-code en Packagist](https://packagist.org/packages/endroid/qr-code)
- [Artículo de Medium sobre Creación de Códigos QR con Imágenes Incrustadas](https://johnrix.medium.com/creating-qr-codes-with-embedded-images-in-php-d926e4546b31)
- [Discusión de Endroid QR Code en Stack Overflow](https://stackoverflow.com/questions/40777377/endroid-qr-code)