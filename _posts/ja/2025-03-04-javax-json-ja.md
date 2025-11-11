---
audio: false
generated: true
lang: ja
layout: post
title: Javax Json処理
translated: true
type: note
---

`javax.json`パッケージ（Java API for JSON Processing - JSON-Pの一部）を使用してJavaでJSONデータを扱う方法を説明します。包括的なガイドは以下の通りです：

1. まず、プロジェクトに依存関係を追加します（Mavenを使用する場合）：
```xml
<dependency>
    <groupId>javax.json</groupId>
    <artifactId>javax.json-api</artifactId>
    <version>1.1.4</version>
</dependency>
<!-- 実装（GlassFishなど） -->
<dependency>
    <groupId>org.glassfish</groupId>
    <artifactId>javax.json</artifactId>
    <version>1.1.4</version>
</dependency>
```

2. `javax.json`の基本的な使用例：

a) JSONオブジェクトの作成：
```java
import javax.json.Json;
import javax.json.JsonObject;
import javax.json.JsonArray;

public class JsonExample {
    public static void main(String[] args) {
        // JSONオブジェクトを作成
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

b) JSON配列の作成：
```java
JsonArray jsonArray = Json.createArrayBuilder()
    .add("Apple")
    .add("Banana")
    .add(Json.createObjectBuilder()
        .add("name", "Orange")
        .add("price", 0.99))
    .build();
```

c) 文字列からのJSON解析：
```java
import javax.json.JsonReader;
import java.io.StringReader;

String jsonString = "{\"name\":\"Jane\",\"age\":25}";
JsonReader jsonReader = Json.createReader(new StringReader(jsonString));
JsonObject parsedObject = jsonReader.readObject();
jsonReader.close();

// 値へのアクセス
String name = parsedObject.getString("name");
int age = parsedObject.getInt("age");
```

d) JSONを文字列に書き込み：
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
- `Json`：JSONビルダーとリーダーを作成するファクトリクラス
- `JsonObject`：JSONオブジェクトを表現
- `JsonArray`：JSON配列を表現
- `JsonObjectBuilder`：JSONオブジェクトを構築
- `JsonArrayBuilder`：JSON配列を構築
- `JsonReader`：入力ソースからJSONを読み取り
- `JsonWriter`：出力ソースにJSONを書き込み

4. 異なるJSON値タイプの処理：
```java
JsonObject obj = // ... 何らかのJSONオブジェクト
String stringValue = obj.getString("key");
int intValue = obj.getInt("key");
boolean boolValue = obj.getBoolean("key");
JsonObject nestedObj = obj.getJsonObject("key");
JsonArray arrayValue = obj.getJsonArray("key");

// キーの存在確認とnullの処理
if (obj.containsKey("key") && !obj.isNull("key")) {
    String value = obj.getString("key");
}
```

5. ストリーミングAPIの例（大規模なJSON用）：
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
- `JsonReader`、`JsonWriter`、`JsonParser`は使用後に必ずクローズする
- 解析エラーの可能性に対して`javax.json.JsonException`を処理する
- 大規模なJSONドキュメントにはストリーミングAPI（`JsonParser`）を使用する
- APIは不変です - ビルダーは新しいインスタンスを作成する

これで`javax.json`の基本的な使用方法を網羅しました。より具体的な例が必要な場合や特定のユースケースがある場合はお知らせください！