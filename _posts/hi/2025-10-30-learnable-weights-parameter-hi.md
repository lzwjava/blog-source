---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: पाइटॉर्च सीखने योग्य वज़नों के लिए पैरामीटर
translated: true
type: note
---

`torch.nn.Parameter` PyTorch में `torch.Tensor` का एक उपवर्ग है, जिसे विशेष रूप से न्यूरल नेटवर्क मॉड्यूल में सीखने योग्य पैरामीटर्स को दर्शाने के लिए डिज़ाइन किया गया है। इसका मुख्य उद्देश्य टेंसर्स को स्वचालित रूप से मॉड्यूल पैरामीटर्स के रूप में पंजीकृत करना है जब उन्हें `torch.nn.Module` के विशेषताओं के रूप में निर्दिष्ट किया जाता है, जिससे वे `module.parameters()` या `module.named_parameters()` जैसे तरीकों के माध्यम से सुलभ हो जाते हैं। यह प्रशिक्षण योग्य वज़न (जैसे, layers के लिए) को नियमित टेंसर्स से अलग करने में मदद करता है, जिससे अस्थायी गणनाओं (जैसे RNNs में cached states) को गलती से पैरामीटर्स के रूप में नहीं माना जाता।

### मुख्य विशेषताएं
- **स्वचालित पंजीकरण**: जब आप एक `Parameter` को किसी मॉड्यूल को निर्दिष्ट करते हैं (जैसे, कस्टम मॉड्यूल के `__init__` में `self.weight = nn.Parameter(torch.randn(3, 3))`), तो इसे अतिरिक्त कोड के बिना मॉड्यूल की पैरामीटर सूची में जोड़ दिया जाता है।
- **ग्रेडिएंट ट्रैकिंग**: डिफ़ॉल्ट रूप से, `requires_grad=True` होता है, इसलिए यह backpropagation में भाग लेता है। यह `torch.no_grad()` context के अंदर भी लागू रहता है—बेहतर नियंत्रण के लिए autograd के local disabling का उपयोग करें।
- **विशेषताएं**: यह सभी `Tensor` गुणों को विरासत में लेता है लेकिन अपने विशेष मॉड्यूल व्यवहार के अलावा कोई नई विशेषताएं नहीं जोड़ता।

### बुनियादी उपयोग
यहाँ एक कस्टम मॉड्यूल में एक सरल उदाहरण दिया गया है:

```python
import torch
import torch.nn as nn

class MyModule(nn.Module):
    def __init__(self):
        super().__init__()
        # यह स्वचालित रूप से एक पैरामीटर के रूप में पंजीकृत हो जाता है
        self.weight = nn.Parameter(torch.randn(2, 3))
        # एक साधारण टेंसर पंजीकृत नहीं होगा
        self.bias = torch.zeros(3)

    def forward(self, x):
        return x @ self.weight + self.bias

model = MyModule()
print(list(model.parameters()))  # आउटपुट: [Parameter containing: tensor(...)]
```

अधिक जानकारी के लिए, आधिकारिक दस्तावेज़ देखें: [Parameter — PyTorch 2.9 documentation](https://pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html)