---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Python 正則表達式指南
translated: true
type: note
---

### 導入 `re` 模組
`re` 模組（正則表達式的縮寫）是 Python 標準函式庫的一部分。它並非獨立的「正則表達式套件」，而是內建模組。請在腳本頂部導入：

```python
import re
```

### 基本概念
正則表達式（regex）是用於匹配、搜尋和操作字串的模式。它們使用特殊字符，例如：
- `.`（任意字符）
- `*`（零次或多次出現）
- `+`（一次或多次出現）
- `[]`（字符類別，例如 `[a-z]` 表示小寫字母）
- `^`（字串開頭），`$`（字串結尾）

範例基於 Python 的 `re` 文檔。為提升效率，複雜模式應使用 `re.compile()` 進行編譯。

### 主要功能與用法

#### 1. **從開頭匹配模式**
   - `re.match(pattern, string)`：檢查模式是否從字串開頭匹配。
   - 返回匹配物件或 `None`。

   範例：
   ```python
   import re
   result = re.match(r"Hello", "Hello world")
   print(result.group())  # 輸出：Hello
   ```

#### 2. **在字串任意位置搜尋**
   - `re.search(pattern, string)`：尋找模式在任意位置的首次出現。
   - 返回匹配物件或 `None`。

   範例：
   ```python
   result = re.search(r"world", "Hello world")
   print(result.group())  # 輸出：world
   ```

#### 3. **尋找所有匹配**
   - `re.findall(pattern, string)`：返回所有非重疊匹配的列表。

   範例：
   ```python
   matches = re.findall(r"\d+", "I have 3 cats and 42 dogs")
   print(matches)  # 輸出：['3', '42']
   ```

#### 4. **分割字串**
   - `re.split(pattern, string)`：根據模式出現位置分割字串。

   範例：
   ```python
   parts = re.split(r"\s+", "Hello    world   example")
   print(parts)  # 輸出：['Hello', 'world', 'example']
   ```

#### 5. **替換匹配內容**
   - `re.sub(pattern, replacement, string)`：將匹配內容替換為指定字串。

   範例：
   ```python
   new_string = re.sub(r"bad", "good", "This is bad")
   print(new_string)  # 輸出：This is good
   ```

#### 6. **編譯模式以供重複使用**
   - 為提升效能，可將正則表達式編譯為模式物件供重複使用。

   範例：
   ```python
   pattern = re.compile(r"\d+")
   matches = pattern.findall("Room 101 and 102")
   print(matches)  # 輸出：['101', '102']
   ```

### 最佳實踐
- 使用原始字串（`r""`）定義正則表達式模式，避免反斜線轉義問題。
- 處理匹配物件：使用 `.group()` 獲取匹配內容，`.span()` 獲取索引位置。
- 複雜任務可透過線上工具或 Python 互動式 shell 測試模式。
- 更多範例與標誌（如 `re.IGNORECASE`）請參考 Python 官方文檔：https://docs.python.org/3/library/re.html。

如有具體使用情境或錯誤，請提供更多細節！