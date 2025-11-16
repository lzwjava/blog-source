---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: OpenWebTextとWikipediaデータセットトレント
translated: true
type: note
---

### OpenWebText データセットのトレント

OpenWebTextは、OpenAIのWebTextデータセットをオープンソースで再現したもので、高カルマRedditリンク（主に品質のためにスクレイピングおよびフィルタリングされたウェブページ）から抽出された〜38GBのクリーンなテキストで構成されています。言語モデルのトレーニング用の大規模テキストコーパスとして人気があります。完全なスクレイピング済みテキストが単一のトレントとして常に直接利用できるわけではありませんが、以下に信頼性の高いオプションを示します：

- **URLリスト（フィルタリング済み、〜480MB）**： OpenWebTextのスクレイピングに使用された約2600万のURLの事前フィルタリング済みリスト。これを使用してテキストを自分でダウンロードおよび処理できます。
  - トレント: [OpenWebText-urls-26M-filtered.xz](https://academictorrents.com/details/f5161721b322bca66ed74da32b963c1066e64312)
  - ソース: Academic Torrents (コミュニティによってシードされています)。

- **URLリスト（完全版、〜1.75GB）**： Redditの投稿から収集された、重複排除済みの完全なURLリスト。
  - トレント: [WebText dataset urls.txt.tar.gz](https://academictorrents.com/details/15f3494b2991e75194d3af72bf7afa5025a7abc3)
  - ソース: Academic Torrents (コミュニティによってシードされています)。

- **トークン化バージョン（〜16GB）**： スクレイピングされたコーパスからのGPT-2トークン化済みテキストファイル（395ファイル、モデルトレーニング準備済み）。
  - トレント: [OpenWebText (Gokaslan's distribution, 2019), GPT-2 Tokenized](https://academictorrents.com/details/36c39b25657ce1639ccec0a91cf242b42e1f01db)
  - ソース: Academic Torrents (OSUOSLおよびコミュニティによってシードされています)。

完全な生のテキストコーパスについては、公式サイトで直接ダウンロード（トレントベースではない）を確認するか、上記のURLを[OpenWebText GitHubリポジトリ](https://github.com/eukaryote31/openwebtext)のスクレイピングスクリプトと共に使用してください。拡張版であるOpenWebText2（〜マルチTB規模）は、[EleutherAIのリポジトリ](https://github.com/EleutherAI/openwebtext2)から利用可能ですが、トレントではなくストリーミングを使用します。

### Wikipedia ダンプのトレント

Wikipediaダンプは、データベース全体（記事、リビジョン、メタデータ）の月次XMLエクスポートです。英語版は非常に大規模です（要約のみで圧縮済み〜20-25GB、完全な履歴では100+GB）。トレントはコミュニティによって維持され（非公式ですが公式のチェックサムに対して検証済み）、信頼性のためにWikimediaサーバーからウェブシードされています。ダウンロードしたファイルは常に[dumps.wikimedia.org](https://dumps.wikimedia.org/enwiki/latest/)のハッシュ値に対して検証してください。

トレントの主要なハブは[Meta-Wiki Data Dump Torrentsページ](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki)で、最新の英語Wikipediaダンプ（例：enwiki-20251101）がリストされています。最近のものの概要を以下に示します：

| ダンプ日付 | ファイルタイプ | 圧縮サイズ | トレントリンク | 備考 |
|-----------|-----------|-----------------|--------------|-------|
| 2025-11-01 | ページ-記事 (XML, 要約のみ) | ~22GB | [enwiki-20251101-pages-articles-multistream.xml.bz2](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki) | マルチストリーム形式；テキスト抽出が最も容易。 |
| 2025-11-01 | ページ-記事-履歴 (XML, 全リビジョン) | ~120GB | [enwiki-20251101-pages-meta-history*.xml.bz2](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki) | 全ての編集を含む；扱いやすいようにストリームに分割。 |
| 2025-10-01 | ページ-記事 (XML, 要約のみ) | ~21GB | [enwiki-20251001-pages-articles-multistream.xml.bz2](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki) | 前月分；履歴の比較に適しています。 |

- **完全コレクション**: 全ての過去の英語Wikipediaトレントは[Academic Torrents Wikipedia Collection](https://academictorrents.com/collection/wikipedia)で閲覧できます（〜2010年頃までの古いダンプを含む）。
- **Kiwix ZIM形式**: 閲覧可能なオフライン版Wikipedia（HTML、〜100GB）が必要な場合は、[wikipedia_en_all_maxi_2024-01.zim.torrent](https://download.kiwix.org/zim/wikipedia/wikipedia_en_all_maxi_2024-01.zim.torrent)を試してください – コミュニティシードされていますが、2025年の更新については[Kiwix downloads](https://download.kiwix.org/zim/wikipedia/)で確認してください。

これらをプレーンテキストに処理するには、Pythonの`wikiextractor`のようなツールを使用します。トレントはサーバー負荷を軽減し、中断されたダウンロードを再開できます – qBittorrentなどのクライアントを使用してください。他の言語またはサブセットのダンプが必要な場合は、Meta-Wikiページでフィルターをかけられます。