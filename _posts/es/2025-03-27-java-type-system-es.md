---
audio: false
generated: true
lang: es
layout: post
title: Sistema de Tipos de Java
translated: true
type: note
---

¡Adentrémonos en el sistema de tipos de Java! Este tutorial cubrirá los conceptos fundamentales para que puedas comenzar.

**¿Qué es un Sistema de Tipos?**

En programación, un sistema de tipos define los tipos de valores que se pueden utilizar y cómo se pueden manipular. Ayuda a garantizar que los programas sean type-safe, lo que significa que las operaciones se realizan sobre los tipos de datos correctos, previniendo errores inesperados y mejorando la confiabilidad del código.

Java tiene un **sistema de tipos fuerte y estático**.

* **Tipado Fuerte:** Java es fuertemente tipado, lo que significa que el tipo de una variable se aplica estrictamente en tiempo de compilación y en tiempo de ejecución. Generalmente no puedes realizar operaciones en tipos incompatibles sin una conversión explícita (casting). Esto ayuda a detectar errores temprano en el proceso de desarrollo.
* **Tipado Estático:** Java es estáticamente tipado, lo que significa que los tipos de las variables se declaran (o se infieren en algunos casos con `var`) antes de que el programa se ejecute. El compilador verifica la compatibilidad de estos tipos antes de la ejecución.

**Componentes Clave del Sistema de Tipos de Java:**

El sistema de tipos de Java se divide ampliamente en dos categorías principales:

1.  **Tipos Primitivos:** Son los tipos de datos más básicos en Java. Representan valores individuales directamente en la memoria.
2.  **Tipos de Referencia:** Estos tipos representan objetos, que son instancias de clases o interfaces. Las variables de referencia almacenan la dirección de memoria (referencia) del objeto.

Exploremos cada uno de ellos en detalle.

**1. Tipos Primitivos:**

Java tiene ocho tipos de datos primitivos:

| Tipo     | Tamaño (bits) | Descripción                                      | Rango                                                                 | Ejemplo           |
| -------- | ------------- | ------------------------------------------------ | --------------------------------------------------------------------- | ----------------- |
| `byte`   | 8             | Entero con signo                                 | -128 a 127                                                            | `byte edad = 30;` |
| `short`  | 16            | Entero con signo                                 | -32,768 a 32,767                                                      | `short contador = 1000;` |
| `int`    | 32            | Entero con signo                                 | -2,147,483,648 a 2,147,483,647                                      | `int puntuacion = 95;` |
| `long`   | 64            | Entero con signo                                 | -9,223,372,036,854,775,808 a 9,223,372,036,854,775,807              | `long poblacion = 1000000000L;` (Nota el sufijo 'L') |
| `float`  | 32            | Número de punto flotante de precisión simple (IEEE 754) | Aproximadamente ±3.40282347E+38F                                     | `float precio = 19.99F;` (Nota el sufijo 'F') |
| `double` | 64            | Número de punto flotante de precisión doble (IEEE 754) | Aproximadamente ±1.79769313486231570E+308                            | `double pi = 3.14159;` |
| `char`   | 16            | Carácter Unicode único                           | '\u0000' (0) a '\uffff' (65,535)                                    | `char inicial = 'J';` |
| `boolean`| Varía         | Representa un valor lógico                       | `true` o `false`                                                      | `boolean esVisible = true;` |

**Puntos Clave sobre los Tipos Primitivos:**

* Se almacenan directamente en la memoria.
* Tienen tamaños y rangos predefinidos.
* No son objetos y no tienen métodos asociados (aunque las clases wrapper como `Integer`, `Double`, etc., proporcionan representaciones de objetos).
* Se asignan valores predeterminados a los campos de tipo primitivo si no se inicializan explícitamente (por ejemplo, `int` por defecto es 0, `boolean` por defecto es `false`).

**2. Tipos de Referencia:**

Los tipos de referencia representan objetos, que son instancias de clases o interfaces. Las variables de tipos de referencia contienen la dirección de memoria (referencia) del objeto en el heap.

**Tipos de Referencia Comunes:**

* **Clases:** Las clases son planos para crear objetos. Definen los datos (campos/atributos) y el comportamiento (métodos) de los objetos de ese tipo.
    ```java
    class Perro {
        String nombre;
        int edad;

        public void ladrar() {
            System.out.println("¡Guau!");
        }
    }

    public class Main {
        public static void main(String[] args) {
            Perro miPerro = new Perro(); // 'Perro' es el tipo de referencia
            miPerro.nombre = "Buddy";
            miPerro.edad = 3;
            miPerro.ladrar();
        }
    }
    ```
* **Interfaces:** Las interfaces definen un contrato de métodos que una clase puede implementar. Representan un conjunto de comportamientos.
    ```java
    interface Animal {
        void hacerSonido();
    }

    class Gato implements Animal {
        public void hacerSonido() {
            System.out.println("¡Miau!");
        }
    }

    public class Main {
        public static void main(String[] args) {
            Animal miGato = new Gato(); // 'Animal' es el tipo de referencia
            miGato.hacerSonido();
        }
    }
    ```
* **Arrays:** Los arrays son colecciones de elementos del mismo tipo. El tipo del array está determinado por el tipo de sus elementos.
    ```java
    int[] numeros = new int[5]; // 'int[]' es el tipo de referencia
    numeros[0] = 10;

    String[] nombres = {"Alicia", "Bob", "Carlos"}; // 'String[]' es el tipo de referencia
    ```
* **Enums (Enumeraciones):** Los enums representan un conjunto fijo de constantes con nombre.
    ```java
    enum Dia {
        LUNES, MARTES, MIERCOLES, JUEVES, VIERNES, SABADO, DOMINGO
    }

    public class Main {
        public static void main(String[] args) {
            Dia hoy = Dia.LUNES; // 'Dia' es el tipo de referencia
            System.out.println("Hoy es " + hoy);
        }
    }
    ```
* **Clases Wrapper:** Para cada tipo primitivo, Java proporciona una clase wrapper correspondiente (por ejemplo, `Integer` para `int`, `Double` para `double`). Estas permiten tratar los valores primitivos como objetos.
    ```java
    Integer num = 10; // 'Integer' es el tipo de referencia
    Double valorPi = 3.14; // 'Double' es el tipo de referencia
    ```

**Puntos Clave sobre los Tipos de Referencia:**

* Almacenan referencias (direcciones de memoria) a objetos en el heap.
* Pueden ser `null`, lo que significa que la referencia no apunta a ningún objeto.
* Tienen métodos y campos asociados (definidos por su clase o interfaz).
* El valor por defecto para los campos de tipo de referencia no inicializados es `null`.

**3. Inferencia de Tipos con `var` (Java 10 y posteriores):**

Java 10 introdujo la palabra clave `var`, que permite la inferencia de tipos de variables locales. En lugar de declarar explícitamente el tipo, el compilador puede inferir el tipo basándose en la expresión inicializadora.

```java
var mensaje = "Hola"; // El compilador infiere que 'mensaje' es de tipo String
var contador = 100;   // El compilador infiere que 'contador' es de tipo int
var precios = new double[]{10.5, 20.3}; // El compilador infiere que 'precios' es de tipo double[]
```

**Notas Importantes sobre `var`:**

* `var` solo se puede usar para variables locales dentro de métodos, constructores o inicializadores.
* Debes proporcionar un inicializador cuando uses `var` porque el compilador lo necesita para inferir el tipo.
* `var` no cambia el tipado estático de Java. El tipo aún se determina en tiempo de compilación.

**4. Genéricos:**

Los genéricos permiten parametrizar tipos. Esto significa que puedes definir clases, interfaces y métodos que puedan trabajar con diferentes tipos mientras proporcionan seguridad de tipos en tiempo de compilación.

```java
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> nombres = new ArrayList<>(); // Lista de Strings
        nombres.add("Alicia");
        nombres.add("Bob");

        // nombres.add(123); // Esto causaría un error en tiempo de compilación

        List<Integer> numeros = new ArrayList<>(); // Lista de Integers
        numeros.add(10);
        numeros.add(20);
    }
}
```

Aquí, `<String>` y `<Integer>` son parámetros de tipo. Los genéricos ayudan a prevenir `ClassCastException` en tiempo de ejecución al hacer cumplir las restricciones de tipo en tiempo de compilación.

**5. Verificación de Tipos:**

Java realiza la verificación de tipos en dos etapas principales:

* **Verificación de Tipos en Tiempo de Compilación:** El compilador de Java verifica el código en busca de errores de tipo antes de que se ejecute. Si hay incompatibilidades de tipo (por ejemplo, intentar asignar un `String` a una variable `int` sin un casting explícito), el compilador reportará un error y evitará que el programa sea compilado.
* **Verificación de Tipos en Tiempo de Ejecución:** Algunas verificaciones de tipo se realizan durante la ejecución del programa. Por ejemplo, cuando casteas un tipo de referencia a otro tipo, la JVM verifica si el objeto es realmente una instancia del tipo objetivo. Si no lo es, se lanza una `ClassCastException`.

**6. Conversión de Tipos (Casting):**

A veces necesitas convertir un valor de un tipo a otro. Java admite dos tipos de casting:

* **Casting Implícito (Conversión de Ampliación):** Ocurre automáticamente cuando asignas un valor de un tipo primitivo más pequeño a una variable de un tipo primitivo más grande. No ocurre pérdida de datos.
    ```java
    int miInt = 10;
    long miLong = miInt; // Casting implícito de int a long
    double miDouble = miLong; // Casting implícito de long a double
    ```
* **Casting Explícito (Conversión de Reducción):** Debe hacerse manualmente usando un operador de cast `(tipoObjetivo)` cuando asignas un valor de un tipo primitivo más grande a una variable de un tipo primitivo más pequeño. Podría ocurrir pérdida de datos.
    ```java
    double miDouble = 10.99;
    int miInt = (int) miDouble; // Casting explícito de double a int (miInt será 10)
    ```
* **Casting de Tipos de Referencia:** También puedes castear entre tipos de referencia, pero es más complejo e involucra herencia e interfaces.
    * **Upcasting:** Castear un objeto de una subclase al tipo de su superclase. Esto siempre está permitido implícitamente.
    * **Downcasting:** Castear un objeto del tipo de una superclase al tipo de su subclase. Esto requiere un cast explícito y puede resultar en una `ClassCastException` en tiempo de ejecución si el objeto no es realmente una instancia de la subclase.

**Ejemplo de Casting de Tipos de Referencia:**

```java
class Animal {}
class Perro extends Animal {
    public void ladrar() {
        System.out.println("¡Guau!");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal miAnimal = new Perro(); // Upcasting (implícito)

        // Perro miPerro = miAnimal; // Error en tiempo de compilación: No se puede convertir implícitamente de Animal a Perro
        Perro miPerro = (Perro) miAnimal; // Downcasting (explícito)
        miPerro.ladrar(); // Esto funcionará

        Animal otroAnimal = new Animal();
        // Perro otroPerro = (Perro) otroAnimal; // Esto lanzará una ClassCastException en tiempo de ejecución
    }
}
```

**Conclusión:**

Comprender el sistema de tipos de Java es crucial para escribir código correcto y robusto. Al conocer la diferencia entre tipos primitivos y de referencia, cómo funcionan los genéricos y las reglas de verificación y conversión de tipos, puedes evitar errores de programación comunes y construir aplicaciones más confiables.

Este tutorial proporciona una comprensión fundamental. A medida que continúes aprendiendo Java, te encontrarás con conceptos más avanzados relacionados con los tipos, como la herencia, el polimorfismo y escenarios genéricos más complejos. ¡Sigue practicando y experimentando con diferentes tipos para solidificar tu comprensión!