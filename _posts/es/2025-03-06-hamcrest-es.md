---
audio: false
generated: true
lang: es
layout: post
title: Uso de los Matchers de Hamcrest en Pruebas de Java
translated: true
type: note
---

Permíteme guiarte a través del uso de los matchers de Hamcrest en Java. Hamcrest es un framework que proporciona un conjunto de objetos matcher para escribir aserciones más legibles en las pruebas.

1. Primero, añade la dependencia de Hamcrest a tu proyecto:

Para Maven, añade esto a tu pom.xml:
```xml
<dependency>
    <groupId>org.hamcrest</groupId>
    <artifactId>hamcrest</artifactId>
    <version>2.2</version>
    <scope>test</scope>
</dependency>
```

Para Gradle, añade esto a tu build.gradle:
```groovy
testImplementation 'org.hamcrest:hamcrest:2.2'
```

2. Aquí tienes un ejemplo básico del uso de Hamcrest con JUnit:

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;  // Importa los matchers comunes

import org.junit.Test;

public class ExampleTest {
    @Test
    public void testExamples() {
        // Igualdad básica
        assertThat(5, is(5));
        
        // Coincidencia de cadenas
        String text = "Hello World";
        assertThat(text, containsString("World"));
        assertThat(text, startsWith("Hello"));
        
        // Coincidencia de colecciones
        List<String> items = Arrays.asList("apple", "banana", "orange");
        assertThat(items, hasItem("banana"));
        assertThat(items, hasSize(3));
        
        // Comparaciones numéricas
        assertThat(10, greaterThan(5));
        assertThat(3.14, closeTo(3.0, 0.2));
    }
}
```

3. Matchers Comunes de Hamcrest:
- `is()`: Prueba la igualdad
- `equalTo()`: Prueba la igualdad de objetos
- `containsString()`: Comprueba si una cadena contiene una subcadena
- `startsWith()`/ `endsWith()`: Comprobación de prefijo/sufijo de cadena
- `greaterThan()`/ `lessThan()`: Comparaciones numéricas
- `hasItem()`: Comprueba si una colección contiene un elemento
- `hasSize()`: Comprueba el tamaño de una colección
- `closeTo()`: Comprueba si un número está dentro de un rango
- `not()`: Niega cualquier matcher
- `allOf()`: Combina múltiples matchers (AND)
- `anyOf()`: Combina múltiples matchers (OR)

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
- Aserciones de prueba más legibles
- Mejores mensajes de error
- Condiciones de coincidencia flexibles
- Extensible con matchers personalizados

Consejos:
- Usa `import static` para que el código sea más conciso
- Combina matchers para condiciones complejas
- Consulta la documentación de Hamcrest para el conjunto completo de matchers
- Hamcrest funciona bien con JUnit, TestNG y otros frameworks de prueba

¿Te gustaría que profundice en algún matcher específico o que muestre más ejemplos?