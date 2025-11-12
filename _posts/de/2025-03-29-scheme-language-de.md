---
audio: false
generated: true
lang: de
layout: post
title: Scheme-Programmier-Tutorial
translated: true
type: note
---

Scheme ist ein minimalistischer Dialekt von Lisp, der für seine Einfachheit und Eleganz bekannt ist. Dieses Tutorial behandelt die Grundlagen, um Ihnen den Einstieg zu erleichtern.

## 1. Grundlegende Syntax und Konzepte

### Scheme ausführen
- Sie benötigen einen Scheme-Interpreter (wie Racket, Guile oder Chez Scheme)
- Code wird typischerweise in einer `.scm`-Datei geschrieben oder in einer REPL (Read-Eval-Print Loop) eingegeben

### Ausdrücke und Klammern
- Alles in Scheme ist ein Ausdruck, der einen Wert zurückgibt
- Klammern werden für Funktionsaufrufe und Gruppierung verwendet
- Format: `(function arg1 arg2 ...)`

## 2. Grundlegende Datentypen

```scheme
; Zahlen
42          ; Integer
3.14        ; Floating-point
1/2         ; Rational

; Boolesche Werte
#t          ; True
#f         ; False

; Strings
"hello"     ; String literal

; Symbole
'hello      ; Symbol (quoted with ')
```

## 3. Grundlegende Operationen

```scheme
; Arithmetik
(+ 2 3)        ; 5
(- 10 4)       ; 6
(* 3 4)        ; 12
(/ 15 3)       ; 5

; Vergleiche
(= 5 5)        ; #t
(< 3 7)        ; #t
(> 10 5)       ; #t
```

## 4. Variablen definieren

```scheme
; Definiere eine globale Variable
(define x 10)

; Verwende die Variable
(+ x 5)        ; 15
```

## 5. Funktionen

### Funktionen definieren
```scheme
; Grundlegende Funktionsdefinition
(define square
  (lambda (x)    ; lambda erzeugt eine anonyme Funktion
    (* x x)))

(square 4)     ; 16
```

### Mehrere Parameter
```scheme
(define add
  (lambda (x y)
    (+ x y)))

(add 3 5)      ; 8
```

### Kurzschreibweise
```scheme
; Alternative Syntax (syntactic sugar)
(define (multiply x y)
  (* x y))

(multiply 2 3) ; 6
```

## 6. Bedingungen

### If-Anweisung
```scheme
(define (is-positive? n)
  (if (> n 0)
      #t
      #f))

(is-positive? 5)   ; #t
(is-positive? -2)  ; #f
```

### Cond (Mehrfachbedingungen)
```scheme
(define (number-type n)
  (cond
    ((> n 0) "positive")
    ((< n 0) "negative")
    (else "zero")))

(number-type 5)    ; "positive"
(number-type 0)    ; "zero"
```

## 7. Listen

### Listen erstellen
```scheme
; Quote verwenden
'(1 2 3)          ; Liste von Zahlen

; list-Funktion verwenden
(list 1 2 3)      ; Gleich wie oben

; cons verwenden (construct)
(cons 1 '(2 3))   ; Gleich wie oben
```

### Listenoperationen
```scheme
(car '(1 2 3))    ; 1 (erstes Element)
(cdr '(1 2 3))    ; (2 3) (Rest der Liste)
(null? '())       ; #t (prüft, ob leer)
(length '(1 2 3)) ; 3
```

## 8. Rekursion

### Einfache Rekursion
```scheme
(define (factorial n)
  (if (= n 0)
      1
      (* n (factorial (- n 1)))))

(factorial 5)     ; 120 (5 * 4 * 3 * 2 * 1)
```

### Listenrekursion
```scheme
(define (sum-list lst)
  (if (null? lst)
      0
      (+ (car lst) (sum-list (cdr lst)))))

(sum-list '(1 2 3 4))  ; 10
```

## 9. Higher-Order Functions

### Mapping
```scheme
(map square '(1 2 3 4))    ; (1 4 9 16)
(map + '(1 2 3) '(4 5 6))  ; (5 7 9)
```

### Filtern
```scheme
(define (even? n) (= (remainder n 2) 0))
(filter even? '(1 2 3 4 5 6))  ; (2 4 6)
```

## 10. Let-Bindungen

```scheme
; Lokale Variablenbindungen
(define (circle-area r)
  (let ((pi 3.14159))
    (* pi (square r))))

(circle-area 2)    ; 12.56636
```

## 11. Eingabe/Ausgabe

```scheme
; Ausgabe anzeigen
(display "Hello, Scheme!")
(newline)

; Eingabe lesen (Implementierung kann variieren)
(define name (read))
(display "Hello, ")
(display name)
```

## 12. Beispielprogramm

Hier ist ein vollständiges Programm, das mehrere Konzepte kombiniert:

```scheme
; Programm zur Berechnung des Durchschnitts einer Zahlenliste
(define (average lst)
  (define (sum lst)
    (if (null? lst)
        0
        (+ (car lst) (sum (cdr lst)))))
  (define len (length lst))
  (if (= len 0)
      0
      (/ (sum lst) len)))

; Teste das Programm
(display (average '(1 2 3 4 5)))  ; 3
(newline)
(display (average '()))           ; 0
```

## Wichtige Merkmale von Scheme

1. **Minimalistisch**: Kleine Kernsprache mit mächtigen Funktionen
2. **Funktional**: Betonung auf pure Funktionen und Unveränderlichkeit
3. **Präfix-Notation**: Alle Operationen verwenden Präfix-Syntax
4. **First-class Functions**: Funktionen können als Argumente übergeben werden
5. **Tail-call Optimization**: Effiziente Rekursion

## Lerntipps

1. Üben Sie in einer REPL, um sofortige Ergebnisse zu sehen
2. Beginnen Sie mit einfachen Funktionen und steigern Sie die Komplexität
3. Denken Sie rekursiv für die Listenverarbeitung
4. Verwenden Sie korrekte Einrückung, um Klammern zu verwalten
5. Experimentieren Sie mit Higher-Order Functions

Dieses Tutorial behandelt die Kernkonzepte von Scheme. Um Ihr Verständnis zu vertiefen, versuchen Sie:
- Komplexere rekursive Funktionen zu schreiben
- Makrosysteme zu erkunden (fortgeschrittenes Thema)
- Kleine Projekte wie Taschenrechner oder Listenprozessoren zu bauen
- Die Standardbibliotheken von Scheme zu studieren (variiert je nach Implementierung)

Möchten Sie, dass ich einen bestimmten Abschnitt näher erläutere oder weitere Beispiele liefere?