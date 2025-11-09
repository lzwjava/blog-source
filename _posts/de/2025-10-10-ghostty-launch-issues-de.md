---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Probleme bei der Installation und dem Start von Ghostty
translated: true
type: note
---

### Problemdiagnose

Basierend auf den geteilten Logs war die Installation von Ghostty 1.1.3 über das `.deb`-Paket erfolgreich, aber das Starten schlägt aus zwei Hauptgründen fehl:

1.  **CLI-Argumentfehler**: Der Befehl `ghostty .` behandelt `.` als ungültiges Konfigurationsfeld (wahrscheinlich als Verzeichnis gemeint, aber Ghostty unterstützt diese Syntax nicht). Dies verursacht das sofortige Beenden mit "invalid field".

2.  **OpenGL/GTK-Kompatibilitätsproblem**: Wenn `ghostty` ohne Argumente ausgeführt wird, initialisiert es sich, stürzt dann aber ab wegen "OpenGL version is too old. Ghostty requires OpenGL 3.3" (Ihr System meldet OpenGL 3.2 an Ghostty). Dies ist ein bekanntes Problem unter Ubuntu 22.04, insbesondere mit NVIDIA-Treibern unter X11. Obwohl `glxinfo` oft OpenGL 4.6+ anzeigt, kann Ghosttys GTK 4.6 Runtime mit NVIDIA GL nicht richtig auf höhere Versionen zugreifen. Die "GDK_DEBUG=vulkan-disable"-Warnung ist ein Lösungsversuch, behebt aber das Kernproblem nicht. Der finale Gtk-CRITICAL-Fehler ist ein Symptom der fehlgeschlagenen Surface Realization.

Dies betrifft viele Nutzer auf Ubuntu 22.04 (und Ableitern wie Pop!\_OS) aufgrund der älteren GTK-Version (4.6 vs. der neueren 4.12+, die für volle NVIDIA-Kompatibilität benötigt wird).

### Schnellüberprüfungen
-   Überprüfen Sie Ihre tatsächliche OpenGL-Unterstützung (installieren Sie `mesa-utils` falls nötig: `sudo apt install mesa-utils`):
    ```
    glxinfo | grep "OpenGL version"
    ```
    Falls 3.3+ gemeldet wird, ist das Problem tatsächlich GTK/NVIDIA-spezifisch.
-   Überprüfen Sie Ihren Sitzungstyp: `echo $XDG_SESSION_TYPE`. Falls es `x11` ist, trägt das wahrscheinlich dazu bei.

### Lösungen
Hier sind Schritt-für-Schritt-Lösungen, beginnend mit der einfachsten:

1.  **Zu Wayland wechseln (falls Sie Hybrid-Grafik haben, z.B. Intel + NVIDIA)**:
    -   Melden Sie sich ab und wählen Sie eine Wayland-Sitzung beim Login (oder fügen Sie `WaylandEnable=true` zu `/etc/gdm3/custom.conf` hinzu und starten Sie GDM neu).
    -   Führen Sie Ghostty mit integrierter Grafik aus: `prime-run --gpu intel ghostty` (installieren Sie `nvidia-prime` falls nötig).
    -   Dies umgeht die NVIDIA X11-Probleme für einige Nutzer.

2.  **Installation via Snap (Einfacheres alternatives Paket)**:
    -   Das inoffizielle `.deb`-Paket, das Sie verwendet haben, kann System-Eigenheiten übernehmen. Versuchen Sie das offizielle Snap, das Abhängigkeiten bündelt:
        ```
        sudo snap install ghostty --classic
        ```
    -   Starten Sie es mit `snap run ghostty`. Falls OpenGL immer noch fehlschlägt, fahren Sie mit den Upgrades fort.

3.  **Upgrade auf Ubuntu 24.04 (Empfohlen für langfristige Lösung)**:
    -   Ubuntu 24.04 enthält GTK 4.14+, was die NVIDIA-Kompatibilität behebt.
    -   Folgen Sie dem offiziellen Upgrade-Guide: `sudo do-release-upgrade`.
    -   Installieren Sie Ghostty nach dem Upgrade über das gleiche `.deb`-Paket oder Snap neu. Nutzer berichten, dass es nach dem Upgrade einwandfrei funktioniert.

4.  **Build from Source mit GLFW-Backend (Temporäre Problemumgehung)**:
    -   Dies verwendet eine Nicht-GTK-Runtime, um das OpenGL-Problem zu umgehen (Hinweis: Keine Tabs, nur zum Testen).
        ```
        sudo apt install git zig libgtk-4-dev libadwaita-1-dev libharfbuzz-dev libpango1.0-dev libcairo2-dev libgdk-pixbuf-2.0-dev libglib2.0-dev libwayland-dev libxkbcommon-dev libinput-dev libudev-dev libseat-dev libpipewire-0.3-dev libsystemd-dev libx11-dev libxext-dev libxfixes-dev libxi-dev libxrandr-dev libxtst-dev libxdamage-dev libxcomposite-dev libxrender-dev libxcursor-dev libxinerama-dev libxss-dev libxv-dev libxxf86vm-dev libgl1-mesa-dev libegl1-mesa-dev libgles2-mesa-dev libgbm-dev libdrm-dev libvulkan-dev libclang-dev
        git clone https://github.com/ghostty-org/ghostty.git
        cd ghostty
        zig build -Doptimize=ReleaseFast -Dapp-runtime=glfw
        sudo cp zig-out/bin/ghostty /usr/local/bin/
        ```
    -   Führen Sie `ghostty` aus. Wechseln Sie für volle Funktionalität nach einem Upgrade zurück zu GTK.

### Zusätzliche Tipps
-   Aktualisieren Sie Ihre NVIDIA-Treiber: `sudo ubuntu-drivers autoinstall` (oder verwenden Sie manuell die 550+ Serie).
-   Falls Sie nur AMD/Intel-Grafik haben, stellen Sie sicher, dass Mesa aktualisiert ist: `sudo apt update && sudo apt upgrade mesa-vulkan-drivers`.
-   Für die Konfigurationswarnung in Ihrer Template-Datei (`~/.config/ghostty/config`) bearbeiten Sie diese, um ungültige Zeilen zu entfernen (z.B. verirrtes `.`).

Falls nichts davon funktioniert, teilen Sie Ihre `glxinfo`-Ausgabe oder GPU-Details (`lspci | grep VGA`) für eine maßgeschneidertere Beratung mit.

[OpenGL Too Old Discussion](https://github.com/ghostty-org/ghostty/discussions/3159)  
[Ghostty Ubuntu Builds](https://github.com/mkasberg/ghostty-ubuntu)  
[Ghostty Snap](https://snapcraft.io/ghostty)