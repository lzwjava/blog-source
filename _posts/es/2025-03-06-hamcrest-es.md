---
audio: false
generated: true
lang: es
layout: post
title: Usando Hamcrest Matchers en Pruebas de Java
translated: true
---

Déjame guiarte en el uso de los matchers de Hamcrest en Java. Hamcrest es un marco que proporciona un conjunto de objetos matchers para escribir afirmaciones más legibles en las pruebas.

1. Primero, agrega la dependencia de Hamcrest a tu proyecto:

Para Maven, agrega esto a tu `pom.xml`:
```xml
<dependency>
    <groupId>org.hamcrest</groupId>
    <artifactId>hamcrest</artifactId>
    <version>2.2</version>
    <scope>test</scope>
</dependency>
```

Para Gradle, agrega esto a tu `build.gradle`:
```groovy
testImplementation 'org.hamcrest:hamcrest:2.2'
```

2. Aquí tienes un ejemplo básico de usar Hamcrest con JUnit:

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;  // Importa matchers comunes

import org.junit.Test;

public class ExampleTest {
    @Test
    public void testExamples() {
        // Igualdad básica
        assertThat(5, is(5));

        // Coincidencia de cadena
        String text = "Hello World";
        assertThat(text, containsString("World"));
        assertThat(text, startsWith("Hello"));

        // Coincidencia de colección
        List<String> items = Arrays.asList("apple", "banana", "orange");
        assertThat(items, hasItem("banana"));
        assertThat(items, hasSize(3));

        // Comparaciones numéricas
        assertThat(10, greaterThan(5));
        assertThat(3.14, closeTo(3.0, 0.2));
    }
}
```

3. Matchers comunes de Hamcrest:
- `is()`: Prueba la igualdad
- `equalTo()`: Prueba la igualdad de objetos
- `containsString()`: Verifica si la cadena contiene una subcadena
- `startsWith()`/ `endsWith()`: Verificación de prefijo/sufijo de cadena
- `greaterThan()`/ `lessThan()`: Comparaciones numéricas
- `hasItem()`: Verifica si la colección contiene un elemento
- `hasSize()`: Verifica el tamaño de la colección
- `closeTo()`: Verifica si el número está dentro de un rango
- `not()`: Niega cualquier matcher
- `allOf()`: Combina múltiples matchers (Y)
- `anyOf()`: Combina múltiples matchers (O)

4. Ejemplo de Matcher Personalizado:
```java
import org.hamcrest.BaseMatcher;
import org.hamcrest.Description;
import org.hamcrest.Matcher;

public class CustomMatchers {
    public static Matcher<String> isPalindrome() {
        return new BaseMatcher<String>() {
            @Override
            public boolean matches(Object item) {
                String str = (String) item;
                String reversed = new StringBuilder(str).reverse().toString();
                return str.equals(reversed);
            }

            @Override
            public void describeTo(Description description) {
                description.appendText("un palíndromo");
            }
        };
    }
}

// Uso:
@Test
public void testPalindrome() {
    assertThat("racecar", isPalindrome());
}
```

5. Combinando Matchers:
```java
@Test
public void testCombined() {
    List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
    assertThat(numbers, allOf(
        hasSize(5),
        hasItem(greaterThan(4)),
        everyItem(lessThan(10))
    ));
}
```

Beneficios Clave:
- Afirmaciones de prueba más legibles
- Mejores mensajes de fallo
- Condiciones de coincidencia flexibles
- Extensible con matchers personalizados

Consejos:
- Usa `import static` para hacer el código más conciso
- Combina matchers para condiciones complejas
- Consulta la documentación de Hamcrest para el conjunto completo de matchers
- Hamcrest funciona bien con JUnit, TestNG y otros marcos de prueba

¿Te gustaría que profundice en algún matcher específico o que muestre más ejemplos?