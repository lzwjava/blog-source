---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Definición del Adjunto y Relación con el Cofactor
translated: true
type: note
---

### Aclarando la definición del adjunto (y su relación con los cofactores)

Vas por buen camino en cuanto a cómo se construye el adjunto mediante cofactores, pero hay una pequeña pero importante corrección en tu descripción. La matriz adjunta (a menudo denotada como `adj(A)`) no se construye multiplicando la entrada original `a(i,j)` por el determinante con signo del "resto" (la submatriz después de eliminar la fila i y la columna j). En su lugar:

- El **cofactor** `C_ij` de la entrada `a(i,j)` se define como `C_ij = (-1)^{i+j} * det(M_ij)`, donde `M_ij` es la submatriz obtenida al eliminar la fila i y la columna j de A. Esto es puramente el **menor con signo**—no hay multiplicación por `a(i,j)` misma.
- La **matriz de cofactores** C tiene estos `C_ij` como sus entradas.
- El **adjunto** es la **transpuesta** de la matriz de cofactores: `adj(A) = C^T`. Por lo tanto, la entrada en la posición (i,j) de `adj(A)` es en realidad `C_ji` (el cofactor de los índices intercambiados).

Esta configuración del menor con signo proviene de la expansión de Laplace para calcular determinantes (más sobre esto a continuación). Tu descripción suena un poco a la fórmula del determinante mismo: `det(A) = suma sobre j de a(i,j) * C_ij` (a lo largo de cualquier fila i), que *sí* implica multiplicar por `a(i,j)`. Pero el adjunto omite esa multiplicación—es solo la colección de esos menores con signo, transpuestos, para permitir identidades algebraicas ordenadas.

Para un ejemplo rápido de 2x2 para ilustrar (digamos A = [[a, b], [c, d]]):
- Cofactores: C_11 = (-1)^{1+1} det([d]) = d; C_12 = (-1)^{1+2} det([c]) = -c; C_21 = (-1)^{2+1} det([b]) = -b; C_22 = (-1)^{2+2} det([a]) = a.
- Matriz de cofactores C = [[d, -c], [-b, a]].
- Adjunto adj(A) = C^T = [[d, -b], [-c, a]].
- Observa que no hay multiplicadores originales de a, b, c, d en los cofactores—todo se trata de las submatrices del "resto".

Sí, así es exactamente como se calcula el adjunto: eliminar fila/columna para cada posición, tomar el det del resto, aplicar el signo `(-1)^{i+j}`, ensamblar en C, luego transponer para obtener adj(A). Es recursivo (los menores obtienen matrices más pequeñas), por lo que para matrices grandes de n x n, es computacionalmente intensivo—por eso a menudo usamos la eliminación gaussiana para inversas en la práctica.

### ¿Por qué necesitamos el adjunto? (Es más que solo un paso intermedio)

Tienes razón en que parece una "presentación intermedia" para la inversión de matrices—y en muchos sentidos computacionales, ¡lo es! La fórmula clave es `A^{-1} = (1 / det(A)) * adj(A)`, asumiendo que det(A) ≠ 0. Esto da directamente la inversa usando solo determinantes de submatrices, sin necesidad de operaciones de fila. Pero no es *solo* un peldaño; he aquí por qué es útil y necesario:

1. **Fórmula de Inversión de Matrices**: Para matrices pequeñas o computación simbólica (por ejemplo, en demostraciones o aritmética exacta), esta es una forma limpia y explícita de expresar la inversa. Destaca cómo la inversa se "descompone" en cofactores escalados.

2. **Perspectivas Teóricas**: La identidad `A * adj(A) = adj(A) * A = det(A) * I` (donde I es la matriz identidad) revela una estructura profunda. Muestra que toda matriz conmuta con su adjunta hasta un escalar, y es la base para comprender las matrices singulares (det(A)=0 implica A adj(A)=0, por lo que los espacios nulos se alinean).

3. **Regla de Cramer para Sistemas Lineales**: Para resolver Ax = b, la i-ésima entrada de la solución es `x_i = det(A_i) / det(A)`, donde A_i reemplaza la columna i de A con b. Pero det(A_i) se expande mediante cofactores que involucran entradas de b—esencialmente aprovechando el adjunto en segundo plano para un cálculo eficiente sin inversión completa.

4. **Expansiones de Determinantes**: Los cofactores permiten la expansión de Laplace (tu idea de "det(resto)"), que es crucial para calcular det(A) dividiéndolo en problemas más pequeños. Históricamente, esto hizo que los determinantes fueran manejables antes de las computadoras.

5. **Aplicaciones más Amplias**: En geometría proyectiva, gráficos por computadora (transformaciones) e incluso física (por ejemplo, matrices de impedancia), los adjuntos aparecen para manejar singularidades o derivar inversas en anillos más allá de los reales (como polinomios).

En resumen, mientras que la reducción de filas es más rápida para cálculos numéricos, el adjunto proporciona un camino "analítico" que es elegante para la teoría, la educación y los casos donde se necesitan fórmulas explícitas. Es como el "por qué" detrás de la inversa, no solo un medio para un fin.

### ¿Cómo se inventó el adjunto? (Un poco de historia)

El adjunto no surgió de un momento "eureka"—es un crecimiento natural del trabajo de los siglos XVIII-XIX sobre determinantes y ecuaciones lineales, cuando las matrices aún no estaban formalizadas (el término "matriz" llegó en 1850). No se atribuye a un solo inventor, pero aquí está la trayectoria:

- **Raíces en los Determinantes (Finales de 1600–1700)**: Los determinantes surgieron de resolver sistemas lineales (por ejemplo, Leibniz en 1693 para casos 2x2). Para el siglo XVIII, matemáticos como Cramer (1750) usaban expansiones de menores para soluciones, tocando implícitamente los cofactores.

- **Conceptos Tempranos de "Adjunto" (1760–1800)**: Joseph-Louis Lagrange acuñó "ecuaciones adjuntas" alrededor de 1766 para ecuaciones diferenciales, donde un operador "adjunto" refleja el original (como la transpuesta para matrices). Arthur Cayley (1840–50) extendió esto a "formas lineales adjuntas" en su trabajo con matrices. Maxime Bocher formalizó "matriz adjunta" a principios del siglo XX, pero la idea central es anterior a él.

- **La Idea Clave de Gauss (1801)**: Carl Friedrich Gauss, en sus *Disquisitiones Arithmeticae*, definió un "adjunto" para formas cuadráticas (por ejemplo, ax² + 2bxy + cy²). Construyó una forma compañera cuyos coeficientes son esencialmente los menores 2x2 con signo de la matriz simétrica que representa la original—precisamente el adjunto (hasta convenciones de signo). Esto fue para teoría de números (formas cuadráticas binarias), pero anticipa directamente la definición moderna. El trabajo de Gauss hizo que la construcción fuera sistemática.

- **Formalización (Mediados del siglo XIX en adelante)**: A medida que la teoría de matrices se solidificó (Cayley, Sylvester, Kronecker), la expansión por cofactores (de Laplace, 1772) se fusionó con estas ideas. Para la década de 1850–60, la fórmula completa de la inversa `A^{-1} = adj(A)/det(A)` apareció en textos, con "adjunto" (del latín "adjugare", unir en yugo) enfatizando su papel vinculante en la inversión.

La "invención" probablemente surgió de detectar patrones: mientras expandían determinantes, los matemáticos notaron que las colecciones de cofactores "invierten" la matriz cuando se escalan. Fue menos un destello de genialidad y más una evolución orgánica de resolver ecuaciones a mano. Los textos modernos (por ejemplo, *Introduction to Linear Algebra* de Strang) aún lo enseñan de esta manera para la intuición.

Si deseas ejemplos en código (por ejemplo, Python vía NumPy/SymPy para calcular uno) o una inmersión más profunda en la construcción de Gauss, ¡solo dilo!

[Adjugate matrix - Wikipedia](https://en.wikipedia.org/wiki/Adjugate_matrix)  
[First usage of "adjoint" - History of Science and Mathematics Stack Exchange](https://hsm.stackexchange.com/questions/5908/what-is-the-first-usage-of-the-term-adjoint-and-why-was-this-word-chosen)