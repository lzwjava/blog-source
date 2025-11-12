---
audio: false
generated: true
lang: de
layout: post
title: 'Teil 5: Busse und Erweiterung'
translated: true
type: note
---

### 1. System Bus Standards

#### Was ist ein System Bus?

Ein System Bus ist ein Kommunikationsweg, der die CPU mit dem Speicher und Peripheriegeräten verbindet. Er ermöglicht den Datentransfer, die Adressierung und Steuersignale zwischen diesen Komponenten, sodass die CPU effizient mit anderen Teilen des Computersystems interagieren kann[^3].

---

### 2. ISA Bus Überblick

- **ISA (Industry Standard Architecture)** ist einer der frühesten System Bus Standards, eingeführt mit dem IBM PC AT in den 1980er Jahren.
- Es handelt sich um einen 16-Bit-Bus mit einer Taktrate von 4,77 MHz, der Datentransferraten von bis zu ca. 9 MB/s erreichen kann[^5].
- ISA unterstützt mehrere Erweiterungskarten, jede mit ihrer eigenen Interrupt-Anforderungsleitung, wodurch Geräte wie Netzwerkkarten, serielle Anschlüsse und Grafikkarten angeschlossen werden können.
- Der Bus ist abwärtskompatibel zu älteren 8-Bit-PC-XT-Systemen und verwendet einen 98-poligen Stecker, der zwei Kantenstecker in einem einzigen Steckplatz kombiniert.
- ISA verwendet asynchrone Signalisierung und Bus Mastering, greift jedoch nur direkt auf die ersten 16 MB des Hauptspeichers zu[^5].
- Aufgrund seines Alters ist ISA größtenteils veraltet, aber historisch wichtig als Grundlage für spätere Bus-Designs.

---

### 3. PCI Bus Überblick

- **PCI (Peripheral Component Interconnect)** ist ein modernerer, synchroner, paralleler Busstandard, der entwickelt wurde, um die Einschränkungen von ISA zu überwinden[^1][^3].
- PCI-Busse laufen mit 33 MHz mit einem 32-Bit-gemultiplexten Adress-/Datenbus und bieten eine Grundbandbreite von 44 bis 66 MB/s.
- Bei sequenziellen Speicherzugriffen kann PCI durch die Übertragung eines 32-Bit-Worts pro Taktzyklus ohne erneutes Senden von Adressen bis zu 132 MB/s erreichen[^1].
- PCI verwendet eine Bridge-Schnittstelle zur Verbindung mit dem CPU-Bus, die Daten puffert und den Speicherzugriff optimiert, sodass die CPU die Ausführung ohne Wartezustände während der Peripheriekommunikation fortsetzen kann[^1].
- PCI unterstützt Bus Mastering und DMA (Direct Memory Access), wobei Geräte die Kontrolle über den Bus übernehmen können, um Daten direkt zu übertragen.
- Es gibt eine 64-Bit-Erweiterung von PCI, um die Bandbreite weiter zu erhöhen.
- PCI-Geräte werden durch Busnummer, Gerätenummer und Funktion identifiziert, wobei Konfigurationsregister Hersteller, Gerätetyp, Speicher- und E/A-Adressen sowie Interrupts angeben[^3].
- PCI-Transaktionen umfassen Adressphasen und Datenphasen und unterstützen verschiedene Befehle wie Speicherlesen/-schreiben und E/A-Lesen/-Schreiben[^3].

---

### 4. Moderne Schnittstellentechnologien

Die moderne Peripheriekommunikation hat sich hin zu seriellen Schnittstellen verlagert, die einfacher und flexibler sind als parallele Busse.

---

#### USB (Universal Serial Bus)

- USB ist eine weit verbreitete Hochgeschwindigkeits-Serielle Schnittstelle, die für den Anschluss von Peripheriegeräten wie Tastaturen, Mäusen, Speichergeräten und mehr entwickelt wurde.
- Es unterstützt Plug-and-Play und Hot-Swapping, sodass Geräte angeschlossen und getrennt werden können, ohne das System herunterzufahren.
- USB verwendet eine Topologie in Tier-Stern-Form und unterstützt Datenraten von 1,5 Mbps (Low Speed) bis zu 10 Gbps (USB 3.1 und höher).
- Es versorgt Geräte mit Strom und unterstützt mehrere Geräteklassen mit standardisierten Protokollen.
- USB-Controller verwalten Datentransfers mithilfe von Endpunkten und Pipes mit verschiedenen Transfertypen wie Steuer-, Bulk-, Interrupt- und isochrone Transfers.

---

#### SPI (Serial Peripheral Interface)

- SPI ist ein synchroner serieller Kommunikationsbus, der häufig für die Kommunikation über kurze Distanzen mit Peripheriegeräten wie Sensoren, EEPROMs und Displays verwendet wird[^4].
- Er verwendet vier Signale: SCLK (Takt), MOSI (Master Out Slave In), MISO (Master In Slave Out) und CS (Chip Select).
- SPI ist vollduplexfähig und ermöglicht gleichzeitige Datenübertragung und -empfang.
- Es ist einfach und schnell, erfordert jedoch eine Chip-Select-Leitung pro Gerät, was die Skalierbarkeit einschränken kann.
- Die SPI-Moduseinstellungen umfassen Taktpolarität und -phase, die definieren, wann Daten abgetastet und geschoben werden[^6].
- SPI wird typischerweise in Embedded Systems und Mikrocontroller-Anwendungen verwendet.

---

#### I²C (Inter-Integrated Circuit)

- I²C ist ein Zwei-Draht-Serienbus, der für die Kommunikation zwischen Mikrocontrollern und Peripheriegeräten wie Sensoren und EEPROMs verwendet wird[^4].
- Er verwendet zwei bidirektionale Leitungen: SDA (Daten) und SCL (Takt).
- I²C unterstützt mehrere Master und Slaves auf demselben Bus, wobei Geräte durch eindeutige 7- oder 10-Bit-Adressen adressiert werden.
- Es unterstützt Halbduplex-Kommunikation und verwendet Open-Drain-/Open-Collector-Ausgänge mit Pull-up-Widerständen.
- I²C ist langsamer als SPI, erfordert jedoch weniger Pins und unterstützt die Kommunikation mit mehreren Geräten mit einfacher Verdrahtung.
- Typische Geschwindigkeiten sind 100 kHz (Standardmodus), 400 kHz (Fast Mode) und höher in neueren Spezifikationen.

---

### Vergleichstabelle: ISA vs PCI vs USB vs SPI vs I²C

| Merkmal | ISA | PCI | USB | SPI | I²C |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Bustyp | Parallel, asynchron | Parallel, synchron | Serial, asynchron | Serial, synchron | Serial, synchron |
| Datenbreite | 8 oder 16 Bit | 32 oder 64 Bit gemultiplext | Serial (1 Bit) | 1 Bit pro Leitung, Vollduplex | 1 Bit pro Leitung, Halbduplex |
| Taktgeschwindigkeit | 4,77 MHz | 33 MHz (Basis-PCI) | Bis zu 10 Gbps (USB 3.1) | Typisch bis zu mehreren MHz | Typisch bis zu 400 kHz+ |
| Maximale Bandbreite | ~9 MB/s | 44-132 MB/s | Variiert je nach USB-Version | Hängt von der Taktgeschwindigkeit ab | Niedriger als SPI |
| Anzahl der Leitungen | Viele (Adresse, Daten, Steuerung) | Viele (gemultiplext) | 4 (Strom, Masse, D+, D-) | 4 (SCLK, MOSI, MISO, CS) | 2 (SDA, SCL) |
| Geräteadressierung | Steckplatzbasiert | Bus/Gerät/Funktionsnummer | Geräte-Enumeration | Chip Select pro Gerät | Adressierte Geräte |
| Typische Anwendungsfälle | Alte Erweiterungskarten | Moderne Erweiterungskarten | Externe Peripheriegeräte | Eingebettete Peripheriegeräte | Eingebettete Peripheriegeräte |
| Bus Mastering | Ja | Ja | Wird vom Host-Controller verwaltet | Master/Slave | Multi-Master unterstützt |

---

### Praktische Hinweise zur Verwendung von SPI und I²C

- Auf Plattformen wie dem Raspberry Pi sind die SPI- und I²C-Schnittstellen standardmäßig nicht aktiviert und müssen über die Systemeinstellungen (z.B. `raspi-config`) konfiguriert werden[^4].
- Bibliotheken wie `wiringPi`, `spidev` (für SPI) und `smbus` (für I²C) bieten Programmier-Schnittstellen in C/C++ und Python, um mit Geräten auf diesen Bussen zu kommunizieren.
- Die SPI-Konfiguration umfasst das Einstellen des Modus (Taktpolarität und -phase), der Bitreihenfolge (MSB oder LSB zuerst) und die Auswahl des richtigen Chip-Select-Pins[^6].
- Die I²C-Kommunikation umfasst das Angeben von Geräteadressen und das Handhaben von Start-/Stopp-Bedingungen für den Datentransfer.

---

Dieses Tutorial skizziert die grundlegenden Konzepte und praktischen Aspekte von Systembussen und modernen Peripherieschnittstellen und bietet eine solide Grundlage für das Verständnis von Mikrocomputer-Busarchitekturen und Erweiterungstechnologien.

<div style="text-align: center">⁂</div>

[^1]: https://people.ece.ubc.ca/~edc/464/lectures/lec17.pdf

[^2]: https://spotpear.com/wiki/USB-TO-UART-I2C-SPI-JTAG-Wiki.html

[^3]: https://home.mit.bme.hu/~rtamas/rendszerarchitekturak/eloadas/08_bus_introduction.pdf

[^4]: https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all

[^5]: https://www.techtarget.com/searchwindowsserver/definition/ISA-Industry-Standard-Architecture

[^6]: https://www.ratocsystems.com/english/download/pdffiles/usb61_e_10.pdf

[^7]: https://webstor.srmist.edu.in/web_assets/srm_mainsite/files/files/PCI.pdf

[^8]: https://www.infineon.com/dgdl/Infineon-USB-Serial_VCP_I2CSPI_API_Guide-Software-v01_00-EN.pdf?fileId=8ac78c8c7d0d8da4017d0f6a8b015fe6\&da=t

[^9]: https://network.nvidia.com/pdf/whitepapers/PCI_3GIO_IB_WP_120.pdf

[^10]: https://people.scs.carleton.ca/~sivarama/org_book/org_book_web/slides/chap_1_versions/ch5_1.pdf

[^11]: https://www.youtube.com/watch?v=BBobCtfOjbM

[^12]: https://www.sciencedirect.com/topics/engineering/peripheral-component-interconnect-bus

[^13]: http://mcatutorials.com/mca-tutorials-bus-standards-and-types.php

[^14]: https://www.youtube.com/watch?v=YRJ9gWaxfJY

[^15]: https://docs.nxp.com/bundle/UM12018/page/topics/connecting_to_a_target_through_a_usb-to-spi_or_usb.html

[^16]: https://www.i2ctools.com/Downloads/USBtoI2Cpro/USB-to-SPI_Software_Users_Manual.pdf

[^17]: https://www.youtube.com/watch?v=WIIR77fCHYc

[^18]: https://ftdichip.com/wp-content/uploads/2021/08/AN_255_USB-to-I2C-Example-using-the-FT232H-and-FT201X-devices.pdf

[^19]: https://www.youtube.com/watch?v=IyGwvGzrqp8