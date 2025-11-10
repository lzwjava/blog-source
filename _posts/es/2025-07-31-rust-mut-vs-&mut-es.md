---
audio: false
generated: true
image: false
lang: es
layout: post
title: Mut y &mut de Rust explicados
translated: true
type: note
---

En Rust, las palabras clave `mut` y `&mut` tienen propósitos relacionados pero distintos, y no son directamente equivalentes a los conceptos de copia profunda/superficial de Java o a los punteros de C—aunque podemos establecer algunas analogías para mayor claridad. Lo desglosaré paso a paso, explicaré las diferencias y abordaré tus preguntas sobre paso por valor vs. paso por referencia, mutabilidad y cómo los cambios afectan a los datos originales. Usaré ejemplos basados en tu código proporcionado para ilustrarlo.

### 1. **Entendiendo `mut` en Declaraciones de Variables**
   - Cuando declaras una variable con `let mut`, estás haciendo que el *binding* (el nombre de la variable) sea mutable. Esto significa que puedes reasignar la variable o modificar su contenido directamente, pero solo dentro del ámbito donde se declara.
   - Ejemplo de tu código:
     ```rust
     let mut arr = [3, 6, 8, 10, 1, 2, 1];
     ```
     Aquí, `arr` es mutable, por lo que podrías hacer `arr[0] = 99;` o incluso reasignar `arr = [1, 2, 3];` más tarde si quisieras. Sin `mut`, Rust se quejaría de intentar modificar una variable inmutable (Rust tiene la inmutabilidad por defecto para mayor seguridad).
   - Este `mut` se refiere a la variable en sí, no a cómo se pasa a las funciones. No implica copia o referencia—es solo un permiso para cambiar la variable en su lugar.

### 2. **Entendiendo `&mut` en Parámetros de Función y Referencias**
   - `&mut` crea una *referencia mutable* (también llamada préstamo mutable). Esto es como un puntero en C que permite leer *y* escribir en los datos apuntados, pero con el estricto comprobador de préstamos de Rust garantizando seguridad (sin carreras de datos, sin punteros colgantes).
   - En tu código:
     ```rust
     fn quick_sort(arr: &mut [i32]) { ... }
     ```
     - El parámetro `arr` es una referencia mutable a un segmento de `i32`s (`&mut [i32]`). Los segmentos en Rust son vistas a arrays o vectores (como un puntero + longitud), y casi siempre se pasan como referencias porque los segmentos son tipos "sin tamaño" (su tamaño no se conoce en tiempo de compilación).
     - Cuando llamas a `quick_sort(&mut arr);`, estás pasando una referencia mutable al `arr` original. Esto permite a la función modificar los elementos del array original a través de la referencia (por ejemplo, mediante intercambios en `partition`).
     - Dentro de la función, operaciones como `arr.swap(i, j);` afectan directamente a los datos originales porque `arr` es una referencia que apunta a ellos.
   - Sin el `&`, no podrías pasar un segmento como `[i32]` directamente como parámetro de esta manera—Rust requiere referencias para tipos sin tamaño. Pero más generalmente, `&mut` permite el paso por referencia con derechos de mutación.

### 3. **Paso por Valor vs. Paso por Referencia en Rust**
   - Rust utiliza *propiedad* como su modelo central, que es diferente de Java (que es mayormente basado en referencia con recolección de basura) o C (punteros manuales).
     - **Paso por valor (transferencia de propiedad)**: Cuando pasas un valor sin `&` (por ejemplo, `fn foo(x: i32)` o `fn bar(mut v: Vec<i32>)`), la propiedad de los datos se mueve a la función. La función puede modificarlos localmente, pero los cambios no afectan al original del llamador (porque el llamador ya no es el propietario). Si el tipo implementa `Copy` (como los primitivos `i32`), se copia automáticamente en lugar de moverse—no hay copia profunda a menos que clones explícitamente.
       - Ejemplo:
         ```rust
         fn foo(mut x: i32) {
             x += 1;  // Modifica la x local, pero el original del llamador no cambia (o se movió/copió).
             println!("Dentro: {}", x);
         }

         let y = 5;
         foo(y);  // Pasa por valor (copia, ya que i32 es Copy).
         println!("Después: {}", y);  // Sigue siendo 5.
         ```
       - Esto es como "paso por valor" en otros lenguajes: los primitivos se copian, los tipos más grandes (como arrays/vectores) se mueven (eficiente, sin copia a menos que se clone).
     - **Paso por referencia (préstamo)**: Usar `&` (referencia inmutable) o `&mut` (referencia mutable) "toma prestados" los datos sin transferir la propiedad. La función obtiene una vista temporal (como un puntero), y el propietario original retiene el control.
       - `&`: Préstamo de solo lectura. No se puede modificar el original.
       - `&mut`: Préstamo de lectura-escritura. *Sí puede* modificar el original, como pasar por referencia en C++ o un puntero mutable en C.
       - Ejemplo:
         ```rust
         fn bar(x: &mut i32) {
             *x += 1;  // Desreferencia y modifica el original.
         }

         let mut y = 5;
         bar(&mut y);  // Pasa referencia mutable.
         println!("Después: {}", y);  // Ahora 6, el original cambió.
         ```
       - En tu código de quicksort, es paso por referencia con `&mut`, por lo que los intercambios cambian el array original. Si fuera solo `& [i32]`, no podrías modificarlo (préstamo inmutable).

   - Respecto a tu punto: Sí, `&mut` permite cambiar los valores originales (paso por referencia con mutación), mientras que pasar sin `&` (paso por valor) o copia o mueve los datos, por lo que las modificaciones son locales y no afectan al original. Pero:
     - No todos los tipos se copian automáticamente—solo aquellos que implementan `Copy` (por ejemplo, `i32`, no arrays o vectores). Para tipos que no son `Copy` como tu array, pasar por valor *movería* la propiedad, y necesitarías devolverlo para "devolvérselo" al llamador.
     - Rust evita copias innecesarias por eficiencia. Tu array no se copia cuando se pasa como `&mut [i32]`—es solo una referencia (superficial, como un puntero).

### 4. **Comparación con Java y C**
   - **Java**: Todo lo no primitivo se pasa por referencia (superficial—los objetos se comparten, pero reasignar el parámetro no afecta al llamador). Los primitivos se pasan por valor (copia). No hay un equivalente directo a `mut` o `&mut`; la mutabilidad se controla por el diseño de la clase (por ejemplo, campos final). Java no tiene el sistema de propiedad de Rust, por lo que es más propenso a problemas de estado mutable compartido. La copia profunda requiere clonación manual.
   - **C**: `&mut` es como pasar un puntero (`int*`) donde puedes desreferenciar y modificar (`*ptr = 10;`). `mut` simple (en declaraciones) es como variables no constantes. Pero C no tiene comprobador de préstamos, por lo que gestionas los tiempos de vida manualmente (propenso a errores). Pasar por valor en C copia los datos (superficial para structs a menos que hagas una copia profunda).
   - Diferencia clave: Rust aplica "una referencia mutable a la vez" (o múltiples inmutables), previniendo errores. Sin nulos, sin punteros salvajes.

### 5. **¿Por Qué `mut` a Veces y `&mut` Otras Veces en Tu Código?**
   - Solo `mut`: Se usa para variables locales que necesitan ser modificables, como `let mut arr` (para poder pasar `&mut arr` más tarde o modificarla directamente).
   - `&mut`: Se usa en parámetros cuando la función necesita tomar prestados y modificar los datos del llamador sin tomar propiedad. En `quick_sort` y `partition`, `&mut [i32]` les permite ordenar el array en el lugar sin moverlo/copiarlo.
   - Si intentaras `fn quick_sort(mut arr: [i32])`, no compilaría—los segmentos no se pueden pasar por valor así. Necesitarías un array de tamaño fijo (por ejemplo, `[i32; 7]`) y movería la propiedad.
   - En `partition`, el bucle usa `mut i` internamente—esa es una variable mutable local, no relacionada con el paso.

### 6. **¿Cambia los Valores Originales?**
   - Sí para `&mut`: Los cambios se propagan al original (paso por referencia).
   - No para paso por valor (sin `&`): Cambios locales solamente (a menos que devuelvas el valor modificado).
   - En tu `quick_sort_interact()`, el `println!("After: {:?}", arr);` mostrará el array ordenado porque se usó `&mut`.

Si ejecutas tu código, debería mostrar:
```
Before: [3, 6, 8, 10, 1, 2, 1]
After: [1, 1, 2, 3, 6, 8, 10]
```
(El `mod simple;` y `simple::run_simple();` parecen no estar relacionados—¿quizás un marcador de posición? Si hay un error allí, podría ser porque `simple` no está definido).

Si esto no aclara tus dudas o tienes una parte específica del código para ajustar/probar, ¡avísame!