---
audio: false
generated: true
image: false
lang: de
layout: post
title: JaCoCo-Leitfaden für Python-API-Tests
translated: true
type: note
---

Gute Frage – das ist ein klassisches Integrationsproblem zwischen **Java Code Coverage Tools** (JaCoCo) und **non-Java Test Harnesses** (wie Python `unittest`, die Ihre REST-Endpoints aufrufen).

---

### Warum JaCoCo mit JUnit funktioniert, aber nicht direkt mit Python-Tests

* JaCoCo funktioniert, indem es einen **Java Agent** (`-javaagent:jacocoagent.jar`) an die JVM anhängt.
* Wenn Ihre Tests **innerhalb derselben JVM** laufen (JUnit, TestNG, etc.), kann JaCoCo sehen, welche Klassen und Methoden geladen/ausgeführt werden, und detaillierte Coverage-Reports generieren.
* Wenn Sie Python `unittest` + `requests` verwenden, um Ihre API-Endpoints aufzurufen, testen Sie den **laufenden Server** von außerhalb der JVM.
  Das bedeutet, JaCoCo sieht die Abdeckung nicht automatisch, es sei denn, der Server-Prozess selbst hat den Agenten attached.

---

### Wie Sie genaue Coverage mit JaCoCo und Python-Tests erhalten können

Sie müssen nicht zu JUnit wechseln. Sie können JaCoCo weiterhin verwenden, aber Sie müssen **den Agenten an die JVM anhängen, in der Ihr großes Java-Projekt (der Server) läuft**, nicht an den Test Runner.

1. **Starten Sie Ihre Java-Anwendung mit dem JaCoCo-Agenten**
   Fügen Sie den Agenten zu Ihrem Java-Server-Start hinzu:

   ```bash
   java -javaagent:/pfad/zu/jacocoagent.jar=destfile=jacoco-it.exec,output=file,append=false \
        -jar mein-server.jar
   ```

   Dies sammelt Ausführungsdaten (`jacoco-it.exec`), während Ihre Python-Tests die Endpoints aufrufen.

2. **Führen Sie Ihre Python-Tests normal aus**

   ```bash
   python -m unittest discover tests/
   ```

   Da der Server bereits mit dem Agenten läuft, werden alle Klassen und Methoden, die von HTTP-Requests getroffen werden, aufgezeichnet.

3. **Fahren Sie den Server herunter**
   Die `.exec`-Datei wird geschrieben.

4. **Generieren Sie einen Coverage-Report**
   Verwenden Sie das Maven-Plugin oder die CLI, um die `.exec`-Datei in HTML/XML-Reports umzuwandeln:

   ```bash
   mvn jacoco:report -Djacoco.dataFile=jacoco-it.exec
   ```

   oder mit der CLI:

   ```bash
   java -jar jacococli.jar report jacoco-it.exec \
        --classfiles target/classes \
        --sourcefiles src/main/java \
        --html report
   ```

---

### Zwei Testmodi mit JaCoCo

* **Unit-Tests (in-JVM mit JUnit):** funktioniert out-of-the-box mit dem Maven-Plugin (`prepare-agent` + `report`).
* **Integrationstests (externe Clients wie Python):** erfordert das Starten der JVM mit dem Agenten, dann das Zusammenführen der `.exec`-Daten zurück in die Reports.

---

### Zu Ihrer log4j-Idee

Das Zählen von Log-Statements pro Datei ist extrem grob:

* Nicht jede Methode logged.
* Logs decken keine Conditionals oder Branches ab.
* Coverage ist nicht zuverlässig.

JaCoCo misst im Gegensatz dazu **Class-, Method-, Line- und Branch-Coverage** – eine viel feinere Granularität.

---

✅ **Antwort:** Ja, Sie können den JaCoCo-Ansatz absolut verwenden, selbst wenn Ihre Tests in Python sind. Der Trick ist, **JaCoCo an den Java-Prozess unter Test (Ihren Server) zu hängen**, nicht an den Test Runner. Generieren Sie dann anschließend den Report. Auf diese Weise erhalten Sie dieselbe Method-level und Branch-level Coverage wie mit JUnit.

---

Möchten Sie, dass ich eine **Maven-Konfigurationsbeispiel** entwerfe, das ein spezielles Profil für "Integrationstests" mit JaCoCo einrichtet, sodass Sie Ihren Server starten, ihn mit Python-Tests aufrufen und dann die Coverage in einem Befehl generieren können?