---
audio: false
generated: true
lang: de
layout: post
title: Java-API für RocksDB
translated: true
type: note
---

Um die `org.rocksdb`-Bibliothek zu verwenden, welche die Java-API für RocksDB ist – eine hochperformante eingebettete Datenbank für Schlüssel-Wert-Daten – müssen Sie die folgenden Schritte befolgen. RocksDB ist für schnelles Speichern und Abrufen optimiert und eignet sich daher ideal für Anwendungen, die schnellen Zugriff auf Daten über bekannte Schlüssel erfordern. Nachfolgend finden Sie eine umfassende Anleitung für den Einstieg:

---

### 1. **Abhängigkeit hinzufügen**
Um `org.rocksdb` in Ihrem Java-Projekt zu verwenden, müssen Sie die RocksDB JNI (Java Native Interface)-Abhängigkeit einbinden. Wenn Sie Maven verwenden, fügen Sie dies Ihrer `pom.xml`-Datei hinzu:

```xml
<dependency>
    <groupId>org.rocksdb</groupId>
    <artifactId>rocksdbjni</artifactId>
    <version>7.10.2</version>
</dependency>
```

Für Gradle fügen Sie dies Ihrer `build.gradle` hinzu:

```groovy
implementation 'org.rocksdb:rocksdbjni:7.10.2'
```

**Hinweis**: Überprüfen Sie [Maven Central](https://search.maven.org/search?q=g:org.rocksdb%20AND%20a:rocksdbjni) auf die neueste Version, da `7.10.2` möglicherweise nicht aktuell ist.

---

### 2. **Native Bibliothek laden**
RocksDB basiert auf nativem C++-Code, daher müssen Sie die native Bibliothek laden, bevor Sie sie verwenden. Fügen Sie diese Zeile am Anfang Ihres Codes hinzu:

```java
RocksDB.loadLibrary();
```

Wenn Sie dies unterlassen, führt dies zu Laufzeitfehlern.

---

### 3. **Datenbank öffnen**
Um RocksDB zu verwenden, müssen Sie eine Datenbankinstanz öffnen, indem Sie einen Dateipfad angeben, unter dem die Datenbank gespeichert wird. Verwenden Sie die `Options`-Klasse, um Einstellungen zu konfigurieren, z. B. das Erstellen der Datenbank, falls sie nicht existiert:

```java
import org.rocksdb.Options;
import org.rocksdb.RocksDB;

Options options = new Options().setCreateIfMissing(true);
RocksDB db = RocksDB.open(options, "/pfad/zur/db");
```

- **`options`**: Konfiguriert das Datenbankverhalten (z. B. stellt `setCreateIfMissing(true)` sicher, dass die Datenbank erstellt wird, falls sie nicht existiert).
- **`/pfad/zur/db`**: Ersetzen Sie dies durch einen gültigen Verzeichnispfad auf Ihrem System, unter dem die Datenbankdateien gespeichert werden sollen.

---

### 4. **Grundlegende Operationen durchführen**
RocksDB ist ein Schlüssel-Wert-Speicher, und seine Kernoperationen sind `put`, `get` und `delete`. Schlüssel und Werte werden als Byte-Arrays gespeichert, daher müssen Sie Daten (z. B. Zeichenketten) in Bytes konvertieren.

- **Put**: Fügt ein Schlüssel-Wert-Paar ein oder aktualisiert es.
  ```java
  db.put("key".getBytes(), "value".getBytes());
  ```

- **Get**: Ruft den Wert ab, der einem Schlüssel zugeordnet ist.
  ```java
  byte[] value = db.get("key".getBytes());
  if (value != null) {
      System.out.println(new String(value));  // Gibt "value" aus
  } else {
      System.out.println("Key not found");
  }
  ```

- **Delete**: Entfernt ein Schlüssel-Wert-Paar.
  ```java
  db.delete("key".getBytes());
  ```

---

### 5. **Datenbank schließen**
Das ordnungsgemäße Schließen der Datenbank ist entscheidend, um Ressourcen freizugeben. Der einfachste Weg ist die Verwendung eines try-with-resources-Blocks, der die Datenbank automatisch schließt, wenn Sie fertig sind:

```java
try (RocksDB db = RocksDB.open(options, "/pfad/zur/db")) {
    // Operationen hier durchführen
} catch (Exception e) {
    e.printStackTrace();
}
```

---

### 6. **Ausnahmen behandeln**
RocksDB-Operationen können `RocksDBException` auslösen, daher sollten Sie immer eine Ausnahmebehandlung einbinden, um Ressourcenlecks oder Datenbeschädigung zu verhindern:

```java
try {
    db.put("key".getBytes(), "value".getBytes());
} catch (RocksDBException e) {
    e.printStackTrace();
}
```

---

### 7. **Konfigurationsoptionen**
Sie können die Leistung von RocksDB mit der `Options`-Klasse feinabstimmen. Zum Beispiel:

```java
Options options = new Options()
    .setCreateIfMissing(true)
    .setWriteBufferSize(64 * 1024 * 1024);  // 64MB Schreibpuffer
```

Häufige Optionen sind:
- `setWriteBufferSize`: Steuert den für Schreibvorgänge verwendeten Speicher.
- `setMaxOpenFiles`: Begrenzt die Anzahl geöffneter Dateien.
- `setCompactionStyle`: Passt an, wie Daten auf der Festplatte kompaktiert werden.

Entdecken Sie die [RocksDB-Dokumentation](https://github.com/facebook/rocksdb/wiki) für weitere Optionen.

---

### 8. **Einfaches Beispiel**
Hier ist ein vollständiges Beispiel, das das Öffnen einer Datenbank, das Speichern eines Schlüssel-Wert-Paares und dessen Abruf demonstriert:

```java
import org.rocksdb.RocksDB;
import org.rocksdb.Options;

public class SimpleRocksDBExample {
    public static void main(String[] args) {
        RocksDB.loadLibrary();  // Native Bibliothek laden
        Options options = new Options().setCreateIfMissing(true);
        
        try (RocksDB db = RocksDB.open(options, "/tmp/rocksdb_example")) {
            // Schlüssel-Wert-Paar speichern
            db.put("hello".getBytes(), "world".getBytes());
            
            // Wert abrufen
            byte[] value = db.get("hello".getBytes());
            if (value != null) {
                System.out.println(new String(value));  // Gibt "world" aus
            } else {
                System.out.println("Key not found");
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
- **Byte-Arrays**: Schlüssel und Werte sind `byte[]`, daher müssen Sie die Serialisierung/Deserialisierung für komplexe Objekte handhaben.
- **Leistung**: RocksDB glänzt mit schnellem Speicher (z. B. SSDs) und wird in Hochleistungssystemen verwendet, wie z. B. bei Facebook, wo es entwickelt wurde.
- **Nicht relational**: Es handelt sich um einen Schlüssel-Wert-Speicher, nicht um eine relationale Datenbank – kein SQL oder Joins.

---

### Häufige Fallstricke
- **`RocksDB.loadLibrary()` vergessen**: Führt zu `UnsatisfiedLinkError`.
- **Unsachgemäße Ressourcenverwaltung**: Das Nicht-Schließen der Datenbank kann Probleme verursachen, insbesondere auf ressourcenbeschränkten Systemen.
- **Fehler bei Datentypen**: Direktes Übergeben von Zeichenketten oder Objekten anstatt der Konvertierung in `byte[]`.

---

### Weiterführende Schritte
- **Erweiterte Funktionen**: Erkunden Sie Transaktionen, Snapshots oder Column Families für komplexere Anwendungsfälle.
- **Ressourcen**: Besuchen Sie die [RocksDB Java-API](https://github.com/facebook/rocksdb/tree/main/java) und das [RocksDB Wiki](https://github.com/facebook/rocksdb/wiki) für detaillierte Dokumentation und Beispiele.

Diese Anleitung bietet eine solide Grundlage für die Verwendung von `org.rocksdb`. Wenn Sie Hilfe zu bestimmten Funktionen oder Anwendungsfällen benötigen, fragen Sie gerne!