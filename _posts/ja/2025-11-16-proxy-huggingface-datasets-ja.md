---
audio: false
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: Hugging Faceデータセットでのプロキシの使用
translated: true
type: note
---

はい — `datasets` はあなたの**システム/環境プロキシ設定**に従いますが、独自のプロキシ設定は**持ちません**。
つまり、中国にいる場合でもプロキシを通じて Hugging Face のデータセットをダウンロードすることは確実に可能です。

以下に方法を説明します。

---

# `load_dataset` にプロキシを使用させる方法（中国対応）

## 1. HTTP/HTTPS プロキシの環境変数を設定する

`datasets` は内部で Python の `requests` ライブラリを使用しています。
`requests` は標準のプロキシ環境変数を自動的に使用します：

### Linux / macOS

```bash
export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"
```

プロキシが SOCKS5 を使用する場合：

```bash
export HTTP_PROXY="socks5://127.0.0.1:1080"
export HTTPS_PROXY="socks5://127.0.0.1:1080"
```

### Windows (PowerShell)

```powershell
setx HTTP_PROXY "http://127.0.0.1:7890"
setx HTTPS_PROXY "http://127.0.0.1:7890"
```

その後、ターミナルを再起動してください。

---

## 2. Python をコード内（Jupyter など）で実行している場合、Python 内部で設定する

```python
import os

os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'
```

この方法は確実に動作します。

---

## 3. プロキシが動作していることを確認する

以下のコードでテストできます：

```python
import requests
print(requests.get("https://api.ipify.org?format=json").text)
```

IP があなたのプロキシの出口ノードの場合、Hugging Face のデータセットダウンロードもそのプロキシを経由します。

---

## 4. Hugging Face の `huggingface_hub` もこれらの変数を尊重する

`datasets` は内部で `huggingface_hub` を使用しており、これも以下に従います：

* `HTTP_PROXY`
* `HTTPS_PROXY`
* `http_proxy`
* `https_proxy`

したがって、環境変数が設定されると、モデルとデータセットの両方のダウンロードが自動的にあなたのプロキシを使用します。

---

# 中国での使用に関する注意点

* Hugging Face の生ダウンロードは、多くの場合、プロキシを必要とします。これは、それらが US/Europe エンドポイントでホストされているためです。
* `.zst` データセットファイルからのタイムアウトが表示される場合、これはプロキシなしでは正常です。
* グローバルプロキシ (Clash, V2Ray, Qv2ray など) を使用すると、すべてがよりスムーズになります。

---

# 必要であれば、以下の方法も説明できます：

* NanoGPT が確実にプロキシを通じてデータセットをダウンロードする方法
* 将来のダウンロードを避けるためにデータセットをローカルにキャッシュする方法
* 中国で Hugging Face データセットをローカルにミラーリングする方法（例：清華大学ミラーの回避策）

必要なものをお知らせください。