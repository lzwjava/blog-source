---
audio: false
generated: true
lang: ja
layout: post
title: JDBC URLの構築
translated: true
type: note
---

WebSphere Liberty Profileの`server.xml`ファイル内の`properties.db2.jcc`要素に基づいてDB2データベースに接続するためのJDBC URLを構築するには、`databaseName`、`serverName`、`portNumber`などの特定のキー属性に指定された値を使用する必要があります。以下にその方法を説明します。

### DB2の基本的なJDBC URL形式
DB2 JDBC Type 4ドライバ（Liberty Profileのセットアップで一般的に使用される）を使用したJDBC URLの標準形式は次のとおりです。

```
jdbc:db2://<serverName>:<portNumber>/<databaseName>
```

- **`jdbc:db2://`** - これはType 4ドライバを使用するDB2データベースのプロトコル識別子で、直接ネットワーク接続を示します。
- **`<serverName>`** - DB2サーバーのホスト名またはIPアドレス。`properties.db2.jcc`の`serverName`属性で指定されます。
- **`<portNumber>`** - DB2インスタンスがリッスンしているポート。`portNumber`属性で指定されます（指定がない場合、デフォルトは通常`50000`）。
- **`<databaseName>`** - 接続するデータベースの名前。`databaseName`属性で指定されます。

### URL構築の手順
1. **必要なプロパティの特定**: `server.xml`の`properties.db2.jcc`要素から、`serverName`、`portNumber`、`databaseName`の値を抽出します。これらはURLに必要な必須コンポーネントです。
2. **URLの組み立て**: これらの値を上記の形式に組み合わせ、適切な区切り文字（サーバーとポートの間は`:`、データベース名の前は`/`）を確実に使用します。
3. **追加プロパティの処理（存在する場合）**: `properties.db2.jcc`に他の属性（例: `currentSchema`、`sslConnection`）が含まれている場合、それらをURLに追加できることがありますが、これはその性質によります。通常、`user`や`password`などのプロパティは、セキュリティ上の理由からURLには含めず、接続確立時に個別に渡されます。

### 例
`server.xml`に以下の`properties.db2.jcc`設定が含まれているとします。

```xml
<properties.db2.jcc databaseName="SAMPLE" serverName="localhost" portNumber="50000" user="dbuser" password="dbpass"/>
```

- `serverName="localhost"`
- `portNumber="50000"`
- `databaseName="SAMPLE"`

JDBC URLは次のようになります。

```
jdbc:db2://localhost:50000/SAMPLE
```

- `user`と`password`はURLに含まれません。これらは通常、JDBCドライバを介して接続を取得する際に（`DataSource`や`DriverManager`を介して）個別に提供されます。

### 追加プロパティの包含（オプション）
`currentSchema`や`sslConnection`などの追加プロパティが`properties.db2.jcc`で指定されており、それらをURLに含めたい場合（ただし、一部のプロパティは接続プロパティで設定する方が適切な場合があります）、データベース名の後にコロン（`:`）と続けて、セミコロン区切りの`property=value`ペアを追加します。例えば：

```xml
<properties.db2.jcc databaseName="SAMPLE" serverName="localhost" portNumber="50000" currentSchema="MYSCHEMA" sslConnection="true"/>
```

URLは次のようになる可能性があります。

```
jdbc:db2://localhost:50000/SAMPLE:currentSchema=MYSCHEMA;sslConnection=true;
```

ただし：
- `sslConnection=true`のようなプロパティは、多くの場合、URLではなく`Properties`オブジェクトまたはデータソース設定で設定されます。
- どのプロパティがURLで有効で、どれが個別の設定を必要とするかは、DB2 JDBCドライバのドキュメントを確認してください。

### 最終的な回答
お問い合わせの文脈において、`properties.db2.jcc`が少なくとも`databaseName`、`serverName`、`portNumber`を提供していると仮定すると、JDBC URLは次のように構築されます。

```
jdbc:db2://<serverName>:<portNumber>/<databaseName>
```

`<serverName>`、`<portNumber>`、`<databaseName>`を`properties.db2.jcc`設定からの実際の値に置き換えてください。追加プロパティが存在し、URLに含めることを意図している場合は、`:property1=value1;property2=value2;`として追加しますが、通常、`user`、`password`、`sslConnection`などのプロパティは接続設定で個別に処理されます。