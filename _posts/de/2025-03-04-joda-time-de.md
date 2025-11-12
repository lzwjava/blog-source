---
audio: false
generated: true
lang: de
layout: post
title: Datum- und Zeitoperationen in Java
translated: true
type: note
---

### Wichtige Punkte
- Es scheint wahrscheinlich, dass Sie `org.joda.time` zu Ihrem Java-Projekt hinzufügen und seine Klassen für Datums- und Zeitoperationen importieren müssen.
- Recherchen legen nahe, die Bibliothek über Maven mit Version 2.13.1 einzubinden oder die JAR-Datei herunterzuladen und dann Klassen wie `DateTime` und `LocalDate` zu verwenden.
- Die Indizien deuten darauf hin, dass Joda-Time nützlich für die Handhabung von Zeitzonen, Kalendersystemen und Zeitintervallen ist, mit Beispielen wie der Erstellung von Datumsobjekten und deren Modifikation.

### Was ist Joda-Time und wie richtet man es ein?
Joda-Time ist eine Bibliothek für die Handhabung von Datum und Zeit in Java, die besonders vor Java 8 nützlich war und eine intuitive API bietet, um die älteren, weniger threadsicheren `Date`- und `Calendar`-Klassen zu ersetzen. Um sie zu verwenden, binden Sie zunächst die Bibliothek in Ihr Projekt ein. Bei Verwendung von Maven fügen Sie diese Abhängigkeit zu Ihrer `pom.xml` hinzu:
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
Alternativ laden Sie die JAR-Datei von [dieser Website](https://www.joda.org/joda-time/download.html) herunter und fügen sie dem Classpath Ihres Projekts hinzu, z.B. in Eclipse durch Erstellen eines "libs"-Ordners und Verlinken der JAR über Projekteigenschaften.

### Grundlegende Verwendungsbeispiele
Nach der Einrichtung importieren Sie Klassen wie `org.joda.time.DateTime` oder `org.joda.time.LocalDate`. Hier sind einige Beispiele:
- Erstellen Sie ein aktuelles Datum-Zeit-Objekt: `DateTime now = new DateTime();`
- Greifen Sie auf Felder zu: `int year = now.getYear(); String monthName = now.monthOfYear().getAsText();`
- Modifizieren Sie es: `DateTime future = now.plusDays(5);`

### Erweiterte Funktionen
Joda-Time unterstützt Zeitzonen (z.B. `DateTimeZone.forID("America/New_York")`) und verschiedene Kalendersysteme (z.B. Koptisch über `CopticChronology.getInstance()`). Es handhabt auch Intervalle und Dauern, wie `Interval interval = new Interval(startDt, endDt);`.

Ein unerwartetes Detail ist, dass Joda-Time als "abgeschlossen" betrachtet wird, wobei das `java.time`-Paket von Java 8 für neue Projekte empfohlen wird, es aber für Legacy-Systeme oder spezifische Anforderungen dennoch relevant ist.

---

### Umfragehinweis: Umfassende Anleitung zur Verwendung von `org.joda.time`

Dieser Abschnitt bietet eine detaillierte Erkundung der Verwendung der `org.joda.time`-Bibliothek, erweitert die direkte Antwort mit zusätzlichem Kontext und technischer Tiefe und ist geeignet für Entwickler, die ein gründliches Verständnis anstreben. Er enthält Einrichtung, Verwendungsbeispiele, Schlüsselfunktionen und weitere Ressourcen und gewährleistet so eine vollständige Referenz für die Implementierung.

#### Einführung in Joda-Time
Joda-Time, entwickelt von joda.org, ist eine weit verbreitete Bibliothek für die Verarbeitung von Datum und Zeit, insbesondere vor der Veröffentlichung von Java 8. Sie adressiert Designprobleme in den Java-`Date`- und `Calendar`-Klassen, wie z.B. Thread-Safety-Bedenken, durch die Verwendung unveränderlicher Klassen. Vor Java 8 waren die `Date`-Klasse und `SimpleDateFormatter` nicht threadsicher, und Operationen wie Tages-/Monats-/Jahresverschiebungen waren kontraintuitiv (z.B. Tage beginnen bei 0, Monate bei 1, erforderten `Calendar`). Joda-Time bietet eine saubere, flüssige API und unterstützt acht Kalendersysteme im Vergleich zu Javas zwei (Gregorianisch und Japanisch Kaiserlich). Nach Java 8 betrachten die Autoren Joda-Time als weitgehend abgeschlossen und empfehlen die Migration zu `java.time` (JSR-310) für neue Projekte, aber es bleibt relevant für Legacy-Systeme oder spezifische Anwendungsfälle.

#### Einrichtung von Joda-Time
Um Joda-Time zu verwenden, müssen Sie es zunächst in Ihr Java-Projekt einbinden. Die neueste Version zum 3. März 2025 ist 2.13.1, was Stabilität und Kompatibilität mit JDK 1.5 oder höher gewährleistet. Für Maven-Benutzer fügen Sie die folgende Abhängigkeit zu Ihrer `pom.xml` hinzu:
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
Diese ist auf [Maven Repository](https://mvnrepository.com/artifact/joda-time/joda-time) zu finden. Für Nicht-Maven-Projekte laden Sie die `.tar.gz`-Datei von [dieser Website](https://www.joda.org/joda-time/download.html) herunter, entpacken sie und fügen die `joda-time-2.13.1.jar` zum Classpath Ihres Projekts hinzu. Zum Beispiel in Eclipse: Erstellen Sie einen "libs"-Ordner, kopieren Sie die JAR und verlinken Sie sie über Eigenschaften -> Java Build Path -> Libraries -> Add Jars. Testen Sie die Einrichtung mit `DateTime test = new DateTime();`, um die Funktionalität sicherzustellen.

#### Grundlegende Verwendung und Beispiele
Nach dem Einbinden importieren Sie Klassen aus `org.joda.time`, wie `DateTime`, `LocalDate`, `LocalTime` und `LocalDateTime`, die alle unveränderlich für Thread-Safety sind. Hier sind detaillierte Beispiele:

- **Erstellen von Datum-Zeit-Objekten:**
  - Von der aktuellen Zeit: `DateTime now = new DateTime();` verwendet die Standardzeitzone und den ISO-Kalender.
  - Von einem Java `Date`: `java.util.Date juDate = new Date(); DateTime dt = new DateTime(juDate);` für Interoperabilität.
  - Von spezifischen Werten: Konstruktoren akzeptieren `Long` (Millisekunden), `String` (ISO8601) oder andere Joda-Time-Objekte, z.B. `DateTime dt = new DateTime(2025, 3, 3, 8, 39);`.

- **Zugreifen auf Felder:**
  - Verwenden Sie Getter-Methoden: `int year = now.getYear(); int month = now.getMonthOfYear();` wobei Januar 1 und Dezember 12 ist.
  - Für textuelle Darstellung: `String dayName = now.dayOfWeek().getAsText();` gibt z.B. "Montag" für den 3. März 2025 aus.
  - Eigenschaften prüfen: `boolean isLeap = now.year().isLeap();` gibt `false` für 2025 zurück.

- **Modifizieren von Datum-Zeit:**
  - Erstellen Sie neue Instanzen mit Modifikationen: `DateTime newDt = now.withYear(2025);` oder `DateTime future = now.plusDays(5);`.
  - Dauern hinzufügen: `DateTime later = now.plusHours(2);` zum Hinzufügen von zwei Stunden, gibt eine neue Instanz zurück.

Ein praktisches Beispiel von GeeksforGeeks veranschaulicht die Verwendung:
```java
import org.joda.time.DateTime;
import org.joda.time.LocalDateTime;
public class JodaTime {
    public static void main(String[] args) {
        DateTime now = new DateTime();
        System.out.println("Aktueller Tag: " + now.dayOfWeek().getAsText());
        System.out.println("Aktueller Monat: " + now.monthOfYear().getAsText());
        System.out.println("Aktuelles Jahr: " + now.year().getAsText());
        System.out.println("Aktuelles Jahr ist ein Schaltjahr: " + now.year().isLeap());
        LocalDateTime dt = LocalDateTime.now();
        System.out.println(dt);
    }
}
```
Für den 3. März 2025 könnte die Ausgabe enthalten "Aktueller Tag: Montag", "Aktueller Monat: März", "Aktuelles Jahr: 2025", "Aktuelles Jahr ist ein Schaltjahr: false" und einen Zeitstempel wie "2025-03-03T08:39:00.000".

#### Schlüsselfunktionen und erweiterte Verwendung
Joda-Time bietet robuste Funktionen für komplexe Datum-Zeit-Operationen, wie folgt detailliert:

- **Zeitzonen:**
  - Verwaltet über `DateTimeZone`, unterstützt benannte Zonen (z.B. "Asia/Tokyo") und feste Offsets. Beispiel:
    ```java
    DateTimeZone zone = DateTimeZone.forID("America/New_York");
    DateTime nyTime = new DateTime(zone);
    ```
  - Die Standardzone entspricht der des JDK, kann aber mit `DateTimeZone.setDefault(zone);` überschrieben werden. Zeitzonendaten werden manuell mehrmals im Jahr aktualisiert, basierend auf [global-tz](https://github.com/JodaOrg/global-tz).

- **Kalendersysteme:**
  - Unterstützt sieben Systeme: Buddhistisch, Koptisch, Äthiopisch, Gregorianisch, Gregorianisch-Julianisch, Islamisch, Julianisch, mit Bereitstellung für benutzerdefinierte Systeme. Beispiel:
    ```java
    Chronology coptic = CopticChronology.getInstance();
    LocalDate copticDate = new LocalDate(coptic);
    ```
  - Standardmäßig ISO-Kalender, historisch ungenau vor 1583, aber geeignet für den modernen zivilen Gebrauch.

- **Intervalle, Dauern und Perioden:**
  - `Interval`: Repräsentiert einen Zeitbereich, halb-offen (Start inklusive, Ende exklusive), z.B. `Interval interval = new Interval(startDt, endDt);`.
  - `Duration`: Exakte Zeit in Millisekunden, z.B. `Duration duration = new Duration(interval);`, nützlich zum Hinzufügen zu Zeitpunkten.
  - `Period`: Definiert in Feldern (Jahre, Monate, Tage, etc.), ungenau in Millisekunden, z.B. `Period period = new Period(startDt, endDt);`. Beispielunterschied: Das Hinzufügen von 1 Tag bei Zeitumstellung (z.B. 2005-03-26 12:00:00) mit `plus(Period.days(1))` fügt 23 Stunden hinzu, während `plus(new Duration(24L*60L*60L*1000L))` 24 Stunden hinzufügt, was das Verhalten von Periode vs. Dauer verdeutlicht.

Der Quick Start Guide bietet eine Tabelle, die Hauptklassen und Anwendungsfälle zusammenfasst:
| **Aspekt**                  | **Details**                                                                                     |
|-----------------------------|-------------------------------------------------------------------------------------------------|
| **Haupt-Datum-Zeit-Klassen**   | Instant, DateTime, LocalDate, LocalTime, LocalDateTime (5 Klassen, alle unveränderlich)               |
| **Instant Anwendungsfall**         | Zeitstempel eines Ereignisses, kein Kalendersystem oder Zeitzone                                          |
| **LocalDate Anwendungsfall**       | Geburtsdatum, keine Tageszeit benötigt                                                           |
| **LocalTime Anwendungsfall**       | Tageszeit, z.B. Ladenöffnungs-/schließzeiten, kein Datum                                               |
| **DateTime Anwendungsfall**        | Allgemeiner Zweck, ersetzt JDK Calendar, enthält Zeitzoneninformation                          |
| **Konstruktortypen**        | Objektkonstruktor akzeptiert: Date, Calendar, String (ISO8601), Long (Millisekunden), Joda-Time-Klassen |
| **Beispielkonvertierung**       | `java.util.Date` zu `DateTime`: `DateTime dt = new DateTime(new Date());`                      |
| **Feldzugriffsmethoden**     | `getMonthOfYear()` (1=Januar, 12=Dezember), `getYear()`                                        |
| **Modifikationsmethoden**     | `withYear(2000)`, `plusHours(2)`                                                               |
| **Property-Methoden Beispiele**| `monthOfYear().getAsText()`, `monthOfYear().getAsShortText(Locale.FRENCH)`, `year().isLeap()`, `dayOfMonth().roundFloorCopy()` |
| **Standard-Kalendersystem**  | ISO-Kalendersystem (De-facto-Bürgerkalender, historisch ungenau vor 1583)              |
| **Standard-Zeitzone**        | Gleich wie JDK-Standard, kann überschrieben werden                                                         |
| **Chronologie-Klasse**         | Unterstützt mehrere Kalendersysteme, z.B. `CopticChronology.getInstance()`                     |
| **Zeitzonen-Beispiel**        | `DateTimeZone zone = DateTimeZone.forID("Asia/Tokyo");`, `GJChronology.getInstance(zone)`      |
| **Interval-Klasse**           | `Interval` - hält Start- und End-Datum-Zeit, Operationen basieren auf Bereich                          |
| **Period-Klasse**             | `Period` - hält Periode wie 6 Monate, 3 Tage, 7 Stunden, kann aus Intervall abgeleitet werden               |
| **Duration-Klasse**           | `Duration` - exakte Dauer in Millisekunden, kann aus Intervall abgeleitet werden                          |
| **Periode vs. Dauer Beispiel**| Hinzufügen von 1 Tag bei Zeitumstellung (2005-03-26 12:00:00): `plus(Period.days(1))` fügt 23 Stunden hinzu, `plus(new Duration(24L*60L*60L*1000L))` fügt 24 Stunden hinzu |

Ein interessantes Detail ist die Erweiterbarkeit der Objektkonstruktoren, die die Konvertierung von JDK `Date` oder `Calendar` durch direktes Übergeben ermöglicht, was die Migration von Legacy-Code vereinfacht.

#### Weiterführendes Lernen und Ressourcen
Für eine tiefgehende Erkundung konsultieren Sie die offizielle Dokumentation unter [Joda-Time User Guide](https://www.joda.org/joda-time/userguide.html), die fortgeschrittene Themen wie Formatierung und Parsing abdeckt. Der Quick Start Guide unter [Joda-Time Quick Start](https://www.joda.org/joda-time/quickstart.html) bietet eine knappe Einführung. Zusätzliche Tutorials sind verfügbar bei [Baeldung Joda-Time](https://www.baeldung.com/joda-time) und [GeeksforGeeks Joda-Time](https://www.geeksforgeeks.org/joda-time/), mit Codebeispielen und Einrichtungsanleitungen. Die API-Dokumentation unter [Joda-Time API Docs](https://www.joda.org/joda-time/apidocs/index.html) ist nützlich für Referenzzwecke, allerdings technischer.

#### Fazit
Joda-Time bietet eine robuste, threadsichere Alternative für Datums- und Zeitoperationen, mit umfassender Unterstützung für Zeitzonen, Kalendersysteme und Zeitberechnungen. Obwohl es nach Java 8 als abgeschlossen betrachtet wird, bleibt es wertvoll für Legacy-Systeme, mit Einrichtung über Maven oder manuelles JAR-Einbinden und Verwendung durch unveränderliche Klassen wie `DateTime` und `LocalDate`. Diese Anleitung stellt sicher, dass Entwickler alle notwendigen Informationen für die Implementierung haben, von grundlegenden Beispielen bis zu erweiterten Funktionen, unterstützt durch umfassende Ressourcen.

### Wichtige Zitate
- [Joda-Time Homepage mit allgemeinen Informationen](https://www.joda.org/joda-time/)
- [Joda-Time Quick Start Guide für Anfänger](https://www.joda.org/joda-time/quickstart.html)
- [Baeldung Tutorial zur Joda-Time Verwendung](https://www.baeldung.com/joda-time)
- [GeeksforGeeks Artikel zu Joda-Time mit Beispielen](https://www.geeksforgeeks.org/joda-time/)
- [Joda-Time User Guide für detaillierte Referenz](https://www.joda.org/joda-time/userguide.html)
- [Joda-Time Download- und Installationsseite](https://www.joda.org/joda-time/download.html)
- [Maven Repository für Joda-Time Abhängigkeit](https://mvnrepository.com/artifact/joda-time/joda-time)
- [Joda-Time API-Dokumentation für technische Referenz](https://www.joda.org/joda-time/apidocs/index.html)