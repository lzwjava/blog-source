---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: ビッグデータにおけるRustの可能性
translated: true
type: note
---

### Rustはビッグデータのための言語 (#rust2018)

**著者:** Andy Grove  
**公開日:** 2018年1月28日

このブログ記事は、「#rust2018」イニシアチブの一環として書かれた将来展望の記事です。Apache Sparkを使用して分散データ処理システムを構築してきた開発者であるAndy Groveは、Rustがメモリ安全性、パフォーマンス、予測可能性という中核的な強みを持ち、Javaのような言語で一般的なガベージコレクションやランタイムオーバーヘッドの落とし穴なしに、ビッグデータ処理に革命をもたらす未開拓の可能性を秘めていると論じています。

#### ビッグデータにおけるRustの主な論点
Groveは、自身のRustへの道のりを振り返ることから始めます。数年前に同僚から紹介され、2016年にRustConfに参加した後に夢中になりました。彼は、RustがC言語のような速度を実現しながら、バッファオーバーフローのような一般的なセキュリティ脆弱性を排除する能力を称賛しています。サーバーサイド作業では、スケーラブルな非同期アプリケーションを構築するための *futures* や *tokio* のようなクレートに注目しています。しかし、彼の真の情熱はビッグデータにあり、Rustが既存ツールの課題を解決できる可能性があるとしています。

彼の日々の仕事ではApache Sparkを使用しています。Sparkは分散データ処理の定番となりましたが、当初は単純な学術プロジェクトとして始まり、画期的なエンジニアリング修正によって規模が拡大されました。初期のSparkは以下の点で苦労していました:
- **Javaシリアライゼーションのオーバーヘッド**: ノード間のデータシャッフルが遅く、メモリを大量に消費しました。
- **ガベージコレクション(GC)のポーズ**: これらは予測不能なパフォーマンスを引き起こし、「OutOfMemory」エラーを発生させ、終わりのないチューニングを必要としました。

Sparkの「Project Tungsten」(2014年頃開始)は、以下によってこれを軽減しました:
- GCを回避するために、データをバイナリ形式(例: Parquetのようなカラムナー形式)でオフヒープに保存。
- バイトコードを介してCPU実行を最適化するための全段階コード生成を使用。

これらの変更により、ボトルネックはJVMの特性から生のCPUの限界へと移行し、パフォーマンス向上が高レベルの抽象化ではなく低レベルの効率性からもたらされることを証明しました。

Groveの大胆な仮説: もしSparkが最初からRustで構築されていたなら、基本的な実装であっても最初からパフォーマンスと信頼性を確立できたはずだ、というものです。Rustの所有権モデルは、GCなしでメモリ安全性を保証し、シリアライゼーションの肥大化や不安定なポーズを回避します。JVMフラグの微調整はもう必要なく、予測可能で高速な実行が実現します。彼はこれを、データ量が爆発的に増加する中で、Sparkのような既存のシステムを凌駕するRustの「独自の機会」と見ています。

#### DataFusionプロジェクト
このビジョンを具体化するために、Groveは**DataFusion**という、Rustで書かれたオープンソースのクエリエンジンのプロトタイプを立ち上げました。執筆時点(2018年初頭)ではアルファ版ですが、以下のデモが既に可能です:
- Parquetファイルを読み込み、フィルター、結合、集計などの操作を実行するための**DataFrame API** (例: [parquet_dataframe.rs](https://github.com/andygrove/datafusion/blob/master/examples/parquet_dataframe.rs))。
- 同じデータに対して宣言型のクエリを実行するための**SQL API** (例: [parquet_sql.rs](https://github.com/andygrove/datafusion/blob/master/examples/parquet_sql.rs))。

彼は2018年を通じて自身のRustスキルを磨き、何か有用なものを構築するために、空き時間を使ってこれをハックする計画です。コミュニティへの貢献を呼びかけ、リポジトリ [github.com/apache/arrow-datafusion](https://github.com/apache/arrow-datafusion) を紹介しています。

#### 更新情報 (2024年5月時点)
この記事には、DataFusionの成長を強調する回顧的な補足が含まれています:
- 2019年2月にApache Arrowに寄贈。
- 2019年7月にBallista(分散実行レイヤー)を発表: [Announcing Ballista](https://andygrove.io/2019/07/announcing-ballista/)。
- 2020年2月にDataFusion/Ballistaの内部を解説する自著 *How Query Engines Work* を出版: [Leanpubリンク](https://leanpub.com/how-query-engines-work)。
- 2021年4月にBallistaをApache Arrowに寄贈。
- 2024年3月にAppleが**DataFusion Comet**を寄贈し、SparkをRustベースの高速化で強化: [Arrowブログ](https://arrow.apache.org/blog/2024/03/06/comet-donation/) および [GitHub](https://github.com/apache/datafusion-comet)。
- 2024年4月にGroveがAppleに加入し、Cometの開発に従事。
- 2024年5月にDataFusionがトップレベルApacheプロジェクトとして卒業: [Arrowブログ](https://arrow.apache.org/blog/2024/05/07/datafusion-tlp/)。

Groveは、自身の本を通じてクエリエンジンに飛び込むよう読者を促し、データ集約型アプリケーションのゲームチェンジャーとしてのRustを位置づけて締めくくっています。

[Rustはビッグデータのための言語 (#rust2018)](https://andygrove.io/2018/01/rust-is-for-big-data/)