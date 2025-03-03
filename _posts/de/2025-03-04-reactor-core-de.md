---
audio: false
generated: true
lang: de
layout: post
title: Reaktive Programmierung in Java
translated: true
---

Um **reactor-core** zu verwenden, eine Java-Bibliothek zum Erstellen von nicht blockierenden, asynchronen Anwendungen basierend auf der Reactive Streams-Spezifikation, befolgen Sie diese Schritte:

---

### 1. reactor-core als Abhängigkeit hinzufügen
Zunächst fügen Sie **reactor-core** in Ihr Projekt ein. Abhängig von Ihrem Build-Tool:

- **Maven**: Fügen Sie dies zu Ihrer `pom.xml` hinzu:
  ```xml
  <dependency>
    <groupId>io.projectreactor</groupId>
    <artifactId>reactor-core</artifactId>
    <version>3.7.3</version>
  </dependency>
  ```

- **Gradle**: Fügen Sie dies zu Ihrer `build.gradle` hinzu:
  ```groovy
  implementation 'io.projectreactor:reactor-core:3.7.3'
  ```

Dadurch wird sichergestellt, dass die Bibliothek in Ihrem Projekt verfügbar ist. Überprüfen Sie die neueste Version auf [Maven Central](https://central.sonatype.com/artifact/io.projectreactor/reactor-core), falls erforderlich.

---

### 2. Die Kernkomponenten verstehen
Reactor-core stellt zwei Hauptklassen für die reaktive Programmierung bereit:
- **`Flux`**: Repräsentiert einen asynchronen Stream, der **0 bis N Elemente** emittieren kann.
- **`Mono`**: Repräsentiert einen asynchronen Stream, der **0 oder 1 Element** emittiert.

Diese sind die Bausteine, die Sie verwenden, um Daten reaktiv zu verarbeiten.

---

### 3. Ein Flux oder Mono erstellen
Sie können Instanzen von `Flux` oder `Mono` erstellen, um Ihre Datenströme darzustellen.

- **Beispiel mit Flux** (mehrere Elemente):
  ```java
  Flux<Integer> numbers = Flux.just(1, 2, 3, 4, 5);
  ```

- **Beispiel mit Mono** (einzelnes Element):
  ```java
  Mono<String> greeting = Mono.just("Hello, World!");
  ```

Die `just`-Methode ist eine einfache Möglichkeit, einen Stream aus statischen Werten zu erstellen, aber Reactor bietet viele andere Erstellungsmethoden (z.B. aus Arrays, Bereichen oder benutzerdefinierten Quellen).

---

### 4. Abonnieren, um die Daten zu verarbeiten
Um die emittierten Elemente zu konsumieren, müssen Sie sich bei dem `Flux` oder `Mono` **abonnieren**. Das Abonnieren löst die Ausführung des Streams aus, der mit dem Emittieren von Daten beginnt.

- **Abonnieren bei Flux**:
  ```java
  numbers.subscribe(System.out::println);  // Gibt aus: 1, 2, 3, 4, 5
  ```

- **Abonnieren bei Mono**:
  ```java
  greeting.subscribe(System.out::println); // Gibt aus: Hello, World!
  ```

Die `subscribe`-Methode kann auch zusätzliche Argumente wie Fehlerbehandler oder Abschluss-Callbacks enthalten, um mehr Kontrolle zu haben.

---

### 5. Daten mit Operatoren transformieren
Reactor stellt eine reichhaltige Sammlung von Operatoren zur Verfügung, um Streams zu manipulieren, wie z.B. `map`, `filter` und mehr.

- **Beispiel mit Flux und map**:
  ```java
  numbers.map(n -> n * 2).subscribe(System.out::println);  // Gibt aus: 2, 4, 6, 8, 10
  ```

- **Beispiel mit Mono und map**:
  ```java
  greeting.map(s -> s.toUpperCase()).subscribe(System.out::println); // Gibt aus: HELLO, WORLD!
  ```

Diese Operatoren ermöglichen es Ihnen, Daten deklarativ zu transformieren, zu filtern oder zu kombinieren.

---

### 6. Fehler und Backpressure behandeln
Reactor-core unterstützt Fehlerbehandlung und Backpressure-Management:
- **Fehlerbehandlung**: Verwenden Sie `subscribe` mit einem Fehlerverbraucher:
  ```java
  Flux.error(new RuntimeException("Oops!"))
      .subscribe(System.out::println, error -> System.err.println(error.getMessage()));
  // Gibt aus: Oops!
  ```
- **Backpressure**: Steuern Sie, wie Abonnenten überwältigende Datenströme mit Operatoren wie `onBackpressureBuffer()` oder `onBackpressureDrop()` verarbeiten.

---

### 7. Weiter erkunden
Für fortgeschrittene Nutzung:
- Überprüfen Sie die [offizielle Reactor-Dokumentation](https://projectreactor.io/docs/core/release/reference/) für detaillierte Beispiele und Tutorials.
- Schauen Sie sich das [reactor-core GitHub Repository](https://github.com/reactor/reactor-core) für zusätzliche Ressourcen an.

---

### Zusammenfassung
Um **reactor-core** zu verwenden:
1. Fügen Sie es als Abhängigkeit in Ihrem Projekt hinzu.
2. Verwenden Sie `Flux` für mehrere Elemente oder `Mono` für ein einzelnes Element.
3. Erstellen Sie Streams mit Methoden wie `just`.
4. Abonnieren Sie, um die Daten zu verarbeiten.
5. Wenden Sie Operatoren an, um die Streams nach Bedarf zu transformieren.

Dies ist ein anfängerfreundlicher Ausgangspunkt für die reaktive Programmierung mit reactor-core. Experimentieren Sie mit kleinen Beispielen, um sich mit seinem reaktiven Paradigma vertraut zu machen!