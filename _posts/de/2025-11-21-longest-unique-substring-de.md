---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Längste Teilzeichenkette mit eindeutigen Zeichen
translated: true
type: note
---

**Problem**: Finden Sie die Länge des längsten Teilstrings ohne wiederholte Zeichen.

**Solution**: Sliding Window + HashMap (oder Array, da Kleinbuchstaben)

Wir verwenden zwei Zeiger (`left` und `right`), um ein Fenster `[left, right]` zu verwalten.  
Während wir `right` bewegen, prüfen wir, ob `s[right]` bereits im aktuellen Fenster vorhanden ist:
- Falls ja, bewegen wir `left` nach vorne, bis das Duplikat entfernt ist.
- Wir verfolgen die Position, an der jedes Zeichen zuletzt gesehen wurde, um `left` direkt zu verschieben.

Dies läuft in **O(n)** Zeit und **O(1)** Speicher (höchstens 26 oder 128 Zeichen).

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

### Test cases

```python
print(lengthOfLongestSubstring("abacabcbb"))  # 3 ("abc" or "bac")
print(lengthOfLongestSubstring("bbbbb"))      # 1 ("b")
print(lengthOfLongestSubstring("pwwkew"))     # 3 ("wke")
```

**Explanation of examples**:
- "abacabcbb" → "abc" oder "bac" Länge = 3
- "bbbbb" → nur "b" Länge = 1
- "pwwkew" → "wke" Länge = 3 (Hinweis: "pwke" ist auch gültig, aber "ww" bricht es früher ab)

Sie können auch eine Liste der Größe 128 anstelle eines Dicts für etwas schnellere konstante Zeit verwenden, wenn Sie wissen, dass der Zeichensatz ASCII ist.