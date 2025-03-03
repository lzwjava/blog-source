---
audio: false
generated: true
lang: ja
layout: post
title: JDBC URLの構築
translated: true
---

WebSphere Liberty Profileの`server.xml`ファイル内の`properties.db2.jcc`要素に基づいてDB2データベースに接続するためのJDBC URLを構築するには、特定のキー属性（`databaseName`、`serverName`、`portNumber`など）に提供される値を使用する必要があります。以下にその方法を示します。

### DB2の基本的なJDBC URL形式
DB2 JDBC Type 4ドライバー（Liberty Profileセットアップで一般的に使用される）を使用したJDBC URLの標準形式は以下の通りです：

```
jdbc:db2://<serverName>:<portNumber>/<databaseName>
```

- **`jdbc:db2://`** - これは、Type 4ドライバーを使用してDB2データベースに直接ネットワーク接続を示すプロトコル識別子です。
- **`<serverName>`** - `properties.db2.jcc`の`serverName`属性で指定されたDB2サーバーのホスト名またはIPアドレスです。
- **`<portNumber>`** - DB2インスタンスがリッスンしているポートで、`portNumber`属性で指定されます（指定されていない場合、デフォルトは通常`50000`です）。
- **`<databaseName>`** - 接続するデータベースの名前で、`databaseName`属性で指定されます。

### URLの構築手順
1. **必要なプロパティを特定する**: `server.xml`の`properties.db2.jcc`要素から、`serverName`、`portNumber`、`databaseName`の値を抽出します。これらがURLに必要な基本的なコンポーネントです。
2. **URLを組み立てる**: これらの値を上記の形式に組み合わせ、適切な区切り記号（サーバーとポートの間に`:`、データベース名の前に`/`）を確認します。
3. **追加のプロパティを処理する（必要に応じて）**: `properties.db2.jcc`に他の属性（例：`currentSchema`、`sslConnection`）が含まれている場合、これらをURLに追加することができますが、その性質によって異なります。通常、`user`や`password`のようなプロパティは、セキュリティ上の理由から接続を確立する際にURLではなく別途提供されます。

### 例
`server.xml`に以下の`properties.db2.jcc`構成が含まれているとします：

```xml
<properties.db2.jcc databaseName="SAMPLE" serverName="localhost" portNumber="50000" user="dbuser" password="dbpass"/>
```

- `serverName="localhost"`
- `portNumber="50000"`
- `databaseName="SAMPLE"`

JDBC URLは以下のようになります：

```
jdbc:db2://localhost:50000/SAMPLE
```

- `user`と`password`はURLに含まれません。これらは通常、JDBCドライバーを通じて接続を取得する際に別途提供されます（例：`DataSource`または`DriverManager`を通じて）。

### 追加のプロパティを含める（オプション）
`properties.db2.jcc`に`currentSchema`や`sslConnection`のような追加のプロパティが指定されている場合、これらをURLに含めることができます（ただし、一部は接続プロパティとして設定する方が良い場合があります）。データベース名の後にコロン（`:`）とセミコロン区切りの`property=value`ペアを追加します。例えば：

```xml
<properties.db2.jcc databaseName="SAMPLE" serverName="localhost" portNumber="50000" currentSchema="MYSCHEMA" sslConnection="true"/>
```

URLは以下のようになります：

```
jdbc:db2://localhost:50000/SAMPLE:currentSchema=MYSCHEMA;sslConnection=true;
```

ただし：
- `sslConnection=true`のようなプロパティは、URLではなく`Properties`オブジェクトやデータソース構成で設定されることが多いです。
- DB2 JDBCドライバーのドキュメントを確認して、URLで有効なプロパティと接続設定で設定する必要があるプロパティを確認してください。

### 最終的な回答
あなたの質問の文脈では、`properties.db2.jcc`が少なくとも`databaseName`、`serverName`、`portNumber`を提供していると仮定すると、JDBC URLは以下のように構築されます：

```
jdbc:db2://<serverName>:<portNumber>/<databaseName>
```

`<serverName>`、`<portNumber>`、`<databaseName>`を実際の`properties.db2.jcc`構成からの値に置き換えます。追加のプロパティが存在し、URLに含めることを意図している場合は、`:property1=value1;property2=value2;`の形式で追加しますが、通常、`user`、`password`、`sslConnection`のようなプロパティは接続設定で別途処理されます。