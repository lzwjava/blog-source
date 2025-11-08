---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: फ्लेक्सबॉक्स के साथ स्टैक्ड फॉर्म एलिमेंट्स को केंद्रित करना
translated: true
type: note
---

```css
.sort-container {
    display: flex;
    flex-direction: column; /* आइटम्स को लंबवत रूप से स्टैक करने के लिए इसे जोड़ें */
    align-items: center; /* कॉलम में आइटम्स को क्षैतिज रूप से केंद्रित करता है */
    justify-content: center; /* कॉलम को लंबवत रूप से केंद्रित करता है */
    gap: 10px;
    margin-bottom: 1rem;
}

.sort-container select {
    padding: 5px;
    font-size: 16px;
}

.sort-container .post-number {
    font-size: 16px;
}
```

### व्याख्या
- **flex-direction: column**: मुख्य अक्ष को क्षैतिज (पंक्ति) से लंबवत में बदलता है, जिससे `select` और `.post-number` एलिमेंट्स ऊपर से नीचे की ओर स्टैक हो जाते हैं।
- **align-items: center**: चाइल्ड एलिमेंट्स के क्षैतिज केंद्रीकरण को बनाए रखता है।
- **justify-content: center**: पूरे लंबवत स्टैक को कंटेनर के भीतर केंद्रित करता है।
- मैंने नेस्टेड सेलेक्टर सिंटैक्स को भी ठीक किया है (बेहतर प्रैक्टिस के लिए `select` और `.post-number` को मुख्य ब्लॉक के बाहर ले जाया गया है, यह मानते हुए कि वे डायरेक्ट चाइल्ड हैं—ज़रूरत पड़ने पर एडजस्ट करें)। `gap` अब आइटम्स के बीच लंबवत रूप से लागू होता है।