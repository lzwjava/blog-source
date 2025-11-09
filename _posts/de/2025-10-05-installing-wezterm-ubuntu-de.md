---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Installation von WezTerm auf Ubuntu
translated: true
type: note
---

Der Fehler "Unable to locate package wezterm" tritt auf, weil WezTerm nicht in den Standard-Repositorys von Ubuntu verfügbar ist. Sie müssen zuerst das offizielle Drittanbieter-Repository hinzufügen. Hier ist die schrittweise Lösung mit der nativen APT-Methode (empfohlen für nahtlose Integration):

1.  Fügen Sie den GPG-Schlüssel für das Repository hinzu:
    ```
    curl -fsSL https://apt.fury.io/wez/gpg.key | sudo gpg --yes --dearmor -o /usr/share/keyrings/wezterm-fury.gpg
    ```

2.  Fügen Sie das Repository zu Ihren Quellen hinzu:
    ```
    echo 'deb [signed-by=/usr/share/keyrings/wezterm-fury.gpg] https://apt.fury.io/wez/ * *' | sudo tee /etc/apt/sources.list.d/wezterm.list
    ```

3.  Setzen Sie die korrekten Berechtigungen für die Schlüsseldatei:
    ```
    sudo chmod 644 /usr/share/keyrings/wezterm-fury.gpg
    ```

4.  Aktualisieren Sie Ihre Paketliste:
    ```
    sudo apt update
    ```

5.  Installieren Sie nun WezTerm:
    ```
    sudo apt install wezterm
    ```

Nach der Installation können Sie es mit `wezterm` im Terminal ausführen. Wenn Sie stattdessen die Nightly (Bleeding-Edge) Version möchten, verwenden Sie `sudo apt install wezterm-nightly` in Schritt 5 – beachten Sie jedoch, dass sie nicht parallel zur stabilen Version installiert werden kann.

### Alternative: Flatpak (Kein Repository benötigt)
Wenn Sie eine sandboxed Installation ohne Änderung der APT-Quellen bevorzugen:
1.  Installieren Sie Flatpak, falls noch nicht vorhanden: `sudo apt install flatpak`.
2.  Fügen Sie Flathub hinzu: `flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo`.
3.  Installieren Sie es: `flatpak install flathub org.wezfurlong.wezterm`.
4.  Führen Sie es aus: `flatpak run org.wezfurlong.wezterm` (oder fügen Sie einen Alias hinzu: `alias wezterm='flatpak run org.wezfurlong.wezterm'`).

Flatpak ist isoliert, was einige erweiterte Funktionen einschränken könnte, aber es ist einfacher zum Testen.

[WezTerm Linux Installation Guide](https://wezterm.org/install/linux.html)