---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: GraalVM Native Image Überblick
translated: true
type: note
---

### Was ist Native Image in GraalVM?

Im Kontext der Einführung von GraalVM bezieht sich **Native Image** auf eine Funktion, die Java- (oder andere JVM-basierte) Anwendungen Ahead-of-Time (AOT) in eigenständige, native ausführbare Binärdateien kompiliert. Diese Ausführbaren werden direkt auf dem Host-Rechner ausgeführt, ohne zur Laufzeit eine Java Virtual Machine (JVM) zu benötigen. Im Wesentlichen ist es eine Möglichkeit, Ihren Java-Code in etwas ähnliches wie einen nativen C/C++-Binary zu verwandeln, jedoch erstellt aus Hochsprachen wie Java, Kotlin oder Scala.

#### Wichtige Technologie dahinter
- **GraalVM Compiler**: Native Image nutzt den GraalVM-Compiler (einen fortschrittlichen, optimierenden Compiler für die JVM), um eine statische Analyse und AOT-Kompilierung durchzuführen. Während des Build-Prozesses:
  1. **Statische Analyse**: Er durchsucht Ihre gesamte Anwendung (einschließlich Abhängigkeiten), um alle erreichbaren Codepfade, Klassen, Methoden und Ressourcen zu identifizieren. Dies schafft eine "Closed-World"-Annahme, die dynamisches Verhalten zur Build-Zeit auflöst.
  2. **Partielle Auswertung**: Der Compiler wertet Teile des Codes symbolisch aus (z.B. Reflection, dynamisches Klassenladen) ahead-of-time und ersetzt sie durch optimierten Maschinencode.
  3. **Code-Generierung**: Er generiert eine native ausführbare Datei unter Verwendung einer Low-Level Virtual Machine (LLVM) oder SubstrateVM (der eingebetteten VM von GraalVM), um plattformspezifische Binärdateien zu erzeugen (z.B. für Linux, Windows, macOS oder sogar Embedded Systems).
  
- **SubstrateVM**: Dies ist die zugrundeliegende Laufzeitumgebung unter Native Image. Es ist eine schlanke, einbettbare VM, die JVM-Funktionen entfernt, die für AOT nicht benötigt werden (wie Just-in-Time-Kompilierung), und nur das einbindet, was statisch mit Ihrer App verlinkt ist.

Das Ergebnis ist eine eigenständige Binärdatei – keine externe JVM, keine JRE-Installation erforderlich. Tools wie die `native-image` CLI oder Maven/Gradle-Plugins übernehmen den Build-Vorgang.

#### Vorteile und Kompromisse
- **Vorteile**:
  - **Sofortiger Start**: Millisekunden statt Sekunden (ideal für Serverless/Microservices).
  - **Geringerer Speicherbedarf**: Oft nur 1/10 der Nutzung einer JVM.
  - **Kleinere Bereitstellungsgröße**: Einzelne Datei, keine Classpath-Probleme.
- **Nachteile**:
  - **Build-Zeit**: Kann für große Anwendungen aufgrund der Analyse Minuten bis Stunden dauern.
  - **Eingeschränkte dynamische Features**: Dinge wie Dynamic Proxies oder spät gebundenes Reflection benötigen eine explizite Konfiguration (über Metadatendateien).
  - **Plattformspezifisch**: Binärdateien sind an das Betriebssystem/die Architektur der Build-Maschine gebunden.

Diese Technologie ist beliebt für Cloud-native Apps, Container (z.B. Docker-Images unter 50MB) und Edge Computing.

Weitere Details finden Sie in der offiziellen GraalVM-Dokumentation: [GraalVM Native Image Guide](https://www.graalvm.org/latest/reference-manual/native-image/).