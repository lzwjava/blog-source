---
audio: false
generated: true
lang: de
layout: post
title: Aktualisierung von Maven-Abhängigkeiten und Plugins
translated: true
type: note
---

Hier ist eine Liste der Versionen in Ihrer `pom.xml`, die aktualisiert werden können, zusammen mit ihren neuesten verfügbaren Versionen Stand 5. Juli 2025:

**Abhängigkeiten:**

* `org.junit.jupiter:junit-jupiter-api`
    * Aktuell: `5.9.2`
    * Neueste stabile Version: `5.13.2` (Veröffentlicht am 24. Juni 2025)
    * Neueste Vorschauversion: `6.0.0-M1` (Veröffentlicht am 27. Juni 2025) - In Betracht ziehen, falls Sie eine Milestone-Version verwenden möchten.
* `org.junit.jupiter:junit-jupiter-engine`
    * Aktuell: `5.9.2`
    * Neueste stabile Version: `5.13.2` (Veröffentlicht am 24. Juni 2025)
    * Neueste Vorschauversion: `6.0.0-M1` (Veröffentlicht am 27. Juni 2025) - In Betracht ziehen, falls Sie eine Milestone-Version verwenden möchten.

**Plugins:**

* `org.apache.maven.plugins:maven-compiler-plugin`
    * Aktuell: `3.13.0`
    * Neueste: `3.14.0` (Veröffentlicht am 17. Februar 2025)
* `org.apache.maven.plugins:maven-jar-plugin`
    * Aktuell: `3.4.2`
    * Neueste: `3.4.2` (Keine neuere stabile Version gefunden. Zuletzt veröffentlicht am 16. Juni 2024, aber das aktuelle Datum ist der 5. Juli 2025, daher ist diese Version immer noch aktuell).
* `com.diffplug.spotless:spotless-maven-plugin`
    * Aktuell: `2.44.5`
    * Neueste: `2.44.5` (Keine neuere stabile Version gefunden. Zuletzt veröffentlicht am 28. Mai 2025, daher ist diese Version immer noch aktuell).
* `org.apache.maven.plugins:maven-checkstyle-plugin`
    * Aktuell: `3.6.0`
    * Neueste: `3.6.0` (Keine neuere stabile Version gefunden. Zuletzt veröffentlicht am 22. Oktober 2024, daher ist diese Version immer noch aktuell).
    * **Hinweis:** Die `checkstyle`-Abhängigkeit innerhalb der Checkstyle-Plugin-Konfiguration kann aktualisiert werden:
        * Aktuell: `10.25.0`
        * Neueste: `10.26.1` (Veröffentlicht am 29. Juni 2025)
* `org.apache.maven.plugins:maven-surefire-plugin`
    * Aktuell: `3.0.0-M7`
    * Neueste stabile Version: `3.5.3` (Veröffentlicht am 27. März 2025) - Dies ist ein signifikanter Sprung von einer Milestone-Version.
* `org.codehaus.mojo:exec-maven-plugin`
    * Aktuell: `3.5.1`
    * Neueste: `3.5.1` (Keine neuere stabile Version gefunden. Zuletzt veröffentlicht am 27. Mai 2025, daher ist diese Version immer noch aktuell).

**Zusammenfassung der Aktualisierungen:**

* **JUnit Jupiter API:** 5.9.2 -> 5.13.2 (oder 6.0.0-M1)
* **JUnit Jupiter Engine:** 5.9.2 -> 5.13.2 (oder 6.0.0-M1)
* **Maven Compiler Plugin:** 3.13.0 -> 3.14.0
* **Checkstyle (Abhängigkeit innerhalb des Plugins):** 10.25.0 -> 10.26.1
* **Maven Surefire Plugin:** 3.0.0-M7 -> 3.5.3

**Wichtige Überlegungen vor der Aktualisierung:**

* **Breaking Changes:** Überprüfen Sie immer die Release Notes für jede Komponente, die Sie aktualisieren möchten. Hauptversionssprünge (wie von JUnit 5 zu 6 oder Surefire 3.0.0-M7 zu 3.5.3) könnten Breaking Changes einführen, die Codeänderungen erfordern.
* **Kompatibilität:** Stellen Sie sicher, dass die neuen Versionen mit Ihrer Java-Version (in Ihrem Fall JDK 21) und anderen Abhängigkeiten in Ihrem Projekt kompatibel sind.
* **Tests:** Führen Sie nach der Aktualisierung gründliche Tests Ihrer Anwendung durch, um sicherzustellen, dass alles weiterhin wie erwartet funktioniert.