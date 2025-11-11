---
audio: false
generated: true
lang: fr
layout: post
title: Tutoriel de programmation en Scheme
translated: true
type: note
---

Scheme est un dialecte minimaliste de Lisp connu pour sa simplicité et son élégance. Ce tutoriel couvrira les bases pour bien démarrer.

## 1. Syntaxe et concepts de base

### Exécuter Scheme
- Vous aurez besoin d'un interpréteur Scheme (comme Racket, Guile ou Chez Scheme)
- Le code est généralement écrit dans un fichier `.scm` ou saisi dans un REPL (Read-Eval-Print Loop)

### Expressions et parenthèses
- Tout dans Scheme est une expression qui renvoie une valeur
- Les parenthèses sont utilisées pour les appels de fonction et le regroupement
- Format : `(function arg1 arg2 ...)`

## 2. Types de données de base

```scheme
; Nombres
42          ; Entier
3.14        ; Nombre à virgule flottante
1/2         ; Rationnel

; Booléens
#t          ; Vrai
#f         ; Faux

; Chaînes de caractères
"hello"     ; Littéral de chaîne

; Symboles
'hello      ; Symbole (précédé de ')
```

## 3. Opérations de base

```scheme
; Arithmétique
(+ 2 3)        ; 5
(- 10 4)       ; 6
(* 3 4)        ; 12
(/ 15 3)       ; 5

; Comparaisons
(= 5 5)        ; #t
(< 3 7)        ; #t
(> 10 5)       ; #t
```

## 4. Définition de variables

```scheme
; Définir une variable globale
(define x 10)

; Utiliser la variable
(+ x 5)        ; 15
```

## 5. Fonctions

### Définition de fonctions
```scheme
; Définition de fonction basique
(define square
  (lambda (x)    ; lambda crée une fonction anonyme
    (* x x)))

(square 4)     ; 16
```

### Paramètres multiples
```scheme
(define add
  (lambda (x y)
    (+ x y)))

(add 3 5)      ; 8
```

### Définition raccourcie
```scheme
; Syntaxe alternative (sucre syntaxique)
(define (multiply x y)
  (* x y))

(multiply 2 3) ; 6
```

## 6. Conditionnelles

### Instruction If
```scheme
(define (is-positive? n)
  (if (> n 0)
      #t
      #f))

(is-positive? 5)   ; #t
(is-positive? -2)  ; #f
```

### Cond (Conditions multiples)
```scheme
(define (number-type n)
  (cond
    ((> n 0) "positif")
    ((< n 0) "négatif")
    (else "zéro")))

(number-type 5)    ; "positif"
(number-type 0)    ; "zéro"
```

## 7. Listes

### Création de listes
```scheme
; Utilisation de quote
'(1 2 3)          ; Liste de nombres

; Utilisation de la fonction list
(list 1 2 3)      ; Identique à ci-dessus

; Utilisation de cons (construire)
(cons 1 '(2 3))   ; Identique à ci-dessus
```

### Opérations sur les listes
```scheme
(car '(1 2 3))    ; 1 (premier élément)
(cdr '(1 2 3))    ; (2 3) (reste de la liste)
(null? '())       ; #t (vérifier si vide)
(length '(1 2 3)) ; 3
```

## 8. Récursion

### Récursion simple
```scheme
(define (factorial n)
  (if (= n 0)
      1
      (* n (factorial (- n 1)))))

(factorial 5)     ; 120 (5 * 4 * 3 * 2 * 1)
```

### Récursion sur les listes
```scheme
(define (sum-list lst)
  (if (null? lst)
      0
      (+ (car lst) (sum-list (cdr lst)))))

(sum-list '(1 2 3 4))  ; 10
```

## 9. Fonctions d'ordre supérieur

### Mapping
```scheme
(map square '(1 2 3 4))    ; (1 4 9 16)
(map + '(1 2 3) '(4 5 6))  ; (5 7 9)
```

### Filtrage
```scheme
(define (even? n) (= (remainder n 2) 0))
(filter even? '(1 2 3 4 5 6))  ; (2 4 6)
```

## 10. Liaisons Let

```scheme
; Liaisons de variables locales
(define (circle-area r)
  (let ((pi 3.14159))
    (* pi (square r))))

(circle-area 2)    ; 12.56636
```

## 11. Entrée/Sortie

```scheme
; Afficher une sortie
(display "Hello, Scheme!")
(newline)

; Lire une entrée (l'implémentation peut varier)
(define name (read))
(display "Hello, ")
(display name)
```

## 12. Exemple de programme

Voici un programme complet qui combine plusieurs concepts :

```scheme
; Programme pour calculer la moyenne d'une liste de nombres
(define (average lst)
  (define (sum lst)
    (if (null? lst)
        0
        (+ (car lst) (sum (cdr lst)))))
  (define len (length lst))
  (if (= len 0)
      0
      (/ (sum lst) len)))

; Tester le programme
(display (average '(1 2 3 4 5)))  ; 3
(newline)
(display (average '()))           ; 0
```

## Caractéristiques clés de Scheme

1. **Minimaliste** : Petit langage central avec des fonctionnalités puissantes
2. **Fonctionnel** : Accent mis sur les fonctions pures et l'immuabilité
3. **Notation préfixe** : Toutes les opérations utilisent la syntaxe préfixe
4. **Fonctions de première classe** : Les fonctions peuvent être passées comme arguments
5. **Optimisation des appels terminaux** : Récursion efficace

## Conseils d'apprentissage

1. Pratiquez dans un REPL pour voir les résultats immédiatement
2. Commencez par des fonctions simples et augmentez la complexité
3. Pensez de manière récursive pour le traitement des listes
4. Utilisez une indentation appropriée pour gérer les parenthèses
5. Expérimentez avec les fonctions d'ordre supérieur

Ce tutoriel couvre les concepts fondamentaux de Scheme. Pour approfondir votre compréhension, essayez :
- D'écrire des fonctions récursives plus complexes
- D'explorer les systèmes de macros (sujet avancé)
- De construire de petits projets comme des calculatrices ou des processeurs de listes
- D'étudier les bibliothèques standard de Scheme (varie selon l'implémentation)

Souhaitez-vous que je développe une section spécifique ou que je fournisse plus d'exemples ?