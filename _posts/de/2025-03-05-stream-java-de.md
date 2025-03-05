---
audio: false
generated: true
lang: de
layout: post
title: Stream-API in Java
translated: true
---

Um `java.util.stream` in Java zu verwenden, können Sie die Stream-API, die in Java 8 eingeführt wurde, nutzen, um Sammlungen von Daten auf funktionale und deklarative Weise zu verarbeiten. Streams ermöglichen es Ihnen, Operationen wie Filtern, Abbilden und Reduzieren auf Sequenzen von Elementen (wie Listen oder Arrays) effizient und prägnant durchzuführen. Im Folgenden werde ich erklären, wie man `java.util.stream` verwendet, indem ich ein spezifisches Beispiel durchgehe: das Finden des Durchschnitts der geraden Zahlen größer als 10 aus einer Liste von Ganzzahlen. Dies wird die wichtigsten Stream-Operationen und -Konzepte demonstrieren.

---

### **Übersicht über `java.util.stream`**
Das Paket `java.util.stream` stellt die `Stream`-Schnittstelle und verwandte Klassen (wie `IntStream`, `DoubleStream` usw.) zur Verarbeitung von Daten bereit. Ein Stream ist eine Sequenz von Elementen, die Operationen unterstützt, die in einer Pipeline ausgeführt werden. Diese Operationen sind:
- **Zwischenoperationen**: Transformieren oder filtern den Stream (z.B. `filter`, `map`) und geben einen neuen Stream zurück. Diese sind träge und werden nur ausgeführt, wenn eine Endoperation aufgerufen wird.
- **Endoperationen**: Erzeugen ein Ergebnis oder eine Nebenwirkung (z.B. `average`, `collect`), wodurch die Pipeline veranlasst wird, die Daten zu verarbeiten.

Um Streams zu verwenden, tun Sie dies in der Regel:
1. Erstellen Sie einen Stream aus einer Datenquelle (z.B. einer Liste).
2. Wenden Sie Zwischenoperationen an, um die Daten zu transformieren oder zu filtern.
3. Verwenden Sie eine Endoperation, um ein Ergebnis zu erzeugen.

---

### **Beispielproblem**
Lösen wir dieses Problem: Gegeben sei eine `List<Integer>`, berechnen Sie den Durchschnitt aller geraden Zahlen größer als 10. Wenn keine solchen Zahlen existieren, geben Sie 0.0 zurück. Hier ist, wie man dies mit `java.util.stream` macht.

#### **Schritt-für-Schritt-Lösung**
1. **Stream erstellen**
   - Beginnen Sie mit einer `List<Integer>` (z.B. `List.of(1, 2, 12, 15, 20, 25, 30)`).
   - Verwenden Sie die `stream()`-Methode, um einen `Stream<Integer>` zu erstellen:
     ```java
     list.stream()
     ```

2. **Stream filtern**
   - Verwenden Sie die `filter`-Methode, um nur die Zahlen zu behalten, die gerade und größer als 10 sind.
   - Die `filter`-Methode nimmt ein `Predicate` (eine Funktion, die einen Boolean zurückgibt) als Lambda-Ausdruck entgegen:
     ```java
     .filter(number -> number % 2 == 0 && number > 10)
     ```
     - `number % 2 == 0` überprüft, ob eine Zahl gerade ist.
     - `number > 10` stellt sicher, dass die Zahl größer als 10 ist.
     - Für die Beispiel-Liste `[1, 2, 12, 15, 20, 25, 30]` behält dies `[12, 20, 30]`.

3. **In einen `IntStream` umwandeln**
   - Da `average()` auf primitiven Streams wie `IntStream` (nicht `Stream<Integer>`) verfügbar ist, wandeln Sie den `Stream<Integer>` mit `mapToInt` in einen `IntStream` um:
     ```java
     .mapToInt(i -> i)
     ```
     - `i -> i` entpackt jedes `Integer` zu einem `int`. Alternativ könnten Sie `Integer::intValue` verwenden.
     - Dies ergibt einen `IntStream` von `[12, 20, 30]`.

4. **Durchschnitt berechnen**
   - Verwenden Sie die `average()`-Methode auf `IntStream`, die ein `OptionalDouble` zurückgibt (da der Stream leer sein könnte):
     ```java
     .average()
     ```
     - Für `[12, 20, 30]` berechnet dies `(12 + 20 + 30) / 3 = 20.666...`.
     - Wenn der Stream leer ist, gibt es ein leeres `OptionalDouble`.

5. **Leeren Fall behandeln**
   - Verwenden Sie `orElse(0.0)` auf dem `OptionalDouble`, um 0.0 zurückzugeben, wenn keine Zahlen die Filterung bestehen:
     ```java
     .orElse(0.0)
     ```
     - Für `[12, 20, 30]` gibt dies `20.666...` zurück.
     - Für eine Liste wie `[1, 3, 5]` (keine geraden Zahlen > 10) gibt dies `0.0` zurück.

#### **Vollständiger Code**
Hier ist die vollständige Lösung als Methode:
```java
import java.util.List;

public class Main {
    public static double averageOfEvenGreaterThanTen(List<Integer> list) {
        return list.stream()
                   .filter(number -> number % 2 == 0 && number > 10)
                   .mapToInt(i -> i)
                   .average()
                   .orElse(0.0);
    }

    public static void main(String[] args) {
        // Testfälle
        System.out.println(averageOfEvenGreaterThanTen(List.of(1, 2, 12, 15, 20, 25, 30)));  // ~20.666
        System.out.println(averageOfEvenGreaterThanTen(List.of(1, 3, 5)));                    // 0.0
        System.out.println(averageOfEvenGreaterThanTen(List.of(12)));                         // 12.0
        System.out.println(averageOfEvenGreaterThanTen(List.of()));                           // 0.0
        System.out.println(averageOfEvenGreaterThanTen(List.of(10, 8, 6)));                   // 0.0
        System.out.println(averageOfEvenGreaterThanTen(List.of(11, 13, 14, 16)));             // 15.0
    }
}
```

---

### **Wichtige Merkmale von `java.util.stream` Demonstriert**
- **Verkettung**: Operationen werden in einem flüssigen Stil verkettet (z.B. `.filter().mapToInt().average()`).
- **Trägheit**: Zwischenoperationen (wie `filter` und `mapToInt`) werden nur ausgeführt, wenn die Endoperation (`average`) aufgerufen wird.
- **Primitive Streams**: `IntStream` stellt Methoden wie `average()` bereit, die für numerische Operationen optimiert sind und die Boxing-Overhead vermeiden.
- **Optional-Verarbeitung**: `OptionalDouble` behandelt Fälle, in denen kein Ergebnis existiert, wobei `orElse` einen Standardwert bereitstellt.

---

### **Alternative Vorgehensweise**
Sie könnten auch die `Collectors`-Klasse verwenden:
```java
import java.util.stream.Collectors;

double average = list.stream()
                     .filter(number -> number % 2 == 0 && number > 10)
                     .collect(Collectors.averagingInt(i -> i));
```
- Dies gibt einen `Double` direkt zurück und gibt `0.0` für einen leeren Stream zurück. Allerdings ist `mapToInt().average()` für diesen einfachen Fall direkter und stimmt mit der Verwendung von primitiven Streams überein.

---

### **Wann Streams verwenden**
- Verwenden Sie `java.util.stream` für prägnanten, lesbaren Code beim Verarbeiten von Sammlungen.
- Bei großen Datensätzen können Sie `parallelStream()` anstelle von `stream()` verwenden, um Parallelität zu nutzen, obwohl dies für kleine Listen aufgrund des Overheads übertrieben ist.

---

Dieses Beispiel zeigt, wie man `java.util.stream` verwendet, um ein praktisches Problem zu lösen. Sie können diese Schritte – Erstellen eines Streams, Filtern, Abbilden und Reduzieren – an andere Szenarien anpassen, wie benötigt!