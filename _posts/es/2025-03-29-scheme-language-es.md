---
audio: false
generated: true
lang: es
layout: post
title: Tutorial de Programación en Scheme
translated: true
type: note
---

Scheme es un dialecto minimalista de Lisp conocido por su simplicidad y elegancia. Este tutorial cubrirá los conceptos básicos para que puedas comenzar.

## 1. Sintaxis y Conceptos Básicos

### Ejecutando Scheme
- Necesitarás un intérprete de Scheme (como Racket, Guile o Chez Scheme)
- El código se escribe típicamente en un archivo `.scm` o se introduce en un REPL (Read-Eval-Print Loop)

### Expresiones y Paréntesis
- Todo en Scheme es una expresión que devuelve un valor
- Los paréntesis se usan para llamadas a funciones y agrupación
- Formato: `(función arg1 arg2 ...)`

## 2. Tipos de Datos Básicos

```scheme
; Números
42          ; Entero
3.14        ; Punto flotante
1/2         ; Racional

; Booleanos
#t          ; Verdadero
#f         ; Falso

; Cadenas
"hello"     ; Literal de cadena

; Símbolos
'hello      ; Símbolo (citado con ')
```

## 3. Operaciones Básicas

```scheme
; Aritmética
(+ 2 3)        ; 5
(- 10 4)       ; 6
(* 3 4)        ; 12
(/ 15 3)       ; 5

; Comparaciones
(= 5 5)        ; #t
(< 3 7)        ; #t
(> 10 5)       ; #t
```

## 4. Definiendo Variables

```scheme
; Define una variable global
(define x 10)

; Usa la variable
(+ x 5)        ; 15
```

## 5. Funciones

### Definiendo Funciones
```scheme
; Definición básica de función
(define square
  (lambda (x)    ; lambda crea una función anónima
    (* x x)))

(square 4)     ; 16
```

### Múltiples Parámetros
```scheme
(define add
  (lambda (x y)
    (+ x y)))

(add 3 5)      ; 8
```

### Definición Abreviada
```scheme
; Sintaxis alternativa (azúcar sintáctico)
(define (multiply x y)
  (* x y))

(multiply 2 3) ; 6
```

## 6. Condicionales

### Sentencia If
```scheme
(define (is-positive? n)
  (if (> n 0)
      #t
      #f))

(is-positive? 5)   ; #t
(is-positive? -2)  ; #f
```

### Cond (Múltiples Condiciones)
```scheme
(define (number-type n)
  (cond
    ((> n 0) "positive")
    ((< n 0) "negative")
    (else "zero")))

(number-type 5)    ; "positive"
(number-type 0)    ; "zero"
```

## 7. Listas

### Creando Listas
```scheme
; Usando quote
'(1 2 3)          ; Lista de números

; Usando la función list
(list 1 2 3)      ; Igual que arriba

; Usando cons (construir)
(cons 1 '(2 3))   ; Igual que arriba
```

### Operaciones con Listas
```scheme
(car '(1 2 3))    ; 1 (primer elemento)
(cdr '(1 2 3))    ; (2 3) (resto de la lista)
(null? '())       ; #t (verificar si está vacía)
(length '(1 2 3)) ; 3
```

## 8. Recursión

### Recursión Simple
```scheme
(define (factorial n)
  (if (= n 0)
      1
      (* n (factorial (- n 1)))))

(factorial 5)     ; 120 (5 * 4 * 3 * 2 * 1)
```

### Recursión con Listas
```scheme
(define (sum-list lst)
  (if (null? lst)
      0
      (+ (car lst) (sum-list (cdr lst)))))

(sum-list '(1 2 3 4))  ; 10
```

## 9. Funciones de Orden Superior

### Mapeo
```scheme
(map square '(1 2 3 4))    ; (1 4 9 16)
(map + '(1 2 3) '(4 5 6))  ; (5 7 9)
```

### Filtrado
```scheme
(define (even? n) (= (remainder n 2) 0))
(filter even? '(1 2 3 4 5 6))  ; (2 4 6)
```

## 10. Enlaces Let

```scheme
; Enlaces de variables locales
(define (circle-area r)
  (let ((pi 3.14159))
    (* pi (square r))))

(circle-area 2)    ; 12.56636
```

## 11. Entrada/Salida

```scheme
; Mostrar salida
(display "Hello, Scheme!")
(newline)

; Leer entrada (la implementación puede variar)
(define name (read))
(display "Hello, ")
(display name)
```

## 12. Programa de Ejemplo

Aquí hay un programa completo que combina varios conceptos:

```scheme
; Programa para calcular el promedio de una lista de números
(define (average lst)
  (define (sum lst)
    (if (null? lst)
        0
        (+ (car lst) (sum (cdr lst)))))
  (define len (length lst))
  (if (= len 0)
      0
      (/ (sum lst) len)))

; Probar el programa
(display (average '(1 2 3 4 5)))  ; 3
(newline)
(display (average '()))           ; 0
```

## Características Clave de Scheme

1. **Minimalista**: Lenguaje central pequeño con características potentes
2. **Funcional**: Énfasis en funciones puras e inmutabilidad
3. **Notación Prefija**: Todas las operaciones usan sintaxis prefija
4. **Funciones de Primera Clase**: Las funciones pueden pasarse como argumentos
5. **Optimización de Llamada de Cola**: Recursión eficiente

## Consejos de Aprendizaje

1. Practica en un REPL para ver resultados inmediatos
2. Comienza con funciones simples y aumenta la complejidad
3. Piensa de forma recursiva para el procesamiento de listas
4. Usa una sangría adecuada para manejar los paréntesis
5. Experimenta con funciones de orden superior

Este tutorial cubre los conceptos centrales de Scheme. Para profundizar tu comprensión, intenta:
- Escribir funciones recursivas más complejas
- Explorar sistemas de macros (tema avanzado)
- Construir pequeños proyectos como calculadoras o procesadores de listas
- Estudiar las bibliotecas estándar de Scheme (varía según la implementación)

¿Te gustaría que profundice en alguna sección específica o que proporcione más ejemplos?