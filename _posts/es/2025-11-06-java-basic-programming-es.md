---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Guía Básica de Programación en Java
translated: true
type: note
---

Aquí tienes una guía centrada para la **Parte II: Programación Básica** de *08553 Introducción a la Programación—Java*, adaptada para el **Examen Nacional de Educación Superior por Autodidactas (自考)**. Esta sección te entrena para escribir pequeños programas Java correctos y entender cómo Java maneja los datos y las expresiones.

---

## 1. Leer Entrada desde la Consola

### 1.1 Usar `Scanner`

Java lee la entrada con la clase `Scanner` en `java.util`.

```java
import java.util.Scanner;

public class InputExample {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Introduce tu nombre: ");
        String name = sc.nextLine();
        System.out.print("Introduce tu edad: ");
        int age = sc.nextInt();
        System.out.println("Hola " + name + ", tienes " + age + " años.");
        sc.close();
    }
}
```

**Puntos clave:**

* Siempre `import java.util.Scanner;`
* Usa `nextInt()`, `nextDouble()`, `nextLine()` según el tipo de dato.
* Cierra el `Scanner` para liberar recursos.
* Ten cuidado: `nextLine()` lee el resto de la línea, así que mezclarlo con `nextInt()` puede causar que se omita una entrada.

---

## 2. Identificadores, Variables, Expresiones, Asignaciones y Constantes

### 2.1 Identificadores

Nombres que das a variables, métodos o clases.
**Reglas:**

* Debe comenzar con una letra, `_` o `$`.
* No puede comenzar con un número.
* Distingue entre mayúsculas y minúsculas (`score` ≠ `Score`).
* No puede ser una palabra clave (`int`, `class`, `if`, etc.).

**Ejemplos:**
`studentName`, `_total`, `$price`

### 2.2 Variables

Una variable contiene datos de un **tipo** determinado.
Ejemplos de declaración:

```java
int age = 20;
double price = 12.5;
char grade = 'A';
boolean passed = true;
```

### 2.3 Sentencias de Asignación

Asigna un valor usando `=` (derecha → izquierda):

```java
x = 5;
y = x + 2;
```

### 2.4 Constantes

Declaradas con `final`, no se pueden cambiar después:

```java
final double PI = 3.14159;
```

Usa nombres en mayúsculas para las constantes.

---

## 3. Tipos de Datos Numéricos y Operaciones

### 3.1 Tipos Numéricos Comunes

* `byte` (entero de 8 bits)
* `short` (16 bits)
* `int` (32 bits, más común)
* `long` (64 bits)
* `float` (decimal de 32 bits)
* `double` (decimal de 64 bits, más preciso)

**Ejemplo:**

```java
int count = 5;
double price = 19.99;
```

### 3.2 Operadores Aritméticos Básicos

`+`, `-`, `*`, `/`, `%`

Ejemplos:

```java
int a = 10, b = 3;
System.out.println(a / b);  // 3 (división entera)
System.out.println(a % b);  // 1
System.out.println((double)a / b); // 3.3333 (conversión de tipo)
```

---

## 4. Conversión de Tipo (Casting)

### 4.1 Conversión Automática (Ampliación)

Tipo pequeño → grande automáticamente:
`int` → `long` → `float` → `double`

Ejemplo:

```java
int i = 10;
double d = i;  // conversión automática
```

### 4.2 Conversión Manual (Casting)

Convertir explícitamente tipo grande → pequeño:

```java
double d = 9.7;
int i = (int) d; // i = 9 (se pierde la fracción)
```

Ten cuidado con la **pérdida de precisión**.

---

## 5. Evaluación de Expresiones y Precedencia de Operadores

### 5.1 Orden de las Operaciones

Java sigue un orden definido:

1. Paréntesis `( )`
2. Unarios `+`, `-`, `++`, `--`
3. Multiplicación, división, módulo `* / %`
4. Suma y resta `+ -`
5. Asignación `=`

Ejemplo:

```java
int x = 2 + 3 * 4;   // 14, no 20
int y = (2 + 3) * 4; // 20
```

### 5.2 Expresiones Mixtas

Si un operando es `double`, el resultado se convierte en `double`:

```java
double result = 5 / 2;     // 2.0 (división entera primero)
double result2 = 5.0 / 2;  // 2.5 (división de punto flotante)
```

---

## 6. Asignación Aumentada e Incremento/Decremento

### 6.1 Asignación Aumentada

Operadores abreviados:

```java
x += 3;  // igual que x = x + 3
y *= 2;  // igual que y = y * 2
```

### 6.2 Incremento y Decremento

`++` aumenta en 1, `--` disminuye en 1.
Dos formas:

```java
int a = 5;
System.out.println(a++); // imprime 5, luego a = 6
System.out.println(++a); // a = 7, luego imprime 7
```

**Recuerda:**

* Postfijo (`a++`) → usar luego incrementar
* Prefijo (`++a`) → incrementar luego usar

---

## 7. Errores Comunes a Evitar

* Usar `=` en lugar de `==` en comparaciones.
* División entera cuando esperas decimales.
* Olvidar inicializar una variable antes de usarla.
* Perder datos en la conversión de tipo (ej., `(int) 3.9` → 3).

---

## 8. Preguntas Típicas de Examen

**Ejemplo 1:**

> ¿Cuál es la salida del siguiente código?
>
> ```java
> int x = 5, y = 2;
> double z = x / y;
> System.out.println(z);
> ```

**Respuesta:** `2.0` (división entera antes de la asignación)

**Ejemplo 2:**

> ¿Qué operador tiene la precedencia más alta?
> A. `+`
> B. `*`
> C. `=`
> D. `++`
> **Respuesta:** D

**Ejemplo 3:**

> ¿Cuál es la salida de este código?
>
> ```java
> int a = 3;
> int b = ++a + a++;
> System.out.println(b);
> ```

**Explicación:**
`++a` hace `a = 4`, suma `4`, luego `a++` usa `4` e incrementa a `5`.
Entonces `b = 8`.

---

¿Te gustaría que continúe con la **Parte III: Estructuras de Control (Sentencias de Selección y Bucle)** a continuación? Cubre `if`, `switch`, `for`, `while`, y es el núcleo de la lógica procedural en el examen de Java.