---
audio: false
generated: true
lang: de
layout: post
title: Geschichte des Mikrocomputers
translated: true
type: note
---

Der Kurs **Microcomputer and Interface Technology**, wie beschrieben, konzentriert sich auf die Architektur, Programmierung und Anbindung von Mikrocomputersystemen, mit einem besonderen Schwerpunkt auf den Intel 8086/8088 Mikroprozessoren und verwandten Schnittstellentechnologien (z.B. 8255, 8253, 8251 Chips). Um einen umfassenden historischen Überblick zu geben, werde ich die Ursprünge und Entwicklung der im Kurs behandelten Schlüsseltechnologien nachzeichnen, die wichtigsten Persönlichkeiten und Unternehmen hinter ihrer Entwicklung identifizieren und die Geschichten hinter ihrer Entstehung beleuchten. Dies umfasst den Mikrocomputer selbst, die 8086/8088 Mikroprozessoren, die Assembler-Programmierung, Speichersysteme, E/A-Schnittstellentechnologien und Bus-Standards.

---

### **1. Der Mikrocomputer: Ursprünge und Evolution**

#### **Was ist ein Mikrocomputer?**
Ein Mikrocomputer ist ein kleiner, erschwinglicher Computer, der um einen Mikroprozessor herum aufgebaut ist und CPU, Speicher und E/A-Fähigkeiten integriert. Der Kurs beginnt mit einem Überblick über Mikrocomputersysteme, die in der **Von-Neumann-Architektur** verwurzelt sind (eine CPU, Speicher für Befehle und Daten, sowie E/A, die über Busse verbunden sind).

#### **Geschichte und Entdeckung**
- **Vor den 1970er Jahren: Grundlagen**
  - Das Konzept eines programmierbaren Computers reicht bis zu **Charles Babbages** Analytical Engine (1830er Jahre) zurück, die jedoch nie gebaut wurde. **Alan Turings** theoretische Arbeit (1936) und **John von Neumanns** Bericht von 1945 über den EDVAC formalisierten den speicherprogrammierbaren Computer, bei dem Befehle und Daten denselben Speicher teilen. Diese **Von-Neumann-Architektur** wurde zum Blaupause für Mikrocomputer.
  - Frühe Computer (z.B. ENIAC, 1945) waren riesig und verwendeten Vakuumröhren. Die Erfindung des **Transistors** (1947, **John Bardeen**, **Walter Brattain**, **William Shockley** bei Bell Labs) und der **integrierten Schaltung** (1958, **Jack Kilby** bei Texas Instruments und **Robert Noyce** bei Fairchild) ermöglichten kompakte Elektronik.

- **1971: Der erste Mikroprozessor**
  - **Wer hat ihn entdeckt?**: **Intel**, insbesondere die Ingenieure **Federico Faggin**, **Ted Hoff** und **Stan Mazor**, entwickelten den **Intel 4004**, den ersten Mikroprozessor, der im November 1971 veröffentlicht wurde.
  - **Geschichte**: Im Auftrag des japanischen Taschenrechnerherstellers Busicom wurde Intel mit dem Design eines Chips für einen programmierbaren Taschenrechner beauftragt. Ted Hoff schlug einen einzelnen, universellen Chip anstelle mehrerer spezialisierter Chips vor, um Kosten und Komplexität zu reduzieren. Federico Faggin leitete das Design und packte 2.300 Transistoren in einen 4-Bit-Prozessor (740 kHz, 12-Bit-Adressbus). Der 4004 konnte 60.000 Befehle pro Sekunde ausführen, ein Sprung für seine Zeit.
  - **Auswirkung**: Der 4004 trieb den Busicom 141-PF Taschenrechner an und inspirierte Intel, ihn als universellen Prozessor zu vermarkten, was die Mikroprozessorindustrie gebar.

- **1970er Jahre: Entstehung des Mikrocomputers**
  - **1974**: Intels **8080** (8-Bit, 2 MHz) trieb den **Altair 8800** (1975, MITS) an, den ersten kommerziell erfolgreichen Mikrocomputer. Als Bausatz für Hobbyisten vermarktet, lief er unter **CP/M** (einem frühen Betriebssystem) und inspirierte **Bill Gates** und **Paul Allen**, Microsoft zu gründen, indem sie einen BASIC-Interpreter dafür schrieben.
  - **1977**: Der **Apple II** (Steve Wozniak, Steve Jobs), **Commodore PET** und **TRS-80** machten Mikrocomputer für Verbraucher zugänglich, mit Tastaturen, Displays und Software.
  - **Geschichte**: Der Erfolg des Altair beruhte auf seinem offenen Design und der Berichterstattung in *Popular Electronics*. Hobbyisten gründeten Clubs (z.B. Homebrew Computer Club), die Innovation förderten. Wozniaks Apple II-Design priorisierte Erschwinglichkeit und Benutzerfreundlichkeit und verwendete den MOS 6502 Prozessor.

- **Kurskontext**: Der Kurs konzentriert sich auf den **Intel 8086/8088**, eingeführt 1978, der den **IBM PC** (1981) antrieb und Mikrocomputer für Geschäfts- und Heimgebrauch standardisierte.

#### **Schlüsselfiguren**
- **Federico Faggin**: Leitete das 4004-Design, gründete später Zilog (Z80 Prozessor).
- **Ted Hoff**: Konzipierte das Mikroprozessor-Konzept.
- **Robert Noyce und Gordon Moore**: Intel-Gründer, trieben die Entwicklung integrierter Schaltungen und Mikroprozessoren voran.
- **Ed Roberts**: MITS-Gründer, schuf den Altair 8800.

---

### **2. Der Intel 8086/8088 Mikroprozessor**

#### **Was ist das?**
Der 8086 (16-Bit, 5-10 MHz) und der 8088 (8-Bit externer Bus) sind Mikroprozessoren, die zentral für den Kurs sind, bekannt für ihr segmentiertes Speichermodell, 1 MB Adressraum und die x86-Architektur, die bis heute dominant ist.

#### **Geschichte und Entdeckung**
- **1976-1978: Entwicklung**
  - **Wer hat ihn entdeckt?**: Intels Team, geleitet von **Stephen Morse** (Architektur und Befehlssatz), **Bruce Ravenel** (Mikrocode) und **Jim McKevitt** (Projektmanagement), entwarf den 8086, der im Juni 1978 veröffentlicht wurde. Der 8088 folgte 1979.
  - **Geschichte**: Intel zielte darauf ab, 8-Bit-Prozessoren (z.B. 8080, Z80) zu übertreffen, um auf einem wachsenden Markt zu konkurrieren. Der 8086 wurde als 16-Bit-Prozessor mit einem 20-Bit-Adressbus entworfen, der 1 MB Speicher unterstützte (gegenüber 64 KB bei 8-Bit-Chips). Sein Befehlssatz war abwärtskompatibel zum 8080, was Software-Übergänge erleichterte. Der 8088 mit seinem 8-Bit externen Bus reduzierte die Systemkosten und machte ihn für IBM attraktiv.
  - **Herausforderungen**: Die Komplexität des 8086 (29.000 Transistoren) stieß an die Grenzen von Intels Fertigung. Sein segmentiertes Speichermodell (64-KB-Segmente, Offset-Adressierung) war ein Kompromiss, um Leistung und Kompatibilität auszugleichen.

- **1981: IBM PC Übernahme**
  - **Geschichte**: IBM, das in den PC-Markt eintrat, wählte den 8088 für seinen **IBM PC** (Modell 5150) aufgrund seiner Kosteneffizienz und Intels Unterstützung. Die Entscheidung wurde vom Team von **Bill Lowe** in IBMs Boca Raton Labor beeinflusst, das eine offene Architektur mit Standardkomponenten priorisierte. Der 8088 lief mit 4,77 MHz, und der Erfolg des PCs standardisierte die x86-Architektur.
  - **Auswirkung**: Das offene Design des IBM PCs ermöglichte Klone (z.B. Compaq, Dell), die die PC-Industrie befeuerten. Microsofts **MS-DOS**, entwickelt für den PC, wurde das dominante Betriebssystem.

- **Vermächtnis**: Die x86-Architektur entwickelte sich weiter über den 80286 (1982), 80386 (1985) bis zu modernen Prozessoren.

---

### **3. Assemblersprache und Programmierung**

#### **Was ist das?**
Assemblersprache ist eine low-level Programmiersprache, die direkt den Maschinenbefehlen des Prozessors entspricht. Der Kurs behandelt 8086/8088 Assembler, einschließlich Befehlen, Adressierungsmodi und der Struktur von Assemblerprogrammen.

#### **Geschichte und Entdeckung**
- **1940er-1950er: Ursprünge**
  - Die ersten Computer wurden in Maschinensprache programmiert (Binärcode). **Kathleen Booth** wird oft die Erfindung der Assemblersprache (1947) für die ARC2 am Birkbeck College zugeschrieben. Sie führte mnemonische Codes ein (z.B. `ADD` statt `0001`).
  - **Geschichte**: Assembler entstand aus der Notwendigkeit, die mühsame Maschinenprogrammierung zu vereinfachen. Frühe Assembler (z.B. für EDSAC, 1949) übersetzten mnemonische Befehle in Maschinencode.

- **1960er-1970er: Standardisierung**
  - Mit der Reife der Computerarchitekturen wurden Assemblersprachen spezifischer. Der **Intel 8080** (1974) hatte einen eigenen Assembler, der den Weg für den 8086 ebnete.
  - **Geschichte**: Die Einführung des 8086 erforderte einen neuen Assembler. Intels Dokumentation und Entwicklungswerkzeuge förderten seine Verbreitung.

- **Kurskontext**: Der Kurs lehrt 8086-Assembler, um die Hardware-Steuerung zu verstehen, z.B. Registermanipulation, Speicherzugriff und Interrupt-Behandlung.

#### **Schlüsselfiguren**
- **Kathleen Booth**: Pionierin der Assemblersprache.
- **Intel Ingenieure**: Entwickelten den 8086-Befehlssatz und die zugehörigen Werkzeuge.

---

### **4. Speichersysteme**

#### **Was ist das?**
Speichersysteme speichern Daten und Befehle. Der Kurs behandelt RAM, ROM und Speicherhierarchie, einschließlich Technologien wie DRAM und EPROM.

#### **Geschichte und Entdeckung**
- **1940er-1950er: Früher Speicher**
  - Frühe Computer verwendeten Williams-Röhren oder Quecksilberverzögerungsleitungen. Der **Magnetkernspeicher** (ca. 1955, **An Wang**, **Jay Forrester**) wurde zum Standard für RAM bis zu den 1970er Jahren.
  - **Geschichte**: Magnetkernspeicher war nichtflüchtig, aber teuer und schwer herzustellen.

- **1970er: Halbleiterspeicher**
  - **Intel** brachte 1970 den ersten kommerziellen **DRAM**-Chip (1103, 1 Kbit) auf den Markt, entwickelt von **Robert Noyce** und seinem Team. DRAM war einfacher zu fertigen, aber flüchtig und erforderte periodisches Auffrischen. Statischer RAM (SRAM) war schneller, aber teurer.
  - **ROM**: Speicherte Firmware, mit Varianten wie **EPROM** (löschbar via UV-Licht, George Perlegos, 1971) und **EEPROM** (elektrisch löschbar, Eli Harari, 1977).
  - **Kurskontext**: Der Kurs behandelt Speichererweiterung (z.B. Adressdekodierung), kritisch für 8086-Systeme mit 1 MB Adressraum.

#### **Schlüsselfiguren**
- **Robert Noyce**: Miterfinder der integrierten Schaltung, ermöglichte dichte Speicherchips.
- **Ted Hoff**: Frühe DRAM-Designs bei Intel.
- **Dov Frohman**: Erfand EPROM bei Intel.

---

### **5. E/A- und Schnittstellentechnologie**

#### **Was ist das?**
E/A-Schnittstellen verbinden die CPU mit Peripheriegeräten (z.B. Tastaturen, Druckern). Der Kurs behandelt **8255A** (parallel), **8253/8254** (Timer), **8251A** (seriell) und Interrupt-Systeme (z.B. **8259A**).

#### **Geschichte und Entdeckung**
- **1970er: Bedarf für E/A**
  - Frühe Mikrocomputer verwendeten einfache E/A-Ports, aber Peripheriegeräte verlangten nach spezialisierten Chips. Intel entwickelte eine Familie von Peripherie-Controllern für den 8080 und 8086.
  - **Geschichte**: Als Mikrocomputer komplexer wurden, wurde die direkte CPU-Steuerung der E/A ineffizient. Intels Peripheriechips entlasteten die CPU und verbesserten die Leistung.

- **8255A Programmierbare Peripherieschnittstelle (1977)**
  - **Wer?**: Intel, entworfen für 8080/8086-Systeme.
  - **Geschichte**: Der 8255A bot drei 8-Bit-Ports, konfigurierbar in Modi für grundlegende E/A, gesteuerte E/A oder bidirektionale Übertragungen. Er vereinfachte die Anbindung von Geräten wie Tastaturen und Displays und wurde zu einem Standard in PCs.
  - **Auswirkung**: Verwendet in IBM PC Parallelports (z.B. für Drucker).

- **8253/8254 Programmierbarer Intervalltimer (1977/1982)**
  - **Wer?**: Intel, entwickelte sich aus früheren Timer-Designs.
  - **Geschichte**: Der 8253 bot drei 16-Bit-Zähler für Timing (z.B. Systemuhren) oder Zählung (z.B. Pulsmessung). Der 8254 verbesserte die Zuverlässigkeit. Verwendet in PC-Lautsprechern, DRAM-Auffrischung und Echtzeituhren.
  - **Auswirkung**: Essentiell für PC-Timing-Funktionen.

- **8251A Serielle Schnittstelle (1976)**
  - **Wer?**: Intel, für serielle Kommunikation.
  - **Geschichte**: Der 8251A handhabte asynchrone (z.B. RS-232) und synchrone Protokolle und ermöglichte Modems und Terminals. Er war kritisch für frühe Vernetzung.
  - **Auswirkung**: Betrieb PC-Serielleports (COM-Ports).

- **8259A Interrupt-Controller (1979)**
  - **Wer?**: Intel, entworfen für interrupt-gesteuerte Systeme.
  - **Geschichte**: Der 8259A verwaltete bis zu 8 Interrupt-Quellen, mit Kaskadierung für mehr, was es Peripheriegeräten ermöglichte, die CPU effizient zu signalisieren. Er war integraler Bestandteil des Interrupt-Systems des IBM PC.
  - **Auswirkung**: Standardisierte die Interrupt-Behandlung in PCs.

- **Datenübertragungsmodi**
  - **Programmgesteuerte E/A**: Die CPU fragte Geräte ab, einfach aber langsam.
  - **Interrupt-gesteuert**: Peripheriegeräte lösten Interrupts aus, gelehrt im Kurs via 8259A.
  - **DMA**: Der **Intel 8237** DMA-Controller (1980) ermöglichte Hochgeschwindigkeitsübertragungen, verwendet in Disk-Controllern.

#### **Schlüsselfiguren**
- **Intel Ingenieure**: Unbenannte Teams entwarfen diese Chips, aufbauend auf 8080/8086-Ökosystemen.
- **Gary Kildall**: CP/M Betriebssystem nutzte diese Chips und beeinflusste PC-E/A-Standards.

---

### **6. Busse und Erweiterung**

#### **Was ist das?**
Busse standardisieren die CPU-Speicher-Peripherie-Kommunikation. Der Kurs behandelt **ISA**, **PCI** und moderne Schnittstellen (**USB**, **SPI**, **I²C**).

#### **Geschichte und Entdeckung**
- **1970er: Frühe Busse**
  - Der **S-100-Bus** (1975, Ed Roberts, MITS) war ein früher Standard für Altair-ähnliche Systeme, der von Hobbyisten übernommen wurde.
  - **Geschichte**: Die Offenheit des S-100 förderte ein Mikrocomputer-Ökosystem, aber es mangelte an Standardisierung.

- **1981: ISA-Bus**
  - **Wer?**: IBM, für den IBM PC.
  - **Geschichte**: Entworfen für den 8088, unterstützte der ISA-Bus (Industry Standard Architecture) 8-Bit- (PC) und 16-Bit-Karten (PC/AT). Seine Einfachheit und IBMs Marktdominanz machten ihn zum Standard, obwohl langsam (8 MHz).
  - **Auswirkung**: Verwendet für Erweiterungskarten (z.B. Sound, Grafik) bis in die 1990er Jahre.

- **1992: PCI-Bus**
  - **Wer?**: Intel, mit Beiträgen von IBM und Compaq.
  - **Geschichte**: PCI (Peripheral Component Interconnect) adressierte die Limitierungen von ISA, bot 33 MHz Geschwindigkeit, 32-Bit-Datenpfade und Plug-and-Play. Es wurde der Standard für PCs der 1990er Jahre.
  - **Auswirkung**: Entwickelte sich zu PCIe, das heute verwendet wird.

- **Moderne Schnittstellen**
  - **USB (1996)**: Entwickelt von einem Konsortium (Intel, Microsoft, Compaq, etc.), angeführt von **Ajay Bhatt** bei Intel. USB vereinheitlichte Peripherieverbindungen mit Hot-Plugging und Skalierbarkeit (1,5 Mbps bis 480 Mbps für USB 2.0).
  - **SPI (1980er)**: Motorolas serieller Bus für Hochgeschwindigkeits-, Kurzstrecken-Kommunikation (z.B. SD-Karten).
  - **I²C (1982)**: Philips' Zwei-Draht-Bus für Low-Speed-Peripherie (z.B. Sensoren).
  - **Geschichte**: USB entstand aus der Notwendigkeit eines universellen Anschlusses, der serielle/parallele Ports ersetzte. SPI und I²C wurden für eingebettete Systeme entworfen, um die Chip-Kommunikation zu vereinfachen.

#### **Schlüsselfiguren**
- **Ajay Bhatt**: Leitender Architekt von USB.
- **IBM Ingenieure**: Definierten ISA für den PC.
- **Intel Teams**: Trieben PCI- und USB-Standards voran.

---

### **Der Kontext des Kurses und der Dozent**

- **Yang Quansheng**: Es gibt wenig öffentliche Informationen über den Dozenten, wahrscheinlich ein Professor oder Ingenieur mit Spezialisierung auf Computertechnik. Der Fokus des Kurses auf 8086 und Intel-Chips legt nahe, dass er in den 1980er-1990er Jahren konzipiert wurde, als diese Technologien die Ausbildung in China und weltweit dominierten, insbesondere für Ingenieurstudiengänge.
- **Geschichte hinter dem Kurs**:
  - In den 1980er Jahren priorisierte China die Informatik- und Elektronikausbildung, um mit der westlichen Technologie Schritt zu halten. Kurse wie dieser waren kritisch für die Ausbildung von Ingenieuren in Mikrocomputer-Design, eingebetteten Systemen und industrieller Automatisierung.
  - Der 8086/8088 und Intels Peripheriechips waren ideal für den Unterricht aufgrund ihrer Einfachheit, weiten Verbreitung und Dokumentation. Die Einbeziehung moderner Schnittstellen (USB, SPI, I²C) spiegelt Aktualisierungen wider, um relevant zu bleiben.
  - **Zielstudiengänge**: Informatik, Elektrotechnik und Automatisierung stimmen mit dem Fokus des Kurses auf Hardware-Design, Programmierung und Systemintegration überein, Schlüsselkompetenzen für Branchen wie Robotik, Telekommunikation und Informatik.

---

### **Bedeutung und Vermächtnis**

- **Mikrocomputer**: Verwandeln das Rechnen von raumgroßen Maschinen in persönliche und eingebettete Geräte. Die x86-Architektur des 8086/8088 bleibt das Rückgrat von PCs und Servern.
- **Assemblerprogrammierung**: Obwohl weniger verbreitet, ist sie entscheidend für Low-Level-Aufgaben (z.B. OS-Kernel, Firmware).
- **Schnittstellenchips**: Die Prinzipien des 8255, 8253 und 8251 bestehen in modernen Mikrocontrollern fort (z.B. Arduino, STM32).
- **Busse**: ISA und PCI ebneten den Weg für PCIe, während USB, SPI und I²C moderne Systeme dominieren.
- **Bildungseinfluss**: Kurse wie dieser bildeten Generationen von Ingenieuren aus und trugen zu globalen technologischen Fortschritten bei, insbesondere in Chinas Tech-Boom.

---

### **Moderne Relevanz**
- **Eingebettete Systeme**: Mikrocontroller-basierte Systeme verwenden ähnliche E/A-, Interrupt- und Timing-Konzepte.
- **Altsysteme**: Einige industrielle und militärische Systeme verwenden noch immer 8086-basierte Designs.
- **Bildung**: Die Einfachheit des 8086 macht ihn zu einem zeitlosen Lehrmittel für Computerarchitektur.
- **x86-Evolution**: Moderne CPUs (z.B. Intel Core, AMD Ryzen) führen ihre Abstammung auf den 8086 zurück.

---

Wenn Sie spezifische Details benötigen (z.B. technische Spezifikationen des 8255, die Entwicklung von USB oder den Hintergrund von Yang Quansheng) oder verwandte Themen erkunden möchten (z.B. Chinas Technologieausbildung in den 1980er Jahren), lassen Sie es mich wissen!