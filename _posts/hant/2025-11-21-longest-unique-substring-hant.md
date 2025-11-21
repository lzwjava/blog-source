---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 最長不重複字符子串長度
translated: true
type: note
---

**問題**：找出最長不重複字符子串的長度。

**解決方案**：滑動窗口 + HashMap（或數組，因僅含小寫字母）

我們使用兩個指針（`left` 和 `right`）來維護一個窗口 `[left, right]`。  
當移動 `right` 時，檢查 `s[right]` 是否已在當前窗口中出現：
- 若是，則將 `left` 向前移動，直到重複字符被移除。
- 記錄每個字符最後出現的位置，以便直接跳轉 `left`。

此方法時間複雜度為 **O(n)**，空間複雜度為 **O(1)**（最多 26 或 128 個字符）。

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

### 測試案例

```python
print(lengthOfLongestSubstring("abacabcbb"))  # 3 ("abc" or "bac")
print(lengthOfLongestSubstring("bbbbb"))      # 1 ("b")
print(lengthOfLongestSubstring("pwwkew"))     # 3 ("wke")
```

**範例說明**：
- "abacabcbb" → "abc" 或 "bac" 長度 = 3
- "bbbbb" → 僅 "b" 長度 = 1
- "pwwkew" → "wke" 長度 = 3（注意："pwke" 亦有效，但 "ww" 會提前中斷）

若已知字符集為 ASCII，亦可使用大小為 128 的列表代替字典，以獲得更快的常數時間操作。