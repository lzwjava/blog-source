---
audio: false
generated: true
lang: de
layout: post
title: Chez-Scheme-Fakultätsprogramm
translated: true
type: note
---

Hier ist ein einfaches Chez Scheme-Programm, das die Fakultät einer Zahl berechnet. Speichere es als `factorial.scm`:

```scheme
(define (factorial n)
  (if (<= n 1)
      1
      (* n (factorial (- n 1)))))

(display "Fakultät von 5 ist: ")
(display (factorial 5))
(newline)
```

So führst du es aus:
1. Speichere den Code in einer Datei namens `factorial.scm`.
2. Navigiere in deinem Terminal zu dem Verzeichnis, das die Datei enthält.
3. Führe aus: `scheme --script factorial.scm`

Dies gibt Folgendes aus:
```
Fakultät von 5 ist: 120
```

Das Programm definiert eine rekursive `factorial`-Funktion und berechnet die Fakultät von 5. Die Option `--script` (wie in der `scheme --help`-Ausgabe gezeigt) ermöglicht es, die Datei direkt auszuführen.