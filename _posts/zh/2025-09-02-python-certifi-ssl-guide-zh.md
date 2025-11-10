---
audio: false
generated: true
image: false
lang: zh
layout: post
title: Python Certifi SSL证书指南
translated: true
type: note
---

PyPI 上的 **`certifi`** 包是一个提供 **Mozilla 受信任根证书** 捆绑库的小型工具库。它常被 `requests`、`urllib3` 等需要验证 SSL/TLS 证书的 Python HTTPS 客户端库使用。

使用方法如下：

---

### 1. 安装 `certifi`

```bash
pip install certifi
```

---

### 2. 获取 CA 证书捆绑包路径

在 Python 中执行：

```python
import certifi

print(certifi.where())
```

这将输出 CA 证书捆绑包（`.pem` 文件）的完整路径，例如：

```
/usr/local/lib/python3.11/site-packages/certifi/cacert.pem
```

---

### 3. 在 `requests` 或 `urllib3` 中使用

```python
import requests
import certifi

response = requests.get("https://example.com", verify=certifi.where())
print(response.status_code)
```

默认情况下 `requests` 已内置使用 `certifi`，但显式传递 `verify=certifi.where()` 可确保使用最新的证书捆绑包。

---

### 4. 在其他 HTTPS 库中使用

若直接使用 `urllib3`：

```python
import urllib3
import certifi

http = urllib3.PoolManager(
    cert_reqs="CERT_REQUIRED",
    ca_certs=certifi.where()
)

response = http.request("GET", "https://example.com")
print(response.status)
```

---

### 5. 系统级使用（可选）

有时可能需要让应用程序指向 certifi 的 CA 证书捆绑包：

```bash
export SSL_CERT_FILE=$(python -m certifi)
```

---

👉 核心要点：

* 通过 `pip install certifi` 安装
* 使用 `certifi.where()` 获取证书捆绑包路径
* 将其传递给需要证书验证的库

---

需要我继续演示 **如何让整个 Python 环境默认使用 certifi 的证书**，从而无需单独配置每个库吗？