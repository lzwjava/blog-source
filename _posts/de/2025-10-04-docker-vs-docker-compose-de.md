---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Docker versus Docker Compose Unterschiede
translated: true
type: note
---

### Docker vs. Docker Compose: Hauptunterschiede

Docker und Docker Compose sind verwandt, erfüllen aber unterschiedliche Zwecke in Containerisierungs-Workflows. Docker ist die grundlegende Technologie, während Docker Compose darauf aufbaut, um komplexere Setups zu ermöglichen.

#### Was ist Docker?
Docker ist eine Plattform zur Entwicklung, Auslieferung und Ausführung von Anwendungen in leichtgewichtigen, portablen **Containern**. Diese Container packen eine App mit all ihren Abhängigkeiten (Code, Laufzeitumgebung, Bibliotheken usw.) zusammen und stellen so sicher, dass sie konsistent in verschiedenen Umgebungen wie Entwicklung, Testing und Produktion läuft. Man interagiert mit Docker hauptsächlich über die Kommandozeilenschnittstelle (CLI) mittels Befehlen wie `docker run`, `docker build` und `docker ps`, um einzelne Container zu verwalten.

#### Was ist Docker Compose?
Docker Compose ist ein Orchestrierungstool, das Docker erweitert, um **Multi-Container-Anwendungen** zu handhaben. Es verwendet eine einfache YAML-Datei (typischerweise `docker-compose.yml`), um den gesamten Anwendungs-Stack zu definieren – einschließlich mehrerer Services, Netzwerke, Volumes und Umgebungsvariablen. Anstatt Dutzende von `docker run`-Befehlen zu jonglieren, kann man alles mit einem einzigen Befehl, `docker-compose up`, starten.

#### Hauptunterschiede
Hier ein kurzer Vergleich:

| Aspekt               | Docker                                | Docker Compose                            |
|----------------------|---------------------------------------|-------------------------------------------|
| **Hauptfokus**       | Bauen, Ausführen und Verwalten von **einzelnen Containern** | Definieren und Orchestrieren von **Multi-Container-Apps** |
| **Konfiguration**    | Inline-CLI-Flags (z.B. `docker run -p 80:80 image`) | YAML-Datei für deklarative Einrichtung (Services, Ports, Volumes) |
| **Befehle**          | `docker run`, `docker build`, etc.    | `docker-compose up`, `down`, `scale`, etc. |
| **Umfang**           | Low-Level-Container-Lebenszyklus      | High-Level-Anwendungs-Stacks (z.B. App + DB + Cache) |
| **Netzwerk/Abhäng.** | Manuelle Einrichtung pro Container    | Automatisch (z.B. können Services sich gegenseitig per Namen referenzieren) |
| **Anwendungsfall**   | Einfache, isolierte Services          | Komplexe Apps wie Webserver mit Datenbanken |

Kurz gesagt: Docker ist wie ein Einmotorenfahrzeug für eine Aufgabe, während Docker Compose ein Flottenmanager ist, der mehrere Fahrzeuge für eine Reise koordiniert.

### Warum brauchen wir Docker Compose?
Während Docker allein für Single-Container-Apps leistungsstark ist, umfassen Anwendungen in der realen Welt oft mehrere miteinander verbundene Komponenten (z.B. ein Frontend, Backend-API, Datenbank und Redis-Cache). Hier ist der Grund, warum Docker Compose unerlässlich ist:

- **Vereinfacht die Verwaltung mehrerer Container**: Ohne Compose müsste man Container manuell starten/stoppen, Netzwerke konfigurieren und Abhängigkeiten über wiederholte CLI-Befehle handhaben – was unübersichtlich und fehleranfällig wird. Compose automatisiert dies mit einer Datei und einem Befehl.

- **Reproduzierbarkeit und Zusammenarbeit**: Die YAML-Datei dient als Blaupause. Teammitglieder können exakt die gleiche Umgebung mit `docker-compose up` hochfahren, was die Entwicklung konsistent und portabel macht (großartig für CI/CD-Pipelines).

- **Effizienz in der Entwicklung**: Funktionen wie Service-Linking (z.B. Ihre App verbindet sich automatisch mit einer Datenbank über einen Hostnamen) und Volume-Mounting für Live-Code-Neuladung beschleunigen die Iteration. Man kann Services auch skalieren (z.B. `docker-compose scale web=3`), ohne Images neu zu bauen.

- **Umgebungsisolation**: Es erstellt isolierte Netzwerke und Volumes pro Projekt und vermeidet so Konflikte, wenn mehrere Apps lokal laufen.

Im Wesentlichen verwandelt Docker Compose Docker von einem Solo-Tool in einen Teamplayer für moderne, microservice-basierte Architekturen. Wenn Sie gerade erst anfangen, probieren Sie eine einfache `docker-compose.yml` für einen WordPress + MySQL Stack aus, um den Zauber zu sehen.

#### Referenzen
- [Docker vs. Docker Compose: Simple and Fun Explanation](https://medium.com/@ShantKhayalian/docker-vs-docker-compose-simple-and-fun-explanation-4811582127f7)
- [What is the difference between docker and docker-compose](https://stackoverflow.com/questions/37966552/what-is-the-difference-between-docker-and-docker-compose)
- [How To Choose Between Docker Compose vs Docker?](https://cyberpanel.net/blog/docker-compose-vs-docker)
- [Docker Compose - What is It, Example & Tutorial](https://spacelift.io/blog/docker-compose)