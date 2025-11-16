---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 修復緩慢的Hugging Face下載
translated: true
type: note
---

這是在透過代理下載大型 HF 資料集時常見的問題。以下因素組合：

* 多個數百 MB 的大型檔案
* Python `requests` / `huggingface_hub`
* 本地 HTTP 代理（特別是 Clash、V2Ray 或 tun2socks）

經常導致極慢的傳輸速度或連線重設。

以下是最有效的解決方法。

---

## 1. **最佳解決方案：使用 `hf_transfer`**

Hugging Face 提供了一個加速下載工具，可帶來 **10 倍至 50 倍更快** 的速度且更穩定。

安裝：

```bash
pip install hf_transfer
export HF_HUB_ENABLE_HF_TRANSFER=1
```

再次執行您的指令。

僅此一項通常就能解決透過代理下載緩慢的問題。

---

## 2. 搭配 Hugging Face CLI 使用 `aria2c`（對超大檔案最快速）

若手動下載：

```bash
pip install huggingface_hub[cli]
sudo apt install aria2
```

然後下載：

```bash
huggingface-cli download --repo-type dataset openwebtext --local-dir ./openwebtext --local-dir-use-symlinks False
```

HF CLI 會自動使用 aria2，它能比 `requests` 更好地處理：

* 並行連線
* 續傳
* 不穩定的代理

---

## 3. 針對本地代理緩慢的修復：使用系統級 SOCKS 替代 HTTP

若您使用類似：

```
HTTP_PROXY=http://127.0.0.1:7890
HTTPS_PROXY=http://127.0.0.1:7890
```

請切換至 SOCKS5（如果您的代理支援）：

```bash
export ALL_PROXY=socks5://127.0.0.1:7891
```

SOCKS 對於大型檔案串流**穩定得多**。

---

## 4. 對大型檔案停用代理

如果您的原始網路連線良好，但代理導致速度變慢：

```bash
unset HTTP_PROXY
unset HTTPS_PROXY
unset ALL_PROXY
```

然後重試。根據地區，部分 HF 伺服器即使不透過代理也很快。

---

## 5. 使用 HF 鏡像（中國大陸 / 台灣有時較慢）

您可以強制使用 CDN：

```bash
export HF_ENDPOINT=https://hf-mirror.com
```

然後再次執行。
這對某些地區能顯著提升速度。

---

## 6. 恢復中斷的下載

HF 資料集快取位置：

```
~/.cache/huggingface/datasets/
```

若有任何檔案部分下載，HF 會自動續傳 — 無需從頭開始。

---

## 7. 若仍緩慢：避免下載完整資料集，改用小部分資料

OpenWebText 超過 40GB。
您可以僅載入一小部分：

```python
from datasets import load_dataset
ds = load_dataset("openwebtext", split="train[:1%]")
```

---

## 快速建議

最快速 + 最簡便：

```bash
pip install hf_transfer
export HF_HUB_ENABLE_HF_TRANSFER=1
python data/openwebtext_10k/prepare.py
```

您應能立即看到下載速度飆升。

---

如果您需要，我可以示範如何修改您的 `prepare.py`，以使用完全自訂的下載器，具備重試/退避機制和並行獲取功能，讓您的管道始終快速下載且永不卡頓。