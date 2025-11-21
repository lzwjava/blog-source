---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4.1-fast
title: WebSphereとSpring Bootのリクエストフィルタ比較
translated: true
type: note
---

### 概要
IBM WebSphere Application Server（WAS、従来型またはLiberty）とSpring Bootはどちらも、標準のJava Servlet APIの `javax.servlet.Filter` と `FilterChain` に基づく **リクエスト処理チェーン** の概念をサポートしています。これは、受信HTTPリクエストがサーブレット（またはコントローラ/ハンドラ）に到達する前に一連のフィルタを通過し、レスポンスも戻り経路で変更できる仕組みです。

- フィルタは、リクエスト/レスポンスの事前処理（例：認証、ロギング、圧縮）と事後処理を可能にします。
- コアメカニズム — `Filter` を実装し、処理を継続するために `chain.doFilter(request, response)` を呼び出す — は、両者がServletコンテナで実行されるため **同一です**（WASは独自の完全なJava EE Webコンテナを持ち、Spring BootはデフォルトでTomcat/Jetty/Undertowを組み込みます）。

基本的な「リクエストチェーンフィルタ」の動作方法に根本的な違いはありません。しかし、各プラットフォームのアーキテクチャにより、フィルタの設定、順序付け、統合の方法が大きく異なります。

### 主な比較

| 観点                      | IBM WebSphere Application Server (従来型/Liberty)                                                                 | Spring Boot                                                                                                                               |
|---------------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| **基盤となるメカニズム**    | 標準Servletフィルタ (`javax.servlet.Filter`)。WASは、一部のシナリオ（ポータルやカスタムIBM APIなど）での内部リクエスト転送/チェーニングのために、`ChainedRequest`/`ChainedResponse` のような独自の拡張機能も持ちます。 | 標準Servletフィルタ。Spring Bootは `@Component` が付いたFilter Beanを自動登録するか、`FilterRegistrationBean` を介して明示的に登録します。                                                              |
| **設定**                  | 主に `web.xml`（宣言的）またはプログラムによる登録を介して行います。グローバルフィルタ（すべてのアプリケーションに跨る）の場合：複雑 — 共有ライブラリ、カスタムリスナー、またはIBM固有の拡張機能が必要です（Tomcatのような単純なサーバー全体のweb.xmlはありません）。 | 設定より規約: `@Component` + `@Order` でアノテーションを付けると自動登録されます。または、細かい制御（URLパターン、ディスパッチャタイプ）のために `FilterRegistrationBean` を使用します。非常に開発者フレンドリーです。 |
| **順序付け**              | `web.xml` での順序、またはプログラムによる場合は `@Order` を介して定義されます。グローバルな順序付けは困難です。                                                              | `@Order(n)`（数値が小さいほど先）または `Ordered` インターフェースで簡単に行えます。Spring Bootがチェーンを自動的に管理します。                                                              |
| **セキュリティフィルタチェーン** | 標準ServletフィルタまたはIBM固有のセキュリティ（TAI、JEEロールなど）を使用します。Spring Securityのような組み込みのセキュリティチェーンはありません。                                      | Spring Securityは、15以上の順序付けられたフィルタ（CSRF、認証、セッション管理など）を含む強力な `SecurityFilterChain`（`FilterChainProxy` 経由）を提供します。パスごとに複数のチェーンを持つ高度なカスタマイズが可能です。 |
| **カスタムフィルタ追加の容易さ** | より冗長、特にグローバル/アプリケーション横断的なフィルタの場合。多くの場合、管理者コンソールの調整や共有ライブラリが必要です。                                                              | 非常に簡単 — `@Component` Beanまたは設定クラスを定義するだけです。組み込みコンテナに自動統合されます。                                                                      |
| **デプロイメントモデル**    | 従来型の完全なJava EEサーバー。アプリはWAR/EARとしてデプロイされます。強力なエンタープライズ機能（クラスタリング、トランザクション、JMS）をサポートします。                                          | 組み込みコンテナ（デフォルトはスタンドアロン実行可能JAR）。外部サーバー（WASを含む）にWARとしてデプロイ可能です。軽量/マイクロサービス指向です。                                                              |
| **パフォーマンス/オーバーヘッド** | オーバーヘッドが高い（完全なアプリケーションサーバー）。トランスポートチェーン、Webコンテナチャネルがレイヤーを追加します。                                                                  | オーバーヘッドが低い（組み込みの軽量コンテナ）。起動が速く、リソース使用量が少ないです。                                                                                  |
| **フィルタ実行タイミング**   | WAS Webコンテナのインバウンドチェーン内で実行されます。サーバーレベルのトランスポートフィルタ（TCPチャネルでのIPフィルタリングなど）を持つことができます。                                            | 組み込みコンテナのフィルタチェーン内で実行されます。Spring Bootは独自のフィルタ（エラーハンドリング、文字エンコーディングなど）を追加します。                                                              |
| **一般的な使用例**         | エンタープライズモノリス、ポータル、グローバルなセキュリティ/ロギングを必要とするレガシーJava EEアプリケーション。                                                                  | モダンなマイクロサービス、REST API、Spring Securityを使用した迅速な開発。                                                                                             |

### 実践的な例

**標準的なカスタムフィルタ（同じコードが両方で動作）:**
```java
@Component  // Spring Bootのみで有効。WASではweb.xmlで宣言
@Order(1)
public class LoggingFilter implements Filter {
    public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain)
            throws IOException, ServletException {
        System.out.println("Request: " + ((HttpServletRequest) req).getRequestURI());
        chain.doFilter(req, res);  // 重要: 次のフィルタ/サーブレットに渡す
    }
    // init/destroy...
}
```

**Spring Bootの場合（自動登録）:**
上記のクラスに `@Component` を付けるだけです。

**WASの場合:**
`web.xml` に追加:
```xml
<filter>
    <filter-name>LoggingFilter</filter-name>
    <filter-class>com.example.LoggingFilter</filter-class>
</filter>
<filter-mapping>
    <filter-name>LoggingFilter</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
```

### どちらを選ぶべきか
- **WASフィルタを使用する** のは、レガシーなIBM環境にある場合、完全なJava EE機能が必要な場合、またはコード変更なしで多くのアプリケーションにグローバルにフィルタを適用する必要がある場合です。
- **Spring Bootフィルタ**（特にSpring Securityと共に）を使用するのは、新規/グリーンフィールドのプロジェクト、マイクロサービス、迅速な反復開発、または複数のセキュリティチェーンと簡単な順序付けが必要な場合です。

要約すると、**リクエストチェーンフィルタの概念は同じ**（Servlet仕様）ですが、**Spring Bootはほとんどのモダンなユースケースに対してはるかにシンプルで強力**であり、WASはよりエンタープライズ向けで設定が複雑です。

[IBM WAS Servletフィルタリング ドキュメント](https://www.ibm.com/docs/en/was/9.0.5?topic=extensions-servlet-filtering)  
[Spring Boot カスタムフィルタ](https://www.baeldung.com/spring-boot-add-filter)  
[Spring Security フィルタチェーン](https://docs.spring.io/spring-security/reference/servlet/architecture.html)