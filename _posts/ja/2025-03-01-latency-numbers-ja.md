---
audio: false
generated: true
lang: ja
layout: post
title: 遅延数
translated: true
---

### 重要ポイント
- ビデオのタイトルと関連するオンラインコンテンツから、プログラマーが知っておくべき標準的な遅延数値について議論している可能性が高いです。これには、L1キャッシュアクセス（0.5 ns）やネットワークの往復（最大150 ms）などの操作の時間が含まれます。これらの数値はハードウェアによって異なります。
- 証拠は、これらの数値が概算であり、特にSSDやネットワークの技術進歩を反映する更新が行われることを示唆しています。

### 導入
「Latency Numbers Programmer Should Know: Crash Course System Design #1」というビデオは、コンピュータ操作の重要な遅延数値をカバーしている可能性が高く、システム設計にとって不可欠です。これらの数値は、プログラマーにパフォーマンスの影響を理解し、システムを最適化するのに役立ちます。

### 遅延数値とその重要性
遅延は、メモリへのアクセスやデータの送信など、操作の開始から完了までの遅れです。ビデオでは、以下のような典型的な遅延がリストされている可能性があります：
- L1キャッシュ参照が0.5ナノ秒（ns）で、最も速いメモリアクセス。
- 同じデータセンター内での往復が500マイクロ秒（us）または0.5ミリ秒（ms）で、分散システムに影響を与えます。

これらの数値は概算ですが、システム設計の決定に役立ちます。例えば、メモリとディスクストレージの選択などです。

### システム設計におけるコンテキスト
これらの遅延を理解することは、コードの最適化、トレードオフの判断、ユーザー体験の向上に役立ちます。例えば、ディスクシークが10 msかかることを知っていると、データベース設計を最適化してそのような操作を最小限に抑えることができます。

### 予期せぬ詳細
興味深い点は、SSDの読み取り時間などの数値が技術の進歩により改善されている一方で、L1キャッシュアクセスなどのコアCPU遅延は安定していることです。これは、ハードウェア進化の影響が不均等であることを示しています。

---

### アンケートノート：ビデオからの遅延数値の詳細な分析

このノートは、YouTubeで視聴可能な「Latency Numbers Programmer Should Know: Crash Course System Design #1」というビデオで議論されている遅延数値について、オンラインコンテンツと関連リソースを基に包括的な探討を行います。この分析は、プログラマーとシステム設計者のために情報を総合し、これらの数値の重要性について概要と詳細な洞察を提供することを目指しています。

#### 背景とコンテキスト
このビデオは、システム設計に関するシリーズの一部であり、プログラマーにとって重要な遅延数値に焦点を当てています。遅延は、操作の開始から完了までの時間遅れであり、システムパフォーマンスを理解する上で重要です。ビデオのタイトルと関連検索から、GoogleのJeff Deanなどの人物がプログラミングコミュニティで人気のある標準的な遅延数値をカバーしていることが示唆されています。

オンライン検索により、いくつかのリソースがこれらの数値について議論しており、その中には「Latency Numbers Every Programmer Should Know」というGitHub Gist（[GitHub Gist](https://gist.github.com/jboner/2841832)）や2023年のMedium記事（[Medium記事](https://medium.com/@bojanskr/latency-numbers-every-programmer-should-know-d85f8d3f8e6a)）があります。これらのソースと2013年のHigh Scalabilityの投稿（[High Scalability](https://highscalability.com/more-numbers-every-awesome-programmer-must-know/)）を基に、ビデオの内容をまとめるための基礎を提供しました。

#### 遅延数値のまとめ
収集した情報を基に、ビデオで議論されている可能性のある標準的な遅延数値を以下の表にまとめました。各操作の説明も含まれています。

| 操作                                      | 遅延（ns） | 遅延（us） | 遅延（ms） | 説明                                                          |
|-------------------------------------------|------------|------------|------------|----------------------------------------------------------------------|
| L1キャッシュ参照                          | 0.5        | -          | -          | CPUに最も近い最も速いメモリへのデータアクセス。 |
| 分岐ミス予測                              | 5          | -          | -          | CPUが条件分岐を誤って予測した場合のペナルティ。       |
| L2キャッシュ参照                          | 7          | -          | -          | L1より大きいが遅いレベル2キャッシュへのデータアクセス。           |
| ミューテックスロック/アンロック              | 25         | -          | -          | マルチスレッドプログラムでミューテックスを取得および解放する時間。        |
| メインメモリ参照                          | 100        | -          | -          | メインランダムアクセスメモリ（RAM）からのデータアクセス。                  |
| Zippyを使用して1Kバイト圧縮               | 10,000     | 10         | -          | Zippyアルゴリズムを使用して1キロバイトを圧縮する時間。                |
| 1Gbpsネットワークを介して1KBバイト送信      | 10,000     | 10         | -          | 1ギガビット毎秒のネットワークを介して1キロバイトを送信する時間。      |
| SSDから4KBをランダムに読み取り            | 150,000    | 150        | -          | ソリッドステートドライブからの4キロバイトのランダム読み取り。                  |
| メモリから1MBを順次読み取り             | 250,000    | 250        | -          | メインメモリからの1メガバイトの順次読み取り。                       |
| 同じデータセンター内での往復              | 500,000    | 500        | 0.5        | 同じデータセンター内のネットワーク往復時間。                   |
| SSDから1MBを順次読み取り                | 1,000,000  | 1,000      | 1          | SSDからの1メガバイトの順次読み取り。                            |
| HDDシーク                                      | 10,000,000 | 10,000     | 10         | ハードディスクドライブが新しい位置にシークする時間。                 |
| ディスクから1MBを順次読み取り              | 20,000,000 | 20,000     | 20         | HDDからの1メガバイトの順次読み取り。                            |
| パケットCA->オランダ->CA送信                | 150,000,000| 150,000    | 150        | カリフォルニアからオランダへのネットワークパケットの往復時間。  |

これらの数値は主に2012年のもので、一部の更新が含まれています。特にSSDやネットワークの技術進歩により、ハードウェアの典型的なパフォーマンスが反映されています。

#### 分析と影響
これらの遅延数値は固定されておらず、特定のハードウェアや設定によって異なることがあります。例えば、2020年のIvan Pesinのブログ投稿（[Pesin Space](http://pesin.space/posts/2020-09-22-latencies/)）では、より高速なSSD（NVMe）やネットワーク（10/100Gb）のおかげでディスクとネットワークの遅延が改善されたことが示されていますが、L1キャッシュアクセスなどのコアCPU遅延は安定しています。この不均等な進化は、システム設計におけるコンテキストの重要性を強調しています。

実践において、これらの数値は以下の点を指導します：
- **パフォーマンス最適化**：ディスクシーク（10 ms）などの高遅延操作を最小限に抑えることで、アプリケーションの速度を大幅に向上させることができます。例えば、メモリ（250 usで1MB読み取り）に頻繁にアクセスするデータをキャッシュすることで、待ち時間を短縮できます。
- **トレードオフの決定**：システム設計者は、インメモリキャッシュを使用するかデータベースを使用するかのような選択を迫られることが多いです。メインメモリ参照（100 ns）がL1キャッシュ参照（0.5 ns）の200倍速いことを知っていると、そのような決定に役立ちます。
- **ユーザー体験**：ウェブアプリケーションでは、ネットワーク遅延（データセンター内の往復が500 us）がページ読み込み時間に影響を与え、ユーザー満足度に影響を与えることがあります。2024年のVercelブログ投稿（[Vercelブログ](https://vercel.com/blog/latency-numbers-every-web-developer-should-know)）では、フロントエンド開発においてネットワークウォーターフォールが遅延を重ねることが強調されています。

#### 歴史的背景と更新
これらの数値は、Jeff Deanが2010年頃に提唱し、Peter Norvigによって広く知られるようになったものです。研究者のColin Scott（[Interactive Latencies](https://colin-scott.github.io/personal_website/research/interactive_latency.html)）による更新もあります。2019年のDan HonのMedium投稿（[Dan Hon Medium](https://medium.com/@hondanhon/more-latency-numbers-every-programmer-should-know-3142f0cf614d)）では、MacBook Proの再起動（90秒）など、より広範な技術関連の遅延がユーモラスながらも関連性のあるものとして追加されています。しかし、コア遅延数値はほとんど変更されておらず、GitHub Gistは2023年までに「非常に似ている」と示唆しています。

#### 結論と推奨事項
プログラマーとシステム設計者にとって、これらの遅延数値を覚えることは、パフォーマンス調整のメンタルモデルを提供します。これらの数値はガイドラインとして扱われるべきであり、特定のハードウェアに対する実際のベンチマークが行われるべきです。量子コンピュータや5Gネットワークなどの新しい技術の更新について最新の情報を得ることが重要です。GitHub GistやMedium記事などのリソースは、さらに探求するための出発点を提供します。

この分析は、ビデオの内容を基にし、広範なオンライン調査を補助しています。これにより、コンピュータにおける遅延数値の持続的な関連性が強調され、技術的な変化に適応することがシステム設計の最適化にとって重要であることが示されています。

#### 主要な引用
- [Latency Numbers Every Programmer Should Know GitHub Gist](https://gist.github.com/jboner/2841832)
- [Latency Numbers Programmer Should Know YouTube Video](https://www.youtube.com/watch?v=FqR5vESuKe0)
- [Updated Latency Numbers Medium Article](https://medium.com/@bojanskr/latency-numbers-every-programmer-should-know-d85f8d3f8e6a)
- [More Numbers Every Awesome Programmer Must Know High Scalability](https://highscalability.com/more-numbers-every-awesome-programmer-must-know/)
- [Latency Numbers Every Web Developer Should Know Vercel Blog](https://vercel.com/blog/latency-numbers-every-web-developer-should-know)
- [Latency Numbers Every Engineer Should Know Pesin Space Blog](http://pesin.space/posts/2020-09-22-latencies/)
- [More Latency Numbers Every Programmer Should Know Dan Hon Medium](https://medium.com/@hondanhon/more-latency-numbers-every-programmer-should-know-3142f0cf614d)
- [Numbers Every Programmer Should Know By Year Interactive Latencies](https://colin-scott.github.io/personal_website/research/interactive_latency.html)