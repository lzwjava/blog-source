---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 修復HuggingFace下載代理設定
translated: true
type: note
---

是的 — 它**可以**使用你的代理，但從你貼上的輸出判斷，**你的代理目前並未啟用**。
這就是下載速度卡在**17.6 bytes/s**的原因 — 這是中國直連 HuggingFace 的典型症狀。

讓我告訴你**如何確認**以及**如何修復**這個問題。

---

# 1. 為何當前執行*未使用*代理

這行資訊：

```
78.0/630M [00:16<9947:51:33, 17.6B/s]
```

很明顯：如果透過 `HTTP_PROXY` / `HTTPS_PROXY` 設定了正確的代理（Clash、V2Ray、Shadowsocks），你應該會看到這樣的速度：

* 數百 KB/s
* 或數 MB/s
* 而不是 ~17 bytes/s

所以 Python 進程並未讀取到任何代理環境變數。

---

# 2. 檢查代理環境變數是否存在

請在執行以下指令的**同一個終端機**中：

```
python data/openwebtext_10k/prepare.py
```

執行：

```bash
echo $HTTP_PROXY
echo $HTTPS_PROXY
```

如果沒有顯示任何內容 → 表示變數未設定，所以 HuggingFace 無法使用代理。

---

# 3. 修復：為該終端機工作階段設定代理

以運行在 7890 埠的 Clash 為例：

```bash
export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"
```

如果使用 SOCKS5（例如 Shadowsocks）：

```bash
export HTTP_PROXY="socks5://127.0.0.1:1080"
export HTTPS_PROXY="socks5://127.0.0.1:1080"
```

**然後重新執行：**

```bash
python data/openwebtext_10k/prepare.py
```

現在你的下載速度應該會大幅提升。

---

# 4. 在 Python 內部進行額外檢查

在 `prepare.py` 開頭加入這些測試程式碼：

```python
import os
print("HTTP_PROXY:", os.getenv("HTTP_PROXY"))
print("HTTPS_PROXY:", os.getenv("HTTPS_PROXY"))
```

如果顯示 `None` → 你的 shell 未傳遞這些變數 → 請修復你的環境設定。

---

# 5. 可選：在載入資料集前用 `requests` 驗證

執行：

```python
import requests
print(requests.get("https://api.ipify.org?format=json", timeout=5).text)
```

* 如果回傳的 IP 屬於你的 VPN/代理 → 正常
* 如果顯示你家中的 ISP IP → 代理未啟用

---

# 6. 重要細節：HuggingFace 使用 **HTTP** 而非 SOCKS**，除非安裝 pysocks

如果你的代理是 SOCKS5，部分 Python 環境需要安裝 `PySocks` 才能正常運作：

```bash
pip install pysocks
```

安裝後 SOCKS 代理即可正常使用。

---

# 7. 總結

✔ HuggingFace *會*使用代理  
✔ 但僅在環境變數正確設定的情況下  
✘ 你的日誌顯示代理目前未啟用  
✔ 解決方案：在同一個 shell 中設定代理環境變數  

---

如果你需要，我可以協助：

* 調整你的 shell 設定檔（`.bashrc` 或 `.zshrc`）以持續使用代理
* 建立「代理開啟」/「代理關閉」的切換指令稿
* 修改你的 NanoGPT `prepare.py` 以在 Python 內部強制使用代理

請告訴我你希望採用哪種方案。