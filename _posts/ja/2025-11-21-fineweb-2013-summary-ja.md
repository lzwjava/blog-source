---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4.1-fast
title: FineWeb 2013データセット概要
translated: true
type: note
---

**CC-MAIN-2013-20** (2013年夏のダンプ) をFineWebデータセットで見ると:

- **.parquetファイル数**: 約**460–500**  
  (ファイルは様々なサイズにシャーディングされています: 多くのファイルが~1 GB、一部は~2 GBまで大きくなります。ディレクトリ合計は**422 GB**なので、422 ÷ ~0.9 GB（平均）≈ 460–480 シャードとなります。ファイル名は連番で `000_00000.parquet` からおよそ `000_004xx.parquet` までです。)

- **全parquetファイルの合計サイズ**: **422 GB**

- **GPTスタイルのトークナイザーでエンコードした場合のトークン数** (GPT-4に使用されるcl100k_base、またはFineWebのレポートで使用された古いGPT-2トークナイザー):  
  **1445億トークン** (FineWebのクリーニング、フィルタリング、重複排除パイプライン適用後)

注: 元の生のCommon Crawlダンプははるかに大規模でした (~3930億トークン、フィルタリング前) が、FineWebは高品質な英語テキストのみを保持するため、この古い2013年のダンプはこれほど劇的に縮小しています。

ディレクトリ全体をダウンロードする場合 (例: `huggingface-cli download` を使用するか、全シャードをループ処理するスクリプトで)、トレーニング準備が整った144.5Bトークンを含む~422 GBのparquetファイルを入手することになります。

[FineWebデータセットカード (ダンプごとのトークンテーブルを含む)](https://huggingface.co/datasets/HuggingFaceFW/fineweb)  
[HF上のCC-MAIN-2013-20ディレクトリ (合計サイズを表示)](https://huggingface.co/datasets/HuggingFaceFW/fineweb/tree/main/data/CC-MAIN-2013-20)