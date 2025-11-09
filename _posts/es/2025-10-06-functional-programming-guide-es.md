---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Guía de Programación Funcional en Java
translated: true
type: note
---

Java ha adoptado los principios de programación funcional desde Java 8, introduciendo lambdas, streams y otras características que hacen el código más conciso, legible y declarativo. Esta guía cubre desde los fundamentos hasta conceptos avanzados, asumiendo familiaridad con Java básico. Usaremos sintaxis de Java 8+, ya que fue cuando debutaron estas características. Los ejemplos están en bloques de código Java para facilitar la copia.

## 1. Introducción a la Programación Funcional en Java

La programación funcional (FP) enfatiza:
- **Funciones puras**: Funciones sin efectos secundarios (ej., sin cambios de estado mutable).
- **Inmutabilidad**: Los datos no cambian una vez creados.
- **Funciones de orden superior**: Funciones que toman o devuelven otras funciones.
- **Estilo declarativo**: Enfocarse en *qué* hacer, no en *cómo* (ej., mediante streams en lugar de bucles).

Java no es puramente funcional como Haskell, pero combina FP con sus raíces orientadas a objetos. Facilitadores clave:
- Expresiones lambda (funciones anónimas).
- Interfaces funcionales (interfaces con un método abstracto).
- Streams API para procesar colecciones de forma funcional.

Beneficios: Menos código boilerplate, paralelismo más fácil, mejor capacidad de composición.

## 2. Expresiones Lambda

Las lambdas son funciones anónimas utilizadas para implementaciones cortas y únicas. Son la puerta de entrada a FP en Java.

### Sintaxis Básica
Una lambda es: `(parámetros) -> { cuerpo }`
- Paréntesis opcionales para un solo parámetro.
- Llaves opcionales para una sola expresión (retorno implícito).
- La inferencia de tipos suele funcionar, pero puedes especificar tipos.

```java
// Clase anónima interna tradicional
Runnable r = new Runnable() {
    @Override
    public void run() {
        System.out.println("Hello, World!");
    }
};

// Equivalente lambda
Runnable lambda = () -> System.out.println("Hello, World!");
lambda.run();
```

### Con Parámetros
```java
// Ejemplo de operador binario
BinaryOperator<Integer> add = (a, b) -> a + b;
System.out.println(add.apply(2, 3)); // 5

// Cuerpo multi-línea
Comparator<String> comparator = (s1, s2) -> {
    int lenDiff = s1.length() - s2.length();
    return lenDiff != 0 ? lenDiff : s1.compareTo(s2);
};
```

### Captura de Variables (Efectivamente Final)
Las lambdas pueden acceder a variables externas, pero deben ser **efectivamente final** (no reasignadas).
```java
int threshold = 10;
Predicate<Integer> isHigh = x -> x > threshold; // OK
// threshold = 20; // Error: no es efectivamente final
```

## 3. Interfaces Funcionales

Una interfaz funcional tiene exactamente un método abstracto (SAM - Single Abstract Method). Java proporciona integradas en `java.util.function`.

### Ejemplos Integrados
- `Predicate<T>`: `boolean test(T t)`
- `Function<T, R>`: `R apply(T t)`
- `Consumer<T>`: `void accept(T t)`
- `Supplier<T>`: `T get()`
- `BiFunction<T, U, R>`, etc., para dos entradas.

Personalizadas:
```java
@FunctionalInterface  // Opcional, pero buena práctica
interface Transformer {
    String transform(String input);
}

Transformer upper = s -> s.toUpperCase();
System.out.println(upper.transform("java")); // JAVA
```

Usa `@FunctionalInterface` para hacer cumplir SAM.

### Métodos Default y Estáticos
Las interfaces funcionales pueden tener métodos default (Java 8+), como `Optional.orElse()`.
```java
default int compare(String a, String b) { ... } // Permitido
static void utility() { ... } // Permitido
```

## 4. Referencias a Métodos

Abreviaturas para lambdas que invocan métodos existentes. Sintaxis: `Clase::método` o `instancia::método`.

Tipos:
- Estático: `Clase::métodoEstático`
- Instancia de tipo específico: `Clase::métodoDeInstancia`
- Instancia de objeto arbitrario: `objeto::métodoDeInstancia`
- Constructor: `Clase::new`

Ejemplos:
```java
// Lambda: x -> System.out.println(x)
Consumer<String> printer = System.out::println;

// Método estático
Function<String, Integer> length = String::length;

// Método de instancia
List<String> list = Arrays.asList("a", "b");
list.forEach(System.out::println); // Imprime cada uno

// Constructor
Supplier<List<String>> listSupplier = ArrayList::new;
```

## 5. Streams API

Los Streams procesan colecciones de forma declarativa: crear → transformar → recolectar. Evaluación perezosa (las operaciones intermedias no se ejecutan hasta la operación terminal).

### Creando Streams
```java
import java.util.*;
import java.util.stream.*;

List<String> names = Arrays.asList("Alice", "Bob", "Charlie");

// Desde colección
Stream<String> stream = names.stream();

// Desde array
String[] arr = {"x", "y"};
Stream<String> arrStream = Arrays.stream(arr);

// Infinito
Stream<Integer> infinite = Stream.iterate(0, n -> n + 1);
```

### Operaciones Intermedias (Perezosas)
Encadénalas; no hay cálculo hasta la operación terminal.
- `filter(Predicate)`: Mantiene elementos que coinciden.
- `map(Function)`: Transforma cada elemento.
- `flatMap(Function<? super T, ? extends Stream<? extends R>>)`: Aplana streams anidados.
- `distinct()`, `sorted()`, `limit(n)`, `skip(n)`.

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
List<Integer> evensSquared = numbers.stream()
    .filter(n -> n % 2 == 0)
    .map(n -> n * n)
    .collect(Collectors.toList()); // [4, 16]
```

### Operaciones Terminales (Ansiosas)
Desencadenan el cálculo y devuelven un resultado.
- `collect(Collector)`: A lista, set, map.
- `forEach(Consumer)`: Efecto secundario (evitar si es posible).
- `reduce()`: Agregar (ej., suma).
- `anyMatch()`, `allMatch()`, `findFirst()`.

```java
// Reduce: suma
int sum = numbers.stream().reduce(0, Integer::sum); // 15

// Recolectar a map
Map<String, Integer> nameLengths = Stream.of("Alice", "Bob")
    .collect(Collectors.toMap(s -> s, String::length)); // {Alice=5, Bob=3}

// Agrupación
Map<Integer, List<String>> byLength = names.stream()
    .collect(Collectors.groupingBy(String::length)); // {5=[Alice, Charlie], 3=[Bob]}
```

### Streams Paralelos
Para paralelismo: `parallelStream()` o `.parallel()`. Usar con cautela (la depuración es más difícil).
```java
long count = names.parallelStream().count(); // 3
```

## 6. Colectores

De `java.util.stream.Collectors`. Construyen reducciones complejas.

Comunes:
- `toList()`, `toSet()`, `toMap()`
- `joining()`: Concatenar strings.
- `summingInt()`, `averagingDouble()`
- `groupingBy()`, `partitioningBy()`
- `collectingAndThen()`: Post-procesar.

```java
// Colector personalizado para máximo por longitud
String longest = names.stream()
    .collect(Collectors.maxBy(Comparator.comparingInt(String::length)))
    .orElse(""); // "Charlie"

// Particionar pares/impares
Map<Boolean, List<Integer>> partitions = numbers.stream()
    .collect(Collectors.partitioningBy(n -> n % 2 == 0));
```

## 7. Optional

Evita `NullPointerException` envolviendo valores potencialmente nulos. Fomenta el manejo explícito de nulos.

Creación:
- `Optional.of(valor)`: No nulo.
- `Optional.ofNullable(valor)`: Nulo → vacío.
- `Optional.empty()`.

Operaciones:
- `isPresent()`, `ifPresent(Consumer)`
- `orElse(valor_por_defecto)`, `orElseThrow()`
- `map()`, `flatMap()` para encadenar.

```java
Optional<String> opt = Optional.ofNullable(getName()); // Asume que puede devolver null

String name = opt.orElse("Unknown");
opt.ifPresent(System.out::println);

String upper = opt.map(String::toUpperCase).orElse("DEFAULT");
```

Los Streams a menudo devuelven `Optional` (ej., `findFirst()`).

## 8. Temas Avanzados

### Funciones Componibles
`Function.andThen()`, `Function.compose()` para encadenar.
```java
Function<String, Integer> len = String::length;
Function<Integer, String> toStr = i -> "Len: " + i;

Function<String, String> chain = len.andThen(toStr);
System.out.println(chain.apply("Java")); // Len: 4
```

### Recursión y Llamadas de Cola
Java carece de optimización, pero usa `Stream.iterate()` para recursión iterativa.

### Ayudantes de Inmutabilidad
Usa `Collections.unmodifiableList()` o bibliotecas como Guava/Immutable Collections (aunque integrado desde Java 10+ con `List.of()`).

`List.of("a", "b")` crea listas inmutables (Java 9+).

### Pattern Matching (Java 21+ Preview/Estable)
Mejora la FP con desestructuración en switches.
```java
// Característica en vista previa; habilitar con --enable-preview
String desc = switch (obj) {
    case Integer i -> "int: " + i;
    case String s -> "str: " + s.length();
    default -> "unknown";
};
```

### Hilos Virtuales (Java 21+)
La FP brilla con hilos livianos para streams concurrentes.

## 9. Mejores Prácticas

- **Prefiere la inmutabilidad**: Usa campos final, evita mutar colecciones.
- **Evita efectos secundarios**: Mantén las lambdas puras; efectos secundarios solo en `forEach` o consumidores explícitos.
- **Streams vs. Bucles**: Usa streams para legibilidad; bucles para código crítico de rendimiento.
- **Nulos**: Favorece `Optional` sobre comprobaciones de nulos.
- **Testing**: Simula interfaces funcionales fácilmente con lambdas.
- **Rendimiento**: Los streams tienen sobrecarga; perfila antes de usar paralelos.
- **Legibilidad**: Las lambdas cortas están bien; extrae métodos para lógica compleja.

Errores comunes:
- Modificar estado externo en lambdas.
- Olvidar la operación terminal (¡los streams no hacen nada!).
- Uso excesivo de streams paralelos (no siempre son más rápidos).

## 10. Ejemplo: Pipeline Funcional

Procesa una lista de empleados de forma funcional.

```java
import java.util.*;
import java.util.stream.Collectors;

class Employee {
    String name;
    int salary;
    Department dept;

    Employee(String name, int salary, Department dept) {
        this.name = name;
        this.salary = salary;
        this.dept = dept;
    }
}

enum Department { ENG, HR }

public class FunctionalExample {
    public static void main(String[] args) {
        List<Employee> employees = Arrays.asList(
            new Employee("Alice", 50000, Department.ENG),
            new Employee("Bob", 60000, Department.HR),
            new Employee("Charlie", 55000, Department.ENG)
        );

        // Nombres de ingenieros bien pagados, ordenados
        List<String> result = employees.stream()
            .filter(e -> e.dept == Department.ENG)
            .filter(e -> e.salary > 52000)
            .map(Employee::getName)  // Asume getter
            .sorted()
            .collect(Collectors.toList());

        System.out.println(result); // [Charlie]
    }
}
```

## Conclusión

Las lambdas y la FP transforman Java de imperativo a expresivo. Comienza con reemplazos simples (ej., `forEach` sobre bucles), luego construye pipelines. Practica en proyectos reales para dominarlo. Para inmersiones más profundas, experimenta en un IDE.

### Referencias
- [Oracle Java Tutorials: Lambda Expressions](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html)
- [Baeldung: Java 8 Functional Interfaces](https://www.baeldung.com/java-functional-interfaces)
- [Java Streams Guide](https://www.baeldung.com/java-8-streams)
- [Effective Java (3rd Ed.) - Item 42-45 on Lambdas](https://www.oreilly.com/library/view/effective-java-3rd/9780134686097/)