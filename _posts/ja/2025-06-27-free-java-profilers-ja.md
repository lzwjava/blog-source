---
audio: false
generated: true
lang: ja
layout: post
title: YourKit Java プロファイラーの無料代替トップ
translated: true
type: note
---

はい、YourKit Java Profilerと同様の機能を提供する無料のJavaプロファイラが存在しますが、機能性、使いやすさ、分析の深さは様々です。以下に、CPU、メモリ、スレッドのプロファイリング能力、および開発環境と本番環境の両方への適合性に基づいて、YourKit Java Profilerの最高の無料代替ツールをいくつか紹介します：

1. **Java VisualVM**:
   - **説明**: 無料のオープンソースプロファイリングツールで、JDK 8までJava Development Kit (JDK)に同梱され、現在は[visualvm.github.io](https://visualvm.github.io/)からスタンドアロンでダウンロード可能です。いくつかのJDKコマンドラインツール（例: `jstat`, `jmap`, `jconsole`）をユーザーフレンドリーなGUIに統合しています。
   - **機能**:
     - CPU使用率、メモリ、ガベージコレクション、スレッドアクティビティの監視。
     - ローカルおよびリモートプロファイリングをサポート。
     - プラグインによる機能拡張（例: MBeans, スレッドダンプ）。
     - ヒープダンプとスレッド状態の可視化による基本的なメモリリーク検出とパフォーマンス分析。
   - **YourKitとの比較**: YourKitほど機能豊富ではありませんが、VisualVMは軽量で基本的なプロファイリングタスクに十分です。YourKitの「what-if」CPUプロファイリングや詳細なデータベースクエリ分析のような高度な機能はありませんが、開発者にとっては優れた出発点です。
   - **Ubuntuでのセットアップ**:
     ```bash
     sudo apt update
     sudo apt install visualvm
     visualvm
     ```
     または、公式サイトから最新版をダウンロードして実行：
     ```bash
     unzip visualvm_<バージョン>.zip -d /opt/visualvm
     cd /opt/visualvm/visualvm_<バージョン>/bin
     ./visualvm
     ```
   - **最適な用途**: 初心者、小規模プロジェクト、または迅速でコストのかからないプロファイリングソリューションを必要とする開発者。[](https://www.baeldung.com/java-profilers)

2. **Java Mission Control (JMC)**:
   - **説明**: JDK（JDK 7u40以降）に含まれる無料のオープンソースツールで、パフォーマンス監視とプロファイリングを行います。低オーバーヘッドで詳細なランタイムデータをキャプチャするJava Flight Recorder (JFR) を基盤としています。
   - **機能**:
     - CPU、メモリ、JVMイベントの詳細な分析のためのフライトレコーディングを提供。
     - メソッド呼び出しツリー、メモリ割り当て、スレッドアクティビティの可視化。
     - 低オーバーヘッドのため、本番環境に適しています。
     - IntelliJ IDEAやEclipseなどのIDEと統合可能（プラグイン経由）。
   - **YourKitとの比較**: JMCはVisualVMよりも高度で、本番環境でのプロファイリングにおいてYourKitと競合します。YourKitの高度なUI機能（例: フレームグラフ、詳細な例外プロファイリング）の一部は欠けていますが、JVM内部の分析と長時間実行アプリケーションの最適化において強力です。
   - **Ubuntuでのセットアップ**:
     - JMCはOpenJDKまたはOracle JDKに含まれています。起動するには：
       ```bash
       jmc
       ```
     - JDKがバージョン7以上であることを確認（例: OpenJDK 11 または 17）：
       ```bash
       sudo apt install openjdk-17-jdk
       ```
     - アプリケーションに対してJFRを有効化するためにJVMフラグを追加（古いJDKでは `-XX:+UnlockCommercialFeatures -XX:+FlightRecorder` など。新しいバージョンでは不要）。
   - **最適な用途**: 詳細なJVMの洞察を必要とする、本番グレードのアプリケーションを扱う開発者および運用チーム。[](https://www.bairesdev.com/blog/java-profiler-tool/)[](https://www.javacodegeeks.com/2024/04/top-java-profilers-for-2024.html)

3. **Async Profiler**:
   - **説明**: 低オーバーヘッドのCPUおよびメモリプロファイリング用に設計された、無料のオープンソース（Apache 2.0 ライセンス）プロファイラ。ネイティブメソッド呼び出しや高性能アプリケーション、特に高頻度取引（HFT）などの低レイテンシードメインで広く使用されています。
   - **機能**:
     - CPUボトルネックを直感的に可視化するフレームグラフを生成。
     - CPU、メモリ割り当て、ロック競合のプロファイリングをサポート。
     - Linux、macOS、Windowsで動作し、オーバーヘッドが最小限。
     - ローカルおよびリモートアプリケーションのプロファイリングが可能。
   - **YourKitとの比較**: Async Profilerは、フレームグラフの生成とネイティブメソッドのプロファイリングにおいて優れており、YourKitもこれらをサポートしていますが、より洗練されたUIを備えています。YourKitの包括的なデータベースクエリプロファイリングやGUI駆動の分析機能はありませんが、パフォーマンスボトルネックの特定に非常に効果的です。
   - **Ubuntuでのセットアップ**:
     - [GitHub](https://github.com/async-profiler/async-profiler)から最新リリースをダウンロード：
       ```bash
       wget https://github.com/async-profiler/async-profiler/releases/download/v3.0/async-profiler-3.0-linux-x64.tar.gz
       tar -xvzf async-profiler-3.0-linux-x64.tar.gz -C /opt/async-profiler
       ```
     - Javaアプリケーションでプロファイラを実行（`<pid>` をプロセスIDに置き換え）：
       ```bash
       /opt/async-profiler/profiler.sh -d 30 -f profile.svg <pid>
       ```
     - 生成されたフレームグラフ（`profile.svg`）をブラウザで表示。
   - **最適な用途**: フレームグラフやネイティブメソッドのプロファイリングを必要とする、パフォーマンスがクリティカルなアプリケーションを扱う上級開発者。[](https://www.reddit.com/r/java/comments/1brrdvc/java_profilers/)

4. **Arthas**:
   - **説明**: Alibabaによるオープンソース（Apache 2.0 ライセンス）の診断ツールで、アプリケーションの再起動なしでのリアルタイムの本番環境監視とプロファイリング向けに設計されています。[arthas.aliyun.com](https://arthas.aliyun.com/)で利用可能。
   - **機能**:
     - CPU、メモリ、スレッド使用率のリアルタイム監視。
     - トラブルシューティングのための動的クラス再定義と逆コンパイル。
     - 本番環境での問題診断のためのコマンドラインインターフェース。
     - メソッド実行時間のプロファイリングとホットスポットの特定。
   - **YourKitとの比較**: ArthasはYourKitほどGUI駆動ではなく、詳細な事後分析よりもリアルタイム診断に焦点を当てています。メモリリーク検出についてはYourKitほど包括的ではありませんが、中断を最小限に抑えることが重要な本番環境において優れています。
   - **Ubuntuでのセットアップ**:
     - Arthasをダウンロードしてインストール：
       ```bash
       wget https://arthas.aliyun.com/arthas-boot.jar
       java -jar arthas-boot.jar
       ```
     - インタラクティブなプロンプトに従って、実行中のJVMプロセスにアタッチ。
   - **最適な用途**: 重いセットアップなしで、本番環境でのリアルタイム診断を必要とする運用チームと開発者。[](https://www.javacodegeeks.com/2024/04/top-java-profilers-for-2024.html)

5. **Eclipse Memory Analyzer (MAT)**:
   - **説明**: メモリプロファイリングとヒープダンプ分析に特化した無料のオープンソースツール。[eclipse.org/mat/](https://eclipse.org/mat/)で利用可能。
   - **機能**:
     - メモリリークの検出とメモリ使用量の最適化のためのヒープダンプ分析。
     - オブジェクト割り当てと参照に関する詳細なレポートを提供。
     - 軽量でEclipse IDEと統合可能。
   - **YourKitとの比較**: MATはメモリ分析に特化しており、YourKitのCPUやデータベースプロファイリング機能はありません。メモリ固有のタスクでは強力な代替手段ですが、YourKitの包括的な機能セットを完全に置き換えるものではありません。
   - **Ubuntuでのセットアップ**:
     - MATをダウンロードしてインストール：
       ```bash
       sudo apt install eclipse-mat
       ```
     - または、EclipseのWebサイトからスタンドアロンバージョンをダウンロードして実行：
       ```bash
       unzip MemoryAnalyzer-<バージョン>.zip -d /opt/mat
       /opt/mat/MemoryAnalyzer
       ```
     - `jmap` または YourKitを使用してヒープダンプを生成し、MATで開いて分析。
   - **最適な用途**: メモリリーク検出とヒープ分析に焦点を当てる開発者。[](https://alternativeto.net/software/yourkit-java-profiler/)

### 主な考慮事項：
- **機能ギャップ**: VisualVM、JMC、Async Profilerなどの無料ツールは強力ですが、YourKitの詳細なデータベースクエリプロファイリング、例外分析、または「what-if」CPUプロファイリング機能などの高度な機能が不足している場合があります。YourKitの洗練されたUIと統合機能（Eclipse、IntelliJなどとの）も、一部のワークフローではより使いやすくしています。[](https://www.baeldung.com/java-profilers)[](https://digma.ai/9-best-java-profilers-to-use-in-2024/)
- **ユースケース**:
  - **小規模プロジェクトまたは初心者**には、VisualVMまたはEclipse MATが十分でセットアップが容易です。
  - **本番環境**では、低オーバーヘッドとリアルタイム機能のため、JMCまたはAsync Profilerが優れています。
  - **複雑なエンタープライズアプリケーション**では、包括的な機能セットのためにYourKitまたはJProfiler（もう一つの有料代替手段）が依然として好まれるかもしれませんが、追加の努力で無料ツールでも十分な場合があります。[](https://www.javacodegeeks.com/2024/04/top-java-profilers-for-2024.html)[](https://xperti.io/best-java-profiler-tools/)
- **コスト**: YourKitは商用ライセンス（個人利用で約499ドル～）が必要ですが、15日間の無料トライアルと非商用のオープンソースプロジェクト向けの無料ライセンスを提供しています。対照的に、上記のツールは完全に無料です。[](https://bell-sw.com/blog/a-guide-to-java-profiling-tools-techniques-best-practices/)[](https://xperti.io/best-java-profiler-tools/)
- **コミュニティのフィードバック**: XやRedditの投稿では、Async Profilerがネイティブメソッドのプロファイリングとフレームグラフの正確さで人気があることが強調されています。