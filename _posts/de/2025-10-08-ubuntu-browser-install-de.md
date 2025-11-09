---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Ubuntu 24.04 Browser-Installationshandbuch
translated: true
type: note
---

Neben **Firefox** und **Chromium** gibt es einige weitere gute Browser, die Sie auf **Ubuntu 24.04** installieren können – je nach Ihren Prioritäten (Geschwindigkeit, Privatsphäre, Kompatibilität, Ressourcenverbrauch usw.). Hier ist eine kategorisierte Liste mit Anmerkungen:

---

### 🧠 Gängige Browser

**1. Google Chrome**

* Basiert auf Chromium, beinhaltet aber Googles Sync, Codecs und proprietäre Funktionen.
* Große Kompatibilität mit Web-Apps (wie Google Docs, Meet, etc.).
* Installation via `.deb` von der offiziellen Google-Website.

**2. Microsoft Edge (Linux-Version)**

* Chromium-basiert, polierte Benutzeroberfläche, Integration mit Microsoft-Diensten.
* Oft schneller als Chrome im Umgang mit Arbeitsspeicher.
* `.deb`-Paket von der Microsoft-Website.

---

### 🔒 Auf Privatsphäre fokussierte Browser

**3. Brave**

* Basiert auf Chromium, aber mit integriertem Werbeblocker, Tracker-Blockierung und Tor-Fenstermodus.
* Behält die Chrome-Erweiterungskompatibilität bei.
* Installation:

  ```bash
  sudo apt install apt-transport-https curl
  sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
  echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list
  sudo apt update
  sudo apt install brave-browser
  ```

**4. Vivaldi**

* Ebenfalls Chromium-basiert, aber hochgradig anpassbar (Tab-Kachelung, Tastenkürzel, Seitenleisten-Tools).
* Funktionsreicher als Chrome oder Edge.
* Laden Sie die `.deb`-Datei von [vivaldi.com](https://vivaldi.com) herunter.

**5. Tor Browser**

* Konzentriert sich auf Anonymität und Umgehung von Zensur.
* Basiert auf Firefox ESR, leitet Datenverkehr durch das Tor-Netzwerk.
* Installation via:

  ```bash
  sudo apt install torbrowser-launcher
  ```

---

### 🪶 Leichtgewichtige Browser

**6. Falkon (Qt WebEngine)**

* Leichtgewichtig, minimale Oberfläche, integriert sich gut in KDE/Qt-Systeme.
* Installation:

  ```bash
  sudo apt install falkon
  ```

**7. Midori**

* Älteres Projekt, das für Einfachheit und geringen Ressourcenverbrauch wiederbelebt wurde.
* Gut für einfaches Surfen, nicht ideal für aufwändige Web-Apps.
* Installation:

  ```bash
  sudo apt install midori
  ```

**8. Epiphany (GNOME Web)**

* Standard-GNOME-Browser, WebKit-basiert (nicht Chromium).
* Einfach, leichtgewichtig, passt perfekt in die GNOME-Umgebung.
* Installation:

  ```bash
  sudo apt install epiphany-browser
  ```

---

### 🧪 Entwickler- / Nischen-Browser

**9. Ungoogled Chromium**

* Chromium, befreit von allen Google-Tracking- und API-Abhängigkeiten.
* Manueller Setup, aber gut für strenge Privatsphäre.
* Oft über Community-`.deb`-Pakete oder Flatpak erhältlich.

**10. Floorp**

* Ein moderner Fork von Firefox mit verbesserter Privatsphäre und Anpassbarkeit.
* Wird von japanischen Entwicklern erstellt; wird immer beliebter.
* Flatpak von Flathub verfügbar.

---

Möchten Sie, dass ich eine Kombination (z.B. *einen privatsphärenfokussierten, einen leichtgewichtigen, einen voll ausgestatteten*) empfehle, die zu Ihrem Workflow auf diesem Ubuntu-System passt?