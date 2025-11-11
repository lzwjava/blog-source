---
audio: false
generated: true
lang: de
layout: post
title: Verwendung von FastJson
translated: true
type: note
---

FastJSON ist eine hochperformante JSON-Verarbeitungsbibliothek für Java, die von Alibaba entwickelt wurde. Sie wird häufig zum Parsen von JSON-Strings in Java-Objekte, zum Serialisieren von Java-Objekten in JSON und zur effizienten Verarbeitung von JSON-Daten verwendet. Im Folgenden finden Sie eine Anleitung zur Verwendung von FastJSON basierend auf seinen Kernfunktionen.

### Schritt 1: FastJSON zu Ihrem Projekt hinzufügen
Um FastJSON zu verwenden, müssen Sie es in Ihr Projekt einbinden. Wenn Sie Maven verwenden, fügen Sie die folgende Abhängigkeit zu Ihrer `pom.xml` hinzu:

```xml
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>2.0.51</version> <!-- Verwenden Sie die neueste verfügbare Version -->
</dependency>
```

Für Gradle fügen Sie dies zu Ihrer `build.gradle` hinzu:

```gradle
implementation 'com.alibaba:fastjson:2.0.51'
```

Überprüfen Sie das [Maven Central Repository](https://mvnrepository.com/artifact/com.alibaba/fastjson) auf die neueste Version.

### Schritt 2: Grundlegende Verwendung
Hier erfahren Sie, wie Sie FastJSON für häufige Aufgaben wie Serialisierung und Deserialisierung verwenden können.

#### 1. **Serialisieren von Java-Objekten zu JSON**
Sie können ein Java-Objekt in einen JSON-String mit `JSON.toJSONString()` konvertieren.

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        // Ein Beispielobjekt erstellen
        User user = new User("Alice", 25);
        
        // Zu JSON-String serialisieren
        String jsonString = JSON.toJSONString(user);
        System.out.println(jsonString);
    }
}

// Beispiel User-Klasse
class User {
    private String name;
    private int age;

    public User(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Getter und Setter (erforderlich, damit FastJSON korrekt funktioniert)
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }
}
```

**Ausgabe:**
```json
{"age":25,"name":"Alice"}
```

#### 2. **Deserialisieren von JSON zu Java-Objekten**
Sie können einen JSON-String mit `JSON.parseObject()` wieder in ein Java-Objekt parsen.

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        String jsonString = "{\"age\":25,\"name\":\"Alice\"}";
        
        // Zu User-Objekt deserialisieren
        User user = JSON.parseObject(jsonString, User.class);
        System.out.println("Name: " + user.getName() + ", Age: " + user.getAge());
    }
}
```

**Ausgabe:**
```
Name: Alice, Age: 25
```

#### 3. **Parsen von JSON in eine Liste**
Wenn Ihr JSON eine Liste von Objekten darstellt, verwenden Sie `JSON.parseArray()`.

```java
import com.alibaba.fastjson.JSON;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        String jsonArray = "[{\"name\":\"Alice\",\"age\":25},{\"name\":\"Bob\",\"age\":30}]";
        
        // Zu List<User> deserialisieren
        List<User> users = JSON.parseArray(jsonArray, User.class);
        for (User user : users) {
            System.out.println("Name: " + user.getName() + ", Age: " + user.getAge());
        }
    }
}
```

**Ausgabe:**
```
Name: Alice, Age: 25
Name: Bob, Age: 30
```

### Schritt 3: Erweiterte Funktionen
FastJSON bietet zusätzliche Anpassungsoptionen:

#### 1. **Anpassen der Serialisierung**
Sie können steuern, wie Felder serialisiert werden, indem Sie `SerializerFeature`-Optionen verwenden.

```java
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.serializer.SerializerFeature;

public class Main {
    public static void main(String[] args) {
        User user = new User("Alice", 25);
        
        // PrettyFormat für lesbare Ausgabe verwenden
        String jsonString = JSON.toJSONString(user, SerializerFeature.PrettyFormat);
        System.out.println(jsonString);
    }
}
```

**Ausgabe:**
```json
{
	"age":25,
	"name":"Alice"
}
```

Häufige `SerializerFeature`-Optionen:
- `WriteNullListAsEmpty`: Leere Listen werden als `[]` statt `null` geschrieben.
- `WriteMapNullValue`: Felder mit `null`-Werten in die Ausgabe aufnehmen.

#### 2. **Umgang mit komplexen Objekten**
Stellen Sie bei verschachtelten Objekten sicher, dass die inneren Klassen über ordnungsgemäße Getter/Setter verfügen.

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        Address address = new Address("123 Main St", "NY");
        User user = new User("Alice", 25, address);
        
        String jsonString = JSON.toJSONString(user);
        System.out.println(jsonString);

        User parsedUser = JSON.parseObject(jsonString, User.class);
        System.out.println(parsedUser.getAddress().getCity());
    }
}

class User {
    private String name;
    private int age;
    private Address address;

    public User(String name, int age, Address address) {
        this.name = name;
        this.age = age;
        this.address = address;
    }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }
    public Address getAddress() { return address; }
    public void setAddress(Address address) { this.address = address; }
}

class Address {
    private String street;
    private String city;

    public Address(String street, String city) {
        this.street = street;
        this.city = city;
    }

    public String getStreet() { return street; }
    public void setStreet(String street) { this.street = street; }
    public String getCity() { return city; }
    public void setCity(String city) { this.city = city; }
}
```

**Ausgabe:**
```json
{"address":{"city":"NY","street":"123 Main St"},"age":25,"name":"Alice"}
NY
```

### Schritt 4: Hinweise und Best Practices
- **Sicherheit**: FastJSON hatte in älteren Versionen Schwachstellen (z.B. Remote Code Execution). Verwenden Sie immer die neueste Version und vermeiden Sie die Aktivierung von `Feature.SupportAutoType`, es sei denn, es ist unbedingt erforderlich.
- **Performance**: FastJSON ist auf Geschwindigkeit optimiert, testen Sie es jedoch für große Datensätze in Ihrem spezifischen Anwendungsfall.
- **Dokumentation**: Weitere Details finden Sie auf der offiziellen [FastJSON GitHub-Seite](https://github.com/alibaba/fastjson).

Lassen Sie mich wissen, wenn Sie Hilfe bei einem spezifischen Anwendungsfall oder bei der Fehlerbehebung benötigen!