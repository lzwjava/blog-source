---
audio: false
generated: true
lang: es
layout: post
title: Biblioteca PHPExcel
translated: true
type: note
---

### Puntos Clave
- Es probable que para usar "phpoffice/phpexcel": "^1.8", necesites instalarlo mediante Composer y usar código PHP para leer y escribir archivos de Excel.
- La investigación sugiere que la librería está obsoleta, por lo que se recomienda considerar PhpSpreadsheet para nuevos proyectos.
- La evidencia indica que se requieren extensiones de PHP como mbstring, XML y XMLWriter.

### Instalación
Para comenzar, añade `"phpoffice/phpexcel": "^1.8"` a tu archivo `composer.json` y ejecuta `composer install`. Esto descargará la librería, que es esencial para trabajar con archivos de Excel en PHP.

### Uso Básico
Para escribir en un archivo de Excel:
- Incluye la librería con `require 'vendor/autoload.php';`.
- Crea un nuevo objeto PHPExcel: `$objPHPExcel = new PHPExcel();`.
- Establece valores en las celdas, ej., `$sheet->setCellValue('A1', 'valor');`.
- Guarda el archivo usando un escritor, como `$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');` seguido de `$writer->save('nombre_archivo.xlsx');`.

Para leer desde un archivo de Excel:
- Carga el archivo con `$objPHPExcel = PHPExcel_IOFactory::load('nombre_archivo.xlsx');`.
- Accede a los valores de las celdas, ej., `$cellValue = $sheet->getCell('A1')->getValue();`.

### Detalle Inesperado
Un aspecto inesperado es que PHPExcel admite varios formatos de archivo como .xls y .xlsx, y puede detectar automáticamente los tipos de archivo al leer, lo que simplifica su uso.

---

### Nota de Estudio: Guía Completa para Usar "phpoffice/phpexcel": "^1.8"

Esta nota proporciona una exploración detallada del uso de la librería PHPExcel, específicamente la versión 1.8 o superior, según lo especificado por la dependencia de Composer "phpoffice/phpexcel": "^1.8". Dado su estado de obsolescencia, esta guía también destaca consideraciones para alternativas modernas y asegura una comprensión exhaustiva tanto para usuarios principiantes como avanzados. El contenido está estructurado para cubrir instalación, uso, dependencias y contexto adicional, asegurando que se incluyan todos los detalles relevantes de la investigación.

#### Antecedentes y Contexto
PHPExcel es una librería de PHP diseñada para leer y escribir archivos de hojas de cálculo, particularmente formatos de Excel como .xls y .xlsx. La especificación de versión "^1.8" indica un rango de versionado semántico, lo que significa cualquier versión desde la 1.8 hasta, pero sin incluir, la 2.0, lo que, dada la historia de la librería, apunta a la versión 1.8.1 como la más reciente, lanzada en 2015. Sin embargo, la investigación indica que PHPExcel fue oficialmente declarada obsoleta en 2017 y archivada en 2019, con la recomendación de migrar a su sucesor, PhpSpreadsheet, debido a la falta de mantenimiento y posibles problemas de seguridad. Este contexto es crucial para los usuarios, ya que sugiere precaución para nuevos proyectos, aunque la guía se centrará en usar la versión especificada según lo solicitado.

La funcionalidad de la librería incluye crear, leer y manipular archivos de Excel, admitiendo formatos más allá de Excel como CSV y HTML. Formaba parte del proyecto PHPOffice, que desde entonces ha cambiado su enfoque a PhpSpreadsheet, ofreciendo características mejoradas y cumplimiento de los estándares de PHP. Dada la fecha actual, 3 de marzo de 2025, y el estado de archivo de la librería, los usuarios deben ser conscientes de sus limitaciones, especialmente con versiones más nuevas de PHP y actualizaciones de seguridad.

#### Proceso de Instalación
Para instalar "phpoffice/phpexcel": "^1.8", el proceso aprovecha Composer, el gestor de dependencias de PHP. Los pasos son los siguientes:
- Añade la dependencia a tu archivo `composer.json` en la sección "require": `"phpoffice/phpexcel": "^1.8"`.
- Ejecuta el comando `composer install` en el directorio de tu proyecto. Este comando descarga la librería y actualiza el directorio `vendor` con los archivos necesarios.

La notación de acento circunflejo (^) en Composer sigue el versionado semántico, asegurando que se instalen las versiones 1.8, 1.8.1 o cualquier actualización de parche, pero no versiones que rompan la compatibilidad (es decir, no la 2.0 o superior). Dado que el último lanzamiento de la librería fue la 1.8.1 en 2015, esto normalmente se resuelve a la versión 1.8.1.

La investigación confirma que la página de Packagist para phpoffice/phpexcel la lista como abandonada, sugiriendo phpoffice/phpspreadsheet en su lugar, pero sigue disponible para su instalación, alineándose con la solicitud del usuario.

#### Uso Básico: Escritura en Excel
Una vez instalada, usar PHPExcel implica incluir el archivo de autoload para la carga de clases y luego utilizar sus clases para la manipulación de hojas de cálculo. Aquí hay un desglose detallado:

- **Incluir el Archivo Autoload:** Comienza tu script PHP con `require 'vendor/autoload.php';`. Esta línea asegura que todas las librerías instaladas por Composer, incluyendo PHPExcel, se carguen automáticamente, aprovechando el autoloading PSR-0 según la estructura de la librería de 2015.

- **Crear un Nuevo Objeto PHPExcel:** Inicializa una nueva hoja de cálculo con `$objPHPExcel = new PHPExcel();`. Este objeto representa el libro de trabajo completo, permitiendo múltiples hojas y propiedades.

- **Trabajar con Hojas:** Accede a la hoja activa usando `$sheet = $objPHPExcel->getSheet(0);` para la primera hoja, o crea una nueva con `$sheet = $objPHPExcel->createSheet();`. Las hojas se indexan desde cero, por lo que `getSheet(0)` apunta a la primera hoja.

- **Establecer Valores de Celda:** Rellena las celdas usando el método `setCellValue`, ej., `$sheet->setCellValue('A1', 'Hola');`. Este método toma una referencia de celda (como 'A1') y el valor a insertar, que puede ser texto, números o fórmulas.

- **Guardar el Archivo:** Para guardar, crea un escritor para el formato deseado. Para Excel 2007 y superior (.xlsx), usa `$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');`. Luego guarda con `$writer->save('nombre_archivo.xlsx');`. Otros formatos incluyen 'Excel5' para .xls (Excel 95) o 'CSV' para valores separados por comas.

Un script de ejemplo para escribir podría verse así:
```php
require 'vendor/autoload.php';
$objPHPExcel = new PHPExcel();
$sheet = $objPHPExcel->getSheet(0);
$sheet->setCellValue('A1', 'Hola');
$sheet->setCellValue('B1', 'Mundo');
$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');
$writer->save('hola_mundo.xlsx');
```
Esto crea un archivo de Excel simple con "Hola" en A1 y "Mundo" en B1.

#### Uso Básico: Lectura desde Excel
Leer desde un archivo de Excel sigue un patrón similar pero comienza cargando el archivo:
- **Cargar el Archivo:** Usa `$objPHPExcel = PHPExcel_IOFactory::load('nombre_archivo.xlsx');` para cargar un archivo de Excel existente. El IOFactory puede detectar automáticamente el tipo de archivo, pero puedes especificar un lector, ej., `$objReader = PHPExcel_IOFactory::createReader('Excel2007'); $objPHPExcel = $objReader->load('nombre_archivo.xlsx');` para un tipo explícito.

- **Acceder a Hojas y Celdas:** Después de cargar, accede a las hojas como antes, ej., `$sheet = $objPHPExcel->getSheet(0);`. Recupera los valores de las celdas con `$cellValue = $sheet->getCell('A1')->getValue();`, que devuelve el contenido de la celda especificada.

Un ejemplo para leer:
```php
require 'vendor/autoload.php';
$objPHPExcel = PHPExcel_IOFactory::load('hola_mundo.xlsx');
$sheet = $objPHPExcel->getSheet(0);
$cellValue = $sheet->getCell('A1')->getValue();
echo $cellValue; // Muestra "Hola"
```
Esto lee el valor de A1, demostrando la recuperación básica.

#### Dependencias y Requisitos
PHPExcel tiene requisitos específicos de PHP y extensiones necesarias para su operación:
- **Versión de PHP:** Requiere PHP 5.2 o 7.0 o superior, según los metadatos de Packagist. Dada la fecha actual, 3 de marzo de 2025, la mayoría de las instalaciones modernas de PHP deberían cumplir esto, pero configuraciones más antiguas pueden necesitar actualizaciones.
- **Extensiones:** La librería depende de `ext-mbstring`, `ext-XML` y `ext-XMLWriter`, que deben estar habilitadas en tu configuración de PHP. Estas extensiones manejan la codificación de cadenas, el análisis XML y la escritura XML, respectivamente, esenciales para las operaciones con archivos de Excel.

Los usuarios deben verificar que estas extensiones estén activas usando `phpinfo()` o revisando el archivo `php.ini`, asegurando que no surjan problemas de compatibilidad.

#### Características Adicionales y Formatos
Más allá de la lectura/escritura básica, PHPExcel admite varios formatos de archivo, lo que es un detalle inesperado para usuarios familiarizados solo con Excel. La librería puede manejar:
- Excel 2007 (.xlsx) mediante el escritor/lector 'Excel2007'.
- Excel 95 (.xls) mediante 'Excel5'.
- Archivos CSV mediante 'CSV'.
- HTML mediante 'HTML'.

Al guardar, especifica el tipo de escritor; al leer, IOFactory a menudo detecta automáticamente, pero se pueden usar lectores explícitos para mayor confiabilidad. Por ejemplo, para guardar como .xls:
```php
$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel5');
$writer->save('nombre_archivo.xls');
```
Esta flexibilidad es útil para sistemas heredados o necesidades de formato específicas, aunque los usuarios deben tener en cuenta posibles limitaciones específicas del formato, especialmente con versiones antiguas de Excel.

#### Obsolescencia y Consejos de Migración
Un punto crítico es la obsolescencia de PHPExcel. La investigación muestra que fue archivada en 2019, con la última actualización en 2015, y ya no se mantiene. Esto plantea preocupaciones sobre vulnerabilidades de seguridad y compatibilidad con versiones de PHP más allá de la 7.0, especialmente con estándares modernos como PHP 8.x. Tanto el repositorio de GitHub como la página de Packagist recomiendan migrar a PhpSpreadsheet, que ofrece espacios de nombres, cumplimiento PSR y desarrollo activo.

Para los usuarios, esto significa:
- Para proyectos existentes que usan PHPExcel 1.8, continuar con precaución, asegurando pruebas de seguridad y compatibilidad.
- Para nuevos proyectos, considerar firmemente PhpSpreadsheet, con herramientas de migración disponibles, como se señala en la documentación de PhpSpreadsheet ([Migración desde PHPExcel](https://phpspreadsheet.readthedocs.io/en/latest/topics/migration-from-PHPExcel/)).

Este consejo es particularmente relevante dada la fecha actual, asegurando que los usuarios se alineen con librerías modernas y soportadas.

#### Documentación y Aprendizaje Adicional
Para una exploración más profunda, la documentación oficial de PHPExcel está disponible en su repositorio de GitHub bajo la carpeta Documentation, aunque el acceso puede requerir descargar archivos como la documentación de desarrollador DOC. En línea, tutoriales como el de SitePoint ([Generar Archivos de Excel y Gráficos con PHPExcel](https://www.sitepoint.com/generate-excel-files-charts-phpexcel/)) proporcionan ejemplos prácticos, cubriendo gráficos y formato, que van más allá del uso básico. Los hilos de Stack Overflow también ofrecen información de la comunidad, aunque se debe tener cuidado con respuestas desactualizadas dado el estado de la librería.

#### Tabla Comparativa: PHPExcel vs. PhpSpreadsheet
Para ayudar en la toma de decisiones, aquí hay una tabla comparativa que destaca las diferencias clave, basada en la investigación:

| Característica           | PHPExcel (1.8)                     | PhpSpreadsheet                  |
|--------------------------|------------------------------------|---------------------------------|
| Última Actualización     | 2015                              | Activo (a partir de 2025)       |
| Espacios de Nombres      | No, espacio de nombres raíz       | Sí, compatible con PSR-4        |
| Estado de Mantenimiento  | Obsoleto, archivado 2019          | Mantenido activamente           |
| Soporte de Versión PHP   | Hasta 7.0                         | PHP 7.4+                        |
| Soporte de Formatos      | Excel, CSV, HTML, etc.            | Mejorado, incluyendo ODS, PDF   |
| Rendimiento              | Moderado, intensivo en memoria    | Optimizado, escalable           |

Esta tabla subraya el cambio a PhpSpreadsheet para necesidades modernas, aunque PHPExcel sigue siendo funcional para propósitos heredados.

#### Conclusión
Usar "phpoffice/phpexcel": "^1.8" implica instalar mediante Composer, aprovechar sus clases para operaciones con Excel y asegurar las extensiones de PHP requeridas. Aunque es funcional, su obsolescencia requiere precaución, recomendándose PhpSpreadsheet para proyectos futuros. Esta guía proporciona un punto de partida completo, con ejemplos, dependencias y recursos adicionales para que los usuarios exploren más.

### Citas Clave
- [Página de Packagist phpoffice/phpexcel con detalles de instalación](https://packagist.org/packages/phpoffice/phpexcel)
- [Tutorial de SitePoint sobre generación de archivos Excel con PHPExcel](https://www.sitepoint.com/generate-excel-files-charts-phpexcel/)
- [Estado de archivo del repositorio de GitHub de PHPExcel](https://github.com/PHPOffice/PHPExcel)
- [Guía de migración de PhpSpreadsheet desde PHPExcel](https://phpspreadsheet.readthedocs.io/en/latest/topics/migration-from-PHPExcel/)