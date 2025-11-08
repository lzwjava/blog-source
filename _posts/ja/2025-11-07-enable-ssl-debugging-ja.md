---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Java SSL TLS デバッグの有効化
translated: true
type: note
---

### JavaでのSSL/TLSデバッグの有効化

JavaでSSL/TLS関連のアクティビティ（ハンドシェイク、証明書検証、鍵交換など）の詳細なロギングを有効にするには、JVMシステムプロパティ `-Djavax.net.debug` を使用します。これにより、Javaアプリケーションの実行時にデバッグ情報がコンソール（stdout/stderr）に出力されます。

#### ステップバイステップの手順

1. **デバッグレベルの選択**:
   - 基本的なSSL/TLSハンドシェイクの詳細には `ssl` を使用します。
   - 詳細なハンドシェイクメッセージ（暗号スイートや証明書を含む）には `ssl:handshake` を使用します。
   - 包括的なデバッグ（SSLに加えて他のネットワークプロトコルを含む）には `all` を使用します（非常に冗長なので控えめに使用してください）。
   - 一般的な推奨事項：対象を絞ったSSLの情報を得るには `ssl:handshake:verbose,keymanager:trustmanager` から始めてください。

2. **Javaアプリケーション実行時のプロパティ設定**:
   - **コマンドライン実行**（例：`java` コマンド経由）:
     ```
     java -Djavax.net.debug=ssl:handshake -jar your-app.jar
     ```
     `your-app.jar` を実際のアプリケーションやクラス（例：`com.example.Main`）に置き換えてください。

   - **IDE（例：IntelliJ IDEA、Eclipse）の場合**:
     - 実行/デバッグ構成に移動します。
     - **VMオプション** フィールドに `-Djavax.net.debug=ssl:handshake` を追加します。
     - 構成を実行またはデバッグします。

   - **ビルドツール（例：Maven、Gradle）の場合**:
     - **Maven**（surefire用に `<build><plugins><plugin>` の下の `pom.xml` 内）:
       ```xml
       <configuration>
         <argLine>-Djavax.net.debug=ssl:handshake</argLine>
       </configuration>
       ```
     - **Gradle**（`build.gradle` 内）:
       ```groovy
       test {
         jvmArgs '-Djavax.net.debug=ssl:handshake'
       }
       ```

3. **ログの取得**:
   - 出力はコンソール/ターミナルに表示されます。
   - 確認を容易にするためにファイルにリダイレクトします:
     ```
     java -Djavax.net.debug=ssl:handshake -jar your-app.jar > ssl-debug.log 2>&1
     ```
   - `***` で始まる行（例：ハンドシェイク開始の `*** ClientHello`）または `javax.net.ssl` プレフィックスを探してください。

4. **無効化**:
   - 完了したら単純に `-D` フラグを削除してください。パフォーマンスのオーバーヘッドを避けるため、デフォルトでは設定されていません。

#### 出力例の一部
有効にすると、以下のような内容が表示されます:
```
*** ServerHello, TLSv1.2
RandomCookie:  GMT: 1731000000 bytes = { ... }
Cipher Suite: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
Compression Method: 0
***
```

#### ヒント
- これはJava 8以降（11、17、21を含む）で動作します。新しいバージョンでは、プロトコル固有のログのために `-Djdk.tls.client.protocols=TLSv1.2,TLSv1.3` も有効にすることができます。
- 高い冗長性はアプリケーションを遅くし、ログをあふれさせる可能性があります。開発環境でテストしてください。
- Spring Bootのようなフレームワークを使用している場合、`application.properties` に `debug=true`（一般的な場合）を追加するか、コマンドライン引数を介して追加します。

詳細については、公式Oracleドキュメントを参照してください：[Java Secure Socket Extension (JSSE) Reference Guide](https://docs.oracle.com/en/java/javase/17/docs/specs/security/standard-names.html#jsse-cipher-suite-names)。