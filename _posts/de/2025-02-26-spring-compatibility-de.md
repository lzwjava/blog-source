---
audio: false
generated: true
lang: de
layout: post
title: Java-Version-Kompatibilität mit Spring Boot
translated: true
type: note
---

### Den Fehler verstehen

Wenn Sie `mvn spring-boot:run` mit Spring Boot 3.4.3 ausführen und auf den Fehler "class file has wrong version 61.0, should be 52.0" stoßen, deutet dies auf ein Java-Version-Kompatibilitätsproblem hin. In Java haben Klassendateien eine Versionsnummer, die der Java-Version entspricht, mit der sie kompiliert wurden:

- **Version 52.0** entspricht Java 8.
- **Version 61.0** entspricht Java 17.

Der Fehler deutet darauf hin, dass die Klassendateien Ihrer Spring Boot-Anwendung mit Java 17 (Version 61.0) kompiliert wurden, aber die Java Virtual Machine (JVM), die versucht, sie auszuführen, Klassendateien erwartet, die mit Java 8 (Version 52.0) kompatibel sind. Da die JVM von Java 8 keine mit Java 17 kompilierten Klassendateien ausführen kann (weil Java in diesem Kontext abwärtskompatibel, aber nicht aufwärtskompatibel ist), erhalten Sie diesen Fehler.

### Warum das passiert

Spring Boot 3.4.3 erfordert **Java 17 oder höher** als minimale unterstützte Version. Das bedeutet, dass Ihr Projekt sowohl kompiliert als auch mit mindestens Java 17 ausgeführt werden sollte. Die Fehlanpassung tritt wahrscheinlich aus folgenden Gründen auf:

1. **Kompilierung**: Ihr Projekt ist so konfiguriert, dass es mit Java 17 kompiliert, wodurch Klassendateien mit der Version 61.0 erzeugt werden. Dies wird typischerweise in Ihrer `pom.xml` mit dem `maven-compiler-plugin` oder der Eigenschaft `<java.version>` festgelegt.
2. **Laufzeit**: Wenn Sie `mvn spring-boot:run` ausführen, startet das Spring Boot Maven Plugin einen neuen Java-Prozess, um die Anwendung auszuführen. Die verwendete `java`-Executable stammt jedoch von einer Java 8-Installation (Version 52.0), die die mit Java 17 kompilierten Klassendateien nicht verarbeiten kann.

### Schritte zur Behebung des Problems

Um dies zu beheben, müssen Sie sicherstellen, dass sowohl die Kompilierungs- als auch die Laufzeitumgebung Java 17 verwenden. So gehen Sie vor:

#### 1. Überprüfen Sie die Java-Version Ihres Projekts
Stellen Sie zunächst sicher, dass Ihr Projekt für die Verwendung von Java 17 konfiguriert ist. Überprüfen Sie dazu Folgendes in Ihrer `pom.xml`:

```xml
<properties>
    <java.version>17</java.version>
</properties>
```

Diese Eigenschaft weist den `maven-compiler-plugin` an, Ihren Code mit Java 17 zu kompilieren. Spring Boot 3.4.3 setzt dies standardmäßig, aber es ist gut, dies zu überprüfen. Wenn sie fehlt oder auf eine andere Version (z.B. 8) gesetzt ist, aktualisieren Sie sie auf 17.

#### 2. Installieren Sie Java 17
Stellen Sie sicher, dass Java 17 auf Ihrem System installiert ist. Sie können es von folgenden Quellen herunterladen:

- [Adoptium (Eclipse Temurin)](https://adoptium.net/)
- [Oracle JDK](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html) (falls Sie die Lizenzbedingungen akzeptieren)

Um zu überprüfen, ob Java 17 installiert ist, öffnen Sie ein Terminal und führen Sie aus:

```bash
java -version
```

Wenn es nicht Java 17 anzeigt (z.B. `openjdk 17.x.x` oder ähnliches), installieren Sie es und fahren Sie fort.

#### 3. Aktualisieren Sie Ihre Umgebung auf Java 17
Das Spring Boot Maven Plugin verwendet die `java`-Executable aus Ihrer Umgebung, die typischerweise durch die Umgebungsvariable `JAVA_HOME` oder den `java`-Befehl im PATH Ihres Systems bestimmt wird. Wenn Ihr aktueller `java`-Befehl auf Java 8 verweist, müssen Sie ihn aktualisieren.

##### Option A: JAVA_HOME und PATH setzen
Setzen Sie Ihre `JAVA_HOME`-Umgebungsvariable so, dass sie auf die Java 17-Installation verweist, und stellen Sie sicher, dass der `java`-Befehl in Ihrem PATH diese verwendet.

- **Unter Linux/Mac**:
  1. Finden Sie Ihr Java 17-Installationsverzeichnis (z.B. `/usr/lib/jvm/java-17-openjdk` oder wo auch immer Sie es installiert haben).
  2. Setzen Sie `JAVA_HOME` und aktualisieren Sie `PATH` in Ihrem Terminal:
     ```bash
     export JAVA_HOME=/pfad/zu/java-17
     export PATH=$JAVA_HOME/bin:$PATH
     ```
  3. Überprüfen Sie:
     ```bash
     java -version
     ```
     Es sollte nun Java 17 anzeigen.

  Um dies dauerhaft zu machen, fügen Sie die `export`-Zeilen zu Ihrer Shell-Konfigurationsdatei hinzu (z.B. `~/.bashrc`, `~/.zshrc`).

- **Unter Windows**:
  1. Finden Sie das Java 17-Installationsverzeichnis (z.B. `C:\Programme\Java\jdk-17`).
  2. Setzen Sie `JAVA_HOME`:
     - Öffnen Sie das Fenster "Systemeigenschaften" (suchen Sie im Startmenü nach "Umgebungsvariablen").
     - Fügen Sie unter "Systemvariablen" `JAVA_HOME` hinzu oder aktualisieren Sie es auf `C:\Programme\Java\jdk-17`.
  3. Aktualisieren Sie `Path`:
     - Bearbeiten Sie unter "Systemvariablen" `Path` und fügen Sie `%JAVA_HOME%\bin` hinzu (stellen Sie sicher, dass es sich oben befindet oder entfernen Sie ältere Java-Pfade wie Java 8).
  4. Öffnen Sie eine neue Eingabeaufforderung und überprüfen Sie:
     ```cmd
     java -version
     ```
     Es sollte Java 17 anzeigen.

##### Option B: Eine spezifische Java-Version für Maven verwenden
Wenn Sie mehrere Java-Versionen installiert haben und Ihre systemweite `JAVA_HOME` nicht ändern möchten, können Sie Maven mit einer bestimmten Java-Version ausführen:

- Bevor Sie `mvn spring-boot:run` ausführen, setzen Sie `JAVA_HOME` nur für diesen Befehl:
  ```bash
  JAVA_HOME=/pfad/zu/java-17 mvn spring-boot:run
  ```
  Dies stellt sicher, dass das Spring Boot Maven Plugin Java 17 verwendet, ohne Ihre Systemeinstellungen zu ändern.

#### 4. Führen Sie die Anwendung erneut aus
Wenn Java 17 korrekt eingestellt ist, führen Sie aus:

```bash
mvn spring-boot:run
```

Das Plugin verwendet nun Java 17, um Ihre Anwendung auszuführen, was der Version der kompilierten Klassendateien (61.0) entspricht, und der Fehler sollte verschwinden.

### Zusätzliche Überprüfungen
- **Mavens Java-Version**: Führen Sie `mvn -version` aus, um zu sehen, welche Java-Version Maven verwendet. Sie sollte mit Ihrer `JAVA_HOME` übereinstimmen. Wenn nicht, stellen Sie sicher, dass Ihr PATH und `JAVA_HOME` korrekt konfiguriert sind.
- **Abhängigkeiten**: Wenn der Fehler weiterhin besteht, könnte eine Abhängigkeit mit Java 17 kompiliert worden sein, während Ihre Laufzeit immer noch falsch konfiguriert ist. Da Spring Boot 3.4.3 Java 17 vorschreibt, sollte das Sicherstellen, dass Ihre Laufzeit Java 17 ist, dies beheben.

### Warum nicht Java 8?
Spring Boot 3.4.3 unterstützt Java 8 nicht. Wenn Sie Java 8 verwenden müssen, müssten Sie auf eine ältere Spring Boot-Version (z.B. 2.x) downgraden, was jedoch nicht empfohlen wird, es sei denn, Sie haben spezifische Einschränkungen. Da Ihre Klassendateien die Version 61.0 haben, ist das Beibehalten von Java 17 mit den Anforderungen von Spring Boot 3.4.3 konsistent.

### Zusammenfassung der endgültigen Lösung
Um "class file has wrong version 61.0, should be 52.0" zu beheben, wenn Sie `mvn spring-boot:run` mit Spring Boot 3.4.3 ausführen:

1. Stellen Sie sicher, dass `<java.version>17</java.version>` in Ihrer `pom.xml` vorhanden ist.
2. Installieren Sie Java 17, falls noch nicht vorhanden.
3. Setzen Sie `JAVA_HOME` auf Ihr Java 17-Installationsverzeichnis.
4. Aktualisieren Sie Ihren PATH, sodass `java -version` Java 17 anzeigt.
5. Führen Sie `mvn spring-boot:run` erneut aus.

Dies stellt sicher, dass Ihre Laufzeitumgebung mit Ihren kompilierten Java 17-Klassendateien übereinstimmt und behebt das Kompatibilitätsproblem.