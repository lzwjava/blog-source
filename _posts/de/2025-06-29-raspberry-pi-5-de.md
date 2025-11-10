---
audio: false
generated: true
lang: de
layout: post
title: 'Raspberry Pi 5: Leistungsstark und vielseitig'
translated: true
type: note
---

Die Raspberry Pi 5, die im Oktober 2023 von der Raspberry Pi Foundation veröffentlicht wurde, ist die neueste Iteration der beliebten Single-Board-Computer-Serie, die entwickelt wurde, um Hobbyisten, Lehrkräften und Fachleuten hohe Leistung, Vielseitigkeit und Erschwinglichkeit zu bieten. Aufbauend auf dem Erfolg ihrer Vorgänger führt die Raspberry Pi 5 bedeutende Upgrades in Bezug auf Rechenleistung, Konnektivität und Funktionen ein, was sie für eine breite Palette von Anwendungen geeignet macht, von Bildungsprojekten über industrielle Automatisierung bis hin zu anspruchsvollen Computing-Aufgaben. Nachfolgend finden Sie eine umfassende Einführung in die Raspberry Pi 5, die ihre Geschichte, Spezifikationen, Funktionen, Einrichtung, Anwendungen und mehr abdeckt.

---

### **Überblick und Geschichte**
Die Raspberry-Pi-Serie begann im Jahr 2012 mit der Mission, eine erschwingliche, zugängliche Plattform zum Erlernen von Programmierung und Informatik bereitzustellen. Ursprünglich für Schüler und Hobbyisten konzipiert, erfreute sich der Raspberry Pi schnell großer Beliebtheit bei Entwicklern und Ingenieuren aufgrund seines kompakten Designs, seines geringen Stromverbrauchs und seiner Vielseitigkeit. Jede Iteration verbesserte die Leistung und erweiterte die Fähigkeiten, wobei die Raspberry Pi 5 einen bedeutenden Sprung gegenüber der 2019 veröffentlichten Raspberry Pi 4 darstellt.

Die Raspberry Pi 5, angekündigt am 28. September 2023 und kurz darauf vorbestellbar, ist die erste, die einen hauseigenen Chip (den RP1 I/O-Controller) enthält und fortschrittliche Funktionen wie PCIe-Unterstützung für schnellere Speicheroptionen einführt. Zum Preis von 60 $ für das 4GB-Modell, 80 $ für das 8GB-Modell, 50 $ für das 2GB-Modell (eingeführt im August 2024) und 120 $ für das 16GB-Modell (eingeführt im Januar 2025) bleibt sie eine erschwingliche und dennoch leistungsstarke Computing-Lösung.[](https://www.raspberrypi.com/products/raspberry-pi-5/)[](https://www.raspberrypi.com/news/introducing-raspberry-pi-5/)

---

### **Wichtige Spezifikationen**
Die Raspberry Pi 5 wird von einer robusten Reihe von Hardwarekomponenten angetrieben und bietet eine 2–3x höhere Leistung als die Raspberry Pi 4. Hier sind ihre Kernspezifikationen:

- **Prozessor**: Broadcom BCM2712, ein 2,4 GHz Quad-Core 64-Bit ARM Cortex-A76 CPU mit Kryptografie-Erweiterungen, 512 KB pro Kern L2-Cache und einem 2 MB geteilten L3-Cache. Diese CPU ist deutlich schneller als der Cortex-A72 in der Raspberry Pi 4 und ermöglicht eine bessere Leistung für anspruchsvolle Aufgaben wie Desktop-Computing und Emulation.[](https://www.raspberrypi.com/products/raspberry-pi-5/)[](https://www.zimaspace.com/blog/raspberry-pi-5-everything-you-need-to-know.html)
- **GPU**: VideoCore VII GPU, unterstützt OpenGL ES 3.1 und Vulkan 1.2, in der Lage, duale 4K-Displays mit 60 Hz über micro-HDMI-Anschlüsse zu betreiben.[](https://www.linkedin.com/pulse/introduction-raspberry-pi-5-specs-harshvardhan-mishra-wkbmf)
- **RAM**: Verfügbar in 2GB, 4GB, 8GB und 16GB LPDDR4X-4267 SDRAM Varianten, die eine schnellere Speicherbandbreite als die Raspberry Pi 4 bieten.[](https://wagnerstechtalk.com/rpi5/)[](https://www.raspberrypi.com/products/raspberry-pi-5/)
- **Speicher**:
  - MicroSD-Kartensteckplatz mit Unterstützung für den High-Speed-SDR104-Modus (empfohlen: 32 GB oder höher für Raspberry Pi OS, 16 GB für Lite). Kapazitäten über 2 TB werden aufgrund von MBR-Beschränkungen nicht unterstützt.
  - PCIe-Schnittstelle für M.2 NVMe SSDs über optionale HATs, ermöglicht schnelleres Booten und Datenübertragung.[](https://www.raspberrypi.com/documentation/computers/getting-started.html)[](https://www.raspberrypi.com/products/raspberry-pi-5/)
- **Konnektivität**:
  - Dual-Band 2,4 GHz und 5 GHz 802.11ac Wi-Fi.
  - Bluetooth 5.0 und Bluetooth Low Energy (BLE).
  - Gigabit Ethernet mit Power over Ethernet (PoE) Unterstützung (erfordert PoE+ HAT).
  - 2x USB-3.0-Anschlüsse (5 Gbps simultaner Betrieb) und 2x USB-2.0-Anschlüsse.
  - 40-poliger GPIO-Header zum Anschluss von Sensoren, Displays und anderen Peripheriegeräten.
  - 2x micro-HDMI-Anschlüsse für duale 4K@60Hz-Ausgabe.
  - 2x 4-lane MIPI Camera/Display Transceiver (austauschbar für eine Kamera und ein Display oder zwei gleiche).
  - Dedizierter UART-Connector zum Debuggen (921.600 bps).[](https://www.linkedin.com/pulse/introduction-raspberry-pi-5-specs-harshvardhan-mishra-wkbmf)[](https://www.waveshare.com/wiki/Raspberry_Pi_5)
- **Stromversorgung**: Erfordert ein 5V/5A USB-C-Netzteil (z.B. Raspberry Pi 27W USB-C Power Supply). Unzureichende Netzteile können zu Instabilität führen.[](https://www.raspberrypi.com/products/raspberry-pi-5/)
- **Echtzeituhr (RTC)**: Integrierte Echtzeituhr mit Batterie-Backup-Anschluss (J5), eliminiert die Notwendigkeit externer Taktmodule im ausgeschalteten Zustand.[](https://en.wikipedia.org/wiki/Raspberry_Pi)
- **Andere Funktionen**:
  - RP1 I/O-Controller, ein benutzerdefinierter Chip von Raspberry Pi für verbesserte I/O-Leistung.
  - Ein-/Ausschalter, eine Premiere für die Serie.
  - Kompatibilität mit M.2 HAT+ für NVMe SSDs und andere PCIe-Geräte.[](https://www.tomshardware.com/reviews/raspberry-pi-5)[](https://www.raspberrypi.com/news/introducing-raspberry-pi-5/)

---

### **Physisches Design**
Die Raspberry Pi 5 behält das kreditkartengroße Format (85 mm x 56 mm) der vorherigen Flaggschiff-Modelle bei und gewährleistet so die Kompatibilität mit vielen bestehenden Setups. Allerdings benötigt sie ein neues Gehäuse aufgrund von Layoutänderungen und erhöhten thermischen Anforderungen. Das offizielle Raspberry Pi 5 Gehäuse (10 $) beinhaltet einen integrierten Lüfter für aktive Kühlung, und der Active Cooler (5 $) wird für anspruchsvolle Aufgaben empfohlen, um Thermal Throttling zu verhindern. Die Platine weist außerdem sauberere Kanten aufgrund verbesserter Fertigungsprozesse wie intrusive Reflow für Anschlüsse und gerouteter Panel-Singulation auf.[](https://www.raspberrypi.com/products/raspberry-pi-5/)[](https://www.raspberrypi.com/news/introducing-raspberry-pi-5/)

---

### **Betriebssystem und Software**
Das empfohlene Betriebssystem ist **Raspberry Pi OS** (basierend auf Debian Bookworm), optimiert für die Hardware der Raspberry Pi 5. Es ist verfügbar in:
- **Full**: Beinhaltet eine Desktop-Umgebung und vorinstallierte Software für den allgemeinen Gebrauch.
- **Standard**: Desktop-Umgebung mit minimaler Software.
- **Lite**: Nur Kommandozeile, ideal für Headless-Setups oder schlanke Anwendungen.

Andere unterstützte Betriebssysteme sind:
- **Ubuntu**: Robuste Linux-Distribution für Desktop- und Server-Einsatz.
- **Arch Linux ARM**: Minimalistisch und hochgradig anpassbar.
- **LibreELEC**: Schlankes Betriebssystem für den Betrieb des Kodi Media Centers.
- **Batocera/Recalbox**: Für Retro-Gaming.
- **Windows 10/11**: Experimentelle Unterstützung für Desktop-Einsatz (nicht offiziell empfohlen).[](https://www.jaycon.com/ultimate-guide-to-raspberry-pi/)[](https://wagnerstechtalk.com/rpi5/)

Der **Raspberry Pi Imager** ist das offizielle Tool zum Aufspielen von Betriebssystemen auf microSD-Karten oder SSDs. Es vereinfacht den Einrichtungsprozess, indem Benutzer das Betriebssystem auswählen und konfigurieren können, inklusive Vorabkonfiguration von Hostname, Benutzerkonten und SSH für Headless-Betrieb.[](https://wagnerstechtalk.com/rpi5/)[](https://www.scribd.com/document/693937166/Bash-A-Getting-started-with-Raspberry-Pi-5-A-beginners-Guide-2023)

---

### **Einrichtungsprozess**
Die Einrichtung einer Raspberry Pi 5 ist unkompliziert, erfordert jedoch eine spezielle Hardware- und Softwarevorbereitung. Hier ist eine Schritt-für-Schritt-Anleitung:

1. **Hardware zusammensuchen**:
   - Raspberry Pi 5 (2GB, 4GB, 8GB oder 16GB Variante).
   - MicroSD-Karte (32GB+ empfohlen, Class 10 für Leistung).
   - 5V/5A USB-C-Netzteil.
   - Micro-HDMI-zu-HDMI-Kabel für das Display.
   - USB-Tastatur und Maus (oder Bluetooth-Alternativen).
   - Optional: Monitor, Ethernet-Kabel, M.2 SSD mit HAT, Gehäuse mit Kühlung.[](https://robocraze.com/blogs/post/how-to-setup-your-raspberry-pi-5)

2. **Die MicroSD-Karte vorbereiten**:
   - Laden Sie den Raspberry Pi Imager von der offiziellen Raspberry Pi Website herunter.
   - Formatieren Sie die microSD-Karte mit einem Tool wie SDFormatter.
   - Verwenden Sie den Imager, um Raspberry Pi OS (Bookworm) auszuwählen und auf die Karte zu schreiben.[](https://www.waveshare.com/wiki/Raspberry_Pi_5)

3. **Peripheriegeräte anschließen**:
   - Stecken Sie die microSD-Karte in die Raspberry Pi 5.
   - Schließen Sie den Monitor an den HDMI0-Port an (bei Verwendung dualer Displays, verwenden Sie beide micro-HDMI-Ports).
   - Schließen Sie Tastatur, Maus und Ethernet an (falls kein Wi-Fi verwendet wird).
   - Stecken Sie das USB-C-Netzteil ein.[](https://www.raspberrypi.com/documentation/computers/getting-started.html)

4. **Booten und Konfigurieren**:
   - Schalten Sie die Raspberry Pi 5 ein. Die rote Stromversorgungs-LED sollte leuchten und die grüne ACT-LED wird während des Bootvorgangs blinken.
   - Folgen Sie den Bildschirmanweisungen, um Raspberry Pi OS zu konfigurieren, inklusive Zeitzone, Wi-Fi und Benutzeranmeldedaten.
   - Für Headless-Setups, aktivieren Sie SSH über den Imager oder verbinden Sie sich via UART zum Debuggen.[](https://www.waveshare.com/wiki/Raspberry_Pi_5)

5. **Optionale Zubehörteile**:
   - Installieren Sie eine M.2 SSD mit dem M.2 HAT+ für schnelleren Speicher.
   - Fügen Sie eine Batterie an den RTC-Anschluss für die Zeitnahme im ausgeschalteten Zustand an.
   - Verwenden Sie ein Gehäuse mit aktiver Kühlung für anspruchsvolle Aufgaben.[](https://www.theengineeringprojects.com/2023/10/introduction-to-raspberry-pi-5.html)[](https://www.raspberrypi.com/products/raspberry-pi-5/)

---

### **Wichtige Funktionen und Verbesserungen**
Die Raspberry Pi 5 führt mehrere Fortschritte gegenüber der Raspberry Pi 4 ein:
- **Leistung**: Die Cortex-A76 CPU und VideoCore VII GPU bieten eine 2–3x schnellere Verarbeitung und Grafik, geeignet für Aufgaben wie PS2-Emulation, Desktop-Computing und AI-Workloads. Die CPU kann mit entsprechender Kühlung auf 3 GHz übertaktet werden.[](https://wagnerstechtalk.com/rpi5/)[](https://www.tomshardware.com/reviews/raspberry-pi-5)
- **PCIe-Unterstützung**: Die Hinzufügung einer PCIe-Schnittstelle ermöglicht NVMe SSDs und andere Hochgeschwindigkeits-Peripheriegeräte, was die Boot- und Datenübertragungsgeschwindigkeit erheblich verbessert.[](https://www.raspberrypi.com/news/introducing-raspberry-pi-5/)
- **RP1 I/O-Controller**: Dieser benutzerdefinierte Chip verbessert die USB-3.0-Bandbreite, Kamera/Display-Konnektivität und die allgemeine I/O-Leistung.[](https://www.raspberrypi.com/products/raspberry-pi-5/)
- **Duale 4K-Display-Unterstützung**: Zwei micro-HDMI-Ports ermöglichen gleichzeitige 4K@60Hz-Ausgabe, ideal für Multimedia- und Produktivitäts-Setups.[](https://www.linkedin.com/pulse/introduction-raspberry-pi-5-specs-harshvardhan-mishra-wkbmf)
- **Integrierte Echtzeituhr**: Die integrierte Echtzeituhr mit Batterie-Backup gewährleistet eine genaue Zeitnahme ohne Internetverbindung.[](https://en.wikipedia.org/wiki/Raspberry_Pi)
- **Stromtaste**: Eine dedizierte Ein-/Aus-Taste vereinfacht das Strommanagement.[](https://www.tomshardware.com/reviews/raspberry-pi-5)
- **Verbesserte Wärmeabfuhr**: Der 40-nm-Fertigungsprozess und der optionale Active Cooler verbessern die thermische Effizienz, obwohl aktive Kühlung für anhaltend hohe Leistung empfohlen wird.[](https://robocraze.com/blogs/post/how-to-setup-your-raspberry-pi-5)

---

### **Anwendungen**
Die erweiterten Fähigkeiten der Raspberry Pi 5 machen sie für eine breite Palette von Projekten geeignet:
- **Bildung**: Erlernen von Programmierung (Python, C++, Java) und Elektronik mit dem 40-poligen GPIO-Header für Sensoren, LEDs und Robotik.[](https://www.rs-online.com/designspark/introduction-to-raspberry-pi-5-specifications-and-features)
- **Hausautomation**: Steuerung von Smart-Home-Geräten wie Lichtern, Schlössern und Kameras mit IoT-Frameworks.[](https://www.rs-online.com/designspark/introduction-to-raspberry-pi-5-specifications-and-features)
- **Media Center**: Betrieb von Kodi via LibreELEC für Streaming und Medienwiedergabe auf dualen 4K-Displays.[](https://www.jaycon.com/ultimate-guide-to-raspberry-pi/)
- **Retro-Gaming**: Verwendung von Batocera oder Recalbox zum Emulieren von Konsolen bis zur PS2.[](https://wagnerstechtalk.com/rpi5/)
- **Server**: Hosten von schlanken Web-Servern, VPNs oder Home-Automation-Hubs (z.B. HomeBridge).[](https://arstechnica.com/gadgets/2024/01/what-i-learned-from-using-a-raspberry-pi-5-as-my-main-computer-for-two-weeks/)
- **Industrie- und Embedded-Systeme**: Das Compute Module 5, basierend auf der Raspberry Pi 5, ist ideal für kundenspezifische Embedded-Anwendungen.
- **KI und Maschinelles Lernen**: Nutzen Sie die verbesserte CPU/GPU für Edge-AI-Projekte, wie Bildverarbeitung oder Spracherkennung, mit kompatiblen AI-HATs.[](https://www.jaycon.com/ultimate-guide-to-raspberry-pi/)[](https://www.raspberrypi.com/documentation/)
- **Desktop-Computing**: Verwendung als kostengünstiger, energieeffizienter Desktop für das Surfen im Internet, Textverarbeitung und leichte Produktivitätsaufgaben.[](https://arstechnica.com/gadgets/2024/01/what-i-learned-from-using-a-raspberry-pi-5-as-my-main-computer-for-two-weeks/)

---

### **Kompatibilität und Herausforderungen**
Während die Raspberry Pi 5 bedeutende Upgrades bietet, ergeben sich einige Kompatibilitätsprobleme:
- **Gehäuse**: Die Raspberry Pi 5 passt nicht in Raspberry Pi 4 Gehäuse aufgrund von Layoutänderungen. Verwenden Sie das offizielle Raspberry Pi 5 Gehäuse oder kompatible Drittanbieter-Optionen.[](https://www.raspberrypi.com/products/raspberry-pi-5/)
- **HATs und Add-ons**: Einige ältere HATs verfügen möglicherweise nicht über Softwareunterstützung für die Raspberry Pi 5 und benötigen Community-Updates. Auch die GPIO-Programmierung muss möglicherweise angepasst werden.[](https://www.dfrobot.com/blog-13550.html)
- **Stromversorgung**: Ein 5V/5A USB-C-Netzteil ist erforderlich, um Instabilität zu vermeiden, anders als das 5V/3A-Netzteil der Raspberry Pi 4.[](https://www.waveshare.com/wiki/Raspberry_Pi_5)
- **Betriebssystem**: Nur das neueste Raspberry Pi OS (Bookworm) ist vollständig optimiert. Ältere OS-Versionen unterstützen möglicherweise keine neuen Funktionen wie PCIe.[](https://www.waveshare.com/wiki/Raspberry_Pi_5)

Die Raspberry-Pi-Community geht diese Herausforderungen aktiv an und teilt Lösungen und Firmware-Updates, um die Kompatibilität zu verbessern.[](https://www.dfrobot.com/blog-13550.html)

---

### **Zubehör und Ökosystem**
Die Raspberry Pi 5 wird von einem reichen Ökosystem an Zubehör unterstützt:
- **Offizielles Zubehör**:
  - Raspberry Pi 5 Gehäuse (10 $) mit integriertem Lüfter.
  - Active Cooler (5 $) für anspruchsvolle Aufgaben.
  - 27W USB-C-Netzteil (12 $).
  - M.2 HAT+ für NVMe SSDs (10–20 $).
  - Raspberry Pi-eigene NVMe SSDs (256 GB oder 512 GB).[](https://www.theengineeringprojects.com/2023/10/introduction-to-raspberry-pi-5.html)[](https://www.raspberrypi.com/products/raspberry-pi-5/)
- **Drittanbieter-Zubehör**: Unternehmen wie CanaKit, Pimoroni und Pineboards bieten Kits, HATs und Speicherlösungen für die Raspberry Pi 5 an.[](https://wagnerstechtalk.com/rpi5/)[](https://www.tomshardware.com/reviews/raspberry-pi-5)
- **Dokumentation und Ressourcen**:
  - Der Offizielle Raspberry Pi Beginner's Guide (5. Auflage) von Gareth Halfacree behandelt Einrichtung, Programmierung und Projekte. Ein kostenloses PDF ist über die Raspberry Pi Bookshelf App verfügbar.[](https://www.raspberrypi.com/news/available-now-the-official-raspberry-pi-beginners-guide-5th-edition/)
  - Community-Ressourcen wie Wagner's TechTalk und das Raspberry Pi Subreddit bieten Tutorials und Projektideen.[](https://wagnerstechtalk.com/rpi5/)[](https://www.reddit.com/r/RASPBERRY_PI_PROJECTS/comments/16upxc0/total_beginner_with_raspberry_pi_where_do_i_start/)

---

### **Leistung und Anwendungsfälle**
Die Leistung der Raspberry Pi 5 macht sie zu einer praktikablen Alternative zu stromsparenden ARM-basierten Mini-PCs. In Tests wurde sie erfolgreich als Allzweck-Desktop für Webbrowsing, Textverarbeitung und leichtes Multitasking eingesetzt, obwohl sie bei anspruchsvollen Browser-Aufgaben (z.B. mehrere Chrome-Tabs) an ihre Grenzen stoßen kann. Ihre Fähigkeit, PS2-Emulation zu betreiben und duale 4K-Displays zu handhaben, macht sie zu einem Favoriten für Retro-Gaming und Media Center. Übertakten auf 3 GHz und der GPU auf 1,1 GHz steigert die Leistung weiter, wobei aktive Kühlung unerlässlich ist.[](https://arstechnica.com/gadgets/2024/01/what-i-learned-from-using-a-raspberry-pi-5-as-my-main-computer-for-two-weeks/)[](https://www.tomshardware.com/reviews/raspberry-pi-5)

Für professionelle Anwendungen unterstützt das 16GB-Modell anspruchsvollere Aufgaben wie Softwareentwicklung und Server-Hosting. Das Compute Module 5 und die Raspberry Pi 500 (eine tastaturintegrierte Version) richten sich an Embedded-Systeme und All-in-One-Computing-Bedürfnisse.[](https://www.jaycon.com/ultimate-guide-to-raspberry-pi/)[](https://en.wikipedia.org/wiki/Raspberry_Pi)

---

### **Community und Support**
Die Raspberry-Pi-Community ist eine zentrale Stärke, mit Foren, Subreddits und Websites wie raspberrypi.org, die umfangreichen Support bieten. Die Raspberry Pi Foundation stellt regelmäßig Firmware-Updates bereit, wie z.B. solche, die die Unterstützung für duale NVMe-Laufwerke und verbessertes Übertakten ermöglichen. Das MagPi-Magazin und die offizielle Dokumentation bieten Projektideen und technische Details.[](https://www.linkedin.com/pulse/introduction-raspberry-pi-5-specs-harshvardhan-mishra-wkbmf)[](https://www.raspberrypi.com/documentation/)

---

### **Schlussfolgerung**
Die Raspberry Pi 5 ist ein leistungsstarker, vielseitiger und erschwinglicher Single-Board-Computer, der auf das Erbe ihrer Vorgänger aufbaut und gleichzeitig wegweisende Funktionen wie PCIe-Unterstützung, einen benutzerdefinierten RP1-Chip und eine integrierte Echtzeituhr einführt. Mit RAM-Optionen bis zu 16 GB, dualer 4K-Display-Unterstützung und einem 2–3x Leistungsschub ist sie ideal für Bildung, Hobbyprojekte, Hausautomation, Retro-Gaming und industrielle Anwendungen. Während Kompatibilitätsherausforderungen bestehen, sorgen die aktive Community und regelmäßige Updates für eine reibungslose Erfahrung. Ob Sie ein Anfänger sind, der Python lernt, oder ein Ingenieur, der IoT-Systeme baut – die Raspberry Pi 5 bietet endlose Möglichkeiten zu einem Preis, der Computing demokratisiert.[](https://www.zimaspace.com/blog/raspberry-pi-5-everything-you-need-to-know.html)[](https://www.rs-online.com/designspark/introduction-to-raspberry-pi-5-specifications-and-features)

Für weitere Details besuchen Sie die offizielle Raspberry Pi Website (raspberrypi.com) oder erkunden Sie Community-Ressourcen wie Wagner's TechTalk und The MagPi Magazine.[](https://wagnerstechtalk.com/rpi5/)[](https://www.linkedin.com/pulse/introduction-raspberry-pi-5-specs-harshvardhan-mishra-wkbmf)