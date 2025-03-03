---
audio: false
generated: true
lang: ja
layout: post
title: JSON処理のJava
translated: true
---

`com.fasterxml.jackson` パッケージをJavaプロジェクトでJSON処理に使用するには、Jacksonライブラリを活用することができます。Jacksonライブラリは、JavaオブジェクトをJSONに変換し、その逆も行うために広く使用されています。以下は、Mavenベースのプロジェクトを使用していることを前提とした、Jacksonライブラリを使用するためのステップバイステップのガイドです。このガイドは、`jackson-databind` モジュールに焦点を当てており、JSONデータバインディングのための高水準の機能を提供します。

---

### 1. プロジェクトにJacksonの依存関係を追加する
`com.fasterxml.jackson` パッケージを使用するには、プロジェクトにJacksonライブラリを含める必要があります。Mavenを使用している場合は、`pom.xml` ファイルに以下の依存関係を追加します：

```xml
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.12.5</version> <!-- 最新バージョンに置き換えてください -->
</dependency>
```

- **注意**: [Maven Central Repository](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind) で最新バージョンを確認してください。2.12.5より新しいバージョンがあるかもしれません。
- `jackson-databind` モジュールは、`jackson-core` と `jackson-annotations` に依存しているため、特定の要件がない限り、これらを別に追加する必要はありません。

依存関係を追加した後、`mvn install` を実行するか、IDEでプロジェクトを更新してライブラリをダウンロードします。

---

### 2. `ObjectMapper` インスタンスを作成する
`com.fasterxml.jackson.databind` パッケージの `ObjectMapper` クラスは、JSON操作の主要なツールです。スレッドセーフであり、リソース集約的なインスタンス化であるため、再利用可能な単一のインスタンスを作成するのが最適です：

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonExample {
    private static final ObjectMapper mapper = new ObjectMapper();
}
```

JSON操作を行うクラスにこれを配置します。

---

### 3. JavaオブジェクトをJSONに変換する（シリアライズ）
JavaオブジェクトをJSON文字列に変換するには、`writeValueAsString` メソッドを使用します。以下に例を示します：

#### Javaクラスを定義する
シリアライズしたいフィールドを持つクラスを作成します。Jacksonはデフォルトでこれらを使用してプライベートフィールドにアクセスするため、ゲッターとセッターを持つようにします：

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
`ObjectMapper` を使用してオブジェクトをJSONに変換します：

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

### 4. JSONをJavaオブジェクトに変換する（デシリアライズ）
JSON文字列をJavaオブジェクトに戻すには、`readValue` メソッドを使用します：

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonExample {
    private static final ObjectMapper mapper = new ObjectMapper();

    public static void main(String[] args) throws Exception {
        String json = "{\"field1\":\"value1\",\"field2\":123}";
        MyClass obj = mapper.readValue(json, MyClass.class);
        System.out.println(obj.getField1()); // "value1" を出力
    }
}
```

- **エラーハンドリング**: `readValue` メソッドは、JSONが不正またはクラス構造に一致しない場合に `JsonProcessingException`（チェック例外）をスローします。try-catchブロックで処理するか、メソッドシグネチャで宣言します：

```java
try {
    MyClass obj = mapper.readValue(json, MyClass.class);
} catch (JsonProcessingException e) {
    e.printStackTrace();
}
```

---

### 5. アノテーションを使用してJSON処理をカスタマイズする
Jacksonは、フィールドがシリアライズまたはデシリアライズされる方法をカスタマイズするためのアノテーションを提供します。これらのアノテーションを `com.fasterxml.jackson.annotation` からクラスに追加します：

#### フィールド名を変更する
`@JsonProperty` を使用して、Javaフィールドを異なるJSONフィールド名にマッピングします：

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
`@JsonIgnore` を使用して、フィールドをシリアライズから除外します：

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
`@JsonFormat` を使用して、日付がシリアライズされる方法を指定します：

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

**出力** (例):
```json
{"field1":"value1","date":"2023-10-25"}
```

---

### 6. 高度なシナリオを処理する
以下は、役立つかもしれない追加機能です：

#### JSONを整形して表示する
可読性の高いJSON出力を得るには、`writerWithDefaultPrettyPrinter` を使用します：

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
JSONにJavaクラスに存在しないフィールドが含まれている場合、`ObjectMapper` を設定して無視します：

```java
mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
```

#### ファイルを操作する
ファイルから読み取ったり、ファイルに書き込んだりします：

```java
// ファイルに書き込む
mapper.writeValue(new File("output.json"), obj);

// ファイルから読み込む
MyClass obj = mapper.readValue(new File("input.json"), MyClass.class);
```

#### リストやジェネリックを扱う
コレクションの場合は、`TypeReference` を使用してジェネリック型情報を保持します：

```java
import com.fasterxml.jackson.core.type.TypeReference;
import java.util.List;

List<MyClass> list = mapper.readValue(json, new TypeReference<List<MyClass>>() {});
```

---

### 7. `JsonNode` を使用した動的JSON操作
特定のクラスにJSONをマッピングしたくない場合は、`JsonNode` を使用してツリーベースのアプローチを採用します：

```java
import com.fasterxml.jackson.databind.JsonNode;

JsonNode node = mapper.readTree("{\"field1\":\"value1\",\"field2\":123}");
String value = node.get("field1").asText(); // "value1" を返す
```

JSONを動的に構築することもできます：

```java
import com.fasterxml.jackson.databind.node.ObjectNode;

ObjectNode node = mapper.createObjectNode();
node.put("field1", "value1");
node.put("field2", 123);
String json = mapper.writeValueAsString(node);
```

---

### まとめ
`com.fasterxml.jackson` パッケージを使用するには：
1. `pom.xml` に `jackson-databind` の依存関係を追加します。
2. 再利用可能な単一の `ObjectMapper` インスタンスを作成します。
3. `writeValueAsString` を使用してJavaオブジェクトをJSONに変換し、`readValue` を使用してJSONをJavaオブジェクトに変換します。
4. `@JsonProperty`、`@JsonIgnore`、`@JsonFormat` などのアノテーションを使用して動作をカスタマイズします。
5. 例外（例：`JsonProcessingException`）を処理し、`ObjectMapper` を特定の要件（例：未知のプロパティを無視する）に設定します。
6. 高度な機能（例：整形された出力、ファイルI/O、または動的JSON処理のための `JsonNode`）を探索します。

これらの手順に従うことで、Jacksonライブラリを使用してJavaアプリケーションでJSONを効果的に処理することができます。