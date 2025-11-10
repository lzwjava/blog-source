---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Spring SessionとJSESSIONIDとサーバー検出
translated: true
type: note
---

これを2つの部分に分けて説明します：**Spring Session/JSESSIONID** の仕組みと、Springが **Tomcat と Netty のどちらで動作しているか**を判断する方法です。

---

## 1. Spring Session と `JSESSIONID` の仕組み

* **JSESSIONID** は、サーブレットコンテナ（Tomcat、Jetty、Undertowなど）で使用される標準的なHTTPセッション識別子です。
* セッションを必要とする最初のリクエストがクライアントから送信されると、コンテナ（またはSpring Sessionを使用している場合はそれ）がランダムなセッションIDを生成し、サーバー上にセッションデータを保存し、`Set-Cookie` ヘッダーでIDをクライアントに返送します。
* クライアントはこの `JSESSIONID` クッキーを後続のリクエストに含め、サーバーが正しいセッションを見つけられるようにします。
* デフォルトでは、セッションデータは**サーブレットコンテナのメモリ内**に保存されます。例：

  * Tomcatはセッションをメモリ内に保存します（永続性を設定しない限り）。
  * **Spring Session** を使用する場合、セッションストレージは外部化（Redis、JDBC、Hazelcastなど）できますが、それでも `JSESSIONID` クッキーを使用してユーザーを識別します。
* Spring Securityやその他のSpring機能は、認証と状態管理のためにこのセッション機構に依存しています。

---

## 2. SpringがTomcatとNettyのどちらを使用しているかを知る方法

Spring Bootは、さまざまな組み込みサーバーで実行できます：

* **Tomcat** (Spring Boot starter-web のデフォルト)
* **Jetty** (依存関係を入れ替えた場合)
* **Undertow** (代替のサーブレットコンテナ)
* **Netty** (Spring WebFluxで使用され、サーブレットベースではありません)

### 確認方法:

1. **依存関係を確認する**

   * `pom.xml` または `build.gradle` に `spring-boot-starter-web` が含まれている場合、デフォルトで **Tomcat** を使用します。
   * `spring-boot-starter-webflux` が含まれている場合、デフォルトで **Netty** を使用します。

2. **起動ログを確認する**

   * アプリケーション起動時、Spring Bootは組み込みサーバーをログ出力します。
   * 例 (Tomcat):

     ```
     Tomcat started on port(s): 8080 (http)
     ```
   * 例 (Netty):

     ```
     Netty started on port(s): 8080
     ```

3. **ランタイムクラスを確認する**

   * コードまたはアクチュエーター経由で、どのサーバークラスが読み込まれているかを確認します。
   * Tomcatクラスは `org.apache.catalina.` で始まります。
   * Nettyクラスは `io.netty.` で始まります。

---

✅ **まとめ**:

* `JSESSIONID` は、サーバー側のセッションを指し示す単なるクッキーであり、Tomcat（デフォルト）またはSpring Session（Redis/DB）によって管理されます。
* Springが **Tomcat と Netty のどちらを使用しているか**は、依存関係、起動ログ、またはランタイムクラスを確認することで判断できます。

---

**Spring MVC (Tomcat) と Spring WebFlux (Netty) でのセッションハンドリングの違い**についても説明しましょうか？この区別が最も重要になる部分です。