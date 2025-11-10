---
audio: false
generated: true
lang: de
layout: post
title: Installation von Firefox über APT auf Ubuntu
translated: true
type: note
---

Diese Anleitung beschreibt, wie Sie Firefox aus dem Mozilla APT-Repository unter Ubuntu installieren und damit das standardmäßige Snap-Paket ersetzen.

**Warum die APT-Version verwenden?**

Während die Snap-Version praktisch ist, bevorzugen einige Benutzer die APT-Version aufgrund einer besseren Integration und Leistung.

**Schritte:**

1.  **Deinstallieren Sie das Firefox-Snap:**

    ```bash
    sudo snap remove firefox
    ```

2.  **Erstellen Sie ein APT-Keyring-Verzeichnis (falls es nicht existiert):**

    ```bash
    sudo install -d -m 0755 /etc/apt/keyrings
    ```

3.  **Importieren Sie den Mozilla APT-Repository-Signaturschlüssel:**

    ```bash
    wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- | sudo tee /etc/apt/keyrings/packages.mozilla.org.asc > /dev/null
    ```
    *Falls `wget` fehlt, installieren Sie es zuerst: `sudo apt install wget`*

4.  **Fügen Sie das Mozilla-Repository zu Ihrer Quellenliste hinzu:**

    ```bash
    echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://packages.mozilla.org/apt mozilla main" | sudo tee -a /etc/apt/sources.list.d/mozilla.list > /dev/null
    ```

5.  **Setzen Sie die Paketpriorität, um das Mozilla-DEB-Paket zu bevorzugen:**

    Dies verhindert, dass das Ubuntu-Transition-Paket das Snap wieder installiert.

    ```bash
    echo '
    Package: *
    Pin: origin packages.mozilla.org
    Pin-Priority: 1000

    Package: firefox*
    Pin: release o=Ubuntu
    Pin-Priority: -1' | sudo tee /etc/apt/preferences.d/mozilla
    ```

6.  **Entfernen Sie das Ubuntu Firefox-DEB-Paket (falls vorhanden) und installieren Sie die Mozilla-Version:**

    ```bash
    sudo apt update && sudo apt remove firefox
    sudo apt install firefox
    ```

Jetzt haben Sie Firefox aus dem offiziellen Mozilla APT-Repository installiert!