---
audio: false
lang: hant
layout: post
title: 自然語言處理任務
translated: true
type: note
---

基礎自然語言處理任務是理解、處理和生成人類語言的基礎。以下是一些核心的自然語言處理任務：

### 1. **分詞**
   - 將文本分割成更小的單位，例如單詞、句子或子詞。
   - 範例：
     - 輸入："Natural Language Processing is fun!"
     - 輸出：["Natural", "Language", "Processing", "is", "fun", "!"]

### 2. **詞性標註**
   - 為句子中的單詞分配文法標籤（例如名詞、動詞、形容詞）。
   - 範例：
     - 輸入："I love NLP."
     - 輸出：[("I", "PRP"), ("love", "VBP"), ("NLP", "NN")]

### 3. **命名實體識別**
   - 識別並分類文本中的實體（例如人物、組織、地點）。
   - 範例：
     - 輸入："Barack Obama was born in Hawaii."
     - 輸出：[("Barack Obama", "PERSON"), ("Hawaii", "LOCATION")]

### 4. **情感分析**
   - 判斷文本傳達的情感或情緒（例如正面、負面、中性）。
   - 範例：
     - 輸入："I love this movie!"
     - 輸出："Positive"

### 5. **詞形還原與詞幹提取**
   - 將單詞還原為其詞根形式。
   - 範例：
     - 輸入："running", "ran", "runs"
     - 輸出（詞形還原）："run"
     - 輸出（詞幹提取）："run"

### 6. **停用詞移除**
   - 移除沒有重要意義的常見詞語（例如"and"、"is"、"the"）。
   - 範例：
     - 輸入："The cat is on the mat."
     - 輸出：["cat", "mat"]

### 7. **文本分類**
   - 將文本分類到預定義的類別或標籤中。
   - 範例：
     - 輸入："This is a sports article."
     - 輸出："Sports"

### 8. **語言建模**
   - 預測序列中的下一個詞語，或為詞語序列分配概率。
   - 範例：
     - 輸入："The cat sat on the ___"
     - 輸出：["mat" (0.8), "chair" (0.1), "floor" (0.1)]

### 9. **機器翻譯**
   - 將文本從一種語言翻譯成另一種語言。
   - 範例：
     - 輸入："Hello, how are you?"
     - 輸出："Hola, ¿cómo estás?"

### 10. **文本摘要**
   - 從較長的文本生成簡潔的摘要。
   - 範例：
     - 輸入："Natural language processing is a subfield of AI. It involves understanding and generating human language."
     - 輸出："NLP is a subfield of AI for understanding and generating language."

### 11. **共指消解**
   - 識別不同詞語是否指向同一實體。
   - 範例：
     - 輸入："Alice said she would come."
     - 輸出："Alice" -> "she"

### 12. **問答系統**
   - 根據給定的上下文或知識回答問題。
   - 範例：
     - 輸入：上下文："Paris is the capital of France."
       問題："What is the capital of France?"
     - 輸出："Paris"

### 13. **詞嵌入**
   - 將詞語表示為高維空間中的連續向量。
   - 範例：
     - 輸入："king", "queen", "man", "woman"
     - 輸出：關係如 "king - man + woman ≈ queen"

### 14. **拼寫檢查與文本正規化**
   - 修正拼寫錯誤並標準化文本（例如"u r" -> "you are"）。
   - 範例：
     - 輸入："I luv NLP!"
     - 輸出："I love NLP!"

### 15. **文本生成**
   - 從模型或輸入提示生成連貫的文本。
   - 範例：
     - 輸入："Once upon a time,"
     - 輸出："Once upon a time, there lived a brave knight in a faraway kingdom."

這些任務是構建更複雜自然語言處理系統和應用（例如聊天機械人、虛擬助手和推薦系統）的基礎組件。