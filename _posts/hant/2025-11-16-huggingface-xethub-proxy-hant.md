---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 配置 Hugging Face XetHub 代理
translated: true
type: note
---

是的 — **Rust reqwest 絕對支援明確的代理伺服器設定**，而 Hugging Face 的 XetHub 客戶端（使用 Rust 編寫）也允許這樣做。
但是：Hugging Face 並**未提供**Python API 讓您直接傳遞代理設定。
相反地，XetHub 依賴於 reqwest 自動讀取的**環境變數**。

因此，reqwest 的明確代理設定如下所示：

---

# ✔ reqwest 如何偵測代理伺服器（官方說明）

Reqwest 會自動使用以下**環境變數**：

* `https_proxy`
* `http_proxy`
* `all_proxy**

**小寫**是關鍵部分。
除非在編譯時啟用了特定功能標誌，否則 reqwest **會忽略**大寫變數（`HTTPS_PROXY`）。

**Hugging Face XetHub 使用預設的 reqwest → 僅支援小寫。**

這表示：

```
export https_proxy="http://127.0.0.1:7890"
export http_proxy="http://127.0.0.1:7890"
```

是唯一保證對 XetHub 有效的明確代理設定。

---

# ✔ HuggingFace XetHub 如何載入代理設定

當 Python 執行 `load_dataset` 時，會觸發一個 Rust 二進位檔案，該檔案：

1. 尋找小寫的代理環境變數
2. 重寫 URL
3. 透過 reqwest 開啟連線
4. 從 `https://transfer.xethub.hf.co` 下載檔案區塊

如果這些環境變數未設定或無法連線 → 連線被拒絕。

---

# ✔ 手動強制 reqwest 使用代理（參考程式碼）

僅展示 reqwest 在內部會執行的操作：

```rust
let proxy = reqwest::Proxy::https("http://127.0.0.1:7890")?;
let client = reqwest::Client::builder()
    .proxy(proxy)
    .build()?;
```

Hugging Face 的 XetHub 客戶端*執行了等效操作*，但由環境變數觸發。

---

# ✔ 總是與 reqwest 相容的完整明確代理設定（HF 相容）

執行**所有**以下指令：

```bash
export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"
export all_proxy="http://127.0.0.1:7890"
```

使用 `http` 代理，而非 `socks5`，因為：

* reqwest 的 socks 支援是可選的
* XetHub 客戶端二進位檔案在 HF 中未編譯此功能

因此 socks 可能會無聲無息地失敗。

---

# ✔ 驗證您的代理是否正在被使用

嘗試：

```bash
env | grep proxy
```

如果您看到小寫 → 良好。

然後：

```bash
curl -I https://transfer.xethub.hf.co --proxy http://127.0.0.1:7890
```

如果 curl 成功 → reqwest 將會成功。

---

# 總結

* Hugging Face 資料集有時透過 **XetHub**（Rust reqwest 客戶端）下載
* Reqwest 預設僅遵循**小寫**代理變數
* 您必須明確設定它們
* 使用 **HTTP** 代理，而非 SOCKS
* 如果需要，`HF_HUB_DISABLE_XETHUB=1` 可以完全繞過 reqwest

---

如果您需要，我可以準備：

* 一鍵式「HF 代理修復」指令碼
* 用於您的 `.bashrc` 的永久設定
* 自動偵測以確認 reqwest 是否正在使用代理

請告訴我。