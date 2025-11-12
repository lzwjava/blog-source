---
audio: false
generated: true
lang: de
layout: post
title: Wie man die Spring Boot CLI benutzt
translated: true
type: note
---

Spring Boot CLI (Command Line Interface) ist ein leistungsstarkes Tool, mit dem Sie Spring Boot-Anwendungen direkt von der Kommandozeile aus schnell entwickeln, testen und prototypisieren können. Es ist besonders nützlich zum Ausführen von Groovy-Skripten ohne Einrichtung einer vollständigen Projektstruktur, zum Generieren neuer Projekte oder zum Experimentieren mit Spring Boot-Funktionen. Im Folgenden finden Sie eine vollständige Anleitung zur Installation und effektiven Nutzung von Spring Boot CLI.

---

## Installation
Bevor Sie Spring Boot CLI verwenden können, müssen Sie es installieren. Es gibt zwei Hauptmethoden, abhängig von Ihrem Betriebssystem:

### 1. Verwendung von SDKMAN! (Empfohlen für Unix-basierte Systeme wie Linux oder macOS)
SDKMAN! ist ein Tool zur Verwaltung von Software Development Kits und erleichtert die Installation von Spring Boot CLI.

- **Schritt 1: SDKMAN! installieren**
  Öffnen Sie Ihr Terminal und führen Sie aus:
  ```bash
  curl -s "https://get.sdkman.io" | bash
  ```
  Folgen Sie den Aufforderungen, um SDKMAN! durch Sourcing des Skripts zu initialisieren:
  ```bash
  source "$HOME/.sdkman/bin/sdkman-init.sh"
  ```

- **Schritt 2: Spring Boot CLI installieren**
  Führen Sie den folgenden Befehl aus:
  ```bash
  sdk install springboot
  ```

### 2. Manuelle Installation (Für Windows oder manuelle Einrichtung)
Wenn Sie Windows verwenden oder eine manuelle Installation bevorzugen:
- Laden Sie die Spring Boot CLI ZIP-Datei von der [offiziellen Spring-Website](https://spring.io/projects/spring-boot) herunter.
- Extrahieren Sie die ZIP-Datei in ein Verzeichnis Ihrer Wahl.
- Fügen Sie das `bin`-Verzeichnis des extrahierten Ordners zur PATH-Umgebungsvariable Ihres Systems hinzu.

### Installation überprüfen
Um zu bestätigen, dass Spring Boot CLI korrekt installiert ist, führen Sie diesen Befehl in Ihrem Terminal aus:
```bash
spring --version
```
Sie sollten die installierte Version von Spring Boot CLI sehen (z.B. `Spring CLI v3.3.0`). Wenn dies funktioniert, können Sie mit der Nutzung beginnen!

---

## Wichtige Verwendungsmöglichkeiten von Spring Boot CLI
Spring Boot CLI bietet mehrere Funktionen, die es ideal für die schnelle Entwicklung und Prototypenerstellung machen. Hier sind die Hauptverwendungsmöglichkeiten:

### 1. Ausführen von Groovy-Skripten
Eine der herausragenden Funktionen von Spring Boot CLI ist die Fähigkeit, Groovy-Skripte direkt ohne eine vollständige Projekteinrichtung auszuführen. Dies ist perfekt für schnelles Prototyping oder zum Experimentieren mit Spring Boot.

- **Beispiel: Erstellen einer einfachen Webanwendung**
  Erstellen Sie eine Datei namens `hello.groovy` mit folgendem Inhalt:
  ```groovy
  @RestController
  class HelloController {
      @RequestMapping("/")
      String home() {
          "Hello, World!"
      }
  }