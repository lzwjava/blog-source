---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: WebSphere開発のためのIntelliJ IDEA
translated: true
type: note
---

### IBM WebSphere Application Server (WAS) 開発での IntelliJ IDEA の使用

IntelliJ IDEA は、IBM WebSphere Application Server (WAS) をターゲットとした Java EE アプリケーション開発において確かな選択肢です。IntelliJ IDEA は WAS が準拠する Java EE 標準をサポートし、エンタープライズアプリの構築、デプロイ、デバッグのための優れたツールを提供します。Eclipse は IBM のツールを介してよりネイティブな WAS 連携を備えていますが、IntelliJ も多少の設定でうまく動作します。以下では、基本設定、リモートデバッグ (WAS の JVM にアタッチできます)、および追加のヒントについて説明します。

#### 1. IntelliJ での WAS 開発のための初期設定
- **必要なプラグインのインストール**:
  - **ファイル > 設定 > プラグイン** に移動し、JetBrains Marketplace で "WebSphere Server" を検索します。ローカルサーバー管理 (例: IntelliJ からの WAS の起動/停止) を向上させるためにインストールします。このプラグインはバンドルされていないためオプションですが、ローカル開発では推奨されます。
  - Java EE および Jakarta EE プラグインが有効になっていることを確認してください (通常はプリインストールされています)。

- **プロジェクトの作成**:
  - 新しい **Java Enterprise** プロジェクトを開始します (または既存のプロジェクトをインポートします)。
  - **Web アプリケーション** アーキタイプを選択し、Java EE (例: WAS のバージョンが 9.x の場合、バージョン 8 または 9) 用に構成します。
  - 必要に応じて WAS 固有のライブラリへの依存関係を追加します (例: Maven/Gradle 経由で JSP サポートのために `com.ibm.websphere.appserver.api:jsp-2.3`)。

- **ローカル WAS サーバーの構成 (ローカル実行の場合、オプション)**:
  - **実行 > 構成の編集 > + > WebSphere Server > ローカル** に移動します。
  - ローカルの WAS インストールディレクトリを指定します (例: `/opt/IBM/WebSphere/AppServer`)。
  - サーバー名、JRE (WAS にバンドルされている IBM の JDK を使用)、およびデプロイオプション (例: ホットリロードのための展開済み WAR) を設定します。
  - デプロイの場合: **デプロイメント** タブで、アーティファクト (例: WAR ファイル) を追加し、コンテキストパスを設定します。

この設定により、ローカルテスト用に IntelliJ から直接実行/デプロイできるようになります。

#### 2. リモートデバッグ: IntelliJ を WAS JVM にアタッチする
IntelliJ デバッガーをリモートの WAS JVM に確実にアタッチできます。これは JDWP (Java Debug Wire Protocol) を介した標準的な Java リモートデバッグです。これはローカルおよびリモートの WAS インスタンスの両方で動作します。サーバーを「リモート JVM」として扱います。

**ステップ 1: WAS サーバーでデバッグを有効にする**
- **管理コンソール経由 (プロダクション環境に近い設定で推奨)**:
  - WAS 管理コンソールにログインします (例: `https://your-host:9043/ibm/console`)。
  - **サーバー > サーバーの種類 > WebSphere Application Servers > [対象サーバー] > デバッグサービス** に移動します。
  - **サーバー起動時にサービスを有効にする** をチェックします。
  - **JVM デバッグポート** を設定します (デフォルトは 7777。競合を避けるため 8000 などの未使用ポートを選択)。
  - 保存し、サーバーを再起動します。

- **server.xml 経由 (スタンドアロンまたはクイック編集用)**:
  - `$WAS_HOME/profiles/[プロファイル]/config/cells/[セル]/nodes/[ノード]/servers/[サーバー]/server.xml` を編集します。
  - `<processDefinitions>` セクション内の `<jvmEntries>` セクションに、以下を追加または更新します:
    ```
    <jvmEntries xmi:id="..." debugMode="true">
      <debugArgs>-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:8000</debugArgs>
    </jvmEntries>
    ```
    - `suspend=n` はサーバーを通常起動します (起動時に一時停止するには `suspend=y` を使用)。
    - `8000` を自身のポートに置き換えてください。
  - 保存し、サーバーを再起動します: `./startServer.sh [サーバー名]` (またはコンソール経由)。

- 検証: サーバーログに "JDWP: transport=dt_socket, address=*:8000" または類似のメッセージがあることを確認します。

**ステップ 2: IntelliJ でリモートデバッグを構成する**
- **実行 > 構成の編集 > + > リモート JVM デバッグ** に移動します。
  - 名前を付けます (例: "WAS Remote Debug")。
  - **デバッガーモード** を "Attach to remote JVM" に設定します。
  - **ホスト**: WAS サーバーの IP/ホスト名 (例: ローカルの場合は `localhost`、リモートの場合は `192.168.1.100`)。
  - **ポート**: JVM デバッグポート (例: 8000)。
  - オプションで、プロジェクトに特定のライブラリがある場合は **Use module classpath** を設定します。
  - 適用して閉じます。

**ステップ 3: アタッチとデバッグ**
  - コードにブレークポイントを設定します (例: サーブレットや EJB 内)。
  - アプリを WAS にデプロイします (管理コンソールまたは wsadmin スクリプト経由で手動)。
  - デバッグ構成を実行します (**実行 > 'WAS Remote Debug' のデバッグ**)。
  - アプリをトリガーします (例: HTTP リクエスト経由)。IntelliJ がアタッチし、実行がブレークポイントで一時停止します。
  - 一般的な問題: ファイアウォールがポートをブロックしている、JDK バージョンが一致しない (IntelliJ で WAS の IBM JDK を使用する)、設定変更後にサーバーが再起動されていない。

これは WAS 7+ (Liberty プロファイルを含む) で動作します。リモートサーバーの場合、デバッグポートへのネットワークアクセスを確保してください。

#### 3. 効率的な WAS 開発のためのその他のヒント
- **ホットデプロイ/ホットスワップ**: より高速な反復処理のために、「展開済み」WAR (解凍済み) としてデプロイします。WAS は JSP と一部のクラスのホットリロードをサポートしますが、完全なホットスワップ (再起動なしでのコード変更) には、JRebel プラグイン (有料) または DCEVM + HotSwapAgent (無料、ただし WAS の IBM JDK との互換性をテスト要) を使用します。

- **ビルドツール**: 依存関係に Maven または Gradle を使用します。クラスパスの肥大化を避けるため、WAS ランタイムライブラリを provided スコープとして追加します:
  ```
  <dependency>
    <groupId>com.ibm.websphere.appserver.runtime</groupId>
    <artifactId>shared</artifactId>
    <version>9.0.5</version>
    <scope>provided</scope>
  </dependency>
  ```
  `mvn clean package` を実行し、管理コンソール経由で WAR をデプロイします。

- **ロギングとプロファイリング**: アプリログに SLF4J/Logback を統合します。パフォーマンスには、VisualVM または YourKit を使用します (デバッグと同様にリモートでアタッチ)。WAS の PMI (Performance Monitoring Infrastructure) は優れています。メトリクスのために管理コンソールで有効にしてください。

- **テスト**: リモート WAS に対する統合テストに Arquillian を使用します。または、フル WAS なしでのローカル単体テストに Open Liberty (WAS 互換) を組み込みます。

- **バージョン固有の注意点**: WAS 9.x+ では、IntelliJ の Jakarta EE 移行ツールを活用します。WAS Liberty (マイクロプロファイル中心) を使用する場合、Liberty Tools プラグインは自動リロード付きの dev モードを追加します。

- **一般的な落とし穴**:
  - クラスパス問題: IntelliJ のプロジェクト SDK が WAS の JDK と一致していることを確認してください。
  - セキュリティ: リモートデバッグはポートを公開します。開発/信頼されたネットワークでのみ使用してください。
  - プラグインの制限: WebSphere プラグインは基本的な機能です。高度な機能には IBM の Rational Application Developer を検討してください (ただし、UX のためには IntelliJ に固執することをお勧めします)。

これで作業を開始できるはずです。特定の WAS バージョンを使用している場合は、詳細を共有するとより具体的なアドバイスが得られます。

#### 参考文献
- [Run/Debug Configuration: WebSphere Server | IntelliJ IDEA](https://www.jetbrains.com/help/idea/run-debug-configuration-websphere-server.html)
- [WebSphere remote server debug configuration in IntelliJ Idea](https://stackoverflow.com/questions/33013860/websphere-remote-server-debug-configuration-in-intellij-idea)
- [Debug code running on IBM Websphere using Eclipse / Intellij IDEA](https://davanum.wordpress.com/2009/11/20/debug-code-running-on-ibm-websphere-using-eclipse-intellij-idea/)
- [Debugging applications - IBM](https://www.ibm.com/docs/en/was/9.0.5?topic=applications-debugging)
- [Remote Debugging with IntelliJ IDEA | Baeldung](https://www.baeldung.com/intellij-remote-debugging)