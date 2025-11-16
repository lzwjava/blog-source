---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 修復 Python 3.13 正則表達式錯誤
translated: true
type: note
---

你所遇到的錯誤是由於 **Python 3.13** 對於正則表達式語法的檢查比之前的版本更為嚴格所致。

具體來說，`wikiextractor/extract.py` 中（大約在第 378 行）的這行程式碼在 Python 3.13 中現已無效：

```python
ExtLinkBracketedRegex = re.compile(
    '\\[(((?i)' + '|'.join(wgUrlProtocols) + ')' + EXT_LINK_URL_CLASS + r'+)\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\]',
    re.S | re.U)
```

問題在於字串拼接後置於字串中間的內嵌旗標 `(?i)`。從 Python 3.12/3.13 開始，**像 `(?i)` 這樣的內嵌旗標，除了能放在正則表達式模式的最開頭之外，不再允許放在其他任何位置**。

### 快速修復（適用於 Python 3.13）

編輯檔案：

```bash
~/.local/lib/python3.13/site-packages/wikiextractor/extract.py
```

找到大約第 378 行，並將損壞的程式碼區塊替換為以下修正後的版本：

```python
# 舊的損壞寫法（在 Python 3.13 上失敗）
# ExtLinkBracketedRegex = re.compile(
#     '\\[(((?i)' + '|'.join(wgUrlProtocols) + ')' + EXT_LINK_URL_CLASS + r'+)\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\]',
#     re.S | re.U)

# 修正版本 – 將大小寫不敏感旗標移至 re.compile 的旗標參數中
protocol_pattern = '|'.join(wgUrlProtocols)
ExtLinkBracketedRegex = re.compile(
    r'\\['
    r'(((' + protocol_pattern + r')' + EXT_LINK_URL_CLASS + r'+)'
    r'\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\])',
    re.IGNORECASE | re.DOTALL | re.UNICODE
)
```

或者更簡潔的寫法（推薦）：

```python
ExtLinkBracketedRegex = re.compile(
    r'\\['
    r'(((' + '|'.join(wgUrlProtocols) + r')' + EXT_LINK_URL_CLASS + r'+)'
    r'\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\])',
    re.I | re.S | re.U
)
```

`re.I` 與 `re.IGNORECASE` 相同，可以作為旗標傳遞，而不需要將 `(?i)` 嵌入到模式內部。

### 替代解決方案

1. 使用 Python 3.11 或 3.12（最簡單，如果你不想修補）
   ```bash
   python3.11 -m pip install wikiextractor
   # 然後使用 python3.11 wikiextractor ... 執行
   ```

2. 使用已維護且修復了 Python 3.13 相容性的分支：
   ```bash
   pip uninstall wikiextractor
   pip install git+https://github.com/attardi/wikiextractor.git
   ```

   Giuseppe Attardi 的分支已針對 Python 3.12+ 進行更新，並在 3.13 上運行良好。

3. 使用非常快速的現代替代方案（強烈推薦用於處理大型傾印檔案）：
   ```bash
   pip install wikiextractor-ng   # 或者 "wiki-dump-tools", "wikitextprocessor" 等
   ```

套用修補程式或切換到已修復的分支後，你的指令將再次正常運作：

```bash
wikiextractor *.bz2
```

如果你需要一行指令的修補方法或確切的 `sed` 指令來自動修復，請告訴我。