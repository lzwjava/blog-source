---
audio: false
date: 2025-09-07
generated: true
image: false
lang: de
layout: post
title: Behebung fehlender JaCoCo-Ausführungsdatendatei
translated: true
type: note
---

Um die JaCoCo-Ausführungsdatendatei, oft als **'.exec'-Datei** bezeichnet, zu generieren, müssen Sie Ihre Tests mit dem angehängten JaCoCo-Agenten ausführen. Die Log-Meldung "Skipping JaCoCo execution due to missing execution data file" zeigt an, dass das `report`-Ziel ausgeführt wurde, ohne dass das `prepare-agent`-Ziel zuvor erfolgreich ausgeführt wurde.

-----

### Schritt 1: Konfigurieren Sie das JaCoCo Maven Plugin

Stellen Sie zunächst sicher, dass Ihre `pom.xml`-Datei das JaCoCo Maven Plugin korrekt konfiguriert hat. Es sollte in etwa so aussehen:

```xml
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.12</version>
    <executions>
        <execution>
            <goals>
                <goal>prepare-agent</goal>
            </goals>
        </execution>
        <execution>
            <id>report</id>
            <phase>test</phase>
            <goals>
                <goal>report</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

Das **`prepare-agent`**-Ziel ist entscheidend, da es den JaCoCo-Laufzeitagenten einrichtet. Dieser Agent instrumentiert Ihren Code während des Testlaufs, um die Abdeckungsdaten zu sammeln.

-----

### Schritt 2: Führen Sie die Tests aus

Nach der Konfiguration des Plugins führen Sie Ihren Maven-Build aus. Der typische Befehl zum Ausführen der Tests und Generieren des Berichts lautet:

`mvn clean install`

Wenn Sie diesen Befehl ausführen, führt Maven zuerst das `prepare-agent`-Ziel aus, das den JaCoCo-Agenten an die JVM anhängt. Wenn dann die `test`-Phase läuft, zeichnet der Agent die Code-Abdeckungsdaten auf und speichert sie in einer Datei, typischerweise unter **`target/jacoco.exec`**. Anschließend wird das `report`-Ziel ausgeführt, das diese `.exec`-Datei liest und die endgültigen HTML- oder XML-Berichte generiert.

Wenn Sie weiterhin Probleme haben, überprüfen Sie Folgendes:

  * **Projektstruktur**: Stellen Sie sicher, dass sich Ihre Tests im standardmäßigen Maven-Verzeichnis `src/test/java` befinden.
  * **Testfehler**: Wenn Ihre Tests fehlschlagen, könnte der Build anhalten, bevor die `.exec`-Datei generiert werden kann. Beheben Sie zuerst alle Testfehler.
  * **Versionskonflikt**: Stellen Sie sicher, dass die JaCoCo Plugin-Version mit Ihren Maven- und Java-Versionen kompatibel ist.