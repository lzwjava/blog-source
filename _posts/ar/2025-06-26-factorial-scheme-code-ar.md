---
audio: false
generated: true
lang: ar
layout: post
title: برنامج العاملي في تشيز سكيم
translated: true
type: note
---

إليك برنامج Chez Scheme بسيط يحسب عاملي رقم. احفظه باسم `factorial.scm`:

```scheme
(define (factorial n)
  (if (<= n 1)
      1
      (* n (factorial (- n 1)))))

(display "Factorial of 5 is: ")
(display (factorial 5))
(newline)
```

لتشغيله:
1. احفظ الكود في ملف باسم `factorial.scm`.
2. في طرفيتك، انتقل إلى الدليل الذي يحتوي على الملف.
3. شغّل: `scheme --script factorial.scm`

هذا سيعطي الناتج:
```
Factorial of 5 is: 120
```

يُعرّف البرنامج دالة `factorial` متكررة ويحسب عاملي الرقم 5. خيار `--script` (كما هو موضح في ناتج `scheme --help`) يسمح لك بتشغيل الملف مباشرة.