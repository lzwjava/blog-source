---
audio: false
generated: true
lang: de
layout: post
title: Objekt-Serialisierung in Java
translated: true
type: note
---

Ich nehme an, Sie meinten "java.io.Serializable" - eine wichtige Schnittstelle in Java, die für die Objektserialisierung verwendet wird. Hier ist eine praktische Anleitung zur Verwendung:

### Was ist Serializable?
`java.io.Serializable` ist eine Marker-Schnittstelle (keine zu implementierenden Methoden), die der Java-Laufzeitumgebung mitteilt, dass eine Klasse serialisiert werden kann - in einen Bytestrom umgewandelt, um in einer Datei gespeichert, über ein Netzwerk gesendet oder in einer Datenbank gespeichert zu werden, und später wieder in ein Objekt deserialisiert zu werden.

### Grundlegende Schritte zur Verwendung von Serializable

1. **Die Schnittstelle implementieren**
   Fügen Sie `implements Serializable` zu Ihrer Klasse hinzu. Das ist die Mindestanforderung.

   ```java
   import java.io.Serializable;

   public class Person implements Serializable {
       private String name;
       private int age;

       // Konstruktor
       public Person(String name, int age) {
           this.name = name;
           this.age = age;
       }

       // Getter und Setter
       public String getName() { return name; }
       public void setName(String name) { this.name = name; }
       public int getAge() { return age; }
       public void setAge(int age) { this.age = age; }

       @Override
       public String toString() {
           return "Person{name='" + name + "', age=" + age + "}";
       }
   }
   ```

2. **Serialisierung - Das Objekt schreiben**
   Verwenden Sie `ObjectOutputStream`, um das Objekt in eine Datei oder einen Stream zu schreiben.

   ```java
   import java.io.FileOutputStream;
   import java.io.ObjectOutputStream;
   import java.io.IOException;

   public class SerializeExample {
       public static void main(String[] args) {
           Person person = new Person("Alice", 25);

           try (FileOutputStream fileOut = new FileOutputStream("person.ser");
                ObjectOutputStream out = new ObjectOutputStream(fileOut)) {
               out.writeObject(person);
               System.out.println("Serialisierte Daten sind in person.ser gespeichert");
           } catch (IOException e) {
               e.printStackTrace();
           }
       }
   }
   ```

3. **Deserialisierung - Das Objekt lesen**
   Verwenden Sie `ObjectInputStream`, um das Objekt zurückzulesen.

   ```java
   import java.io.FileInputStream;
   import java.io.ObjectInputStream;
   import java.io.IOException;

   public class DeserializeExample {
       public static void main(String[] args) {
           try (FileInputStream fileIn = new FileInputStream("person.ser");
                ObjectInputStream in = new ObjectInputStream(fileIn)) {
               Person person = (Person) in.readObject();
               System.out.println("Deserialisierte Person: " + person);
           } catch (IOException | ClassNotFoundException e) {
               e.printStackTrace();
           }
       }
   }
   ```

### Wichtige Punkte zu beachten

- **serialVersionUID**: Um Kompatibilität während der Deserialisierung sicherzustellen, definieren Sie eine `serialVersionUID`. Wenn Sie keine definieren, generiert Java automatisch eine, diese kann jedoch zwischen JVMs oder bei Klassenänderungen variieren.

   ```java
   private static final long serialVersionUID = 1L;
   ```

   Fügen Sie dies zu Ihrer `Person`-Klasse hinzu.

- **Transiente Felder**: Felder, die mit `transient` markiert sind, werden nicht serialisiert.
   ```java
   private transient String temporaryData;
   ```

- **Nicht-serialisierbare Felder**: Wenn die Klasse eines Feldes `Serializable` nicht implementiert, erhalten Sie eine `NotSerializableException`. Machen Sie entweder diese Klasse `Serializable` oder markieren Sie das Feld als `transient`.

- **Vererbung**: Wenn eine Superklasse `Serializable` implementiert, sind Unterklassen ebenfalls serialisierbar. Wenn nicht, muss die Superklasse einen parameterlosen Konstruktor haben, damit die Deserialisierung funktioniert.

### Beispiel mit transient und serialVersionUID
```java
import java.io.Serializable;

public class Employee implements Serializable {
    private static final long serialVersionUID = 1L;
    private String name;
    private transient String password; // Wird nicht serialisiert
    private int id;

    public Employee(String name, String password, int id) {
        this.name = name;
        this.password = password;
        this.id = id;
    }

    @Override
    public String toString() {
        return "Employee{name='" + name + "', password='" + password + "', id=" + id + "}";
    }
}
```

### Testen
Serialisieren und deserialisieren Sie `Employee`. Sie werden feststellen, dass `password` nach der Deserialisierung `null` ist, weil es `transient` ist.

### Häufige Anwendungsfälle
- Speichern des Objektzustands in einer Datei (z.B. Spielstände).
- Senden von Objekten über ein Netzwerk (z.B. in RMI oder verteilten Systemen).
- Caching von Objekten.

### Fallstricke
- **Sicherheit**: Serialisierung kann private Felder offenlegen, wenn nicht sorgfältig gehandhabt. Erwägen Sie benutzerdefinierte `writeObject`- und `readObject`-Methoden für sensible Daten.
- **Leistung**: Serialisierung kann für komplexe Objekte langsam sein.
- **Versionierung**: Klassenänderungen (z.B. Hinzufügen von Feldern) können die Deserialisierung unterbrechen, es sei denn, `serialVersionUID` wird verwaltet.

### Benutzerdefinierte Serialisierung (Optional)
Wenn Sie Kontrolle über die Serialisierung benötigen, implementieren Sie diese Methoden:
```java
private void writeObject(ObjectOutputStream out) throws IOException {
    out.defaultWriteObject();
    // Benutzerdefinierte Logik
}

private void readObject(ObjectInputStream in) throws IOException, ClassNotFoundException {
    in.defaultReadObject();
    // Benutzerdefinierte Logik
}
```

Lassen Sie mich wissen, wenn Sie tiefer in einen bestimmten Teil einsteigen möchten!