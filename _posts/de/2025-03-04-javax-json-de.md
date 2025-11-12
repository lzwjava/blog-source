---
audio: false
generated: true
lang: de
layout: post
title: Javax Json Verarbeitung
translated: true
type: note
---

Ich werde erklären, wie man das `javax.json`-Paket, das Teil der Java API for JSON Processing (JSON-P) ist, verwendet, um mit JSON-Daten in Java zu arbeiten. Hier ist eine umfassende Anleitung:

1. Fügen Sie zunächst die Abhängigkeit zu Ihrem Projekt hinzu (wenn Sie Maven verwenden):
```xml
<dependency>
    <groupId>javax.json</groupId>
    <artifactId>javax.json-api</artifactId>
    <version>1.1.4</version>
</dependency>
<!-- Implementation (wie GlassFish) -->
<dependency>
    <groupId>org.glassfish</groupId>
    <artifactId>javax.json</artifactId>
    <version>1.1.4</version>
</dependency>
```

2. Grundlegende Beispiele für die Verwendung von `javax.json`:

a) Erstellen eines JSON-Objekts:
```java
import javax.json.Json;
import javax.json.JsonObject;
import javax.json.JsonArray;

public class JsonExample {
    public static void main(String[] args) {
        // Ein JSON-Objekt erstellen
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

b) Erstellen eines JSON-Arrays:
```java
JsonArray jsonArray = Json.createArrayBuilder()
    .add("Apple")
    .add("Banana")
    .add(Json.createObjectBuilder()
        .add("name", "Orange")
        .add("price", 0.99))
    .build();
```

c) Parsen von JSON aus einem String:
```java
import javax.json.JsonReader;
import java.io.StringReader;

String jsonString = "{\"name\":\"Jane\",\"age\":25}";
JsonReader jsonReader = Json.createReader(new StringReader(jsonString));
JsonObject parsedObject = jsonReader.readObject();
jsonReader.close();

// Werte abrufen
String name = parsedObject.getString("name");
int age = parsedObject.getInt("age");
```

d) Schreiben von JSON in einen String:
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

3. Wichtige Klassen und Interfaces:
- `Json`: Factory-Klasse zum Erstellen von JSON-Buildern und Readern
- `JsonObject`: Repräsentiert ein JSON-Objekt
- `JsonArray`: Repräsentiert ein JSON-Array
- `JsonObjectBuilder`: Baut JSON-Objekte
- `JsonArrayBuilder`: Baut JSON-Arrays
- `JsonReader`: Liest JSON aus einer Eingabequelle
- `JsonWriter`: Schreibt JSON in eine Ausgabequelle

4. Umgang mit verschiedenen JSON-Werttypen:
```java
JsonObject obj = // ... irgendein JSON-Objekt
String stringValue = obj.getString("key");
int intValue = obj.getInt("key");
boolean boolValue = obj.getBoolean("key");
JsonObject nestedObj = obj.getJsonObject("key");
JsonArray arrayValue = obj.getJsonArray("key");

// Prüfen, ob Schlüssel existiert und Null-Werte behandeln
if (obj.containsKey("key") && !obj.isNull("key")) {
    String value = obj.getString("key");
}
```

5. Streaming-API-Beispiel (für große JSON-Daten):
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

Tipps:
- Schließen Sie immer `JsonReader`, `JsonWriter` und `JsonParser`, wenn Sie fertig sind
- Behandeln Sie `javax.json.JsonException` für mögliche Parsing-Fehler
- Verwenden Sie die Streaming-API (`JsonParser`) für große JSON-Dokumente
- Die API ist unveränderlich - Builder erstellen neue Instanzen

Dies deckt die Grundlagen der Verwendung von `javax.json` ab. Lassen Sie mich wissen, wenn Sie spezifischere Beispiele benötigen oder einen bestimmten Anwendungsfall im Sinn haben!