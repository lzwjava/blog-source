---
audio: false
generated: false
lang: hi
layout: post
title: न्यूरल नेटवर्क को समझना
translated: true
---

ज़िवेई:

क्या आप कोड समझा सकते हैं?

```python
        self.weights = [w-(eta/len(mini_batch))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb
                       for b, nb in zip(self.biases, nabla_b)]
```

इस कोड को हिंदी में समझाएं:

यह कोड एक न्यूरल नेटवर्क के वज़न (weights) और पूर्वाग्रह (biases) को अपडेट करने के लिए है। यह ग्रेडिएंट डिसेंट (gradient descent) एल्गोरिदम का उपयोग करता है, जहां `eta` सीखने की दर (learning rate) है और `mini_batch` ट्रेनिंग डेटा का एक छोटा हिस्सा है।

- `self.weights` और `self.biases` नेटवर्क के वर्तमान वज़न और पूर्वाग्रह हैं।
- `nabla_w` और `nabla_b` वज़न और पूर्वाग्रह के लिए ग्रेडिएंट हैं।
- `eta/len(mini_batch)` सीखने की दर को मिनी-बैच के आकार से विभाजित करता है, जिससे प्रत्येक अपडेट छोटा हो जाता है।
- `zip(self.weights, nabla_w)` और `zip(self.biases, nabla_b)` वज़न और ग्रेडिएंट, तथा पूर्वाग्रह और ग्रेडिएंट को जोड़ते हैं, ताकि प्रत्येक वज़न और पूर्वाग्रह को उसके संबंधित ग्रेडिएंट के साथ अपडेट किया जा सके।

