---
audio: false
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: オープンウェブテキストの一部をダウンロード
translated: true
type: note
---

ああ、なるほど — **Hugging Face CLI** を使いたいが、それでも少量だけ取得したいのですね。問題は、CLI が**ファイル全体**をダウンロードするように設計されており、一部を切り取る機能はないことです。OpenWebText は 21 個の `.tar` サブセットファイルに分割されています；CLI を使用すると、ターボール全体をダウンロードするため、大きな塊をダウンロードせずに正確に「1%」を得ることはできません。

以下に実用的なアプローチを示します：

---

### 1. ファイルの一部のみをダウンロード

21 ファイル全てではなく、数個のターボールだけを選択します：

```bash
huggingface-cli download \
  --repo-type dataset openwebtext/subsets/urlsf_subset00.tar \
  --local-dir ./openwebtext
huggingface-cli download \
  --repo-type dataset openwebtext/subsets/urlsf_subset01.tar \
  --local-dir ./openwebtext
```

* 各ターボールは約 625MB です。そのため、1–2 個ダウンロードすれば、データセットの約 1–2% に相当します。
* どのサブセットを選択するかは調整可能です；HF は連番順序を強制しません。

---

### 2. 必要な部分のみを抽出

ダウンロード後：

```bash
cd ./openwebtext
tar -xvf urlsf_subset00.tar
tar -xvf urlsf_subset01.tar
```

その後、これらのサブセットから文書を数個だけ処理できます。

---

### 3. オプション：HF Transfer との組み合わせ

CLI ダウンロードを高速化するには：

```bash
pip install hf_transfer
export HF_HUB_ENABLE_HF_TRANSFER=1
```

その後、CLI コマンドを再試行してください — ダウンロードが大幅に高速化されます。

---

もし希望であれば、**CLI のみを使用して OpenWebText の約 1% を自動選択する小さなコマンドスニペット**を作成できます。手動でターボールを選択する必要がなくなります。作成しましょうか？