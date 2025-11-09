---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: WARとEARパッケージングの比較
translated: true
type: note
---

### 概要
Java EE（現在のJakarta EE）において、WAR（Web Archive）とEAR（Enterprise Archive）は、Tomcat、WildFly、GlassFishなどのアプリケーションサーバーにアプリケーションをデプロイするための標準的なパッケージング形式です。WARはWeb層コンポーネントに焦点を当て、EARは完全なエンタープライズアプリケーション向けに複数のモジュールをバンドルします。以下に詳細な比較を示します。

| 観点              | WAR (Web Archive)                                                                 | EAR (Enterprise Archive)                                                                 |
|---------------------|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **目的**        | Webアプリケーション（サーブレット、JSP、静的コンテンツなど）を単一ユニットとしてデプロイし、Web層の機能を提供する。 | 複数のサブモジュール（WAR、EJB JARなど）をパッケージ化し、多層分散システム向けのエンタープライズアプリケーションをデプロイする。 |
| **内容**       | - Webアプリケーションファイル: JSP、HTML/CSS/JS、サーブレット。<br>- ライブラリ: WEB-INF/lib内のJARファイル。<br>- デプロイメント記述子: web.xml（現代のバージョンでは任意）。 | - 複数モジュール: WAR、EJB JAR、クライアントJAR。<br>- 共有ライブラリ。<br>- デプロイメント記述子: application.xml。<br>- リソースアダプタ用のRAR（任意）。 |
| **構造**      | - ルート: 静的リソース（例: index.html）。<br>- WEB-INF/: classes、lib、web.xml。 | - ルート: META-INF/application.xml。<br>- 各モジュール用のサブディレクトリ（例: myapp.war、myejb.jar）。 |
| **ファイル拡張子** | .war                                                                             | .ear                                                                                     |
| **デプロイメント範囲**| 単一モジュール。Webコンテナ（Tomcatなど）または完全なアプリケーションサーバーにデプロイ可能。     | 複数モジュール。トランザクションなどのエンタープライズ機能をサポートする完全なアプリケーションサーバー（JBoss、WebLogicなど）にのみデプロイ可能。 |
| **サイズと複雑さ** | 小さくシンプル。スタンドアロンのWebアプリケーションに最適。                              | 大きく複雑。モジュール性とモジュール間の共有リソースをサポート。        |
| **ユースケース**      | Webポータル、REST API、シンプルなサービス（Spring BootのWebアプリをWARとしてパッケージ化した例など）。 | 複雑なエンタープライズシステム（Web UI＋ビジネスロジック＋データアクセスを備えた銀行アプリなど）。 |
| **依存関係**   | Webサービスにおいてコンテナに依存。EJBサポートは組み込まれていない。                    | EJB、JMS、モジュール間の依存関係をサポート。疎結合を促進。              |

### 主な違いのまとめ
- **モジュール性**: WARはWeb層向けのモノリシックな構造。EARは複数のWAR/JARを組み合わせることを可能にする。
- **サーバー要件**: WARは軽量なWebサーバーで動作。EARは完全なJEEサーバーを必要とする。
- **進化**: マイクロサービスやクラウドネイティブの潮流（Spring Boot、Quarkusなど）において、WARはコンテナ化デプロイ（Docker）でよく利用され、EARはレガシーなエンタープライズアプリケーションで依然として重要である。

実践的な例については、公式のJakarta EEドキュメント [Jakarta EE Tutorial](https://jakartaee.github.io/tutorial/) またはOracleのJava EEアーカイブ [Java EE Packaging](https://docs.oracle.com/javaee/7/tutorial/packaging.htm) を参照してください。