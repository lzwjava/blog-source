---
audio: false
generated: true
lang: de
layout: post
title: Java-API für RocksDB
translated: true
---

Um die `org.rocksdb`-Bibliothek zu verwenden, die die Java-API für RocksDB ist – eine hochleistungsfähige eingebettete Datenbank für Schlüssel-Wert-Daten – müssen Sie die folgenden Schritte befolgen. RocksDB ist für schnellen Speicher und schnellen Abruf optimiert, was sie ideal für Anwendungen macht, die schnellen Zugriff auf Daten durch bekannte Schlüssel benötigen. Hier ist eine umfassende Anleitung, um Ihnen den Einstieg zu erleichtern:

---

### 1. **Abhängigkeit hinzufügen**
Um `org.rocksdb` in Ihrem Java-Projekt zu verwenden, müssen Sie die RocksDB JNI (Java Native Interface)-Abhängigkeit hinzufügen. Wenn Sie Maven verwenden, fügen Sie dies zu Ihrer `pom.xml`-Datei hinzu:

```xml
<dependency>
    <groupId>org.rocksdb</groupId>
    <artifactId>rocksdbjni</artifactId>
    <version>7.10.2</version>
</dependency>
```

Für Gradle fügen Sie dies zu Ihrer `build.gradle`-Datei hinzu:

```groovy
implementation 'org.rocksdb:rocksdbjni:7.10.2'
```

**Hinweis**: Überprüfen Sie [Maven Central](https://search.maven.org/search?q=g:org.rocksdb%20AND%20a:rocksdbjni) auf die neueste Version, da `7.10.2` möglicherweise nicht aktuell ist.

---

### 2. **Native Bibliothek laden**
RocksDB basiert auf nativem C++-Code, daher müssen Sie die native Bibliothek vor der Verwendung laden. Fügen Sie diese Zeile zu Beginn Ihres Codes hinzu:

```java
RocksDB.loadLibrary();
```

Andernfalls treten Laufzeitfehler auf.

---

### 3. **Datenbank öffnen**
Um mit RocksDB zu beginnen, müssen Sie eine Datenbankinstanz öffnen, indem Sie einen Dateipfad angeben, an dem die Datenbank gespeichert wird. Verwenden Sie die `Options`-Klasse, um Einstellungen zu konfigurieren, wie z. B. das Erstellen der Datenbank, wenn sie nicht existiert:

```java
import org.rocksdb.Options;
import org.rocksdb.RocksDB;

Options options = new Options().setCreateIfMissing(true);
RocksDB db = RocksDB.open(options, "/path/to/db");
```

- **`options`**: Konfiguriert das Datenbankverhalten (z. B. `setCreateIfMissing(true)` stellt sicher, dass die Datenbank erstellt wird, wenn sie nicht existiert).
- **`/path/to/db`**: Ersetzen Sie dies durch einen gültigen Verzeichnispfad auf Ihrem System, an dem die Datenbankdateien gespeichert werden sollen.

---

### 4. **Grundlegende Operationen durchführen**
RocksDB ist ein Schlüssel-Wert-Speicher, und seine Kernoperationen sind `put`, `get` und `delete`. Schlüssel und Werte werden als Byte-Arrays gespeichert, sodass Sie Daten (z. B. Zeichenfolgen) in Bytes umwandeln müssen.

- **Put**: Fügen Sie ein Schlüssel-Wert-Paar ein oder aktualisieren Sie es.
  ```java
  db.put("key".getBytes(), "value".getBytes());
  ```

- **Get**: Holen Sie sich den Wert, der mit einem Schlüssel verbunden ist.
  ```java
  byte[] value = db.get("key".getBytes());
  if (value != null) {
      System.out.println(new String(value));  // Gibt "value" aus
  } else {
      System.out.println("Schlüssel nicht gefunden");
  }
  ```

- **Delete**: Entfernen Sie ein Schlüssel-Wert-Paar.
  ```java
  db.delete("key".getBytes());
  ```

---

### 5. **Datenbank schließen**
Das ordnungsgemäße Schließen der Datenbank ist wichtig, um Ressourcen freizugeben. Die einfachste Methode besteht darin, einen try-with-resources-Block zu verwenden, der die Datenbank automatisch schließt, wenn Sie fertig sind:

```java
try (RocksDB db = RocksDB.open(options, "/path/to/db")) {
    // Operationen hier durchführen
} catch (Exception e) {
    e.printStackTrace();
}
```

---

### 6. **Ausnahmen behandeln**
RocksDB-Operationen können `RocksDBException` auslösen, daher sollten Sie immer eine Ausnahmebehandlung einbeziehen, um Ressourcenlecks oder Datenbeschädigungen zu verhindern:

```java
try {
    db.put("key".getBytes(), "value".getBytes());
} catch (RocksDBException e) {
    e.printStackTrace();
}
```

---

### 7. **Konfigurationsoptionen**
Sie können die Leistung von RocksDB mit der `Options`-Klasse fein abstimmen. Zum Beispiel:

```java
Options options = new Options()
    .setCreateIfMissing(true)
    .setWriteBufferSize(64 * 1024 * 1024);  // 64MB-Schreibpuffer
```

Gängige Optionen umfassen:
- `setWriteBufferSize`: Steuert den für Schreibvorgänge verwendeten Speicher.
- `setMaxOpenFiles`: Begrenzt die Anzahl der offenen Dateien.
- `setCompactionStyle`: Passt an, wie Daten auf der Festplatte komprimiert werden.

Erkundigen Sie sich in der [RocksDB-Dokumentation](https://github.com/facebook/rocksdb/wiki) nach weiteren Optionen.

---

### 8. **Einfaches Beispiel**
Hier ist ein vollständiges Beispiel, das das Öffnen einer Datenbank, das Speichern eines Schlüssel-Wert-Paars und das Abrufen zeigt:

```java
import org.rocksdb.RocksDB;
import org.rocksdb.Options;

public class SimpleRocksDBExample {
    public static void main(String[] args) {
        RocksDB.loadLibrary();  // Lade die native Bibliothek
        Options options = new Options().setCreateIfMissing(true);

        try (RocksDB db = RocksDB.open(options, "/tmp/rocksdb_example")) {
            // Füge ein Schlüssel-Wert-Paar hinzu
            db.put("hello".getBytes(), "world".getBytes());

            // Hole den Wert
            byte[] value = db.get("hello".getBytes());
            if (value != null) {
                System.out.println(new String(value));  // Gibt "world" aus
            } else {
                System.out.println("Schlüssel nicht gefunden");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

**Ausgabe**: `world`

---

### Wichtige Überlegungen
- **Eingebettete Natur**: RocksDB läuft innerhalb des Prozesses Ihrer Anwendung, nicht als separater Server.
- **Byte-Arrays**: Schlüssel und Werte sind `byte[]`, sodass Sie Serialisierung/Deserialisierung für komplexe Objekte handhaben müssen.
- **Leistung**: RocksDB glänzt mit schnellem Speicher (z. B. SSDs) und wird in Hochleistungsystemen wie denen bei Facebook verwendet, wo es entwickelt wurde.
- **Nicht relational**: Es ist ein Schlüssel-Wert-Speicher, keine relationale Datenbank – keine SQL oder Joins.

---

### Häufige Stolpersteine
- **Vergessen von `RocksDB.loadLibrary()`**: Führt zu `UnsatisfiedLinkError`.
- **Unzureichendes Ressourcenmanagement**: Nicht Schließen der Datenbank kann Probleme verursachen, insbesondere auf ressourcenbeschränkten Systemen.
- **Fehler bei Datentypen**: Übergeben von Zeichenfolgen oder Objekten direkt anstelle der Umwandlung in `byte[]`.

---

### Weiterführende Informationen
- **Erweiterte Funktionen**: Erkunden Sie Transaktionen, Snapshots oder Spaltenfamilien für komplexere Anwendungsfälle.
- **Ressourcen**: Überprüfen Sie die [RocksDB Java API](https://github.com/facebook/rocksdb/tree/main/java) und die [RocksDB Wiki](https://github.com/facebook/rocksdb/wiki) für detaillierte Dokumentation und Beispiele.

Diese Anleitung bietet eine solide Grundlage für die Verwendung von `org.rocksdb`. Wenn Sie Hilfe bei spezifischen Funktionen oder Anwendungsfällen benötigen, zögern Sie nicht zu fragen!