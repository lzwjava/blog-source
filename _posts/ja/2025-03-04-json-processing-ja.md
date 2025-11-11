---
audio: false
generated: true
lang: ja
layout: post
title: JavaにおけるJSON処理
translated: true
type: note
---

JavaプロジェクトでJSON処理に`com.fasterxml.jackson`パッケージを使用するには、Jacksonライブラリを活用できます。このライブラリはJavaオブジェクトとJSONの相互変換に広く使用されています。以下は、Mavenベースのプロジェクトを想定した基本的な手順です。このガイドはJSONデータバインディングの高レベル機能を提供する`jackson-databind`モジュールに焦点を当てています。

---

### 1. プロジェクトにJackson依存関係を追加する
`com.fasterxml.jackson`パッケージを使用するには、プロジェクトにJacksonライブラリを含める必要があります。Mavenを使用している場合は、`pom.xml`ファイルに以下の依存関係を追加してください：

```xml
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.12.5</version> <!-- 最新バージョンに置き換えてください -->
</dependency>
```

- **注意**: 最新バージョンは[Maven Central Repository](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind)で確認してください。2.12.5より新しい場合があります。
- `jackson-databind`モジュールは`jackson-core`と`jackson-annotations`に依存しているため、特定の要件がない限りこれらを個別に追加する必要はありません。

依存関係を追加した後、`mvn install`を実行するか、IDEでプロジェクトをリフレッシュしてライブラリをダウンロードしてください。

---

### 2. `ObjectMapper`インスタンスを作成する
`com.fasterxml.jackson.databind`パッケージの`ObjectMapper`クラスは、JSON操作の主要なツールです。これはスレッドセーフで、インスタンス化にはリソースが多く必要となるため、単一の再利用可能なインスタンスを作成するのが最適です：

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonExample {
    private static final ObjectMapper mapper = new ObjectMapper();
}
```

これをJSON操作を実行するクラスに配置してください。

---

### 3. JavaオブジェクトをJSONに変換する（シリアライゼーション）
JavaオブジェクトをJSON文字列に変換するには、`writeValueAsString`メソッドを使用します。以下は例です：

#### Javaクラスを定義する
シリアライズしたいフィールドを持つクラスを作成します。Jacksonはデフォルトでプライベートフィールドにアクセスするためにゲッターとセッターを使用するため、これらを確実に含めてください：

```java
public class MyClass {
    private String field1;
    private int field2;

    public MyClass(String field1, int field2) {
        this.field1 = field1;
        this.field2 = field2;
    }

    public String getField1() {
        return field1;
    }

    public void setField1(String field1) {
        this.field1 = field1;
    }

    public int getField2() {
        return field2;
    }

    public void setField2(int field2) {
        this.field2 = field2;
    }
}
```

#### JSONにシリアライズする
`ObjectMapper`を使用してオブジェクトをJSONに変換します：

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonExample {
    private static final ObjectMapper mapper = new ObjectMapper();

    public static void main(String[] args) throws Exception {
        MyClass obj = new MyClass("value1", 123);
        String json = mapper.writeValueAsString(obj);
        System.out.println(json);
    }
}
```

**出力**:
```json
{"field1":"value1","field2":123}
```

---

### 4. JSONをJavaオブジェクトに変換する（デシリアライゼーション）
JSON文字列をJavaオブジェクトに戻すには、`readValue`メソッドを使用します：

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonExample {
    private static final ObjectMapper mapper = new ObjectMapper();

    public static void main(String[] args) throws Exception {
        String json = "{\"field1\":\"value1\",\"field2\":123}";
        MyClass obj = mapper.readValue(json, MyClass.class);
        System.out.println(obj.getField1()); // "value1"を出力
    }
}
```

- **エラーハンドリング**: JSONが不正な形式の場合やクラス構造と一致しない場合、`readValue`メソッドは`JsonProcessingException`（チェック例外）をスローします。try-catchブロックで処理するか、メソッドシグネチャで宣言してください：

```java
try {
    MyClass obj = mapper.readValue(json, MyClass.class);
} catch (JsonProcessingException e) {
    e.printStackTrace();
}
```

---

### 5. アノテーションでJSON処理をカスタマイズする
Jacksonは、フィールドのシリアライズやデシリアライズ方法をカスタマイズするためのアノテーションを提供します。これらをクラスに追加してください（`com.fasterxml.jackson.annotation`から）：

#### フィールド名を変更する
`@JsonProperty`を使用して、Javaフィールドを異なるJSONフィールド名にマッピングします：

```java
import com.fasterxml.jackson.annotation.JsonProperty;

public class MyClass {
    @JsonProperty("name")
    private String field1;
    private int field2;
    // コンストラクタ、ゲッター、セッター
}
```

**出力**:
```json
{"name":"value1","field2":123}
```

#### フィールドを無視する
`@JsonIgnore`を使用して、フィールドをシリアライズから除外します：

```java
import com.fasterxml.jackson.annotation.JsonIgnore;

public class MyClass {
    private String field1;
    @JsonIgnore
    private int field2;
    // コンストラクタ、ゲッター、セッター
}
```

**出力**:
```json
{"field1":"value1"}
```

#### 日付をフォーマットする
`@JsonFormat`を使用して、日付のシリアライズ方法を指定します：

```java
import com.fasterxml.jackson.annotation.JsonFormat;
import java.util.Date;

public class MyClass {
    private String field1;
    @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "yyyy-MM-dd")
    private Date date;
    // コンストラクタ、ゲッター、セッター
}
```

**出力**（例）:
```json
{"field1":"value1","date":"2023-10-25"}
```

---

### 6. 高度なシナリオを扱う
以下に、役立つ可能性のある追加機能を示します：

#### JSONを整形出力する
読みやすいJSON出力には、`writerWithDefaultPrettyPrinter`を使用します：

```java
String prettyJson = mapper.writerWithDefaultPrettyPrinter().writeValueAsString(obj);
```

**出力**:
```json
{
  "field1" : "value1",
  "field2" : 123
}
```

#### 未知のプロパティを無視する
JSONにJavaクラスに存在しないフィールドが含まれている場合、`ObjectMapper`を設定して無視するようにします：

```java
mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
```

#### ファイルを扱う
ファイルへの書き込みや読み込み：

```java
// ファイルに書き込み
mapper.writeValue(new File("output.json"), obj);

// ファイルから読み込み
MyClass obj = mapper.readValue(new File("input.json"), MyClass.class);
```

#### リストやジェネリクスを扱う
コレクションの場合、`TypeReference`を使用してジェネリック型情報を保持します：

```java
import com.fasterxml.jackson.core.type.TypeReference;
import java.util.List;

List<MyClass> list = mapper.readValue(json, new TypeReference<List<MyClass>>() {});
```

---

### 7. `JsonNode`による動的JSON操作
特定のクラスにJSONをマッピングしたくない場合は、ツリーベースのアプローチとして`JsonNode`を使用します：

```java
import com.fasterxml.jackson.databind.JsonNode;

JsonNode node = mapper.readTree("{\"field1\":\"value1\",\"field2\":123}");
String value = node.get("field1").asText(); // "value1"を返す
```

動的にJSONを構築することもできます：

```java
import com.fasterxml.jackson.databind.node.ObjectNode;

ObjectNode node = mapper.createObjectNode();
node.put("field1", "value1");
node.put("field2", 123);
String json = mapper.writeValueAsString(node);
```

---

### まとめ
`com.fasterxml.jackson`パッケージを使用するには：
1. `pom.xml`に`jackson-databind`依存関係を追加します。
2. 再利用するための単一の`ObjectMapper`インスタンスを作成します。
3. JavaオブジェクトをJSONに変換するには`writeValueAsString`を、JSONをJavaオブジェクトに変換するには`readValue`を使用します。
4. `@JsonProperty`、`@JsonIgnore`、`@JsonFormat`などのアノテーションで動作をカスタマイズします。
5. 例外（例：`JsonProcessingException`）を処理し、特定のニーズ（例：未知のプロパティを無視する）に合わせて`ObjectMapper`を設定します。
6. 整形出力、ファイルI/O、動的JSON処理のための`JsonNode`などの高度な機能を探求します。

これらの手順により、Jacksonライブラリを使用してJavaアプリケーションで効果的にJSONを処理できます。