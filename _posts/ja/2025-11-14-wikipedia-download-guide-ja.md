---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 英語版ウィキペディアダウンロードガイド
translated: true
type: note
---

これは公式Wikimediaダウンロードミラーの1つ（通常は https://dumps.wikimedia.org/enwiki/latest/）からのディレクトリ一覧です。  
2025年11月初旬時点の現在の英語版Wikipedia記事をダウンロードできるすべての異なる方法が含まれています。

### 主なフォーマットと実際の内容

| ファイル名パターン | 内容 | おおよそのサイズ（非圧縮） | LLMトレーニングに最適？ | 備考 |
| --- | --- | --- | --- | --- |
| `enwiki-latest-pages-articles.xml.bz2` | **すべての**記事＋トークページ、テンプレート、リダイレクトなどを含む単一の巨大ファイル | ~85–90 GB 非圧縮 | はい、非常に一般的に使用されます | ストレージと帯域幅に余裕がある場合に最も簡単 |
| `enwiki-latest-pages-articles1.xml-p1p41242.bz2`  … 最大 … `enwiki-latest-pages-articles27.xml-…` | 同じデータを27の小さなチャンクに分割したもの（マルチストリーム） | 各々 ~200–600 MB 圧縮 → 合計で依然として ~85–90 GB 非圧縮 | はい、最も人気のある選択肢 | 並列ダウンロードと簡単な再開が可能 |
| `enwiki-latest-pages-articles-multistreamX.xml.bz2` (例: multistream27) | 上記の分割バージョンに属する実際の巨大な圧縮データファイル | 各々 300–600 MB 圧縮 | これらが求める実際のデータファイルです | これら + インデックスファイルが必要 |
| `enwiki-latest-pages-articles-multistreamX.xml.bz2.md5` / `.meta` | チェックサムと小さなメタデータファイル | < 1 KB | テキスト抽出には不要 | ダウンロード検証専用 |
| `enwiki-latest-pages-articles-multistream-indexX.xml.bz2` | どの記事が大きなマルチストリームファイルのどのバイトオフセットにあるかを示すインデックスファイル | 各々 ~30–60 MB 圧縮 | マルチストリームを使用する場合に必須 | 高速なランダムアクセスに必要。ほとんどの処理スクリプトがこれを要求 |

### 推奨：2025年にモデルをトレーニングする際にほぼ誰もが使用する方法

事実上の標準的な方法（LLaMA、Mistral、Qwen、DeepSeek、Gemma、Phiなどで使用）は以下の通りです：

**27個のマルチストリームファイル + 対応する27個のインデックスファイル**をダウンロードする  
（つまり、`enwiki-latest-pages-articlesXX.xml-p…p….bz2` で始まり、対応する `…-indexXX…bz2` と一致するすべてのファイル）

またはさらに簡単に：接続とディスクに余裕がある場合は、**単一の巨大ファイル**をダウンロードするだけ：

```
enwiki-latest-pages-articles.xml.bz2    ← 24.6 GB 圧縮、~85–90 GB 非圧縮
```

どちらもまったく同じ生のXMLデータ（すべてのメインネームスペース記事 + 多くの追加ページ）を含みます。

### 小さなファイル（multistream3.xml-p…, multistream4.xml-p… など）が推奨されない理由は？
これらは2010年から2015年頃の非常に古い分割版で、Wikipediaのごく一部（当時そのページID範囲にたまたま該当した記事）のみを含んでいます。これらは歴史的な理由で保持されているだけで、今日では基本的に役に立ちません。

### クイックスタートコマンド（2025年ダンプ）

推奨される27+27ファイルの並列ダウンロード（最速）：

```bash
# ファイルリストを取得
wget -q https://dumps.wikimedia.org/enwiki/latest/ -O - | \
  grep -E 'enwiki-latest-pages-articles[0-9]+[02468]\.xml-p[0-9]+p[0-9]+\.bz2"' | \
  sed -e 's/.*href="//' -e 's/".*//' | \
  xargs -n1 -P10 wget https://dumps.wikimedia.org/enwiki/latest/

# 対応するインデックスファイルもダウンロード
wget -q https://dumps.wikimedia.org/enwiki/latest/ -O - | \
  grep -E 'enwiki-latest-pages-articles-multistream-index' | \
  sed -e 's/.*href="//' -e 's/".*//' | \
  xargs -n1 -P10 wget https://dumps.wikimedia.org/enwiki/latest/
```

または単一ファイルのみ（最も簡単）：

```bash
wget https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2
```

その後、通常は以下のようなツールで処理します：
- wikiextractor (Python) → クリーンなテキストへ
- Hugging Face `datasets` Wikipediaローダー（すべてを自動で処理）
- DeepSeekやEleutherAIの処理スクリプトなど

つまり要約すると：  
単一の24GBファイル `enwiki-latest-pages-articles.xml.bz2` または27の分割ファイル + インデックスのいずれかをダウンロードします。リスト内の他のすべては、チェックサム、古い不要なデータ、またはトレーニングに不要なメタデータです。