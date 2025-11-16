---
audio: false
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: Hugging Face XetHubプロキシ問題の修正
translated: true
type: note
---

あなたのログには非常に重要な情報が示されています：

**失敗している接続はHuggingFaceに直接向かっているのではありません。**
それは **[https://transfer.xethub.hf.co](https://transfer.xethub.hf.co)** に向かっています — これはHugging Faceの*XetHub*バックエンド（Rustクライアント `reqwest`）であり、あなたが設定したプロキシはこれを自動的に**傍受しません**。

これですべてが説明できます：

* あなたはすでにPython用に `HTTP_PROXY` を設定済み → 問題なし
* しかし、XetHubは**Python requestsではなく、rust reqwest**を使用しています
* Rust reqwestは、**HTTPS_PROXYのような小文字のプロキシ変数を設定しない限り、または明示的なプロキシ設定を使用しない限り、システムのプロキシ変数を無視します**

つまり：**あなたのPython環境はプロキシを使用していますが、XetHub（新しいHFストレージプロバイダー）は使用していません**。

これが以下の表示される理由です：

```
ConnectError("Connection refused")
```

そしてリトライ。

---

# これが起こる理由（短いバージョン）

Hugging Faceは最近、ストレージを**XetHub**に移行しました。これはRustクライアントを使用します。
このクライアントは以下に従います：

* `https_proxy`
* `http_proxy`

しかし、**ビルドに依存して大文字バージョンには常には従いません**。

あなたが大文字を設定した？ → それらを無視するかもしれません。

---

# 修正（中国で確実に動作します）

## 1. 小文字と大文字の両方のプロキシ変数を設定する

**NanoGPTを実行する前**にシェルで：

```bash
export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"

export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"
```

Rust reqwestは小文字を優先
Python requestsは大文字を優先
両方を設定することで問題を回避。

その後、実行：

```bash
python data/openwebtext_10k/prepare.py
```

すぐに適切なダウンロード速度が表示されるはずです。

---

# 2. あなたのプロキシがSOCKS5の場合、重要

Rust reqwestは、オプション機能でコンパイルされていない限り、**socks5をサポートしません**。
したがって、あなたのプロキシが socks5:// の場合 → 失敗します。

あなたのクライアントのHTTPプロキシポートに切り替える必要があります。通常は：

* Clash: 7890 (HTTP)
* V2RayN: 10809 (HTTP)

SOCKSではなく、HTTPを使用してください。

---

# 3. Rust部分がプロキシを使用しているかテストする方法

Pythonではなく `curl` でテストします。なぜならcurlはプロキシルールでRustと同様に動作するからです：

```bash
curl -I https://transfer.xethub.hf.co --proxy http://127.0.0.1:7890
```

これが動作する場合 → Rustダウンロードも動作します。

失敗する場合 → あなたのプロキシは `xethub.hf.co` ドメインに到達できません。

---

# 4. Hugging FaceにXetHubを使用しないように強制したい場合

環境変数を設定できます：

```bash
export HF_HUB_DISABLE_XETHUB=1
```

これにより、XetHubの代わりに古いHuggingFace S3バックエンドが強制され、プロキシとの親和性がはるかに高くなります。

その後：

```bash
python data/openwebtext_10k/prepare.py
```

これが最も安定した修正です。

---

# 推奨される解決策（中国に優しい）

信頼性のために：

```bash
export HF_HUB_DISABLE_XETHUB=1

export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"
export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"

python data/openwebtext_10k/prepare.py
```

---

必要であれば、以下を提供できます：

* ワンクリックbashスクリプト (`hf_proxy_on.sh`)
* 恒久的な `.bashrc` プロキシ設定
* 将来のダウンロードを避けるためにOpenWebTextを完全にローカルにミラーリングする手順

お知らせください。