---
audio: false
generated: true
lang: es
layout: post
title: Herramienta PHP para Generar Códigos QR
translated: true
type: note
---

### Puntos Clave
- Parece probable que para usar "endroid/qr-code" versión 2.2.2, necesitas instalarlo vía Composer y asegurarte de que la extensión GD esté habilitada.
- La investigación sugiere que puedes generar códigos QR usando la clase Builder, configurando parámetros como datos, tamaño y escritor, luego guardar o mostrar el resultado.
- La evidencia indica que la biblioteca soporta formatos PNG, SVG y otros, con opciones para logos y etiquetas, pero verifica para la versión 2.2.2.

### Instalación
Primero, instala la biblioteca usando Composer con el comando:
```
composer require endroid/qr-code:2.2.2
```
Asegúrate de que tu configuración de PHP tenga la extensión GD habilitada, ya que es requerida para la generación de imágenes.

### Ejemplo de Uso
Aquí hay un ejemplo básico usando la clase Builder, que es probablemente compatible con la versión 2.2.2:
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
Esto crea un código QR para una URL y lo guarda como un archivo PNG. También puedes mostrarlo como un data URI para visualización web.

### Notas Adicionales
La biblioteca soporta varios escritores (ej. PNG, SVG) y permite personalizaciones como agregar logos o etiquetas. Sin embargo, dado que la versión 2.2.2 es antigua, algunas características en la documentación actual (como opciones avanzadas de logos) podrían no estar disponibles, así que consulta la documentación para esa versión específica en [GitHub](https://github.com/endroid/qr-code).

---

### Nota de Estudio: Guía Detallada sobre el Uso de "endroid/qr-code" Versión 2.2.2

Esta nota proporciona una guía completa sobre el uso de la biblioteca "endroid/qr-code", versión 2.2.2, para generar códigos QR en aplicaciones PHP. Amplía la respuesta directa incluyendo todos los detalles relevantes de la investigación, asegurando una comprensión exhaustiva para los desarrolladores, especialmente aquellos nuevos en la biblioteca. El contenido está estructurado para imitar un artículo profesional, con tablas para claridad y URLs integradas para referencia futura.

#### Introducción
La biblioteca "endroid/qr-code" es una herramienta PHP para generar códigos QR, ampliamente usada para aplicaciones como seguimiento de productos, gestión de documentos y marketing. La versión 2.2.2, especificada en la consulta, es una versión antigua, y aunque la biblioteca está marcada como abandonada en [Packagist](https://packagist.org/packages/endroid/qr-code), sigue siendo funcional para la generación básica de códigos QR. Esta guía describe la instalación y el uso, con un enfoque en asegurar la compatibilidad con la versión 2.2.2, reconociendo posibles diferencias con versiones más nuevas.

#### Proceso de Instalación
Para comenzar, debes instalar la biblioteca vía Composer, el gestor de paquetes de PHP. El comando es:
```
composer require endroid/qr-code:2.2.2
```
Esto asegura que obtengas la versión exacta 2.2.2. Un requisito crítico es la extensión GD para PHP, que debe estar habilitada y configurada, ya que es esencial para la generación de imágenes. Sin ella, la biblioteca no puede producir códigos QR visuales.

| Paso                  | Detalles                                                                 |
|-----------------------|-------------------------------------------------------------------------|
| Comando de Instalación| `composer require endroid/qr-code:2.2.2`                                |
| Requisito de PHP      | Asegurar que la extensión GD esté habilitada (verificar `phpinfo()` para confirmación) |

La investigación indica que el repositorio GitHub de la biblioteca ([GitHub](https://github.com/endroid/qr-code)) y las páginas de [Packagist](https://packagist.org/packages/endroid/qr-code) confirman este método de instalación, sin que se haya encontrado documentación específica para la versión 2.2.2, lo que sugiere depender de patrones de uso generales.

#### Detalles de Uso
La biblioteca ofrece dos métodos principales para la generación de códigos QR: usando la clase Builder o directamente con la clase QrCode. Dado el enfoque de la consulta en el uso, se recomienda el enfoque Builder por su simplicidad, aunque ambos se detallan aquí para mayor exhaustividad.

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
Este código crea un código QR para la URL, usando formato PNG, con codificación ISO-8859-1 para mejor compatibilidad con escáneres y alta corrección de errores. También puedes mostrarlo como un data URI:
```php
$qrCodeDataUri = $qrCode->getDataUri();
```
Esto es útil para incrustar en HTML, ej., `<img src="<?php echo $qrCodeDataUri; ?>">`.

Sin embargo, dada la antigüedad de la versión 2.2.2, algunas clases como `ErrorCorrectionLevelHigh` podrían tener nombres diferentes (ej., `ErrorCorrectionLevel::HIGH` en versiones más antiguas). La investigación de publicaciones en Stack Overflow ([Stack Overflow](https://stackoverflow.com/questions/40777377/endroid-qr-code)) sugiere que las versiones antiguas usaban métodos como `setErrorCorrection('high')`, así que verifica la API para la 2.2.2.

##### Usando la Clase QrCode Directamente
Para más control, puedes usar la clase QrCode, como se ve en los ejemplos:
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
Este método es más detallado pero permite ajustes finos, como establecer colores de primer plano y fondo, lo que podría ser relevante para la versión 2.2.2. Nuevamente, verifica la disponibilidad de los métodos en la documentación.

#### Opciones de Configuración
La biblioteca soporta varios escritores para diferentes formatos de salida, como se detalla en la tabla a continuación, basada en la documentación actual, con una nota para verificar para la versión 2.2.2:

| Clase de Escritor     | Formato  | Notas                                                                 |
|-----------------------|----------|----------------------------------------------------------------------|
| PngWriter             | PNG      | Nivel de compresión configurable, por defecto -1                     |
| SvgWriter             | SVG      | Adecuado para gráficos vectoriales, sin opciones de compresión       |
| WebPWriter            | WebP     | Calidad 0-100, por defecto 80, bueno para uso web                    |
| PdfWriter             | PDF      | Unidad en mm, por defecto, bueno para impresión                      |

Las opciones de codificación incluyen UTF-8 (por defecto) e ISO-8859-1, recomendándose esta última para compatibilidad con escáneres de códigos de barras. Los modos de tamaño de bloque redondeado (margen, agrandar, reducir, ninguno) pueden mejorar la legibilidad, pero su disponibilidad en la 2.2.2 necesita confirmación.

#### Características Avanzadas y Consideraciones
Para uso avanzado, como incrustar logos, la clase Builder soporta métodos como `logoPath()` y `logoResizeToWidth()`, como se ve en un artículo de Medium ([Medium](https://johnrix.medium.com/creating-qr-codes-with-embedded-images-in-php-d926e4546b31)). Sin embargo, estas podrían ser adiciones posteriores a la 2.2.2, así que prueba la compatibilidad. La validación de códigos QR generados es posible pero impacta el rendimiento y está deshabilitada por defecto, un detalle de [GitHub](https://github.com/endroid/qr-code).

Dada la nota de abandono de la biblioteca en [Packagist](https://packagist.org/packages/endroid/qr-code), vale la pena señalar posibles preocupaciones de seguridad o mantenimiento, aunque para uso básico, sigue siendo viable. Para usuarios de Symfony, hay un bundle ([GitHub](https://github.com/endroid/qr-code-bundle)), pero eso está fuera del uso general de PHP.

#### Notas Específicas de la Versión
La investigación no mostró documentación directa para la versión 2.2.2, y las etiquetas de GitHub no la listan, sugiriendo que podría ser una versión antigua o un error tipográfico. El repositorio actual muestra versiones hasta la 6.0.0, y [Packagist](https://packagist.org/packages/endroid/qr-code) la lista como abandonada, recomendando endroid/qr-code, lo que es confuso ya que es el mismo paquete. Esto indica posibles problemas de renombrado o versionado, por lo que los usuarios deben bloquear dependencias y probar actualizaciones.

#### Conclusión
Usar "endroid/qr-code" versión 2.2.2 implica instalar vía Composer, asegurar la extensión GD, y generar códigos QR con la clase Builder o QrCode. Aunque los ejemplos se basan en la documentación actual, verifica las diferencias de API para la 2.2.2, especialmente para características avanzadas. Para más detalles, consulta la página GitHub de la biblioteca y las discusiones relacionadas en Stack Overflow.

#### Citas Clave
- [Repositorio GitHub del Generador de Códigos QR](https://github.com/endroid/qr-code)
- [Página Packagist de endroid/qr-code](https://packagist.org/packages/endroid/qr-code)
- [Artículo de Medium sobre Crear Códigos QR con Imágenes Incrustadas](https://johnrix.medium.com/creating-qr-codes-with-embedded-images-in-php-d926e4546b31)
- [Discusión en Stack Overflow sobre Endroid QR Code](https://stackoverflow.com/questions/40777377/endroid-qr-code)