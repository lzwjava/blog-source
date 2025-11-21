---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: सबसे लंबा अद्वितीय अक्षर उपस्ट्रिंग लंबाई
translated: true
type: note
---

**समस्या**: बिना दोहराए वर्णों वाली सबसे लंबी उपस्ट्रिंग की लंबाई ज्ञात करें।

**हल**: स्लाइडिंग विंडो + HashMap (या लोअरकेस अक्षरों के लिए सरणी)

हम एक विंडो `[left, right]` को बनाए रखने के लिए दो पॉइंटर्स (`left` और `right`) का उपयोग करते हैं।  
जैसे ही हम `right` को आगे बढ़ाते हैं, हम जांचते हैं कि क्या `s[right]` वर्तमान विंडो में पहले से मौजूद है:
- यदि हाँ, तो `left` को तब तक आगे बढ़ाएँ जब तक डुप्लिकेट हट न जाए।
- प्रत्येक वर्ण को अंतिम बार कहाँ देखा गया था, यह ट्रैक करने के लिए `left` को सीधे उस स्थान पर ले जाएँ।

यह **O(n)** समय और **O(1)** स्थान में चलता है (अधिकतम 26 या 128 वर्ण)।

```python
def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0
    
    # char -> last seen index
    last_seen = {}
    max_len = 0
    left = 0
    
    for right in range(len(s)):
        ch = s[right]
        
        # If character is already in current window, shrink from left
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        else:
            # Update max length when window is valid
            max_len = max(max_len, right - left + 1)
        
        # Record the latest position of this character
        last_seen[ch] = right
    
    return max_len
```

### टेस्ट केस

```python
print(lengthOfLongestSubstring("abacabcbb"))  # 3 ("abc" or "bac")
print(lengthOfLongestSubstring("bbbbb"))      # 1 ("b")
print(lengthOfLongestSubstring("pwwkew"))     # 3 ("wke")
```

**उदाहरणों की व्याख्या**:
- "abacabcbb" → "abc" या "bac" लंबाई = 3
- "bbbbb" → केवल "b" लंबाई = 1
- "pwwkew" → "wke" लंबाई = 3 (ध्यान दें: "pwke" भी वैध है, लेकिन "ww" इसे पहले ही तोड़ देता है)

यदि आप जानते हैं कि वर्ण सेट ASCII है, तो आप थोड़े तेज स्थिर समय के लिए डिक्शनरी के बजाय 128 आकार की एक सूची का भी उपयोग कर सकते हैं।