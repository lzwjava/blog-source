---
audio: false
generated: true
lang: de
layout: post
title: 'Leitfaden für Mikrometer: Werkzeuge und Beobachtbarkeit'
translated: true
type: note
---

Dieser umfassende Leitfaden behandelt zwei verschiedene Themen: **Messschrauben (das Messwerkzeug)** und **Micrometer (die Observability-Fassade für Java-Anwendungen, insbesondere Spring Boot), mit Fokus auf Tracing-Lösungen.**

Lassen Sie uns diese aufschlüsseln:

-----

## Teil 1: Umfassender Leitfaden zu Messschrauben (Messwerkzeug)

Eine Messschraube, oft auch Mikrometerschraube genannt, ist ein Präzisionsmessinstrument, das verwendet wird, um hochgenaue Messungen kleiner Abstände zu erhalten, typischerweise im Bereich von Tausendstel Zoll oder Hundertstel Millimeter. Sie wird häufig im Ingenieurwesen, in der Metallbearbeitung, in der Fertigung und in wissenschaftlichen Bereichen eingesetzt, in denen präzise Abmessungen kritisch sind.

### 1. Was ist eine Messschraube?

Im Kern nutzt eine Messschraube einen präzise gefertigten Schraubenmechanismus, um eine Drehbewegung in eine lineare Bewegung umzuwandeln. Dies ermöglicht feine Einstellungen und genaue Ablesungen der Abmessungen eines Objekts, indem es zwischen einem festen Amboss und einer beweglichen Spindel eingeklemmt wird.

### 2. Wichtige Komponenten einer Messschraube:

*   **Bügel:** Der C-förmige Hauptkörper, der alle anderen Komponenten hält. Er sorgt für Stabilität und muss vorsichtig behandelt werden, um Fehler durch Wärmeausdehnung zu vermeiden.
*   **Amboss:** Die feststehende Messfläche, an der das Objekt platziert wird.
*   **Spindel:** Die bewegliche Messfläche, die sich beim Drehen des Schneidenrands auf den Amboss zu oder von ihm weg bewegt.
*   **Hülse (oder Skalenzylinder):** Der feststehende Teil der Messschraube, der die Hauptlinearskala beherbergt und ganze Zahlen und Halbeinheiten anzeigt (z. B. in Zoll oder Millimetern).
*   **Schneidenrand (oder Drehkranz):** Der drehbare Teil, der die Spindel bewegt und eine fein unterteilte Skala für präzisere Ablesungen hat.
*   **Ratsche:** Befindet sich am Ende des Schneidenrands und sorgt für einen konsistenten Messdruck, indem sie durchrutscht, wenn die richtige Kraft ausgeübt wird. Dies verhindert ein Überanziehen und eine Verformung des Werkstücks.
*   **Arretierung (oder Arretierhebel):** Wird verwendet, um die Spindel nach erfolgter Messung zu arretieren, um ein versehentliches Bewegen zu verhindern und die Ablesung zu sichern.

### 3. Arten von Messschrauben:

Messschrauben gibt es in verschiedenen Ausführungen, die jeweils für spezifische Messaufgaben konzipiert sind:

*   **Außenmessschraube (Extern):** Der gebräuchlichste Typ, verwendet für die Messung äußerer Abmessungen wie dem Durchmesser einer Welle oder der Dicke einer Platte.
*   **Innenmessschraube (Intern):** Wird zur Messung innerer Abmessungen verwendet, wie z. B. dem Durchmesser einer Bohrung oder eines Lochs. Sie haben oft unterschiedliche Designs, wie z. B. tubus- oder backenförmige Messschrauben.
*   **Tiefenmessschraube:** Wird verwendet, um die Tiefe von Löchern, Schlitzen oder Stufen zu messen.
*   **Gewindemessschraube:** Konzipiert zur Messung des Flankendurchmessers von Schraubengewinden.
*   **Kugelkopfmessschraube:** Verfügt über kugelförmige Ambosse/Spindeln zur Messung der Dicke gekrümmter Oberflächen oder spezifischer Merkmale wie Rohrwänden.
*   **Scheibenmessschraube:** Hat flache, scheibenförmige Messflächen zur Messung dünner Materialien, Papier oder Zahnradzähne.
*   **Digitale Messschraube:** Verfügt über eine elektronische Anzeige für direkte digitale Ablesungen, eliminiert Parallaxenfehler und erleichtert das Ablesen.
*   **Analoge Messschraube:** Erfordert das manuelle Ablesen der Skalen auf der Hülse und dem Schneidenrand.
*   **Messschraube mit Nonius:** Enthält eine zusätzliche Nonius-Skala für noch höhere Präzision, die Ablesungen über die Hauptteilungen des Schneidenrands hinaus ermöglicht.

### 4. Wie man eine Messschraube abliest (Analog/Imperial-Beispiel):

Während sich spezifische Ablesungen zwischen imperial (Zoll) und metrisch (Millimeter) sowie analog/digital unterscheiden, ist das allgemeine Prinzip für analoge Messschrauben:

1.  **Hülsen-Skala (Hauptskala) ablesen:**
    *   **Ganze Zoll:** Notieren Sie die größte sichtbare ganze Zoll-Markierung.
    *   **Zehntel Zoll (0.100"):** Jede nummerierte Linie auf der Hülse repräsentiert 0,100 Zoll.
    *   **Fünfundzwanzig Tausendstel (0.025"):** Jede unnummerierte Linie zwischen den Zehntel-Markierungen repräsentiert 0,025 Zoll.
2.  **Schneidenrand-Skala ablesen:**
    *   Der Schneidenrand hat 25 Teilungen, wobei jede Markierung 0,001 Zoll repräsentiert.
    *   Lesen Sie die Linie auf dem Schneidenrand ab, die mit der Indexlinie auf der Hülse übereinstimmt.
3.  **Ablesungen kombinieren:** Addieren Sie die Werte von der Hülse (ganze Zoll, Zehntel und fünfundzwanzig Tausendstel) und dem Schneidenrand (Tausendstel), um die endgültige Messung zu erhalten.

**Beispiel (Imperial):**

*   Hülse:
    *   Angenommen, Sie sehen "1" (für 1.000")
    *   Dann 3 Linien nach der "1" (3 x 0.100" = 0.300")
    *   Und 2 Linien unter der Hauptlinie (2 x 0.025" = 0.050")
    *   Gesamt von der Hülse: 1.000 + 0.300 + 0.050 = 1.350"
*   Schneidenrand:
    *   Die 15. Markierung auf dem Schneidenrand stimmt mit der Indexlinie überein (0.015")
*   **Gesamtablesung:** 1.350" + 0.015" = **1.365"**

### 5. Richtige Verwendung und Best Practices:

*   **Sauberkeit:** Stellen Sie immer sicher, dass die Messflächen (Amboss und Spindel) sauber und frei von Staub, Öl oder Schmutz sind.
*   **Nullpunkt-Einstellung:** Vor der Verwendung die Messschraube immer "nullen". Schließen Sie die Messflächen sanft mit der Ratsche, bis sie sich berühren. Die Anzeige sollte 0,000 (oder den Startbereich, z. B. 25-50 mm) betragen. Wenn nicht, stellen Sie die Messschraube auf Nullfehler ein. Digitale Messschrauben haben normalerweise eine Reset-Taste.
*   **Temperatur:** Handhaben Sie die Messschraube an ihrem isolierten Bügel oder tragen Sie Handschuhe, da Körperwärme eine thermische Ausdehnung verursachen und die Genauigkeit beeinträchtigen kann, insbesondere bei größeren Messschrauben. Lassen Sie sowohl das Werkzeug als auch das Objekt Raumtemperatur erreichen.
*   **Konsistenter Druck:** Verwenden Sie immer die Ratsche, um einen konsistenten und angemessenen Messdruck auszuüben. Übermäßiges Anziehen kann das Objekt oder die Messschraube verformen.
*   **Objektpositionierung:** Positionieren Sie das Objekt rechtwinklig zwischen Amboss und Spindel, um verzerrte Ablesungen zu vermeiden.
*   **Mehrfachmessungen:** Nehmen Sie für kritische Abmessungen mehrere Messungen an verschiedenen Punkten des Objekts vor, um Schwankungen zu berücksichtigen.
*   **Lagerung:** Bewahren Sie Messschrauben in ihren Schutzetuis auf, um Beschädigungen zu vermeiden.
*   **Kalibrierung:** Überprüfen und kalibrieren Sie Messschrauben regelmäßig gegen bekannte Standards (z. B. Endmaße), um ihre Genauigkeit sicherzustellen.

-----

## Teil 2: Micrometer als Tracing-Lösung für Spring Java-Projekte

Im Kontext von Spring Java-Projekten bezieht sich "Micrometer" auf eine **Application-Observability-Fassade**, die eine herstellerneutrale API zur Instrumentierung JVM-basierter Anwendungen bereitstellt. Sie ermöglicht das Sammeln und Exportieren verschiedener Telemetriedaten, einschließlich Metriken, Logging und **Distributed Tracing**.

Micrometer Tracing ist der Nachfolger von Spring Cloud Sleuth und wurde entwickelt, um Einblicke in komplexe verteilte Systeme zu ermöglichen, indem Anfragen über mehrere Dienste hinweg verfolgt werden.

### 1. Was ist Distributed Tracing?

In einer Microservices-Architektur durchläuft eine einzelne Benutzeranfrage oft mehrere Dienste. Distributed Tracing ermöglicht es Ihnen:

*   **Den Fluss zu verfolgen:** Sehen Sie den vollständigen Pfad, den eine Anfrage durch Ihr System nimmt.
*   **Engpässe zu identifizieren:** Lokalisieren Sie, welcher Dienst oder welche Operation Latenz verursacht.
*   **Abhängigkeiten zu verstehen:** Visualisieren Sie die Interaktionen zwischen verschiedenen Diensten.
*   **Debugging zu vereinfachen:** Korrelieren Sie Logs mit bestimmten Anfragen, was die Fehlerbehebung erheblich erleichtert.

Ein verteilter Trace setzt sich aus **Spans** zusammen. Ein **Span** repräsentiert eine einzelne Operation oder Arbeitseinheit innerhalb eines Traces (z. B. eine HTTP-Anfrage an einen Dienst, eine Datenbankabfrage, eine Methodenausführung). Spans haben eine eindeutige ID, eine Start- und Endzeit und können Tags (Schlüssel-Wert-Paare) und Events für zusätzliche Metadaten enthalten. Spans sind hierarchisch organisiert, mit Eltern-Kind-Beziehungen, und bilden einen Trace.

### 2. Micrometer Tracing in Spring Boot 3.x+

Spring Boot 3.x+ integriert sich tief mit Micrometers Observation API und Micrometer Tracing, was die Implementierung von Distributed Tracing erheblich erleichtert.

#### 2.1. Kernkonzepte:

*   **Observation API:** Die vereinheitlichte API von Micrometer zur Instrumentierung Ihres Codes, die in der Lage ist, Metriken, Traces und Logs von einem einzigen Instrumentierungspunkt aus zu erzeugen.
*   **Micrometer Tracing:** Eine Fassade über beliebten Tracer-Bibliotheken wie OpenTelemetry und OpenZipkin Brave. Es verwaltet den Lebenszyklus von Spans, Context Propagation und die Meldung an Tracing-Backends.
*   **Tracer Bridges:** Micrometer Tracing stellt "Bridges" bereit, um seine API mit spezifischen Tracing-Implementierungen zu verbinden (z. B. `micrometer-tracing-bridge-otel` für OpenTelemetry, `micrometer-tracing-bridge-brave` für OpenZipkin Brave).
*   **Reporter/Exporters:** Diese Komponenten senden die gesammelten Trace-Daten an ein Tracing-Backend (z. B. Zipkin, Jaeger, Grafana Tempo).

#### 2.2. Einrichten von Micrometer Tracing in einem Spring Boot Java-Projekt:

Hier ist eine Schritt-für-Schritt-Anleitung:

**Schritt 1: Abhängigkeiten hinzufügen**

Sie benötigen `spring-boot-starter-actuator` für Observability-Features, eine Micrometer Tracing Bridge und einen Reporter/Exporter für Ihr gewähltes Tracing-Backend.

**Beispiel mit OpenTelemetry und Zipkin (gängige Wahl):**

In Ihrer `pom.xml` (Maven):

```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>

    <dependency>
        <groupId>io.micrometer</groupId>
        <artifactId>micrometer-observation</artifactId>
    </dependency>

    <dependency>
        <groupId>io.micrometer</groupId>
        <artifactId>micrometer-tracing-bridge-otel</artifactId>
    </dependency>

    <dependency>
        <groupId>io.opentelemetry</groupId>
        <artifactId>opentelemetry-exporter-zipkin</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-webflux</artifactId>
    </dependency>
</dependencies>
```

**Schritt 2: Tracing-Eigenschaften konfigurieren**

In `application.properties` oder `application.yml` können Sie das Tracing-Verhalten konfigurieren.

```properties
# Tracing aktivieren (normalerweise standardmäßig true mit Actuator und Tracing-Abhängigkeiten)
management.tracing.enabled=true

# Sampling-Wahrscheinlichkeit konfigurieren (1.0 = 100% der Anfragen werden getraced)
# Standard ist oft 0.1 (10%), für Entwicklung/Test auf 1.0 setzen
management.tracing.sampling.probability=1.0

# Zipkin Basis-URL konfigurieren (falls Zipkin verwendet wird)
spring.zipkin.base-url=http://localhost:9411
```

**Schritt 3: Ein Tracing-Backend ausführen (z. B. Zipkin)**

Sie benötigen einen Tracing-Server, um Ihre Traces zu sammeln und zu visualisieren. Zipkin ist eine beliebte Wahl für die lokale Entwicklung.

Sie können Zipkin via Docker ausführen:

```bash
docker run -d -p 9411:9411 openzipkin/zipkin
```

Sobald es läuft, können Sie auf die Zipkin-UI unter `http://localhost:9411` zugreifen.

**Schritt 4: Automatische Instrumentierung (Spring Boot Magic!)**

Für viele gängige Komponenten in Spring Boot (wie `RestController`-Endpunkte, `RestTemplate`, `WebClient`, `JdbcTemplate`, Kafka-Listener/Producer, etc.) bietet Micrometer Tracing **automatische Instrumentierung**. Das bedeutet, dass Sie oft keinen expliziten Tracing-Code schreiben müssen, damit grundlegendes Request-Tracing funktioniert.

Spring Boot stellt sicher, dass:

*   Eingehende HTTP-Anfragen automatisch einen neuen Trace erstellen oder einen bestehenden fortsetzen, wenn Trace-Header vorhanden sind.
*   Ausgehende Anfragen, die mit automatisch konfiguriertem `RestTemplateBuilder`, `RestClient.Builder` oder `WebClient.Builder` gemacht werden, den Trace-Kontext an nachgelagerte Dienste weitergeben.
*   Log-Anweisungen automatisch `traceId` und `spanId` enthalten (wenn Sie Ihr Logging-Pattern konfigurieren).

**Beispiel Logging-Pattern (in `application.properties`):**

```properties
logging.pattern.level=%5p [${spring.application.name:},%X{traceId:-},%X{spanId:-}] %c{1.}:%M:%L - %m%n
```

Dieses Pattern fügt die `traceId` und `spanId` in Ihre Log-Zeilen ein, was es einfach macht, Logs mit einem bestimmten Trace zu korrelieren.

**Schritt 5: Manuelle Instrumentierung (für benutzerdefinierte Logik)**

Während die automatische Instrumentierung vieles abdeckt, möchten Sie oft spezifische Geschäftslogik oder kritische Operationen innerhalb Ihrer Anwendung nachverfolgen. Sie können dies tun mit:

*   **`@Observed` Annotation (Empfohlen für Spring Boot 3.x+):**
    Diese Annotation ist Teil der Micrometer Observation API und die bevorzugte Methode, um Observations zu erstellen (die sowohl Metriken als auch Traces erzeugen können).

    ```java
    import io.micrometer.observation.annotation.Observed;
    import org.springframework.stereotype.Service;

    @Service
    public class MyService {

        @Observed(name = "myService.processData", contextualName = "processing-data")
        public String processData(String input) {
            // ... Ihre Geschäftslogik ...
            System.out.println("Processing data: " + input);
            return "Processed: " + input;
        }
    }
    ```

    Das `name`-Attribut definiert den Namen für die Observation (der zum Metriknamen und Trace-Span-Namen wird). `contextualName` bietet einen besser lesbaren Namen für den Span in Tracing-Tools.

*   **Programmatische API (für mehr Kontrolle):**
    Sie können direkt die von Spring Boot bereitgestellten `ObservationRegistry`- und `Tracer`-Beans verwenden.

    ```java
    import io.micrometer.observation.Observation;
    import io.micrometer.observation.ObservationRegistry;
    import org.springframework.stereotype.Service;

    @Service
    public class AnotherService {

        private final ObservationRegistry observationRegistry;

        public AnotherService(ObservationRegistry observationRegistry) {
            this.observationRegistry = observationRegistry;
        }

        public String performComplexOperation(String id) {
            return Observation.createNotStarted("complex.operation", observationRegistry)
                    .lowCardinalityKeyValue("operation.id", id) // Einen Tag hinzufügen
                    .observe(() -> {
                        // ... komplexe Logik hier ...
                        try {
                            Thread.sleep(100); // Arbeit simulieren
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt();
                        }
                        return "Completed complex operation for " + id;
                    });
        }
    }
    ```

    Hier umschließt `observe()` den Codeblock, und `lowCardinalityKeyValue` fügt dem Span einen Tag hinzu.

### 3. Distributed Tracing in Microservices:

Wenn Sie mehrere Spring Boot-Dienste haben, erleichtert Micrometer Tracing die Context Propagation automatisch für `RestTemplate`, `WebClient` und andere instrumentierte Clients. Das bedeutet, dass die `traceId` und `spanId` in HTTP-Headern zwischen Diensten weitergegeben werden (z. B. `traceparent`-Header für W3C Trace Context).

Wenn eine Anfrage in einen nachgelagerten Dienst eingeht, erkennt Micrometer Tracing diese Header und setzt den bestehenden Trace fort, wobei neue Spans erstellt werden, die Kinder des Parent-Spans des aufrufenden Dienstes sind. Dies bildet den vollständigen End-to-End-Trace.

### 4. Visualisierung von Traces:

Sobald Ihre Anwendung instrumentiert ist und Traces an ein Backend wie Zipkin (oder Jaeger, Lightstep, etc.) sendet, können Sie:

1.  **Auf die UI zugreifen:** Gehen Sie zur Web-UI des Tracing-Backends (z. B. `http://localhost:9411` für Zipkin).
2.  **Traces finden:** Verwenden Sie Filter (Dienstname, Span-Name, Trace-ID), um bestimmte Traces zu finden.
3.  **Trace-Details analysieren:** Klicken Sie auf einen Trace, um seine Zeitleiste, einzelne Spans, deren Dauer, Tags und Events zu sehen.
4.  **Abhängigkeitsgraph:** Die meisten Tracing-Backends können die Dienstabhängigkeiten basierend auf den gesammelten Traces visualisieren.

### 5. Best Practices für Micrometer Tracing:

*   **Benennen Sie Ihre Spans aussagekräftig:** Verwenden Sie klare, prägnante und niedrig-kardinale Namen für Ihre Spans (z. B. "userService.getUser", "productService.updateStock"). Vermeiden Sie hochdynamische Daten in Span-Namen.
*   **Verwenden Sie Tags für Details (Hochkardinale Daten):** Anstatt dynamische Daten in Span-Namen zu packen, verwenden Sie Tags (Schlüssel-Wert-Paare) für zusätzlichen Kontext. Zum Beispiel `userId`, `orderId`, `customerType`. Seien Sie sich der **hohen Kardinalität** von Tags bewusst, da diese die Speicherkosten und Abfragezeiten in Ihrem Tracing-Backend erheblich erhöhen können. Verwenden Sie sie mit Bedacht.
*   **Halten Sie Spans granular, aber nicht übermäßig:** Erstellen Sie Spans für signifikante Operationen, aber vermeiden Sie zu viele winzige Spans, da dies Overhead verursachen kann. Streben Sie ein Gleichgewicht an, das ausreichende Einblicke bietet, ohne das System zu überlasten.
*   **Propagieren Sie den Kontext:** Stellen Sie sicher, dass der Trace-Kontext korrekt über Dienstgrenzen hinweg weitergegeben wird. Die Auto-Konfiguration von Spring Boot kümmert sich darum für gängige Szenarien, aber seien Sie sich bewusst, wenn Sie benutzerdefinierte Clients oder asynchrone Operationen verwenden.
*   **Sampling:** Erwägen Sie für Produktionsumgebungen mit hohem Verkehrsaufkommen Sampling-Strategien, um das Volumen der Trace-Daten, die an Ihr Backend gesendet werden, zu reduzieren. Spring Boot erlaubt die Konfiguration von `management.tracing.sampling.probability`.
*   **Korrelieren Sie Logs:** Nutzen Sie die in Logs eingefügte `traceId` und `spanId` für einfacheres Debugging und Korrelation des Anwendungsverhaltens mit bestimmten Anfragen.
*   **Überwachen Sie Ihr Tracing-Backend:** Stellen Sie sicher, dass Ihr Tracing-Backend (z. B. Zipkin-Server) über ausreichende Ressourcen verfügt, um das eingehende Trace-Volumen zu bewältigen.
*   **Integrieren Sie andere Observability-Tools:** Tracing ist ein Teil von Observability. Kombinieren Sie es mit Metriken (ebenfalls über Micrometer) und strukturiertem Logging für einen ganzheitlichen Blick auf die Gesundheit und Leistung Ihrer Anwendung.

Indem Sie diese Richtlinien befolgen, können Sie Micrometer Tracing effektiv nutzen, um tiefe Einblicke in Ihre Spring Boot-Anwendungen zu gewinnen, insbesondere in verteilten Umgebungen.