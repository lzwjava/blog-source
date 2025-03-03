---
audio: false
generated: true
lang: ja
layout: post
title: Javax Json 処理
translated: true
---

`javax.json` パッケージを使用して JSON データを Java で操作する方法を説明します。これは Java API for JSON Processing (JSON-P) の一部です。以下に包括的なガイドを示します。

1. まず、プロジェクトに依存関係を追加します（Maven を使用する場合）：
```xml
<dependency>
    <groupId>javax.json</groupId>
    <artifactId>javax.json-api</artifactId>
    <version>1.1.4</version>
</dependency>
<!-- 実装（GlassFish のようなもの） -->
<dependency>
    <groupId>org.glassfish</groupId>
    <artifactId>javax.json</artifactId>
    <version>1.1.4</version>
</dependency>
```

2. `javax.json` の基本的な使用例：

a) JSON オブジェクトの作成：
```java
import javax.json.Json;
import javax.json.JsonObject;
import javax.json.JsonArray;

public class JsonExample {
    public static void main(String[] args) {
        // JSON オブジェクトを作成
        JsonObject jsonObject = Json.createObjectBuilder()
            .add("name", "John Doe")
            .add("age", 30)
            .add("isStudent", false)
            .add("address", Json.createObjectBuilder()
                .add("street", "123 Main St")
                .add("city", "New York"))
            .build();

        System.out.println(jsonObject.toString());
    }
}
```

b) JSON 配列の作成：
```java
JsonArray jsonArray = Json.createArrayBuilder()
    .add("Apple")
    .add("Banana")
    .add(Json.createObjectBuilder()
        .add("name", "Orange")
        .add("price", 0.99))
    .build();
```

c) 文字列から JSON を解析：
```java
import javax.json.JsonReader;
import java.io.StringReader;

String jsonString = "{\"name\":\"Jane\",\"age\":25}";
JsonReader jsonReader = Json.createReader(new StringReader(jsonString));
JsonObject parsedObject = jsonReader.readObject();
jsonReader.close();

// 値にアクセス
String name = parsedObject.getString("name");
int age = parsedObject.getInt("age");
```

d) JSON を文字列に書き込む：
```java
import javax.json.JsonWriter;
import java.io.StringWriter;

JsonObject jsonObject = Json.createObjectBuilder()
    .add("title", "Example")
    .build();

StringWriter stringWriter = new StringWriter();
JsonWriter jsonWriter = Json.createWriter(stringWriter);
jsonWriter.writeObject(jsonObject);
jsonWriter.close();

String result = stringWriter.toString();
```

3. 主要なクラスとインターフェース：
- `Json`：JSON ビルダーとリーダーを作成するためのファクトリクラス
- `JsonObject`：JSON オブジェクトを表す
- `JsonArray`：JSON 配列を表す
- `JsonObjectBuilder`：JSON オブジェクトを構築する
- `JsonArrayBuilder`：JSON 配列を構築する
- `JsonReader`：入力ソースから JSON を読み取る
- `JsonWriter`：出力ソースに JSON を書き込む

4. 異なる JSON 値の種類を処理する：
```java
JsonObject obj = // ... 何かの JSON オブジェクト
String stringValue = obj.getString("key");
int intValue = obj.getInt("key");
boolean boolValue = obj.getBoolean("key");
JsonObject nestedObj = obj.getJsonObject("key");
JsonArray arrayValue = obj.getJsonArray("key");

// キーが存在し、null でないことを確認
if (obj.containsKey("key") && !obj.isNull("key")) {
    String value = obj.getString("key");
}
```

5. ストリーミング API の例（大規模な JSON 用）：
```java
import javax.json.stream.JsonParser;
import java.io.StringReader;

String json = "{\"name\":\"John\",\"scores\":[1,2,3]}";
JsonParser parser = Json.createParser(new StringReader(json));
while (parser.hasNext()) {
    JsonParser.Event event = parser.next();
    switch (event) {
        case KEY_NAME:
            System.out.println("Key: " + parser.getString());
            break;
        case VALUE_STRING:
            System.out.println("String: " + parser.getString());
            break;
        case VALUE_NUMBER:
            System.out.println("Number: " + parser.getBigDecimal());
            break;
    }
}
parser.close();
```

ヒント：
- `JsonReader`、`JsonWriter`、`JsonParser` を使用した後は必ず閉じる
- 解析エラーの可能性があるため、`javax.json.JsonException` を処理する
- 大規模な JSON ドキュメントにはストリーミング API（`JsonParser`）を使用する
- API は不変である - ビルダーは新しいインスタンスを作成する

これは `javax.json` の基本的な使用方法です。特定の使用例や詳細な例が必要な場合はお知らせください！