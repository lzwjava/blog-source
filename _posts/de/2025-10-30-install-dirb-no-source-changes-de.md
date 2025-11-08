---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Installieren von DirB ohne Quellcodeänderungen
translated: true
type: note
---

### Alternativen zur Modifikation des DirB-Quellcodes

Wenn das Bearbeiten des Quellcodes (wie z.B. `variables.h`) keine Option ist – vielleicht aufgrund eines schreibgeschützten Setups, Richtlinien oder einfach Präferenz – hier sind unkomplizierte Wege, um DirB ohne Kompilierung zum Laufen zu bringen. Diese nutzen vorgefertigte Pakete oder Neuimplementierungen. Ich priorisiere Linux (basierend auf Ihrem Build-Pfad), aber beachten Sie OS-spezifische Anpassungen.

#### 1. **Installation über den Paketmanager (Am einfachsten für Debian/Ubuntu/Kali)**
   DirB ist als vorkompiliertes Paket in vielen Distro-Repos verfügbar, sodass keine Quellcode-Änderungen oder Builds nötig sind.
   - **Auf Kali Linux** (empfohlen für Penetration-Testing-Tools wie dieses):
     ```
     sudo apt update
     sudo apt install dirb
     ```
     - Es wird offiziell unterstützt und in den Kali-Repos gepflegt. [Kali Tools Page](https://www.kali.org/tools/dirb/)
   - **Auf Ubuntu/Debian**:
     ```
     sudo apt update
     sudo apt install dirb
     ```
     - Falls nicht gefunden (ältere Versionen könnten es nicht haben), aktivieren Sie das Universe-Repo: `sudo add-apt-repository universe && sudo apt update`.
   - **Verifikation**: Führen Sie `dirb --help` nach der Installation aus. Wordlists befinden sich in `/usr/share/dirb/wordlists/`.
   - **Warum das funktioniert**: Pakete behandeln alle Fixes (einschließlich mehrfacher Definitionen) upstream.

   Wenn Sie eine andere Distro verwenden:
   - **Fedora/RHEL**: `sudo dnf install dirb` (falls in EPEL-Repos; fügen Sie EPEL hinzu falls nötig: `sudo dnf install epel-release`).
   - **Arch**: `sudo pacman -S dirb`.

#### 2. **Eine Python-Neuimplementierung verwenden (Plattformübergreifend, Keine C-Kompilierung)**
   Das originale DirB ist C-basiert und heikel zu bauen, aber es gibt einen modernen Python-Port, der funktional identisch (oder besser) ist und über pip installiert wird – keine Quellcode-Anpassungen erforderlich.
   - **Repo**: [ct-Open-Source/dirb auf GitHub](https://github.com/ct-Open-Source/dirb)
   - **Installation**:
     ```
     pip install git+https://github.com/ct-Open-Source/dirb.git
     ```
     - Oder klonen: `git clone https://github.com/ct-Open-Source/dirb.git && cd dirb && pip install .`
   - **Verwendung**: Gleich wie das Original, z.B. `dirb https://example.com /usr/share/wordlists/dirb/common.txt`.
   - **Vorteile**: Aktiv gepflegt, in manchen Fällen schneller, funktioniert auf Mac/Windows/Linux. Enthält Extras wie rekursives Scannen.
   - **Nachteile**: Nicht das "offizielle" Binary, aber die Ausgabe stimmt weitgehend überein.

#### 3. **Vorgebautes Binary herunterladen (Begrenzte Verfügbarkeit)**
   - Offizielle SourceForge-Releases sind meistens Source-Tarballs (z.B. dirb222.tar.gz), die immer noch ein Bauen erfordern.
   - Es gibt keine universellen Binaries, aber wenn Sie auf Kali/Parrot OS sind, ist der Paketweg der beste.
   - Als Workaround: Wenn Sie Docker haben, holen Sie sich ein Kali-Image und führen Sie DirB darin aus:
     ```
     docker run -it kalilinux/kali-rolling dirb http://example.com
     ```
     - Keine Installation nötig; Container sind vorgebaut.

#### Schneller Vergleich

| Methode              | OS-Unterstützung          | Aufwand | Anmerkungen |
|---------------------|---------------------|--------|-------|
| **Apt/DNF/Pacman** | Linux (Debian/Fedora/Arch) | Gering | Vorkompiliert; Wordlists inklusive. |
| **Python Port**    | Beliebig (Python 3+)    | Gering | Moderne Alternative; nur pip nötig. |
| **Docker**         | Beliebig (mit Docker)    | Mittel | Isoliert; keine Installation auf dem Host. |

Wenn nichts passt (z.B. eingeschränkte Umgebung), ziehen Sie Alternativen wie Gobuster in Betracht (`go install github.com/OJ/gobuster/v3@latest`) – es ist Go-basiert, kompiliert einfach ohne Probleme und macht ähnliches Directory Busting.

Auf welchem OS sind Sie? Das hilft bei der Eingrenzung. Wenn Sie auf Probleme stoßen, teilen Sie die Fehler-/Ausgabemeldung mit.