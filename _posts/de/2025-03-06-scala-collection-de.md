---
audio: false
generated: true
lang: de
layout: post
title: Verwendung der Scala-Sammlungsbibliothek in Java
translated: true
---

Um die `scala.collection`-Paket in Java zu verwenden, können Sie die Interoperabilität zwischen Scala und Java nutzen, da beide Sprachen zu JVM-Bytecode kompiliert werden. Dies ermöglicht es Java-Code, Scala-Klassen aufzurufen, einschließlich derjenigen im `scala.collection`-Paket, vorausgesetzt, die Scala-Bibliothek ist für Ihr Java-Projekt zugänglich. Hier ist eine Schritt-für-Schritt-Anleitung, um dies zu erreichen, einschließlich Erklärungen und Beispielen.

---

### **Schritt 1: Scala-Bibliothek in Ihr Java-Projekt einbinden**
Da das `scala.collection`-Paket Teil der Scala-Standardbibliothek ist, müssen Sie die Scala-Bibliothek in den Klassenspeicher Ihres Java-Projekts einbinden. Dies kann durch Hinzufügen der Scala-Bibliothek-Abhängigkeit zu Ihrem Build-Tool erfolgen:

- **Maven**:
  Fügen Sie Folgendes zu Ihrer `pom.xml` hinzu:
  ```xml
  <dependency>
      <groupId>org.scala-lang</groupId>
      <artifactId>scala-library</artifactId>
      <version>2.13.12</version> <!-- Verwenden Sie die Version, die Ihren Anforderungen entspricht -->
  </dependency>
  ```

- **Gradle**:
  Fügen Sie dies zu Ihrer `build.gradle` hinzu:
  ```gradle
  implementation 'org.scala-lang:scala-library:2.13.12'
  ```

Dadurch wird sichergestellt, dass Scala-Klassen, einschließlich derjenigen in `scala.collection`, für Ihren Java-Code verfügbar sind.

---

### **Schritt 2: Scala-Sammlungsklassen importieren**
Sobald die Scala-Bibliothek in Ihrem Klassenspeicher ist, können Sie spezifische Klassen aus dem `scala.collection`-Paket in Ihrem Java-Code importieren. Um beispielsweise Scala's unveränderliche `List` zu verwenden, würden Sie importieren:

```java
import scala.collection.immutable.List;
```

Andere häufig verwendete Sammlungen umfassen:
- `scala.collection.immutable.Set`
- `scala.collection.immutable.Map`
- `scala.collection.mutable.Buffer`

Beachten Sie, dass Scala-Sammlungen sowohl in veränderlicher als auch in unveränderlicher Form vorliegen, im Gegensatz zu Java-Sammlungen, die typischerweise veränderlich sind, es sei denn, sie werden umhüllt (z. B. über `Collections.unmodifiableList`).

---

### **Schritt 3: Scala-Sammlungen in Java erstellen**
Scala-Sammlungen werden in der Regel unter Verwendung von Begleitobjekten erstellt, die Fabrikmethoden wie `apply` bereitstellen. Da Java Scala-Syntax jedoch nicht direkt unterstützt (z. B. `List(1, 2, 3)`), müssen Sie diese Methoden explizit verwenden. Zusätzlich erwartet Scala's `apply`-Methode für Sammlungen wie `List` ein `Seq` als Argument, wenn sie von Java aufgerufen wird, aufgrund der Art und Weise, wie Scala's varargs kompiliert werden.

Um Java- und Scala-Sammlungen zu verbinden, verwenden Sie die von Scala bereitgestellten Konvertierungsdienste, wie `scala.collection.JavaConverters` (für Scala 2.12 und früher) oder `scala.jdk.CollectionConverters` (für Scala 2.13 und später). Hier ist, wie Sie eine Scala `List` aus einer Java `List` erstellen:

#### **Beispiel: Erstellen einer Scala-Liste**
```java
import scala.collection.immutable.List;
import scala.collection.Seq;
import scala.jdk.CollectionConverters;
import java.util.Arrays;

public class ScalaCollectionExample {
    public static void main(String[] args) {
        // Erstellen Sie eine Java-Liste
        java.util.List<Integer> javaList = Arrays.asList(1, 2, 3);

        // Konvertieren Sie die Java-Liste in eine Scala-Seq
        Seq<Integer> scalaSeq = CollectionConverters.asScala(javaList);

        // Erstellen Sie eine Scala-Liste unter Verwendung des Begleitobjekts
        List<Integer> scalaList = List$.MODULE$.apply(scalaSeq);

        // Drucken Sie die Scala-Liste
        System.out.println(scalaList); // Ausgabe: List(1, 2, 3)
    }
}
```

- **`CollectionConverters.asScala`**: Konvertiert eine Java `List` in eine Scala `Seq` (spezifisch ein `mutable.Buffer` in Scala 2.13, das ein Untertyp von `Seq` ist).
- **`List$.MODULE$`**: Greift auf die Singleton-Instanz des `List`-Begleitobjekts in Scala zu, sodass Sie seine `apply`-Methode aufrufen können.
- **`apply(scalaSeq)`**: Erstellt eine neue unveränderliche Scala `List` aus der `Seq`.

---

### **Schritt 4: Verwendung von Scala-Sammlungen**
Sobald Sie eine Scala-Sammlung in Java haben, können Sie deren Methoden verwenden. Beachten Sie jedoch die Unterschiede zwischen Scala und Java:
- **Unveränderlichkeit**: Viele Scala-Sammlungen (z. B. `scala.collection.immutable.List`) sind unveränderlich, was bedeutet, dass Methoden neue Sammlungen zurückgeben, anstatt die ursprüngliche zu ändern.
- **Typauslöschung**: Sowohl Scala als auch Java verwenden Typauslöschung, sodass Sie möglicherweise Ergebnisse beim Abrufen von Elementen gießen müssen.
- **Funktionale Methoden**: Scala-Sammlungen unterstützen funktionale Operationen wie `map`, `filter` usw., die Sie mit Java 8+-Lambdas verwenden können.

#### **Beispiel: Zugriff auf Elemente**
```java
// Holen Sie sich das erste Element
Integer head = (Integer) scalaList.head();
System.out.println("Head: " + head); // Ausgabe: Head: 1

// Holen Sie sich den Rest (alles außer dem Kopf)
List<Integer> tail = scalaList.tail();
System.out.println("Tail: " + tail); // Ausgabe: Tail: List(2, 3)
```

#### **Beispiel: Abbilden über eine Scala-Liste**
Verwenden Sie eine Lambda, um jedes Element zu verdoppeln:
```java
import scala.Function1;

Function1<Integer, Integer> doubler = x -> x * 2;
List<Integer> doubledList = scalaList.map(doubler);
System.out.println("Doubled: " + doubledList); // Ausgabe: Doubled: List(2, 4, 6)
```

Hier ist `Function1` ein Scala-Interface, das eine Funktion mit einem Argument darstellt, das mit der Java-Lambda-Syntax übereinstimmt.

---

### **Wichtige Überlegungen**
- **Typsicherheit**: Scala-Sammlungen sind parametrisiert, aber Rückgabetypen von Methoden können in Java aufgrund der Typauslöschung als `Object` erscheinen. Gießen Sie bei Bedarf (z. B. `(Integer) scalaList.head()`).
- **Leistung**: Das Überschreiten der Java-Scala-Grenze führt zu einigen Überkopfkosten, obwohl dies in der Regel gering ist.
- **Paradigmenwechsel**: Scala-Sammlungen betonen Unveränderlichkeit und funktionales Programmieren, was sich von Java's imperativem Stil unterscheiden kann. Zum Beispiel können Sie einer unveränderlichen `List` nichts hinzufügen – Sie erstellen eine neue (z. B. unter Verwendung von `:+` zum Anhängen, was eine neue `List` zurückgibt).
- **Versionskompatibilität**: Stellen Sie sicher, dass die Scala-Bibliothek-Version Ihren Anforderungen entspricht. Für Scala 2.13+ verwenden Sie `scala.jdk.CollectionConverters`; für 2.12 oder früher verwenden Sie `scala.collection.JavaConverters`.

---

### **Zusammenfassung**
Sie können das `scala.collection`-Paket in Java verwenden, indem Sie:
1. Die Scala-Bibliothek zum Klassenspeicher Ihres Projekts hinzufügen (z. B. über Maven oder Gradle).
2. Die gewünschten Scala-Sammlungsklassen importieren (z. B. `scala.collection.immutable.List`).
3. Scala-Sammlungen unter Verwendung von Begleitobjekten (z. B. `List$.MODULE$.apply`) erstellen und Java-Sammlungen in Scala `Seq` mit `CollectionConverters` konvertieren.
4. Die Sammlungen mit Scala-Methoden manipulieren, wobei Sie bei Bedarf Güsse und Lambdas verwenden.

Dieser Ansatz ermöglicht es Ihnen, die leistungsstarke Sammlungsbibliothek von Scala in Java zu nutzen, wie z. B. ihre unveränderlichen Datenstrukturen oder funktionalen Operationen, während Sie innerhalb des Java-Ökosystems arbeiten.