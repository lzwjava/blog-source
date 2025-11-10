---
audio: false
generated: true
lang: es
layout: post
title: Implementación Rápida de Ordenación Zig
translated: true
type: note
---

Aquí tienes la implementación equivalente de Quick Sort en Zig.

```zig
const std = @import("std");

// Función Quick Sort
fn quickSort(arr: []i32) void {
    if (arr.len <= 1) {
        return;
    }

    const pivot_index = partition(arr);

    // Dividir el array en particiones izquierda y derecha
    // Nota: La división de slices en Zig es ligeramente diferente a la de Rust
    // Necesitamos manejar cuidadosamente el elemento pivote
    var left_slice = arr[0..pivot_index];
    var right_slice = arr[pivot_index + 1 .. arr.len]; // Excluir el pivote del slice derecho

    quickSort(left_slice);
    quickSort(right_slice);
}

// Función de partición
fn partition(arr: []i32) usize {
    const len = arr.len;
    // Por simplicidad, usaremos el último elemento como pivote, similar al ejemplo de Rust.
    // En un quicksort de producción, podrías elegir un pivote aleatorio o mediana-de-tres para un mejor rendimiento en el caso promedio.
    const pivot = arr[len - 1];
    var i: usize = 0; // Índice del elemento más pequeño

    for (0..(len - 1)) |j| {
        if (arr[j] <= pivot) {
            std.mem.swap(i32, &arr[i], &arr[j]);
            i += 1;
        }
    }

    // Colocar el pivote en su posición correcta
    std.mem.swap(i32, &arr[i], &arr[len - 1]);

    return i;
}

pub fn main() !void {
    var arr = [_]i32{ 3, 6, 8, 10, 1, 2, 1 };

    // Crear un slice mutable del array para la función quicksort
    var slice: []i32 = &arr;

    std.debug.print("Antes: {any}\n", .{slice});

    quickSort(slice);

    std.debug.print("Después: {any}\n", .{slice});
}

```

### Explicación de Cambios y Conceptos de Zig:

1.  **`const std = @import("std");`**: Esta línea importa la biblioteca estándar de Zig, que proporciona utilidades como `std.debug.print` para imprimir y `std.mem.swap` para intercambiar elementos.
2.  **`fn quickSort(arr: []i32) void`**:
      * `fn` declara una función.
      * `arr: []i32` declara `arr` como un slice de `i32` (enteros de 32 bits). En Zig, `[]T` denota un slice mutable de tipo `T`. No hay un `&mut` separado como en Rust; la mutabilidad está implícita según si la variable que contiene el slice es mutable.
      * `void` indica que la función no devuelve un valor.
3.  **`if (arr.len <= 1)`**: Las sentencias condicionales usan paréntesis alrededor de la condición.
4.  **`const pivot_index = partition(arr);`**: `const` se usa para variables inmutables.
5.  **División de Slices en Zig**:
      * `var left_slice = arr[0..pivot_index];`
      * `var right_slice = arr[pivot_index + 1 .. arr.len];`
      * A diferencia de `split_at_mut` de Rust, que crea dos slices mutables que no se superponen, el slicing de Zig `arr[start..end]` crea nuevos slices (vistas) del array original.
      * Crucialmente, en las llamadas recursivas, *debemos* excluir el pivote tanto de los sub-arrays izquierdo como derecho, ya que el pivote ya está en su posición final ordenada después de `partition`. En el código de Rust, `right[1..]` logra esto al omitir efectivamente el primer elemento del slice `right`, que es el pivote. Replicamos esto usando `pivot_index + 1` para el inicio del `right_slice`.
6.  **`std.mem.swap(i32, &arr[i], &arr[j]);`**:
      * `std.mem.swap` se usa para intercambiar elementos.
      * El primer argumento (`i32`) es el tipo de los elementos que se intercambian.
      * Los argumentos siguientes son punteros a las ubicaciones de memoria que se intercambiarán (`&arr[i]` y `&arr[j]`).
7.  **`for (0..(len - 1)) |j| { ... }`**: Este es un bucle `for` que itera desde `0` hasta (pero sin incluir) `len - 1`. La variable del bucle se captura como `j`.
8.  **`pub fn main() !void { ... }`**:
      * `pub` hace que la función `main` sea accesible públicamente.
      * `!void` indica que la función puede devolver un error, pero en este caso, no estamos manejando ninguno explícitamente. Para programas simples, `void` está bien, pero `!void` se ve a menudo en Zig ya que fomenta un manejo robusto de errores.
9.  **`var arr = [_]i32{ 3, 6, 8, 10, 1, 2, 1 };`**:
      * `[_]i32` declara un array de tamaño fijo de `i32`. El `_` le dice al compilador que infiera el tamaño a partir de la lista de inicialización.
10. **`var slice: []i32 = &arr;`**: Creamos un slice mutable (`[]i32`) a partir del array de tamaño fijo `arr` porque `quickSort` espera un slice.
11. **`std.debug.print("Antes: {any}\n", .{slice});`**:
      * `std.debug.print` es el equivalente en Zig de `println!` para salida de depuración.
      * `{any}` es un especificador de formato que le dice a Zig que imprima el valor en un formato legible para humanos, apto para depuración.
      * `.{slice}` es un "literal de estructura" (estructura anónima) usado para pasar los argumentos a la cadena de formato.

Para compilar y ejecutar este código de Zig:

1.  Guárdalo como `quick_sort.zig`.
2.  Abre tu terminal en el mismo directorio.
3.  Ejecuta: `zig run quick_sort.zig`