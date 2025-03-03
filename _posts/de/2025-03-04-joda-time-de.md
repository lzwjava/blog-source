---
audio: false
generated: true
lang: de
layout: post
title: Datums- und Zeitoperationen in Java
translated: true
---

### Wichtige Punkte
- Es scheint wahrscheinlich, dass zur Verwendung von `org.joda.time` die Bibliothek zu Ihrem Java-Projekt hinzugefügt und ihre Klassen für Datums- und Zeitoperationen importiert werden müssen.
- Die Forschung legt nahe, die Bibliothek über Maven mit der Version 2.13.1 einzubinden oder die JAR-Datei herunterzuladen und dann Klassen wie `DateTime` und `LocalDate` zu verwenden.
- Die Beweise deuten darauf hin, dass Joda-Time nützlich ist, um Zeitzonen, Kalendersysteme und Zeitintervalle zu verwalten, mit Beispielen wie dem Erstellen von Datum-Objekten und deren Modifikation.

### Was ist Joda-Time und wie richtet man es ein?
Joda-Time ist eine Bibliothek zur Handhabung von Daten und Zeiten in Java, besonders nützlich vor Java 8, und bietet eine intuitive API, um die älteren, weniger thread-sicheren `Date`- und `Calendar`-Klassen zu ersetzen. Um es zu verwenden, fügen Sie zunächst die Bibliothek in Ihr Projekt ein. Wenn Sie Maven verwenden, fügen Sie diese Abhängigkeit zu Ihrer `pom.xml` hinzu:
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
Alternativ können Sie die JAR-Datei von [dieser Website](https://www.joda.org/joda-time/download.html) herunterladen und sie zum Klassenspeicher Ihres Projekts hinzufügen, z.B. in Eclipse, indem Sie einen "libs"-Ordner erstellen und die JAR über die Projekteigenschaften verknüpfen.

### Grundlegende Verwendungsbeispiele
Nach der Einrichtung importieren Sie Klassen wie `org.joda.time.DateTime` oder `org.joda.time.LocalDate`. Hier sind einige Beispiele:
- Erstellen Sie ein aktuelles Datum-Zeit-Objekt: `DateTime now = new DateTime();`
- Zugriff auf Felder: `int year = now.getYear(); String monthName = now.monthOfYear().getAsText();`
- Modifizieren: `DateTime future = now.plusDays(5);`

### Fortgeschrittene Funktionen
Joda-Time unterstützt Zeitzonen (z.B. `DateTimeZone.forID("America/New_York")`) und verschiedene Kalendersysteme (z.B. Koptisch über `CopticChronology.getInstance()`). Es verarbeitet auch Intervalle und Dauer, wie `Interval interval = new Interval(startDt, endDt);`.

Eine unerwartete Einzelheit ist, dass Joda-Time als "abgeschlossenes" Projekt gilt, wobei das `java.time`-Paket von Java 8 für neue Projekte empfohlen wird, aber es bleibt für Legacy-Systeme oder spezifische Anforderungen relevant.

---

### Umfragehinweis: Umfassender Leitfaden zur Verwendung von `org.joda.time`

Dieser Abschnitt bietet eine detaillierte Untersuchung der Verwendung der `org.joda.time`-Bibliothek, erweitert die direkte Antwort mit zusätzlichem Kontext und technischer Tiefe, geeignet für Entwickler, die ein umfassendes Verständnis suchen. Er umfasst Einrichtung, Verwendungsbeispiele, Schlüsselmerkmale und weitere Ressourcen, um eine vollständige Referenz für die Implementierung zu gewährleisten.

#### Einführung in Joda-Time
Joda-Time, entwickelt von joda.org, ist eine weit verbreitete Bibliothek zur Verarbeitung von Datum und Uhrzeit, insbesondere vor der Veröffentlichung von Java 8. Es behandelt Designprobleme in den Java `Date`- und `Calendar`-Klassen, wie z.B. Thread-Sicherheitsprobleme, durch die Verwendung unveränderlicher Klassen. Vor Java 8 waren die `Date`-Klasse und `SimpleDateFormatter` nicht thread-sicher, und Operationen wie Tag/Monat/Jahr-Verschiebungen waren nicht intuitiv (z.B. Tage beginnen bei 0, Monate bei 1, erfordern `Calendar`). Joda-Time bietet eine saubere, flüssige API und unterstützt acht Kalendersysteme, im Vergleich zu den zwei von Java (Gregorian und Japanisches Kaiserreich). Nach Java 8 betrachten die Autoren Joda-Time als weitgehend abgeschlossen und empfehlen die Migration zu `java.time` (JSR-310) für neue Projekte, aber es bleibt für Legacy-Systeme oder spezifische Anwendungsfälle relevant.

#### Einrichtung von Joda-Time
Um Joda-Time zu verwenden, müssen Sie es zunächst in Ihr Java-Projekt einbinden. Die neueste Version bis zum 3. März 2025 ist 2.13.1, was Stabilität und Kompatibilität mit JDK 1.5 oder später gewährleistet. Für Maven-Nutzer fügen Sie die folgende Abhängigkeit zu Ihrer `pom.xml` hinzu:
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
Dies kann auf [Maven Repository](https://mvnrepository.com/artifact/joda-time/joda-time) gefunden werden. Für Nicht-Maven-Projekte laden Sie die `.tar.gz`-Datei von [dieser Website](https://www.joda.org/joda-time/download.html) herunter, entpacken Sie sie und fügen Sie die `joda-time-2.13.1.jar` zu Ihrem Klassenspeicher hinzu. Zum Beispiel in Eclipse, erstellen Sie einen "libs"-Ordner, kopieren Sie die JAR und verknüpfen Sie sie über Eigenschaften -> Java Build Path -> Libraries -> Add Jars. Testen Sie die Einrichtung mit `DateTime test = new DateTime();`, um die Funktionalität sicherzustellen.

#### Grundlegende Verwendung und Beispiele
Nach dem Einbinden importieren Sie Klassen von `org.joda.time`, wie `DateTime`, `LocalDate`, `LocalTime` und `LocalDateTime`, die alle unveränderlich sind, um Thread-Sicherheit zu gewährleisten. Hier sind detaillierte Beispiele:

- **Erstellen von Datum-Zeit-Objekten:**
  - Aus der aktuellen Zeit: `DateTime now = new DateTime();` verwendet die Standardzeitzone und das ISO-Kalender.
  - Aus einem Java `Date`: `java.util.Date juDate = new Date(); DateTime dt = new DateTime(juDate);` für die Interoperabilität.
  - Aus spezifischen Werten: Konstruktoren akzeptieren `Long` (Millisekunden), `String` (ISO8601) oder andere Joda-Time-Objekte, z.B. `DateTime dt = new DateTime(2025, 3, 3, 8, 39);`.

- **Zugriff auf Felder:**
  - Verwenden Sie Getter-Methoden: `int year = now.getYear(); int month = now.getMonthOfYear();` wobei Januar 1 und Dezember 12 ist.
  - Für die textuelle Darstellung: `String dayName = now.dayOfWeek().getAsText();` gibt z.B. "Montag" für den 3. März 2025 aus.
  - Überprüfen Sie Eigenschaften: `boolean isLeap = now.year().isLeap();` gibt `false` für 2025 zurück.

- **Modifizieren von Datum-Zeit:**
  - Erstellen Sie neue Instanzen mit Modifikationen: `DateTime newDt = now.withYear(2025);` oder `DateTime future = now.plusDays(5);`.
  - Fügen Sie Dauer hinzu: `DateTime later = now.plusHours(2);` zum Hinzufügen von zwei Stunden, zurückgegeben wird eine neue Instanz.

Ein praktisches Beispiel von GeeksforGeeks zeigt die Verwendung:
```java
import org.joda.time.DateTime;
import org.joda.time.LocalDateTime;
public class JodaTime {
    public static void main(String[] args) {
        DateTime now = new DateTime();
        System.out.println("Aktueller Tag: " + now.dayOfWeek().getAsText());
        System.out.println("Aktueller Monat: " + now.monthOfYear().getAsText());
        System.out.println("Aktuelles Jahr: " + now.year().getAsText());
        System.out.println("Aktuelles Jahr ist Schaltjahr: " + now.year().isLeap());
        LocalDateTime dt = LocalDateTime.now();
        System.out.println(dt);
    }
}
```
Für den 3. März 2025 könnte die Ausgabe "Aktueller Tag: Montag", "Aktueller Monat: März", "Aktuelles Jahr: 2025", "Aktuelles Jahr ist Schaltjahr: false" und ein Zeitstempel wie "2025-03-03T08:39:00.000" enthalten sein.

#### Schlüsselmerkmale und fortgeschrittene Verwendung
Joda-Time bietet robuste Funktionen für komplexe Datum-Zeit-Operationen, wie folgt beschrieben:

- **Zeitzonen:**
  - Verwaltet über `DateTimeZone`, unterstützt benannte Zonen (z.B. "Asia/Tokyo") und feste Versetzungen. Beispiel:
    ```java
    DateTimeZone zone = DateTimeZone.forID("America/New_York");
    DateTime nyTime = new DateTime(zone);
    ```
  - Die Standardzone entspricht der JDK, kann jedoch mit `DateTimeZone.setDefault(zone);` überschrieben werden. Zeitzonendaten werden manuell mehrere Male im Jahr aktualisiert, basierend auf [global-tz](https://github.com/JodaOrg/global-tz).

- **Kalendersysteme:**
  - Unterstützt sieben Systeme: Buddhistisch, Koptisch, Äthiopisch, Gregorianisch, Gregorianisch-Julianisch, Islamisch, Julianisch, mit Bereitstellung für benutzerdefinierte Systeme. Beispiel:
    ```java
    Chronology coptic = CopticChronology.getInstance();
    LocalDate copticDate = new LocalDate(coptic);
    ```
  - Standardmäßig auf ISO-Kalender, historisch ungenau vor 1583, aber geeignet für moderne zivile Nutzung.

- **Intervalle, Dauer und Perioden:**
  - `Interval`: Repräsentiert einen Zeitbereich, halb offen (Start inklusiv, Ende exklusiv), z.B. `Interval interval = new Interval(startDt, endDt);`.
  - `Duration`: Genauer Zeit in Millisekunden, z.B. `Duration duration = new Duration(interval);`, nützlich zum Hinzufügen zu Momenten.
  - `Period`: Definiert in Feldern (Jahre, Monate, Tage usw.), ungenau in Millisekunden, z.B. `Period period = new Period(startDt, endDt);`. Beispielunterschied: Hinzufügen von 1 Tag zur Sommerzeit (z.B. 2005-03-26 12:00:00) mit `plus(Period.days(1))` fügt 23 Stunden hinzu, während `plus(new Duration(24L*60L*60L*1000L))` 24 Stunden hinzufügt, was das Verhalten von Periode vs. Dauer hervorhebt.

Der Schnellstart-Leitfaden bietet eine Tabelle, die die Hauptklassen und Anwendungsfälle zusammenfasst:
| **Aspekt**                  | **Details**                                                                                     |
|-----------------------------|-------------------------------------------------------------------------------------------------|
| **Haupt-Datum-Zeit-Klassen** | Instant, DateTime, LocalDate, LocalTime, LocalDateTime (5 Klassen, alle unveränderlich)               |
| **Instant Anwendungsfall**  | Zeitstempel eines Ereignisses, kein Kalendersystem oder Zeitzone                                          |
| **LocalDate Anwendungsfall** | Geburtsdatum, keine Tageszeit erforderlich                                                           |
| **LocalTime Anwendungsfall** | Tageszeit, z.B. Ladenöffnungs-/schließzeiten, kein Datum                                               |
| **DateTime Anwendungsfall** | Allgemeiner Zweck, ersetzt JDK Calendar, enthält Zeitzoneninformation                          |
| **Konstruktortypen**        | Objektkonstruktor akzeptiert: Date, Calendar, String (ISO8601), Long (Millisekunden), Joda-Time-Klassen |
| **Beispielkonvertierung**   | `java.util.Date` zu `DateTime`: `DateTime dt = new DateTime(new Date());`                      |
| **Feldzugriffsmethoden**    | `getMonthOfYear()` (1=Januar, 12=Dezember), `getYear()`                                        |
| **Modifikationsmethoden**   | `withYear(2000)`, `plusHours(2)`                                                               |
| **Beispieleigenschaftenmethoden** | `monthOfYear().getAsText()`, `monthOfYear().getAsShortText(Locale.FRENCH)`, `year().isLeap()`, `dayOfMonth().roundFloorCopy()` |
| **Standardkalendersystem**  | ISO-Kalendersystem (de facto ziviles Kalender, historisch ungenau vor 1583)              |
| **Standardzeitzone**        | Gleiche wie JDK-Standard, kann überschrieben werden                                                         |
| **Chronology-Klasse**       | Unterstützt mehrere Kalendersysteme, z.B. `CopticChronology.getInstance()`                     |
| **Zeitzonenbeispiel**       | `DateTimeZone zone = DateTimeZone.forID("Asia/Tokyo");`, `GJChronology.getInstance(zone)`      |
| **Interval-Klasse**         | `Interval` - hält Start- und Enddatum-Zeit, Operationen basierend auf Bereich                          |
| **Period-Klasse**           | `Period` - hält Periode wie 6 Monate, 3 Tage, 7 Stunden, kann von Intervall abgeleitet werden               |
| **Duration-Klasse**         | `Duration` - genaue Dauer in Millisekunden, kann von Intervall abgeleitet werden                          |
| **Period vs. Duration Beispiel** | Hinzufügen von 1 Tag zur Sommerzeit (2005-03-26 12:00:00): `plus(Period.days(1))` fügt 23 Stunden hinzu, `plus(new Duration(24L*60L*60L*1000L))` fügt 24 Stunden hinzu |

Eine interessante Einzelheit ist die Erweiterbarkeit der Objektkonstruktoren, die die Konvertierung von JDK `Date` oder `Calendar` durch direktes Übergeben ermöglichen, was die Migration von Legacy-Code vereinfacht.

#### Weitere Lernressourcen und Ressourcen
Für eine tiefere Untersuchung konsultieren Sie die offizielle Dokumentation unter [Joda-Time Benutzerhandbuch](https://www.joda.org/joda-time/userguide.html), die fortgeschrittene Themen wie Formatierung und Parsen abdeckt. Der Schnellstart-Leitfaden unter [Joda-Time Schnellstart](https://www.joda.org/joda-time/quickstart.html) bietet eine knappe Einführung. Zusätzliche Tutorials sind auf [Baeldung Joda-Time](https://www.baeldung.com/joda-time) und [GeeksforGeeks Joda-Time](https://www.geeksforgeeks.org/joda-time/) verfügbar, mit Codebeispielen und Einrichtungsanweisungen. Die API-Dokumentation unter [Joda-Time API-Dokumentation](https://www.joda.org/joda-time/apidocs/index.html) ist für Referenzen nützlich, aber technischer.

#### Schlussfolgerung
Joda-Time bietet eine robuste, thread-sichere Alternative für Datum- und Zeitoperationen, mit umfangender Unterstützung für Zeitzonen, Kalendersysteme und Zeitberechnungen. Obwohl es nach Java 8 als abgeschlossen gilt, bleibt es für Legacy-Systeme wertvoll, mit Einrichtung über Maven oder manuelle JAR-Einfügung und Verwendung durch unveränderliche Klassen wie `DateTime` und `LocalDate`. Dieser Leitfaden stellt sicher, dass Entwickler alle notwendigen Informationen für die Implementierung haben, von grundlegenden Beispielen bis hin zu fortgeschrittenen Funktionen, unterstützt durch umfassende Ressourcen.

### Wichtige Zitate
- [Joda-Time Startseite mit allgemeinen Informationen](https://www.joda.org/joda-time/)
- [Joda-Time Schnellstart-Leitfaden für Anfänger](https://www.joda.org/joda-time/quickstart.html)
- [Baeldung-Tutorial zur Verwendung von Joda-Time](https://www.baeldung.com/joda-time)
- [GeeksforGeeks-Artikel zu Joda-Time mit Beispielen](https://www.geeksforgeeks.org/joda-time/)
- [Joda-Time Benutzerhandbuch für detaillierte Referenz](https://www.joda.org/joda-time/userguide.html)
- [Joda-Time Download- und Installationsseite](https://www.joda.org/joda-time/download.html)
- [Maven-Repository für Joda-Time-Abhängigkeit](https://mvnrepository.com/artifact/joda-time/joda-time)
- [Joda-Time API-Dokumentation für technische Referenz](https://www.joda.org/joda-time/apidocs/index.html)