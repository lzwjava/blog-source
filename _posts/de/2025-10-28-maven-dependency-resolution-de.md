---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Maven Multi-Module-Abhängigkeitsauflösung
translated: true
type: note
---

Ja, das ist korrekt – in einem Maven-Multi-Modul-Projekt, wenn ein Modul (z.B. ein EAR-Modul) von einem anderen Modul (z.B. einem WAR-Modul) abhängt, löst Maven die Abhängigkeit standardmäßig aus dem lokalen `.m2/repository`-Verzeichnis auf, nicht direkt aus dem `target/`-Verzeichnis des anderen Moduls. Das liegt daran, dass Maven Abhängigkeiten zwischen Modulen als standardmäßige Artefaktreferenzen behandelt (wie externe Bibliotheken), daher muss das abhängige Artefakt installiert sein (oder zumindest packaged und über den Build-Reaktor auffindbar).

### Warum das passiert
- **Lokale Repository-Auflösung**: Mavens Abhängigkeitsauflösungsmechanismus sucht zuerst nach Artefakten im lokalen Repository. Das `target/`-Verzeichnis wird nur temporär während des Builds eines einzelnen Moduls verwendet, aber für modulübergreifende Referenzen erwartet es, dass das Artefakt "veröffentlicht" (installiert) ist.
- **Reaktor-Builds helfen, sind aber nicht immer ausreichend**: Wenn Sie `mvn package` (oder `mvn install`) aus dem **Parent-POM**-Stammverzeichnis ausführen, baut Mavens Reaktor die Module automatisch in topologischer Reihenfolge. Es löst modulübergreifende Abhängigkeiten on-the-fly ohne explizite Installationen auf und bezieht die Ausgabe aus dem frischen `target/`-Verzeichnis des anderen Moduls während der Sitzung. Aber wenn Sie das abhängige Modul (z.B. EAR) **unabhängig** bauen (z.B. `cd ear-module && mvn package`), wird es den `target/` des WAR-Moduls nicht sehen – es schlägt fehl, es sei denn, das WAR-Artefakt befindet sich bereits in `.m2`.

### Speziell für WAR-zu-EAR-Packaging
In einem EAR-Projekt:
- Das EAR-Plugin (`maven-ear-plugin`) erwartet das WAR (und andere Module) als aufgelöste Artefakte, die in das EAR-Archiv aufgenommen werden sollen (z.B. über `<modules>` in der EAR-POM).
- Wenn das WAR nicht installiert ist, erhalten Sie Fehler wie "Could not resolve dependencies" oder fehlende Module im EAR.

**Lösung**: Ja, im Allgemeinen müssen Sie `mvn install` (oder zumindest `mvn package` in einem vollständigen Reaktor-Build) auf dem "ursprünglichen" (Abhängigkeits-) Modul zuerst ausführen, wenn Sie unabhängig bauen. Best Practices:
1. **Bevorzugt: Bauen vom Parent aus**: `mvn clean install` im Projektstammverzeichnis. Dies installiert alles in `.m2` und behandelt die Reihenfolge automatisch.
2. **Wenn Module separat gebaut werden**:
   - `cd war-module && mvn clean install` (installiert das WAR-JAR in `.m2`).
   - Dann `cd ear-module && mvn clean package` (oder `install` – EARs benötigen oft nur `package`).
3. **Direkte Target-Referenzen vermeiden**: Umgehen Sie dies nicht mit `<systemPath>` oder Dateipfaden zu `target/` – das ist fehleranfällig und umgeht Mavens Checksummen/Transitivität.

Dieses Verhalten hat sich in den letzten Maven-Versionen (bis zu 3.9.x Stand 2025) nicht geändert. Für weitere Details siehe den offiziellen Multi-Modul-Leitfaden.

[Introduction to the Build Lifecycle - Multi-module Projects](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html#multi-module)
[Maven EAR Plugin Documentation](https://maven.apache.org/plugins/maven-ear-plugin/ear-mojo.html)