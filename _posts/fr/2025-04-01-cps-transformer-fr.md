---
audio: false
generated: true
lang: fr
layout: post
title: Transformateur CPS
translated: true
type: note
---

```scheme
;; Un transformateur CPS simple qui gère correctement les appels en queue et ne
;; duplique pas les contextes pour les expressions if.
;; auteur : Yin Wang (yw21@cs.indiana.edu)
(load "pmatch.scm") ; Charge une bibliothèque de correspondance de motifs pour Scheme, facilitant la gestion des différentes structures d'expression.

(define cps
  (lambda (exp)
    (letrec
        ([trivial? (lambda (x) (memq x '(zero? add1 sub1)))] ; Vérifie si un symbole donné est l'un des opérateurs primitifs : zero?, add1, sub1. Ceux-ci sont traités spécialement dans la transformation.
         [id (lambda (v) v)] ; La fonction identité, utilisée comme continuation initiale pour l'expression de haut niveau.
         [ctx0 (lambda (v) `(k ,v))]      ; contexte de queue. Crée une continuation qui applique simplement la continuation courante 'k' à une valeur 'v'. Utilisée lorsque l'appel courant est en position de queue.
         [fv (let ([n -1]) ; Crée un générateur pour des noms de variables fraîches.
               (lambda ()
                 (set! n (+ 1 n))
                 (string->symbol (string-append "v" (number->string n)))))]
         [cps1
          (lambda (exp ctx) ; La fonction récursive principale qui effectue la transformation CPS. Elle prend une expression 'exp' et une continuation 'ctx' comme arguments. La continuation représente ce qu'il faut faire avec le résultat de l'évaluation de 'exp'.
            (pmatch exp ; Utilise la correspondance de motifs pour analyser la structure de l'expression.
              [,x (guard (not (pair? x))) (ctx x)] ; Cas de base : Si l'expression 'x' n'est pas une paire (c'est-à-dire, c'est un littéral ou une variable), cela signifie que c'est déjà une valeur. Applique la continuation courante 'ctx' à cette valeur.

              [(if ,test ,conseq ,alt) ; Correspond à une expression 'if' avec un test, un conséquent et un alternatif.
               (cps1 test ; Transforme récursivement l'expression 'test'.
                     (lambda (t) ; La continuation pour l'expression 'test'. Elle prend le résultat du test (qui sera une valeur booléenne) comme 't'.
                       (cond
                        [(memq ctx (list ctx0 id)) ; Si le contexte courant 'ctx' est soit le contexte de queue 'ctx0', soit le contexte d'identité initial 'id', cela signifie que l'expression 'if' elle-même est en position de queue.
                         `(if ,t ,(cps1 conseq ctx) ,(cps1 alt ctx))] ; Dans ce cas, l'expression 'if' reste une expression 'if' dans le code CPSé. Le conséquent et l'alternatif sont CPSés avec le même contexte 'ctx'. Cela évite de dupliquer les contextes.
                        [else ; Si le contexte courant n'est pas un contexte de queue, cela signifie que le résultat de l'expression 'if' doit être passé à un calcul ultérieur.
                         (let ([u (fv)]) ; Génère un nom de variable fraîche 'u' pour contenir le résultat de l'expression 'if'.
                           `(let ([k (lambda (,u) ,(ctx u))]) ; Crée une nouvelle continuation 'k' qui prend le résultat 'u' et applique le contexte original 'ctx' à celui-ci.
                              (if ,t ,(cps1 conseq ctx0) ,(cps1 alt ctx0))))])))] ; L'expression 'if' est encapsulée dans un 'let' qui introduit la nouvelle continuation 'k'. Le conséquent et l'alternatif sont CPSés avec le contexte de queue 'ctx0', car leurs résultats seront immédiatement passés à 'k'.

              [(lambda (,x) ,body) ; Correspond à une expression lambda avec un seul argument 'x' et un corps.
               (ctx `(lambda (,x k) ,(cps1 body ctx0)))] ; L'expression lambda est transformée en une nouvelle expression lambda qui prend un argument supplémentaire 'k' (la continuation). Le corps de la lambda originale est CPSé avec le contexte de queue 'ctx0', car son résultat sera passé à cette continuation 'k'.

              [(,op ,a ,b) ; Correspond à une expression avec un opérateur binaire 'op' et deux opérandes 'a' et 'b'.
               (cps1 a ; Transforme récursivement le premier opérande 'a'.
                     (lambda (v1) ; La continuation pour 'a'. Elle prend le résultat 'v1'.
                       (cps1 b ; Transforme récursivement le deuxième opérande 'b'.
                             (lambda (v2) ; La continuation pour 'b'. Elle prend le résultat 'v2'.
                                   (ctx `(,op ,v1 ,v2))))))] ; Applique le contexte original 'ctx' à l'expression formée par l'opérateur 'op' et les résultats CPSés des opérandes 'v1' et 'v2'.

              [(,rator ,rand) ; Correspond à une application de fonction avec un rator (la fonction) et un rand (l'argument).
               (cps1 rator ; Transforme récursivement le rator.
                     (lambda (r) ; La continuation pour le rator. Elle prend le résultat 'r' (la fonction).
                       (cps1 rand ; Transforme récursivement l'opérande.
                             (lambda (d) ; La continuation pour l'opérande. Elle prend le résultat 'd' (l'argument).
                               (cond
                                [(trivial? r) (ctx `(,r ,d))] ; Si le rator 'r' est un opérateur trivial (comme zero?, add1, sub1), applique le contexte courant 'ctx' à l'application de l'opérateur à l'opérande.
                                [(eq? ctx ctx0) `(,r ,d k)]  ; appel en queue. Si le contexte courant est le contexte de queue 'ctx0', cela signifie que cette application de fonction est en position de queue. La fonction CPSée 'r' est appelée avec l'argument CPSé 'd' et la continuation courante 'k'.
                                [else ; Si l'application de fonction n'est pas en position de queue.
                                 (let ([u (fv)]) ; Génère un nom de variable fraîche 'u' pour le résultat.
                                   `(,r ,d (lambda (,u) ,(ctx u))))])))))]))]) ; La fonction CPSée 'r' est appelée avec l'argument CPSé 'd' et une nouvelle continuation qui prend le résultat 'u' et applique le contexte original 'ctx' à celui-ci.

      (cps1 exp id))));; Démarre la transformation CPS en appelant 'cps1' avec l'expression d'entrée 'exp' et la continuation d'identité initiale 'id'.

;;; tests
;; var
(cps 'x) ; Transforme la variable 'x'. Le résultat sera '(k x)' car le contexte initial est 'id', et 'id' est appliqué à 'x'.

(cps '(lambda (x) x)) ; Transforme une simple fonction lambda identité. Le résultat sera '(lambda (x k) (k x))'.

(cps '(lambda (x) (x 1))) ; Transforme une fonction lambda qui applique son argument à 1. Le résultat sera '(lambda (x k) (x 1 k))'.

;; pas de lambda (générera des fonctions identité pour retourner au niveau supérieur)
(cps '(if (f x) a b)) ; Transforme une expression if où le test est un appel de fonction.

(cps '(if x (f a) b)) ; Transforme une expression if où le test est une variable.

;; if autonome (queue)
(cps '(if x (f a) b)) ; Ici, le 'if' est au niveau supérieur, donc il est dans un contexte de queue.

;; if à l'intérieur du test if (non-queue)
(cps '(lambda (x) (if (f x) a b))) ; Le 'if' est à l'intérieur d'une lambda, et son résultat est utilisé par la lambda (retourné implicitement), donc il n'est pas dans un contexte de queue.

(cps '(lambda (x) (if (if x (f a) b) c d))) ; Expressions 'if' imbriquées. Le 'if' interne est dans le test du 'if' externe.

;; les deux branches sont triviales, devrait faire plus d'optimisations
(cps '(lambda (x) (if (if x (zero? a) b) c d)))

;; if à l'intérieur de la branche if (queue)
(cps '(lambda (x) (if t (if x (f a) b) c))) ; Le 'if' interne est dans la branche conséquente du 'if' externe. Si le 'if' externe est dans un contexte de queue, l'interne le sera aussi.

;; if à l'intérieur de la branche if, mais encore à l'intérieur d'un autre test if (non-queue)
(cps '(lambda (x) (if (if t (if x (f a) b) c) e w)))

;; if comme opérande (non-queue)
(cps '(lambda (x) (h (if x (f a) b)))) ; Le résultat de l'expression 'if' est utilisé comme argument pour 'h'.

;; if comme opérateur (non-queue)
(cps '(lambda (x) ((if x (f g) h) c))) ; Le résultat de l'expression 'if' est utilisé comme la fonction à appeler.

;; pourquoi nous avons besoin de plus de deux noms
(cps '(((f a) (g b)) ((f c) (g d)))) ; Cet exemple démontre probablement la nécessité du générateur de noms de variables fraîches ('fv') pour éviter les conflits de noms lors de la transformation d'expressions imbriquées complexes.

;; factorielle
(define fact-cps
  (cps
   '(lambda (n)
      ((lambda (fact)
         ((fact fact) n))
       (lambda (fact)
         (lambda (n)
           (if (zero? n)
               1
               (* n ((fact fact) (sub1 n))))))))));; affiche la fonction CPSée

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

**Explication du transformateur CPS :**

Ce code Scheme implémente une transformation de style de passage de continuation (CPS) pour un sous-ensemble simple du langage Scheme. Voici une explication des concepts clés et du fonctionnement du code :

**1. Style de Passage de Continuation (CPS) :**

* En CPS, une fonction ne retourne pas directement une valeur. Au lieu de cela, elle prend un argument supplémentaire appelé une **continuation**.
* La continuation est une fonction qui représente le reste du calcul à effectuer avec le résultat de la fonction courante.
* Lorsqu'une fonction CPS termine son calcul, elle appelle la continuation avec le résultat.

**Pourquoi utiliser CPS ?**

* **Flux de Contrôle Explicite :** CPS rend le flux de contrôle explicite. Les appels de fonction et les retours sont remplacés par des appels à des continuations.
* **Optimisation des Appels en Queue :** CPS permet une mise en œuvre facile de l'optimisation des appels en queue. Dans le code transformé, les appels de fonction en position de queue deviennent la dernière opération, permettant une exécution efficace sans augmenter la profondeur de la pile.
* **Implémentation de Structures de Contrôle Avancées :** CPS peut être utilisé comme représentation intermédiaire dans les compilateurs pour implémenter des fonctionnalités comme les exceptions, les coroutines et le retour en arrière.

**2. La fonction `cps` :**

* Le point d'entrée principal pour la transformation. Elle prend une expression `exp` en entrée.
* Elle utilise `letrec` pour définir plusieurs fonctions auxiliaires mutuellement récursives.
* Elle initialise la transformation en appelant `cps1` avec l'expression d'entrée et la fonction identité `id` comme continuation initiale. Cela signifie que le résultat final de l'expression transformée sera retourné directement.

**3. Fonctions auxiliaires :**

* **`trivial?` :** Identifie les opérateurs primitifs comme `zero?`, `add1` et `sub1`. Ceux-ci sont traités spécialement dans la transformation.
* **`id` :** La fonction identité `(lambda (v) v)`. C'est la continuation initiale, signifiant "retourne simplement la valeur".
* **`ctx0` :** Crée un "contexte de queue". Étant donné une valeur `v`, elle retourne `(k v)`, où `k` est la continuation courante. Cela signifie que le calcul courant est en position de queue, et le résultat doit être passé directement à la continuation en attente.
* **`fv` :** Génère des noms de variables fraîches (par exemple, `v0`, `v1`, `v2`, ...). Ceci est crucial pour éviter la capture de variable lors de l'introduction de nouvelles continuations.

**4. La fonction `cps1` (La transformation principale) :**

* Cette fonction parcourt récursivement l'expression d'entrée et la transforme en CPS.
* Elle prend deux arguments : l'expression `exp` à transformer et la continuation courante `ctx`.
* Elle utilise la bibliothèque `pmatch` pour la correspondance de motifs afin de gérer différents types d'expressions :

    * **Littéraux et Variables :** Si l'expression n'est pas une paire (un littéral ou une variable), c'est déjà une valeur. La continuation courante `ctx` est appliquée à cette valeur : `(ctx x)`.

    * **Expressions `if` :** C'est une partie clé du transformateur qui gère les appels en queue et évite la duplication de contexte.
        * Elle transforme d'abord l'expression `test` avec une continuation qui prend le résultat du test (`t`).
        * Si le contexte courant `ctx` est un contexte de queue (`ctx0`) ou le contexte d'identité initial (`id`), cela signifie que l'expression `if` elle-même est en position de queue. Dans ce cas, la structure `if` est préservée, et les branches `conseq` et `alt` sont CPSées avec le même contexte `ctx`.
        * Si le contexte courant n'est pas un contexte de queue, cela signifie que le résultat de l'expression `if` doit être utilisé ultérieurement. Une nouvelle continuation `k` est créée qui prend le résultat du `if` et applique le contexte original `ctx` à celui-ci. Les branches `conseq` et `alt` sont ensuite CPSées avec le contexte de queue `ctx0`, et l'expression `if` entière est encapsulée dans un `let` qui introduit `k`.

    * **Expressions `lambda` :** Une expression `lambda` `(lambda (x) body)` est transformée en une nouvelle expression `lambda` qui prend un argument supplémentaire `k` (la continuation) : `(lambda (x k) (cps1 body ctx0))`. Le corps de la lambda originale est CPSé avec le contexte de queue `ctx0`.

    * **Opérations binaires (`op a b`) :** Les opérandes `a` et `b` sont CPSées séquentiellement. La continuation pour `a` prend son résultat `v1`, puis CPSe `b` avec une continuation qui prend son résultat `v2`. Finalement, le contexte original `ctx` est appliqué à l'expression formée par l'opérateur `op` et les résultats CPSés `v1` et `v2`.

    * **Applications de fonction (`rator rand`) :** Le `rator` (fonction) et le `rand` (argument) sont CPSés séquentiellement.
        * Si le `rator` est un opérateur `trivial?`, le contexte courant `ctx` est directement appliqué au résultat de l'application de l'opérateur à l'opérande.
        * Si le contexte courant est un contexte de queue (`ctx0`), la fonction CPSée `r` est appelée avec l'argument CPSé `d` et la continuation courante `k`. Ceci assure des appels en queue corrects.
        * Sinon (appel non en queue), une nouvelle continuation est créée qui prend le résultat de l'appel de fonction et applique le contexte original `ctx` à celui-ci. La fonction CPSée `r` est appelée avec l'argument CPSé `d` et cette nouvelle continuation.

**5. Tests :**

* Le code inclut plusieurs cas de test qui démontrent la transformation de différents types d'expressions, y compris des variables, des fonctions lambda, des expressions `if` dans divers contextes et des applications de fonction.

**6. Exemple de factorielle :**

* La définition `fact-cps` montre comment le transformateur CPS peut être appliqué à une fonction factorielle récursive.
* La sortie `pretty-print` montre la version CPSée de la fonction factorielle, qui prend maintenant un argument de continuation supplémentaire `k`.
* La dernière ligne évalue la fonction factorielle CPSée avec l'entrée `5` et une continuation de haut niveau `(lambda (v) v)` qui retourne simplement la valeur finale.

**En résumé, ce code implémente une transformation CPS qui vise à :**

* Convertir les expressions en style de passage de continuation.
* Assurer l'optimisation des appels en queue en passant explicitement la continuation courante.
* Gérer efficacement les expressions `if` sans dupliquer le contexte environnant lorsque le `if` lui-même est en position de queue. Ceci est réalisé en conservant la structure `if` et en CPSant les branches avec le même contexte. Lorsque le `if` n'est pas en position de queue, il introduit une nouvelle continuation pour gérer le résultat.