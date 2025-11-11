---
audio: false
generated: true
lang: de
layout: post
title: Reaktive Programmierung in Java
translated: true
type: note
---

Um **reactor-core** zu verwenden, eine Java-Bibliothek zum Erstellen von nicht-blockierenden, asynchronen Anwendungen basierend auf der Reactive Streams-Spezifikation, befolgen Sie diese Schritte:

---

### 1. reactor-core als Abhängigkeit hinzufügen
Fügen Sie zunächst **reactor-core** zu Ihrem Projekt hinzu. Abhängig von Ihrem Build-Tool:

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

Dies stellt sicher, dass die Bibliothek in Ihrem Projekt verfügbar ist. Überprüfen Sie bei Bedarf die neueste Version auf [Maven Central](https://central.sonatype.com/artifact/io.projectreactor/reactor-core).

---

### 2. Die Kernkomponenten verstehen
Reactor-core bietet zwei Hauptklassen für reaktive Programmierung:
- **`Flux`**: Stellt einen asynchronen Stream dar, der **0 bis N Elemente** emittieren kann.
- **`Mono`**: Stellt einen asynchronen Stream dar, der **0 oder 1 Element** emittiert.

Dies sind die Bausteine, die Sie verwenden werden, um Daten reaktiv zu verarbeiten.

---

### 3. Einen Flux oder Mono erstellen
Sie können Instanzen von `Flux` oder `Mono` erstellen, um Ihre Datenströme darzustellen.

- **Beispiel mit Flux** (mehrere Elemente):
  ```java
  Flux<Integer> zahlen = Flux.just(1, 2, 3, 4, 5);
  ```

- **Beispiel mit Mono** (einzelnes Element):
  ```java
  Mono<String> begruessung = Mono.just("Hello, World!");
  ```

Die `just`-Methode ist eine einfache Möglichkeit, einen Stream aus statischen Werten zu erstellen, aber Reactor bietet viele andere Erstellungsmethoden (z. B. aus Arrays, Bereichen oder benutzerdefinierten Quellen).

---

### 4. Abonnieren, um die Daten zu verarbeiten
Um die emittierten Elemente zu konsumieren, müssen Sie den `Flux` oder `Mono` **abonnieren**. Das Abonnieren löst aus, dass der Stream beginnt, Daten zu emittieren.

- **Flux abonnieren**:
  ```java
  zahlen.subscribe(System.out::println);  // Gibt aus: 1, 2, 3, 4, 5
  ```

- **Mono abonnieren**:
  ```java
  begruessung.subscribe(System.out::println); // Gibt aus: Hello, World!
  ```

Die `subscribe`-Methode kann auch zusätzliche Argumente nehmen, wie Fehlerbehandler oder Abschluss-Callbacks, für mehr Kontrolle.

---

### 5. Daten mit Operatoren transformieren
Reactor bietet einen umfangreichen Satz an Operatoren, um Ströme zu manipulieren, wie z.B. `map`, `filter` und mehr.

- **Beispiel mit Flux und map**:
  ```java
  zahlen.map(n -> n * 2).subscribe(System.out::println);  // Gibt aus: 2, 4, 6, 8, 10
  ```

- **Beispiel mit Mono und map**:
  ```java
  begruessung.map(s -> s.toUpperCase()).subscribe(System.out::println); // Gibt aus: HELLO, WORLD!
  ```

Diese Operatoren ermöglichen es Ihnen, Daten auf deklarative Weise zu transformieren, filtern oder zu kombinieren.

---

### 6. Fehler und Backpressure behandeln
Reactor-core unterstützt Fehlerbehandlung und Backpressure-Management:
- **Fehlerbehandlung**: Verwenden Sie `subscribe` mit einem Error-Consumer:
  ```java
  Flux.error(new RuntimeException("Hoppla!"))
      .subscribe(System.out::println, error -> System.err.println(error.getMessage()));
  // Gibt aus: Hoppla!
  ```
- **Backpressure**: Steuern Sie, wie Abonnenten überwältigende Datenströme behandeln, mit Operatoren wie `onBackpressureBuffer()` oder `onBackpressureDrop()`.

---

### 7. Weitere Erkundungen
Für fortgeschrittenere Verwendungen:
- Lesen Sie die [offizielle Reactor-Dokumentation](https://projectreactor.io/docs/core/release/reference/) für detaillierte Beispiele und Tutorials.
- Sehen Sie sich das [reactor-core GitHub-Repository](https://github.com/reactor/reactor-core) für zusätzliche Ressourcen an.

---

### Zusammenfassung
Um **reactor-core** zu verwenden:
1. Fügen Sie es als Abhängigkeit in Ihrem Projekt hinzu.
2. Verwenden Sie `Flux` für mehrere Elemente oder `Mono` für ein einzelnes Element.
3. Erstellen Sie Ströme mit Methoden wie `just`.
4. Abonnieren Sie, um die Daten zu verarbeiten.
5. Wenden Sie Operatoren an, um die Ströme nach Bedarf zu transformieren.

Dies ist ein einsteigerfreundlicher Ausgangspunkt für die reaktive Programmierung mit reactor-core. Experimentieren Sie mit kleinen Beispielen, um sich mit seinem reaktiven Paradigma vertraut zu machen!