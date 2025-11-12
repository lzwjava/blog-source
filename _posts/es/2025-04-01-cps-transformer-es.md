---
audio: false
generated: true
lang: es
layout: post
title: Transformador de CPS
translated: true
type: note
---

```scheme
;; Un transformador CPS simple que maneja correctamente las llamadas de cola y no
;; duplica contextos para expresiones if.
;; autor: Yin Wang (yw21@cs.indiana.edu)
(load "pmatch.scm") ; Carga una biblioteca de coincidencia de patrones para Scheme, facilitando el manejo de diferentes estructuras de expresión.

(define cps
  (lambda (exp)
    (letrec
        ([trivial? (lambda (x) (memq x '(zero? add1 sub1)))] ; Comprueba si un símbolo dado es uno de los operadores primitivos: zero?, add1, sub1. Estos se tratan de forma especial en la transformación.
         [id (lambda (v) v)] ; La función identidad, utilizada como continuación inicial para la expresión de nivel superior.
         [ctx0 (lambda (v) `(k ,v))]      ; contexto de cola. Crea una continuación que simplemente aplica la continuación actual 'k' a un valor 'v'. Se utiliza cuando la llamada actual está en posición de cola.
         [fv (let ([n -1]) ; Crea un generador para nombres de variables frescas.
               (lambda ()
                 (set! n (+ 1 n))
                 (string->symbol (string-append "v" (number->string n)))))]
         [cps1
          (lambda (exp ctx) ; La función recursiva central que realiza la transformación CPS. Toma una expresión 'exp' y una continuación 'ctx' como argumentos. La continuación representa qué hacer con el resultado de evaluar 'exp'.
            (pmatch exp ; Utiliza coincidencia de patrones para analizar la estructura de la expresión.
              [,x (guard (not (pair? x))) (ctx x)] ; Caso base: Si la expresión 'x' no es un par (es decir, es un literal o una variable), significa que ya es un valor. Aplica la continuación actual 'ctx' a este valor.

              [(if ,test ,conseq ,alt) ; Coincide con una expresión 'if' con un test, un consecuente y una alternativa.
               (cps1 test ; Transforma recursivamente la expresión 'test'.
                     (lambda (t) ; La continuación para la expresión 'test'. Toma el resultado del test (que será un valor booleano) como 't'.
                       (cond
                        [(memq ctx (list ctx0 id)) ; Si el contexto actual 'ctx' es el contexto de cola 'ctx0' o el contexto de identidad inicial 'id', significa que la expresión 'if' en sí está en posición de cola.
                         `(if ,t ,(cps1 conseq ctx) ,(cps1 alt ctx))] ; En este caso, la expresión 'if' permanece como una expresión 'if' en el código CPS. El consecuente y la alternativa se transforman a CPS con el mismo contexto 'ctx'. Esto evita duplicar contextos.
                        [else ; Si el contexto actual no es un contexto de cola, significa que el resultado de la expresión 'if' necesita pasarse a algún cálculo posterior.
                         (let ([u (fv)]) ; Genera un nombre de variable fresco 'u' para contener el resultado de la expresión 'if'.
                           `(let ([k (lambda (,u) ,(ctx u))]) ; Crea una nueva continuación 'k' que toma el resultado 'u' y aplica el contexto original 'ctx' a él.
                              (if ,t ,(cps1 conseq ctx0) ,(cps1 alt ctx0))))])))] ; La expresión 'if' se envuelve en un 'let' que introduce la nueva continuación 'k'. El consecuente y la alternativa se transforman a CPS con el contexto de cola 'ctx0', ya que sus resultados se pasarán inmediatamente a 'k'.

              [(lambda (,x) ,body) ; Coincide con una expresión lambda con un único argumento 'x' y un cuerpo.
               (ctx `(lambda (,x k) ,(cps1 body ctx0)))] ; La expresión lambda se transforma en una nueva expresión lambda que toma un argumento adicional 'k' (la continuación). El cuerpo de la lambda original se transforma a CPS con el contexto de cola 'ctx0', ya que su resultado se pasará a esta continuación 'k'.

              [(,op ,a ,b) ; Coincide con una expresión con un operador binario 'op' y dos operandos 'a' y 'b'.
               (cps1 a ; Transforma recursivamente el primer operando 'a'.
                     (lambda (v1) ; La continuación para 'a'. Toma el resultado 'v1'.
                       (cps1 b ; Transforma recursivamente el segundo operando 'b'.
                             (lambda (v2) ; La continuación para 'b'. Toma el resultado 'v2'.
                                   (ctx `(,op ,v1 ,v2))))))] ; Aplica el contexto original 'ctx' a la expresión formada por el operador 'op' y los resultados transformados de los operandos 'v1' y 'v2'.

              [(,rator ,rand) ; Coincide con una aplicación de función con un rator (la función) y un rand (el argumento).
               (cps1 rator ; Transforma recursivamente el rator.
                     (lambda (r) ; La continuación para el rator. Toma el resultado 'r' (la función).
                       (cps1 rand ; Transforma recursivamente el operando.
                             (lambda (d) ; La continuación para el operando. Toma el resultado 'd' (el argumento).
                               (cond
                                [(trivial? r) (ctx `(,r ,d))] ; Si el rator 'r' es un operador trivial (como zero?, add1, sub1), aplica el contexto actual 'ctx' a la aplicación del operador al operando.
                                [(eq? ctx ctx0) `(,r ,d k)]  ; llamada de cola. Si el contexto actual es el contexto de cola 'ctx0', significa que esta aplicación de función está en posición de cola. La función CPS 'r' se llama con el argumento CPS 'd' y la continuación actual 'k'.
                                [else ; Si la aplicación de función no está en posición de cola.
                                 (let ([u (fv)]) ; Genera un nombre de variable fresco 'u' para el resultado.
                                   `(,r ,d (lambda (,u) ,(ctx u))))])))))]))]) ; La función CPS 'r' se llama con el argumento CPS 'd' y una nueva continuación que toma el resultado 'u' y aplica el contexto original 'ctx' a él.

      (cps1 exp id))));; Inicia la transformación CPS llamando a 'cps1' con la expresión de entrada 'exp' y la continuación identidad inicial 'id'.

;;; pruebas
;; var
(cps 'x) ; Transforma la variable 'x'. El resultado será '(k x)' porque el contexto inicial es 'id', y 'id' se aplica a 'x'.

(cps '(lambda (x) x)) ; Transforma una función lambda identidad simple. El resultado será '(lambda (x k) (k x))'.

(cps '(lambda (x) (x 1))) ; Transforma una función lambda que aplica su argumento a 1. El resultado será '(lambda (x k) (x 1 k))'.

;; sin lambda (generará funciones identidad para retornar al nivel superior)
(cps '(if (f x) a b)) ; Transforma una expresión if donde el test es una llamada a función.

(cps '(if x (f a) b)) ; Transforma una expresión if donde el test es una variable.

;; if independiente (cola)
(cps '(if x (f a) b)) ; Aquí, el 'if' está en el nivel superior, por lo que está en contexto de cola.

;; if dentro de test-if (no cola)
(cps '(lambda (x) (if (f x) a b))) ; El 'if' está dentro de una lambda, y su resultado es utilizado por la lambda (retornado implícitamente), por lo que no está en contexto de cola.

(cps '(lambda (x) (if (if x (f a) b) c d))) ; Expresiones 'if' anidadas. El 'if' interno está en el test del 'if' externo.

;; ambas ramas son triviales, debería hacer algunas optimizaciones más
(cps '(lambda (x) (if (if x (zero? a) b) c d)))

;; if dentro de rama-if (cola)
(cps '(lambda (x) (if t (if x (f a) b) c))) ; El 'if' interno está en la rama consecuente del 'if' externo. Si el 'if' externo está en contexto de cola, el interno también lo estará.

;; if dentro de rama-if, pero nuevamente dentro de otro test-if (no cola)
(cps '(lambda (x) (if (if t (if x (f a) b) c) e w)))

;; if como operando (no cola)
(cps '(lambda (x) (h (if x (f a) b)))) ; El resultado de la expresión 'if' se utiliza como argumento para 'h'.

;; if como operador (no cola)
(cps '(lambda (x) ((if x (f g) h) c))) ; El resultado de la expresión 'if' se utiliza como la función a llamar.

;; por qué necesitamos más de dos nombres
(cps '(((f a) (g b)) ((f c) (g d)))) ; Este ejemplo probablemente demuestra la necesidad del generador de nombres de variables frescas ('fv') para evitar conflictos de nombres al transformar expresiones anidadas complejas.

;; factorial
(define fact-cps
  (cps
   '(lambda (n)
      ((lambda (fact)
         ((fact fact) n))
       (lambda (fact)
         (lambda (n)
           (if (zero? n)
               1
               (* n ((fact fact) (sub1 n))))))))));; imprime la función CPS

(pretty-print fact-cps);; =>
;; '(lambda (n k)
;;    ((lambda (fact k) (fact fact (lambda (v0) (v0 n k))))
;;     (lambda (fact k)
;;       (k
;;        (lambda (n k)
;;          (if (zero? n)
;;            (k 1)
;;            (fact
;;             fact
;;             (lambda (v1) (v1 (sub1 n) (lambda (v2) (k (* n v2))))))))));
;;     k))

((eval fact-cps) 5 (lambda (v) v));; => 120
```

**Explicación del Transformador CPS:**

Este código Scheme implementa una transformación de Estilo de Paso de Continuaciones (CPS) para un subconjunto simple del lenguaje Scheme. Aquí hay un desglose de los conceptos clave y cómo funciona el código:

**1. Estilo de Paso de Continuaciones (CPS):**

* En CPS, una función no retorna un valor directamente. En su lugar, toma un argumento extra llamado **continuación**.
* La continuación es una función que representa el resto del cómputo a realizar con el resultado de la función actual.
* Cuando una función CPS termina su cómputo, llama a la continuación con el resultado.

**¿Por qué usar CPS?**

* **Flujo de Control Explícito:** CPS hace explícito el flujo de control. Las llamadas y retornos de funciones se reemplazan por llamadas a continuaciones.
* **Optimización de Llamadas de Cola:** CPS permite una implementación fácil de la optimización correcta de llamadas de cola. En el código transformado, las llamadas a funciones en posición de cola se convierten en la última operación, permitiendo una ejecución eficiente sin aumentar la profundidad de la pila.
* **Implementar Estructuras de Control Avanzadas:** CPS puede usarse como una representación intermedia en compiladores para implementar características como excepciones, corrutinas y backtracking.

**2. La Función `cps`:**

* El punto de entrada principal para la transformación. Toma una expresión `exp` como entrada.
* Utiliza `letrec` para definir varias funciones auxiliares mutuamente recursivas.
* Inicializa la transformación llamando a `cps1` con la expresión de entrada y la función identidad `id` como la continuación inicial. Esto significa que el resultado final de la expresión transformada se retornará directamente.

**3. Funciones Auxiliares:**

* **`trivial?`:** Identifica operadores primitivos como `zero?`, `add1` y `sub1`. Estos se manejan de forma especial en la transformación.
* **`id`:** La función identidad `(lambda (v) v)`. Es la continuación inicial, que significa "simplemente retorna el valor".
* **`ctx0`:** Crea un "contexto de cola". Dado un valor `v`, retorna `(k v)`, donde `k` es la continuación actual. Esto significa que el cómputo actual está en posición de cola, y el resultado debe pasarse directamente a la continuación que espera.
* **`fv`:** Genera nombres de variables frescos (por ejemplo, `v0`, `v1`, `v2`, ...). Esto es crucial para evitar la captura de variables al introducir nuevas continuaciones.

**4. La Función `cps1` (La Transformación Central):**

* Esta función recorre recursivamente la expresión de entrada y la transforma a CPS.
* Toma dos argumentos: la expresión `exp` a transformar y la continuación actual `ctx`.
* Utiliza la biblioteca `pmatch` para coincidencia de patrones para manejar diferentes tipos de expresiones:

    * **Literales y Variables:** Si la expresión no es un par (un literal o una variable), ya es un valor. La continuación actual `ctx` se aplica a este valor: `(ctx x)`.

    * **Expresiones `if`:** Esta es una parte clave del transformador que maneja llamadas de cola y evita la duplicación de contexto.
        * Primero transforma la expresión `test` con una continuación que toma el resultado del test (`t`).
        * Si el contexto actual `ctx` es un contexto de cola (`ctx0`) o el contexto de identidad inicial (`id`), significa que la expresión `if` en sí está en posición de cola. En este caso, se preserva la estructura `if`, y las ramas `conseq` y `alt` se transforman a CPS con el mismo contexto `ctx`.
        * Si el contexto actual no es un contexto de cola, significa que el resultado de la expresión `if` se usará más tarde. Se crea una nueva continuación `k` que toma el resultado del `if` y aplica el contexto original `ctx` a él. Las ramas `conseq` y `alt` se transforman entonces a CPS con el contexto de cola `ctx0`, y toda la expresión `if` se envuelve en un `let` que introduce `k`.

    * **Expresiones `lambda`:** Una expresión `lambda` `(lambda (x) body)` se transforma en una nueva expresión `lambda` que toma un argumento adicional `k` (la continuación): `(lambda (x k) (cps1 body ctx0))`. El cuerpo de la lambda original se transforma a CPS con el contexto de cola `ctx0`.

    * **Operaciones Binarias (`op a b`):** Los operandos `a` y `b` se transforman a CPS secuencialmente. La continuación para `a` toma su resultado `v1`, y luego transforma `b` a CPS con una continuación que toma su resultado `v2`. Finalmente, el contexto original `ctx` se aplica a la expresión formada por el operador `op` y los resultados transformados `v1` y `v2`.

    * **Aplicaciones de Función (`rator rand`):** El `rator` (función) y el `rand` (argumento) se transforman a CPS secuencialmente.
        * Si el `rator` es un operador `trivial?`, el contexto actual `ctx` se aplica directamente al resultado de aplicar el operador al operando.
        * Si el contexto actual es un contexto de cola (`ctx0`), la función CPS `r` se llama con el argumento CPS `d` y la continuación actual `k`. Esto asegura llamadas de cola correctas.
        * En caso contrario (llamada no de cola), se crea una nueva continuación que toma el resultado de la llamada a función y aplica el contexto original `ctx` a él. La función CPS `r` se llama con el argumento CPS `d` y esta nueva continuación.

**5. Pruebas:**

* El código incluye varios casos de prueba que demuestran la transformación de diferentes tipos de expresiones, incluyendo variables, funciones lambda, expresiones `if` en varios contextos y aplicaciones de función.

**6. Ejemplo de Factorial:**

* La definición `fact-cps` muestra cómo se puede aplicar el transformador CPS a una función factorial recursiva.
* La salida `pretty-print` muestra la versión CPS de la función factorial, que ahora toma un argumento de continuación extra `k`.
* La última línea evalúa la función factorial CPS con la entrada `5` y una continuación de nivel superior `(lambda (v) v)` que simplemente retorna el valor final.

**En resumen, este código implementa una transformación CPS que pretende:**

* Convertir expresiones a estilo de paso de continuaciones.
* Asegurar la optimización correcta de llamadas de cola pasando la continuación actual explícitamente.
* Manejar expresiones `if` eficientemente sin duplicar el contexto circundante cuando el `if` en sí está en posición de cola. Esto se logra manteniendo la estructura `if` y transformando las ramas a CPS con el mismo contexto. Cuando el `if` no está en posición de cola, introduce una nueva continuación para manejar el resultado.