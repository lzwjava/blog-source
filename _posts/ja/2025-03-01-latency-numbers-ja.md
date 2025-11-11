---
audio: false
generated: true
lang: ja
layout: post
title: レイテンシーの数値
translated: true
type: note
---

### 主なポイント
- 動画のタイトルと関連するオンラインコンテンツから、プログラマーが知っておくべき標準的なレイテンシー数値について議論している可能性が高い。
- 調査によると、これらの数値にはL1キャッシュアクセス（0.5 ns）やネットワーク往復時間（最大150 ms）などの操作時間が含まれており、ハードウェアによって異なる。
- 証拠から、これらの数値は概算であり、特にSSDとネットワークの技術進歩を反映して更新されている傾向がある。

### はじめに
「Latency Numbers Programmer Should Know: Crash Course System Design #1」という動画は、システム設計において重要なコンピューター操作の基本的なレイテンシー数値をカバーしている可能性が高い。これらの数値は、プログラマーがパフォーマンスへの影響を理解し、システムを最適化するのに役立つ。

### レイテンシー数値とその重要性
レイテンシーとは、メモリへのアクセスやネットワーク経由でのデータ送信などの操作を開始してから完了するまでの遅延時間である。動画ではおそらく、以下のような典型的なレイテンシーがリストアップされている：
- L1キャッシュ参照：0.5ナノ秒（ns） - 最速のメモリアクセス。
- 同一データセンター内での往復：500マイクロ秒（us）または0.5ミリ秒（ms） - 分散システムに影響。

これらの数値は概算ではあるが、メモリとディスクストレージの選択など、システム設計における意思決定の指針となる。

### システム設計における文脈
これらのレイテンシーを理解することは、コードの最適化、トレードオフの判断、ユーザーエクスペリエンスの向上に役立つ。例えば、ディスクシークに10 msかかることを知っていれば、そのような操作を最小限に抑えるデータベース設計に影響を与えることができる。

### 意外な詳細
興味深い点は、SSD読み取り時間などの数値が技術の進歩とともに改善されている一方で、L1キャッシュアクセスなどのコアCPUレイテンシーは安定したままであることで、ハードウェア進化の不均一な影響を示している。

---

### 調査ノート：動画のレイテンシー数値の詳細分析

このノートは、動画「Latency Numbers Programmer Should Know: Crash Course System Design #1」でおそらく議論されているレイテンシー数値について、利用可能なオンラインコンテンツと関連リソースに基づいた包括的な探求を提供する。この分析は、プログラマーとシステム設計者のための情報を統合し、要約と詳細な洞察の両方を提供することを目的としている。

#### 背景と文脈
この動画は、[YouTube](https://www.youtube.com/watch?v=FqR5vESuKe0)でアクセス可能で、プログラマーにとって重要なレイテンシー数値に焦点を当てたシステム設計シリーズの一部である。レイテンシーは、操作の開始から完了までの時間遅延と定義され、システムパフォーマンスを理解する上で極めて重要である。動画のタイトルと関連する検索から、プログラミングコミュニティでよく参照される、GoogleのJeff Deanのような人物によって広められた標準的なレイテンシー数値をカバーしている可能性が高い。

オンライン検索により、「Latency Numbers Every Programmer Should Know」というGitHub Gist（[GitHub Gist](https://gist.github.com/jboner/2841832)）や2023年のMedium記事（[Medium Article](https://medium.com/@bojanskr/latency-numbers-every-programmer-should-know-d85f8d3f8e6a)）など、これらの数値について議論するいくつかのリソースが明らかになった。これらの情報源は、2013年のHigh Scalabilityの投稿（[High Scalability](https://highscalability.com/more-numbers-every-awesome-programmer-must-know/)）とともに、動画の可能性のあるコンテンツをまとめるための基礎を提供した。

#### レイテンシー数値のまとめ
収集した情報に基づくと、以下の表は、動画でおそらく議論されている標準的なレイテンシー数値をまとめたものであり、各操作の説明を含む：

| 操作                                      | レイテンシー (ns) | レイテンシー (us) | レイテンシー (ms) | 説明                                                          |
|-----------------------------------------|-----------------|-----------------|-----------------|-------------------------------------------------------------|
| L1キャッシュ参照                         | 0.5             | -               | -               | CPUに最も近い最速メモリであるレベル1キャッシュ内のデータへのアクセス。        |
| 分岐予測ミス                             | 5               | -               | -               | CPUが条件分岐を誤って予測した場合のペナルティ。                      |
| L2キャッシュ参照                         | 7               | -               | -               | L1より大きいが遅いレベル2キャッシュ内のデータへのアクセス。               |
| Mutex ロック/アンロック                  | 25              | -               | -               | マルチスレッドプログラムにおけるmutexの取得と解放にかかる時間。           |
| メインメモリ参照                          | 100             | -               | -               | メインメモリ（RAM）からのデータアクセス。                            |
| Zippyで1Kバイトを圧縮                   | 10,000          | 10              | -               | Zippyアルゴリズムを使用して1キロバイトを圧縮する時間。                |
| 1 Gbpsネットワークで1 KBを送信          | 10,000          | 10              | -               | 1ギガビット/秒のネットワークで1キロバイトを送信する時間。               |
| SSDから4 KBをランダム読み取り            | 150,000         | 150             | -               | ソリッドステートドライブからの4キロバイトのランダム読み取り。              |
| メモリから1 MBをシーケンシャル読み取り     | 250,000         | 250             | -               | メインメモリからの1メガバイトのシーケンシャル読み取り。                  |
| 同一データセンター内での往復              | 500,000         | 500             | 0.5             | 同一データセンター内でのネットワーク往復時間。                        |
| SSDから1 MBをシーケンシャル読み取り       | 1,000,000       | 1,000           | 1               | SSDからの1メガバイトのシーケンシャル読み取り。                       |
| HDDシーク                               | 10,000,000      | 10,000          | 10              | ハードディスクドライブが新しい位置にシークする時間。                    |
| ディスクから1 MBをシーケンシャル読み取り   | 20,000,000      | 20,000          | 20              | HDDからの1メガバイトのシーケンシャル読み取り。                       |
| パケット送信 CA->オランダ->CA            | 150,000,000     | 150,000         | 150             | カリフォルニアからオランダへのネットワークパケットの往復時間。             |

これらの数値は、主に2012年時点のものに一部更新を加えており、典型的なハードウェア性能を反映している。特にSSDとネットワークについては、技術進歩により変動があることが最近の議論で指摘されている。

#### 分析と含意
レイテンシー数値は固定されておらず、特定のハードウェアと構成に基づいて変動する可能性がある。例えば、Ivan Pesinの2020年のブログ投稿（[Pesin Space](http://pesin.space/posts/2020-09-22-latencies/)）は、ディスクとネットワークのレイテンシーがより優れたSSD（NVMe）と高速ネットワーク（10/100Gb）のおかげで改善された一方で、L1キャッシュアクセスなどのコアCPUレイテンシーは安定したままであると指摘している。この不均一な進化は、システム設計における文脈の重要性を強調している。

実際には、これらの数値は以下のいくつかの側面を導く：
- **パフォーマンス最適化**: ディスクシーク（10 ms）のような高レイテンシーの操作を最小化することは、アプリケーション速度を大幅に改善できる。例えば、頻繁にアクセスされるデータをディスクではなくメモリ（1 MB読み取りで250 us）にキャッシュすることで、待ち時間を削減できる。
- **トレードオフの判断**: システム設計者は、インメモリキャッシュとデータベースの使用など、選択に直面することが多い。メインメモリ参照（100 ns）がL1キャッシュ参照（0.5 ns）より200倍高速であることを知ることは、そのような判断に役立つ。
- **ユーザーエクスペリエンス**: Webアプリケーションでは、データセンター往復（500 us）のようなネットワークレイテンシーはページ読み込み時間に影響し、ユーザー満足度に影響を与える可能性がある。2024年のVercelブログ投稿（[Vercel Blog](https://vercel.com/blog/latency-numbers-every-web-developer-should-know)）は、フロントエンド開発においてこれを強調し、ネットワークの滝がレイテンシーを複合的にする方法に注目している。

#### 歴史的文脈と更新
元の数値は、Jeff Deanに帰され、Peter Norvigによって広められたもので、2010年頃にさかのぼり、Colin Scott（[Interactive Latencies](https://colin-scott.github.io/personal_website/research/interactive_latency.html)）のような研究者による更新がなされている。Dan Honによる2019年のMedium投稿（[Dan Hon Medium](https://medium.com/@hondanhon/more-latency-numbers-every-programmer-should-know-3142f0cf614d)）は、MacBook Proの再起動（90秒）のような、ユーモアがありながらも関連性のあるレイテンシーを追加し、技術関連のより広範な遅延を説明している。しかし、コアのレイテンシー数値は最小限の変更しか見ておらず、GitHub Gistは、物理的な制限に基づき、2023年時点で「非常に類似した」ままであると示唆している。

#### 結論と推奨事項
プログラマーとシステム設計者にとって、これらのレイテンシー数値を記憶することは、パフォーマンスチューニングのためのメンタルモデルを提供する。これらはガイドラインとして扱われるべきであり、特定のハードウェアに対して実際のベンチマークが実施されるべきである。量子コンピューティングや5Gネットワークなどの新興技術における更新に通じていることが重要である。GitHub GistやMedium記事などのリソースは、さらなる探求の出発点を提供する。

この分析は、動画の可能性のあるコンテンツに基づき、広範なオンライン調査で補完され、コンピューティングにおけるレイテンシー数値の永続的な関連性を強調し、最適なシステム設計のための技術的変化への適応を呼びかけている。

#### 主要な引用
- [Latency Numbers Every Programmer Should Know GitHub Gist](https://gist.github.com/jboner/2841832)
- [Latency Numbers Programmer Should Know YouTube Video](https://www.youtube.com/watch?v=FqR5vESuKe0)
- [Updated Latency Numbers Medium Article](https://medium.com/@bojanskr/latency-numbers-every-programmer-should-know-d85f8d3f8e6a)
- [More Numbers Every Awesome Programmer Must Know High Scalability](https://highscalability.com/more-numbers-every-awesome-programmer-must-know/)
- [Latency Numbers Every Web Developer Should Know Vercel Blog](https://vercel.com/blog/latency-numbers-every-web-developer-should-know)
- [Latency Numbers Every Engineer Should Know Pesin Space Blog](http://pesin.space/posts/2020-09-22-latencies/)
- [More Latency Numbers Every Programmer Should Know Dan Hon Medium](https://medium.com/@hondanhon/more-latency-numbers-every-programmer-should-know-3142f0cf614d)
- [Numbers Every Programmer Should Know By Year Interactive Latencies](https://colin-scott.github.io/personal_website/research/interactive_latency.html)