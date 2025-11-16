---
audio: false
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: Hugging Face XetHubプロキシの設定
translated: true
type: note
---

はい — **Rust reqwestは明示的なプロキシ設定を完全にサポートしており**、Hugging FaceのXetHubクライアント（Rustで書かれている）も同様です。
ただし：Hugging Faceはプロキシ設定を直接渡すための**Python APIを公開していません**。
代わりに、XetHubはreqwestが自動的に読み取る**環境変数**に依存しています。

したがって、reqwestの明示的なプロキシ設定は以下のようになります：

---

# ✔ reqwestがプロキシを検出する方法（公式）

Reqwestは自動的に以下の**環境変数**を使用します：

* `https_proxy`
* `http_proxy`
* `all_proxy`

**小文字**が重要です。
Reqwestは、特定の機能フラグがコンパイル時に有効になっていない限り、大文字の変数（`HTTPS_PROXY`）を**無視します**。

**Hugging Face XetHubはデフォルトのreqwestを使用 → 小文字のみ対応**

つまり：

```
export https_proxy="http://127.0.0.1:7890"
export http_proxy="http://127.0.0.1:7890"
```

これがXetHubで確実に動作する唯一の明示的なプロキシ設定です。

---

# ✔ HuggingFace XetHubがプロキシ設定を読み込む方法

Pythonが `load_dataset` を実行すると、Rustバイナリが起動し、以下を行います：

1. 小文字のプロキシ環境変数を探す
2. URLを書き換える
3. reqwestを通じて接続を開く
4. `https://transfer.xethub.hf.co` からファイルチャンクをダウンロードする

これらの環境変数が設定されていない、または到達不能な場合 → 接続拒否されます。

---

# ✔ reqwestにプロキシを使用するよう手動で強制する（参考コード）

reqwestが内部的に何を行うかを示すためだけのコード：

```rust
let proxy = reqwest::Proxy::https("http://127.0.0.1:7890")?;
let client = reqwest::Client::builder()
    .proxy(proxy)
    .build()?;
```

Hugging FaceのXetHubクライアントは*同等の処理を行います*が、環境変数によってトリガーされます。

---

# ✔ reqwestで常に動作する完全な明示的プロキシ設定（HF互換）

**すべて**を実行してください：

```bash
export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"
export all_proxy="http://127.0.0.1:7890"
```

`socks5` ではなく `http` プロキシを使用してください。理由は：

* reqwestのsocksサポートはオプション機能です
* XetHubクライアントバイナリはHF用にそれでコンパイルされていません

そのため、socksは暗黙的に失敗する可能性があります。

---

# ✔ プロキシが使用されているか確認する

試してください：

```bash
env | grep proxy
```

小文字が表示されれば → 良好です。

次に：

```bash
curl -I https://transfer.xethub.hf.co --proxy http://127.0.0.1:7890
```

curlが成功すれば → reqwestも成功します。

---

# まとめ

* Hugging Face datasetsは**XetHub**（Rust reqwestクライアント）経由でダウンロードされることがあります
* Reqwestはデフォルトで**小文字**のプロキシ変数のみを認識します
* これらを明示的に設定する必要があります
* SOCKSではなく **HTTP** プロキシを使用してください
* 必要に応じて `HF_HUB_DISABLE_XETHUB=1` でreqwestを完全にバイパスできます

---

もし希望があれば、以下を準備できます：

* ワンコマンドの「HFプロキシ修正」スクリプト
* `.bashrc` 用の永続的な設定
* reqwestがプロキシを使用しているか確認する自動検出機能

お知らせください。