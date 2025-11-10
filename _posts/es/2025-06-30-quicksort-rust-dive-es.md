---
audio: false
generated: true
lang: es
layout: post
title: Ordenamiento Rápido en Rust para Desarrolladores Experimentados
translated: true
type: note
---

De acuerdo, dada tu sólida experiencia en algoritmos, desarrollo full-stack e incluso ingeniería móvil, encontrarás que el enfoque de Rust en cuanto a seguridad de memoria y control explícito te resultará bastante familiar en concepto, aunque la sintaxis y el rigor sean nuevos. Desglosemos esta implementación de Quicksort en Rust.

-----

### Quicksort en Rust: Una Inmersión para Desarrolladores Experimentados

Este código en Rust implementa el clásico **algoritmo Quicksort**. La idea central de Quicksort es elegir un elemento como pivote y particionar el array a su alrededor, de modo que los elementos menores que el pivote queden a un lado y los mayores al otro. Este proceso se aplica luego recursivamente a los sub-arrays.

Repasemos las funciones:

-----

### `fn quick_sort(arr: &mut [i32])`

```rust
fn quick_sort(arr: &mut [i32]) {
    if arr.len() <= 1 {
        return;
    }
    let pivot_index = partition(arr);
    let (left, right) = arr.split_at_mut(pivot_index);
    quick_sort(left);
    quick_sort(&mut right[1..]);
}
```

  * **`arr: &mut [i32]`**: Aquí es donde el sistema de tipos de Rust muestra inmediatamente sus colores.
      * `&mut` significa una **referencia mutable**. Esto significa que la función `quick_sort` obtiene una referencia prestada al array `arr`, y tiene permitido modificar el contenido de ese array *en el lugar*.
      * `[i32]` es un **slice** de enteros `i32`. En Rust, `[T]` es el tipo para un slice, que es una vista a una secuencia contigua de elementos. No posee los datos; solo apunta a una porción de un array o `Vec`. Esto es crucial para la eficiencia, ya que evita copiar datos. Estás familiarizado con punteros y secciones de arrays de tu experiencia en C/C++/Java; piensa en esto como la forma segura y explícita de Rust de manejar eso.
  * **Caso Base `if arr.len() <= 1`**: Caso base recursivo estándar para Quicksort. Si el slice tiene 0 o 1 elemento, ya está ordenado, así que simplemente retorna.
  * **`let pivot_index = partition(arr);`**: Esto llama a la función `partition` (que veremos a continuación) para reorganizar el slice. Retorna la posición final del elemento pivote.
  * **`let (left, right) = arr.split_at_mut(pivot_index);`**: Esta es una característica clave de Rust para el alias mutable seguro.
      * `split_at_mut` es un método en slices mutables. Toma un índice y divide el slice mutable en dos slices mutables *disjuntos*.
      * `left` será `arr[0..pivot_index]` y `right` será `arr[pivot_index..len]`.
      * Esto es fundamental para el **verificador de préstamos** de Rust. No puedes tener dos referencias mutables a los *mismos datos* al mismo tiempo. `split_at_mut` garantiza que `left` y `right` se refieran a partes completamente separadas del array original, satisfaciendo al verificador de préstamos y previniendo carreras de datos en un contexto multi-hilo (aunque esto sea de un solo hilo, el principio se aplica).
  * **`quick_sort(left);`**: Ordena recursivamente el sub-slice `left`.
  * **`quick_sort(&mut right[1..]);`**: Ordena recursivamente el sub-slice `right`.
      * `right[1..]` es importante: El slice `right` comienza en `pivot_index`. Dado que `arr[pivot_index]` es ahora el elemento pivote correctamente posicionado, lo excluimos de la llamada recursiva en el lado derecho.
      * `&mut` re-borra explícitamente un slice mutable de `right`.

-----

### `fn partition(arr: &mut [i32]) -> usize`

```rust
fn partition(arr: &mut [i32]) -> usize {
    let len = arr.len();
    let pivot = arr[len - 1];
    let mut i = 0;
    for j in 0..len - 1 {
        if arr[j] <= pivot {
            arr.swap(i, j);
            i += 1;
        }
    }
    arr.swap(i, len - 1);
    i
}
```

Esta función implementa el esquema de partición de Lomuto, que es una forma común de particionar un array para Quicksort.

  * **`let len = arr.len();`**: Obtiene la longitud del slice actual.
  * **`let pivot = arr[len - 1];`**: Se elige el **último elemento** del slice como pivote.
  * **`let mut i = 0;`**: `i` actúa como un puntero al "límite" entre los elementos menores o iguales al pivote y los elementos mayores al pivote. Los elementos a la izquierda de `i` serán menores o iguales al pivote.
  * **`for j in 0..len - 1`**: Este bucle itera a través de todos los elementos *excepto* el pivote (que está en `len - 1`).
  * **`if arr[j] <= pivot { ... }`**: Si el elemento actual `arr[j]` es menor o igual al pivote:
      * **`arr.swap(i, j);`**: Intercambia `arr[j]` con `arr[i]`. Esto mueve el elemento más pequeño a la sección "menor o igual".
      * **`i += 1;`**: Incrementa `i` para extender la sección "menor o igual".
  * **`arr.swap(i, len - 1);`**: Después del bucle, `i` es la posición correcta para el pivote. Intercambiamos el pivote (que todavía está en `len - 1`) a su posición final ordenada. Ahora, todos los elementos a la izquierda de `i` son menores o iguales a `arr[i]` (el pivote), y todos los elementos a la derecha son mayores.
  * **`i`**: La función retorna `i`, que es el índice final del elemento pivote.

-----

### `fn main()`

```rust
fn main() {
    let mut arr = [3, 6, 8, 10, 1, 2, 1];
    println!("Before: {:?}", arr);
    quick_sort(&mut arr);
    println!("After: {:?}", arr);
}
```

  * **`let mut arr = [3, 6, 8, 10, 1, 2, 1];`**:
      * `let mut` declara una **variable mutable**. Esto te permite reasignar la variable o modificar su contenido (si es de un tipo mutable).
      * `[3, ...]` crea un **array de tamaño fijo** en el stack. Su tamaño se conoce en tiempo de compilación.
  * **`println!("Before: {:?}", arr);`**: Usa la macro `println!` para la salida.
      * `{:?}` es el especificador de formato **debug print**. Utiliza el trait `Debug` para imprimir una representación legible del array.
  * **`quick_sort(&mut arr);`**: Llama a la función `quick_sort`, pasando una referencia mutable al array `arr`.
  * **`println!("After: {:?}", arr);`**: Imprime el array nuevamente después de ordenarlo.

-----

### Conclusiones Específicas de Rust para Ti

  * **Propiedad y Préstamo**: Este código es un ejemplo principal de los conceptos centrales de Rust. Estás pasando **referencias (`&` y `&mut`)** en lugar de copiar datos. Las referencias `&mut` son críticas para modificar el array en el lugar, y el **verificador de préstamos** (por ejemplo, aplicado por `split_at_mut`) garantiza que nunca tengas múltiples referencias mutables a los mismos datos, eliminando toda una clase de errores de concurrencia en tiempo de compilación. Este es probablemente el mayor cambio de paradigma desde lenguajes como Java o Python, pero ofrece seguridad de memoria sin un recolector de basura.
  * **Slices `[T]`**: Estos son increíblemente poderosos para trabajar con datos contiguos. Proporcionan una vista segura y eficiente de partes de arrays o vectores sin asignar nueva memoria.
  * **Macros (`println!`)**: Verás `!` después de muchas funciones de la biblioteca estándar (como `println!`, `vec!`, `format!`). Estos indican que son **macros**, no funciones regulares. Las macros expanden el código en tiempo de compilación, ofreciendo más flexibilidad y poder (como argumentos variables o generación de código en tiempo de compilación) en comparación con las funciones regulares.

Dada tu experiencia, es probable que aprecies las características de rendimiento y las garantías de seguridad que ofrece Rust, incluso si el "baile del verificador de préstamos" requiere un poco de práctica para acostumbrarse. Es una forma diferente de pensar sobre la gestión de memoria, pero una que conduce a código altamente robusto y eficiente.