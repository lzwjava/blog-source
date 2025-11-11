---
audio: false
generated: true
lang: es
layout: post
title: Configuración de Checkstyle
translated: true
type: note
---

Este es un archivo de configuración de Checkstyle escrito en XML, diseñado para hacer cumplir estándares de codificación y mejores prácticas para código Java basado en las convenciones de codificación de Sun, la Especificación del Lenguaje Java, las guías de Javadoc y algunas mejores prácticas adicionales. Checkstyle es una herramienta de análisis de código estático que verifica el código fuente Java para asegurar el cumplimiento de un conjunto de reglas definidas. A continuación, explicaré la estructura y los componentes clave de este archivo de configuración.

---

### **Descripción General**
- **Propósito**: El archivo define reglas para verificar archivos Java, properties y XML en busca de violaciones de estándares de codificación, como formato, convenciones de nomenclatura, requisitos de Javadoc y estructura del código.
- **Estructura**: La configuración está organizada jerárquicamente usando elementos `<module>`, comenzando con un módulo raíz `Checker`, que contiene otros módulos para verificaciones o filtros específicos.
- **Estándares**: Se alinea con:
  - Especificación del Lenguaje Java (Java SE 11)
  - Convenciones de Código Sun
  - Guías de Javadoc
  - Documentación de la API de JDK
  - Mejores prácticas generales
- **Características Clave**:
  - Gravedad configurable (establecida en `error`).
  - Admite extensiones de archivo: `.java`, `.properties`, `.xml`.
  - Permite la supresión de verificaciones específicas mediante archivos de supresión o anotaciones `@SuppressWarnings`.

---

### **Módulo Raíz: `<module name="Checker">`**
El módulo `Checker` es el módulo de nivel superior que orquesta todas las verificaciones y filtros.

- **Propiedades**:
  - `severity="error"`: Trata todas las violaciones como errores (otras opciones incluyen `warning` o `info`).
  - `fileExtensions="java, properties, xml"`: Aplica las verificaciones a archivos `.java`, `.properties` y `.xml`.

- **Submódulos**:
  - **Filtros de Archivo**:
    - `BeforeExecutionExclusionFileFilter`: Excluye archivos `module-info.java` de las verificaciones (usando la expresión regular `module\-info\.java$`).
  - **Filtros de Supresión**:
    - `SuppressionFilter`: Carga reglas de supresión desde un archivo (por defecto: `checkstyle-suppressions.xml`). Si el archivo falta, es opcional (`optional="true"`).
    - `SuppressWarningsFilter`: Habilita la supresión de verificaciones específicas usando anotaciones `@SuppressWarnings("checkstyle:...")` en el código.
  - **Verificaciones Misceláneas**:
    - `JavadocPackage`: Asegura que cada paquete tenga un archivo `package-info.java` con Javadoc.
    - `NewlineAtEndOfFile`: Verifica que los archivos terminen con un carácter de nueva línea.
    - `Translation`: Verifica que los archivos properties (ej., para internacionalización) contengan las mismas claves en todas las traducciones.
  - **Verificaciones de Tamaño**:
    - `FileLength`: Verifica la longitud total de un archivo (se aplican límites por defecto a menos que se sobrescriban).
    - `LineLength`: Asegura que las líneas en archivos `.java` no excedan una longitud por defecto (típicamente 80 o 120 caracteres, configurable).
  - **Verificaciones de Espacios en Blanco**:
    - `FileTabCharacter`: Prohíbe caracteres de tabulación en archivos fuente (impone el uso de espacios para la sangría).
    - `RegexpSingleline`: Detecta espacios en blanco al final de la línea (líneas que terminan con `\s+$`) y los reporta con el mensaje "Line has trailing spaces."
  - **Verificación de Cabecera** (Comentada):
    - `Header`: Si se descomenta, impondría una cabecera de archivo específica (ej., un aviso de copyright) desde un archivo especificado en `checkstyle.header.file` para archivos `.java`.

---

### **Submódulo: `<module name="TreeWalker">`**
El módulo `TreeWalker` procesa el árbol de sintaxis abstracta (AST) del código fuente Java para realizar verificaciones detalladas. Contiene una variedad de submódulos agrupados por categoría.

#### **Verificaciones de Javadoc**
Estas hacen cumplir comentarios Javadoc apropiados para clases, métodos y variables:
- `InvalidJavadocPosition`: Asegura que los comentarios Javadoc estén colocados correctamente (ej., antes de una clase o método, no en otro lugar).
- `JavadocMethod`: Verifica que los métodos tengan comentarios Javadoc apropiados, incluyendo parámetros, tipos de retorno y excepciones.
- `JavadocType`: Asegura que clases, interfaces y enums tengan comentarios Javadoc.
- `JavadocVariable`: Requiere Javadoc para campos públicos/protegidos.
- `JavadocStyle`: Impone reglas estilísticas para Javadoc (ej., etiquetas HTML apropiadas, sin comentarios malformados).
- `MissingJavadocMethod`: Señala métodos a los que les faltan comentarios Javadoc.

#### **Convenciones de Nomenclatura**
Estas aseguran que los identificadores (variables, métodos, clases, etc.) sigan las convenciones de nomenclatura:
- `ConstantName`: Las constantes (ej., `static final`) deben seguir un patrón de nomenclatura (típicamente `MAYÚSCULAS_CON_GUION_BAJO`).
- `LocalFinalVariableName`: Las variables locales `final` deben seguir un patrón de nomenclatura (ej., `camelCase`).
- `LocalVariableName`: Las variables locales deben seguir un patrón de nomenclatura (ej., `camelCase`).
- `MemberName`: Los campos de instancia deben seguir un patrón de nomenclatura (ej., `camelCase`).
- `MethodName`: Los métodos deben seguir un patrón de nomenclatura (ej., `camelCase`).
- `PackageName`: Los paquetes deben seguir un patrón de nomenclatura (ej., minúsculas con puntos, como `com.example`).
- `ParameterName`: Los parámetros de método deben seguir un patrón de nomenclatura (ej., `camelCase`).
- `StaticVariableName`: Los campos estáticos (no finales) deben seguir un patrón de nomenclatura.
- `TypeName`: Los nombres de clase/interfaz/enum deben seguir un patrón de nomenclatura (ej., `UpperCamelCase`).

#### **Verificaciones de Import**
Estas regulan el uso de sentencias `import`:
- `AvoidStarImport`: Prohíbe imports comodín (ej., `import java.util.*`).
- `IllegalImport`: Bloquea imports de paquetes restringidos (por defecto `sun.*`).
- `RedundantImport`: Señala imports duplicados o innecesarios.
- `UnusedImports`: Detecta imports no utilizados (ignora imports relacionados con Javadoc con `processJavadoc="false"`).

#### **Verificaciones de Tamaño**
Estas limitan el tamaño de métodos y parámetros:
- `MethodLength`: Asegura que los métodos no excedan un número máximo de líneas (por defecto típicamente 150).
- `ParameterNumber`: Limita el número de parámetros en un método (por defecto típicamente 7).

#### **Verificaciones de Espacios en Blanco**
Estas hacen cumplir el uso consistente de espacios en blanco en el código:
- `EmptyForIteratorPad`: Verifica el relleno en iteradores vacíos de bucle `for` (ej., `for (int i = 0; ; i++)`).
- `GenericWhitespace`: Asegura el espaciado correcto alrededor de tipos genéricos (ej., `List<String>`).
- `MethodParamPad`: Verifica el espaciado antes de las listas de parámetros de método.
- `NoWhitespaceAfter`: Prohíbe el espacio en blanco después de ciertos tokens (ej., `++` o arrays).
- `NoWhitespaceBefore`: Prohíbe el espacio en blanco antes de ciertos tokens (ej., punto y coma).
- `OperatorWrap`: Asegura que los operadores (ej., `+`, `=`) estén en la línea correcta.
- `ParenPad`: Verifica el espaciado dentro de paréntesis (ej., `( x )` vs. `(x)`).
- `TypecastParenPad`: Asegura el espaciado correcto en conversiones de tipo.
- `WhitespaceAfter`: Requiere espacio en blanco después de ciertos tokens (ej., comas, punto y coma).
- `WhitespaceAround`: Asegura espacio en blanco alrededor de operadores y palabras clave (ej., `if (x == y)`).

#### **Verificaciones de Modificador**
Estas regulan el uso de modificadores de Java:
- `ModifierOrder`: Asegura que los modificadores estén en el orden correcto (ej., `public static final`, según JLS).
- `RedundantModifier`: Señala modificadores innecesarios (ej., `final` en una clase `final`).

#### **Verificaciones de Bloque**
Estas hacen cumplir el uso apropiado de bloques de código (`{}`):
- `AvoidNestedBlocks`: Prohíbe bloques anidados innecesarios (ej., `{ { ... } }`).
- `EmptyBlock`: Señala bloques vacíos (ej., `{}`) a menos que sean intencionados.
- `LeftCurly`: Asegura que las llaves de apertura (`{`) se coloquen correctamente (ej., al final de una línea).
- `NeedBraces`: Requiere llaves para bloques de una sola sentencia (ej., `if (x) y();` debe ser `if (x) { y(); }`).
- `RightCurly`: Asegura que las llaves de cierre (`}`) se coloquen correctamente (ej., en una nueva línea o en la misma línea, dependiendo del estilo).

#### **Verificaciones de Problemas de Codificación**
Estas identifican problemas comunes de codificación:
- `EmptyStatement`: Señala sentencias vacías (ej., `;;`).
- `EqualsHashCode`: Asegura que si se anula `equals()`, también se anule `hashCode()`.
- `HiddenField`: Detecta campos ocultados por variables locales o parámetros.
- `IllegalInstantiation`: Prohíbe la instanciación de ciertas clases (ej., clases `java.lang` como `String`).
- `InnerAssignment`: No permite asignaciones dentro de expresiones (ej., `if (x = y)`).
- `MagicNumber`: Señala literales numéricos codificados (ej., `42`) a menos que estén en contextos específicos.
- `MissingSwitchDefault`: Requiere un caso `default` en sentencias `switch`.
- `MultipleVariableDeclarations`: Prohíbe declarar múltiples variables en una sola línea (ej., `int x, y;`).
- `SimplifyBooleanExpression`: Señala expresiones booleanas excesivamente complejas (ej., `if (x == true)`).
- `SimplifyBooleanReturn`: Simplifica sentencias de retorno booleanas (ej., `if (x) return true; else return false;`).

#### **Verificaciones de Diseño de Clase**
Estas hacen cumplir buenas prácticas de diseño de clases:
- `DesignForExtension`: Asegura que las clases no finales tengan métodos protegidos o abstractos para extensibilidad.
- `FinalClass`: Señala clases con solo constructores privados como candidatas para `final`.
- `HideUtilityClassConstructor`: Asegura que las clases de utilidad (con solo miembros estáticos) tengan constructores privados.
- `InterfaceIsType`: Prohíbe interfaces usadas únicamente como interfaces marcadoras (sin métodos).
- `VisibilityModifier`: Hace cumplir la visibilidad apropiada para los campos (ej., prefiere campos privados con getters/setters).

#### **Verificaciones Misceláneas**
- `ArrayTypeStyle`: Hace cumplir un estilo de declaración de array consistente (ej., `int[]` vs. `int []`).
- `FinalParameters`: Requiere que los parámetros de método sean `final` donde sea posible.
- `TodoComment`: Señala comentarios `TODO` en el código (útil para rastrear trabajo incompleto).
- `UpperEll`: Asegura que se use la letra `L` para literales long (ej., `100L` en lugar de `100l`).

#### **Filtros de Supresión (Dentro de TreeWalker)**
- `SuppressionXpathFilter`: Permite la supresión de verificaciones usando expresiones XPath definidas en un archivo (por defecto: `checkstyle-xpath-suppressions.xml`, opcional).
- `SuppressWarningsHolder`: Admite anotaciones `@SuppressWarnings("checkstyle:...")` para suprimir verificaciones específicas dentro del AST.

---

### **Puntos Clave**
- **Configurabilidad**: La mayoría de los módulos tienen configuraciones por defecto pero pueden personalizarse mediante propiedades (ej., `LineLength` puede establecer una longitud `max` específica).
- **Supresión**: La configuración admite una supresión flexible de verificaciones mediante archivos externos (`checkstyle-suppressions.xml`, `checkstyle-xpath-suppressions.xml`) o anotaciones.
- **Extensibilidad**: Se pueden añadir verificaciones adicionales, y las existentes pueden deshabilitarse comentándolas o eliminándolas.
- **Documentación**: La configuración hace referencia a la documentación de Checkstyle (ej., `https://checkstyle.org`) para detalles sobre cada módulo.
- **Verificación de Cabecera**: El módulo `Header` está comentado, por lo que no está activo a menos que se descomente y configure con un archivo de cabecera.

---

### **Cómo Se Usa**
1. **Integración**: Este archivo se usa típicamente con una herramienta de construcción como Maven, Gradle, o un plugin de IDE para ejecutar Checkstyle durante el proceso de construcción o en el desarrollo.
2. **Reporte de Violaciones**: Cuando el código viola una regla (ej., una línea excede la longitud máxima), Checkstyle lo reporta como un error (debido a `severity="error"`).
3. **Supresión**: Los desarrolladores pueden suprimir violaciones específicas usando `@SuppressWarnings("checkstyle:<nombre-de-verificación>")` o definiendo reglas en archivos de supresión.
4. **Personalización**: Propiedades como `basedir`, `checkstyle.header.file`, o rutas de archivos de supresión pueden establecerse externamente (ej., mediante configuraciones de herramientas de construcción).

---

### **Ejemplos de Violaciones**
- **JavadocMethod**: Un método público sin Javadoc activará un error.
- **LineLength**: Una línea en un archivo `.java` que exceda el máximo por defecto (ej., 80 caracteres) será marcada.
- **AvoidStarImport**: Usar `import java.util.*` causará un error.
- **MagicNumber**: Escribir `int x = 42;` sin una constante nombrada será marcado.

---

Si necesitas una explicación más profunda de un módulo específico, ejemplos de violaciones o orientación sobre cómo personalizar esta configuración, ¡avísame!