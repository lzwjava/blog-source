---
audio: false
generated: true
lang: de
layout: post
title: Anwendungsmetriken in Java
translated: true
type: note
---

Die `com.yammer.metrics`-Bibliothek, ursprünglich von Yammer entwickelt, ist jetzt Teil der **Dropwizard Metrics**-Bibliothek. Sie bietet eine robuste Möglichkeit, Anwendungsmetriken in Java zu sammeln und zu berichten, und hilft Ihnen, Leistungsaspekte wie Anforderungszahlen, Antwortzeiten und mehr zu überwachen. Im Folgenden finden Sie eine Anleitung zur effektiven Nutzung.

---

### Schritt 1: Fügen Sie die Abhängigkeit hinzu
Da `com.yammer.metrics` sich zu Dropwizard Metrics weiterentwickelt hat, sollten Sie die Dropwizard Metrics-Bibliothek verwenden. Wenn Sie Maven verwenden, fügen Sie die folgende Abhängigkeit zu Ihrer `pom.xml` hinzu:

```xml
<dependency>
    <groupId>io.dropwizard.metrics</groupId>
    <artifactId>metrics-core</artifactId>
    <version>4.2.0</version> <!-- Verwenden Sie die neueste verfügbare Version -->
</dependency>
```

Je nach Bedarf möchten Sie möglicherweise auch zusätzliche Module hinzufügen, wie zum Beispiel:
- `metrics-jvm` für JVM-bezogene Metriken.
- `metrics-httpclient` für HTTP-Client-Metriken.
- `metrics-jersey` für die Integration mit dem Jersey Web Framework.

Überprüfen Sie die [Dropwizard Metrics-Dokumentation](https://metrics.dropwizard.io/) auf die neueste Version und verfügbare Module.

---

### Schritt 2: Erstellen Sie eine Metric Registry
Die `MetricRegistry` ist die zentrale Stelle, an der alle Metriken gespeichert werden. Sie erstellen typischerweise eine Instanz für Ihre Anwendung:

```java
import com.codahale.metrics.MetricRegistry;

public class MyApplication {
    public static void main(String[] args) {
        MetricRegistry registry = new MetricRegistry();
    }
}
```

---

### Schritt 3: Verwenden Sie verschiedene Arten von Metriken
Dropwizard Metrics unterstützt mehrere Arten von Metriken, die jeweils für unterschiedliche Überwachungsanforderungen geeignet sind:

#### **Counter**
Counter werden verwendet, um Werte zu verfolgen, die steigen oder fallen können (z. B. die Anzahl der verarbeiteten Anfragen).

```java
import com.codahale.metrics.Counter;

Counter counter = registry.counter("requests.processed");
counter.inc();  // Um 1 erhöhen
counter.inc(5); // Um 5 erhöhen
counter.dec();  // Um 1 verringern
```

#### **Gauges**
Gauges liefern eine Momentaufnahme eines Wertes zu einem bestimmten Zeitpunkt (z. B. die aktuelle Warteschlangengröße). Sie definieren einen Gauge durch die Implementierung des `Gauge`-Interface:

```java
import com.codahale.metrics.Gauge;

registry.register("queue.size", new Gauge<Integer>() {
    @Override
    public Integer getValue() {
        return someQueue.size(); // Ersetzen Sie dies durch Ihre Logik
    }
});
```

#### **Histograms**
Histograms verfolgen die statistische Verteilung von Werten (z. B. Anforderungsgrößen):

```java
import com.codahale.metrics.Histogram;

Histogram histogram = registry.histogram("request.sizes");
histogram.update(150); // Einen Wert aufzeichnen
```

#### **Meters**
Meters messen die Rate von Ereignissen (z. B. Anfragen pro Sekunde):

```java
import com.codahale.metrics.Meter;

Meter meter = registry.meter("requests.rate");
meter.mark(); // Ein Ereignis aufzeichnen
```

#### **Timers**
Timers messen sowohl die Rate als auch die Dauer von Ereignissen (z. B. Anforderungsverarbeitungszeit):

```java
import com.codahale.metrics.Timer;

Timer timer = registry.timer("request.duration");
Timer.Context context = timer.time();
try {
    // Simulieren Sie einige Arbeiten
    Thread.sleep(100);
} finally {
    context.stop(); // Die Dauer aufzeichnen
}
```

---

### Schritt 4: Melden Sie Metriken
Um Metriken nutzbar zu machen, müssen Sie sie an einem Ort melden. Dropwizard Metrics unterstützt verschiedene Reporter, wie z. B. Konsole, JMX oder Graphite. Hier ist ein Beispiel für einen Konsolen-Reporter, der Metriken alle 10 Sekunden protokolliert:

```java
import com.codahale.metrics.ConsoleReporter;
import java.util.concurrent.TimeUnit;

ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
    .convertRatesTo(TimeUnit.SECONDS)
    .convertDurationsTo(TimeUnit.MILLISECONDS)
    .build();
reporter.start(10, TimeUnit.SECONDS); // Alle 10 Sekunden berichten
```

Für den Produktionseinsatz sollten Sie die Integration mit Systemen wie Graphite oder das Bereitstellen von Metriken über JMX in Betracht ziehen.

---

### Schritt 5: Integrieren Sie in Frameworks (Optional)
Wenn Sie ein Web-Framework wie Jersey verwenden, können Sie das Modul `metrics-jersey` verwenden, um Ihre Endpunkte automatisch zu instrumentieren. Zusätzlich können Annotationen wie `@Timed` oder `@Counted` die Metrik-Sammlung vereinfachen:

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

Fügen Sie die `metrics-jersey`-Abhängigkeit hinzu und konfigurieren Sie sie mit Ihrer Jersey-Anwendung, um diese Funktion zu aktivieren.

---

### Best Practices
- **Namenskonventionen**: Verwenden Sie ein hierarchisches Namensschema für Klarheit (z. B. `com.example.myapp.requests.total`).
- **Leistung**: Seien Sie vorsichtig mit der Anzahl und Häufigkeit der Metriken, da übermäßige Sammlung die Leistung beeinträchtigen kann.
- **Dokumentation**: Konsultieren Sie die [Dropwizard Metrics-Dokumentation](https://metrics.dropwizard.io/) für aktuelle Beispiele und erweiterte Funktionen.

---

### Beispiel: Alles zusammenfügen
Hier ist ein einfaches Beispiel, das mehrere Konzepte kombiniert:

```java
import com.codahale.metrics.*;
import java.util.concurrent.TimeUnit;

public class MetricsExample {
    public static void main(String[] args) throws InterruptedException {
        MetricRegistry registry = new MetricRegistry();

        // Einen Counter erstellen
        Counter counter = registry.counter("example.counter");
        counter.inc();

        // Einen Timer erstellen
        Timer timer = registry.timer("example.timer");
        Timer.Context context = timer.time();
        Thread.sleep(100); // Arbeit simulieren
        context.stop();

        // Einen Konsolen-Reporter starten
        ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
            .convertRatesTo(TimeUnit.SECONDS)
            .convertDurationsTo(TimeUnit.MILLISECONDS)
            .build();
        reporter.start(1, TimeUnit.SECONDS);

        // Das Programm laufen lassen, um Berichte zu sehen
        Thread.sleep(5000);
    }
}
```

Dieser Code verfolgt einen Counter und einen Timer und meldet die Ergebnisse jede Sekunde an die Konsole.

---

### Abschließende Hinweise
Die `com.yammer.metrics`-Bibliothek hat sich zu Dropwizard Metrics weiterentwickelt, verwenden Sie daher immer die neueste Version aus der Gruppe `io.dropwizard.metrics`. Wenn Sie ein neues Projekt starten, könnten Sie auch moderne Alternativen wie Micrometer erkunden, aber Dropwizard Metrics bleibt eine solide Wahl für viele Java-Anwendungen. Weitere Details finden Sie in der offiziellen Dokumentation!