---
audio: false
generated: true
lang: es
layout: post
title: Expresiones Regulares
translated: true
type: note
---

Las expresiones regulares, a menudo abreviadas como "regex" o "regexp", son una herramienta potente y versátil para la coincidencia de patrones en texto. Proporcionan una forma concisa y flexible de buscar, manipular y validar cadenas basándose en patrones definidos. Aunque la sintaxis puede parecer desalentadora al principio, dominar las regex puede mejorar significativamente tus capacidades de procesamiento de texto en varios lenguajes de programación, editores de texto y herramientas de línea de comandos.

Esta guía te llevará desde los conceptos básicos hasta conceptos más avanzados de las expresiones regulares.

**I. Los Fundamentos: Bloques de Construcción de Regex**

En esencia, una regex es una secuencia de caracteres que define un patrón de búsqueda. Estos caracteres pueden ser literales (que coinciden consigo mismos) o especiales (que tienen significados específicos).

**A. Caracteres Literales:**

La mayoría de los caracteres en una regex coinciden literalmente consigo mismos. Por ejemplo:

* `abc` coincidirá con la secuencia exacta "abc" en una cadena.
* `123` coincidirá con la secuencia exacta "123".
* `hello` coincidirá con la secuencia exacta "hello".

**B. Metacaracteres: Los Poderes Especiales**

Los metacaracteres son los bloques de construcción que le dan a regex su potencia. Tienen significados especiales y no coinciden literalmente consigo mismos. Aquí están los más comunes:

1.  **`.` (Punto):** Coincide con cualquier carácter único *excepto* un carácter de nueva línea (`\n` por defecto).
    * `a.c` coincidirá con "abc", "adc", "a1c", "a c", pero no con "ac" o "abbc".

2.  **`^` (Acento Circunflejo):**
    * **Dentro de un conjunto de caracteres (ver más abajo):** Niega el conjunto, coincidiendo con cualquier carácter *que no esté* en el conjunto.
    * **Fuera de un conjunto de caracteres:** Coincide con el principio de una cadena (o el principio de una línea en modo multilínea).
        * `^hello` coincidirá con "hello world" pero no con "say hello".

3.  **`$` (Signo de Dólar):** Coincide con el final de una cadena (o el final de una línea en modo multilínea).
    * `world$` coincidirá con "hello world" pero no con "world hello".

4.  **`*` (Asterisco):** Coincide con el carácter o grupo precedente cero o más veces.
    * `ab*c` coincidirá con "ac", "abc", "abbc", "abbbc", y así sucesivamente.

5.  **`+` (Signo Más):** Coincide con el carácter o grupo precedente una o más veces.
    * `ab+c` coincidirá con "abc", "abbc", "abbbc", pero no con "ac".

6.  **`?` (Signo de Interrogación):**
    * Coincide con el carácter o grupo precedente cero o una vez (haciéndolo opcional).
        * `ab?c` coincidirá con "ac" y "abc", pero no con "abbc".
    * Se utiliza como modificador de cuantificador para hacer una coincidencia no codiciosa (ver sección Cuantificadores).

7.  **`{}` (Llaves):** Especifica el número exacto o rango de ocurrencias del carácter o grupo precedente.
    * `a{3}` coincide exactamente con tres "a"s (ej., "aaa").
    * `a{2,4}` coincide entre dos y cuatro "a"s (ej., "aa", "aaa", "aaaa").
    * `a{2,}` coincide con dos o más "a"s (ej., "aa", "aaa", "aaaa", ...).

8.  **`[]` (Corchetes):** Define un conjunto de caracteres, coincidiendo con cualquier carácter único dentro de los corchetes.
    * `[abc]` coincidirá con "a", "b", o "c".
    * `[a-z]` coincidirá con cualquier letra minúscula de "a" a "z" (rango).
    * `[0-9]` coincidirá con cualquier dígito del "0" al "9".
    * `[A-Za-z0-9]` coincidirá con cualquier carácter alfanumérico.
    * `[^abc]` (con `^` al principio) coincidirá con cualquier carácter *excepto* "a", "b", o "c".

9.  **`\` (Barra Invertida):** Escapa el siguiente carácter, tratando un metacarácter como un carácter literal o introduciendo una secuencia de caracteres especiales.
    * `\.` coincidirá con un punto literal ".".
    * `\*` coincidirá con un asterisco literal "*".
    * `\d` coincide con cualquier dígito (equivalente a `[0-9]`).
    * `\D` coincide con cualquier carácter que no sea un dígito (equivalente a `[^0-9]`).
    * `\s` coincide con cualquier carácter de espacio en blanco (espacio, tabulación, nueva línea, etc.).
    * `\S` coincide con cualquier carácter que no sea un espacio en blanco.
    * `\w` coincide con cualquier carácter de palabra (alfanumérico y guión bajo, equivalente a `[a-zA-Z0-9_]`).
    * `\W` coincide con cualquier carácter que no sea de palabra (equivalente a `[^a-zA-Z0-9_]`).
    * `\b` coincide con un límite de palabra (la posición entre un carácter de palabra y un carácter que no es de palabra).
    * `\B` coincide con un límite que no es de palabra.
    * `\n` coincide con un carácter de nueva línea.
    * `\r` coincide con un carácter de retorno de carro.
    * `\t` coincide con un carácter de tabulación.

10. **`|` (Barra Vertical):** Actúa como un operador "O", coincidiendo con la expresión antes o después de la barra.
    * `cat|dog` coincidirá con "cat" o "dog".

11. **`()` (Paréntesis):**
    * **Agrupación:** Agrupa partes de una regex, permitiéndote aplicar cuantificadores o el operador OR a todo el grupo.
        * `(ab)+c` coincidirá con "abc", "ababc", "abababc", y así sucesivamente.
        * `(cat|dog) food` coincidirá con "cat food" o "dog food".
    * **Grupos de Captura:** Captura el texto que coincide con la expresión dentro de los paréntesis. Estos grupos capturados pueden ser referenciados más tarde (ej., para reemplazo o extracción).

**II. Cuantificadores: Controlando la Repetición**

Los cuantificadores especifican cuántas veces puede ocurrir un elemento precedente (carácter, grupo o conjunto de caracteres).

* `*`: Cero o más veces
* `+`: Una o más veces
* `?`: Cero o una vez
* `{n}`: Exactamente `n` veces
* `{n,}`: `n` o más veces
* `{n,m}`: Entre `n` y `m` veces (inclusive)

**Coincidencia Codiciosa vs. No Codiciosa:**

Por defecto, los cuantificadores son **codiciosos**, lo que significa que intentan coincidir con la mayor parte de la cadena posible. Puedes hacer un cuantificador **no codicioso** (o perezoso) añadiendo un `?` después de él. Los cuantificadores no codiciosos intentan coincidir con la cadena más corta posible.

* `a.*b` (codicioso) en "axxbxb" coincidirá con "axxbxb".
* `a.*?b` (no codicioso) en "axxbxb" coincidirá con "axb" y luego con "xb".

**III. Anclajes: Especificando Posición**

Los anclajes no coinciden con ningún carácter en sí mismos, sino que afirman una posición dentro de la cadena.

* `^`: Coincide con el principio de la cadena (o línea).
* `$`: Coincide con el final de la cadena (o línea).
* `\b`: Coincide con un límite de palabra.
* `\B`: Coincide con un límite que no es de palabra.

**IV. Clases de Caracteres: Conjuntos Predefinidos**

Las clases de caracteres proporcionan una forma abreviada para conjuntos de caracteres de uso común.

* `\d`: Coincide con cualquier dígito (0-9).
* `\D`: Coincide con cualquier carácter que no sea un dígito.
* `\s`: Coincide con cualquier carácter de espacio en blanco (espacio, tabulación, nueva línea, retorno de carro, salto de página).
* `\S`: Coincide con cualquier carácter que no sea un espacio en blanco.
* `\w`: Coincide con cualquier carácter de palabra (alfanumérico y guión bajo: a-zA-Z0-9_).
* `\W`: Coincide con cualquier carácter que no sea de palabra.

**V. Agrupación y Captura**

Los paréntesis `()` sirven para dos propósitos principales:

* **Agrupación:** Te permite aplicar cuantificadores o el operador OR a una secuencia de caracteres.
* **Captura:** Crea un grupo de captura, que almacena la porción de la cadena que coincidió con la expresión dentro de los paréntesis. Estos grupos capturados pueden ser accedidos y utilizados para retroreferencias o reemplazos.

**Retroreferencias:**

Puedes hacer referencia a grupos capturados previamente dentro de la misma regex usando `\1`, `\2`, `\3`, y así sucesivamente, donde el número corresponde al orden del paréntesis de apertura del grupo de captura.

* `(.)\1` coincidirá con cualquier carácter seguido del mismo carácter (ej., "aa", "bb", "11").
* `(\w+) \1` coincidirá con una palabra seguida de un espacio y luego la misma palabra (ej., "hello hello").

**Grupos Sin Captura:**

Si necesitas agrupar partes de una regex sin crear un grupo de captura, puedes usar `(?:...)`. Esto es útil por razones de claridad o rendimiento.

* `(?:ab)+c` coincidirá con "abc", "ababc", etc., pero no capturará "ab".

**VI. Lookarounds: Aserciones Sin Consumo**

Los lookarounds son aserciones de ancho cero que verifican un patrón antes o después de la posición actual en la cadena sin incluir la parte coincidente del lookaround en la coincidencia general.

* **Lookahead Positivo `(?=...)`:** Afirma que el patrón dentro de los paréntesis debe seguir a la posición actual.
    * `\w+(?=:)` coincidirá con cualquier palabra seguida de dos puntos, pero los dos puntos mismos no serán parte de la coincidencia (ej., en "name:", coincidirá con "name").

* **Lookahead Negativo `(?!...)`:** Afirma que el patrón dentro de los paréntesis *no* debe seguir a la posición actual.
    * `\w+(?!:)` coincidirá con cualquier palabra no seguida de dos puntos (ej., en "name value", coincidirá con "name" y "value").

* **Lookbehind Positivo `(?<=...)`:** Afirma que el patrón dentro de los paréntesis debe preceder a la posición actual. El patrón dentro del lookbehind debe tener un ancho fijo (sin cuantificadores variables como `*` o `+`).
    * `(?<=\$)\d+` coincidirá con uno o más dígitos que están precedidos por un signo de dólar, pero el signo de dólar mismo no será parte de la coincidencia (ej., en "$100", coincidirá con "100").

* **Lookbehind Negativo `(?<!...)`:** Afirma que el patrón dentro de los paréntesis *no* debe preceder a la posición actual. El patrón dentro del lookbehind debe tener un ancho fijo.
    * `(?<!\$)\d+` coincidirá con uno o más dígitos que no están precedidos por un signo de dólar (ej., en "100$", coincidirá con "100").

**VII. Banderas (Modificadores): Controlando el Comportamiento de Regex**

Las banderas (o modificadores) se utilizan para alterar el comportamiento del motor de expresiones regulares. Generalmente se especifican al principio o al final del patrón de regex, dependiendo de la implementación. Las banderas comunes incluyen:

* **`i` (Insensible a Mayúsculas y Minúsculas):** Hace que la coincidencia sea insensible a mayúsculas y minúsculas. `[a-z]` coincidirá con letras minúsculas y mayúsculas.
* **`g` (Global):** Encuentra todas las coincidencias en la cadena, no solo la primera.
* **`m` (Multilínea):** Hace que `^` y `$` coincidan con el principio y final de cada línea (delimitada por `\n` o `\r`) en lugar de solo con el principio y final de toda la cadena.
* **`s` (Dotall/Una sola línea):** Hace que el metacarácter `.` coincida con cualquier carácter, incluyendo caracteres de nueva línea.
* **`u` (Unicode):** Habilita soporte completo de Unicode para clases de caracteres y otras características.
* **`x` (Extendido/Verboso):** Te permite escribir regex más legibles ignorando los espacios en blanco y los comentarios dentro del patrón (útil para regex complejos).

**VIII. Aplicaciones Prácticas de Regex**

Las regex se utilizan extensamente en varios dominios:

* **Editores de Texto (ej., Notepad++, Sublime Text, VS Code):** Buscar y reemplazar texto basado en patrones.
* **Lenguajes de Programación (ej., Python, JavaScript, Java, C#):**
    * Validar entrada del usuario (ej., direcciones de email, números de teléfono, URLs).
    * Extraer información específica de texto (ej., fechas, números, etiquetas).
    * Reemplazar partes de una cadena basándose en un patrón.
    * Analizar archivos de registro u otros datos de texto estructurados.
* **Herramientas de Línea de Comandos (ej., `grep`, `sed`, `awk`):** Buscar y manipular archivos de texto.
* **Desarrollo Web:** Validación de formularios, enrutamiento de URLs, procesamiento de contenido.
* **Ciencia de Datos:** Limpieza de datos, extracción de datos, reconocimiento de patrones.
* **Seguridad:** Detección de intrusiones, análisis de registros.

**IX. Regex en Diferentes Lenguajes de Programación**

La mayoría de los lenguajes de programación modernos tienen soporte incorporado para expresiones regulares, aunque la sintaxis específica y las características pueden variar ligeramente. Normalmente encontrarás la funcionalidad de regex en bibliotecas o módulos estándar.

* **Python:** El módulo `re`.
* **JavaScript:** El objeto incorporado `RegExp` y métodos de cadena como `match()`, `replace()`, `search()`, `split()`.
* **Java:** El paquete `java.util.regex`.
* **C# (.NET):** El espacio de nombres `System.Text.RegularExpressions`.
* **PHP:** Funciones como `preg_match()`, `preg_replace()`, `preg_match_all()`.

**X. Consejos para Escribir Regex Efectivos**

* **Comienza Simple:** Empieza con un patrón básico y añade complejidad gradualmente.
* **Prueba Frecuentemente:** Usa probadores de regex en línea o las herramientas de regex de tu lenguaje de programación para probar tus patrones con datos de ejemplo.
* **Sé Específico:** Evita patrones excesivamente amplios que puedan coincidir con texto no deseado.
* **Usa Clases de Caracteres y Cuantificadores con Cuidado:** Son potentes pero también pueden llevar a comportamientos inesperados si no se usan correctamente.
* **Comprende la Coincidencia Codiciosa vs. No Codiciosa:** Elige el comportamiento apropiado para tus necesidades.
* **Usa la Agrupación y Captura con Criterio:** Captura solo lo que necesites. Usa grupos sin captura cuando no se requiera capturar.
* **Documenta Tu Regex:** Para patrones complejos, añade comentarios (especialmente cuando uses la bandera `x`) para explicar su propósito.
* **Considera Casos Extremos:** Piensa en diferentes variaciones del texto de entrada y asegúrate de que tu regex las maneja correctamente.
* **Divide Problemas Complejos:** Si tienes una tarea de coincidencia muy compleja, considera dividirla en múltiples patrones de regex más simples.

**XI. Recursos de Aprendizaje**

* **Probadores de Regex en Línea:** regex101.com, regexr.com, regextester.com
* **Documentación Específica del Lenguaje:** Consulta la documentación de regex para tu lenguaje de programación elegido.
* **Tutoriales y Cursos en Línea:** Plataformas como Coursera, Udemy y YouTube ofrecen cursos completos de regex.
* **Libros:** "Mastering Regular Expressions" de Jeffrey Friedl es un recurso muy recomendado.

**Conclusión**

Las expresiones regulares son una herramienta indispensable para cualquier persona que trabaje con datos de texto. Aunque la curva de aprendizaje inicial pueda parecer empinada, la capacidad de buscar, manipular y validar texto de manera eficiente basándose en patrones complejos es una habilidad valiosa. Al comprender los conceptos fundamentales, los metacaracteres, los cuantificadores y otras características de regex, puedes mejorar significativamente tu productividad y capacidades de resolución de problemas en una amplia gama de aplicaciones. La práctica es clave para dominar las regex, así que no dudes en experimentar y explorar diferentes patrones para varias tareas de procesamiento de texto.