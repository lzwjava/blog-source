---
audio: false
generated: true
lang: de
layout: post
title: Auffinden Ihrer OpenJDK 21.0.7 Installation unter Ubuntu 22.04
translated: true
type: note
---

Der Befehl `java --version`, den Sie ausgeführt haben, zeigt, dass Sie OpenJDK 21.0.7 auf Ihrem System installiert haben, speziell die für Ubuntu 22.04 gepackte Version. Diese Ausgabe bestätigt, dass das Java Development Kit (JDK) installiert und von Ihrer Kommandozeile aus erreichbar ist.

Der Ort der Java-Installation kann typischerweise gefunden werden, indem man prüft, wo sich die `java`-Binärdatei befindet. Da Sie ein Ubuntu-basiertes System verwenden, ist OpenJDK wahrscheinlich in einem standardmäßigen Systemverzeichnis installiert, wie z.B. `/usr/lib/jvm/`.

Um den genauen Pfad der Java-Installation zu finden:

1. **Finden Sie den Pfad der `java`-Binärdatei**:
   Führen Sie den folgenden Befehl in Ihrem Terminal aus:
   ```bash
   which java
   ```
   Dies wird wahrscheinlich etwas wie `/usr/bin/java` ausgeben. Dies ist ein symbolischer Link zur eigentlichen Java-Binärdatei.

2. **Verfolgen Sie den symbolischen Link zum tatsächlichen Ort**:
   Da `/usr/bin/java` normalerweise ein Symlink ist, können Sie das tatsächliche Installationsverzeichnis finden, indem Sie ausführen:
   ```bash
   readlink -f $(which java)
   ```
   Dies könnte etwas wie `/usr/lib/jvm/java-21-openjdk-amd64/bin/java` ausgeben, was darauf hinweist, dass das JDK in `/usr/lib/jvm/java-21-openjdk-amd64/` installiert ist.

3. **Überprüfen Sie das Installationsverzeichnis**:
   Sie können die Inhalte des JVM-Verzeichnisses auflisten, um dies zu bestätigen:
   ```bash
   ls /usr/lib/jvm/
   ```
   Sie sollten ein Verzeichnis wie `java-21-openjdk-amd64` oder ähnlich sehen, das die OpenJDK-Installation enthält.

### Zusammenfassung
Ihre Java-Installation befindet sich wahrscheinlich in `/usr/lib/jvm/java-21-openjdk-amd64/` (oder einem ähnlichen Verzeichnis unter `/usr/lib/jvm/`). Der von Ihnen ausgeführte `java`-Befehl ist ein Symlink, der auf die `java`-Binärdatei in diesem Verzeichnis verweist. Wenn Sie den genauen Pfad bestätigen möchten, verwenden Sie den Befehl `readlink -f $(which java)`.