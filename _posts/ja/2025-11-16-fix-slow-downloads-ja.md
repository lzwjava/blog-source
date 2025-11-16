---
audio: false
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: Hugging Faceのダウンロード高速化
translated: true
type: note
---

これは、巨大なHFデータセットをプロキシ経由でダウンロードする際によく発生する問題です。以下の組み合わせによって引き起こされます：

* 数百MBのファイルが多数ある場合
* Pythonの`requests` / `huggingface_hub`を使用している場合
* ローカルHTTPプロキシ（特にClash、V2Ray、tun2socks）を使用している場合

これらが原因で、極端に低速なスループットや接続リセットが発生することがよくあります。

以下に、最も効果的な修正方法を示します。

---

## 1. **最適な修正: `hf_transfer`を使用する**

Hugging Faceには高速なダウンローダーがあり、**10倍から50倍高速**で、より安定しています。

インストール方法：

```bash
pip install hf_transfer
export HF_HUB_ENABLE_HF_TRANSFER=1
```

再度コマンドを実行してください。

これだけで、プロキシ経由の低速なダウンロードが通常修正されます。

---

## 2. Hugging Face CLIで`aria2c`を使用する（巨大ファイルに最速）

手動でダウンロードする場合：

```bash
pip install huggingface_hub[cli]
sudo apt install aria2
```

その後ダウンロード：

```bash
huggingface-cli download --repo-type dataset openwebtext --local-dir ./openwebtext --local-dir-use-symlinks False
```

HF CLIは自動的にaria2を使用します。aria2は以下を処理します：

* 並列接続
* レジューム機能
* 不安定なプロキシ

`requests`よりもはるかに優れています。

---

## 3. ローカルプロキシの低速対策：HTTPの代わりにシステム全体のSOCKSを使用する

以下のような設定を使用している場合：

```
HTTP_PROXY=http://127.0.0.1:7890
HTTPS_PROXY=http://127.0.0.1:7890
```

プロキシが対応していればSOCKS5に切り替えてください：

```bash
export ALL_PROXY=socks5://127.0.0.1:7891
```

SOCKSは大容量ファイルのストリーミングにおいて**はるかに安定しています**。

---

## 4. 大容量ファイルのプロキシを無効化する

生のネットワーク接続が良好で、プロキシのみが低速化の原因である場合：

```bash
unset HTTP_PROXY
unset HTTPS_PROXY
unset ALL_PROXY
```

その後再試行してください。地域によっては、プロキシなしでも一部のHFサーバーは高速です。

---

## 5. HFミラーを使用する（中国本土/台湾では時々低速）

CDNを強制できます：

```bash
export HF_ENDPOINT=https://hf-mirror.com
```

その後再度実行してください。
これにより、一部の地域では速度が劇的に改善されます。

---

## 6. 中断されたダウンロードを再開する

HFデータセットは以下にキャッシュされます：

```
~/.cache/huggingface/datasets/
```

ファイルが部分的にダウンロードされていた場合、HFは自動的に再開します — ゼロから開始する必要はありません。

---

## 7. それでも低速な場合：完全なデータセットを避け、一部のみを使用する

OpenWebTextは40GB以上あります。
一部のみを読み込むことができます：

```python
from datasets import load_dataset
ds = load_dataset("openwebtext", split="train[:1%]")
```

---

## クイック推奨事項

最速かつ最も簡単な方法：

```bash
pip install hf_transfer
export HF_HUB_ENABLE_HF_TRANSFER=1
python data/openwebtext_10k/prepare.py
```

ダウンロード速度がすぐに向上するはずです。

---

必要であれば、`prepare.py`を修正して、リトライ/バックオフと並列取得を備えた完全なカスタムダウンローダーを使用する方法をお見せできます。これにより、パイプラインが常に高速でダウンロードし、停止することはなくなります。