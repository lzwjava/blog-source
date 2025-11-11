---
audio: false
generated: true
lang: de
layout: post
title: GraalVM
translated: true
type: note
---

GraalVM ist eine **leistungsstarke, polyglotte Laufzeitumgebung**, die es ermöglicht, Anwendungen in verschiedenen Programmiersprachen wie Java, JavaScript, Python, Ruby, R und auf dem LLVM-Framework basierenden Sprachen (wie C und C++) in einer einzigen Umgebung auszuführen. Sie wird von Oracle entwickelt und basiert auf der Java HotSpot Virtual Machine.

Hier eine Aufschlüsselung der wichtigsten Funktionen und Vorteile:

**1. Polyglottismus:**

* GraalVM ermöglicht nahtlose Interoperabilität zwischen verschiedenen Programmiersprachen. Sie können Code, der in einer Sprache geschrieben ist, in eine Anwendung einbetten, die in einer anderen Sprache geschrieben wurde. Zum Beispiel können Sie eine Java-Anwendung haben, die Python-Skripte oder Node.js-Module ausführt.
* Dies eröffnet Möglichkeiten, die Stärken verschiedener Sprachen innerhalb einer einzelnen Anwendung zu nutzen.

**2. Native Image-Erstellung:**

* Eine der bedeutendsten Funktionen von GraalVM ist die Fähigkeit, Java-Anwendungen ahead-of-time (AOT) in **native Executables** zu kompilieren.
* Dieser Prozess eliminiert die Notwendigkeit einer traditionellen JVM zum Ausführen der Anwendung. Das resultierende native Image enthält alles, was die Anwendung zum Ausführen benötigt, einschließlich der notwendigen Teile der Laufzeitumgebung.
* **Vorteile von Native Images:**
    * **Schnellere Startzeit:** Native Executables starten fast sofort, was für Cloud-native Anwendungen und Microservices entscheidend ist.
    * **Geringerer Speicherbedarf:** Native Images verbrauchen typischerweise deutlich weniger Speicher im Vergleich zur Ausführung auf einer JVM.
    * **Reduzierte Angriffsfläche:** Durch das Ausschließen von ungenutztem Code und der JIT-Kompilierungsinfrastruktur können native Images die Sicherheit verbessern.
    * **Kleinere Bereitstellungsgröße:** Native Executables sind oft kleiner und einfacher zu paketieren und bereitzustellen.

**3. Hohe Leistung:**

* GraalVM enthält einen fortschrittlichen Optimizing Compiler, ebenfalls Graal genannt, der die Leistung von Anwendungen, einschließlich solcher, die auf der JVM laufen, erheblich verbessern kann.
* Für polyglotte Anwendungen strebt GraalVM eine Leistung an, die mit sprachspezifischen Laufzeitumgebungen vergleichbar oder besser ist.

**4. Einbettbarkeit:**

* GraalVM kann in andere Anwendungen eingebettet werden. Zum Beispiel können Sie die GraalVM JavaScript-Engine in eine Java-Anwendung integrieren, um Skripting-Fähigkeiten bereitzustellen.

**5. Anwendungsfälle:**

* **Microservices:** Native Images sind ideal für den Aufbau schnell startender und ressourceneffizienter Microservices für Cloud-Umgebungen.
* **Serverless Functions:** Die schnelle Startzeit macht GraalVM zu einer ausgezeichneten Wahl für serverlose Funktionen, bei denen Cold Starts ein Problem darstellen können.
* **Polyglotte Anwendungen:** Anwendungen, die Code aus mehreren Programmiersprachen nutzen müssen.
* **Verbesserung der Leistung bestehender Java-Anwendungen:** Durch die Verwendung des Graal-Compilers als JIT-Compiler innerhalb einer Standard-JVM.
* **Erstellung von Sprachlaufzeitumgebungen und Tools:** Das Truffle-Framework innerhalb von GraalVM ermöglicht es Entwicklern, hochperformante Interpreter für neue oder bestehende Programmiersprachen zu bauen.

**6. Open Source:**

* GraalVM Community Edition ist ein Open-Source-Projekt, das für eine breite Palette von Benutzern und Entwicklern zugänglich ist. Es gibt auch eine Enterprise Edition mit zusätzlichen Funktionen und Support.

Zusammenfassend ist GraalVM eine vielseitige und leistungsstarke Laufzeitumgebung, die erhebliche Vorteile in Bezug auf Leistung, Ressourceneffizienz und die Fähigkeit, mit mehreren Programmiersprachen zu arbeiten, bietet. Ihre Fähigkeit zur Erstellung nativer Images ist besonders überzeugend für die moderne Cloud-native Entwicklung.