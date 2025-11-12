---
audio: false
generated: true
lang: de
layout: post
title: Verwendung von Scalas Sammlungsbibliothek in Java
translated: true
type: note
---

Um das `scala.collection`-Paket in Java zu verwenden, können Sie die Interoperabilität zwischen Scala und Java nutzen, da beide Sprachen in JVM-Bytecode kompiliert werden. Dies ermöglicht es Java-Code, Scala-Klassen aufzurufen, einschließlich derjenigen im `scala.collection`-Paket, vorausgesetzt die Scala-Bibliothek ist für Ihr Java-Projekt zugänglich. Nachfolgend finden Sie eine Schritt-für-Schritt-Anleitung, um dies zu erreichen, komplett mit Erklärungen und Beispielen.

---

### **Schritt 1: Fügen Sie die Scala-Bibliothek zu Ihrem Java-Projekt hinzu**
Da das `scala.collection`-Paket Teil der Scala-Standardbibliothek ist, müssen Sie die Scala-Bibliothek in den Classpath Ihres Java-Projekts aufnehmen. Dies kann durch Hinzufügen der Scala-Bibliotheksabhängigkeit zu Ihrem Build-Tool erfolgen:

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

Dies stellt sicher, dass Scala-Klassen, einschließlich derer in `scala.collection`, für Ihren Java-Code verfügbar sind.

---

### **Schritt 2: Importieren Sie Scala Collection-Klassen**
Sobald sich die Scala-Bibliothek in Ihrem Classpath befindet, können Sie spezifische Klassen aus dem `scala.collection`-Paket in Ihrem Java-Code importieren. Um beispielsweise Scalas immutable `List` zu verwenden, würden Sie importieren:

```java
import scala.collection.immutable.List;
```

Andere häufig verwendete Collections sind:
- `scala.collection.immutable.Set`
- `scala.collection.immutable.Map`
- `scala.collection.mutable.Buffer`

Beachten Sie, dass Scala-Collections sowohl in mutable als auch immutable Varianten vorliegen, anders als Javas Collections, die typischerweise mutable sind, es sei denn, sie werden verpackt (z.B. via `Collections.unmodifiableList`).

---

### **Schritt 3: Erstellen von Scala-Collections in Java**
Scala-Collections werden typischerweise mit Companion-Objekten erstellt, die Factory-Methoden wie `apply` bereitstellen. Da Java Scalas Syntax jedoch nicht direkt unterstützt (z.B. `List(1, 2, 3)`), müssen Sie explizit mit diesen Methoden arbeiten. Zusätzlich erwartet Scalas `apply`-Methode für Collections wie `List` bei Aufruf aus Java ein `Seq` als Argument, aufgrund der Art und Weise, wie Scalas Varargs kompiliert werden.

Um Java- und Scala-Collections zu verbinden, verwenden Sie die von Scala bereitgestellten Konvertierungs-Hilfsprogramme, wie `scala.collection.JavaConverters` (für Scala 2.12 und früher) oder `scala.jdk.CollectionConverters` (für Scala 2.13 und später). So erstellen Sie eine Scala `List` aus einer Java `List`:

#### **Beispiel: Erstellen einer Scala List**
```java
import scala.collection.immutable.List;
import scala.collection.Seq;
import scala.jdk.CollectionConverters;
import java.util.Arrays;

public class ScalaCollectionExample {
    public static void main(String[] args) {
        // Erstellen einer Java List
        java.util.List<Integer> javaList = Arrays.asList(1, 2, 3);

        // Konvertieren der Java List in ein Scala Seq
        Seq<Integer> scalaSeq = CollectionConverters.asScala(javaList);

        // Erstellen einer Scala List unter Verwendung des Companion-Objekts
        List<Integer> scalaList = List$.MODULE$.apply(scalaSeq);

        // Ausgeben der Scala List
        System.out.println(scalaList); // Ausgabe: List(1, 2, 3)
    }
}
```

- **`CollectionConverters.asScala`**: Konvertiert eine Java `List` in ein Scala `Seq` (genauer gesagt ein `mutable.Buffer` in Scala 2.13, welches ein Subtyp von `Seq` ist).
- **`List$.MODULE$`**: Greift auf die Singleton-Instanz des `List` Companion-Objekts in Scala zu, um dessen `apply`-Methode aufzurufen.
- **`apply(scalaSeq)`**: Erstellt eine neue immutable Scala `List` aus dem `Seq`.

---

### **Schritt 4: Verwenden von Scala-Collections**
Sobald Sie eine Scala-Collection in Java haben, können Sie deren Methoden verwenden. Beachten Sie jedoch die Unterschiede zwischen Scala und Java:
- **Immutability**: Viele Scala-Collections (z.B. `scala.collection.immutable.List`) sind immutable, was bedeutet, dass Methoden neue Collections zurückgeben, anstatt die ursprüngliche zu modifizieren.
- **Type Erasure**: Sowohl Scala als auch Java verwenden Type Erasure, daher müssen Sie Ergebnisse möglicherweise casten, wenn Sie Elemente abrufen.
- **Funktionale Methoden**: Scala-Collections unterstützen funktionale Operationen wie `map`, `filter` etc., die Sie mit Java 8+ Lambdas verwenden können.

#### **Beispiel: Zugreifen auf Elemente**
```java
// Das erste Element holen
Integer head = (Integer) scalaList.head();
System.out.println("Head: " + head); // Ausgabe: Head: 1

// Den Rest holen (alles außer dem Kopf)
List<Integer> tail = scalaList.tail();
System.out.println("Tail: " + tail); // Ausgabe: Tail: List(2, 3)
```

#### **Beispiel: Mapping über eine Scala List**
Verwenden eines Lambdas, um jedes Element zu verdoppeln:
```java
import scala.Function1;

Function1<Integer, Integer> doubler = x -> x * 2;
List<Integer> doubledList = scalaList.map(doubler);
System.out.println("Doubled: " + doubledList); // Ausgabe: Doubled: List(2, 4, 6)
```

Hier ist `Function1` ein Scala-Interface, das eine Funktion mit einem Argument repräsentiert, was mit Javas Lambda-Syntax kompatibel ist.

---

### **Wichtige Überlegungen**
- **Type Safety**: Scala-Collections sind parametrisiert, aber Methodenrückgabetypen können in Java aufgrund von Type Erasure als `Object` erscheinen. Casten Sie bei Bedarf (z.B. `(Integer) scalaList.head()`).
- **Performance**: Das Überschreiten der Java-Scala-Grenze verursacht einen gewissen Overhead, der jedoch typischerweise gering ist.
- **Paradigmenwechsel**: Scala-Collections betonen Immutability und funktionale Programmierung, was sich von Javas imperativem Stil unterscheiden kann. Beispielsweise können Sie nicht zu einer immutable `List` "hinzufügen" – Sie erstellen stattdessen eine neue (z.B. unter Verwendung von `:+` zum Anhängen, was eine neue `List` zurückgibt).
- **Versionskompatibilität**: Stellen Sie sicher, dass die Version der Scala-Bibliothek Ihren Anforderungen entspricht. Für Scala 2.13+ verwenden Sie `scala.jdk.CollectionConverters`; für 2.12 oder früher verwenden Sie `scala.collection.JavaConverters`.

---

### **Zusammenfassung**
Sie können das `scala.collection`-Paket in Java verwenden, indem Sie:
1. Die Scala-Bibliothek zum Classpath Ihres Projekts hinzufügen (z.B. via Maven oder Gradle).
2. Die gewünschten Scala Collection-Klassen importieren (z.B. `scala.collection.immutable.List`).
3. Scala-Collections unter Verwendung von Companion-Objekten (z.B. `List$.MODULE$.apply`) erstellen und Java-Collections mit `CollectionConverters` zu Scala `Seq` konvertieren.
4. Die Collections mit Scala-Methoden manipulieren und dabei Casts und Lambdas nach Bedarf verwenden.

Dieser Ansatz ermöglicht es Ihnen, die leistungsstarke Collection-Bibliothek von Scala in Java zu nutzen, wie z.B. ihre immutable Datenstrukturen oder funktionalen Operationen, während Sie in Javas Ökosystem arbeiten.