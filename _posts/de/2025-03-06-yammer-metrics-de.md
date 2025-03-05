---
audio: false
generated: true
lang: de
layout: post
title: Anwendungsmetriken in Java
translated: true
---

Die `com.yammer.metrics`-Bibliothek, ursprünglich von Yammer entwickelt, ist jetzt Teil der **Dropwizard Metrics**-Bibliothek. Sie bietet eine robuste Möglichkeit, Anwendungsmetriken in Java zu sammeln und zu berichten, wodurch Sie Leistungsaspekte wie Anforderungsanzahlen, Antwortzeiten und mehr überwachen können. Im Folgenden finden Sie eine Anleitung zur effektiven Verwendung.

---

### Schritt 1: Abhängigkeit hinzufügen
Da `com.yammer.metrics` in Dropwizard Metrics übergegangen ist, sollten Sie die Dropwizard Metrics-Bibliothek verwenden. Wenn Sie Maven verwenden, fügen Sie die folgende Abhängigkeit zu Ihrer `pom.xml` hinzu:

```xml
<dependency>
    <groupId>io.dropwizard.metrics</groupId>
    <artifactId>metrics-core</artifactId>
    <version>4.2.0</version> <!-- Verwenden Sie die neueste verfügbare Version -->
</dependency>
```

Je nach Bedarf möchten Sie möglicherweise zusätzliche Module wie:
- `metrics-jvm` für JVM-bezogene Metriken.
- `metrics-httpclient` für HTTP-Client-Metriken.
- `metrics-jersey` für die Integration mit dem Jersey-Web-Framework.

Überprüfen Sie die [Dropwizard Metrics-Dokumentation](https://metrics.dropwizard.io/) auf die neueste Version und verfügbare Module.

---

### Schritt 2: Metrik-Registry erstellen
Die `MetricRegistry` ist der zentrale Ort, an dem alle Metriken gespeichert werden. Sie erstellen normalerweise eine Instanz für Ihre Anwendung:

```java
import com.codahale.metrics.MetricRegistry;

public class MyApplication {
    public static void main(String[] args) {
        MetricRegistry registry = new MetricRegistry();
    }
}
```

---

### Schritt 3: Verschiedene Metrik-Typen verwenden
Dropwizard Metrics unterstützt mehrere Metrik-Typen, die jeweils für unterschiedliche Überwachungsbedürfnisse geeignet sind:

#### **Zähler**
Zähler werden verwendet, um Werte zu verfolgen, die sich erhöhen oder verringern können (z. B. Anzahl der verarbeiteten Anfragen).

```java
import com.codahale.metrics.Counter;

Counter counter = registry.counter("requests.processed");
counter.inc();  // Erhöhen um 1
counter.inc(5); // Erhöhen um 5
counter.dec();  // Verringern um 1
```

#### **Messgeräte**
Messgeräte bieten einen Momentaufnahme eines Wertes zu einem bestimmten Zeitpunkt (z. B. aktuelle Warteschlangengröße). Sie definieren ein Messgerät, indem Sie die `Gauge`-Schnittstelle implementieren:

```java
import com.codahale.metrics.Gauge;

registry.register("queue.size", new Gauge<Integer>() {
    @Override
    public Integer getValue() {
        return someQueue.size(); // Ersetzen Sie durch Ihre Logik
    }
});
```

#### **Histogramme**
Histogramme verfolgen die statistische Verteilung von Werten (z. B. Anforderungsgrößen):

```java
import com.codahale.metrics.Histogram;

Histogram histogram = registry.histogram("request.sizes");
histogram.update(150); // Wert aufzeichnen
```

#### **Messgeräte**
Messgeräte messen die Rate von Ereignissen (z. B. Anfragen pro Sekunde):

```java
import com.codahale.metrics.Meter;

Meter meter = registry.meter("requests.rate");
meter.mark(); // Ereignis aufzeichnen
```

#### **Timer**
Timer messen sowohl die Rate als auch die Dauer von Ereignissen (z. B. Anforderungsverarbeitungszeit):

```java
import com.codahale.metrics.Timer;

Timer timer = registry.timer("request.duration");
Timer.Context context = timer.time();
try {
    // Simulieren Sie einige Arbeit
    Thread.sleep(100);
} finally {
    context.stop(); // Dauer aufzeichnen
}
```

---

### Schritt 4: Metriken berichten
Um Metriken nützlich zu machen, müssen Sie sie irgendwo berichten. Dropwizard Metrics unterstützt verschiedene Reporter wie Konsole, JMX oder Graphite. Hier ist ein Beispiel für einen Konsolenreporter, der Metriken alle 10 Sekunden protokolliert:

```java
import com.codahale.metrics.ConsoleReporter;
import java.util.concurrent.TimeUnit;

ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
    .convertRatesTo(TimeUnit.SECONDS)
    .convertDurationsTo(TimeUnit.MILLISECONDS)
    .build();
reporter.start(10, TimeUnit.SECONDS); // Berichten Sie alle 10 Sekunden
```

Für den Produktionsgebrauch sollten Sie die Integration mit Systemen wie Graphite in Betracht ziehen oder Metriken über JMX freigeben.

---

### Schritt 5: Integration mit Frameworks (optional)
Wenn Sie ein Web-Framework wie Jersey verwenden, können Sie das `metrics-jersey`-Modul verwenden, um Ihre Endpunkte automatisch zu instrumentieren. Zusätzlich können Annotationen wie `@Timed` oder `@Counted` die Metrikensammlung vereinfachen:

```java
import com.codahale.metrics.annotation.Timed;

@Path("/example")
public class ExampleResource {
    @GET
    @Timed
    public String getExample() {
        return "Hello, world!";
    }
}
```

Fügen Sie die `metrics-jersey`-Abhängigkeit hinzu und konfigurieren Sie sie mit Ihrer Jersey-Anwendung, um dieses Feature zu aktivieren.

---

### Best Practices
- **Benennungskonventionen**: Verwenden Sie ein hierarchisches Benennungsschema für Klarheit (z. B. `com.example.myapp.requests.total`).
- **Leistung**: Seien Sie vorsichtig mit der Anzahl und Häufigkeit der Metriken, da übermäßiges Sammeln die Leistung beeinträchtigen kann.
- **Dokumentation**: Verweisen Sie auf die [Dropwizard Metrics-Dokumentation](https://metrics.dropwizard.io/) für aktuelle Beispiele und erweiterte Funktionen.

---

### Beispiel: Alles zusammenfassen
Hier ist ein einfaches Beispiel, das mehrere Konzepte kombiniert:

```java
import com.codahale.metrics.*;
import java.util.concurrent.TimeUnit;

public class MetricsExample {
    public static void main(String[] args) throws InterruptedException {
        MetricRegistry registry = new MetricRegistry();

        // Erstellen Sie einen Zähler
        Counter counter = registry.counter("example.counter");
        counter.inc();

        // Erstellen Sie einen Timer
        Timer timer = registry.timer("example.timer");
        Timer.Context context = timer.time();
        Thread.sleep(100); // Simulieren Sie Arbeit
        context.stop();

        // Starten Sie einen Konsolenreporter
        ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
            .convertRatesTo(TimeUnit.SECONDS)
            .convertDurationsTo(TimeUnit.MILLISECONDS)
            .build();
        reporter.start(1, TimeUnit.SECONDS);

        // Halten Sie das Programm am Laufen, um Berichte zu sehen
        Thread.sleep(5000);
    }
}
```

Dieser Code verfolgt einen Zähler und einen Timer und berichtet die Ergebnisse alle Sekunden in der Konsole.

---

### Schlussbemerkungen
Die `com.yammer.metrics`-Bibliothek hat sich zu Dropwizard Metrics entwickelt, daher sollten Sie immer die neueste Version aus der Gruppe `io.dropwizard.metrics` verwenden. Wenn Sie ein neues Projekt starten, sollten Sie auch moderne Alternativen wie Micrometer in Betracht ziehen, aber Dropwizard Metrics bleibt eine solide Wahl für viele Java-Anwendungen. Für weitere Details überprüfen Sie die offizielle Dokumentation!