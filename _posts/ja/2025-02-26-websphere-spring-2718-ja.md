---
audio: false
generated: false
lang: ja
layout: post
title: Spring Boot 2.7.18 in WebSphere Liberty Profile
translated: true
---

Spring Boot 2.7.18 を使用して WebSphere Liberty Profile (WLP) にアプリケーションをデプロイする場合、提供されたガイドに従って `DemoApplication` クラスや `SpringBootServletInitializer` の使用に対する変更は不要です。Spring Boot 2.7.18 は 2.7.x シリーズのパッチリリースであり、バグ修正とマイナーな改善を含むものの、標準的な WAR デプロイメントの設定に影響を与えるような破壊的な変更は含まれていません。以下に、その理由を説明し、設定が完全に互換性があることを確認します。

---

### 設定の理解
ガイドは、Spring Boot アプリケーションを WLP 上で WAR ファイルとしてデプロイするように設定します。

1. **`SpringBootServletInitializer` を拡張する:**
   - `DemoApplication` クラスは、外部のサーブレットコンテナである WLP にデプロイするために `SpringBootServletInitializer` を拡張します。このクラスは必要です。Spring Boot はデフォルトで埋め込みサーバー付きのスタンドアロン JAR として実行されるため、WLP のサーブレットコンテナと統合する必要があります。
   - `configure` メソッドは、アプリケーションのソースを指定して、外部コンテナ内でアプリケーションが正しくブートストラップされるようにオーバーライドされます。

   以下はガイドからのコードです:
   ```java
   package com.example.demo;

   import org.springframework.boot.SpringApplication;
   import org.springframework.boot.autoconfigure.SpringBootApplication;
   import org.springframework.boot.builder.SpringApplicationBuilder;
   import org.springframework.boot.web.servlet.support.SpringBootServletInitializer;

   @SpringBootApplication
   public class DemoApplication extends SpringBootServletInitializer {

       @Override
       protected SpringApplicationBuilder configure(SpringApplicationBuilder application) {
           return application.sources(DemoApplication.class);
       }

       public static void main(String[] args) {
           SpringApplication.run(DemoApplication.class, args);
       }
   }
   ```

2. **WAR ファイルとしてパッケージング:**
   - `pom.xml` は `<packaging>war</packaging>` を指定し、`spring-boot-starter-tomcat` 依存関係を `<scope>provided</scope>` にマークして、埋め込み Tomcat サーバーを排除し、代わりに WLP のサーブレットコンテナを使用します。

3. **WLP にデプロイ:**
   - WAR ファイルは、自動デプロイのために WLP の `dropins` ディレクトリに配置され、`javaee-8.0` フェーチャーは Servlet 4.0 サポートを提供し、Spring Boot の要件と互換性があります。

---

### Spring Boot 2.7.18 で変更が不要な理由
Spring Boot 2.7.18 は 2.7.x シリーズの一部であり、デプロイメントメカニズムや API に対する重大な変更は、メジャーバージョン（例：2.x から 3.x）の間で行われるものであり、マイナーまたはパッチリリースではありません。以下に詳細な分析を示します。

#### 1. `SpringBootServletInitializer` との互換性
- **目的:** `SpringBootServletInitializer` は 2.x シリーズで WAR デプロイメントを設定するための標準的な方法です。外部サーブレットコンテナと統合するために、アプリケーションコンテキストを設定するためのフックを提供します。
- **2.7.18 の安定性:** Spring Boot 2.7.18 では、`SpringBootServletInitializer` の非推奨または置き換えはありません。メジャーな変更、例えば Jakarta EE（Java EE API を置き換える）への移行は Spring Boot 3.x で行われ、Java 17 を必要とします。2.7.18 は 2.x シリーズに留まり、Java EE を使用するため、`DemoApplication` の既存の実装は有効であり変更されません。

#### 2. サーブレットコンテナの互換性
- **Spring Boot の要件:** Spring Boot 2.7.x は Servlet 3.1 以上が必要です。ガイドでは `javaee-8.0` フェーチャーを使用する WLP を使用しており、これは Servlet 4.0 というより新しい仕様を含みます。これにより完全な互換性が確保されます。
- **2.7.18 の変更なし:** パッチリリースである 2.7.18 は、サーブレットの互換性や `SpringBootServletInitializer` が WLP と相互作用する方法に影響を与える新しい要件を導入しません。

#### 3. 依存関係とパッケージングの設定
- **Tomcat を `provided` として:** ガイドは `pom.xml` で `spring-boot-starter-tomcat` を `<scope>provided</scope>` に設定して、埋め込み Tomcat を WAR ファイルから排除します。これは外部コンテナへの WAR デプロイメントの標準的な実践であり、2.7.18 でも変更されません。
- **Maven の設定:** パッケージングタイプ（`war`）と依存関係の設定は Spring Boot 2.7.x の慣例に従っており、2.7.18 に特有の更新は不要です。

#### 4. WLP デプロイメントの詳細
- **dropins ディレクトリ:** WLP の `dropins` デプロイメントメカニズムは、Spring Boot のバージョンによって影響を受けません。これは WAR ファイルの構造とサーブレット仕様に依存しており、どちらも互換性があります。
- **コンテキストルートとポート:** コンテキストルート（例：`/myapp`）とデフォルトポート（例：`9080`）は WLP と WAR ファイル名によって決定され、Spring Boot のバージョンによっては変わりません。

#### 5. 新機能または非推奨の可能性
- **リリースノートの考慮:** Spring Boot 2.7.x のリリースノート（2.7.18 を含む）は、依存関係の更新、セキュリティ修正、マイナーな改善をカバーするものの、WAR デプロイメントや `SpringBootServletInitializer` に影響を与えるものはありません。例えば、2.7.18 では既存のアプローチを置き換えるための新しいアノテーションや設定メソッドは導入されていません。
- **3.x との対比:** 対照的に、Spring Boot 3.x は Jakarta EE を採用し、調整が必要になるかもしれません（例：異なるベースクラスや更新されたサーブレット API）。しかし、2.7.18 はその変更に橋渡しをするものではありません。

---

### 結論
Spring Boot 2.7.18 の場合、`DemoApplication` クラスとガイドに示されている `SpringBootServletInitializer` の使用には修正が不要です。設定は以下と完全に互換性があります。

- WAR パッケージングと WLP へのデプロイメント。
- WLP の `javaee-8.0` フェーチャー（Servlet 4.0）。
- Spring Boot 2.7.x のサーブレットとデプロイメントの要件。

ガイドの正確な手順とコードを使用し、Spring Boot 2.7.18 を一般的な 2.7.x バージョンの代わりに使用して、アプリケーションが WLP 上で正常にデプロイされ、実行され、`http://localhost:9080/myapp/` で "Hello World!" を返すことを期待できます。追加の設定、プロパティの変更、コードの調整は必要ありません。