---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: WebSphere WASにおけるホットデプロイメント
translated: true
type: note
---

### WebSphere Application Server (WAS) におけるホットデプロイメントとホットスワップの理解

ホットデプロイメント（ホットリロードやホットスワッピングとも呼ばれる）は、アプリケーションサーバーの完全な再起動を必要とせずに、コード、構成、リソースなどのアプリケーションへの変更を更新およびデプロイできる開発手法です。これは、特に IBM WebSphere Application Server (WAS) のようなエンタープライズ環境において、頻繁なコード変更（例：バグ修正、ロジック調整、UI 要素の更新）が、長時間に及ぶサーバー起動時間によって遅延させられる可能性のある反復的な開発サイクルにおいて特に価値があります。WAS インスタンスの再起動には、大規模なアプリケーションの場合、数分またはそれ以上かかることもあり、ワークフローやテストを中断させます。

ここでは、「展開済み」WAR デプロイメントと強化されたホットスワッピングのためのツールに焦点を当て、WAS における高速な反復処理を実現するための実践的な戦略について、ステップバイステップで説明し、概念、動作方法、制限、実装のヒントを解説します。

#### 1. 「展開済み」WAR (アンパック・デプロイメント) としてのデプロイ
WAR (Web Application Archive) ファイルは、基本的に Web アプリケーションのリソース（JSP、サーブレット、Java クラス、静的ファイル (HTML/CSS/JS)、ライブラリ (JAR)、構成ファイル (例: web.xml)）を含む圧縮されたバンドルです。デフォルトでは、WAR は**パッケージ化された**（圧縮された）ファイルとしてデプロイされ、WAS はこれを不変として扱います。変更を行うには、アーカイブ全体の再パッケージ化と再デプロイが必要です。

**展開済み WAR** とは、デプロイ前に WAR ファイルをディレクトリ構造に展開（解凍）することを指します。これにより、アーカイブ全体に触れることなく、サーバーのファイルシステム上で個々のファイルやサブディレクトリを直接変更できます。

**これが高速な反復を可能にする理由:**
- **ファイル単位の更新:** 単一の JSP や Java クラスファイルを編集でき、WAS はそのコンポーネントのみを検出してリロードできます。
- **再パッケージ化の不要化:** 大規模な WAR の繰り返しの圧縮/解凍によるオーバーヘッドを回避します。
- **ホットリロードとの相乗効果:** サーバーが変更されたファイルを監視し、リフレッシュすることを容易にします。

**WAS で展開済み WAR をデプロイする方法:**
- **Admin Console を使用:**
  1. WAS Integrated Solutions Console (通常は `http://localhost:9060/ibm/console`) にログインします。
  2. **Applications > New Application > New Enterprise Application** に移動します。
  3. パッケージ化された WAR ファイルを選択する代わりに、展開された WAR のルートディレクトリ (例: `/path/to/myapp.war/` — ディレクトリであることを示す末尾のスラッシュに注意) を指定します。
  4. デプロイメントウィザードを完了し、"Deploy Web services" やその他のオプションがアプリに合っていることを確認します。
- **wsadmin (スクリプトツール) を使用:**
  ```bash
  wsadmin.sh -c "AdminApp.install('/path/to/myapp', '[ -MapWebModToVH [[myapp .* default_host.* virtual_host ]]]')"
  ```
  `/path/to/myapp` をあなたの展開済みディレクトリに置き換えてください。
- **開発サーバー (例: Liberty Profile):** 軽量テストの場合は、Open Liberty (WAS の亜種) を `server start` で使用し、展開済みアプリを `dropins` フォルダに配置して自動デプロイします。

**ベストプラクティス:**
- ソース管理ツール (例: Git) を使用して、IDE からの変更を展開済みディレクトリに同期します。
- 展開済みデプロイメントはより多くのストレージを消費するため、ディスク容量を監視します。
- 本番環境では、セキュリティと一貫性のためにパッケージ化された WAR を使用します。ホットデプロイメントは主に開発/テスト用です。

展開済みでデプロイされると、WAS の組み込みメカニズムが部分的なホットリロードのために作動します。

#### 2. WAS の組み込みホットリロードサポート
WAS は、特定のコンポーネントのホットリロードをネイティブでサポートしますが、限定的です。これはサーバーの**ファイルポーリング**メカニズムに依存しており、WAS は展開済みデプロイメントディレクトリの変更を定期的にスキャンします (JVM 引数 `-DwasStatusCheckInterval=5` などで設定可能、5秒間隔のチェック)。

**WAS が標準でサポートするもの:**
- **JSP (JavaServer Pages):**
  - JSP は初回アクセス時にサーブレットに動的にコンパイルされます。展開済み WAR 内の JSP ファイルを変更すると、WAS は変更を検出し、再コンパイルしてサーブレットをリロードできます。
  - **動作方法:** `ibm-web-ext.xmi` (WEB-INF 下) の `reloadInterval` を低い値 (例: 1秒) に設定して頻繁なチェックを行います。または、**Servers > Server Types > WebSphere application servers > [your_server] > Java and Process Management > Process definition > Java Virtual Machine > Custom properties** でグローバル設定 `com.ibm.ws.webcontainer.invokefilterscompatibility=true` を使用します。
  - **制限:** 積極的にキャッシュされていない JSP のみで動作します。インクルードやタグを持つ複雑な JSP はモジュールの再起動が必要な場合があります。
- **一部の Java クラス (サーブレットと EJB):**
  - 展開済みデプロイメントの場合、WAS は WEB-INF/classes または lib ディレクトリにある個々のクラスファイルをリロードできます。
  - **動作方法:** デプロイメント記述子またはコンソール (**Applications > [your_app] > Manage Modules > [module] > Reload behavior > Reload enabled**) で「アプリケーションリロード」を有効にします。
  - これは**モジュールレベルのリロード**をトリガーします。これはアプリ全体の再起動よりも高速ですが、それでもモジュール全体 (例: Web アプリ) をアンロード/リロードします。

**組み込みサポートの制限:**
- **真のホットスワップではない:** コアアプリケーションロジックの変更 (例: 実行中のサーブレットクラスのメソッド変更) は、古いクラスローダーをアンロードしないと有効になりません。`ClassNotFoundException` や古いコードが表示される可能性があります。
- **状態の喪失:** セッション、シングルトン、データベース接続がリセットされる可能性があります。
- **IBM JDK の特性:** WAS は IBM の JDK を使用することが多く、クラスのリロードに関して OpenJDK/HotSpot とは異なる特性があります。
- **構造的変更のサポートなし:** 新しいクラスの追加、メソッドシグネチャの変更、アノテーションの更新には再起動が必要です。
- **パフォーマンスオーバーヘッド:** 頻繁なポーリングは開発環境でリソースに負荷をかける可能性があります。

基本的な UI 調整 (JSP 編集) や単純なクラス更新にはこれで十分であり、無料です。しかし、「完全なホットスワップ」—実行中のコードを実行中に編集し、リロードなしで適用できる—には、サードパーティ製ツールが必要です。

#### 3. 完全なホットスワップソリューション
シームレスなコード変更 (例: Eclipse や IntelliJ のようなデバッガー接続された IDE でメソッド本体を編集し、即座に適用されるのを確認する) を実現するには、JVM のクラスローディングとインストルメンテーションをパッチ適用するプラグインを使用します。

**オプション 1: JRebel (有料プラグイン)**
- **概要:** Perforce (旧 ZeroTurnaround) による商用ツールで、Java アプリ向けの包括的なホットスワップを提供します。起動時にバイトコードをインストルメント化し、クラス、リソース、さらにはフレームワーク固有の変更 (例: Spring Bean, Hibernate エンティティ) のリロードを可能にします。
- **WAS で使用する理由:**
  - 展開済み WAR、OSGi バンドル、IBM JDK へのサポートを含む、WAS との深い統合。
  - メソッドシグネチャの変更やフィールドの追加 (標準 JVMTI ホットスワップの制限を超える) などの複雑なシナリオを処理。
  - **特徴:** IDE からの変更の自動検出; 手動再デプロイ不要; アプリ状態を保持。
- **セットアップ方法:**
  1. 公式サイトから JRebel をダウンロードし、Eclipse/IntelliJ プラグインとしてインストール。
  2. プロジェクト用に `rebel.xml` 設定ファイルを生成 (自動生成または手動)。
  3. WAS サーバーに JVM 引数を追加: `-javaagent:/path/to/jrebel.jar` (エージェント JAR へのフルパス)。
  4. デバッグモードで WAS を起動 (`-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=8000`)。
  5. IDE デバッガーをアタッチし、コードを編集 — JRebel が変更をライブで同期。
- **コスト:** サブスクリプションベース (個人向け ~$400/ユーザー/年; エンタープライズライセンスは様々)。無料トライアルあり。
- **長所:** 信頼性が高く、ユーザーフレンドリー、優れた WAS サポート。
- **短所:** 有料; プロジェクトごとのセットアップが必要。

**オプション 2: DCEVM + HotSwapAgent (無料代替案)**
- **概要:** 高度なホットスワッピングのためのオープンソースの組み合わせ。
  - **DCEVM (Dynamic Code Evolution VM):** HotSpot の JVMTI (Java Virtual Machine Tool Interface) を拡張し、より積極的なクラス再定義 (例: メソッドの追加/削除、階層の変更) を可能にする修正済み JVM。
  - **HotSwapAgent:** DCEVM 上に構築され、自動クラスリロードのための IDE 統合を提供するエージェント。
- **WAS で使用する理由:**
  - 無料でありながら強力な開発機能を提供し、JRebel の機能を模倣。
  - メソッド本体の変更、リソース更新、さらには一部のフレームワークリロード (プラグイン経由) をサポート。
- **WAS の IBM JDK との互換性に関する注意:**
  - WAS は通常 IBM の J9 JDK を同梱しており、これは**DCEVM をネイティブサポートしていません** (DCEVM は HotSpot 固有)。
  - **回避策:** 開発では OpenJDK/HotSpot に切り替えます (例: `setInitial.sh` での `JAVA_HOME` 上書きや Liberty の `jvm.options` 経由)。IBM JDK のガベージコレクションやセキュリティ機能は異なる可能性があるため、十分にテストしてください。
  - 本番環境では IBM JDK に戻します。これは開発専用です。
- **セットアップ方法:**
  1. **DCEVM のインストール:**
     - GitHub から DCEVM パッチャー JAR をダウンロード (例: JDK 11+ 用 `dcevm-11.0.0+7-full.jar`)。
     - 実行: `java -jar dcevm.jar /path/to/your/jdk/jre/lib/server/jvm.dll server` (Windows) または Linux 用同等コマンド (`libjvm.so`)。
     - これは JDK の JVM バイナリをパッチします — まずバックアップを取ってください！
  2. **HotSwapAgent のインストール:**
     - GitHub から `hotswap-agent.jar` をダウンロード。
     - WAS JVM 引数に追加: `-XXaltjvm=dcevm -XX:+TraceClassLoading -javaagent:/path/to/hotswap-agent.jar=DCEVM` (プラグインがある場合は追加、例: Spring 用 `=hotswap-spring`)。
  3. **IDE 統合:**
     - IntelliJ/Eclipse 用 HotSwapAgent プラグインをインストール。
     - 上記のようにデバッグ引数を付けて WAS を起動。
     - IDE でコードを編集して保存 — エージェントが自動的にリロード。
  4. **互換性のテスト:**
     - スモークテストを実行: 単純なサーブレットをデプロイし、メソッド (例: ログ行を追加) を編集し、エンドポイントにアクセスし、再起動なしで変更が反映されることを確認。
     - ログで `HotSwap failed: method limit reached` (DCEVM はクラスごとの変更数に制限あり) のようなエラーを確認。
- **長所:** 無料、カスタマイズ可能 (Spring, CDI などのプラグイン経由)、コミュニティサポート。
- **短所:** セットアップが面倒; 非標準 JVM での不安定性の可能性; HotSpot に限定 (IBM JDK 切り替えは注意深くテスト); JRebel ほど洗練されていない。

#### いつ何を使うべきか
- **展開済み WAR + 組み込みリロード:** 開発初期段階での迅速な JSP/静的ファイル調整用。
- **JRebel:** 予算が許し、エンタープライズレベルの信頼性が必要な場合。
- **DCEVM + HotSwapAgent:** 無料で完全なホットスワップが必要な場合、ただし JVM 互換性テストの時間を確保すること。

まとめると、これらの技術は WAS を重量級サーバーからより機敏な開発環境に変え、反復時間を数分から数秒に短縮します。即時の効果を得るために展開済み WAR から始め、必要に応じてツールを追加していきます。特定のエラーが発生している場合は、詳細を共有してトラブルシューティングを行ってください。

**参考文献:**  
[JRebel Documentation for WebSphere](https://www.jrebel.com/products/jrebel/tutorials/deploy-jrebel-websphere)  
[DCEVM GitHub Repo](https://github.com/dcevm/dcevm)  
[HotSwapAgent GitHub Repo](https://github.com/HotswapProjects/HotswapAgent)  
[IBM Knowledge Center: WebSphere Hot Deployment](https://www.ibm.com/docs/en/was/9.0.5?topic=applications-hot-deployment)