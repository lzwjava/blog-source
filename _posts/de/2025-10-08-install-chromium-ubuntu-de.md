---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Installation von Chromium auf Ubuntu 24.04
translated: true
type: note
---

Um **Chromium** auf **Ubuntu 24.04** zu installieren, haben Sie einige gute Optionen – je nachdem, ob Sie die **offizielle Snap-Version**, die **APT-Version (Debian-Paket)** oder einen **manuellen Download** bevorzugen. Hier ist eine übersichtliche Anleitung für jede Methode:

---

### 🧩 Option 1: Installation über Snap (Der offizielle Ubuntu-Weg)

Dies ist die **Standardmethode** und die stabilste.

```bash
sudo snap install chromium
```

Starten Sie es anschließend mit:

```bash
chromium
```

✅ *Vorteile:*

* Wird offiziell von Canonical gewartet.
* Aktualisiert sich automatisch.

⚠️ *Nachteile:*

* Der Start kann langsamer sein.
* Die Snap-Sandboxing kann Probleme mit Systemproxys oder Dateizugriff verursachen.

---

### ⚙️ Option 2: Installation über APT (Debian-Paket, Non-Snap)

Wenn Sie **Snap nicht mögen**, können Sie Chromium aus einem **Drittanbieter-Repository** installieren, wie z.B. dem offiziellen Debian-Build von **ungoogled-chromium** oder **OBS**.

1.  Fügen Sie das OBS-Repository hinzu:

    ```bash
    sudo apt install wget gnupg
    wget -qO - https://download.opensuse.org/repositories/home:/ungoogled_chromium/Ubuntu_24.04/Release.key | sudo gpg --dearmor -o /usr/share/keyrings/ungoogled-chromium.gpg
    ```

2.  Fügen Sie das Repository hinzu:

    ```bash
    echo "deb [signed-by=/usr/share/keyrings/ungoogled-chromium.gpg] https://download.opensuse.org/repositories/home:/ungoogled_chromium/Ubuntu_24.04/ /" | sudo tee /etc/apt/sources.list.d/ungoogled-chromium.list
    ```

3.  Installieren Sie Chromium:

    ```bash
    sudo apt update
    sudo apt install ungoogled-chromium
    ```

Starten Sie es anschließend mit:

```bash
ungoogled-chromium
```

✅ *Vorteile:*

* Keine Snap-Abhängigkeit.
* Eine datenschutzgestärkte Version ist verfügbar.

⚠️ *Nachteile:*

* Updates kommen langsamer als bei Snap.
* Einige Funktionen (wie Google Sync) sind deaktiviert.

---

### 🧰 Option 3: Installation von Chromiums offiziellem Build (Manuell)

Wenn Sie die **neueste Entwicklerversion** möchten:

```bash
sudo apt install chromium-browser
```

Falls dies zu Snap umleitet und Sie das vermeiden möchten:

```bash
sudo apt purge chromium-browser
sudo apt install chromium
```

Oder laden Sie manuell eine `.deb`-Datei herunter:

```bash
wget https://commondatastorage.googleapis.com/chromium-browser-snapshots/Linux_x64/LAST_CHANGE -O /tmp/LAST_CHANGE
LATEST=$(cat /tmp/LAST_CHANGE)
wget "https://commondatastorage.googleapis.com/chromium-browser-snapshots/Linux_x64/${LATEST}/chrome-linux.zip"
unzip chrome-linux.zip
./chrome-linux/chrome
```

---

### 🌍 Hinweis zu Proxy-Einstellungen

Da Ihr System verwendet:

```
HTTP_PROXY=http://127.0.0.1:7890
HTTPS_PROXY=http://127.0.0.1:7890
```

stellen Sie sicher, dass Snap und APT Ihren Proxy verwenden, indem Sie diese in `/etc/environment` oder Ihr Shell-Profil exportieren:

```bash
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
```

---

Möchten Sie, dass ich Ihnen zeige, wie Sie Chromium so konfigurieren, dass es diesen Proxy automatisch verwendet (damit es sich immer darüber verbindet)?