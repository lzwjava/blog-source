---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 使用代理與Hugging Face數據集
translated: true
type: note
---

是的 — `datasets` 會遵循你的**系統/環境代理設定**，但它**沒有**自己的代理配置。
所以當你在中國時，完全可以透過代理下載 Hugging Face 的資料集。

具體方法如下。

---

# 如何讓 `load_dataset` 使用代理（中國適用）

## 1. 設定 HTTP/HTTPS 代理環境變數

`datasets` 內部使用 Python 的 `requests` 函式庫。
`requests` 會自動使用標準的代理環境變數：

### Linux / macOS

```bash
export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"
```

若你的代理使用 SOCKS5：

```bash
export HTTP_PROXY="socks5://127.0.0.1:1080"
export HTTPS_PROXY="socks5://127.0.0.1:1080"
```

### Windows (PowerShell)

```powershell
setx HTTP_PROXY "http://127.0.0.1:7890"
setx HTTPS_PROXY "http://127.0.0.1:7890"
```

然後重新開啟終端機。

---

## 2. 若你在程式碼中執行 Python（如 Jupyter），請在 Python 內部設定

```python
import os

os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'
```

這個方法可靠有效。

---

## 3. 確認代理正常運作

你可以透過以下方式測試：

```python
import requests
print(requests.get("https://api.ipify.org?format=json").text)
```

若顯示的 IP 是你的代理出口節點，則 Hugging Face 資料集下載也會透過該代理進行。

---

## 4. Hugging Face 的 `huggingface_hub` 同樣遵循這些變數

`datasets` 內部使用 `huggingface_hub`，而它**同樣**遵循：

* `HTTP_PROXY`
* `HTTPS_PROXY`
* `http_proxy`
* `https_proxy`

因此一旦設定環境變數，模型與資料集下載都會自動使用你的代理。

---

# 在中國使用的注意事項

* Hugging Face 原始下載通常需要代理，因為其服務端點位於美國/歐洲。
* 若遇到 `.zst` 資料集檔案下載超時，在無代理情況下屬正常現象。
* 全域代理（Clash、V2Ray、Qv2ray 等）會讓一切更順暢。

---

# 如果你需要，我可以示範：

* 如何確保 NanoGPT 透過你的代理下載資料集
* 如何將資料集快取至本地避免重複下載
* 如何在中國本地鏡像 Hugging Face 資料集（例如清華鏡像解決方案）

只需告訴我你的需求。