---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 最長ユニーク文字部分文字列の長さ
translated: true
type: note
---

**問題**: 繰り返し文字を含まない最長の部分文字列の長さを求めよ。

**解法**: スライディングウィンドウ + HashMap（または配列、小文字のみの場合）

2つのポインタ（`left` と `right`）を使用してウィンドウ `[left, right]` を維持します。  
`right` を移動させながら、`s[right]` が現在のウィンドウ内に既に存在するかチェックします：
- 存在する場合、重複がなくなるまで `left` を前方に移動させます。
- 各文字が最後に出現した位置を記録し、`left` を直接ジャンプさせます。

この解法は **O(n)** 時間、**O(1)** 空間で動作します（最大26または128文字）。

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

### テストケース

```python
print(lengthOfLongestSubstring("abacabcbb"))  # 3 ("abc" or "bac")
print(lengthOfLongestSubstring("bbbbb"))      # 1 ("b")
print(lengthOfLongestSubstring("pwwkew"))     # 3 ("wke")
```

**例の説明**:
- "abacabcbb" → "abc" または "bac" 長さ = 3
- "bbbbb" → "b" のみ 長さ = 1
- "pwwkew" → "wke" 長さ = 3（注: "pwke" も有効ですが、"ww" が先に条件を破ります）

文字セットがASCIIであることが分かっている場合は、dictの代わりにサイズ128のリストを使用して、わずかに高速な定数時間アクセスを実現することもできます。