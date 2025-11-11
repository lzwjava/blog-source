---
audio: false
generated: true
lang: hi
layout: post
title: पायथन इंटीजर
translated: true
type: note
---

पायथन में, `int` टाइप की **कोई fixed range या size limit नहीं** होती। C या Java जैसी भाषाओं के विपरीत, जहाँ integers specific bit sizes (जैसे 32-bit या 64-bit) तक सीमित होते हैं, पायथन का `int` arbitrary-precision वाला होता है, मतलब यह available memory के अनुसार जितना बड़ा हो सकता है, हो सकता है। यह बात पायथन 2 (पायथन 2.2 से, जहाँ `long` और `int` को एक कर दिया गया था) और पायथन 3 दोनों पर लागू होती है।

### मुख्य बातें:
- **कोई Upper या Lower Bound नहीं**: पायथन integers किसी भी पूर्ण संख्या, धनात्मक या ऋणात्मक, को represent कर सकते हैं, जो सिर्फ system की memory तक सीमित होते हैं। उदाहरण के लिए, आपके पास बेहद बड़ी संख्याएँ जैसे `10**100` या बहुत छोटी ऋणात्मक संख्याएँ जैसे `-10**100` हो सकती हैं।
- **Memory Usage**: एक `int` के लिए आवश्यक memory संख्या के magnitude के बढ़ने के साथ dynamically बढ़ती है। पायथन बड़े integers को store करने के लिए variable-length encoding का उपयोग करता है।
- **Performance**: बहुत बड़े integers (जैसे `2**1000000`) पर operations slower हो सकते हैं due to increased memory और computational overhead, लेकिन फिर भी उन्हें support किया जाता है।

### उदाहरण:
```python
# छोटा integer
small = 42
print(small, type(small))  # 42 <class 'int'>

# बड़ा integer
large = 2**1000
print(large, type(large))  # 107150860718626732... <class 'int'>

# ऋणात्मक integer
negative = -10**100
print(negative, type(negative))  # -10000000000... <class 'int'>
```

### आपके पिछले Query से संबंध:
आपके TigerOpen API issue में, `order_id` (`359248847525015552`) एक integer है जो पायथन की `int` range के अंदर ही है, इसलिए पायथन में ही overflow या truncation की कोई चिंता नहीं है। `biz param error` की संभावना API की expectations (जैसे, एक string `order_id` की आवश्यकता) के कारण है, न कि पायथन integer limitation के कारण। `get_order` call में `str(order_id)` try करने का सुझाव इस potential mismatch को address करता है।

### अतिरिक्त जानकारी:
- **System Limitations**: हालांकि पायथन के `int` की कोई theoretical limit नहीं है, practical limits available RAM से उत्पन्न होती हैं। बेहद बड़े integers (जैसे `2**1000000`) significant memory consume कर सकते हैं।
- **Type Checking**: यह जाँचने के लिए कि कोई variable एक integer है या नहीं, `isinstance(x, int)` का उपयोग करें।
- **Conversion**: आप strings या floats को integers में `int()` का उपयोग करके convert कर सकते हैं, लेकिन floats के साथ precision loss से बचने के लिए सावधान रहें (उदाहरण के लिए, `int(3.9)`, `3` देता है)।

यदि आपके पास पायथन में integers के बारे में और प्रश्न हैं या TigerOpen API issue के लिए मदद की आवश्यकता है, तो मुझे बताएं!