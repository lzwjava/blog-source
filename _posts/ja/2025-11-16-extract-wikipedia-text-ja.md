---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: ウィキペディアダンプからのテキスト抽出
translated: true
type: note
---

以下は、Wikipediaの`.bz2`ダンプファイル（例: `enwiki-latest-pages-articles1.xml-p1p41242.bz2`）からプレーンテキストを抽出する最も一般的で効果的な方法です。

### 推奨ツールと方法（簡単なものから効率的なものへ）

#### 1. wikiextractorの使用（ほとんどの人に最適 – 高速でクリーン）
これはNLP/ML分野でWikipediaダンプを扱う際にほぼ全員が使用する標準ツールです。

```bash
# インストール（一度だけ実行）
pip install wikiextractor

# テキスト抽出（テンプレート、テーブルなどを除去し、記事ごとにクリーンなテキストを提供）
wikiextractor enwiki-latest-pages-articles1.xml-p1p41242.bz2 --output wiki_text
```

- 出力: `wiki_text/`フォルダを作成し、AA、ABなどのサブフォルダにクリーンなJSON/テキストの`.bz2`ファイルを格納
- プレーンテキスト（1行に1記事）を取得する場合:
```bash
wikiextractor enwiki-latest-pages-articles1.xml-p1p41242.bz2 --processes 8 -o wiki_text --json
# 必要に応じてJSONをプレーンテキストに変換
find wiki_text -name '*' -exec cat {} \; | grep '"text":' | sed 's/.*"text": "//;s/"$//' > all_text.txt
```

#### 2. gensimのWikiCorpusを使用（PythonでNLPを行う場合に最適）

```python
from gensim.corpora import WikiCorpus

# これは自動的に.bz2を処理し、テキストを抽出＋トークン化
wiki = WikiCorpus("enwiki-latest-pages-articles1.xml-p1p41242.bz2", dictionary=False)

# 記事をイテレート処理
with open("output.txt", "w", encoding="utf-8") as f:
    for i, text in enumerate(wiki.get_texts()):
        f.write(" ".join(text) + "\n")
        if i % 10000 == 0:
            print(f"Processed {i} articles")
```

#### 3. シンプルなbzip2 + grep/awk（簡易＆ラフ、クリーニングなし）

```bash
# 単純に解凍して生のXMLを確認
bzip2 -dc enwiki-latest-pages-articles1.xml-p1p41242.bz2 | less

# <text>コンテンツのみ抽出（非常にラフ、wikiマークアップを保持）
bzip2 -dc enwiki-latest-pages-articles1.xml-p1p41242.bz2 | \
  sed -n '/<text /,/<\/text>/p' | \
  sed 's/<text[^>]*>//g;s/<\/text>//g' > raw_text_with_markup.txt
```

#### 4. 完全なダンプがあり高速にすべて処理したい場合（並列処理）
あなたのファイルは最初のチャンク（p1p41242）のみですが、後で全30+チャンクを所有する場合:

```bash
# すべてを並列で抽出
ls *.bz2 | xargs -P 8 -I {} wikiextractor {} --output wiki_extracted
```

### まとめ – 現時点でのあなたへの推奨方法:

```bash
pip install wikiextractor
wikiextractor enwiki-latest-pages-articles1.xml-p1p41242.bz2 -o extracted_wiki --bytes 1M --json
```

これにより、数分でクリーンで読みやすい記事が得られます（あなたのファイルは圧縮で約2-3GBのみなので、非常に扱いやすいサイズです）。

以下のいずれかを希望する場合はお知らせください:
- メインネームスペースのみ（トークページではなく実際の記事）
- JSONではなくプレーンテキスト
- トークン化された出力
- 中国語Wikipedia（zhwiki）への変更 – プロセスは同一

楽しい抽出を！ 🚀