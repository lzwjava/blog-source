---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 修復 wikiextractor 的 Python 3.13 正則表達式錯誤
translated: true
type: note
---

您遇到的錯誤是由於 `wikiextractor` 套件與 Python 3.13 對正則表達式內聯標誌的嚴格處理存在兼容性問題。具體來說，正則表達式模式中的 `(?i)` 標誌被解釋為全局標誌，但未置於表達式開頭，導致了 `re.PatternError`。

要修復此問題，請編輯檔案 `/home/lzw/.local/lib/python3.13/site-packages/wikiextractor/extract.py` 並修改第 378 行（或附近的 `ExtLinkBracketedRegex` 定義）如下：

- 原始代碼：`'\\[(((?i)' + '|'.join(wgUrlProtocols) + ')' + EXT_LINK_URL_CLASS + r'+)\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\]',`
- 更新後：`'\\[(((?i:' + '|'.join(wgUrlProtocols) + ')' + EXT_LINK_URL_CLASS + r'+)\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\]',`

此修改在 `(?i` 後添加了 `:`，將其轉換為僅適用於協議匹配組的局部內聯標誌 `(?i:...)`，從而解決解析錯誤。

此外，`SyntaxWarning: invalid escape sequence '\\['` 警告來自包含 Python 3.13 更嚴格處理的轉義字符的非原始字符串（儘管這些警告不會導致主要故障）。您可以暫時忽略這些警告，或若覺得困擾，可在同一檔案中將這些字符串更新為原始字符串（例如 `r'\\['`）。

編輯完成後，重新運行 `wikiextractor *.bz2`。如果套件版本過舊，可考慮通過 `pip install --upgrade wikiextractor` 檢查更新，或使用舊版 Python（例如 3.10）的虛擬環境作為臨時解決方案。