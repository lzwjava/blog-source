---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Ordenación Rápida Frente a Ordenación por Mezcla
translated: true
type: note
---

### Por qué Quick Sort parece complicado (y Merge Sort no)

Tienes razón: implementar Quick Sort desde cero sin referencias puede sentirse como luchar con un cerdo engrasado, mientras que Merge Sort es más como doblar la ropa: metódico y predecible. El flujo "dividir, conquistar, combinar" de Merge Sort es lineal y recursivo de manera limpia, sin sorpresas en el paso de fusión. Quick Sort, por otro lado, es *in-place* y se basa en un truco inteligente de partición que implica intercambiar elementos alrededor de un "pivote" (un punto de división elegido). Al principio parece caótico porque el pivote no está fijo—es más como un árbitro que se mezcla durante el juego. Pero una vez que captas la intuición, es elegantemente eficiente (promedio O(n log n), peor caso O(n²) si los pivotes son malos).

Permíteme presentar Quick Sort con una lente natural, como una historia: imagina ordenar una pila desordenada de libros en un estante por altura. En lugar de dividir la pila por la mitad, medir todo y fusionar (eso es Merge Sort), eliges un libro como "punto de referencia" (el pivote), luego reorganizas los demás para que todos los libros más cortos estén a su izquierda y los más altos a su derecha. El pivote termina en su posición *final*, y recursas solo en las sub-pilas izquierda y derecha. No se necesita espacio extra—solo intercambios en el estante. Es como la ceremonia holandesa de izar la bandera "quicksort" (de ahí el nombre), donde particionas en tres grupos: más cortos, referencia, más altos.

### Por qué funciona: La magia de la partición

Quick Sort funciona debido al **divide y vencerás con una garantía**: cada paso de partición coloca *al menos un elemento* (el pivote) en su posición final correcta, reduciendo el problema al menos en esa cantidad cada vez. En el mejor caso, el pivote divide el array de manera uniforme (como partir por la mitad en Merge Sort), lo que lleva a una recursión equilibrada. En el peor caso (por ejemplo, un array ya ordenado con mala elección de pivote), degenera a O(n²) como el bubble sort—pero las buenas elecciones de pivote lo hacen increíblemente rápido en la práctica.

La idea clave: **la partición impone invariantes**. Después de una partición:
- Todo a la izquierda del pivote ≤ pivote.
- Todo a la derecha del pivote ≥ pivote.
- El pivote ahora está ordenado para siempre—no es necesario tocarlo de nuevo.

Esto garantiza progreso: la profundidad del árbol de recursión es como máximo log n en promedio, y cada nivel hace un trabajo total de O(n) (escaneando e intercambiando).

### Cómo elegir el pivote (y por qué se "mueve" durante las comparaciones)

El pivote no es sagrado—es solo cualquier elemento que eliges como punto de referencia. Las malas elecciones (como siempre el primer elemento) pueden desequilibrar las cosas, así que aquí tienes una progresión natural de estrategias, de simple a robusta:

1. **Ingenuo: Elegir el primer (o último) elemento.**
   - Fácil de codificar, pero arriesgado. En un array ordenado `[1,2,3,4,5]`, pivote=1 significa que la izquierda está vacía, la derecha tiene 4 elementos—la recursión se sesga profundamente.
   - El "movimiento": Durante la partición, comparas todo lo demás con este valor de pivote, pero intercambias elementos *alrededor* de su posición. El pivote mismo se intercambia a su lugar a medida que los límites lo cruzan.

2. **Mejor: Elegir el elemento del medio.**
   - Lo intercambia al final temporalmente, lo usa como pivote. Más equilibrado intuitivamente (más cerca de la mediana), pero aún vulnerable a entradas ordenadas/inversamente ordenadas.

3. **Mejor para la práctica: Elegir un elemento aleatorio.**
   - Intercambiarlo al final, particionar. El azar promedia los casos malos, haciendo que el peor caso sea improbable (con alta probabilidad, sigue siendo O(n log n)). Esto es lo que usan la mayoría de las bibliotecas.

4. **Elegante (para entrevistas): Mediana de tres.**
   - Elegir la mediana de primero/medio/último como pivote. Rápido de calcular, esquiva los problemas comunes.

En código, a menudo "arreglas" el pivote intercambiándolo al final primero, particionas alrededor de su *valor* (no posición), luego lo intercambias de nuevo a donde pertenece. Por eso se siente que el pivote se "mueve"—no es estático; el proceso de partición encuentra dinámicamente su lugar a través de dos punteros (izquierda y derecha) que se acercan el uno al otro saltando, intercambiando infractores.

### Un ejemplo práctico: Ordenando [3, 7, 1, 9, 4] con el último elemento como pivote

Recorramos un paso de partición. Array: `[3, 7, 1, 9, 4]`. Pivote = último = 4. (Lo intercambiaremos según sea necesario).

- Comenzar con el puntero izquierdo en el índice 0 (valor 3), derecho en el índice 3 (valor 9, ya que el pivote está en 4).
- Escanear desde la izquierda: ¿3 < 4? Sí, déjalo. Siguiente, ¿7 > 4? Sí, pero espera—intercambiamos con el primer >4 desde la derecha.
- En realidad, partición Lomuto estándar (estilo de un solo puntero simple):
  1. i = -1 (límite para < pivote).
  2. Para j desde 0 hasta n-2 (saltar pivote):
     - Si arr[j] ≤ pivote (4), intercambiar arr[++i] con arr[j]. (Hacer crecer el lado izquierdo).
  3. Finalmente, intercambiar pivote con arr[++i] para colocarlo.

Paso a paso:
- j=0: ¿3 ≤4? Sí. i=0, intercambiar arr[0] con arr[0] (sin cambio). Array: [3,7,1,9,4]
- j=1: ¿7 ≤4? No. Saltar.
- j=2: ¿1 ≤4? Sí. i=1, intercambiar arr[1] (7) con arr[2] (1). Array: [3,1,7,9,4]
- j=3: ¿9 ≤4? No. Saltar.
- Fin: Intercambiar pivote (4 en índice 4) con arr[++i=2] (7). Array: [3,1,4,9,7]

Ahora: Izquierda de 4 (índice 2) es [3,1] (ambos ≤4, sin ordenar), derecha [9,7] (ambos ≥4, sin ordenar). Pivote=4 está *terminado*. Recursión en izquierda [3,1] y derecha [9,7].

- Izquierda: Pivote=1, particiona a [1,3].
- Derecha: Pivote=7, particiona a [7,9].

Orden completo: [1,3,4,7,9]. ¿Ves? Cada paso asegura el progreso, y los intercambios "mueven" el pivote a casa.

### Esquema de pseudocódigo (para facilitar la implementación)

```
quicksort(arr, low, high):
    if low < high:
        pivot_idx = partition(arr, low, high)
        quicksort(arr, low, pivot_idx-1)
        quicksort(arr, pivot_idx+1, high)

partition(arr, low, high):  # Estilo Lomuto, pivote en high
    pivot = arr[high]
    i = low - 1
    for j in low to high-1:
        if arr[j] <= pivot:
            i += 1
            swap arr[i], arr[j]
    swap arr[i+1], arr[high]
    return i+1
```

El "movimiento" ocurre en esos intercambios: los elementos bailan unos alrededor de otros hasta que el pivote se establece. Practica en papel con 5-6 elementos—una vez que la partición haga clic, la recursión se sentirá natural. Si tienes problemas, intenta animarlo mentalmente como ese estante para ordenar libros.

Para inmersiones más profundas:  
[Visualización de Quick Sort](https://visualgo.net/en/sorting?slide=9)  
[Capítulo de CLRS sobre Quicksort](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-20.html#%_sec_3.3)