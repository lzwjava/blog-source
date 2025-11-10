---
audio: false
generated: true
lang: es
layout: post
title: Dominando el Reemplazo Estructural de IntelliJ
translated: true
type: note
---

Claro, desglosemos la función de Reemplazo Estructural de IntelliJ IDEA.

El Reemplazo Estructural de IntelliJ IDEA es una función increíblemente poderosa, aunque a menudo infrautilizada, que te permite buscar y reemplazar patrones de código basándote en su **estructura** en lugar de solo en su contenido textual. Esto va mucho más allá de una simple búsqueda y reemplazo de texto, permitiendo refactorizaciones complejas, aplicación de estilos de código y corrección de errores en una base de código extensa.

Aquí tienes una guía completa:

-----

## IntelliJ IDEA Reemplazo Estructural: Una Guía Completa

### 1. ¿Qué es la Búsqueda y Reemplazo Estructural (SSR)?

En esencia, SSR en IntelliJ IDEA trata sobre trabajar con Árboles de Sintaxis Abstracta (ASTs). En lugar de buscar cadenas literales, defines un *patrón* que describe la estructura del código que quieres encontrar (Búsqueda Estructural) y otro patrón que describe cómo quieres transformarlo (Reemplazo Estructural).

Esto te permite:

* **Refactorizar código:** Cambiar la forma en que se llaman los métodos, reordenar parámetros, encapsular campos, etc.
* **Hacer cumplir estándares de código:** Asegurar un uso consistente de construcciones específicas del lenguaje o llamadas a API.
* **Corregir errores comunes:** Identificar y corregir errores lógicos recurrentes.
* **Migrar APIs:** Actualizar el código cuando las librerías o frameworks cambian.
* **Limpiar código obsoleto:** Encontrar y reemplazar usos de APIs antiguas con las nuevas.

### 2. Accediendo a la Búsqueda y Reemplazo Estructural

Puedes acceder al diálogo de SSR de dos maneras:

* **Ve a Editar -> Buscar -> Buscar Estructuralmente...** (para buscar)
* **Ve a Editar -> Buscar -> Reemplazar Estructuralmente...** (para reemplazar directamente)

El diálogo para ambos es muy similar, con "Reemplazar Estructuralmente" simplemente añadiendo un campo "Plantilla de Reemplazo".

### 3. Entendiendo el Diálogo de Búsqueda Estructural

El diálogo de Búsqueda Estructural es donde defines tu patrón de búsqueda.

#### 3.1. Plantilla de Búsqueda

Esta es la parte más crucial. Escribes un fragmento de código que representa la *estructura* que estás buscando.

**Conceptos Clave:**

* **Código Literal:** Cualquier código que escribas directamente se comparará literalmente.
* **Variables:** Usa variables para representar partes del código que pueden variar. Las variables se definen usando una sintaxis especial y luego se configuran con restricciones.
    * **Sintaxis común de variable:** `$nombreDeVariable$` (encerrado entre signos de dólar).
    * **Ejemplo:** `System.out.println($arg$);` encontrará cualquier llamada a `System.out.println`, donde `$arg$` coincidirá con lo que esté dentro de los paréntesis.

#### 3.2. Restricciones de Script (en variables)

Después de definir variables en tu "Plantilla de Búsqueda", necesitas especificar sus restricciones. Esto se hace seleccionando la variable en la plantilla (o colocando el cursor sobre ella) y luego usando el botón "Editar variables" (a menudo un pequeño icono de lápiz junto al campo de la plantilla o accesible a través de la pestaña "Variables").

Las restricciones comunes incluyen:

* **Texto (regexp):** Una expresión regular con la que el contenido de texto de la variable debe coincidir.
* **Tipo (regexp):** Una expresión regular con la que el tipo de la variable debe coincidir (ej., `java.lang.String`, `int[]`).
* **Recuento:** Especifica cuántas veces puede aparecer un elemento variable (ej., `[0, N]`, `[1, N]`, `[1, 1]`). Esto es especialmente útil para colecciones de sentencias o parámetros de método.
* **Referencia:** Si la variable representa un identificador (como un nombre de método o de variable), puedes restringirlo para que se refiera a un tipo o declaración específica.
* **Dentro de:** Restringe la variable para que esté dentro de un cierto ámbito o declaración.
* **No RegExp:** Excluye coincidencias basadas en una expresión regular.
* **Condición (script Groovy):** Esta es la restricción más poderosa. Puedes escribir un script Groovy que se evalúe como `true` o `false`. Este script tiene acceso al elemento coincidente y sus propiedades, permitiendo lógica muy compleja.
    * **Ejemplo de Script:** Para comprobar si el valor de una variable entera es mayor que 10: `_target.text.toInteger() > 10` (donde `_target` es el elemento coincidente para la variable).

#### 3.3. Opciones

Debajo de la plantilla, hay varias opciones para refinar tu búsqueda:

* **Contexto:** Define el ámbito de la búsqueda (ej., proyecto completo, módulo, directorio, archivos seleccionados, ámbito personalizado).
* **Tipo de archivo:** Restringe la búsqueda a tipos de archivo específicos (Java, Kotlin, XML, etc.).
* **Distinguir mayúsculas y minúsculas:** Alternador estándar de sensibilidad a mayúsculas.
* **Coincidir mayúsculas/minúsculas/palabras completas:** Aplicable para el texto dentro de la plantilla.
* **Coincidir saltos de línea:** Importante para patrones multilínea.
* **Guardar Plantilla:** Guarda tu plantilla de búsqueda actual para uso futuro.

### 4. Entendiendo el Diálogo de Reemplazo Estructural

El diálogo de Reemplazo Estructural añade un campo "Plantilla de Reemplazo" a la "Plantilla de Búsqueda" y "Variables" que defines para la búsqueda.

#### 4.1. Plantilla de Reemplazo

Aquí es donde defines cómo debe transformarse la estructura de código encontrada.

* **Variables de la Plantilla de Búsqueda:** Puedes usar las mismas variables definidas en tu "Plantilla de Búsqueda" dentro de la "Plantilla de Reemplazo". El contenido coincidente con la variable en la búsqueda se insertará en la plantilla de reemplazo.
* **Nuevo Código:** Puedes introducir nuevos elementos de código, reordenar los existentes o eliminar partes.
* **Ejemplo:**
    * **Plantilla de Búsqueda:** `System.out.println($arg$);`
    * **Plantilla de Reemplazo:** `LOGGER.info($arg$);`
    * Esto cambiaría `System.out.println("Hola");` a `LOGGER.info("Hola");`.

#### 4.2. Acortar Nombres Completamente Cualificados

Esta opción (a menudo habilitada automáticamente) intenta reemplazar nombres de clase completamente cualificados (ej., `java.util.ArrayList`) con sus nombres cortos (ej., `ArrayList`) y añadir las sentencias de importación necesarias. Esto es crucial para mantener el código legible.

#### 4.3. Formato

IntelliJ IDEA usualmente reformateará el código reemplazado de acuerdo con la configuración de estilo de código de tu proyecto, lo cual es muy deseable.

### 5. Ejemplos Prácticos

Ilustremos con algunos escenarios comunes.

#### Ejemplo 1: Reemplazar `System.out.println` con un Logger

**Objetivo:** Cambiar todos los `System.out.println("mensaje");` por `LOGGER.info("mensaje");` (asumiendo que `LOGGER` es un campo static final).

1.  **Abrir Reemplazo Estructural:** `Editar -> Buscar -> Reemplazar Estructuralmente...`
2.  **Plantilla de Búsqueda:**
    ```java
    System.out.println($arg$);
    ```
3.  **Variables:** Haz clic en "Editar variables" o ve a la pestaña "Variables".
    * Selecciona `$arg$`.
    * **Recuento:** `[1, 1]` (un argumento).
    * **Tipo (regexp):** `java.lang.String` (si solo quieres reemplazar literales de cadena, de lo contrario déjalo vacío para cualquier tipo).
4.  **Plantilla de Reemplazo:**
    ```java
    LOGGER.info($arg$);
    ```
5.  **Ejecutar:** Haz clic en "Buscar" para previsualizar los cambios, luego "Reemplazar Todo" si estás satisfecho.

#### Ejemplo 2: Intercambiando Parámetros de Método

**Objetivo:** Cambiar `algúnMétodo(paramA, paramB)` a `algúnMétodo(paramB, paramA)`.

1.  **Plantilla de Búsqueda:**
    ```java
    algúnMétodo($paramA$, $paramB$);
    ```
2.  **Variables:**
    * `$paramA$`: `Recuento: [1,1]`, `Tipo (regexp): .*` (cualquier tipo)
    * `$paramB$`: `Recuento: [1,1]`, `Tipo (regexp): .*` (cualquier tipo)
3.  **Plantilla de Reemplazo:**
    ```java
    algúnMétodo($paramB$, $paramA$);
    ```

#### Ejemplo 3: Encapsulando un Campo (Caso Simple)

**Objetivo:** Si tienes campos públicos como `public String nombre;` y quieres reemplazar el acceso directo `obj.nombre` con `obj.getNombre()`. (Este es un ejemplo simplificado; a menudo usarías refactorizaciones dedicadas para encapsulación).

1.  **Plantilla de Búsqueda:**
    ```java
    $objeto$.$nombreCampo$;
    ```
2.  **Variables:**
    * `$objeto$`: `Recuento: [1,1]`, `Tipo (regexp): .*`
    * `$nombreCampo$`: `Recuento: [1,1]`, `Texto (regexp): nombre` (apuntar específicamente al campo `nombre`).
3.  **Plantilla de Reemplazo:**
    ```java
    $objeto$.get$nombreCampo$();
    ```
    * **Nota:** Podrías necesitar ajustar las mayúsculas si `get$nombreCampo$` no capitaliza automáticamente `nombre` a `Nombre`. Para esto, podrías usar un script Groovy en `$nombreCampo$` dentro de la plantilla de reemplazo, pero se vuelve más complejo. Un enfoque más simple para este caso específico son a menudo dos SSRs o una refactorización dedicada. Para `get$nombreCampo$()`, el IDE usualmente maneja la capitalización para patrones de getters comunes.

#### Ejemplo 4: Encontrando Bloques `catch` Vacíos

**Objetivo:** Encontrar todos los bloques `catch` que están vacíos (o solo contienen comentarios/espacios en blanco).

1.  **Plantilla de Búsqueda:**
    ```java
    try {
        $sentencias$;
    } catch ($tipoExcepción$ $variableExcepción$) {
        $cuerpoVacío$;
    }
    ```
2.  **Variables:**
    * `$sentencias$`: `Recuento: [0, N]` (cero o más sentencias en el bloque try)
    * `$tipoExcepción$`: `Recuento: [1,1]`
    * `$variableExcepción$`: `Recuento: [1,1]`
    * `$cuerpoVacío$`: `Recuento: [0, 0]` (esta es la clave para un cuerpo vacío)

#### Ejemplo 5: Usando Script Groovy para Condiciones Avanzadas

**Objetivo:** Encontrar sentencias `if` donde la condición es una constante `true`.

1.  **Plantilla de Búsqueda:**
    ```java
    if ($condición$) {
        $ramaThen$;
    }
    ```
2.  **Variables:**
    * `$condición$`: `Recuento: [1,1]`
        * **Condición (script Groovy):** `_target.text == "true"` (esto comprueba el texto literal de la condición).
    * `$ramaThen$`: `Recuento: [0, N]`

### 6. Consejos y Mejores Prácticas

* **Comienza Simple:** Empieza con patrones básicos y añade complejidad gradualmente.
* **Usa `Buscar` Primero:** Siempre usa "Buscar" (Búsqueda Estructural) antes de "Reemplazar" para previsualizar las coincidencias y asegurarte de que tu patrón es correcto.
* **Prueba en un Ámbito Pequeño:** Antes de ejecutar un reemplazo a gran escala, prueba tu patrón en un conjunto pequeño y aislado de archivos.
* **Guarda Plantillas:** Guarda plantillas de uso frecuente o complejas para reutilizarlas fácilmente.
* **Aprovecha las Plantillas Existentes:** IntelliJ IDEA viene con muchas plantillas predefinidas de Búsqueda y Reemplazo Estructural. Puedes encontrarlas haciendo clic en el icono de la "lupa con un más" en el diálogo SSR y Examinar las plantillas existentes. Estos son excelentes recursos de aprendizaje.
* **Poder del Script Groovy:** Para coincidencias muy específicas o sensibles al contexto, los scripts Groovy son invaluables. Aprende lo básico sobre cómo acceder a elementos (`_target`, `_target.parent`, `_target.text`, `_target.type`, etc.) dentro del script.
* **Entiende los Tipos de Coincidencia:** Sé consciente de lo que tus variables están coincidiendo (ej., una sentencia, una expresión, un tipo, un nombre de variable). Esto influye en las restricciones que puedes aplicar.
* **Expresiones Regulares:** Un buen entendimiento de las expresiones regulares mejorará significativamente tu capacidad para definir restricciones de `Texto` y `Tipo`.
* **Depuración:** Si tu patrón no coincide como esperabas, simplifícalo. Elimina las restricciones una por una hasta que empiece a coincidir, luego reintrodúcelas para precisar el problema.
* **Copia de Seguridad de tu Código:** Antes de cualquier operación importante de reemplazo estructural en una base de código grande, asegúrate de tener una copia de seguridad o de estar trabajando dentro de un sistema de control de versiones donde puedas revertir los cambios fácilmente.

### 7. Limitaciones

* **Complejidad:** Los reemplazos muy complejos o altamente contextuales pueden ser difíciles o imposibles de expresar puramente con SSR. A veces, un plugin personalizado de IntelliJ IDEA o un script dedicado podrían ser más apropiados.
* **Rendimiento:** Los patrones extremadamente amplios o complejos ejecutados en una base de código muy grande pueden ser lentos.
* **Ambigüedad:** Ten cuidado con los patrones excesivamente generales, ya que podrían coincidir y modificar código que no tenías intención de tocar.

-----

Al dominar la Búsqueda y Reemplazo Estructural de IntelliJ IDEA, obtienes una herramienta poderosa para mantener la calidad del código, realizar refactorizaciones a gran escala y automatizar modificaciones de código tediosas. Es una función que realmente empodera a los desarrolladores para trabajar de manera más eficiente y consistente en sus proyectos.