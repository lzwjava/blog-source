---
audio: false
lang: ja
layout: post
title: Eclipseを使用する
translated: true
---

### 主要ポイント
- EclipseをIBM Websphere Liberty、Spring、Spring Boot、Mavenと効果的に使用することが可能であると考えられますが、設定には特定の構成が必要です。
- 研究によると、EclipseにSpring Tool Suite (STS)とIBM Liberty Developer Toolsをプラグインとしてインストールすることで、機能が向上します。
- 証拠は、STSまたはSpring Initializrを使用してSpring Bootプロジェクトを作成し、その後Websphere Libertyへのデプロイメントに設定することを示唆しています。

### Eclipseの設定
まず、[Eclipse Downloads](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers)から「Eclipse IDE for Enterprise Java and Web Developers」をダウンロードしてインストールします。JDK 17またはそれ以降がインストールされていることを確認し、ターミナルで`java -version`を実行して確認します。

### SpringとSpring Bootの設定
Eclipseの「Help -> Eclipse Marketplace」に移動し、「Spring Tools」を検索して適切なバージョンをインストールします。これにより、SpringとSpring Bootの開発が向上します。Eclipseで「File -> New -> Spring Starter Project」を選択して新しいSpring Bootプロジェクトを直接作成し、Mavenをビルドツールとして選択し、Spring Webなどの必要な依存関係を追加します。

### IBM Websphere Libertyとの統合
Eclipse Marketplaceから「IBM Liberty Developer Tools」を検索してインストールプロンプトに従ってインストールします。「Window -> Preferences -> Servers -> Runtime Environments」に移動し、新しいWebsphere Libertyランタイムを追加し、「File -> New -> Other -> Server」を選択してサーバーインスタンスを作成します。サーバーのserver.xmlに`<feature>springBoot-2.0</feature>`を含めることで、Spring Bootのサポートが提供されます。詳細については、[Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html)を参照してください。

### アプリケーションのデプロイ
Spring Bootアプリケーションを`SpringBootServletInitializer`を拡張するように修正し、pom.xmlで`<packaging>war</packaging>`を設定してWARファイルとしてパッケージングします。プロジェクトを右クリックし、「Run As -> Run on Server」を選択し、Libertyサーバーを選択してデプロイします。これにより、アプリケーションがLibertyのWebコンテナ上で実行されます。

---

### アンケートノート: Eclipseを使用してIBM Websphere Liberty、Spring、Spring Boot、Mavenを使用する包括的なガイド

このガイドは、IBM Websphere Liberty、Spring、Spring Boot、Mavenを使用する開発者向けに、Eclipseを効果的に使用するための詳細な手順を提供します。このプロセスには、Eclipseの設定、必要なプラグインのインストール、プロジェクトの作成と設定、アプリケーションのデプロイが含まれ、2025年2月27日現在の統合とベストプラクティスに焦点を当てています。

#### Eclipseの設定と前提条件
Eclipseは、特にエンタープライズアプリケーション向けのJava開発用の強力なIDEです。この設定には、[Eclipse Downloads](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers)で入手できる「Eclipse IDE for Enterprise Java and Web Developers」バージョン2024-06をダウンロードします。ターミナルで`java -version`を実行して、システムにJDK 17またはそれ以降がインストールされていることを確認します。このバージョンは、最新のSpringとLiberty機能との互換性を確保します。

#### 必要なプラグインのインストール
SpringとSpring Bootの開発を強化するために、Spring Tool Suite (STS)をインストールします。Eclipseの「Help -> Eclipse Marketplace」にアクセスし、「Spring Tools」を検索して「Spring Tools (aka Spring IDE and Spring Tool Suite)」とラベル付けされたエントリをインストールします。このプラグインは、[Spring Tools](https://spring.io/tools/)で詳細が記載されており、Springベースのアプリケーションに対する世界的なサポートを提供し、Eclipseとシームレスに統合されています。

IBM Websphere Libertyの統合には、Eclipse Marketplaceから「IBM Liberty Developer Tools」を検索してインストールします。このプラグインは、[IBM Liberty Developer Tools](https://marketplace.eclipse.org/content/ibm-liberty-developer-tools)でEclipse 2024-06のテストが記載されており、Java EEアプリケーションをLibertyに構築およびデプロイするのに役立ちます。

#### Spring Bootプロジェクトの作成
EclipseにSTSがインストールされている場合、Spring Bootプロジェクトを作成する2つの主要な方法があります。

1. **Spring Initializrの使用**: [Spring Initializr](https://start.spring.io/)にアクセスし、Mavenをビルドツールとして選択し、プロジェクトのメタデータ（グループ、アーティファクトなど）を選択し、Spring Webなどの依存関係を追加します。プロジェクトをZIPファイルとして生成し、解凍してEclipseにインポートします。インポート方法は「File -> Import -> Existing Maven Project」を選択し、解凍したフォルダを選択します。

2. **STSの直接使用**: Eclipseを開き、「File -> New -> Other」に移動し、Spring Bootを展開して「Spring Starter Project」を選択します。ウィザードに従い、Mavenをタイプとして選択し、依存関係を選択します。この方法は、[Creating Spring Boot Project with Eclipse and Maven](https://www.springboottutorial.com/creating-spring-boot-project-with-eclipse-and-maven)で説明されており、Eclipseのワークスペースとの統合が優れています。

両方の方法は、Spring Bootの依存関係管理に重要なMavenベースのプロジェクトを確保します。

#### Websphere Libertyへのデプロイメント設定
Websphere Libertyにデプロイするには、Spring BootアプリケーションをLibertyのWebコンテナで実行するように設定する必要があります。これにより、埋め込みサーバーを起動するメインメソッドを使用するのではなく、Libertyが起動を処理します。具体的には、以下のようにします。

- メインアプリケーションクラスが`SpringBootServletInitializer`を拡張するようにします。例えば:

  ```java
  @SpringBootApplication
  public class MyApplication extends SpringBootServletInitializer {
      // メインメソッドはありません; Libertyが起動を処理します
  }
  ```

- pom.xmlを更新してWARファイルとしてパッケージングするようにします。以下のように追加します:

  ```xml
  <packaging>war</packaging>
  ```

  これは、[Deploying Spring Boot Applications](https://docs.spring.io/spring-boot/docs/current/reference/html/deployment.html#deployment.servlet)で説明されているように、伝統的なサーブレットコンテナへのデプロイメントに必要です。

Websphere Liberty、特にそのオープンソースバリエントOpen Libertyは、特定の機能を使用してSpring Bootアプリケーションをサポートします。Libertyサーバーのserver.xmlに`<feature>springBoot-2.0</feature>`を含めることで、Spring Boot 2.xのサポートが提供されます。詳細については、[Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html)を参照してください。この設定により、埋め込みWebコンテナが無効になり、代わりにLibertyのものが使用されます。

#### EclipseでWebsphere Libertyサーバーの設定と構成
IBM Liberty Developer Toolsをインストールした後、Libertyサーバーを設定します。

- 「Window -> Preferences -> Servers -> Runtime Environments」に移動し、「Add」をクリックして「WebSphere Application Server Liberty」を選択します。ウィザードに従ってLibertyのインストール先を指定します。通常は`<Liberty_Root>/wlp`のようなディレクトリにあります。詳細については、[Liberty and Eclipse](https://www.ibm.com/cloud/blog/liberty-and-eclipse-installing-dev-environment-p9)を参照してください。

- 「File -> New -> Other -> Server」を選択し、「WebSphere Application Server Liberty」と設定したランタイムを選択して新しいサーバーインスタンスを作成します。サーバーに名前を付け、必要に応じて設定を調整します。

- サーバーのserver.xmlを編集し、必要な機能を追加します。Spring Bootの場合、以下のように追加します:

  ```xml
  <featureManager>
      <feature>springBoot-2.0</feature>
      <!-- 他の機能、例えばwebサポートのためのservlet-3.1 -->
  </featureManager>
  ```

この設定は、[IBM WebSphere Liberty](https://www.ibm.com/docs/en/was-liberty/base?topic=liberty-overview)でサポートされており、Spring Bootアプリケーションとの互換性を確保します。

#### アプリケーションのデプロイと実行
デプロイするには、プロジェクトエクスプローラーでプロジェクトを右クリックし、「Run As -> Run on Server」を選択し、Libertyサーバーを選択して「Finish」をクリックします。EclipseはWARファイルをLibertyサーバーにデプロイし、コンソールビューでログを監視できます。server.xmlでアプリケーションコンテキストルートが正しく設定されていることを確認し、適切なURL（例: `http://localhost:9080/yourapp`）でアプリケーションにアクセスできます。

デバッグには、デバッグペルスペクティブを使用し、必要に応じてブレークポイントを設定します。Libertyのリモートデバッグサポートを活用して、[Debugging with Eclipse and Liberty](https://stackoverflow.com/questions/41428156/how-to-debug-web-service-with-eclipse-websphere-liberty)で説明されているようにデバッグします。

#### 追加の考慮事項
- **パッケージングオプション**: WARはサーブレットコンテナの標準ですが、Open LibertyもJARデプロイメントをサポートしています。詳細については、[Configure and Deploy Spring Boot to Open Liberty](https://openliberty.io/docs/latest/deploy-spring-boot.html)を参照してください。JARの場合、埋め込みサーバーが起動しないようにアプリケーションを設定する必要があり、これは追加のLiberty機能または設定が必要になる場合があります。
- **Mavenの統合**: Mavenを依存関係管理に使用し、`liberty-maven-plugin`を含めることで、[IBM Liberty Maven Plugin](https://github.com/WASdev/ci.maven#liberty-maven-plugin)で説明されているように自動デプロイが可能です。
- **トラブルシューティング**: 問題が発生した場合は、Libertyサーバーインスタンスの`logs`ディレクトリにあるサーバーログを確認し、LibertyバージョンとSpring Bootの互換性を確認します。バージョン8.5.5.9以降のLibertyは、[Stack Overflow Discussion](https://stackoverflow.com/questions/36132791/how-to-use-websphere-liberty-in-spring-boot-application)で説明されているように、実行可能なJARをサポートします。

この包括的な設定により、Eclipseを使用してIBM Websphere Liberty上でSpring Bootアプリケーションを開発およびデプロイすることができ、Mavenをビルド管理に使用します。

#### 表: デプロイメントオプションの比較

| デプロイメントタイプ | 利点                                      | 欠点                                      | 構成ノート                          |
|-----------------|-------------------------------------------|-------------------------------------------|----------------------------------------------|
| WARファイル        | サーブレットコンテナの標準、広くサポートされている | `SpringBootServletInitializer`を拡張する必要がある | pom.xmlで`<packaging>war</packaging>`を設定  |
| JARファイル        | 開発が簡単、Open Libertyでサポートされている | 追加のLiberty機能が必要になる場合がある   | 埋め込みサーバーが起動しないように設定、springBoot機能を使用 |

この表は、[Open Liberty Docs](https://openliberty.io/docs/latest/deploy-spring-boot.html)に基づいており、プロジェクトのニーズに応じた適切なデプロイメント戦略を選択するのに役立ちます。

### 主要な引用
- [Creating Spring Boot Project with Eclipse and Maven, 手順別ガイド](https://www.springboottutorial.com/creating-spring-boot-project-with-eclipse-and-maven)
- [IBM Liberty Developer Tools, Java EEアプリケーション用Eclipseプラグイン](https://marketplace.eclipse.org/content/ibm-liberty-developer-tools)
- [Open Liberty Docs, Spring Bootアプリケーションのデプロイ](https://openliberty.io/docs/latest/deploy-spring-boot.html)
- [Spring Tools, Spring開発用の次世代ツール](https://spring.io/tools/)
- [Eclipse Downloads, エンタープライズJava開発用パッケージ](https://www.eclipse.org/downloads/packages/release/2024-06/r/eclipse-ide-enterprise-java-and-web-developers)
- [Liberty and Eclipse, 開発環境のインストール](https://www.ibm.com/cloud/blog/liberty-and-eclipse-installing-dev-environment-p9)
- [Deploying Spring Boot Applications, Spring Bootリファレンス](https://docs.spring.io/spring-boot/docs/current/reference/html/deployment.html#deployment.servlet)