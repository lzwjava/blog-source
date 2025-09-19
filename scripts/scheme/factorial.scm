(define (factorial n)
  (if (<= n 1)
      1
      (* n (factorial (- n 1)))))

(display "Factorial of 5 is: ")
(display (factorial 5))
(newline)
