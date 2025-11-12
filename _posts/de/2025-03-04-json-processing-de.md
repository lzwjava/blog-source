---
audio: false
generated: true
lang: de
layout: post
title: JSON-Verarbeitung in Java
translated: true
type: note
---

Um das `com.fasterxml.jackson`-Paket in einem Java-Projekt für die JSON-Verarbeitung zu verwenden, können Sie die Jackson-Bibliothek nutzen, die häufig für die Konvertierung von Java-Objekten in JSON und umgekehrt verwendet wird. Im Folgenden finden Sie eine Schritt-für-Schritt-Anleitung für den Einstieg, vorausgesetzt, Sie arbeiten mit einem Maven-basierten Projekt. Dieser Leitfaden konzentriert sich auf das Modul `jackson-databind`, das High-Level-Funktionalität für JSON-Databinding bietet.

---

### 1. Fügen Sie die Jackson-Abhängigkeit zu Ihrem Projekt hinzu
Um das `com.fasterxml.jackson`-Paket zu verwenden, müssen Sie die Jackson-Bibliothek in Ihr Projekt einbinden. Wenn Sie Maven verwenden, fügen Sie die folgende Abhängigkeit zu Ihrer `pom.xml`-Datei hinzu:

```xml
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.12.5</version> <!-- Ersetzen Sie dies durch die neueste Version -->
</dependency>
```

- **Hinweis**: Überprüfen Sie das [Maven Central Repository](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind) auf die neueste Version, da diese möglicherweise neuer als 2.12.5 ist.
- Das Modul `jackson-databind` hängt von `jackson-core` und `jackson-annotations` ab, daher müssen Sie diese nicht separat hinzufügen, es sei denn, Sie haben spezifische Anforderungen.

Nachdem Sie die Abhängigkeit hinzugefügt haben, führen Sie `mvn install` aus oder aktualisieren Sie Ihr Projekt in Ihrer IDE, um die Bibliothek herunterzuladen.

---

### 2. Erstellen Sie eine `ObjectMapper`-Instanz
Die `ObjectMapper`-Klasse aus dem Paket `com.fasterxml.jackson.databind` ist das Hauptwerkzeug für JSON-Operationen. Sie ist threadsicher und ressourcenintensiv zu instanziieren, daher ist es am besten, eine einzelne, wiederverwendbare Instanz zu erstellen:

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonExample {
    private static final ObjectMapper mapper = new ObjectMapper();
}
```

Platzieren Sie dies in einer Klasse, in der Sie JSON-Operationen durchführen werden.

---

### 3. Konvertieren Sie ein Java-Objekt in JSON (Serialisierung)
Um ein Java-Objekt in einen JSON-String zu konvertieren, verwenden Sie die Methode `writeValueAsString`. Hier ist ein Beispiel:

#### Definieren Sie eine Java-Klasse
Erstellen Sie eine Klasse mit Feldern, die Sie serialisieren möchten. Stellen Sie sicher, dass sie Getter und Setter hat, da Jackson diese standardmäßig verwendet, um auf private Felder zuzugreifen:

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

#### Serialisieren Sie zu JSON
Verwenden Sie `ObjectMapper`, um das Objekt in JSON zu konvertieren:

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
Um einen JSON-String zurück in ein Java-Objekt zu konvertieren, verwenden Sie die Methode `readValue`:

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

- **Fehlerbehandlung**: Die Methode `readValue` wirft `JsonProcessingException` (eine geprüfte Exception), wenn der JSON fehlerhaft ist oder nicht zur Klassenstruktur passt. Behandeln Sie sie mit einem try-catch-Block oder deklarieren Sie sie in der Methodensignatur:

```java
try {
    MyClass obj = mapper.readValue(json, MyClass.class);
} catch (JsonProcessingException e) {
    e.printStackTrace();
}
```

---

### 5. Passen Sie die JSON-Verarbeitung mit Anmerkungen an
Jackson bietet Anmerkungen, um anzupassen, wie Felder serialisiert oder deserialisiert werden. Fügen Sie diese Anmerkungen aus `com.fasterxml.jackson.annotation` zu Ihrer Klasse hinzu:

#### Benennen Sie ein Feld um
Verwenden Sie `@JsonProperty`, um ein Java-Feld einem anderen JSON-Feldnamen zuzuordnen:

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

#### Ignorieren Sie ein Feld
Verwenden Sie `@JsonIgnore`, um ein Feld von der Serialisierung auszuschließen:

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

#### Formatieren Sie Datumsangaben
Verwenden Sie `@JsonFormat`, um anzugeben, wie Datumsangaben serialisiert werden:

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

### 6. Behandeln Sie erweiterte Szenarien
Hier sind einige zusätzliche Funktionen, die nützlich sein könnten:

#### Pretty-Print JSON
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

#### Ignorieren Sie unbekannte Eigenschaften
Wenn der JSON Felder enthält, die nicht in Ihrer Java-Klasse vorhanden sind, konfigurieren Sie `ObjectMapper`, um sie zu ignorieren:

```java
mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
```

#### Arbeiten Sie mit Dateien
Lesen Sie aus einer Datei oder schreiben Sie in eine Datei:

```java
// In Datei schreiben
mapper.writeValue(new File("output.json"), obj);

// Aus Datei lesen
MyClass obj = mapper.readValue(new File("input.json"), MyClass.class);
```

#### Behandeln Sie Listen oder Generics
Verwenden Sie für Sammlungen `TypeReference`, um generische Typinformationen zu erhalten:

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

Sie können JSON auch dynamisch erstellen:

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
3. Verwenden Sie `writeValueAsString`, um Java-Objekte in JSON zu konvertieren, und `readValue`, um JSON in Java-Objekte zu konvertieren.
4. Passen Sie das Verhalten mit Anmerkungen wie `@JsonProperty`, `@JsonIgnore` und `@JsonFormat` an.
5. Behandeln Sie Ausnahmen (z.B. `JsonProcessingException`) und konfigurieren Sie `ObjectMapper` für spezifische Anforderungen (z.B. Ignorieren unbekannter Eigenschaften).
6. Erkunden Sie erweiterte Funktionen wie Pretty-Printing, Datei-I/O oder `JsonNode` für dynamische JSON-Verarbeitung.

Mit diesen Schritten können Sie JSON effektiv in Ihrer Java-Anwendung mit der Jackson-Bibliothek verarbeiten.