---
audio: false
generated: true
lang: de
layout: post
title: JSON-Verarbeitung in Java
translated: true
---

Um das `com.fasterxml.jackson`-Paket in einem Java-Projekt zur JSON-Verarbeitung zu verwenden, können Sie die Jackson-Bibliothek nutzen, die weit verbreitet ist, um Java-Objekte in JSON umzuwandeln und umgekehrt. Hier ist eine Schritt-für-Schritt-Anleitung, um Sie zu starten, vorausgesetzt, Sie arbeiten mit einem Maven-basierten Projekt. Diese Anleitung konzentriert sich auf das `jackson-databind`-Modul, das eine hochwertige Funktionalität für JSON-Databinding bietet.

---

### 1. Jackson-Abhängigkeit zum Projekt hinzufügen
Um das `com.fasterxml.jackson`-Paket zu verwenden, müssen Sie die Jackson-Bibliothek in Ihr Projekt einbinden. Wenn Sie Maven verwenden, fügen Sie die folgende Abhängigkeit zu Ihrer `pom.xml`-Datei hinzu:

```xml
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.12.5</version> <!-- Ersetzen Sie durch die neueste Version -->
</dependency>
```

- **Hinweis**: Überprüfen Sie das [Maven Central Repository](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind) auf die neueste Version, da diese neuer als 2.12.5 sein könnte.
- Das `jackson-databind`-Modul hängt von `jackson-core` und `jackson-annotations` ab, sodass Sie diese nicht separat hinzufügen müssen, es sei denn, Sie haben spezifische Anforderungen.

Nach dem Hinzufügen der Abhängigkeit führen Sie `mvn install` aus oder aktualisieren Sie Ihr Projekt in Ihrer IDE, um die Bibliothek herunterzuladen.

---

### 2. Erstellen Sie eine `ObjectMapper`-Instanz
Die `ObjectMapper`-Klasse aus dem `com.fasterxml.jackson.databind`-Paket ist das Hauptwerkzeug für JSON-Operationen. Sie ist thread-sicher und ressourcenintensiv, sodass es am besten ist, eine einzige, wiederverwendbare Instanz zu erstellen:

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonExample {
    private static final ObjectMapper mapper = new ObjectMapper();
}
```

Platzieren Sie dies in einer Klasse, in der Sie JSON-Operationen durchführen.

---

### 3. Konvertieren Sie ein Java-Objekt in JSON (Serialisierung)
Um ein Java-Objekt in eine JSON-Zeichenkette umzuwandeln, verwenden Sie die `writeValueAsString`-Methode. Hier ist ein Beispiel:

#### Definieren Sie eine Java-Klasse
Erstellen Sie eine Klasse mit Feldern, die Sie serialisieren möchten. Stellen Sie sicher, dass sie Getter- und Setter-Methoden hat, da Jackson diese standardmäßig verwendet, um auf private Felder zuzugreifen:

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

#### Serialisieren Sie in JSON
Verwenden Sie `ObjectMapper`, um das Objekt in JSON umzuwandeln:

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

**Ausgabe**:
```json
{"field1":"value1","field2":123}
```

---

### 4. Konvertieren Sie JSON in ein Java-Objekt (Deserialisierung)
Um eine JSON-Zeichenkette wieder in ein Java-Objekt umzuwandeln, verwenden Sie die `readValue`-Methode:

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonExample {
    private static final ObjectMapper mapper = new ObjectMapper();

    public static void main(String[] args) throws Exception {
        String json = "{\"field1\":\"value1\",\"field2\":123}";
        MyClass obj = mapper.readValue(json, MyClass.class);
        System.out.println(obj.getField1()); // Gibt "value1" aus
    }
}
```

- **Fehlerbehandlung**: Die `readValue`-Methode wirft eine `JsonProcessingException` (eine geprüfte Ausnahme) aus, wenn das JSON fehlerhaft ist oder nicht mit der Klassenstruktur übereinstimmt. Behandeln Sie dies mit einem try-catch-Block oder deklarieren Sie es in der Methoden-Signatur:

```java
try {
    MyClass obj = mapper.readValue(json, MyClass.class);
} catch (JsonProcessingException e) {
    e.printStackTrace();
}
```

---

### 5. JSON-Verarbeitung mit Annotationen anpassen
Jackson bietet Annotationen, um zu steuern, wie Felder serialisiert oder deserialisiert werden. Fügen Sie diese Annotationen aus `com.fasterxml.jackson.annotation` zu Ihrer Klasse hinzu:

#### Feld umbenennen
Verwenden Sie `@JsonProperty`, um ein Java-Feld auf einen anderen JSON-Feldnamen abzubilden:

```java
import com.fasterxml.jackson.annotation.JsonProperty;

public class MyClass {
    @JsonProperty("name")
    private String field1;
    private int field2;
    // Konstruktor, Getter, Setter
}
```

**Ausgabe**:
```json
{"name":"value1","field2":123}
```

#### Feld ignorieren
Verwenden Sie `@JsonIgnore`, um ein Feld aus der Serialisierung auszuschließen:

```java
import com.fasterxml.jackson.annotation.JsonIgnore;

public class MyClass {
    private String field1;
    @JsonIgnore
    private int field2;
    // Konstruktor, Getter, Setter
}
```

**Ausgabe**:
```json
{"field1":"value1"}
```

#### Datumsformat festlegen
Verwenden Sie `@JsonFormat`, um festzulegen, wie Datumsangaben serialisiert werden:

```java
import com.fasterxml.jackson.annotation.JsonFormat;
import java.util.Date;

public class MyClass {
    private String field1;
    @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "yyyy-MM-dd")
    private Date date;
    // Konstruktor, Getter, Setter
}
```

**Ausgabe** (Beispiel):
```json
{"field1":"value1","date":"2023-10-25"}
```

---

### 6. Fortgeschrittene Szenarien behandeln
Hier sind einige zusätzliche Funktionen, die Sie nützlich finden könnten:

#### JSON schön drucken
Für lesbare JSON-Ausgabe verwenden Sie `writerWithDefaultPrettyPrinter`:

```java
String prettyJson = mapper.writerWithDefaultPrettyPrinter().writeValueAsString(obj);
```

**Ausgabe**:
```json
{
  "field1" : "value1",
  "field2" : 123
}
```

#### Unbekannte Eigenschaften ignorieren
Wenn das JSON Felder enthält, die in Ihrer Java-Klasse nicht vorhanden sind, konfigurieren Sie `ObjectMapper`, um diese zu ignorieren:

```java
mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
```

#### Arbeiten mit Dateien
Lesen Sie aus einer Datei oder schreiben Sie in eine Datei:

```java
// In Datei schreiben
mapper.writeValue(new File("output.json"), obj);

// Aus Datei lesen
MyClass obj = mapper.readValue(new File("input.json"), MyClass.class);
```

#### Arbeiten mit Listen oder Generics
Für Sammlungen verwenden Sie `TypeReference`, um die generische Typinformation zu bewahren:

```java
import com.fasterxml.jackson.core.type.TypeReference;
import java.util.List;

List<MyClass> list = mapper.readValue(json, new TypeReference<List<MyClass>>() {});
```

---

### 7. Dynamische JSON-Manipulation mit `JsonNode`
Wenn Sie JSON nicht auf eine bestimmte Klasse abbilden möchten, verwenden Sie `JsonNode` für einen baumbasierten Ansatz:

```java
import com.fasterxml.jackson.databind.JsonNode;

JsonNode node = mapper.readTree("{\"field1\":\"value1\",\"field2\":123}");
String value = node.get("field1").asText(); // Gibt "value1" zurück
```

Sie können auch JSON dynamisch erstellen:

```java
import com.fasterxml.jackson.databind.node.ObjectNode;

ObjectNode node = mapper.createObjectNode();
node.put("field1", "value1");
node.put("field2", 123);
String json = mapper.writeValueAsString(node);
```

---

### Zusammenfassung
Um das `com.fasterxml.jackson`-Paket zu verwenden:
1. Fügen Sie die `jackson-databind`-Abhängigkeit zu Ihrer `pom.xml` hinzu.
2. Erstellen Sie eine einzelne `ObjectMapper`-Instanz zur Wiederverwendung.
3. Verwenden Sie `writeValueAsString`, um Java-Objekte in JSON umzuwandeln, und `readValue`, um JSON in Java-Objekte umzuwandeln.
4. Passen Sie das Verhalten mit Annotationen wie `@JsonProperty`, `@JsonIgnore` und `@JsonFormat` an.
5. Behandeln Sie Ausnahmen (z. B. `JsonProcessingException`) und konfigurieren Sie `ObjectMapper` für spezifische Anforderungen (z. B. Ignorieren unbekannter Eigenschaften).
6. Erkunden Sie erweiterte Funktionen wie schönes Drucken, Datei-E/A oder `JsonNode` für dynamische JSON-Verarbeitung.

Mit diesen Schritten können Sie JSON in Ihrer Java-Anwendung effektiv mit der Jackson-Bibliothek verarbeiten.