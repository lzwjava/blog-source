---
audio: false
date: 2025-09-11
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Verständnis der JaCoCo- und Maven-Integration
translated: true
type: note
---

Verstanden – so arbeiten die JaCoCo-Bausteine in **Ihrer konkreten POM** zusammen, Schritt für Schritt, und warum.

---

# Die zwei Abdeckungsströme, die diese POM erzeugt

1. **Unit-Test-Abdeckung (Surefire-Pfad)**

* Sie binden JaCoCos **`prepare-agent`** ohne spezielle Konfiguration:

  ```xml
  <execution>
    <id>prepare-agent</id>
    <goals><goal>prepare-agent</goal></goals>
  </execution>
  ```

  Dies injiziert `-javaagent:...org.jacoco.agent-<ver>-runtime.jar` via die `argLine`-Property in die **Surefire**-Test-JVM.
  • Standard-**destfile** ist `${project.build.directory}/jacoco.exec`.
  • Standard-**append** ist `true` (der JaCoCo-Agent hängt an, wenn die Datei bereits existiert).
  • Effekt: Wenn Sie Unit-Tests (falls vorhanden) während `test` ausführen, geht die Abdeckung in `target/jacoco.exec`.

2. **Integrationstest-Abdeckung (Jetty-Pfad)**

* Sie definieren eine **separate Datei** für die IT-Abdeckung:

  ```xml
  <properties>
    <jacoco.it.exec>${project.build.directory}/jacoco-it.exec</jacoco.it.exec>
  </properties>
  ```
* Sie starten Jetty **mit einem eigenen JaCoCo-Agenten**, der auf diese Datei zeigt:

  ```xml
  <plugin>
    <artifactId>jetty-maven-plugin</artifactId>
    ...
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals><goal>start</goal></goals>
      <configuration>
        <daemon>true</daemon>
        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec}
        </jvmArgs>
        ...
      </configuration>
    </execution>
  </plugin>
  ```

  • Jetty läuft in einer **separaten JVM**; dessen Agent schreibt in `target/jacoco-it.exec`.
  • Da `append` nicht angegeben ist, gilt JaCoCos Standard `append=true` – daher hängen mehrere Jetty-Starts an dieselbe Datei an, es sei denn, Sie führen `clean` aus oder setzen `append=false`.

---

# Lifecycle-Ablauf (was bei `mvn verify` passiert)

1. **compile**

   * Spotless formatiert (`spotless-maven-plugin`) und Checkstyle läuft (`maven-checkstyle-plugin`).
   * Ihr WAR wird vorbereitet (`maven-war-plugin`).

2. **test (Surefire)**

   * Falls Sie Unit-Tests haben, laufen diese unter dem durch **`prepare-agent`** injizierten argLine → Abdeckung geht nach `target/jacoco.exec`.

3. **pre-integration-test**

   * Jetty wird **im Daemon-Modus** gestartet:

     ```xml
     <daemon>true</daemon>
     ```

     Maven erhält sofort die Kontrolle zurück; Jetty läuft weiter mit dem angehängten JaCoCo-Agenten und schreibt in `jacoco-it.exec`.

4. **integration-test**

   * Ihre Python-Tests greifen auf die laufende App zu:

     ```xml
     <plugin>
       <artifactId>exec-maven-plugin</artifactId>
       <execution>
         <id>python-integration-tests</id>
         <phase>integration-test</phase>
         <goals><goal>exec</goal></goals>
         <configuration>
           <executable>python3</executable>
           <workingDirectory>${project.parent.basedir}</workingDirectory>
           <arguments>
             <argument>-m</argument><argument>unittest</argument>
             <argument>discover</argument><argument>tests/</argument>
             <argument>-v</argument>
           </arguments>
         </configuration>
       </execution>
     </plugin>
     ```

     Diese Tests bearbeiten Jetty, sodass Abdeckung via den Jetty-JVM-Agent in **`target/jacoco-it.exec`** akkumuliert.

5. **post-integration-test**

   * Jetty wird sauber gestoppt:

     ```xml
     <execution>
       <id>stop-jetty</id>
       <phase>post-integration-test</phase>
       <goals><goal>stop</goal></goals>
       ...
     </execution>
     ```

6. **verify**

   * Sie generieren einen **separaten IT-Report** mit der IT-Datendatei und einem benutzerdefinierten Ausgabeverzeichnis:

     ```xml
     <execution>
       <id>report-it</id>
       <phase>verify</phase>
       <goals><goal>report</goal></goals>
       <configuration>
         <dataFile>${jacoco.it.exec}</dataFile>
         <outputDirectory>${project.reporting.outputDirectory}/jacoco-it
         </outputDirectory>
       </configuration>
     </execution>
     ```
   * Ergebnis: HTML landet unter `target/site/jacoco-it/index.html` und fasst nur die **Integrations**abdeckung (von Jetty) zusammen.

> Hinweis: Falls Sie auch einen **Unit-Test**-Report möchten, könnten Sie eine weitere `jacoco:report`-Execution hinzufügen, die auf die Standarddatei `target/jacoco.exec` zeigt und nach `target/site/jacoco` ausgibt – so bleiben Unit- und IT-Reports getrennt.

---

# Zu „Neu erstellen oder ersetzen?“ für die `.exec`-Dateien

* **JaCoCo-Agent-Standard ist `append=true`**.

  * Für **Unit-Tests** ist die Datei `target/jacoco.exec`. Wenn Sie `mvn verify` wiederholt **ohne `clean`** ausführen, können Daten über mehrere Läufe hinweg angehängt werden.
  * Für **Jetty-IT** überschreiben Ihre `jvmArgs` `append` nicht, daher **hängt** `target/jacoco-it.exec` ebenfalls standardmäßig an.

**Beste Praxis** (um das Vermischen alter Daten zu vermeiden):

* Führen Sie `mvn clean verify` aus, **oder** fügen Sie `append=false` in der Jetty-Agent-Zeile hinzu:

  ```xml
  -javaagent:...org.jacoco.agent-...-runtime.jar=destfile=${jacoco.it.exec},append=false
  ```
* Falls Sie jemals mehrere `.exec`-Dateien absichtlich zusammenführen möchten, verwenden Sie `jacoco:merge` vor `jacoco:report`.

---

# Was jeder relevante Block in Ihrer ursprünglichen XML macht (referenziert)

* **IT-Datei-Pfad**

  ```xml
  <properties>
    <jacoco.it.exec>${project.build.directory}/jacoco-it.exec</jacoco.it.exec>
    <it.report.skip>false</it.report.skip>
  </properties>
  ```

  Definiert, wo die Integrationsabdeckung gespeichert wird. `it.report.skip` ist deklariert, aber noch nicht in die Report-Execution eingebunden (siehe Tipp unten).

* **Unit-Test-Agent (Surefire-Pfad)**

  ```xml
  <plugin>
    <artifactId>jacoco-maven-plugin</artifactId>
    <executions>
      <execution>
        <id>prepare-agent</id>
        <goals><goal>prepare-agent</goal></goals>
      </execution>
      ...
    </executions>
  </plugin>
  ```

* **Jetty mit JaCoCo für IT**

  ```xml
  <plugin>
    <artifactId>jetty-maven-plugin</artifactId>
    ...
    <jvmArgs>
      -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec}
    </jvmArgs>
    ...
  </plugin>
  ```

* **Python-Integrationstests während Jetty läuft**

  ```xml
  <plugin>
    <artifactId>exec-maven-plugin</artifactId>
    <execution>
      <id>python-integration-tests</id>
      <phase>integration-test</phase>
      <goals><goal>exec</goal></goals>
      ...
    </execution>
  </plugin>
  ```

* **Generiert den IT-Abdeckungsreport bei verify**

  ```xml
  <execution>
    <id>report-it</id>
    <phase>verify</phase>
    <goals><goal>report</goal></goals>
    <configuration>
      <dataFile>${jacoco.it.exec}</dataFile>
      <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
    </configuration>
  </execution>
  ```

---

# Praktische Tipps / kleine Verbesserungen

* **Vermeiden Sie veraltete IT-Daten**
  Fügen Sie `append=false` zum Jetty-Agenten hinzu (oben gezeigt), oder führen Sie immer `mvn clean verify` aus.

* **Schalten Sie Ihren `it.report.skip`-Schalter ein**
  Falls Sie das Generieren des IT-Reports via Property überspringen möchten:

  ```xml
  <execution>
    <id>report-it</id>
    <phase>verify</phase>
    <goals><goal>report</goal></goals>
    <configuration>
      <skip>${it.report.skip}</skip>
      <dataFile>${jacoco.it.exec}</dataFile>
      <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
    </configuration>
  </execution>
  ```

* **Trennen Sie Unit- und IT-Reports**
  Sie haben den IT-Report bereits nach `site/jacoco-it` ausgelagert. Falls Sie auch den Unit-Report benötigen, fügen Sie einen weiteren `jacoco:report` hinzu (ohne `dataFile`-Override), der nach `site/jacoco` schreibt.

* **Multi-Modul-Hinweis**
  Dieses modul-lokale Setup berichtet die Abdeckung nur für **PlaygroundWeb**. Falls Sie später eine **kombinierte** Ansicht möchten, verwenden Sie `jacoco:merge` (um `.exec`-Dateien zu kombinieren) und/oder `report-aggregate` von einer Parent-`pom` mit `packaging=pom` (JaCoCo 0.8.8+).

---

# TL;DR

* **Unit-Tests** → `prepare-agent` injiziert JaCoCo in die Surefire-JVM → `target/jacoco.exec`.
* **Integrationstests** → Jetty startet mit eigenem JaCoCo-Agenten → `target/jacoco-it.exec`.
* **Report** → Bei `verify` rendert `jacoco:report` **nur die IT**-Abdeckung nach `target/site/jacoco-it`.
* **Dateiverhalten** → JaCoCo **hängt standardmäßig an**; bevorzugen Sie `mvn clean verify` oder `append=false`, um das Vermischen von Läufen zu vermeiden.