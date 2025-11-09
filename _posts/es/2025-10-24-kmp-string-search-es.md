---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Algoritmo KMP Búsqueda Eficiente de Cadenas
translated: true
type: note
---

### Comprendiendo el Algoritmo Knuth-Morris-Pratt (KMP)

Tu intuición es correcta: KMP se trata de **no desperdiciar coincidencias parciales** durante la búsqueda de cadenas. Cuando buscas un patrón (como "abc") en un texto más largo (como "ababcabc"), el enfoque ingenuo reinicia desde cero cada vez que hay una falta de coincidencia, lo cual es ineficiente. KMP "recuerda" inteligentemente cuánto del patrón ya has coincidido y salta hacia adelante, evitando comparaciones redundantes. Esto lo hace súper rápido—tiempo lineal, O(n + m), donde n es la longitud del texto y m es la longitud del patrón.

Lo desglosaré paso a paso con un ejemplo simple. Buscaremos el patrón `P = "abab"` en el texto `T = "ababababc"`. (Aparece en las posiciones 0, 2 y 4).

#### Paso 1: El Problema y el Enfoque Ingenuo
- **Objetivo**: Encontrar todas las posiciones iniciales donde `P` coincide completamente en `T`.
- **Forma ingenua**: Deslizar `P` sobre `T`, comparando carácter por carácter. Si hay falta de coincidencia en la posición i en `P`, desplazar `P` por 1 y reintentar desde el principio de `P`.
  - Para nuestro ejemplo:
    - Empezar en T[0]: "a"=="a" (coincide), "b"=="b" (coincide), "a"=="a" (coincide), "b"=="b" (coincide) → Encontrado en 0.
    - Desplazar a T[1]: "b"=="a"? No → Reiniciar `P` al principio. ¡Desperdicio!
    - T[2]: "a"=="a", "b"=="b", "a"=="a", "b"=="b" → Encontrado en 2.
    - T[3]: "a"=="a", "b"=="b", "a"=="a", "b"=="a"? No → Reiniciar.
    - Y así sucesivamente. Mucho retroceso al carácter 0 de `P`.

Esto puede ser O(n*m) en el peor caso (ej., buscar "aaaaa...a" para "aaa...ab").

#### Paso 2: La Idea Clave de KMP – La Tabla de Prefijos (o "Función de Falla")
KMP precalcula una tabla `π` (pi) para el patrón `P`. Esta tabla te dice, para cada posición i en `P`, **el prefijo propio más largo de `P[0..i]` que también es un sufijo**. En otras palabras: "Si fallamos en coincidir aquí, ¿cuánto de la coincidencia parcial podemos reutilizar saltando a este prefijo superpuesto?"

- **Prefijo/sufijo propio**: Un prefijo/sufijo que no es la cadena completa (ej., para "aba", el prefijo "a" coincide con el sufijo "a").
- ¿Por qué? Te permite "deslizar" el patrón por más de 1 en caso de falta de coincidencia, reutilizando la superposición en lugar de reiniciar.

Para `P = "abab"`:
- Construir `π` paso a paso (lo codificaremos pronto).

| Posición i | P[0..i] | Prefijo propio más largo = sufijo | π[i] |
|------------|---------|-----------------------------------|------|
| 0          | "a"     | Ninguno (carácter único)          | 0    |
| 1          | "ab"    | Ninguno                           | 0    |
| 2          | "aba"   | "a" (prefijo "a" == sufijo "a")   | 1    |
| 3          | "abab"  | "ab" (prefijo "ab" == sufijo "ab")| 2    |

- π[2] = 1 significa: Si coincidiste "aba" pero fallas en el siguiente carácter, finge que has coincidido el prefijo "a" (longitud 1) hasta ahora.
- π[3] = 2 significa: Para "abab" completo, superposición de "ab".

#### Paso 3: Construyendo la Tabla de Prefijos (π)
Esto se hace en tiempo O(m). Es como buscar `P` contra sí mismo, usando una lógica similar.

Pseudocódigo:
```
def compute_prefix_function(P):
    m = len(P)
    pi = [0] * m
    k = 0  # Longitud de la coincidencia prefijo-sufijo actual
    for i in range(1, m):
        while k > 0 and P[k] != P[i]:
            k = pi[k-1]  # Saltar a la superposición anterior (¡reutilizar!)
        if P[k] == P[i]:
            k += 1
        pi[i] = k
    return pi
```

- Empezar con π[0] = 0.
- Para cada i=1 a m-1:
  - Intentar extender la longitud de coincidencia actual k.
  - Si hay falta de coincidencia, retroceder a π[k-1] (no desperdiciar—reutilizar superposición previa).
  - Si coincide, k++.

Para "abab":
- i=1: P[0]='a' != P[1]='b' → k=0, π[1]=0.
- i=2: P[0]='a' == P[2]='a' → k=1, π[2]=1.
- i=3: P[1]='b' == P[3]='b' → k=2, π[3]=2.

#### Paso 4: Buscando con la Tabla de Prefijos
Ahora buscar `T` con `P` y `π`:
- Mantener una variable `q` = estado actual (longitud del prefijo coincidido hasta ahora).
- Para cada carácter en `T`:
  - Mientras haya falta de coincidencia y q>0, establecer q = π[q-1] (saltar hacia atrás inteligentemente).
  - Si coincide, q++.
  - Si q == m, ¡encontrado! Luego q = π[q-1] para continuar por superposiciones.

Pseudocódigo:
```
def kmp_search(T, P):
    n, m = len(T), len(P)
    if m == 0: return []
    pi = compute_prefix_function(P)
    q = 0
    matches = []
    for i in range(n):
        while q > 0 and P[q] != T[i]:
            q = pi[q-1]
        if P[q] == T[i]:
            q += 1
        if q == m:
            matches.append(i - m + 1)  # Posición inicial
            q = pi[q-1]  # Superposición para la siguiente búsqueda
    return matches
```

Para `T = "ababababc"`, `P = "abab"`:
- i=0: 'a'=='a' → q=1
- i=1: 'b'=='b' → q=2
- i=2: 'a'=='a' → q=3
- i=3: 'b'=='b' → q=4 == m → Coincidencia en 0, q=π[3]=2
- i=4: Ahora q=2, T[4]='a' == P[2]='a' → q=3
- i=5: 'b'=='b' → q=4 == m → Coincidencia en 2, q=2
- i=6: q=2, 'a'=='a' → q=3
- i=7: q=3, 'b' == P[3]='b' → q=4 == m → Coincidencia en 4, q=2
- i=8: q=2, 'c' != P[2]='a' → q = π[1]=0; luego 'c' != P[0]='a' → q=0
- Coincidencias encontradas en [0, 2, 4].

¿Ves? En faltas de coincidencia (como si hubiera una), salta q=π[q-1] en lugar de q=0.

#### Por Qué Parece Mágico
- No hay retroceso en `T`—solo te mueves hacia adelante.
- El bucle "while" para faltas de coincidencia se ejecuta un total de O(1) veces amortizado, porque cada salto disminuye q, y q aumenta como máximo n veces.

#### Pruébalo Tú Mismo: Código Python Simple
```python
def compute_prefix_function(P):
    m = len(P)
    pi = [0] * m
    k = 0
    for i in range(1, m):
        while k > 0 and P[k] != P[i]:
            k = pi[k - 1]
        if P[k] == P[i]:
            k += 1
        pi[i] = k
    return pi

def kmp_search(T, P):
    n, m = len(T), len(P)
    if m == 0: return []
    pi = compute_prefix_function(P)
    q = 0
    matches = []
    for i in range(n):
        while q > 0 and P[q] != T[i]:
            q = pi[q - 1]
        if P[q] == T[i]:
            q += 1
        if q == m:
            matches.append(i - m + 1)
            q = pi[q - 1]
    return matches

# Prueba
T = "ababababc"
P = "abab"
print(kmp_search(T, P))  # Salida: [0, 2, 4]
```

Ejecuta esto—modifica P/T para ver los saltos en acción (añade impresiones para q).

#### Errores Comunes y Consejos
- π[0] siempre es 0.
- Para patrones sin auto-superposiciones (ej., "abc"), π es todo 0s—vuelve al modo ingenuo.
- Genial para secuencias de ADN o autocompletado de código.
- Si aún no está claro, visualiza π como una "máquina de estados": cada estado es la longitud coincidida, transiciones por coincidencia/falta de coincidencia.

Esto debería hacer clic ahora—es solo saltos inteligentes mediante superposiciones precalculadas. Si tienes un ejemplo específico que te está confundiendo, ¡compártelo!

[GeeksforGeeks: KMP Algorithm](https://www.geeksforgeeks.org/dsa/kmp-algorithm-for-pattern-searching/)  
[Wikipedia: Knuth–Morris–Pratt Algorithm](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm)