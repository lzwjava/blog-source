---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Hugging Faceのダウンロード速度を最適化
translated: true
type: note
---

現在のダウンロードは Hugging Face のメインエンドポイント (`huggingface.co`) を使用しており、これは主に欧州/米国のデータセンターでホストされています。広州から台湾プロキシを経由することで、以前と同様のレイテンシ問題（往復で約200〜300ms）が発生し、さらに大容量ファイル（このParquetファイルはシャードあたり約500MB〜1GB）ではスロットリングの可能性もあります。表示されている302リダイレクトは、おそらくCloudFront CDNエッジへのものですが、アジアに最適化されていないため、速度低下（例: 1〜5 MB/s）を引き起こしている可能性があります。

Wikimedia ダウンロードでの 20〜60 MB/s の速度を実現するには、以下の調整を行ってください。これらはアジアに適したオプションを優先し、かつ Clash/台湾プロキシ設定を維持します。

### 1. **HF ミラーの使用 (中国/台湾向け最速 - 推奨)**
   HF ミラー (`hf-mirror.com`) は、東アジア向けに最適化されたコミュニティ運営のCDNです（清華大学などの国内ネットワーク経由）。HFのデータセット（FineWeb Parquetファイルを含む）を正確にミラーリングしています。台湾プロキシからは、30〜80 MB/s が期待できます。

   スクリプトを更新:
   ```bash
   #!/bin/bash
   # wget_fineweb_1.sh (速度向上版)
   mkdir -p fineweb_test_dump
   cd fineweb_test_dump
   echo "Downloading FineWeb shard via HF Mirror (faster for Asia)..."

   # huggingface.co を hf-mirror.com に置き換え
   wget -c "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00000.parquet?download=true"

   echo "Done! Shard size: ~500MB–1GB"
   echo "For more shards, loop over e.g., 000_00001.parquet, etc."
   echo "To load in Python: from datasets import load_dataset; ds = load_dataset('HuggingFaceFW/fineweb', name='CC-MAIN-2013-20', split='train', streaming=True)"
   ```

   実行: `./scripts/train/wget_fineweb_1.sh`
   - 万が一ミラーが遅い場合（稀）、公式にフォールバック: `https://huggingface.co/datasets/...` (ただし、#2の速度向上Tipを追加してください)。

### 2. **hf_transfer による高速化 (あらゆるHFダウンロードに有効 - 再開可能なダウンロードで100倍高速化)**
   Hugging Face 公式の Rust 製ツールで、並列/マルチスレッドダウンロードを実現します。自動リトライ、多数の接続を使用し、良好なリンクでは >500 MB/s を達成します。`wget` と間接的、または `huggingface_hub` 経由で直接連携できます。

   インストール (1回のみ、pip経由 - 環境にインストール済み):
   ```bash
   pip install hf_transfer
   export HF_HUB_ENABLE_HF_TRANSFER=1
   ```

   その後、元のスクリプトを再実行してください。HF URL への基礎的な `wget` 呼び出しを加速します。
   - プロTip: フルデータセットをストリーミングする場合（フルダウンロードしない）、パイプラインで Python を使用:
     ```python
     from datasets import load_dataset
     import os
     os.environ['HF_HUB_ENABLE_HF_TRANSFER'] = '1'  # インポート前に有効化
     ds = load_dataset("HuggingFaceFW/fineweb", name="CC-MAIN-2013-20", split="train", streaming=True)
     for example in ds.take(1000):  # オンザフライでストリーム/処理
         print(example)
     ```
     これは、`HF_ENDPOINT=https://hf-mirror.com` を設定すると、ミラー経由でシャードをレイジーにプルします。

### 3. **Clash ルール微調整 (可能な場合 - 超高速な国内接続)**
   プロキシ設定で HF をバイパス（または香港/シンガポールノードにルーティング）できる場合、`huggingface.co` / `hf-mirror.com` に対するルールを追加して直接/国内接続します。`clash.yaml` 内で:
   ```
   rules:
     - DOMAIN-SUFFIX,hf-mirror.com,DIRECT  # または使用中のCNミラーノード
     - DOMAIN-SUFFIX,huggingface.co,DIRECT
   ```
   Clash を再起動し、ダウンロードを実行。#1 と組み合わせることで、清華大学ミラー経由で 50–100+ MB/s を実現します。

### これが Wikimedia 速度に匹敵する理由
- Wikimedia: リダイレクタが自動的にアジア（日本/KR/SG）を選択 → 低レイテンシ。
- HF: デフォルトは EU/US → 高レイテンシ; ミラー + transfer によりアジア最適化に切り替え。

まず1つのシャードでテストしてください。それでも遅い場合は、`curl -I https://hf-mirror.com/...` でヘッダーを確認してください（アジアのCDNが表示されるはずです）。フル 15T の FineWeb については、100GB単位のダウンロードを避けるため、`datasets` ライブラリ経由でストリーミングしてください。速度が向上しない場合は連絡してください！