---
audio: false
generated: true
lang: de
layout: post
title: Konfiguration von Logback für benutzerdefinierte Log-Formate
translated: true
type: note
---

Um das von Ihnen bereitgestrte Log-Format zu erreichen, müssen Sie Ihre `logback.xml`-Datei konfigurieren. Der Schlüssel liegt darin, ein `PatternLayout` innerhalb Ihres Appenders zu verwenden und die `pattern`-Eigenschaft korrekt zu setzen.

Hier ist eine Aufschlüsselung der Komponenten in Ihrem gewünschten Log-Format und wie sie Logback Pattern Convertern zugeordnet werden:

*   **`2025-06-15T01:37:52.452+08:00`**: Dies ist der Zeitstempel. Verwenden Sie hierfür `%d{yyyy-MM-dd'T'HH:mm:ss.SSSXXX}`.
    *   `yyyy-MM-dd'T'HH:mm:ss.SSS`: Datum und Uhrzeit mit Millisekunden.
    *   `XXX`: ISO 8601-Offset von UTC (z.B. `+08:00`).
*   **`DEBUG`**: Dies ist der Log-Level. Verwenden Sie `%-5p` (linksbündig, 5 Zeichen breit).
*   **`302244`**: Dies ist die Prozess-ID. Logback stellt die Prozess-ID nicht direkt in seinen Standardkonvertern bereit. Es stellt jedoch die **Thread-ID** (`%t` oder `%thread`) bereit. Wenn es sich bei "302244" in Ihrem Beispiel tatsächlich um eine Thread-ID handelt (was in Anwendungslogs sehr häufig vorkommt), dann ist `%thread` das, was Sie benötigen. Wenn es sich *zwingend* um die OS-Prozess-ID handeln muss, benötigen Sie möglicherweise einen benutzerdefinierten Logback-Konverter oder eine Systemeigenschaft, falls Ihre Umgebung dies zulässt. Für typische Spring Boot-Anwendungen ist dies normalerweise die Thread-ID. Ich gehe für dieses Beispiel von der Thread-ID aus.
*   **`---`**: Ein Literal-String.
*   **`[nio-8090-exec-1]`**: Dies ist der Thread-Name. Verwenden Sie `[%thread]` oder `%-40.40thread`, wenn Sie eine feste Breite wünschen.
*   **`o.s.w.s.m.m.a.HttpEntityMethodProcessor`**: Dies ist der Logger-Name (typischerweise der vollständig qualifizierte Klassenname). Verwenden Sie `%-40.40logger{39}`, um einen rechtsbündigen, abgeschnittenen Logger-Namen mit bis zu 39 Zeichen zu erhalten.
*   **`:`**: Ein Literal-Doppelpunkt.
*   **`Writing ["{"vnstatversion":"2.9","jsonversion":"2","interfaces":[{"name":"enp4s0","alias":"","created":{"date" (truncated)..."]`**: Dies ist die Log-Nachricht. Verwenden Sie `%msg%n`.

Hier ist eine Beispielkonfiguration für `logback.xml`, die eine sehr ähnliche Ausgabe erzeugen sollte:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>

    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{yyyy-MM-dd'T'HH:mm:ss.SSSXXX} %highlight(%-5p) %thread --- [%thread] %-40.40logger{39} : %msg%n</pattern>
        </encoder>
    </appender>

    <root level="INFO">
        <appender-ref ref="CONSOLE"/>
    </root>

    <logger name="org.springframework.web.servlet.mvc.method.annotation.HttpEntityMethodProcessor" level="DEBUG"/>
    <logger name="org.springframework.web.servlet.DispatcherServlet" level="DEBUG"/>

</configuration>
```

**Erklärung des `pattern`:**

*   `%d{yyyy-MM-dd'T'HH:mm:ss.SSSXXX}`: Datum und Uhrzeit im ISO 8601-Format mit Millisekunden und Zeitzonen-Offset.
*   `%highlight(%-5p)`: Dies gibt den Log-Level (z.B. DEBUG, INFO) linksbündig in 5 Zeichen aus. Wenn die Ausgabe auf einer Konsole erfolgt, wird Logback versuchen, ihn einzufärben.
*   `%thread`: Der Name des Threads, der das Ereignis protokolliert hat. (Wenn Sie die Prozess-ID benötigen, ist es komplexer, aber für Spring-Apps ist die Thread-ID normalerweise das, was hier relevant ist).
*   `---`: Ein Literal-String als Trennzeichen.
*   `[%thread]`: Der Thread-Name in eckigen Klammern.
*   `%-40.40logger{39}`: Der Name des Loggers (normalerweise der Klassenname).
    *   `%-40`: Linksbündig und auf 40 Zeichen aufgefüllt.
    *   `.40logger`: Schneidet den Logger-Namen ab, wenn er länger als 40 Zeichen ist.
    *   `{39}`: Weist Logback an, maximal 39 Zeichen des Logger-Namens anzuzeigen, beginnend vom Ende des Paketnamens aus (z.B. `o.s.w.s.m.m.a.HttpEntityMethodProcessor` könnte, falls passend, so angezeigt werden, oder als `...HttpEntityMethodProcessor`, wenn er vom Anfang abgeschnitten wird). Sie können diese Zahl anpassen.
*   ` :  `: Ein Literal-Doppelpunkt und ein Leerzeichen.
*   `%msg%n`: Die eigentliche Log-Nachricht, gefolgt von einer neuen Zeile.

**Wichtige Hinweise:**

1.  **Platzierung:** Speichern Sie diese XML als `logback.xml` im Verzeichnis `src/main/resources` Ihres Spring Boot-Projekts.
2.  **Prozess-ID vs. Thread-ID:** Wie erwähnt, stellen Logbacks Standard-Pattern-Konverter die OS-Prozess-ID nicht direkt bereit. Wenn `302244` *zwingend* die Prozess-ID sein muss, müssten Sie typischerweise einen benutzerdefinierten `PatternLayoutConverter` implementieren oder eine Systemeigenschaft beim Start setzen, auf die Sie dann in Ihrem Logback-Pattern verweisen. Für die meisten Anwendungslogs ist die Thread-ID (`%thread`) jedoch ausreichend und wird an dieser Position häufig verwendet.
3.  **Spring Boot Standardwerte:** Spring Boot stellt oft eine eigene Standard-Logback-Konfiguration bereit, wenn Sie keine bereitstellen. Durch das Platzieren von `logback.xml` in `src/main/resources` überschreiben Sie die Standardeinstellungen.
4.  **Logger-Level:** Stellen Sie sicher, dass die spezifischen Logger (wie `HttpEntityMethodProcessor` und `DispatcherServlet`) auf den Level `DEBUG` gesetzt sind, wenn Sie deren DEBUG-Meldungen sehen möchten. Wenn der Root-Level `INFO` ist, werden standardmäßig keine DEBUG-Meldungen angezeigt, es sei denn, Sie setzen den Level für bestimmte Logger explizit.

Diese Konfiguration sollte Sie sehr nahe an Ihr gewünschtes Log-Format heranführen.