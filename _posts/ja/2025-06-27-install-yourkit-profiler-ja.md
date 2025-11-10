---
audio: false
generated: true
lang: ja
layout: post
title: UbuntuへのYourKit Java Profilerインストール
translated: true
type: note
---

YourKit Java Profiler を Ubuntu にインストールするには、YourKit ウェブサイトで公開されている情報に基づき、以下の手順に従ってください。

1. **プロファイラのダウンロード**:
   - YourKit Java Profiler のダウンロードページ ([https://www.yourkit.com/java/profiler/download/](https://www.yourkit.com/java/profiler/download/)) にアクセスします。
   - Linux 版 YourKit Java Profiler 2025.3 を選択します。このバージョンは Java 8 から Java 24 をサポートし、arm32, arm64, ppc64le, x64, x86 などのアーキテクチャの Linux (Ubuntu を含む) と互換性があります。お使いのシステムが[システム要件](https://www.yourkit.com/docs/java/system-requirements/)を満たしていることを確認してください。

2. **アーカイブのダウンロード**:
   - Linux 用の `.zip` アーカイブ (例: `YourKit-JavaProfiler-2025.3-<build>.zip`) をダウンロードします。ダウンロードリンクは YourKit のダウンロードページにあります。

3. **アーカイブの解凍**:
   - ターミナルを開き、ダウンロードしたファイルがあるディレクトリ (例: `~/Downloads`) に移動します。
   - 以下のコマンドを使用してアーカイブを解凍します:
     ```bash
     unzip YourKit-JavaProfiler-2025.3-<build>.zip -d /opt/yourkit
     ```
     `<build>` はダウンロードしたファイルの実際のビルド番号に置き換えてください。このコマンドはプロファイラを `/opt/yourkit` に展開します。別のディレクトリを選択することもできます。

4. **プロファイラの実行**:
   - 展開したディレクトリに移動します:
     ```bash
     cd /opt/yourkit
     ```
   - 提供されているスクリプトを使用してプロファイラを実行します:
     ```bash
     ./bin/profiler.sh
     ```
     これにより YourKit Java Profiler のユーザーインターフェースが起動します。

5. **オプション: ライセンスキーを使用した無人インストール**:
   - ライセンスキーをお持ちで、インストールを自動化したい場合は、コマンドラインオプションを使用して EULA に同意し、ライセンスキーを適用できます。例:
     ```bash
     ./bin/profiler.sh -accept-eula -license-key=<key>
     ```
     `<key>` は実際のライセンスキーに置き換えてください。これは自動化やスクリプトによるセットアップに便利です。

6. **開発環境との統合 (オプション)**:
   - Eclipse、IntelliJ IDEA、NetBeans などの IDE を使用する場合、YourKit はシームレスな統合のためのプラグインを提供します。例えば Eclipse の場合:
     - Eclipse を開き、**Help > Install New Software** に移動します。
     - YourKit プラグインリポジトリを追加します: `https://www.yourkit.com/download/yjp2025_3_for_eclipse/`。
     - YourKit Java Profiler プラグインを選択し、インストールのプロンプトに従い、必要に応じて Eclipse を再起動します。
     - または、オフラインアーカイブ `<Profiler Installation Directory>/lib/eclipse-plugin/yjp2025_3_for_eclipse.zip` を使用します。
   - インストール後、Eclipse のツールバー、メインメニュー、またはコンテキストメニューに「Profile」アクションが表示され、簡単にプロファイリングできるようになります。

7. **インストールの確認**:
   - プロファイラが実行されると、ウェルカム画面が表示され、ローカルで実行中の Java アプリケーションの監視、リモートアプリケーションへの接続、既存のスナップショットのオープンが可能になります。プロファイラの機能を探索するためにデモアプリケーションをロードすることもできます。

8. **追加の注意点**:
   - 問題が発生した場合は、YourKit Java Profiler が互換性のある JVM を必要とするため、システムに Java (バージョン 8 以上) がインストールされていることを確認してください。Java のバージョンは以下のコマンドで確認できます:
     ```bash
     java -version
     ```
   - リモートプロファイリングを行う場合は、リモートサーバー上のアプリケーションをプロファイリングするために SSH アクセスが設定されていることを確認してください。
   - YourKit は 15 日間の無料トライアルを提供しているため、最初はライセンスキーは必要ありません。非商用のオープンソースプロジェクトの場合は、YourKit セールスに連絡して無料ライセンスを取得できます。
   - プロファイラの起動に失敗した場合 (例: インストールディレクトリにスペースが含まれている場合)、展開したフォルダを `/opt/yourkit` などのスペースのないパスに移動してください。

さらなるサポートが必要な場合は、[YourKit ドキュメント](https://www.yourkit.com/docs/java/)を参照するか、[YourKit ウェブサイト](https://www.yourkit.com/support/)からサポートに連絡してください。

特定のステップについてサポートが必要な場合はお知らせください！