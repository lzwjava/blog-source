---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Behebung von NVIDIA-Treiberversionskonflikten
translated: true
type: note
---

### Fehleranalyse
Der `nvidia-smi`-Befehl schlägt fehl aufgrund einer Versionsinkonsistenz zwischen Ihrem NVIDIA-Kernel-Treiber (im OS-Kernel geladen) und den NVML-Komponenten (NVIDIA Management Library) im User-Space. Dies tritt häufig nach einem Kernel-Update, einer partiellen Treiberinstallation oder einem System-Upgrade ohne vollständige Neuinstallation des Treibers auf. Die gemeldete NVML-Version (535.274) deutet darauf hin, dass Sie einen relativ aktuellen NVIDIA-Treiberzweig verwenden (wahrscheinlich aus der 535er Serie), aber das Kernel-Modul ist nicht synchron.

Keine Sorge – dies lässt sich beheben, ohne Daten zu verlieren. Im Folgenden finden Sie Schritt-für-Schritt-Anleitungen zur Fehlerbehebung und Lösung, beginnend mit den einfachsten Methoden.

### Schnelle Lösungen (Versuchen Sie diese zuerst)
1. **Starten Sie Ihr System neu**  
   Die häufigste Ursache ist ein veraltetes Kernel-Modul. Ein Neustart lädt alles sauber neu.  
   ```
   sudo reboot
   ```  
   Führen Sie nach dem Neustart erneut `nvidia-smi` aus. Wenn es funktioniert, sind Sie fertig!

2. **Überprüfen Sie die aktuellen Treiber- und Kernelversionen**  
   Verifizieren Sie, was installiert ist:  
   ```
   # Kernel-Treiberversion prüfen
   cat /proc/driver/nvidia/version

   # Geladene Kernel-Module prüfen
   lsmod | grep nvidia

   # Aktuelle Kernel-Version prüfen
   uname -r
   ```  
   Vergleichen Sie die hier angezeigte Treiberversion mit 535.274. Wenn sie nicht übereinstimmen (z.B. Kernel zeigt 535.x, aber x ≠ 274), fahren Sie mit der Neuinstallation fort.

### Vollständige Lösung: NVIDIA-Treiber neu installieren
Wenn ein Neustart nicht hilft, installieren Sie die Treiber neu, um alles zu synchronisieren. Dies setzt voraus, dass Sie Ubuntu/Debian verwenden (üblich für nanoGPT-Setups; passen Sie es für andere Distributionen wie Fedora an).

#### Option 1: Über den Paketmanager (Empfohlen für Stabilität)
1. **Bestehende Treiber bereinigen** (entfernt Inkonsistenzen):  
   ```
   sudo apt update
   sudo apt purge 'nvidia*'
   sudo apt autoremove
   sudo rm -rf /usr/lib/nvidia*  # Optional: Bereinigt verbliebene Dateien
   ```

2. **Neustart, um Module zu leeren**:  
   ```
   sudo reboot
   ```

3. **Passende Treiber installieren**:  
   Da Ihre NVML-Version 535.274 ist, installieren Sie die 535er Serie (oder neuer, falls verfügbar). Prüfen Sie für Ihre GPU auf der NVIDIA-Website, aber für 535:  
   ```
   sudo apt install nvidia-driver-535 nvidia-utils-535
   ```  
   (Ersetzen Sie bei Bedarf durch den Paketnamen Ihrer Distribution, z.B. `dnf` auf Fedora.)

4. **Neustarten und überprüfen**:  
   ```
   sudo reboot
   nvidia-smi  # Sollte jetzt funktionieren
   ```

#### Option 2: Direkt von NVIDIA (Für neueste/benutzerdefinierte Versionen)
1. Laden Sie die 535.274 Runfile von [NVIDIAs Archiv](https://www.nvidia.com/Download/driverResults.aspx/227xxx/en-us/) herunter (suchen Sie nach Ihrer GPU und 535.274).  
   ```
   wget https://us.download.nvidia.com/XFree86/Linux-x86_64/535.274.05/NVIDIA-Linux-x86_64-535.274.05.run
   chmod +x NVIDIA-Linux-x86_64-535.274.05.run
   ```

2. **Display-Manager anhalten** (zur Konsole wechseln):  
   ```
   sudo systemctl stop gdm  # Oder lightdm/sddm
   sudo telinit 3  # Oder Strg+Alt+F3, um zur TTY zu wechseln
   ```

3. **Installieren**:  
   ```
   sudo ./NVIDIA-Linux-x86_64-535.274.05.run --no-questions
   ```  
   Folgen Sie den Anweisungen; es könnte Warnungen zu Inkonsistenzen geben – fahren Sie fort.

4. **Neustarten**:  
   ```
   sudo reboot
   ```

### Falls Probleme bestehen bleiben
- **Secure Boot aktiviert?** Deaktivieren Sie es im BIOS/UEFI, da es nicht signierte Kernel-Module blockiert.
- **Kernel-Inkonsistenz?** Wenn Sie kürzlich Ihren Kernel aktualisiert haben, booten Sie über GRUB in den alten Kernel (beim Booten Umschalttaste gedrückt halten) und installieren Sie die Treiber neu.
- **Logs zur Fehlersuche**: Überprüfen Sie `dmesg | grep nvidia` oder `/var/log/Xorg.0.log` auf Fehler.
- **GPU-spezifisch?** Führen Sie `lspci | grep -i nvidia` aus, um zu bestätigen, dass Ihre GPU erkannt wird.

Nach der Behebung sollten Sie in der `nvidia-smi`-Ausgabe Informationen wie GPU-Auslastung, Speicher etc. sehen. Wenn Sie Modelle in nanoGPT trainieren, wird dies CUDA entsperren. Wenn Sie weitere Details teilen (z.B. Distribution, GPU-Modell oder Ausgabe der Versionsprüfungen), kann ich dies verfeinern!