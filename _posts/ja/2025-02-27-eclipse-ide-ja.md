---
audio: false
generated: true
lang: ja
layout: post
title: Eclipseの使い方
translated: true
type: note
---

### 主なポイント
- Eclipse は IBM WebSphere Liberty、Spring、Spring Boot、Maven と効果的に連携できる可能性が高いですが、セットアップには特定の設定が必要です。
- 調査によると、機能を強化するために Eclipse に Spring Tool Suite (STS) と IBM Liberty Developer Tools をプラグインとしてインストールすることが推奨されています。
- 証拠から、STS または Spring Initializr を使用して Spring Boot プロジェクトを作成し、その後 WebSphere Liberty へのデプロイ用に設定する方法が有力です。

### Eclipse のセットアップ
まず、[Eclipse Downloads](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers) から「Eclipse IDE for Enterprise Java and Web Developers」をダウンロードしてインストールします。ターミナルで `java -version` を実行して、JDK 17 以降がインストールされていることを確認してください。

### Spring および Spring Boot の設定
Eclipse で Help -> Eclipse Marketplace に移動し、「Spring Tools」を検索して適切なバージョンをインストールすることで、Spring Tool Suite (STS) プラグインをインストールします。これにより Spring および Spring Boot 開発が強化されます。File -> New -> Spring Starter Project から Eclipse 内で直接新しい Spring Boot プロジェクトを作成でき、ビルドツールとして Maven を選択し、Spring Web などの必要な依存関係を追加できます。

### IBM WebSphere Liberty との統合
Eclipse Marketplace で「IBM Liberty Developer Tools」を検索し、インストールプロンプトに従ってインストールします。Window -> Preferences -> Servers -> Runtime Environments に移動し、新しい WebSphere Liberty ランタイムを追加し、File -> New -> Other -> Server 経由でサーバーインスタンスを作成することで、WebSphere Liberty サーバーをセットアップします。Spring Boot サポートのために、サーバーの server.xml に `<feature>springBoot-2.0</feature>` が含まれていることを確認してください。詳細は [Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html) を参照してください。

### アプリケーションのデプロイ
Spring Boot アプリケーションを、組み込みサーバーを起動する main メソッドを使用する代わりに `SpringBootServletInitializer` を拡張するように変更し、pom.xml で `<packaging>war</packaging>` を設定して WAR ファイルとしてパッケージ化します。プロジェクトを右クリックし、「Run As -> Run on Server」を選択し、Liberty サーバーを選択してデプロイします。これにより、アプリケーションが Liberty の Web コンテナ上で実行されることが保証されます。

---

### サーベイノート: Eclipse を IBM WebSphere Liberty、Spring、Spring Boot、Maven と共に使用するための包括的ガイド

このガイドは、これらのエコシステムで作業する開発者向けに、Eclipse を IBM WebSphere Liberty、Spring、Spring Boot、Maven と連携させて効果的に使用するための詳細な手順を提供します。このプロセスには、Eclipse のセットアップ、必要なプラグインのインストール、プロジェクトの作成と設定、およびアプリケーションのデプロイが含まれ、2025年2月27日現在の統合とベストプラクティスに焦点を当てています。

#### Eclipse のセットアップと前提条件
Eclipse は、特にエンタープライズアプリケーション向けの堅牢な Java 開発 IDE として機能します。このセットアップでは、[Eclipse Downloads](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers) で利用可能な「Eclipse IDE for Enterprise Java and Web Developers」バージョン 2024-06 をダウンロードします。ターミナルで `java -version` を実行して、システムに JDK 17 以降がインストールされていることを確認してください。このバージョンは、最新の Spring および Liberty 機能との互換性を保証します。

#### 必須プラグインのインストール
Spring および Spring Boot 開発用に Eclipse を強化するには、Spring ツーリングの次世代版である Spring Tool Suite (STS) をインストールします。Help -> Eclipse Marketplace からアクセスし、「Spring Tools」を検索し、「Spring Tools (aka Spring IDE and Spring Tool Suite)」と表示されたエントリをインストールします。このプラグインは、[Spring Tools](https://spring.io/tools/) で詳細が説明されており、プロジェクト作成やデバッグなどの機能のために Eclipse とシームレスに統合され、Spring ベースのアプリケーションに対する世界クラスのサポートを提供します。

IBM WebSphere Liberty との統合には、Eclipse Marketplace で「IBM Liberty Developer Tools」を検索してインストールします。このプラグインは、[IBM Liberty Developer Tools](https://marketplace.eclipse.org/content/ibm-liberty-developer-tools) で述べられているように Eclipse 2024-06 用にテストされており、2019-12 まで遡るバージョンに対応した Liberty への Java EE アプリケーションの構築とデプロイを容易にします。

#### Spring Boot プロジェクトの作成
STS がインストールされた Eclipse で Spring Boot プロジェクトを作成する主な方法は 2 つあります：

1. **Spring Initializr を使用**: [Spring Initializr](https://start.spring.io/) にアクセスし、ビルドツールとして Maven を選択し、プロジェクトメタデータ (Group、Artifact など) を選択し、Spring Web などの依存関係を追加します。プロジェクトを ZIP ファイルとして生成し、解凍して、File -> Import -> Existing Maven Project 経由で解凍したフォルダを選択して Eclipse にインポートします。

2. **STS を直接使用**: Eclipse を開き、File -> New -> Other に移動し、Spring Boot を展開して「Spring Starter Project」を選択します。ウィザードに従い、タイプとして Maven が選択されていることを確認し、依存関係を選択します。この方法は、[Creating Spring Boot Project with Eclipse and Maven](https://www.springboottutorial.com/creating-spring-boot-project-with-eclipse-and-maven) で説明されているように、Eclipse のワークスペースとの統合の点で推奨されます。

どちらの方法も、Spring Boot での依存関係管理に不可欠な Maven ベースのプロジェクトを保証します。

#### WebSphere Liberty デプロイメント用の設定
WebSphere Liberty にデプロイするには、組み込みサーバーを起動するのではなく、Spring Boot アプリケーションが Liberty の Web コンテナ上で実行されるように変更します。これには以下が含まれます：

- メインアプリケーションクラスが `SpringBootServletInitializer` を拡張していることを確認します。例：

  ```java
  @SpringBootApplication
  public class MyApplication extends SpringBootServletInitializer {
      // main メソッドなし。Liberty が起動を処理
  }
  ```

- WAR ファイルとしてパッケージ化するために pom.xml を更新し、以下を追加します：

  ```xml
  <packaging>war</packaging>
  ```

  これは、[Deploying Spring Boot Applications](https://docs.spring.io/spring-boot/docs/current/reference/html/deployment.html#deployment.servlet) で述べられているように、従来のサーブレットコンテナへのデプロイに必要です。

WebSphere Liberty、特にそのオープンソース版である Open Liberty は、特定の機能で Spring Boot アプリケーションをサポートします。Spring Boot 2.x サポートのために、Liberty サーバーの server.xml に `<feature>springBoot-2.0</feature>` が含まれていることを確認してください。詳細は [Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html) で説明されています。この設定により、組み込み Web コンテナが無効化され、代わりに Liberty のものが利用されます。

#### Eclipse での WebSphere Liberty サーバーの設定と構成
IBM Liberty Developer Tools がインストールされたら、Liberty サーバーをセットアップします：

- Window -> Preferences -> Servers -> Runtime Environments に移動し、「Add」をクリックし、「WebSphere Application Server Liberty」を選択します。ウィザードに従って、`<Liberty_Root>/wlp` のようなディレクトリにある Liberty インストール場所を指定します。これは [Liberty and Eclipse](https://www.ibm.com/cloud/blog/liberty-and-eclipse-installing-dev-environment-p9) で言及されています。

- File -> New -> Other -> Server 経由で新しいサーバーインスタンスを作成し、「WebSphere Application Server Liberty」と設定したランタイムを選択します。サーバーに名前を付け、必要に応じて設定を調整します。

- Servers ビューからアクセス可能なサーバーの server.xml を編集し、必要な機能を含めます。Spring Boot の場合、以下を追加します：

  ```xml
  <featureManager>
      <feature>springBoot-2.0</feature>
      <!-- Web サポート用の servlet-3.1 などの他の機能 -->
  </featureManager>
  ```

このセットアップは、[IBM WebSphere Liberty](https://www.ibm.com/docs/en/was-liberty/base?topic=liberty-overview) によってサポートされており、Spring Boot アプリケーションとの互換性を保証します。

#### アプリケーションのデプロイと実行
デプロイするには、Project Explorer でプロジェクトを右クリックし、「Run As -> Run on Server」を選択し、Liberty サーバーを選択して Finish をクリックします。Eclipse は WAR ファイルを Liberty サーバーにデプロイし、Console ビューでログを監視できます。アプリケーションを適切な URL (例: `http://localhost:9080/yourapp`) でアクセスできるように、アプリケーションコンテキストルートが server.xml で、通常は `<webApplication>` タグの下で正しく設定されていることを確認してください。

デバッグには、Debug パースペクティブを使用し、必要に応じてブレークポイントを設定し、[Debugging with Eclipse and Liberty](https://stackoverflow.com/questions/41428156/how-to-debug-web-service-with-eclipse-websphere-liberty) で議論されている Liberty のリモートデバッグサポートを活用します。

#### 追加の考慮事項
- **パッケージングオプション**: WAR はサーブレットコンテナの標準ですが、Open Liberty は [Configure and Deploy Spring Boot to Open Liberty](https://openliberty.io/docs/latest/deploy-spring-boot.html) で見られるように JAR デプロイメントもサポートします。JAR の場合、組み込みサーバーが起動しないようにアプリケーションが設定されていることを確認してください。これには追加の Liberty 機能や設定が必要になる場合があります。
- **Maven 統合**: 依存関係管理に Maven を使用し、自動化されたデプロイメントのために [IBM Liberty Maven Plugin](https://github.com/WASdev/ci.maven#liberty-maven-plugin) で述べられているように `liberty-maven-plugin` が含まれていることを確認します。
- **トラブルシューティング**: 問題が発生した場合は、Liberty サーバーインスタンスの下の `logs` ディレクトリにあるサーバーログを確認し、[Stack Overflow Discussion](https://stackoverflow.com/questions/36132791/how-to-use-websphere-liberty-in-spring-boot-application) によると Liberty 8.5.5.9 以降のようなバージョンが実行可能 JAR をサポートするように、Liberty バージョンと Spring Boot の互換性を確認します。

この包括的なセットアップにより、Maven をビルド管理に活用し、IBM WebSphere Liberty 上で Spring Boot アプリケーションを開発およびデプロイするための Eclipse の効果的な使用が保証されます。

#### 表: デプロイメントオプションの比較

| デプロイメントタイプ | 長所                                      | 短所                                      | 設定上の注意点                          |
|-----------------|-------------------------------------------|-------------------------------------------|----------------------------------------------|
| WAR ファイル    | サーブレットコンテナの標準、広くサポート | `SpringBootServletInitializer` の拡張が必要 | pom.xml で `<packaging>war</packaging>` を設定 |
| JAR ファイル    | 開発がより簡単、Open Liberty でサポート | 追加の Liberty 機能が必要な場合がある   | 組み込みサーバーが起動しないことを確認、springBoot 機能を使用 |

この表は、[Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html) に基づいており、プロジェクトのニーズに基づいて適切なデプロイメント戦略を選択するのに役立ちます。

### 主な引用文献
- [Creating Spring Boot Project with Eclipse and Maven, step-by-step guide](https://www.springboottutorial.com/creating-spring-boot-project-with-eclipse-and-maven)
- [IBM Liberty Developer Tools, Eclipse plugin for Java EE applications](https://marketplace.eclipse.org/content/ibm-liberty-developer-tools)
- [Open Liberty Docs, deploying Spring Boot applications](https://openliberty.io/docs/latest/deploy-spring-boot.html)
- [Spring Tools, next generation tooling for Spring development](https://spring.io/tools/)
- [Eclipse Downloads, packages for enterprise Java development](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers)
- [Liberty and Eclipse, installing development environment](https://www.ibm.com/cloud/blog/liberty-and-eclipse-installing-dev-environment-p9)
- [Deploying Spring Boot Applications, Spring Boot reference](https://docs.spring.io/spring-boot/docs/current/reference/html/deployment.html#deployment.servlet)