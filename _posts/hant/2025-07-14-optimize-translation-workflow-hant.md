---
audio: false
generated: true
lang: hant
layout: post
title: 以段落哈希優化翻譯
translated: true
type: note
---

### 關於優化翻譯工作流程的思考

你的目標很明確：透過僅重新翻譯已更改或新增的段落，同時快取未更改的內容，將 Jekyll 部落格文章（以 Markdown 撰寫）翻譯成 8 種語言時，盡量減少 AI token 的使用量。你希望堅持使用 Markdown 進行編輯，避免對核心內容使用資料庫/JSON/YAML，並處理特殊元素如程式碼區塊（這些不應翻譯）。基於段落的方法很合理，因為它符合你的寫作和編輯方式——在這個層級上，翻譯的語境準確性會比句子級別更高。

主要挑戰：
- **識別變更**：在沒有版本控制差異的情況下，你需要一種方法來檢測哪些內容是新增/更改/未更改的。對段落進行雜湊處理（例如，對標準化的英文文字使用 SHA-256）是高效且無狀態的——無需儲存完整的舊版本。
- **處理 Markdown 結構**：你不能僅靠 `\n\n` 來分割，因為程式碼區塊、標題、列表或其他語法可能會破壞結構。對於基本文章，簡單的基於正規表示式的分割器可能有效，但使用輕量級 Markdown 解析器能更好地保留結構並跳過不可翻譯的部分。
- **快取**：保持基於檔案的簡單快取（例如，JSON 檔案或檔案目錄），避免使用資料庫。按段落雜湊值和語言進行快取。
- **Token 節省**：對於長篇文章，這可以在小幅編輯時減少 80-90% 的使用量，因為只有受影響的段落會呼叫 AI API。
- **邊緣情況**：新增/刪除的段落（透過重新雜湊處理）；微小調整（例如，拼寫錯誤修正）將觸發重新翻譯，除非你標準化空白字元/標點符號；必須排除程式碼區塊或行內程式碼；如果段落重新排序，雜湊值將不匹配，但如果你將其視為「新增」則沒問題。
- **整合**：在你的 Jekyll 工作流程中（例如，透過 bash 腳本或 Git hook）將其作為建置前腳本執行。如果你單獨生成翻譯後的 Markdown 檔案，則不需要 Jekyll 外掛。

這比句子級別（AI 的語境準確性較低）或全文翻譯（沒有節省）更可取。對於寫作想法來說，YAML/JSON 確實會很繁瑣——堅持使用 Markdown。

### 建議的最佳方式：具有快取和 Markdown 感知解析的段落雜湊處理

使用 Python 腳本：
1. 將英文 Markdown 解析為「可翻譯單元」（段落，排除程式碼區塊、標題等）。
2. 對每個單元的英文文字進行雜湊處理（標準化，例如，去除多餘的空白字元）。
3. 檢查基於檔案的快取中是否存在按雜湊值/語言分類的現有翻譯。
4. 透過你的 AI 工具（例如，DeepSeek/Mistral API）翻譯缺失的內容。
5. 快取新翻譯。
6. 重新組合翻譯後的 Markdown 檔案，保留不可翻譯的部分。

**為什麼這是最佳方式**：
- **簡單且低開銷**：無需資料庫，僅使用檔案。除了 AI 呼叫外，可在本地/離線執行。
- **靈活**：透過跳過程式碼區塊來處理它們。可擴展到其他 Markdown 元素（例如，如果標題較短則不翻譯）。
- **成本效益高**：僅為新增/更改的段落付費。對於一篇 10 段落的文章，編輯一段可節省約 90% 的 token。
- **易於維護**：自然地編輯英文 Markdown；腳本處理其餘部分。
- **所需工具**：Python（你可能已經安裝）。函式庫：`hashlib`（內建用於雜湊處理），`markdown` 或 `mistune` 用於解析（如果需要；對於「無特殊語法」的情況，可先從簡單的正規表示式開始）。

#### 逐步實施

1. **設定**：
   - 建立一個 `translations_cache.json` 檔案（或一個像 `cache/` 這樣的目錄，其中包含用於可擴展性的 hash.json 檔案）。
   - 結構：`{ "hash1": { "fr": "翻譯文字", "es": "...", ... }, "hash2": { ... } }`
   - 將其儲存在你的部落格儲存庫中（如果敏感則使用 git-ignore）或單獨的目錄中。
   - 在腳本中列出你的 8 種語言（例如，['fr', 'es', 'de', ...]）。

2. **解析 Markdown**：
   - 對於簡單情況（段落 + 程式碼區塊）：使用逐行處理來檢測圍欄程式碼區塊（``````` 或 `~~~`）和縮排程式碼（>3 個空格）。
   - 將「段落」收集為連續的非程式碼、非空白行區塊。
   - 更好：使用 Python 的 `markdown` 函式庫轉換為 HTML，然後提取文字，但這對於重新組合會有損耗。相反，使用 `mistune`（一個快速的 Markdown 解析器）來獲取 AST（抽象語法樹），這讓你可以遍歷和修改可翻譯節點（例如，「段落」節點）。
   - 如果需要，安裝 `mistune`（但你的環境有基礎工具；假設你可以在本地 pip 安裝）。

3. **雜湊處理**：
   - 標準化：`text.strip().lower()` 或僅 `.strip()` 以忽略空白字元變更（如果需要的話）（但這可能會錯過有意義的編輯）。
   - 雜湊：`hashlib.sha256(normalized.encode()).hexdigest()`

4. **翻譯**：
   - 使用你的 AI API 包裝器（例如，對於 DeepSeek：發送提示如「將此段落翻譯成法文：{text}」）。
   - 如果可能，進行批次處理，但由於段落較小，順序處理也可以。

5. **重新組合**：
   - 透過將可翻譯區塊替換為快取/新的翻譯來重建 Markdown，保持程式碼/標題不變。

6. **腳本執行**：
   - 執行：`python translate_blog.py path/to/english.md`
   - 輸出：`path/to/fr.md`、`path/to/es.md` 等。
   - 對於 Jekyll：將這些檔案放在 `_posts/` 中，並加上語言前綴，或使用像 `jekyll-polyglot` 這樣的多語言外掛來處理。

#### 範例 Python 腳本

這是一個使用逐行解析的基本版本（除了內建函式庫外，無需外部函式庫）。它假設簡單的 Markdown：段落由空白行分隔，圍欄程式碼區塊。對於複雜語法，升級到 `mistune`。

```python
import hashlib
import json
import os
import sys
# 假設你有一個 AI 翻譯函數；替換為你的 DeepSeek/Mistral API 呼叫
def ai_translate(text, lang):
    # 佔位符：回傳 API 呼叫結果
    return f"Translated to {lang}: {text}"  # 替換為真實 API

CACHE_FILE = 'translations_cache.json'
LANGUAGES = ['fr', 'es', 'de', 'it', 'pt', 'zh', 'ja', 'ko']  # 你的 8 種語言

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f, indent=4)

def compute_hash(text):
    normalized = text.strip()  # 自訂標準化
    return hashlib.sha256(normalized.encode('utf-8')).hexdigest()

def parse_markdown(md_text):
    lines = md_text.splitlines()
    blocks = []
    current_block = []
    in_code = False
    for line in lines:
        if line.strip().startswith('```') or line.strip().startswith('~~~'):
            in_code = not in_code
            if current_block:
                blocks.append(('text', '\n'.join(current_block)))
                current_block = []
            blocks.append(('code', line))
            continue
        if in_code:
            blocks.append(('code', line))
        else:
            if line.strip():  # 非空白
                current_block.append(line)
            else:
                if current_block:
                    blocks.append(('text', '\n'.join(current_block)))
                    current_block = []
    if current_block:
        blocks.append(('text', '\n'.join(current_block)))
    return blocks

def translate_post(english_md_path):
    with open(english_md_path, 'r') as f:
        md_text = f.read()
    
    blocks = parse_markdown(md_text)
    cache = load_cache()
    
    for lang in LANGUAGES:
        translated_blocks = []
        for block_type, content in blocks:
            if block_type == 'code':
                translated_blocks.append(content)
            else:  # text
                h = compute_hash(content)
                if h not in cache:
                    cache[h] = {}
                if lang not in cache[h]:
                    translation = ai_translate(content, lang)
                    cache[h][lang] = translation
                translated_blocks.append(cache[h][lang])
        
        # 用換行符重新組合
        translated_md = '\n\n'.join(translated_blocks)  # 根據 Markdown 格式化進行調整
        output_path = english_md_path.replace('.md', f'_{lang}.md')
        with open(output_path, 'w') as f:
            f.write(translated_md)
    
    save_cache(cache)
    print("Translations updated.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py path/to/english.md")
    else:
        translate_post(sys.argv[1])
```

**如何使用**：
- 將 `ai_translate` 替換為你的 API 邏輯。
- 在編輯後對你的文章檔案執行。
- 對於標題/列表：擴展 `parse_markdown` 來檢測（例如，將以 `#` 或 `-` 開頭的行視為獨立區塊）。
- 如果文章有圖片/連結：由於它們位於文字區塊中，因此保持不變。
- 標準化提示：如果你想忽略微小的標點符號變更，請在雜湊處理前使用正規表示式去除它們。

#### 增強功能
- **Git 整合**：使用 `git diff` 預先識別更改的行，但雜湊處理更簡單。
- **批次翻譯**：如果 API 支援，一次發送多個新段落。
- **錯誤處理**：重試失敗的 API 呼叫；驗證翻譯。
- **進階解析**：Pip 安裝 `mistune` 並使用其渲染器來自訂（例如，跳過 'code_block' 節點）。
- **測試**：使用 SHA-256 時雜湊衝突很少見；在範例文章上進行測試。

這應該可以在不使你的工作流程複雜化的情況下節省 token。如果你的 Markdown 更複雜，請從此開始並迭代。如果你需要調整或 API 整合方面的幫助，請告訴我！