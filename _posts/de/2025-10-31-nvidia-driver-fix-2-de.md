---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Behebung von NVIDIA-Treiberpaketkonflikten
translated: true
type: note
---

Das sieht nach einem klassischen Paketkonflikt während eines NVIDIA-Treiberupdates auf Ubuntu (wahrscheinlich 22.04, basierend auf den Paketversionen) aus. Das Paket `nvidia-kernel-common-535` versucht, eine Firmware-Datei (`gsp_ga10x.bin`) zu überschreiben, die bereits im Besitz von `nvidia-firmware-535` ist, was dazu führt, dass dpkg abbricht. Dies ist ein bekanntes Problem mit den NVIDIA-535-Serien-Treibern aus den Ubuntu-Repositories.

Keine Panik – Ihr System sollte immer noch booten (obwohl die Grafik möglicherweise im Software-Rendering-Modus läuft, wenn der Treiber teilweise beschädigt ist). Hier ist eine schrittweise Lösung, um das Problem sicher zu beheben. Führen Sie diese Befehle in einem Terminal aus (verwenden Sie TTY, falls die GUI instabil ist: Strg+Alt+F3 zum Umschalten).

### Schneller Lösungsversuch (Zuerst die sicherste Methode)
1. Versuchen Sie, die beschädigten Pakete automatisch zu reparieren:
   ```
   sudo apt --fix-broken install
   ```
   Dies löst oft Abhängigkeits-/Entpackprobleme ohne manuelles Eingreifen.

2. Wenn das fehlschlägt (oder teilweise erfolgreich ist, aber Fehler hinterlässt), bereinigen Sie die unterbrochene Installation:
   ```
   sudo dpkg --configure -a
   sudo apt update
   sudo apt upgrade
   ```

### Falls immer noch hängengeblieben: Erzwingen Sie das Überschreiben der konfliktierenden Datei
Der Fehler betrifft speziell die Deb-Datei `nvidia-kernel-common-535`. Zwingen Sie dpkg, den Dateikonflikt zu ignorieren:
```
sudo dpkg -i --force-overwrite /var/cache/apt/archives/nvidia-kernel-common-535_535.274.02-0ubuntu1_amd64.deb
```
- Dies installiert nur dieses Paket und ignoriert den Dateikonflikt.
- Führen Sie dann aus:
  ```
  sudo apt --fix-broken install
  sudo apt autoremove
  sudo apt upgrade
  ```
- Starten Sie anschließend neu: `sudo reboot`.

### Nukleare Option: NVIDIA-Pakete bereinigen und neu installieren
Wenn das Obige nicht funktioniert (z.B. bei tiefergehender Versionsinkompatibilität), entfernen Sie die konfliktierenden NVIDIA-Teile und installieren Sie sie neu:
1. Entfernen Sie die Problem-Pakete (passen Sie die Versionen bei Bedarf an – prüfen Sie mit `dpkg -l | grep nvidia`):
   ```
   sudo dpkg --force-all -P nvidia-firmware-535-535.274.02 nvidia-kernel-common-535
   ```
2. Bereinigen Sie:
   ```
   sudo apt autoremove --purge
   sudo apt autoclean
   ```
3. Installieren Sie den Treiber neu:
   ```
   sudo apt update
   sudo apt install nvidia-driver-535
   ```
4. Starten Sie neu.

### Prävention/Tipps
- Fügen Sie das graphics-drivers PPA für stabilere NVIDIA-Updates hinzu: `sudo add-apt-repository ppa:graphics-drivers/ppa && sudo apt update`.
- Wenn Sie einen Laptop verwenden, stellen Sie sicher, dass Secure Boot im BIOS vor der Treiberinstallation deaktiviert ist.
- Testen Sie nach dem Neustart mit `nvidia-smi` (sollte Ihre GPU anzeigen) oder `prime-select query` (bei NVIDIA Optimus).
- Wenn dies Ihre Anzeige komplett zerstört, booten Sie in den Wiederherstellungsmodus und führen Sie die Lösungen von dort aus.

Wenn nichts davon funktioniert oder Sie einen neuen Fehler erhalten, fügen Sie die vollständige Ausgabe hier für weitere Anpassungen ein.

### Referenzen
- [Unmet dependencies nvidia-dkms-535 - package conflict breaks Ubuntu 22.04 install](https://forums.developer.nvidia.com/t/unmet-dependencies-nvidia-dkms-535-package-conflict-breaks-ubuntu-22-04-install/265788)
- [Ubuntu and NVIDIA-provided packages conflict, breaking installation](https://forums.developer.nvidia.com/t/ubuntu-and-nvidia-provided-packages-conflict-breaking-installation/259150)
- [Problem with nvidia package dependencies](https://askubuntu.com/questions/1491916/problem-with-nvidia-package-dependencies)
- [nvidia-kernel-common-535 conflicts with nvidia-firmware-535](https://superuser.com/questions/1833427/nvidia-kernel-common-535-conflicts-with-nvidia-firmware-535-535-161-07-535-161-0)