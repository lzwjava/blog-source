---
audio: false
generated: true
lang: ja
layout: post
title: Google Cloud Java クライアント
translated: true
---

### 主要ポイント
- `com.google.cloud` を Java で使用するためには、Java 開発環境を設定し、Google Cloud クライアントライブラリの依存関係を含め、認証を設定し、ライブラリを使用して Google Cloud サービスとやり取りする必要があります。
- 調査によると、認証は Google Cloud プラットフォームで自動的に処理されるか、サービスアカウントの資格情報を使用してローカル開発で手動で設定できます。
- 依存関係の管理には Maven または Gradle を使用することが推奨され、Cloud Storage が一般的な使用例として提供されています。

### 開発環境の設定
始める前に、Java Development Kit (JDK) バージョン 8 以上とビルドツールである Maven または Gradle がインストールされていることを確認してください。これらのツールはプロジェクトの依存関係とビルドプロセスを管理するのに役立ちます。

### 依存関係のインクルード
プロジェクトに Google Cloud クライアントライブラリの依存関係を追加します。Maven の場合、`pom.xml` ファイルに Bill of Materials (BOM) と特定のサービスライブラリを含めます。例えば、Cloud Storage を使用するには:

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>latest_version</version>
            <type>pom</type>
            <scope.import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
<dependencies>
    <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-storage</artifactId>
    </dependency>
</dependencies>
```

「latest_version」を [Google Cloud Java クライアントライブラリ GitHub リポジトリ](https://github.com/googleapis/google-cloud-java) から実際のバージョンに置き換えてください。

### 認証の設定
認証は、アプリケーションが Compute Engine や App Engine などの Google Cloud プラットフォーム上で実行されている場合、自動的に処理されることが多いです。ローカル開発の場合は、`GOOGLE_APPLICATION_CREDENTIALS` 環境変数をサービスアカウントの JSON キーファイルに設定するか、プログラムで設定します。

### ライブラリの使用
設定が完了したら、必要なクラスをインポートし、サービスオブジェクトを作成し、API 呼び出しを行います。例えば、Cloud Storage のバケットをリスト表示するには:

```java
import com.google.cloud.storage.*;
Storage storage = StorageOptions.getDefaultInstance().getService();
Page<Bucket> buckets = storage.list();
for (Bucket bucket : buckets.iterateAll()) {
    System.out.println(bucket.getName());
}
```

ライブラリは、各サービスごとに `com.google.cloud` のサブパッケージを持つ Google Cloud サービスをサポートしており、例えば `com.google.cloud.bigquery` は BigQuery を提供しており、ストレージを超えた機能が豊富です。

---

### 調査ノート: `com.google.cloud` を Java で使用するための包括的なガイド

このノートは、Google Cloud Java クライアントライブラリ、特に `com.google.cloud` パッケージを使用して Google Cloud サービスとやり取りする方法について詳しく説明しています。研究のすべての関連情報を含み、明確で深い理解を提供するために整理されています。

#### Google Cloud Java クライアントライブラリの紹介
Google Cloud Java クライアントライブラリは、`com.google.cloud` パッケージの下でアクセス可能であり、Cloud Storage、BigQuery、Compute Engine などの Google Cloud サービスとやり取りするための直感的で直感的なインターフェースを提供します。これらのライブラリは、ボイラープレートコードを減らし、低レベルの通信の詳細を処理し、Java 開発の慣行とシームレスに統合されるように設計されています。特に、Spring、Maven、Kubernetes などのツールを使用してクラウドネイティブアプリケーションを構築するのに役立ちます。

#### 開発環境の設定
始めるには、ライブラリと互換性がある Java Development Kit (JDK) バージョン 8 以上が必要です。推奨されるディストリビューションは、セットアップガイドで言及されている Eclipse Temurin です。また、依存関係を管理するためのビルド自動化ツールである Maven または Gradle が必要です。Google Cloud CLI (`gcloud`) もインストールして、コマンドラインからリソースとやり取りし、デプロイメントとモニタリングタスクを容易にすることができます。

#### 依存関係の管理
依存関係の管理は、Google Cloud が提供する Bill of Materials (BOM) を使用して簡素化されており、複数のライブラリ間でバージョンを管理するのに役立ちます。Maven の場合、`pom.xml` に次のように追加します:

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>latest_version</version>
            <type>pom</type>
            <scope.import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
<dependencies>
    <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-storage</artifactId>
    </dependency>
</dependencies>
```

Gradle の場合も同様の設定が適用され、バージョンの一貫性が保たれます。バージョン番号は、最新の更新を確認するために [Google Cloud Java クライアントライブラリ GitHub リポジトリ](https://github.com/googleapis/google-cloud-java) で確認してください。このリポジトリには、x86_64、Mac OS X、Windows、Linux を含むサポート対象プラットフォームが詳細に記載されていますが、Android と Raspberry Pi の制限が記載されています。

#### 認証メカニズム
認証は環境によって異なります。Compute Engine、Kubernetes Engine、App Engine などの Google Cloud プラットフォームでは、資格情報が自動的に推論されるため、プロセスが簡素化されます。他の環境では、以下の方法が利用可能です:

- **サービスアカウント（推奨）:** Google Cloud コンソールから JSON キーファイルを生成し、`GOOGLE_APPLICATION_CREDENTIALS` 環境変数をそのパスに設定します。または、プログラムで読み込みます:
  ```java
  import com.google.auth.oauth2.GoogleCredentials;
  import com.google.cloud.storage.*;
  GoogleCredentials credentials = GoogleCredentials.fromStream(new FileInputStream("path/to/key.json"));
  Storage storage = StorageOptions.newBuilder().setCredentials(credentials).build().getService();
  ```
- **ローカル開発/テスト:** Google Cloud SDK で `gcloud auth application-default login` を使用して一時的な資格情報を使用します。
- **既存の OAuth2 トークン:** 特定の使用例では、`GoogleCredentials.create(new AccessToken(accessToken, expirationTime))` を使用します。

プロジェクト ID の指定の優先順位には、サービスオプション、環境変数 `GOOGLE_CLOUD_PROJECT`、App Engine/Compute Engine、JSON 資格情報ファイル、Google Cloud SDK が含まれ、`ServiceOptions.getDefaultProjectId()` がプロジェクト ID を推論するのに役立ちます。

#### クライアントライブラリの使用
依存関係と認証が設定されると、開発者はライブラリを使用して Google Cloud サービスとやり取りできます。各サービスには `com.google.cloud` のサブパッケージがあり、例えば Cloud Storage は `com.google.cloud.storage`、BigQuery は `com.google.cloud.bigquery` です。以下に Cloud Storage の詳細な例を示します:

```java
import com.google.cloud.storage.*;
Storage storage = StorageOptions.getDefaultInstance().getService();
Page<Bucket> buckets = storage.list();
for (Bucket bucket : buckets.iterateAll()) {
    System.out.println(bucket.getName());
}
```

この例ではすべてのバケットをリスト表示しますが、ライブラリはオブジェクトのアップロード、ファイルのダウンロード、バケットポリシーの管理などの操作もサポートしています。他のサービスでも同様のパターンが適用され、詳細なメソッドはそれぞれの javadocs に記載されています。例えば、BigQuery のものは [Google Cloud Java リファレンスドキュメント](https://googleapis.dev/java/google-cloud-clients/latest/) にあります。

#### 高度な機能と考慮事項
ライブラリは、`OperationFuture` を使用して長時間実行操作 (LROs) をサポートし、タイムアウトと再試行ポリシーを設定できます。例えば、AI Platform (v3.24.0) のデフォルト設定には、初期再試行遅延が 5000ms、乗算子が 1.5、最大再試行遅延が 45000ms、合計タイムアウトが 300000ms です。プロキシ設定もサポートされており、HTTPS/gRPC 用に `https.proxyHost` と `https.proxyPort` を使用し、gRPC 用にカスタムオプションを `ProxyDetector` を使用して設定できます。

API キー認証は、一部の API で利用可能であり、gRPC または REST 用にヘッダーを手動で設定します。例えば、Language サービスの例です。テストは提供されたツールを使用して行われ、リポジトリの TESTING.md に詳細が記載されています。IntelliJ と Eclipse 用の IDE プラグインは、ライブラリの統合を通じて開発を向上させます。

#### サポート対象プラットフォームと制限
ライブラリはさまざまなプラットフォームと互換性があり、HTTP クライアントはどこでも動作し、gRPC クライアントは x86_64、Mac OS X、Windows、Linux でサポートされています。ただし、Android、Raspberry Pi、App Engine Standard Java 7 ではサポートされていません。Datastore、Storage、BigQuery を除きます。サポート対象環境には、Windows x86_64、Mac OS X x86_64、Linux x86_64、GCE、GKE、GAE Std J8、GAE Flex、Alpine Linux (Java 11+) が含まれます。

#### リソースとさらに読む
追加のガイドラインについては、[Google Cloud Java クライアントライブラリ GitHub リポジトリ](https://github.com/googleapis/google-cloud-java) にコードサンプル、貢献ガイドライン、トラブルシューティングリソースが含まれています。例えば、Cloud Storage を使用する方法についての実践的な例が含まれる [Baeldung チュートリアル](https://www.baeldung.com/java-google-cloud-storage) などのチュートリアルがあります。また、[Google Cloud for Developers](https://developers.google.com/learn/topics/cloud-java) の公式ドキュメントには、より広範なアプリケーション開発の概念が含まれています。

#### テーブル: 主要な設定詳細

| **アスペクト**               | **詳細**                                                                                     |
|--------------------------|-------------------------------------------------------------------------------------------------|
| Java バージョン             | Java 8 以上が必要です。                                                                       |
| 依存関係管理    | バージョンの一貫性を保つために BOM を使用します。例えば、Maven の `libraries-bom`。                  |
| 認証方法   | GCE/GKE/GAE で自動、`GOOGLE_APPLICATION_CREDENTIALS` またはプログラムで手動。          |
| サポート対象プラットフォーム      | HTTP クライアントはどこでも、gRPC は x86_64、Mac OS X、Windows、Linux。Android、Raspberry Pi はサポート外。|
| 例のサービス          | Cloud Storage: `com.google.cloud.storage`、バケットのリスト表示、オブジェクト管理のメソッド。       |

この包括的なガイドは、開発者が `com.google.cloud` を Java で効果的に使用するために必要なすべての情報を提供し、設定、認証、使用、高度な機能をカバーし、さらに探求するための権威あるソースへの参照を提供します。

#### 主要な引用
- [Google Cloud Java クライアントライブラリ GitHub リポジトリの詳細なコードとセットアップ](https://github.com/googleapis/google-cloud-java)
- [Java 開発概要の Google Cloud ドキュメント](https://cloud.google.com/products/anthos)
- [Google Cloud Storage を Java で使用する Baeldung チュートリアルの実践的な例](https://www.baeldung.com/java-google-cloud-storage)