---
audio: false
generated: true
lang: es
layout: post
title: Codeforces 2108F
translated: true
type: note
---

Adentrémonos en por qué el código Java proporcionado resuelve el problema de las "Torres Caídas". El problema involucra un arreglo de \\( n \\) torres, cada una con una altura \\( a_i \geq 0 \\). Puedes derribar la torre en la posición \\( i \\), lo que aumenta las alturas de las siguientes \\( a_i \\) torres en 1 (o menos si no quedan suficientes torres), y luego establece \\( a_i \\) a 0. El objetivo es derribar todas las \\( n \\) torres exactamente una vez en cualquier orden, asegurando que el arreglo final sea no decreciente (es decir, para cualquier \\( i < j \\), la altura en la posición \\( i \\) es como máximo la altura en la posición \\( j \\)). La salida es el MEX máximo del arreglo final, donde el MEX es el entero no negativo más pequeño no presente en el arreglo.

---

### Análisis del Problema

1. **Definición de la Operación**:
   - Derribar la torre \\( i \\) con altura \\( a_i \\):
     - Aumenta las alturas de las torres en las posiciones \\( i+1, i+2, \dots, i+a_i \\) en 1 (si existen).
     - Establece \\( a_i = 0 \\).
   - Cada torre debe ser derribada exactamente una vez, en cualquier orden.
   - Si \\( a_i = 0 \\), derribar la torre \\( i \\) no tiene efecto en otras torres.

2. **Arreglo Final No Decreciente**:
   - Después de todas las operaciones, el arreglo final \\( b_1, b_2, \dots, b_n \\) debe satisfacer \\( b_i \leq b_{i+1} \\) para todo \\( i < n \\).

3. **MEX**:
   - El MEX del arreglo final es el entero no negativo más pequeño \\( m \\) no presente en \\( \{b_1, b_2, \dots, b_n\} \\).
   - Dado que el arreglo es no decreciente, si el arreglo contiene los valores \\( 0, 1, 2, \dots, k-1 \\) (posiblemente con repeticiones) pero no \\( k \\), el MEX es \\( k \\).
   - El objetivo es maximizar este MEX.

4. **Interpretación del MEX**:
   - Para que el MEX sea \\( m \\), el arreglo final debe incluir todos los enteros desde 0 hasta \\( m-1 \\) al menos una vez, y \\( m \\) no debe aparecer.
   - Dado que el arreglo es no decreciente, lograr un MEX de \\( m \\) implica que el arreglo final tiene valores como \\( 0, 0, \dots, 1, 1, \dots, m-1, m-1 \\), con cada entero de 0 a \\( m-1 \\) apareciendo al menos una vez, y ningún valor \\( m \\) o superior.

5. **Perspicacia Clave**:
   - El MEX \\( m \\) corresponde a tener al menos una posición con cada valor de 0 a \\( m-1 \\).
   - Equivalentemente, para un MEX de \\( m \\), necesitamos al menos \\( m \\) posiciones en el arreglo final tales que la posición \\( i \\) tenga un valor de al menos \\( i - (n - m) \\), porque:
     - Las últimas \\( m \\) posiciones (del índice \\( n-m+1 \\) a \\( n \\)) deben cubrir los valores 0 a \\( m-1 \\).
     - La posición \\( n-m+1 \\) debe tener un valor de al menos 0, la posición \\( n-m+2 \\) al menos 1, ..., la posición \\( n \\) al menos \\( m-1 \\).
   - Esto se traduce en requerir que la altura final en la posición \\( i \\) sea al menos \\( \max(0, m - (n - i + 1)) = \max(0, m - n + i) \\).

---

### Enfoque de la Solución

El código utiliza una búsqueda binaria para encontrar el MEX máximo posible \\( m \\). Para cada candidato \\( m \\), verifica si es posible lograr un arreglo final no decreciente donde cada posición \\( i \\) tenga una altura de al menos \\( \max(0, m - n + i) \\). Esto asegura que las últimas \\( m \\) posiciones puedan cubrir los valores 0 a \\( m-1 \\), haciendo que el MEX sea al menos \\( m \\).

#### Búsqueda Binaria
- **Rango**: El MEX \\( m \\) es al menos 0 (caso de arreglo vacío) y como máximo \\( n \\) (ya que necesitamos al menos \\( m \\) posiciones para tener los valores 0 a \\( m-1 \\)). Por lo tanto, busca \\( m \\) en \\( [0, n] \\).
- **Función de Verificación**: Para un \\( m \\) dado, determina si existe un orden para derribar las torres tal que el arreglo final satisfaga:
  - \\( b_i \geq \max(0, m - n + i) \\) para todo \\( i \\).
  - El arreglo es no decreciente.

#### Función de Verificación
La función de verificación simula si es posible lograr las alturas requeridas utilizando un enfoque de arreglo de diferencias, asumiendo que las torres pueden ser derribadas en cualquier orden.

1. **Alturas Requeridas**:
   - Para MEX \\( m \\), la posición \\( i \\) necesita una altura final \\( b_i \geq \text{need}_i \\), donde:
     \\[
     \text{need}_i = \max(0, m - n + i)
     \\]
   - Esto asegura que las posiciones \\( n-m+1 \\) a \\( n \\) tengan alturas de al menos 0, 1, ..., \\( m-1 \\), respectivamente.

2. **Arreglo de Diferencias**:
   - El código utiliza un arreglo de diferencias \\( d \\) para rastrear el efecto acumulativo de las operaciones.
   - Inicializa \\( d[i] = 0 \\) para todo \\( i \\).
   - Para cada posición \\( i \\):
     - Calcula la suma acumulada: \\( d[i] += d[i-1] \\) (si \\( i > 0 \\)), representando el número actual de bloques extra en la posición \\( i \\).
     - Verifica si \\( d[i] \geq \text{need}_i \\). Si no, es imposible lograr la altura requerida, por lo que retorna \\( false \\).
     - Calcula la longitud del rango afectado al derribar la torre \\( i \\):
       \\[
       \text{len} = d[i] - \text{need}_i + a_i
       \\]
       - \\( d[i] - \text{need}_i \\): Bloques extra disponibles después de cumplir con el requisito mínimo.
       - \\( a_i \\): El número de bloques contribuidos por la altura de la torre \\( i \\).
       - Esta \\( \text{len} \\) representa cuántas posiciones a la derecha de \\( i \\) pueden incrementarse cuando se derriba la torre \\( i \\).
     - Actualiza el arreglo de diferencias:
       - Incrementa \\( d[i+1] \\) (si \\( i+1 < n \\)) para iniciar el efecto de derribar la torre \\( i \\).
       - Decrementa \\( d[i + \text{len} + 1] \\) (si \\( i + \text{len} + 1 < n \\)) para terminar el efecto después de \\( \text{len} \\) posiciones.

3. **Factibilidad**:
   - El arreglo de diferencias simula el efecto de derribar la torre \\( i \\) con una altura modificada basada en el estado actual.
   - Si el bucle se completa sin retornar \\( false \\), es posible lograr las alturas requeridas para MEX \\( m \\).

4. **Por Qué Esto Funciona**:
   - La función de verificación no simula el orden real de las operaciones, sino que verifica si existe un orden que satisfaga los requisitos de altura.
   - El enfoque del arreglo de diferencias asegura que el número de bloques añadidos a cada posición sea consistente con alguna secuencia válida de operaciones.
   - La condición no decreciente se satisface implícitamente porque las alturas requeridas \\( \text{need}_i = \max(0, m - n + i) \\) son no decrecientes (a medida que \\( i \\) aumenta, \\( m - n + i \\) aumenta o permanece en 0).

#### Bucle Principal
- Lee el número de casos de prueba \\( t \\).
- Para cada caso de prueba:
  - Lee \\( n \\) y el arreglo \\( a \\).
  - Realiza una búsqueda binaria en \\( m \\) de 0 a \\( n \\).
  - Utiliza la función de verificación para determinar si el MEX \\( m \\) es alcanzable.
  - Actualiza \\( lo \\) (si es alcanzable) o \\( hi \\) (si no lo es).
- Imprime el \\( m \\) máximo (es decir, \\( lo \\)) para cada caso de prueba.

---

### Por Qué el Código Resuelve el Problema

1. **Corrección de la Búsqueda Binaria**:
   - La búsqueda binaria encuentra el \\( m \\) máximo tal que la función de verificación retorna \\( true \\).
   - Dado que la factibilidad del MEX \\( m \\) implica factibilidad para todos los valores de MEX más pequeños (un \\( m \\) más bajo requiere menos posiciones con alturas más bajas), la búsqueda binaria identifica correctamente el MEX máximo posible.

2. **Precisión de la Función de Verificación**:
   - La función de verificación asegura que cada posición \\( i \\) pueda tener al menos \\( \max(0, m - n + i) \\) bloques después de todas las operaciones.
   - El arreglo de diferencias simula el efecto acumulativo de derribar torres, teniendo en cuenta que cada torre contribuye \\( a_i \\) bloques a las siguientes \\( a_i \\) posiciones.
   - Al procesar las posiciones de izquierda a derecha y ajustar el arreglo de diferencias, verifica si las alturas iniciales \\( a_i \\) pueden redistribuirse para cumplir con las alturas requeridas.

3. **Manejo de la Restricción No Decreciente**:
   - Las alturas requeridas \\( \max(0, m - n + i) \\) son no decrecientes, lo que se alinea con el requisito del problema de un arreglo final no decreciente.
   - Si la función de verificación tiene éxito, el arreglo resultante puede hacerse no decreciente asegurando que cada posición cumpla o supere la altura requerida.

4. **Eficiencia**:
   - **Búsqueda Binaria**: \\( O(\log n) \\) iteraciones (ya que \\( m \leq n \\)).
   - **Función de Verificación**: \\( O(n) \\) por llamada, ya que procesa cada posición una vez y actualiza el arreglo de diferencias en tiempo constante por posición.
   - **Total por Caso de Prueba**: \\( O(n \log n) \\).
   - **Total para Todos los Casos de Prueba**: Dado que \\( \sum n \leq 10^5 \\), la complejidad general es \\( O(t \cdot n \log n) \\), que se ajusta al límite de tiempo de 3 segundos.

5. **Casos Límite**:
   - **\\( n = 1 \\)**: Si \\( a_1 = 0 \\), MEX = 1 (el arreglo se convierte en [0]). Si \\( a_1 > 0 \\), MEX = 0 (el arreglo se convierte en [0]). El código maneja esto correctamente.
   - **\\( a_i \\) grande**: Dado que \\( a_i \leq 10^9 \\), pero solo se ven afectadas las primeras \\( n-i \\) posiciones, el código limita correctamente el efecto usando los límites del arreglo.
   - **Todos \\( a_i = 0 \\)**: El arreglo final es todo ceros, MEX = 1. La función de verificación lo confirma.
   - **Valores mixtos**: La búsqueda binaria y la función de verificación manejan \\( a_i \geq 0 \\) arbitrarios.

---

### Detalles Específicos del Código Java

El código Java adapta la lógica de C++ usando `BufferedReader` y `PrintWriter` para E/S eficiente, como se solicitó. Aspectos clave:

1. **Manejo de Entrada**:
   - Utiliza `BufferedReader` para leer líneas y `StringTokenizer` para analizar enteros.
   - Lee \\( t \\), luego para cada caso de prueba, lee \\( n \\) y el arreglo \\( a \\).

2. **Clase Checker**:
   - Encapsula la lógica de verificación para imitar la función lambda de C++.
   - Utiliza un arreglo \\( d \\) para simular el enfoque del arreglo de diferencias.

3. **Salida**:
   - Utiliza `PrintWriter` para imprimir el resultado de cada caso de prueba, con `out.flush()` para asegurar que toda la salida se escriba.

4. **Rendimiento**:
   - El código Java mantiene la misma complejidad \\( O(n \log n) \\) por caso de prueba.
   - `BufferedReader` y `PrintWriter` aseguran que la E/S sea lo suficientemente rápida para \\( \sum n \leq 10^5 \\).

---

### Conclusión

El código resuelve el problema de las "Torres Caídas" mediante:
- El uso de búsqueda binaria para encontrar el MEX máximo \\( m \\).
- El empleo de una función de verificación basada en un arreglo de diferencias para verificar si las alturas iniciales de las torres pueden redistribuirse para lograr un arreglo no decreciente con las alturas requeridas.
- Asegurar la corrección mediante la naturaleza no decreciente de las alturas requeridas y la factibilidad de las secuencias de operaciones.
- Manejar todos los casos límite y ajustarse a las restricciones de tiempo y memoria.

La implementación en Java traduce fielmente la lógica de C++, utilizando E/S eficiente para cumplir con los requisitos del problema.