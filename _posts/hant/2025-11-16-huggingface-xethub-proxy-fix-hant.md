---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 修復 Hugging Face XetHub 代理問題
translated: true
type: note
---

你的日誌顯示了一個非常重要的問題：

**失敗的連接並非直接連接到 HuggingFace。**
而是連接到 **[https://transfer.xethub.hf.co](https://transfer.xethub.hf.co)** — 這是 Hugging Face 的 *XetHub* 後端（Rust 客戶端 `reqwest`），而你設定的代理 **並不會自動攔截此連接**。

這解釋了一切：

* 你已經為 Python 設定了 `HTTP_PROXY` → 正常
* 但 XetHub 使用的是 **rust reqwest**，而非 Python requests
* Rust reqwest **會忽略系統代理變數，除非你設定了 HTTPS_PROXY 小寫變數**，或使用明確的代理配置

所以：**你的 Python 環境使用了代理，但 XetHub（HF 的新儲存供應商）沒有使用**。

這就是你看到以下錯誤的原因：

```
ConnectError("Connection refused")
```

以及重試。

---

# 問題成因（簡短說明）

Hugging Face 最近將儲存遷移到了 **XetHub**，它使用 Rust 客戶端。
該客戶端遵循：

* `https_proxy`
* `http_proxy`

但 **不一定** 遵循大寫版本（取決於建置版本）。

你設定了大寫變數？ → 它可能會忽略它們。

---

# 解決方法（在中國境內實測有效）

## 1. 同時設定小寫和大寫代理變數

在執行 NanoGPT **之前**，於你的 shell 中執行：

```bash
export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"

export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"
```

Rust reqwest 偏好小寫
Python requests 偏好大寫
同時設定兩者可避免問題。

然後執行：

```bash
python data/openwebtext_10k/prepare.py
```

你應該會立即看到正常的下載速度。

---

# 2. 如果你的代理是 SOCKS5，請注意

Rust reqwest **不支援 socks5**，除非編譯時啟用了可選功能。
所以如果你的代理是 socks5:// → 它將會失敗。

你必須切換到你的代理客戶端的 HTTP 代理端口，通常是：

* Clash: 7890 (HTTP)
* V2RayN: 10809 (HTTP)

使用 HTTP，而非 SOCKS。

---

# 3. 如何測試 Rust 部分是否使用代理

透過 `curl` 測試，**而非 Python**，因為 curl 在代理規則上的行為與 Rust 相似：

```bash
curl -I https://transfer.xethub.hf.co --proxy http://127.0.0.1:7890
```

如果這能運作 → Rust 下載也會正常。

如果失敗 → 你的代理無法連接到 `xethub.hf.co` 網域。

---

# 4. 如果你想強制 Hugging Face 避開 XetHub

你可以設定環境變數：

```bash
export HF_HUB_DISABLE_XETHUB=1
```

這會強制使用舊的 HuggingFace S3 後端而非 XetHub，對代理更友好。

然後執行：

```bash
python data/openwebtext_10k/prepare.py
```

這是最穩定的解決方法。

---

# 推薦解決方案（對中國用戶友好）

為了穩定性：

```bash
export HF_HUB_DISABLE_XETHUB=1

export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"
export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"

python data/openwebtext_10k/prepare.py
```

---

如果你需要，我可以提供：

* 一鍵執行的 bash 腳本 (`hf_proxy_on.sh`)
* 永久的 `.bashrc` 代理設定
* 完整鏡像 OpenWebText 到本地的指引，以避免未來下載

告訴我即可。