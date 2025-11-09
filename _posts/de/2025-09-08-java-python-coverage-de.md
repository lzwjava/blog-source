---
audio: false
date: 2025-09-08
generated: true
image: false
lang: de
layout: post
title: Mehrmodulige Java-Abdeckung mit Python
translated: true
type: note
---

Bei Ihrer Einrichtung haben Sie es mit einer komplexen, aber interessanten Herausforderung zu tun: die Verwendung von Python-Integrationstests, um Coverage für ein Multi-Modul-Java-Projekt zu generieren. Lassen Sie mich die Situation analysieren und eine umfassende Strategie vorschlagen.

## Aktuelle Herausforderungen

1.  **Sprachübergreifende Tests**: Python-Tests, die Java-Code ausführen
2.  **Multi-Modul-Coverage**: Erfassung der Coverage über alle Module hinweg aus Integrationstests
3.  **Modul-Interdependenzen**: `PlaygroundUtils` hat keine direkten Endpunkte, wird aber durch `PlaygroundWeb` ausgeführt
4.  **Skalierbarkeitsbedenken**: Umgang mit 10+ Modulen

## Empfohlene Strategie

### Option 1: Einzelner JaCoCo-Agent, zusammengeführter Report (Empfohlen)

Dies ist der skalierbarste Ansatz für Ihren Anwendungsfall:

## Wichtige Verbesserungen und Strategie

### 1. **Ansatz mit Einzelnem JaCoCo-Agent**
- Verwenden Sie EINE `jacoco-it.exec`-Datei auf der übergeordneten Ebene
- Konfigurieren Sie den Agent mit `append=true` und `includes=org.lzw.*`
- Dies erfasst die Coverage ALLER Module in einem Durchgang

### 2. **Report-Aggregation**
- Verwenden Sie `jacoco:report-aggregate`, um einen einheitlichen Report zu erstellen
- Dies findet automatisch alle Modulklassen und generiert die Coverage für diese

### 3. **Profilbasierte Ausführung**
- Trennen Sie die Zuständigkeiten: `run-integration-tests`-Profil zum Ausführen der Tests
- `integration-test-coverage`-Profil zum Generieren der Reports
- Macht den Build modularer und wartungsfreundlicher

### 4. **Skalierbarkeit für 10+ Module**

Für größere Projekte sollten Sie diesen erweiterten Ansatz in Betracht ziehen:

## Zusammenfassung und Best Practices

### Für Ihr aktuelles 2-Modul-Setup:
1.  **Verwenden Sie eine einzelne JaCoCo-Exec-Datei** auf der übergeordneten Ebene mit `append=true`
2.  **Starten Sie Jetty einmal** mit dem konfigurierten Agenten, um alle Module zu erfassen
3.  **Verwenden Sie `report-aggregate`**, um einen einheitlichen Report zu generieren

### Für die Skalierung auf 10+ Module:
1.  **Modul-Gruppierung**: Erstellen Sie logische Gruppen (Core, Service, Web) und generieren Sie separate Reports
2.  **Coverage-Tracking**: Implementieren Sie einen Python-Helfer, um zu verfolgen, welche Module abgedeckt sind
3.  **Paralleles Testen**: Führen Sie verschiedene Test-Suiten parallel für schnellere Rückmeldung aus
4.  **Inkrementelle Coverage**: Verwenden Sie Maven-Profile, um die Coverage für bestimmte Modulgruppen auszuführen

### Wichtige Konfigurationspunkte:
-   **`append=true`**: Stellt sicher, dass mehrere Testläufe die Coverage akkumulieren
-   **`includes=org.lzw.*`**: Erfasst alle Ihre Module in einem Agenten
-   **Profil-Trennung**: Halten Sie Integrationstests getrennt von regulären Builds
-   **Einzelne Exec-Datei**: Beseitigt die Notwendigkeit, Jetty mehrmals zu starten

### Kommandozeilen-Verwendung:
```bash
# Vollständige Coverage mit Integrationstests
mvn clean verify -Prun-integration-tests,integration-test-coverage

# Nur Unit-Test-Coverage
mvn clean test

# Coverage für eine bestimmte Modulgruppe
mvn clean verify -Pcoverage-by-layer
```

Dieser Ansatz skaliert gut, weil:
1.  Sie Jetty unabhängig von der Modulanzahl nur einmal starten/stoppen
2.  JaCoCo automatisch Multi-Modul-Klassendateien behandelt
3.  Die Python-Tests die Java-Modulstruktur nicht kennen müssen
4.  Reports je nach Zielgruppe aggregiert oder aufgeteilt werden können

Die entscheidende Erkenntnis ist, dass der JaCoCo-Agent die Coverage für ALLE Klassen in der JVM erfassen kann, nicht nur für das getestete Modul. Durch die Verwendung einer gemeinsamen Exec-Datei und des Aggregate-Goals erhalten Sie vollständige Coverage-Daten in einem einzigen Testlauf.