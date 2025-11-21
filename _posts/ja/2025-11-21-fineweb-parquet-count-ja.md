---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4.1-fast
title: FineWebデータセットのParquetファイル数
translated: true
type: note
---

**FineWeb**データセット（HuggingFaceFW/finewebにある15T+トークンの英語版）には、合計で**約35,000から50,000**の`.parquet`ファイルが含まれています。

### 内訳
- **96**の個別のCommon Crawlスナップショット（ダンプ、例: `CC-MAIN-2013-20`, `CC-MAIN-2024-10`など）で構成されています。
- 各ダンプは`/data/`の下の独自のサブディレクトリに保存され、`000_00000.parquet`, `000_00001.parquet`, …（ゼロ埋め、連番）のように命名された多くのシャード化された`.parquet`ファイルに分割されています。
- parquetファイルの数は、ダンプのサイズによって異なります：
  - 小規模/古いダンプ（あなたのスクリプトにある`CC-MAIN-2013-20`の例）は、しばしば**~200–1,000**ファイルを持ちます。
  - 大規模な最近のダンプは、それぞれ**数千**のファイルを持つことがあります。
- 単一の公式に公開された総数はありませんが、コミュニティの推定およびダンプサイズ/トークン数からの計算は、一貫して**全体の総数が約35k–50k**のparquetファイル（96のダンプ全体で、完全なデータセットは非圧縮で~45–53 TB）であると示しています。

あなたのスクリプトは、非常に小さい`CC-MAIN-2013-20`ダンプからシャード11から20（10ファイル）をダウンロードしますが、このダンプだけでもそれよりはるかに多く — 合計で数百のシャード — を持っています。

正確な数を確認したい場合は、Hugging Face Hub API（例: `huggingface_hub.list_repo_files`の使用）を使ってプログラムで計算できますが、上記のおおよその数値が、完全なデータセットをダウンロードまたは処理する際に一般的に使用されるものです。

[FineWeb dataset card](https://huggingface.co/datasets/HuggingFaceFW/fineweb)  
[FineWeb data tree (example dump)](https://huggingface.co/datasets/HuggingFaceFW/fineweb/tree/main/data)