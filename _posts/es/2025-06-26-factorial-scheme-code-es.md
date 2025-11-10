---
audio: false
generated: true
lang: es
layout: post
title: Programa Factorial en Chez Scheme
translated: true
type: note
---

Aquí tienes un programa simple en Chez Scheme que calcula el factorial de un número. Guárdalo como `factorial.scm`:

```scheme
(define (factorial n)
  (if (<= n 1)
      1
      (* n (factorial (- n 1)))))

(display "Factorial de 5 es: ")
(display (factorial 5))
(newline)
```

Para ejecutarlo:
1. Guarda el código en un archivo llamado `factorial.scm`.
2. En tu terminal, navega al directorio que contiene el archivo.
3. Ejecuta: `scheme --script factorial.scm`

Esto producirá la siguiente salida:
```
Factorial de 5 es: 120
```

El programa define una función recursiva `factorial` y calcula el factorial de 5. La opción `--script` (como se muestra en la salida de `scheme --help`) te permite ejecutar el archivo directamente.