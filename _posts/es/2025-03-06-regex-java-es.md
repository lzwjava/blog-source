---
audio: false
generated: true
lang: es
layout: post
title: Expresiones Regulares en Java
translated: true
---

# Cómo usar `java.util.regex` en Java

El paquete `java.util.regex` en Java proporciona herramientas para trabajar con expresiones regulares (regex), que son patrones utilizados para coincidir y manipular texto. Esta guía te guiará a través de los conceptos básicos del uso de este paquete, centrándose en las dos clases principales: `Pattern` y `Matcher`. También cubriré casos de uso comunes con ejemplos para ayudarte a comenzar.

## Descripción general de `java.util.regex`

El paquete `java.util.regex` incluye:

- **`Pattern`**: Representa una expresión regular compilada. Se crea a partir de una cadena de regex.
- **`Matcher`**: Aplica el patrón a una cadena de entrada específica y realiza operaciones de coincidencia.

Además, la clase `String` de Java ofrece métodos basados en regex para tareas más simples.

## Pasos básicos para usar `java.util.regex`

Para usar expresiones regulares en Java, sigue estos pasos:

1. **Compilar un patrón**: Convierte tu cadena de regex en un objeto `Pattern`.
2. **Crear un `Matcher`**: Usa el patrón para crear un `Matcher` para tu texto de entrada.
3. **Realizar operaciones**: Usa el `Matcher` para verificar coincidencias, encontrar patrones o manipular texto.

Aquí está cómo funciona en la práctica.

## Ejemplo 1: Validar una dirección de correo electrónico

Vamos a crear un validador de correo electrónico simple usando un patrón de regex básico: `".+@.+\\..+"`. Este patrón coincide con cadenas que tienen al menos un carácter antes y después de un símbolo `@`, seguido de un punto y más caracteres (por ejemplo, `example@test.com`).

```java
import java.util.regex.*;

public class EmailValidator {
    public static boolean isValidEmail(String email) {
        // Define el patrón de regex
        String regex = ".+@.+\\..+";
        // Compila el patrón
        Pattern pattern = Pattern.compile(regex);
        // Crea un `Matcher` para la cadena de entrada
        Matcher matcher = pattern.matcher(email);
        // Verifica si toda la cadena coincide con el patrón
        return matcher.matches();
    }

    public static void main(String[] args) {
        String email = "example@test.com";
        if (isValidEmail(email)) {
            System.out.println("Correo electrónico válido");
        } else {
            System.out.println("Correo electrónico inválido");
        }
    }
}
```

### Explicación
- **`Pattern.compile(regex)`**: Compila la cadena de regex en un objeto `Pattern`.
- **`pattern.matcher(email)`**: Crea un `Matcher` para la cadena de entrada `email`.
- **`matcher.matches()`**: Devuelve `true` si toda la cadena coincide con el patrón, `false` en caso contrario.

**Salida**: `Correo electrónico válido`

Nota: Este es un patrón de correo electrónico simplificado. La validación real de correos electrónicos requiere un regex más complejo (por ejemplo, según RFC 5322), pero esto sirve como punto de partida.

## Ejemplo 2: Encontrar todos los hashtags en una cadena

Supongamos que quieres extraer todos los hashtags (por ejemplo, `#java`) de un tuit. Usa el regex `"#\\w+"`, donde `#` coincide con el símbolo de hashtag literal y `\\w+` coincide con uno o más caracteres de palabra (letras, dígitos o guiones bajos).

```java
import java.util.regex.*;

public class HashtagExtractor {
    public static void main(String[] args) {
        String tweet = "This is a #sample tweet with #multiple hashtags like #java";
        String regex = "#\\w+";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(tweet);

        // Encuentra todas las coincidencias
        while (matcher.find()) {
            System.out.println(matcher.group());
        }
    }
}
```

### Explicación
- **`matcher.find()`**: Se mueve a la siguiente coincidencia en la cadena de entrada y devuelve `true` si se encuentra una coincidencia.
- **`matcher.group()`**: Devuelve el texto coincidente para la coincidencia actual.

**Salida**:
```
#sample
#multiple
#java
```

## Ejemplo 3: Reemplazar texto con regex

Para reemplazar todas las ocurrencias de una palabra (por ejemplo, censurar "badword" con asteriscos), puedes usar el método `String.replaceAll()`, que usa regex internamente.

```java
public class TextCensor {
    public static void main(String[] args) {
        String text = "This is a badword example with badword repeated.";
        String censored = text.replaceAll("badword", "*******");
        System.out.println(censored);
    }
}
```

**Salida**: `This is a ******* example with ******* repeated.`

Para reemplazos más complejos, usa `Matcher`:

```java
import java.util.regex.*;

public class ComplexReplacement {
    public static void main(String[] args) {
        String text = "Contact: 123-456-7890";
        String regex = "\\d{3}-\\d{3}-\\d{4}"; // Coincide con números de teléfono
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(text);
        String result = matcher.replaceAll("XXX-XXX-XXXX");
        System.out.println(result);
    }
}
```

**Salida**: `Contact: XXX-XXX-XXXX`

## Ejemplo 4: Usar grupos para analizar datos estructurados

Los grupos de regex, definidos con paréntesis `()`, te permiten capturar partes de una coincidencia. Por ejemplo, para analizar un Número de Seguridad Social (SSN) como `123-45-6789`:

```java
import java.util.regex.*;

public class SSNParser {
    public static void main(String[] args) {
        String ssn = "123-45-6789";
        String regex = "(\\d{3})-(\\d{2})-(\\d{4})"; // Grupos para área, grupo, serie
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(ssn);

        if (matcher.matches()) {
            System.out.println("Número de área: " + matcher.group(1));
            System.out.println("Número de grupo: " + matcher.group(2));
            System.out.println("Número de serie: " + matcher.group(3));
        }
    }
}
```

### Explicación
- **`"(\\d{3})-(\\d{2})-(\\d{4})"`**: Define tres grupos:
  - Grupo 1: `\\d{3}` (tres dígitos)
  - Grupo 2: `\\d{2}` (dos dígitos)
  - Grupo 3: `\\d{4}` (cuatro dígitos)
- **`matcher.group(n)`**: Recupera el texto coincidente por el grupo `n` (índice basado en 1).

**Salida**:
```
Número de área: 123
Número de grupo: 45
Número de serie: 6789
```

También puedes usar **grupos con nombre** para mayor claridad:

```java
String regex = "(?<area>\\d{3})-(?<group>\\d{2})-(?<serial>\\d{4})";
Pattern pattern = Pattern.compile(regex);
Matcher matcher = pattern.matcher("123-45-6789");
if (matcher.matches()) {
    System.out.println("Área: " + matcher.group("area"));
    System.out.println("Grupo: " + matcher.group("group"));
    System.out.println("Serie: " + matcher.group("serial"));
}
```

## Características adicionales y consejos

### Indicadores
Modifica el comportamiento del patrón con indicadores en `Pattern.compile()`:
- **`Pattern.CASE_INSENSITIVE`**: Ignora el caso al coincidir.
  ```java
  Pattern pattern = Pattern.compile("hello", Pattern.CASE_INSENSITIVE);
  Matcher matcher = pattern.matcher("HELLO");
  System.out.println(matcher.matches()); // true
  ```

### Métodos de cadena
Para tareas simples, usa métodos de `String`:
- **`matches()`**: Verifica si toda la cadena coincide con un regex.
  ```java
  String text = "cat";
  System.out.println(text.matches("\\w{3}")); // true
  ```
- **`split()`**: Divide una cadena por un patrón de regex.
  ```java
  String data = "apple, banana, cherry";
  String[] fruits = data.split("\\s*,\\s*");
  // Salida: apple, banana, cherry
  ```

### Escapar caracteres especiales
Regex usa caracteres especiales como `.`, `*`, y `?`. Para coincidir con ellos literalmente, escápalos con `\\`:
- Coincidir con un punto: `"\\."`
- En cadenas de Java, escapa las barras invertidas: `"\\d"` para dígitos, `"\\\\"` para una barra invertida literal.

### Rendimiento
Compilar un patrón es costoso. Reutiliza objetos `Pattern` cuando sea posible:
```java
Pattern pattern = Pattern.compile("\\d+"); // Compila una vez
for (String input : new String[]{"123", "456"}) {
    Matcher matcher = pattern.matcher(input);
    if (matcher.matches()) {
        System.out.println("Número: " + input);
    }
}
```

### Manejo de errores
Los patrones de regex inválidos lanzan `PatternSyntaxException`. Mánajalo en el código de producción:
```java
try {
    Pattern pattern = Pattern.compile("["); // Regex inválido
} catch (PatternSyntaxException e) {
    System.err.println("Regex inválido: " + e.getMessage());
}
```

## Resumen

- **Compilar un patrón**: `Pattern.compile(regex)`
- **Crear un `Matcher`**: `pattern.matcher(input)`
- **Operaciones clave**:
  - `matches()`: Coincidencia de toda la cadena
  - `find()`: Encontrar la siguiente coincidencia
  - `group()`: Extraer texto coincidente
  - `replaceAll()`: Reemplazar coincidencias
- **Conveniencia**: Usa métodos de `String` para tareas simples.
- **Mejores prácticas**: Escapa caracteres especiales, reutiliza patrones y maneja excepciones.

Esto cubre los conceptos esenciales de `java.util.regex`. Para temas avanzados como lookaheads o clases de caracteres, consulta la [documentación de Java](https://docs.oracle.com/en/java/javase/17/docs/api/java.util.regex/package-summary.html) o experimenta con casos de uso específicos.