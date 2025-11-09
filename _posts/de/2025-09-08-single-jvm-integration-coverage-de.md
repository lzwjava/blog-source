---
audio: false
date: 2025-09-08
generated: true
image: false
lang: de
layout: post
title: Integrationsabdeckungsstrategie für eine einzelne JVM
translated: true
type: note
---

Du musst Jetty nicht zweimal ausführen oder eine separate JaCoCo `.exec` pro Modul erstellen. Ein Agent auf der einzelnen JVM, die dein WAR bereitstellt, kann die Abdeckung **aller Klassen, die diese JVM lädt** – inklusive `PlaygroundUtils` – in **eine gemeinsame exec-Datei** aufzeichnen. Dann kann jedes Modul seinen eigenen Bericht generieren, indem es auf dieselbe exec-Datei verweist. Für einen großen Reaktor (10+ Module) skaliert das sauber.

Unten findest du einen konkreten, minimalen Plan und direkte Änderungen für dein Repository.

---

## Die Strategie

1. **Verwende eine einzelne, gemeinsame IT-exec-Datei auf der Eltern-Ebene.**
   Starte Jetty **einmal**, instrumentiert mit JaCoCo, das in `../target/it-coverage/jacoco-it.exec` schreibt (ein pfadbezogener Pfad).
2. **Führe deine externen Python-Tests einmal aus.**
   Sie rufen die bereitgestellte App auf; der Agent zeichnet Treffer für alle geladenen Klassen (Web + Bibliotheken) auf.
3. **Generiere pro-Modul-Berichte**, wobei jedes Modul auf die gemeinsame `jacoco-it.exec` verweist.
   `PlaygroundUtils` erhält einen Bericht, obwohl es keine Tests hat – es ordnet die gemeinsame exec-Datei seinen eigenen `target/classes` zu.
4. (Optional) **Generiere auch einen aggregierten HTML-Bericht** auf der Eltern-Ebene mit `report-aggregate`, oder behalte einfach die pro-Modul-Berichte.

Nur wenn du tatsächlich **mehrere JVMs** hast (z.B. mehrere Microservices), benötigst du mehrere exec-Dateien und einen `jacoco:merge`-Schritt. Für deinen aktuellen Single-JVM (Jetty) Build, belasse es bei einer exec-Datei.

---

## Genaue Änderungen

### 1) Eltern-`pom.xml` (PlaygroundLib)

Füge gemeinsame Properties hinzu, damit jedes Modul auf dieselbe exec-Datei verweisen kann:

```xml
<properties>
  <!-- ... deine vorhandenen Versionen ... -->
  <it.coverage.dir>${project.basedir}/target/it-coverage</it.coverage.dir>
  <jacoco.it.exec>${it.coverage.dir}/jacoco-it.exec</jacoco.it.exec>
  <!-- Schaltet die pro-Modul IT-Berichterstellung um -->
  <it.report.skip>false</it.report.skip>
</properties>
```

(Optional) Wenn du einen einzelnen **aggregierten** HTML-Bericht auf der Eltern-Ebene möchtest, füge diese Execution hinzu:

```xml
<build>
  <pluginManagement>
    <!-- behalte deine vorhandenen Blöcke -->
  </pluginManagement>

  <plugins>
    <plugin>
      <groupId>org.jacoco</groupId>
      <artifactId>jacoco-maven-plugin</artifactId>
      <executions>
        <execution>
          <id>it-aggregate-report</id>
          <phase>verify</phase>
          <goals>
            <goal>report-aggregate</goal>
          </goals>
          <configuration>
            <!-- Verwende die gemeinsame IT-exec, die durch den Jetty-Run erzeugt wurde -->
            <dataFile>${jacoco.it.exec}</dataFile>
            <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
          </configuration>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

> Falls deine JaCoCo-Version `<dataFile>` bei `report-aggregate` ablehnt, überspringe diesen optionalen Block und verlasse dich auf die pro-Modul-Berichte unten. Du kannst später immer noch ein kleines "Coverage"-Aggregator-Modul hinzufügen, um `merge` + `report` auszuführen.

---

### 2) `PlaygroundWeb/pom.xml`

Richte den Jetty-Agenten auf den **eltern-Ebene**-exec-Pfad aus und aktiviere append:

```xml
<plugin>
  <groupId>org.eclipse.jetty</groupId>
  <artifactId>jetty-maven-plugin</artifactId>
  <executions>
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals><goal>start</goal></goals>
      <configuration>
        <daemon>true</daemon>
        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${project.parent.basedir}/target/it-coverage/jacoco-it.exec,append=true,includes=org.lzw.*
        </jvmArgs>
        <httpConnector>
          <port>8080</port>
          <host>127.0.0.1</host>
        </httpConnector>
        <webApp><contextPath>/</contextPath></webApp>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
      </configuration>
    </execution>

    <execution>
      <id>stop-jetty</id>
      <phase>post-integration-test</phase>
      <goals><goal>stop</goal></goals>
      <configuration>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <stopWait>15</stopWait>
      </configuration>
    </execution>
  </executions>
</plugin>
```

Aktualisiere deinen `jacoco:report` in `PlaygroundWeb`, damit er **dieselbe** gemeinsame exec-Datei liest:

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <executions>
    <execution>
      <id>report-it</id>
      <phase>verify</phase>
      <goals><goal>report</goal></goals>
      <configuration>
        <dataFile>${project.parent.basedir}/target/it-coverage/jacoco-it.exec</dataFile>
        <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
      </configuration>
    </execution>
  </executions>
</plugin>
```

Dein vorhandener Exec Maven Plugin, der `python -m unittest discover tests -v` ausführt, ist perfekt – lasse ihn unverändert.

---

### 3) `PlaygroundUtils/pom.xml`

Füge eine **nur-Bericht**-Execution hinzu, damit es die gemeinsame exec-Datei seinen eigenen Klassen zuordnen kann:

```xml
<build>
  <plugins>
    <!-- behalte deine vorhandenen Plugins -->

    <plugin>
      <groupId>org.jacoco</groupId>
      <artifactId>jacoco-maven-plugin</artifactId>
      <executions>
        <execution>
          <id>report-it</id>
          <phase>verify</phase>
          <goals><goal>report</goal></goals>
          <configuration>
            <dataFile>${project.parent.basedir}/target/it-coverage/jacoco-it.exec</dataFile>
            <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
            <skip>${it.report.skip}</skip>
          </configuration>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

Dieses Modul startet nie Jetty oder führt Python aus; es konsumiert nur die gemeinsame exec-Datei und seine eigenen `target/classes`. Falls irgendwelche `PlaygroundUtils`-Klassen während der Tests von der Web-App verwendet werden, werden sie mit Coverage angezeigt. Wenn sie nicht ausgeführt werden, werden sie 0% anzeigen – was das korrekte Signal ist.

---

## Wie du es ausführst

Vom Repository-Stammverzeichnis aus:

```bash
mvn -pl PlaygroundWeb -am clean verify
```

Die Build-Reihenfolge kompiliert beide Module, startet Jetty einmal mit dem Agenten, führt deine Python-Tests aus, stoppt Jetty und generiert dann:

* `PlaygroundWeb/target/site/jacoco-it/index.html`
* `PlaygroundUtils/target/site/jacoco-it/index.html`
* Optional einen aggregierten Bericht unter dem Eltern-Verzeichnis, falls du `report-aggregate` aktiviert hast.

---

## Wenn du 10 Module hast

* Wenn alle 10 im **selben WAR/JVM** landen, behalte das **Single-Shared-exec**-Muster bei. Jedes Modul fügt eine `report`-Execution hinzu, die auf die gemeinsame exec-Datei verweist. Du startest Jetty immer noch einmal und führst die Python-Tests einmal aus.

* Wenn du **mehrere JVMs** hast (z.B. separate Services), gib jeder JVM ihre eigene `destfile` (z.B. `it-coverage/serviceA.exec`, `serviceB.exec`), führe dann im Eltern-Verzeichnis aus:

  ```xml
  <plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <executions>
      <execution>
        <id>merge-it</id>
        <phase>post-integration-test</phase>
        <goals><goal>merge</goal></goals>
        <configuration>
          <destFile>${project.basedir}/target/it-coverage/jacoco-merged.exec</destFile>
          <files>
            <file>${project.basedir}/target/it-coverage/serviceA.exec</file>
            <file>${project.basedir}/target/it-coverage/serviceB.exec</file>
            <!-- bei Bedarf weitere hinzufügen -->
          </files>
        </configuration>
      </execution>

      <execution>
        <id>aggregate-report</id>
        <phase>verify</phase>
        <goals><goal>report-aggregate</goal></goals>
        <configuration>
          <dataFile>${project.basedir}/target/it-coverage/jacoco-merged.exec</dataFile>
          <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
        </configuration>
      </execution>
    </executions>
  </plugin>
  ```

* Wenn du Rauschen begrenzen willst, setze `includes=org.lzw.*` (bereits gezeigt) oder füge `excludes` zur Agenten-Zeile hinzu, um Third-Party-Bibliotheken auszufiltern.

---

## Warum dein aktueller Schmerz auftritt

* Du hast **pro-Modul-exec-Dateien** erstellt, also fühltest du dich gezwungen, Jetty mit verschiedenen Agenten neu zu starten, um jede zu füllen. Das ist unnötig. Dem Agenten ist es egal, zu welchem Modul eine Klasse "gehört" – er zeichnet jede geladene Klasse auf. Zentralisiere die exec-Datei und lasse jedes Modul seinen `report` darauf verweisen.

---

## Schnell-Checkliste

* Eine **gemeinsame** `${jacoco.it.exec}` unter dem Eltern-Verzeichnis.
* Jetty **einmal** gestartet mit `append=true` und `includes=org.lzw.*`.
* Python-Tests **einmal** ausgeführt.
* Jedes Modul hat einen `jacoco:report`, der die gemeinsame exec-Datei liest.
* Optionaler Eltern-`report-aggregate` für eine einzige übergreifende HTML-Datei.

Das sollte dein Setup sowohl einfacher als auch skalierbarer machen. Falls du möchtest, kann ich genaue Diffs für deine aktuellen POMs mit diesen angewendeten Änderungen erstellen.