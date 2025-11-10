---
audio: false
generated: true
lang: ja
layout: post
title: Rustの主要貢献者と創設者たち
translated: true
type: note
---

Rustエコシステムは活気に満ち、成長を続けており、多くの個人や組織が重要な貢献を果たしています。以下に、主要な貢献者、プログラマー、影響力のあるプロジェクト、創設者について紹介します：

### Rustの創設者

Rustプログラミング言語の主な創設者は以下の人物です：

* **Graydon Hoare:** 2006年にMozillaで勤務中、CやC++で蔓延していたメモリ安全性の問題に対処するシステム言語への欲求から、個人プロジェクトとしてRustを開始しました。彼は言語の基礎的な原則を確立しました。

MozillaにおけるRustの初期開発と進化に貢献した他の主要人物には以下が含まれます：

* **Niko Matsakis:** Rustコンパイラと言語設計への長年の貢献者、特にボローチェッカーに関して。
* **Patrick Walton**
* **Felix Klock**
* **Manish Goregaokar**

### トップRustエコシステム貢献者 & プログラマー (高く評価されている、オープンソース作業)

「トップ30」を明確に定義することは困難です。貢献は多様で、多くの個人やチームに広がっています。しかし、以下はオープンソース作業とRustコミュニティへの影響で高く認識されているプログラマーと主要貢献者です：

* **Steve Klabnik:** 多作な著述家、教育者、コアチームメンバー。Rustドキュメント（例：「The Rust Programming Language Book」）への貢献とRustの提唱で知られています。現在はOxide Computer Companyで、Rustをハードウェア/ソフトウェアシステムに応用しています。
* **Nicholas Matsakis (nikomatsakis):** Rustコンパイラ、特にRustのメモリ安全性保証の中核であるボローチェッカーの設計と実装に貢献。AWSでRustに取り組んでいます。
* **Mara Bos:** Rustライブラリチームの著名なメンバーで、標準ライブラリの様々な側面と言語の進化に積極的に関与。Fusion Engineeringの共同創設者でもあります。
* **Carol Nichols:** Rustコミュニティのもう一人の重要人物で、「The Rust Programming Language Book」の共著者、Rust Foundationの理事を務めています。Rustの採用と持続可能性のために積極的に提唱活動を行っています。
* **Jon Gjengset (jonhoo):** Rustの内部構造、特に並行性に関する深い探求と、多くの人々が高度なRustの概念を学ぶのに役立つ優れた教育的コンテンツと配信で知られています。
* **Alex Crichton:** `rust-lang/rust` や `crates.io-index` を含む様々なRustプロジェクトへの重要な貢献者で、エコシステムのインフラストラクチャにおいて重要な役割を果たしています。
* **Ralf Jung:** Rustコードにおける未定義動作を特定するのに役立つ、Rust用UBM（Undefined Behavior Machine）インタプリタであるMiriの作業で知られています。
* **Bryan Cantrill:** Oxide Computer CompanyのCTO兼共同創設者で、システムプログラミングと産業界におけるRustの強力な提唱者です。
* **Josh Triplett:** 長年のRust貢献者でありコアチームメンバーで、言語開発の多くの側面に関与しています。
* **Armin Ronacher (mitsuhiko):** Python Flaskフレームワークの創作者であり、特にSentryにおいて、Rust採用の重要な推進力となっています。
* **Andrew Gallant (BurntSushi):** 高速なgrep代替ツールである `ripgrep` や `regex` など、高度に最適化され広く使用されているRustクレートで知られています。
* **Syrus Akbary:** Rustを動力とするWebAssemblyランタイム、Wasmerの創作者。
* **Frank McSherry:** 差分データフローや、Rustにおける高度な並行性とデータ処理を探求する他のプロジェクトでの作業で知られています。
* **Jeremy Soller:** System76、そして現在はOxide Computer Companyでの作業は、オペレーティングシステムレベルまでRustの実現可能性を示しています。
* **Guillaume Gomez:** RustコンパイラとGTK-RSプロジェクト（GTKのRustバインディング）への多作な貢献者。
* **Pietro Albini:** 重要なRustインフラストラクチャへの多大な貢献者であり、Rustコアチームのメンバーです。
* **Dirkjan Ochtman:** Rustにおける安全な通信のための重要なライブラリである `rustls` と `quinn` のメンテナンスを担当。
* **Gary Guo:** LinuxカーネルへのRust統合を目指す重要な取り組みであるRust for Linuxのメンテナンスを担当。
* **Manish Goregaokar:** Googleのシニアソフトウェアエンジニアで、Unicode関連作業を含む様々なRustプロジェクトに貢献。

### トップオープンソースRustプロジェクト (高い影響力を持つ)

Rustの強みを示し、大きな影響を与えている多くのオープンソースプロジェクトがあります：

1.  **Rust Lang/Rust (Rustコンパイラと標準ライブラリ):** すべての人が信頼性が高く効率的なソフトウェアを構築することを可能にする核心プロジェクト自体。
2.  **Tauri Apps/Tauri:** Webフロントエンドを使用した、より小さく、高速で、安全なデスクトップおよびモバイルアプリケーションを構築するためのフレームワーク。Electronに似ていますが、より効率的です。
3.  **RustDesk/RustDesk:** オープンソースのリモートデスクトップアプリケーション。TeamViewerの人気のある代替品です。
4.  **Alacritty/Alacritty:** その高性能で知られる、クロスプラットフォームのOpenGLターミナルエミュレータ。
5.  **Tokio/Tokio:** Rustの基礎的な非同期ランタイムで、高性能ネットワークアプリケーションの構築に広く使用されています。
6.  **Hyper/Hyper:** Rust用の高速で正確なHTTPライブラリ。しばしばTokioと組み合わせて使用されます。
7.  **Actix/Actix-web:** 強力で高速、かつ高度に並行性の高いRust用Webフレームワーク。
8.  **Axum/Axum:** TokioとHyperで構築されたWebアプリケーションフレームワークで、エルゴノミクスと強力な型付けを重視しています。
9.  **Ripgrep (BurntSushi/ripgrep):** ディレクトリを再帰的に検索して正規表現パターンを探す行指向検索ツール。`grep` よりも大幅に高速です。
10. **Bat (sharkdp/bat):** 翼のある `cat(1)` クローンで、シンタックスハイライト、Git統合などを提供します。
11. **Fd (sharkdp/fd):** `find` のシンプルで高速、かつユーザーフレンドリーな代替品。
12. **Meilisearch/Meilisearch:** 強力で高速、かつ関連性の高い検索エンジン。
13. **Polars/Polars:** 高速なDataFrameライブラリで、データ操作におけるPandasのRust代替としてしばしば見られます。
14. **BevyEngine/Bevy:** 爽快にシンプルなデータ駆動型ゲームエンジン。Rustで構築されています。
15. **Helix Editor/Helix:** NeovimとKakouneにインスパイアされたモダンなモーダルテキストエディタ。Rustで書かれています。
16. **Nushell/Nushell (または Nu):** プログラミング言語の概念をコマンドラインに持ち込むことを目指すモダンなシェル。
17. **Deno/Deno:** JavaScriptとTypeScriptのための安全なランタイム。RustとV8で構築されています。
18. **Firecracker MicroVM/Firecracker:** AWSによって開発された、サーバーレスコンピューティングに使用される軽量仮想化技術。
19. **Crates.io:** Rustプログラミング言語の公式パッケージレジストリ。エコシステムに不可欠です。
20. **Rustlings (rust-lang/rustlings):** ユーザーがRustコードを読み書きすることに慣れるための小さな演習。初心者にとって非常に貴重です。
21. **Yewstack/Yew:** WebAssemblyを使用してクライアント側Webアプリケーションを構築するためのモダンなRustフレームワーク。
22. **DioxusLabs/Dioxus:** クロスプラットフォームアプリケーションを構築するための、もう一つの人気のある宣言型UIライブラリ。
23. **Servo/Servo:** 高性能で並列処理を行うブラウザエンジン。Mozillaによって開発され、後にLinux Foundationに移管されました。
24. **Rocket/Rocket:** 型安全性と開発者体験で知られるRust用Webフレームワーク。
25. **Solana/Solana:** 高性能ブロックチェーンプラットフォーム。そのコアコンポーネントの大部分がRustで書かれています。
26. **Substrate/Substrate:** カスタムブロックチェーンを構築するためのフレームワーク。こちらもRustを多用しています。
27. **Wasmtime/Wasmtime:** WebAssemblyとWASI（WebAssembly System Interface）のためのスタンドアロンのJITスタイルランタイム。
28. **Delta (dandavison/delta):** `diff`、`git`、`merge` 出力用のシンタックスハイライトを備えたページャー。
29. **Spotify TUI (Rigellute/spotify-tui):** Spotify用のターミナルユーザーインターフェース。
30. **mdBook (rust-lang/mdBook):** Markdownファイルから本を作成するコマンドラインツール。「The Rust Programming Language Book」を含む多くのRustプロジェクトで使用されています。

このリストは完全なものではなく、Rustエコシステムは常に進化しており、新しく影響力のあるプロジェクトが定期的に出現しています。コミュニティの強みは、その協力的な性質と、オープンソース貢献の高品質さにあります。