---
audio: false
generated: true
lang: de
layout: post
title: CPS-Transformer
translated: true
type: note
---

```scheme
;; Ein einfacher CPS-Transformer, der korrekten Tail-Call durchführt und
;; Kontexte für if-Ausdrücke nicht dupliziert.
;; Autor: Yin Wang (yw21@cs.indiana.edu)
(lade "pmatch.scm") ; Lädt eine Pattern-Matching-Bibliothek für Scheme, die die Handhabung verschiedener Ausdrucksstrukturen erleichtert.

(define cps
  (lambda (exp)
    (letrec
        ([trivial? (lambda (x) (memq x '(zero? add1 sub1)))] ; Prüft, ob ein gegebenes Symbol einer der primitiven Operatoren ist: zero?, add1, sub1. Diese werden bei der Transformation speziell behandelt.
         [id (lambda (v) v)] ; Die Identitätsfunktion, wird als initiale Fortsetzung für den Top-Level-Ausdruck verwendet.
         [ctx0 (lambda (v) `(k ,v))]      ; Tail-Kontext. Erzeugt eine Fortsetzung, die einfach die aktuelle Fortsetzung 'k' auf einen Wert 'v' anwendet. Wird verwendet, wenn der aktuelle Aufruf in Tail-Position steht.
         [fv (let ([n -1]) ; Erzeugt einen Generator für frische Variablennamen.
               (lambda ()
                 (set! n (+ 1 n))
                 (string->symbol (string-append "v" (number->string n)))))]
         [cps1
          (lambda (exp ctx) ; Die zentrale rekursive Funktion, die die CPS-Transformation durchführt. Sie nimmt einen Ausdruck 'exp' und eine Fortsetzung 'ctx' als Argumente. Die Fortsetzung repräsentiert, was mit dem Ergebnis der Auswertung von 'exp' geschehen soll.
            (pmatch exp ; Verwendet Pattern Matching, um die Struktur des Ausdrucks zu analysieren.
              [,x (guard (not (pair? x))) (ctx x)] ; Basisfall: Wenn der Ausdruck 'x' kein Paar ist (d.h. ein Literal oder eine Variable), bedeutet dies, dass es bereits ein Wert ist. Wende die aktuelle Fortsetzung 'ctx' auf diesen Wert an.

              [(if ,test ,conseq ,alt) ; Trifft auf einen 'if'-Ausdruck mit einem Test, einer Konsequente und einer Alternative zu.
               (cps1 test ; Transformiert den 'test'-Ausdruck rekursiv.
                     (lambda (t) ; Die Fortsetzung für den 'test'-Ausdruck. Sie nimmt das Ergebnis des Tests (ein boolescher Wert) als 't'.
                       (cond
                        [(memq ctx (list ctx0 id)) ; Wenn der aktuelle Kontext 'ctx' entweder der Tail-Kontext 'ctx0' oder der initiale Identitätskontext 'id' ist, bedeutet dies, dass der 'if'-Ausdruck selbst in einer Tail-Position steht.
                         `(if ,t ,(cps1 conseq ctx) ,(cps1 alt ctx))] ; In diesem Fall bleibt der 'if'-Ausdruck ein 'if'-Ausdruck im CPS-transformierten Code. Die Konsequente und Alternative werden mit demselben Kontext 'ctx' CPS-transformiert. Dies vermeidet das Duplizieren von Kontexten.
                        [else ; Wenn der aktuelle Kontext kein Tail-Kontext ist, bedeutet dies, dass das Ergebnis des 'if'-Ausdrucks an eine weitere Berechnung übergeben werden muss.
                         (let ([u (fv)]) ; Erzeuge einen frischen Variablennamen 'u', um das Ergebnis des 'if'-Ausdrucks zu halten.
                           `(let ([k (lambda (,u) ,(ctx u))]) ; Erzeuge eine neue Fortsetzung 'k', die das Ergebnis 'u' nimmt und den ursprünglichen Kontext 'ctx' darauf anwendet.
                              (if ,t ,(cps1 conseq ctx0) ,(cps1 alt ctx0))))])))] ; Der 'if'-Ausdruck wird in ein 'let' eingebettet, das die neue Fortsetzung 'k' einführt. Die Konsequente und Alternative werden mit dem Tail-Kontext 'ctx0' CPS-transformiert, da ihre Ergebnisse sofort an 'k' übergeben werden.

              [(lambda (,x) ,body) ; Trifft auf einen Lambda-Ausdruck mit einem einzelnen Argument 'x' und einem Rumpf.
               (ctx `(lambda (,x k) ,(cps1 body ctx0)))] ; Der Lambda-Ausdruck wird in einen neuen Lambda-Ausdruck transformiert, der ein zusätzliches Argument 'k' (die Fortsetzung) nimmt. Der Rumpf des ursprünglichen Lambdas wird mit dem Tail-Kontext 'ctx0' CPS-transformiert, da sein Ergebnis an diese Fortsetzung 'k' übergeben wird.

              [(,op ,a ,b) ; Trifft auf einen Ausdruck mit einem binären Operator 'op' und zwei Operanden 'a' und 'b'.
               (cps1 a ; Transformiert den ersten Operanden 'a' rekursiv.
                     (lambda (v1) ; Die Fortsetzung für 'a'. Sie nimmt das Ergebnis 'v1'.
                       (cps1 b ; Transformiert den zweiten Operanden 'b' rekursiv.
                             (lambda (v2) ; Die Fortsetzung für 'b'. Sie nimmt das Ergebnis 'v2'.
                                   (ctx `(,op ,v1 ,v2))))))] ; Wende den ursprünglichen Kontext 'ctx' auf den Ausdruck an, der durch den Operator 'op' und die CPS-transformierten Ergebnisse der Operanden 'v1' und 'v2' gebildet wird.

              [(,rator ,rand) ; Trifft auf einen Funktionsapplikation mit einem Rator (die Funktion) und einem Rand (das Argument).
               (cps1 rator ; Transformiert den Rator rekursiv.
                     (lambda (r) ; Die Fortsetzung für den Rator. Sie nimmt das Ergebnis 'r' (die Funktion).
                       (cps1 rand ; Transformiert den Operanden rekursiv.
                             (lambda (d) ; Die Fortsetzung für den Operanden. Sie nimmt das Ergebnis 'd' (das Argument).
                               (cond
                                [(trivial? r) (ctx `(,r ,d))] ; Wenn der Rator 'r' ein trivialer Operator ist (wie zero?, add1, sub1), wende den aktuellen Kontext 'ctx' auf die Applikation des Operators auf den Operanden an.
                                [(eq? ctx ctx0) `(,r ,d k)]  ; Tail-Aufruf. Wenn der aktuelle Kontext der Tail-Kontext 'ctx0' ist, bedeutet dies, dass diese Funktionsapplikation in einer Tail-Position steht. Die CPS-transformierte Funktion 'r' wird mit dem CPS-transformierten Argument 'd' und der aktuellen Fortsetzung 'k' aufgerufen.
                                [else ; Wenn die Funktionsapplikation nicht in einer Tail-Position steht.
                                 (let ([u (fv)]) ; Erzeuge einen frischen Variablennamen 'u' für das Ergebnis.
                                   `(,r ,d (lambda (,u) ,(ctx u))))])))))]))]) ; Die CPS-transformierte Funktion 'r' wird mit dem CPS-transformierten Argument 'd' und einer neuen Fortsetzung aufgerufen, die das Ergebnis 'u' nimmt und den ursprünglichen Kontext 'ctx' darauf anwendet.

      (cps1 exp id))));; Startet die CPS-Transformation durch Aufruf von 'cps1' mit dem Eingabeausdruck 'exp' und der initialen Identitätsfortsetzung 'id'.

;;; Tests
;; var
(cps 'x) ; Transformiert die Variable 'x'. Das Ergebnis wird '(k x)' sein, weil der initiale Kontext 'id' ist und 'id' auf 'x' angewendet wird.

(cps '(lambda (x) x)) ; Transformiert eine einfache Identitäts-Lambda-Funktion. Das Ergebnis wird '(lambda (x k) (k x))' sein.

(cps '(lambda (x) (x 1))) ; Transformiert eine Lambda-Funktion, die ihr Argument auf 1 anwendet. Das Ergebnis wird '(lambda (x k) (x 1 k))' sein.

;; kein Lambda (erzeugt Identitätsfunktionen für die Rückgabe an die Top-Level)
(cps '(if (f x) a b)) ; Transformiert einen if-Ausdruck, bei dem der Test ein Funktionsaufruf ist.

(cps '(if x (f a) b)) ; Transformiert einen if-Ausdruck, bei dem der Test eine Variable ist.

;; if alleinstehend (Tail)
(cps '(if x (f a) b)) ; Hier steht das 'if' auf der obersten Ebene, also in einem Tail-Kontext.

;; if innerhalb eines if-Tests (Non-Tail)
(cps '(lambda (x) (if (f x) a b))) ; Das 'if' ist innerhalb eines Lambdas, und sein Ergebnis wird vom Lambda verwendet (implizit zurückgegeben), also steht es nicht in einer Tail-Position.

(cps '(lambda (x) (if (if x (f a) b) c d))) ; Verschachtelte 'if'-Ausdrücke. Der innere 'if' steht im Test des äußeren 'if'.

;; beide Zweige sind trivial, sollten weitere Optimierungen durchführen
(cps '(lambda (x) (if (if x (zero? a) b) c d)))

;; if innerhalb eines if-Zweigs (Tail)
(cps '(lambda (x) (if t (if x (f a) b) c))) ; Der innere 'if' steht im Konsequenz-Zweig des äußeren 'if'. Wenn der äußere 'if' in einem Tail-Kontext steht, wird der innere es auch sein.

;; if innerhalb eines if-Zweigs, aber wieder innerhalb eines anderen if-Tests (Non-Tail)
(cps '(lambda (x) (if (if t (if x (f a) b) c) e w)))

;; if als Operand (Non-Tail)
(cps '(lambda (x) (h (if x (f a) b)))) ; Das Ergebnis des 'if'-Ausdrucks wird als Argument für 'h' verwendet.

;; if als Operator (Non-Tail)
(cps '(lambda (x) ((if x (f g) h) c))) ; Das Ergebnis des 'if'-Ausdrucks wird als die aufzurufende Funktion verwendet.

;; warum wir mehr als zwei Namen benötigen
(cps '(((f a) (g b)) ((f c) (g d)))) ; Dieses Beispiel demonstriert wahrscheinlich die Notwendigkeit des Generators für frische Variablennamen ('fv'), um Namenskonflikte bei der Transformation komplexer verschachtelter Ausdrücke zu vermeiden.

;; Fakultät
(define fact-cps
  (cps
   '(lambda (n)
      ((lambda (fact)
         ((fact fact) n))
       (lambda (fact)
         (lambda (n)
           (if (zero? n)
               1
               (* n ((fact fact) (sub1 n))))))))));; gibt die CPS-transformierte Funktion aus

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

**Erklärung des CPS-Transformers:**

Dieser Scheme-Code implementiert eine Continuation-Passing Style (CPS) Transformation für eine einfache Teilmenge der Scheme-Sprache. Hier ist eine Aufschlüsselung der Schlüsselkonzepte und der Funktionsweise des Codes:

**1. Continuation-Passing Style (CPS):**

* Im CPS gibt eine Funktion keinen Wert direkt zurück. Stattdessen nimmt sie ein zusätzliches Argument namens **Fortsetzung**.
* Die Fortsetzung ist eine Funktion, die den Rest der Berechnung repräsentiert, der mit dem Ergebnis der aktuellen Funktion durchgeführt werden soll.
* Wenn eine CPS-Funktion ihre Berechnung beendet, ruft sie die Fortsetzung mit dem Ergebnis auf.

**Warum CPS verwenden?**

* **Explizite Ablaufsteuerung:** CPS macht den Ablauf der Steuerung explizit. Funktionsaufrufe und -rückgaben werden durch Aufrufe von Fortsetzungen ersetzt.
* **Tail-Call-Optimierung:** CPS ermöglicht eine einfache Implementierung einer korrekten Tail-Call-Optimierung. Im transformierten Code werden Funktionsaufrufe in Tail-Position zur letzten Operation, was eine effiziente Ausführung ohne Erhöhung der Stacktiefe ermöglicht.
* **Implementierung erweiterter Steuerstrukturen:** CPS kann als Zwischendarstellung in Compilern verwendet werden, um Funktionen wie Ausnahmen, Coroutinen und Backtracking zu implementieren.

**2. Die `cps`-Funktion:**

* Der Haupteinstiegspunkt für die Transformation. Sie nimmt einen Ausdruck `exp` als Eingabe.
* Sie verwendet `letrec`, um mehrere sich gegenseitig rekursive Hilfsfunktionen zu definieren.
* Sie initialisiert die Transformation durch Aufruf von `cps1` mit dem Eingabeausdruck und der Identitätsfunktion `id` als initiale Fortsetzung. Dies bedeutet, dass das Endergebnis des transformierten Ausdrucks direkt zurückgegeben wird.

**3. Hilfsfunktionen:**

* **`trivial?`:** Identifiziert primitive Operatoren wie `zero?`, `add1` und `sub1`. Diese werden bei der Transformation speziell behandelt.
* **`id`:** Die Identitätsfunktion `(lambda (v) v)`. Sie ist die initiale Fortsetzung, bedeutet also "gib einfach den Wert zurück".
* **`ctx0`:** Erzeugt einen "Tail-Kontext". Bei einem Wert `v` gibt sie `(k v)` zurück, wobei `k` die aktuelle Fortsetzung ist. Dies signalisiert, dass die aktuelle Berechnung in einer Tail-Position steht und das Ergebnis direkt an die wartende Fortsetzung übergeben werden soll.
* **`fv`:** Erzeugt frische Variablennamen (z.B. `v0`, `v1`, `v2`, ...). Dies ist entscheidend, um Variablenkonflikte zu vermeiden, wenn neue Fortsetzungen eingeführt werden.

**4. Die `cps1`-Funktion (Die Kern-Transformation):**

* Diese Funktion durchläuft den Eingabeausdruck rekursiv und transformiert ihn in CPS.
* Sie nimmt zwei Argumente: den zu transformierenden Ausdruck `exp` und die aktuelle Fortsetzung `ctx`.
* Sie verwendet die `pmatch`-Bibliothek für Pattern Matching, um verschiedene Arten von Ausdrücken zu behandeln:

    * **Literale und Variablen:** Wenn der Ausdruck kein Paar ist (ein Literal oder eine Variable), ist er bereits ein Wert. Die aktuelle Fortsetzung `ctx` wird auf diesen Wert angewendet: `(ctx x)`.

    * **`if`-Ausdrücke:** Dies ist ein Schlüsselteil des Transformers, der Tail-Aufrufe behandelt und das Duplizieren von Kontexten vermeidet.
        * Zuerst wird der `test`-Ausdruck mit einer Fortsetzung transformiert, die das Ergebnis des Tests (`t`) nimmt.
        * Wenn der aktuelle Kontext `ctx` ein Tail-Kontext (`ctx0`) oder der initiale Identitätskontext (`id`) ist, bedeutet dies, dass der `if`-Ausdruck selbst in einer Tail-Position steht. In diesem Fall wird die `if`-Struktur beibehalten, und die `conseq`- und `alt`-Zweige werden mit demselben Kontext `ctx` CPS-transformiert.
        * Wenn der aktuelle Kontext kein Tail-Kontext ist, bedeutet dies, dass das Ergebnis des `if`-Ausdrucks später verwendet werden muss. Eine neue Fortsetzung `k` wird erzeugt, die das Ergebnis des `if` nimmt und den ursprünglichen Kontext `ctx` darauf anwendet. Die `conseq`- und `alt`-Zweige werden dann mit dem Tail-Kontext `ctx0` CPS-transformiert, und der gesamte `if`-Ausdruck wird in ein `let` eingebettet, das `k` einführt.

    * **`lambda`-Ausdrücke:** Ein `lambda`-Ausdruck `(lambda (x) body)` wird in einen neuen `lambda`-Ausdruck transformiert, der ein zusätzliches Argument `k` (die Fortsetzung) nimmt: `(lambda (x k) (cps1 body ctx0))`. Der Rumpf des ursprünglichen Lambdas wird mit dem Tail-Kontext `ctx0` CPS-transformiert.

    * **Binäre Operationen (`op a b`):** Die Operanden `a` und `b` werden sequentiell CPS-transformiert. Die Fortsetzung für `a` nimmt ihr Ergebnis `v1` und transformiert dann `b` mit einer Fortsetzung, die ihr Ergebnis `v2` nimmt. Schließlich wird der ursprüngliche Kontext `ctx` auf den Ausdruck angewendet, der durch den Operator `op` und die CPS-transformierten Ergebnisse `v1` und `v2` gebildet wird.

    * **Funktionsapplikationen (`rator rand`):** Der `rator` (Funktion) und `rand` (Argument) werden sequentiell CPS-transformiert.
        * Wenn der `rator` ein `trivial?`-Operator ist, wird der aktuelle Kontext `ctx` direkt auf das Ergebnis der Anwendung des Operators auf den Operanden angewendet.
        * Wenn der aktuelle Kontext ein Tail-Kontext (`ctx0`) ist, wird die CPS-transformierte Funktion `r` mit dem CPS-transformierten Argument `d` und der aktuellen Fortsetzung `k` aufgerufen. Dies stellt korrekte Tail-Aufrufe sicher.
        * Andernfalls (Non-Tail-Aufruf) wird eine neue Fortsetzung erzeugt, die das Ergebnis des Funktionsaufrufs nimmt und den ursprünglichen Kontext `ctx` darauf anwendet. Die CPS-transformierte Funktion `r` wird mit dem CPS-transformierten Argument `d` und dieser neuen Fortsetzung aufgerufen.

**5. Tests:**

* Der Code enthält mehrere Testfälle, die die Transformation verschiedener Arten von Ausdrücken demonstrieren, einschließlich Variablen, Lambda-Funktionen, `if`-Ausdrücke in verschiedenen Kontexten und Funktionsapplikationen.

**6. Fakultätsbeispiel:**

* Die `fact-cps`-Definition zeigt, wie der CPS-Transformer auf eine rekursive Fakultätsfunktion angewendet werden kann.
* Die `pretty-print`-Ausgabe zeigt die CPS-transformierte Version der Fakultätsfunktion, die nun ein zusätzliches Fortsetzungsargument `k` nimmt.
* Die letzte Zeile wertet die CPS-transformierte Fakultätsfunktion mit der Eingabe `5` und einer Top-Level-Fortsetzung `(lambda (v) v)` aus, die einfach den Endwert zurückgibt.

**Zusammenfassend implementiert dieser Code eine CPS-Transformation, die darauf abzielt:**

* Ausdrücke in Continuation-Passing Style umzuwandeln.
* Korrekte Tail-Call-Optimierung sicherzustellen, indem die aktuelle Fortsetzung explizit übergeben wird.
* `if`-Ausdrücke effizient zu behandeln, ohne den umgebenden Kontext zu duplizieren, wenn das `if` selbst in einer Tail-Position steht. Dies wird erreicht, indem die `if`-Struktur beibehalten und die Zweige mit demselben Kontext CPS-transformiert werden. Wenn das `if` nicht in einer Tail-Position steht, führt es eine neue Fortsetzung ein, um das Ergebnis zu behandeln.