---
audio: false
generated: true
lang: es
layout: post
title: Interfaces Funcionales en Java
translated: true
type: note
---

El paquete `java.util.function` en Java proporciona una colección de interfaces funcionales diseñadas para soportar la programación funcional, introducida en Java 8. Estas interfaces tienen cada una un único método abstracto, lo que las hace compatibles con expresiones lambda y referencias a métodos. Esta respuesta explica cómo usar algunas de las interfaces funcionales más comunes en este paquete—`Function<T, R>`, `Predicate<T>`, `Consumer<T>`, y `Supplier<T>`—con ejemplos prácticos.

---

### ¿Qué son las Interfaces Funcionales?
Una interfaz funcional es una interfaz con exactamente un método abstracto. El paquete `java.util.function` ofrece interfaces funcionales predefinidas para tareas comunes, por lo que no necesitas crear las tuyas. Estas interfaces se usan ampliamente con expresiones lambda, referencias a métodos y la API Stream para escribir código conciso y expresivo.

Aquí se explica cómo usar las interfaces clave:

---

### 1. `Function<T, R>`: Transformar una Entrada en una Salida
La interfaz `Function<T, R>` representa una función que toma una entrada de tipo `T` y produce una salida de tipo `R`. Su método abstracto es `apply`.

#### Ejemplo: Obtener la Longitud de un String
```java
import java.util.function.Function;

public class Main {
    public static void main(String[] args) {
        Function<String, Integer> stringLength = s -> s.length();
        System.out.println(stringLength.apply("Hello")); // Salida: 5
    }
}
```
- **Explicación**: La expresión lambda `s -> s.length()` define una `Function` que toma un `String` (`T`) y devuelve un `Integer` (`R`). El método `apply` ejecuta esta lógica.

---

### 2. `Predicate<T>`: Evaluar una Condición
La interfaz `Predicate<T>` representa una función booleana que toma una entrada de tipo `T`. Su método abstracto es `test`.

#### Ejemplo: Comprobar si un Número es Par
```java
import java.util.function.Predicate;

public class Main {
    public static void main(String[] args) {
        Predicate<Integer> isEven = n -> n % 2 == 0;
        System.out.println(isEven.test(4)); // Salida: true
        System.out.println(isEven.test(5)); // Salida: false
    }
}
```
- **Explicación**: La lambda `n -> n % 2 == 0` define un `Predicate` que devuelve `true` si la entrada es par. El método `test` evalúa esta condición.

---

### 3. `Consumer<T>`: Realizar una Acción
La interfaz `Consumer<T>` representa una operación que toma una entrada de tipo `T` y no devuelve ningún resultado. Su método abstracto es `accept`.

#### Ejemplo: Imprimir un String
```java
import java.util.function.Consumer;

public class Main {
    public static void main(String[] args) {
        Consumer<String> printer = s -> System.out.println(s);
        printer.accept("Hello, World!"); // Salida: Hello, World!
    }
}
```
- **Explicación**: La lambda `s -> System.out.println(s)` define un `Consumer` que imprime su entrada. El método `accept` realiza la acción.

---

### 4. `Supplier<T>`: Generar un Resultado
La interfaz `Supplier<T>` representa un proveedor de resultados, no toma ninguna entrada y devuelve un valor de tipo `T`. Su método abstracto es `get`.

#### Ejemplo: Generar un Número Aleatorio
```java
import java.util.function.Supplier;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Supplier<Integer> randomInt = () -> new Random().nextInt(100);
        System.out.println(randomInt.get()); // Genera un entero aleatorio entre 0 y 99
    }
}
```
- **Explicación**: La lambda `() -> new Random().nextInt(100)` define un `Supplier` que genera un entero aleatorio. El método `get` recupera el valor.

---

### Usando Interfaces Funcionales con Streams
Estas interfaces brillan en la API Stream de Java, donde permiten un procesamiento de datos conciso. Aquí hay un ejemplo que filtra, transforma e imprime una lista de strings:

#### Ejemplo: Procesar una Lista de Strings
```java
import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;

public class Main {
    public static void main(String[] args) {
        List<String> strings = Arrays.asList("a", "bb", "ccc", "dddd");

        Predicate<String> longerThanTwo = s -> s.length() > 2;       // Filtra strings más largos que 2
        Function<String, String> toUpperCase = s -> s.toUpperCase(); // Convierte a mayúsculas
        Consumer<String> printer = s -> System.out.println(s);       // Imprime cada resultado

        strings.stream()
               .filter(longerThanTwo)   // Mantiene "ccc" y "dddd"
               .map(toUpperCase)        // Convierte a "CCC" y "DDDD"
               .forEach(printer);       // Salida: CCC, DDDD (en líneas separadas)
    }
}
```
- **Explicación**: 
  - `filter` usa un `Predicate` para mantener strings con longitud > 2.
  - `map` usa una `Function` para transformar strings a mayúsculas.
  - `forEach` usa un `Consumer` para imprimir cada resultado.

#### Usando Referencias a Métodos
Puedes hacer esto aún más corto con referencias a métodos:
```java
strings.stream()
       .filter(s -> s.length() > 2)
       .map(String::toUpperCase)      // Referencia a método para Function
       .forEach(System.out::println); // Referencia a método para Consumer
```

---

### Composición de Interfaces Funcionales
Algunas interfaces permiten la composición para operaciones más complejas:
- **Composición de Function**: Usa `andThen` o `compose`.
  ```java
  Function<String, Integer> toLength = s -> s.length();
  Function<Integer, String> toString = i -> "La longitud es " + i;
  Function<String, String> combined = toLength.andThen(toString);
  System.out.println(combined.apply("Hello")); // Salida: La longitud es 5
  ```
- **Combinación de Predicate**: Usa `and`, `or` o `negate`.
  ```java
  Predicate<String> isLong = s -> s.length() > 5;
  Predicate<String> startsWithA = s -> s.startsWith("A");
  Predicate<String> isLongAndStartsWithA = isLong.and(startsWithA);
  System.out.println(isLongAndStartsWithA.test("Avocado")); // Salida: true
  ```

---

### Resumen
Aquí cuándo y cómo usar estas interfaces:
- **`Function<T, R>`**: Transformar una entrada en una salida (ej., `apply`).
- **`Predicate<T>`**: Evaluar una condición (ej., `test`).
- **`Consumer<T>`**: Realizar una acción sobre una entrada (ej., `accept`).
- **`Supplier<T>`**: Generar un valor sin entrada (ej., `get`).
- **Con Streams**: Combínalas para un procesamiento de datos potente.
- **Composición**: Encadénalas o combínalas para lógica compleja.

Puedes implementar estas interfaces usando expresiones lambda (ej., `s -> s.length()`) o referencias a métodos (ej., `String::toUpperCase`). Permiten un estilo de programación funcional en Java, haciendo tu código más conciso, legible y reutilizable, especialmente con la API Stream.