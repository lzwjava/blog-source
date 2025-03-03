---
audio: false
generated: true
lang: es
layout: post
title: Biblioteca PHPExcel
translated: true
---

### Puntos Clave
- Parece probable que para usar "phpoffice/phpexcel": "^1.8", necesites instalarlo a través de Composer y usar código PHP para leer y escribir archivos Excel.
- La investigación sugiere que la biblioteca está obsoleta, por lo que considera usar PhpSpreadsheet para nuevos proyectos.
- La evidencia indica que se requiere extensiones de PHP como mbstring, XML y XMLWriter.

### Instalación
Para comenzar, agrega `"phpoffice/phpexcel": "^1.8"` a tu archivo `composer.json` y ejecuta `composer install`. Esto descargará la biblioteca, que es esencial para trabajar con archivos Excel en PHP.

### Uso Básico
Para escribir en un archivo Excel:
- Incluye la biblioteca con `require 'vendor/autoload.php';`.
- Crea un nuevo objeto PHPExcel: `$objPHPExcel = new PHPExcel();`.
- Establece los valores de las celdas, por ejemplo, `$sheet->setCellValue('A1', 'value');`.
- Guarda el archivo usando un escritor, como `$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');` seguido de `$writer->save('filename.xlsx');`.

Para leer de un archivo Excel:
- Carga el archivo con `$objPHPExcel = PHPExcel_IOFactory::load('filename.xlsx');`.
- Accede a los valores de las celdas, por ejemplo, `$cellValue = $sheet->getCell('A1')->getValue();`.

### Detalle Inesperado
Un aspecto inesperado es que PHPExcel soporta varios formatos de archivo como .xls y .xlsx, y puede detectar automáticamente los tipos de archivo al leer, lo que simplifica el uso.

---

### Nota de Encuesta: Guía Completa para Usar "phpoffice/phpexcel": "^1.8"

Esta nota proporciona una exploración detallada del uso de la biblioteca PHPExcel, específicamente la versión 1.8 o superior, según la dependencia de Composer "phpoffice/phpexcel": "^1.8". Dado su estado de obsolescencia, esta guía también destaca consideraciones para alternativas modernas y asegura una comprensión exhaustiva tanto para principiantes como para usuarios avanzados. El contenido está estructurado para cubrir la instalación, el uso, las dependencias y el contexto adicional, asegurando que todos los detalles relevantes de la investigación estén incluidos.

#### Antecedentes y Contexto
PHPExcel es una biblioteca de PHP diseñada para leer y escribir archivos de hoja de cálculo, especialmente formatos de Excel como .xls y .xlsx. La especificación de versión "^1.8" indica un rango de versionado semántico, lo que significa cualquier versión desde 1.8 hasta, pero sin incluir, 2.0, lo que, dado el historial de la biblioteca, apunta a la versión 1.8.1 como la última, lanzada en 2015. Sin embargo, la investigación indica que PHPExcel fue oficialmente obsoleta en 2017 y archivada en 2019, con la recomendación de migrar a su sucesor, PhpSpreadsheet, debido a la falta de mantenimiento y posibles problemas de seguridad. Este contexto es crucial para los usuarios, ya que sugiere precaución para nuevos proyectos, aunque la guía se centrará en usar la versión especificada según lo solicitado.

La funcionalidad de la biblioteca incluye crear, leer y manipular archivos Excel, soportando formatos más allá de Excel como CSV y HTML. Fue parte del proyecto PHPOffice, que desde entonces ha cambiado su enfoque a PhpSpreadsheet, ofreciendo características mejoradas y cumplimiento con los estándares de PHP. Dado la fecha actual, 3 de marzo de 2025, y el estado de archivo de la biblioteca, los usuarios deben estar conscientes de sus limitaciones, especialmente con versiones más nuevas de PHP y actualizaciones de seguridad.

#### Proceso de Instalación
Para instalar "phpoffice/phpexcel": "^1.8", el proceso utiliza Composer, el gestor de dependencias de PHP. Los pasos son los siguientes:
- Agrega la dependencia a tu archivo `composer.json` en la sección "require": `"phpoffice/phpexcel": "^1.8"`.
- Ejecuta el comando `composer install` en tu directorio de proyecto. Este comando descarga la biblioteca y actualiza el directorio `vendor` con los archivos necesarios.

La notación de cuidado (^) en Composer sigue el versionado semántico, asegurando que se instalen las versiones 1.8, 1.8.1 o cualquier actualización de parche, pero no versiones que romperían la compatibilidad (es decir, no 2.0 o superior). Dado que el último lanzamiento de la biblioteca fue 1.8.1 en 2015, esto generalmente se resuelve en la versión 1.8.1.

La investigación confirma que la página de Packagist para phpoffice/phpexcel la lista como abandonada, sugiriendo phpoffice/phpspreadsheet en su lugar, pero sigue disponible para la instalación, alineándose con la solicitud del usuario.

#### Uso Básico: Escribir en Excel
Una vez instalado, usar PHPExcel implica incluir el archivo de autocarga para la carga de clases y luego utilizar sus clases para la manipulación de hojas de cálculo. Aquí tienes un desglose detallado:

- **Incluir el Archivo de Autocarga:** Comienza tu script de PHP con `require 'vendor/autoload.php';`. Esta línea asegura que todas las bibliotecas instaladas por Composer, incluyendo PHPExcel, se carguen automáticamente, utilizando la carga automática PSR-0 según la estructura de la biblioteca de 2015.

- **Crear un Nuevo Objeto PHPExcel:** Inicializa una nueva hoja de cálculo con `$objPHPExcel = new PHPExcel();`. Este objeto representa todo el libro de trabajo, permitiendo múltiples hojas y propiedades.

- **Trabajar con Hojas:** Accede a la hoja activa usando `$sheet = $objPHPExcel->getSheet(0);` para la primera hoja, o crea una nueva con `$sheet = $objPHPExcel->createSheet();`. Las hojas están indexadas en cero, por lo que `getSheet(0)` apunta a la primera hoja.

- **Establecer Valores de Celdas:** Rellena las celdas usando el método `setCellValue`, por ejemplo, `$sheet->setCellValue('A1', 'Hello');`. Este método toma una referencia de celda (como 'A1') y el valor a insertar, que puede ser texto, números o fórmulas.

- **Guardar el Archivo:** Para guardar, crea un escritor para el formato deseado. Para Excel 2007 y versiones superiores (.xlsx), usa `$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');`. Luego guarda con `$writer->save('filename.xlsx');`. Otros formatos incluyen 'Excel5' para .xls (Excel 95) o 'CSV' para valores separados por comas.

Un script de ejemplo para escribir podría verse así:
```php
require 'vendor/autoload.php';
$objPHPExcel = new PHPExcel();
$sheet = $objPHPExcel->getSheet(0);
$sheet->setCellValue('A1', 'Hello');
$sheet->setCellValue('B1', 'World');
$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');
$writer->save('hello_world.xlsx');
```
Esto crea un archivo Excel simple con "Hello" en A1 y "World" en B1.

#### Uso Básico: Leer de Excel
Leer de un archivo Excel sigue un patrón similar, pero comienza cargando el archivo:
- **Cargar el Archivo:** Usa `$objPHPExcel = PHPExcel_IOFactory::load('filename.xlsx');` para cargar un archivo Excel existente. La IOFactory puede detectar automáticamente el tipo de archivo, pero puedes especificar un lector, por ejemplo, `$objReader = PHPExcel_IOFactory::createReader('Excel2007'); $objPHPExcel = $objReader->load('filename.xlsx');` para un tipo explícito.

- **Acceder a Hojas y Celdas:** Después de cargar, accede a las hojas como antes, por ejemplo, `$sheet = $objPHPExcel->getSheet(0);`. Recupera los valores de las celdas con `$cellValue = $sheet->getCell('A1')->getValue();`, que devuelve el contenido de la celda especificada.

Un ejemplo para leer:
```php
require 'vendor/autoload.php';
$objPHPExcel = PHPExcel_IOFactory::load('hello_world.xlsx');
$sheet = $objPHPExcel->getSheet(0);
$cellValue = $sheet->getCell('A1')->getValue();
echo $cellValue; // Muestra "Hello"
```
Esto lee el valor de A1, demostrando la recuperación básica.

#### Dependencias y Requisitos
PHPExcel tiene requisitos específicos de PHP y extensiones necesarias para su funcionamiento:
- **Versión de PHP:** Requiere PHP 5.2 o 7.0 o superior, según los metadatos de Packagist. Dada la fecha actual, 3 de marzo de 2025, la mayoría de las instalaciones de PHP modernas deberían cumplir con esto, pero las configuraciones más antiguas pueden necesitar actualizaciones.
- **Extensiones:** La biblioteca depende de `ext-mbstring`, `ext-XML` y `ext-XMLWriter`, que deben estar habilitadas en tu configuración de PHP. Estas extensiones manejan la codificación de cadenas, el análisis de XML y la escritura de XML, respectivamente, esenciales para las operaciones de archivos Excel.

Los usuarios deben verificar que estas extensiones estén activas usando `phpinfo()` o revisando el archivo `php.ini`, asegurando que no surjan problemas de compatibilidad.

#### Características Adicionales y Formatos
Más allá de la lectura/escritura básica, PHPExcel soporta varios formatos de archivo, lo cual es un detalle inesperado para los usuarios familiarizados solo con Excel. La biblioteca puede manejar:
- Excel 2007 (.xlsx) a través del escritor/lector 'Excel2007'.
- Excel 95 (.xls) a través de 'Excel5'.
- Archivos CSV a través de 'CSV'.
- HTML a través de 'HTML'.

Al guardar, especifica el tipo de escritor; al leer, la IOFactory a menudo detecta automáticamente, pero los lectores explícitos pueden usarse para confiabilidad. Por ejemplo, para guardar como .xls:
```php
$writer = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel5');
$writer->save('filename.xls');
```
Esta flexibilidad es útil para sistemas heredados o necesidades específicas de formato, aunque los usuarios deben tener en cuenta posibles limitaciones específicas del formato, especialmente con versiones más antiguas de Excel.

#### Obsolescencia y Consejos de Migración
Un punto crítico es la obsolescencia de PHPExcel. La investigación muestra que fue archivada en 2019, con la última actualización en 2015, y ya no se mantiene. Esto plantea preocupaciones sobre vulnerabilidades de seguridad y compatibilidad con versiones de PHP más allá de 7.0, especialmente con estándares modernos como PHP 8.x. El repositorio de GitHub y la página de Packagist ambos recomiendan migrar a PhpSpreadsheet, que ofrece namespaces, cumplimiento con PSR y desarrollo activo.

Para los usuarios, esto significa:
- Para proyectos existentes que usan PHPExcel 1.8, continúa con precaución, asegurando pruebas de seguridad y compatibilidad.
- Para nuevos proyectos, considera fuertemente PhpSpreadsheet, con herramientas de migración disponibles, como se indica en la documentación de PhpSpreadsheet ([Migración desde PHPExcel](https://phpspreadsheet.readthedocs.io/en/latest/topics/migration-from-PHPExcel/)).

Este consejo es particularmente relevante dado la fecha actual, asegurando que los usuarios se alineen con bibliotecas modernas y soportadas.

#### Documentación y Aprendizaje Adicional
Para una exploración más profunda, la documentación oficial de PHPExcel está disponible en su repositorio de GitHub bajo la carpeta de Documentación, aunque el acceso puede requerir descargar archivos como la documentación del desarrollador DOC. En línea, tutoriales como el de SitePoint ([Generar Archivos Excel y Gráficos con PHPExcel](https://www.sitepoint.com/generate-excel-files-charts-phpexcel/)) proporcionan ejemplos prácticos, cubriendo gráficos y formato, que se extienden más allá del uso básico. Los hilos de Stack Overflow también ofrecen conocimientos de la comunidad, aunque se debe tener cuidado con respuestas obsoletas dado el estado de la biblioteca.

#### Tabla Comparativa: PHPExcel vs. PhpSpreadsheet
Para ayudar en la toma de decisiones, aquí tienes una tabla de comparación que destaca las diferencias clave, basada en la investigación:

| Característica                  | PHPExcel (1.8)                     | PhpSpreadsheet                  |
|--------------------------|------------------------------------|---------------------------------|
| Última Actualización              | 2015                              | Activo (hasta 2025)             |
| Namespaces               | No, namespace raíz                | Sí, cumplimiento PSR-4            |
| Estado de Mantenimiento       | Obsoleto, archivado 2019         | Mantenido activamente             |
| Soporte de Versión de PHP      | Hasta 7.0                         | PHP 7.4+                        |
| Soporte de Formato de Archivo      | Excel, CSV, HTML, etc.            | Mejorado, incluyendo ODS, PDF    |
| Rendimiento              | Moderado, intensivo en memoria        | Optimizado, escalable             |

Esta tabla subraya el cambio a PhpSpreadsheet para necesidades modernas, aunque PHPExcel sigue siendo funcional para propósitos heredados.

#### Conclusión
Usar "phpoffice/phpexcel": "^1.8" implica instalarlo a través de Composer, aprovechar sus clases para operaciones de Excel y asegurarse de que las extensiones de PHP necesarias estén disponibles. Aunque funcional, su obsolescencia requiere precaución, con PhpSpreadsheet recomendado para proyectos futuros. Esta guía proporciona un punto de partida completo, con ejemplos, dependencias y recursos adicionales para que los usuarios exploren más a fondo.

### Citaciones Clave
- [Página de Packagist phpoffice/phpexcel con detalles de instalación](https://packagist.org/packages/phpoffice/phpexcel)
- [Tutorial de SitePoint sobre generar archivos Excel con PHPExcel](https://www.sitepoint.com/generate-excel-files-charts-phpexcel/)
- [Estado archivado del repositorio de GitHub de PHPExcel](https://github.com/PHPOffice/PHPExcel)
- [Guía de migración de PhpSpreadsheet desde PHPExcel](https://phpspreadsheet.readthedocs.io/en/latest/topics/migration-from-PHPExcel/)