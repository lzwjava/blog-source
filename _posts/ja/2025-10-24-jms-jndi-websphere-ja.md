---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: WebSphereのためのJMSおよびJNDI API
translated: true
type: note
---

### JavaでのJMSに必要なパッケージとAPI

IBM WebSphere Application ServerでJMS Connection Factoryを検索して接続するためのコードスニペットを使用するには、関連するJavaパッケージをインポートする必要があります。これらはJava EE/Jakarta EEエコシステムの標準APIです：

- **JNDI (Java Naming and Directory Interface)**: `InitialContext` 検索用
  - パッケージ: `javax.naming`（新しいJakarta EEバージョンでは `jakarta.naming`）
  - 主要クラス: `InitialContext` – JNDI操作の開始点です。JNDI名（例: `"jms/MyConnectionFactory"`）でリソース（JMSファクトリやキューなど）を検索するためのコンテキストを提供します。WASのようなコンテナ内では、サーバーのネーミングサービスに自動的に接続します。

- **JMS (Java Message Service) API**: 接続、セッション、送信者/受信者、メッセージの作成用
  - パッケージ: `javax.jms`（JMS 1.1/2.0）または `jakarta.jms`（モダンEEでのJakarta JMS 3.0+）
  - 主要インターフェース: `QueueConnectionFactory`, `QueueConnection`, `QueueSession`, `QueueSender`, `Queue`, `TextMessage` など

Javaクラスの先頭でのインポート例：
```java
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.jms.QueueConnectionFactory;
import javax.jms.QueueConnection;
import javax.jms.QueueSession;
import javax.jms.Queue;
import javax.jms.QueueSender;
import javax.jms.TextMessage;
import javax.jms.JMSException;
```

**`InitialContext`とは？**  
JNDI APIのクラスで、ネーミングサービスへのエントリポイントとして機能します。コード内では：  
```java
InitialContext ctx = new InitialContext();  // アプリサーバーのJNDI環境に紐づくデフォルトコンテキストを作成
QueueConnectionFactory qcf = (QueueConnectionFactory) ctx.lookup("jms/MyConnectionFactory");  // JNDI名で事前設定されたファクトリを検索
```  
WAS*内部*で実行されるアプリの場合、コンストラクタにプロパティは不要です（コンテナが環境を注入します）。WAS*外部*のスタンドアロンクライアントの場合、プロバイダURLなどのプロパティを持つ `Hashtable` を渡す必要があります。

### Maven依存関係 (pom.xml)

Javaアプリが**WAS内部にデプロイされ実行される**場合（例：Webアプリ、EJB、エンタープライズBean）：
- **追加の依存関係は不要**。WASはJMSおよびJNDI APIをJava EEランタイムの一部として提供します。ビルド/デプロイ時にクラスパス上にあるため、それらに対してコンパイルするだけです。
- `pom.xml` では、これらを明示的に宣言し `<scope>provided</scope>` を設定してWAR/EARにバンドルされないようにします（軽量化）：
  ```xml
  <dependencies>
      <dependency>
          <groupId>javax.jms</groupId>  <!-- 新しいバージョンでは jakarta.jms -->
          <artifactId>javax.jms-api</artifactId>
          <version>2.0.1</version>  <!-- JMS 2.0, WAS 8.5+ 互換 -->
          <scope>provided</scope>
      </dependency>
      <dependency>
          <groupId>javax.naming</groupId>
          <artifactId>javax.naming-api</artifactId>
          <version>1.0</version>  <!-- JNDI 1.0, 標準 -->
          <scope>provided</scope>
      </dependency>
  </dependencies>
  ```

アプリが**スタンドアロンクライアント**の場合（WAS外部で実行、例：サーバーに接続するシンクライアント）：
- IIOP経由の完全なJMSサポートには、**WebSphere Application Client**ライブラリが必要です。IBMから「IBM WebSphere Application Server traditional」クライアントパッケージをダウンロードし、クラスパスに追加します。
- `pom.xml` には以下を含めます：
  ```xml
  <dependency>
      <groupId>com.ibm.ws</groupId>
      <artifactId>was-jms-client</artifactId>  <!-- 近似。IBMのMavenリポジトリが利用可能な場合使用 -->
      <version>9.0.5</version>  <!-- WASバージョンに合わせる -->
  </dependency>
  ```  
  または完全なシンクライアントJAR（例: `com.ibm.ws.orb_8.5.5.jar`, `com.ibm.ws.jndi_*.jar`）を使用します。正確な設定はIBMドキュメントを確認してください。

Jakarta EE移行（2020年以降）の場合、`jakarta.*` パッケージに切り替えてください。ただしWAS 9.xはデフォルトで `javax.*` を使用します。必要に応じてフィーチャーパック経由でJakartaを有効にしてください。

[IBM WebSphere JMS API Documentation](https://www.ibm.com/docs/en/was/9.0.5?topic=resources-jms-api)  
[Java EE JNDI Tutorial](https://docs.oracle.com/javase/tutorial/jndi/)