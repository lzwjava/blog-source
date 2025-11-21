---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: أطول طول لسلسلة فرعية ذات أحرف فريدة
translated: true
type: note
---

**المشكلة**: إيجاد طول أطول سلسلة فرعية بدون أحرف متكررة.

**الحل**: نافذة منزلقة + خريطة تجزئة (أو مصفوفة نظرًا لأن الأحرف صغيرة)

نستخدم مؤشرين (`left` و `right`) للحفاظ على نافذة `[left, right]`.  
بينما نحرك `right`، نتحقق مما إذا كان `s[right]` قد ظهر مسبقًا في النافذة الحالية:
- إذا كان نعم، نحرك `left` للأمام حتى يتم إزالة الحرف المكرر.
- نتتبع الموضع الذي شوهد فيه كل حرف آخر مرة للقفز بـ `left` مباشرة.

يعمل هذا في وقت **O(n)** ومساحة **O(1)** (على الأكثر 26 أو 128 حرفًا).

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

### حالات الاختبار

```python
print(lengthOfLongestSubstring("abacabcbb"))  # 3 ("abc" or "bac")
print(lengthOfLongestSubstring("bbbbb"))      # 1 ("b")
print(lengthOfLongestSubstring("pwwkew"))     # 3 ("wke")
```

**شرح الأمثلة**:
- "abacabcbb" → "abc" أو "bac" الطول = 3
- "bbbbb" → فقط "b" الطول = 1
- "pwwkew" → "wke" الطول = 3 (ملاحظة: "pwke" صالحة أيضًا، لكن "ww" تكسرها في وقت أبكر)

يمكنك أيضًا استخدام قائمة بحجم 128 بدلاً من القاموس لوقت ثابت أسرع قليلاً إذا كنت تعلم أن مجموعة الأحرف هي ASCII.