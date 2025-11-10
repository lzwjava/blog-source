---
audio: false
generated: true
lang: hi
layout: post
title: चेज़ स्कीम फैक्टोरियल प्रोग्राम
translated: true
type: note
---

यहाँ एक सरल Chez Scheme प्रोग्राम है जो किसी संख्या का फैक्टोरियल कैलकुलेट करता है। इसे `factorial.scm` के रूप में सेव करें:

```scheme
(define (factorial n)
  (if (<= n 1)
      1
      (* n (factorial (- n 1)))))

(display "Factorial of 5 is: ")
(display (factorial 5))
(newline)
```

इसे रन करने के लिए:
1. कोड को `factorial.scm` नाम की फाइल में सेव करें।
2. अपने टर्मिनल में, उस डायरेक्टरी में नेविगेट करें जहाँ फाइल है।
3. रन करें: `scheme --script factorial.scm`

यह आउटपुट देगा:
```
Factorial of 5 is: 120
```

यह प्रोग्राम एक रिकर्सिव `factorial` फंक्शन को डिफाइन करता है और 5 का फैक्टोरियल कंप्यूट करता है। `--script` ऑप्शन (जैसा कि `scheme --help` आउटपुट में दिखाया गया है) आपको फाइल को सीधे रन करने की अनुमति देता है।