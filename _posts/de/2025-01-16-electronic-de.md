---
audio: false
lang: de
layout: post
title: Elektronische Grundlagen
translated: true
---

### Grundlegende Elektronische Bauelemente

1. Widerstandstypen: Widerstände begrenzen den Stromfluss in einer Schaltung. Typen umfassen Festwiderstände, die einen festen Widerstandswert haben, und variable Widerstände wie Potentiometer, die einen einstellbaren Widerstand ermöglichen.

2. Kondensatortypen: Kondensatoren speichern und geben elektrische Energie ab. Typen umfassen Keramikkondensatoren, die häufig für Hochfrequenzanwendungen verwendet werden, und Elektrolytkondensatoren, die höhere Kapazitätswerte haben, aber polarisiert sind.

3. Induktoren: Induktoren speichern Energie in einem Magnetfeld und setzen Änderungen des Stroms entgegen. Sie werden in Filter- und Abstimmungsanwendungen verwendet.

4. Dioden: Dioden lassen Strom nur in eine Richtung fließen. Zenerdioden werden zur Spannungsregelung verwendet, während LEDs Licht emittieren, wenn sie in Durchlassrichtung vorgespannt sind.

5. Transistoren: Transistoren, wie BJTs, wirken als elektronische Schalter oder Verstärker, wobei NPN- und PNP-Typen den Stromfluss in Schaltungen steuern.

6. Feldeffekttransistor (FET): FETs steuern den Stromfluss durch Anlegen einer Spannung an das Gate, wobei MOSFETs weit verbreitet für Schalt- und Verstärkungsanwendungen verwendet werden.

7. Fotodioden: Diese Dioden erzeugen einen Strom, wenn sie Licht ausgesetzt werden, und werden in optischen Anwendungen wie Lichtsensoren verwendet.

8. Optokoppler: Optokoppler werden verwendet, um verschiedene Teile einer Schaltung zu isolieren, und übertragen elektrische Signale durch Licht, um die elektrische Isolation aufrechtzuerhalten.

9. Gleichrichter: Dioden werden in Gleichrichterschaltungen verwendet, um Wechselstrom (AC) in Gleichstrom (DC) umzuwandeln. Halbwellengleichrichter verwenden eine einzelne Diode, während Vollwellengleichrichter zwei oder mehr Dioden verwenden, um beide Hälften der Wechselstromwelle umzuwandeln.

10. Thermistoren: Diese sind temperaturabhängige Widerstände. Thermistoren mit negativem Temperaturkoeffizienten (NTC) verringern den Widerstand bei steigender Temperatur, während Thermistoren mit positivem Temperaturkoeffizienten (PTC) den Widerstand bei höheren Temperaturen erhöhen.

---

### Elektronische Schaltungstheorie

11. Ohmsches Gesetz: Ohmsches Gesetz bezieht Spannung (V), Strom (I) und Widerstand (R) in einer linearen Schaltung: \(V = I \times R\). Es bildet die Grundlage für die meisten elektrischen Schaltungsanalysen.

12. Kirchhoffsche Gesetze: Kirchhoffs Stromgesetz (KSG) besagt, dass die Summe der Ströme, die in einen Knoten eintreten, gleich der Summe der Ströme ist, die den Knoten verlassen. Kirchhoffs Spannungsgesetz (KSG) besagt, dass die Summe der Spannungen in einer geschlossenen Schleife null ist.

13. Theveninscher Satz: Dieser Satz vereinfacht ein Netzwerk aus Widerständen und Quellen zu einer äquivalenten Spannungsquelle und einem Widerstand für eine einfachere Analyse.

14. Nortonscher Satz: Ähnlich wie der Theveninsche Satz vereinfacht Nortons Satz ein Netzwerk zu einer Stromquelle und einem parallelen Widerstand für eine einfachere Analyse stromgetriebener Schaltungen.

15. Superpositionssatz: In Schaltungen mit mehreren Quellen ermöglicht dieser Satz die Analyse jeder Quelle unabhängig voneinander und kombiniert dann die Ergebnisse.

16. Maschenanalyse: Eine Methode zur Ermittlung unbekannter Ströme in einer Schaltung unter Verwendung von Maschenströmen, die häufig in planaren Schaltungen angewendet wird.

17. Knotenspannungsmethode: Eine Methode zur Lösung von Schaltungen durch Zuweisung von Spannungen an Knoten (Verzweigungen) und Lösen der Unbekannten.

18. Impedanz und Admittanz: Impedanz ist der Gesamtwiderstand gegen den Strom in Wechselstromschaltungen, der Widerstand und Blindwiderstand kombiniert. Admittanz ist das Inverse der Impedanz und beschreibt, wie leicht Strom durch ein Bauteil fließt.

19. Leistung in Wechselstromschaltungen: In Wechselstromschaltungen wird die Leistung in Wirkleistung (aktiv), Blindleistung und Scheinleistung unterteilt. Der Leistungsfaktor stellt das Verhältnis von Wirkleistung zu Scheinleistung dar.

20. Resonanz: Resonanz tritt in LC-Schaltungen auf, wenn die induktive Blindwiderstand und die kapazitive Blindwiderstand betragsmäßig gleich, aber phasenmäßig entgegengesetzt sind, was eine maximale Energietransfer ermöglicht.

---

### Diodenschaltungen

21. Grundlegende Diodentheorie: Dioden lassen Strom nur in der Durchlassrichtung (positiv an der Anode, negativ an der Kathode) fließen und blockieren Strom in Sperrrichtung.

22. Gleichrichterschaltungen: Halbwellengleichrichter verwenden eine einzelne Diode, während Vollwellengleichrichter zwei oder vier Dioden verwenden, um Wechselstrom in Gleichstrom umzuwandeln. Brückengleichrichter sind in Netzteilschaltungen weit verbreitet.

23. Begrenzerschaltungen: Diese Schaltungen begrenzen den Spannungspegel, indem sie die Wellenform bei einem bestimmten Schwellenwert abschneiden. Sie werden zur Wellenformgestaltung und Signalschutz verwendet.

24. Klemmschaltungen: Diese Schaltungen verschieben den Spannungspegel einer Wellenform, oft verwendet, um eine Grundspannung festzulegen oder negative Schwingungen in einem Signal zu eliminieren.

25. Zenerdiode: Zenerdioden sind so gestaltet, dass sie im Rückwärtsdurchbruch arbeiten und eine konstante Spannung über einen weiten Strombereich aufrechterhalten, häufig für Spannungsregelung verwendet.

26. LEDs: Leuchtdioden emittieren Licht, wenn Strom durch sie fließt. Sie werden weit verbreitet in Displays, Anzeigen und Hintergrundbeleuchtungen verwendet.

27. Diodenanwendungen: Dioden werden zur Signalerkennung, Stromgleichrichtung, Spannungsregelung und in Kommunikationssystemen als Modulatoren oder Demodulatoren verwendet.

---

### Transistorschaltungen

28. BJT-Eigenschaften: BJTs haben drei Bereiche: Emitter, Basis und Kollektor. Der Strom, der von der Basis fließt, steuert den größeren Strom zwischen Emitter und Kollektor.

29. Transistorvorspannung: Die Transistorvorspannung legt einen Arbeitspunkt im aktiven Bereich fest. Gängige Methoden umfassen feste Vorspannung, Spannungsteiler-Vorspannung und Emitterstabilisierung.

30. Common-Emitter-Verstärker: Dies ist eine der am häufigsten verwendeten Transistorverstärkerkonfigurationen, die eine gute Spannungsverstärkung bietet, aber eine Phaseninversion aufweist.

31. Common-Collector-Verstärker: Auch als Emitterfolger bekannt, hat diese Schaltung eine Verstärkung von eins und eine hohe Eingangsimpedanz, nützlich für Impedanzanpassung.

32. Common-Base-Verstärker: Typischerweise in Hochfrequenzanwendungen verwendet, bietet er eine hohe Spannungsverstärkung, aber eine niedrige Eingangsimpedanz.

33. Schaltkreise: Transistoren können als digitale Schalter verwendet werden, die Geräte in Logikschaltungen und digitalen Systemen ein- und ausschalten.

34. Darlington-Paar: Eine Kombination aus zwei Transistoren, die eine hohe Stromverstärkung bietet. Es wird oft verwendet, wenn eine hohe Stromverstärkung benötigt wird.

35. Sättigungs- und Sperrbereich: Ein Transistor arbeitet im Sättigungsbereich, wenn er vollständig eingeschaltet ist (verhält sich wie ein geschlossener Schalter), und im Sperrbereich, wenn er vollständig ausgeschaltet ist (verhält sich wie ein offener Schalter).

---

### Feldeffekttransistor-Schaltungen

36. JFET-Eigenschaften: Der Junction Field-Effect Transistor (JFET) wird durch die Spannung am Gate gesteuert, wobei Strom zwischen Source und Drain fließt. Das Gate ist in Sperrrichtung vorgespannt, und der Drainstrom hängt von der Gate-Source-Spannung ab.

37. MOSFET-Typen: MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors) werden häufig zum Schalten und Verstärken verwendet. Sie kommen in zwei Typen: Anreicherungsmodus (normalerweise aus) und Verarmungsmodus (normalerweise ein).

38. MOSFET-Betrieb: Der MOSFET arbeitet durch Erzeugen eines leitenden Kanals zwischen Source und Drain, gesteuert durch die an das Gate angelegte Spannung.

39. Common-Source-Verstärker: Diese Konfiguration wird zur Spannungsverstärkung verwendet und bietet eine hohe Verstärkung und moderate Eingangs-/Ausgangsimpedanz.

40. Common-Drain-Verstärker: Bekannt als Sourcefolger, bietet dieser Verstärker eine niedrige Ausgangsimpedanz, was ihn für die Impedanzanpassung geeignet macht.

41. Common-Gate-Verstärker: Diese Konfiguration wird in Hochfrequenzanwendungen verwendet und bietet eine niedrige Eingangsimpedanz und eine hohe Ausgangsimpedanz.

42. FET-Vorspannung: FETs werden typischerweise mit Widerständen und Spannungsquellen vorgespannt, um sicherzustellen, dass sie im gewünschten Bereich arbeiten (z. B. im Abklemmbereich für MOSFETs).

43. FET-Anwendungen: FETs werden weit verbreitet in rauscharmen Verstärkern, HF-Anwendungen und als spannungsgesteuerte Widerstände in analogen Schaltungen verwendet.

---

### Verstärker

44. Verstärkertypen: Verstärker können basierend auf ihrem Betrieb als Spannungsverstärker (Spannung verstärken), Stromverstärker (Strom verstärken) und Leistungsverstärker (beides verstärken) klassifiziert werden.

45. Transistorverstärker: Die drei Hauptkonfigurationen – Common-Emitter, Common-Collector und Common-Base – bieten jeweils einzigartige Impedanz- und Verstärkungseigenschaften.

46. Operationsverstärker (Op-Amps): Op-Amps sind vielseitige Verstärker mit hoher Verstärkung. Gängige Anwendungen umfassen Differenzverstärkung, Signalfilterung und mathematische Operationen.

47. Verstärkung von Verstärkern: Die Verstärkung eines Verstärkers bezieht sich darauf, wie stark das Eingangssignal verstärkt wird. Sie kann in Bezug auf Spannungs-, Strom- oder Leistungsverstärkung definiert werden, je nach Anwendung.

48. Rückkopplung in Verstärkern: Rückkopplung in Verstärkern kann entweder negativ (Verringerung der Verstärkung und Stabilisierung des Systems) oder positiv (Erhöhung der Verstärkung und potenziell zu Instabilität führend) sein.

49. Spannungs- und Stromrückkopplung: Spannungsrückkopplungsverstärker passen die Ausgabe basierend auf der Eingangsspannung an, während Stromrückkopplungsverstärker die Ausgabe basierend auf dem Eingangsstrom anpassen, was Bandbreite und Slew-Rate beeinflusst.

50. Bandbreite von Verstärkern: Verstärker zeigen typischerweise einen Kompromiss zwischen Bandbreite und Verstärkung. Höhere Verstärkung führt oft zu einer reduzierten Bandbreite und umgekehrt.

51. Leistungsverstärker: Diese werden verwendet, um Signale auf ein Niveau zu verstärken, das für das Ansteuern von Lautsprechern, Motoren oder anderen leistungshungrigen Geräten geeignet ist. Klassen A, B, AB und C definieren unterschiedliche Effizienz- und Linearitätseigenschaften.

52. Impedanzanpassung: Dies stellt sicher, dass die maximale Leistung zwischen Komponenten übertragen wird, indem die Quellen- und Lastimpedanzen angepasst werden.

---

### Oszillatoren

53. Sinusoidaloszillatoren: Diese Oszillatoren erzeugen sinusförmige Wellenformen, die häufig in Funkfrequenz (RF) und Audioanwendungen verwendet werden. Beispiele sind der Colpitts- und Hartley-Oszillator.

54. Relaxationsoszillatoren: Diese werden verwendet, um nicht-sinusförmige Wellenformen, typischerweise Rechteck- oder Sägezahnwellen, zu erzeugen, und werden in Zeit- und Taktanwendungen verwendet.

55. Quarzoszillatoren: Quarzoszillatoren verwenden einen Quarzkristall, um eine hochstabile Frequenz zu erzeugen. Sie werden weit verbreitet in Uhren, Radios und GPS-Systemen verwendet.

56. Phasenregelkreis (PLL): Ein PLL wird für Frequenzsynthese und Synchronisation verwendet, häufig in Kommunikationssystemen für Modulation und Demodulation von Signalen.

---

### Stromversorgungen

57. Lineare Regler: Diese Regler halten eine konstante Ausgangsspannung aufrecht, indem sie überschüssige Spannung als Wärme ableiten. Sie sind einfach, aber weniger effizient für Hochleistungsanwendungen.

58. Schaltregler: Schaltregler (Buck, Boost und Buck-Boost) wandeln die Eingangsspannung in eine gewünschte Ausgangsspannung mit höherer Effizienz im Vergleich zu linearen Reglern um.

59. Gleichrichter und Filter: Stromversorgungen enthalten oft Gleichrichter, um Wechselstrom in Gleichstrom umzuwandeln, gefolgt von Filtern (z. B. Kondensatoren), um die Ausgabe zu glätten.

60. Regeltechniken: Spannungsregelung hält eine stabile Ausgangsspannung trotz Schwankungen der Last oder Eingangsspannung aufrecht. Lineare Regler verwenden einen Durchlasstransistor, während Schaltregler induktive und kapazitive Komponenten verwenden.

61. Leistungsfaktorkorrektur (PFC): Diese Technik wird in Stromversorgungen verwendet, um die Phasendifferenz zwischen Spannung und Strom zu verringern, die Effizienz zu verbessern und die harmonische Verzerrung zu reduzieren.

---

### Kommunikationsschaltungen

62. Amplitudenmodulation (AM): AM ist eine Technik, bei der die Amplitude einer Trägerwelle proportional zum Modulationssignal variiert wird, häufig in Rundfunk verwendet.

63. Frequenzmodulation (FM): FM variiert die Frequenz einer Trägerwelle entsprechend dem Eingangssignal, häufig für hochwertigen Rundfunk verwendet.

64. Phasenmodulation (PM): Bei PM wird die Phase der Trägerwelle als Reaktion auf das Eingangssignal variiert.

65. Pulscode-Modulation (PCM): PCM ist ein Verfahren zur digitalen Darstellung analoger Signale durch Abtasten und Quantisierung des Signals in diskrete Werte.

66. Frequenzmultiplex (FDM): FDM teilt das verfügbare Frequenzspektrum in kleinere Teilbänder auf, wobei jedes Signal eine andere Frequenz trägt, weit verbreitet in Telekommunikationssystemen.

67. Zeitmultiplex (TDM): TDM teilt die Zeit in diskrete Schlitze auf und weist jedem Schlitz ein anderes Signal zu, sodass mehrere Signale das gleiche Übertragungsmedium teilen können.

68. Modulator- und Demodulatorschaltungen: Diese Schaltungen modulieren ein Eingangssignal zur Übertragung und demodulieren empfangene Signale zurück in ihre ursprüngliche Form.

---

### Signalverarbeitung

69. Filter: Filter werden verwendet, um unerwünschte Komponenten aus einem Signal zu entfernen. Typen umfassen Tiefpass-, Hochpass-, Bandpass- und Bandsperrfilter, die jeweils so gestaltet sind, dass sie bestimmte Frequenzen durchlassen, während sie andere dämpfen.

70. Verstärkung: Signalverstärkung verstärkt die Stärke eines Signals, ohne dessen Frequenzkomponenten zu verändern. Verstärker können in verschiedenen Konfigurationen verwendet werden, wie in Vorverstärkern, Leistungsverstärkern und Differenzverstärkern.

71. Digitale Signalverarbeitung (DSP): DSP ist die Manipulation von Signalen unter Verwendung digitaler Techniken. Sie umfasst Abtasten, Quantisierung und das Anwenden von Algorithmen wie Fourier-Transformationen, Faltung und Filterung zur Signalverarbeitung.

72. Analog-Digital-Wandlung (ADC): ADCs wandeln kontinuierliche analoge Signale in diskrete digitale Daten um. Sie sind für die Verbindung analoger Sensoren mit digitalen Systemen unerlässlich.

73. Digital-Analog-Wandlung (DAC): DACs führen den umgekehrten Prozess von ADCs durch, indem sie diskrete digitale Daten wieder in kontinuierliche analoge Signale umwandeln, zur Verwendung in Stellgliedern und anderen analogen Geräten.

74. Fourier-Transformation: Die Fourier-Transformation ist eine mathematische Technik, die zur Analyse des Frequenzinhalts eines Signals verwendet wird. Sie wird weit verbreitet in der Signalverarbeitung, Kommunikation und Steuerungssystemen verwendet.

75. Abtasttheorem: Das Nyquist-Shannon-Abtasttheorem besagt, dass ein Signal, um genau rekonstruiert zu werden, mindestens zweimal die höchste im Signal vorhandene Frequenz abgetastet werden muss.

---

### Drahtlose Kommunikation

76. Modulationstechniken: Modulation bezieht sich auf das Variieren eines Trägersignals entsprechend dem Informationssignal. Gängige Techniken umfassen Amplitudenmodulation (AM), Frequenzmodulation (FM), Phasenmodulation (PM) und fortschrittlichere Schemata wie Quadrature Amplitude Modulation (QAM), die in digitalen Kommunikationen verwendet werden.

77. Antennen: Antennen werden verwendet, um elektromagnetische Wellen zu senden und zu empfangen. Typen von Antennen umfassen Dipolantennen, Schleifenantennen, Parabolantennen und Patchantennen, die jeweils für verschiedene Anwendungen in drahtlosen Kommunikationssystemen geeignet sind.

78. Funkfrequenz (RF) Kommunikation: RF-Kommunikation umfasst das Übertragen von Daten über Funkwellen. RF-Systeme werden in Mobilfunknetzen, Wi-Fi, Bluetooth und Satellitenkommunikation verwendet, mit Frequenzen von einigen MHz bis zu mehreren GHz.

79. Drahtloses Netzwerken: Drahtlose Netze verbinden Geräte ohne physikalische Kabel. Technologien umfassen Wi-Fi, Bluetooth, Zigbee und 5G, jede mit spezifischen Anwendungsfällen für Kurzstrecken- oder Langstreckenkommunikation, Hochgeschwindigkeitsdatenübertragung und IoT-Anwendungen.

80. Spreizspektrum: Spreizspektrum ist eine Technik, die in der drahtlosen Kommunikation verwendet wird, um ein Signal über ein breites Frequenzband zu verbreiten, die Störungsresistenz zu erhöhen und die Sicherheit zu verbessern. Techniken umfassen Direct Sequence Spread Spectrum (DSSS) und Frequency Hopping Spread Spectrum (FHSS).

81. Mikrowellenkommunikation: Mikrowellenkommunikation verwendet Hochfrequenzfunkwellen (typischerweise 1 GHz bis 100 GHz) für Punkt-zu-Punkt-Kommunikation, einschließlich Satellitenverbindungen, Radarsystemen und Hochgeschwindigkeitsdatenverbindungen.

82. Drahtlose Protokolle: Drahtlose Protokolle definieren, wie Daten in einem drahtlosen Netzwerk übertragen werden. Beispiele umfassen IEEE 802.11 (Wi-Fi), IEEE 802.15 (Bluetooth) und Zigbee, jede mit unterschiedlichen Merkmalen für Datenrate, Reichweite und Stromverbrauch.

---

### Embedded Systems

83. Mikrocontroller: Mikrocontroller sind kleine Computer, die in einem einzigen Chip integriert sind, und werden in eingebetteten Systemen zur Steuerung von Geräten wie Sensoren, Motoren und Displays verwendet. Beliebte Mikrocontroller umfassen Arduino, Raspberry Pi und PIC-Mikrocontroller.

84. Echtzeitbetriebssysteme (RTOS): Ein RTOS ist ein Betriebssystem, das für Echtzeitanwendungen entwickelt wurde, bei denen Aufgaben innerhalb strenger Zeitvorgaben abgeschlossen werden müssen. Beispiele umfassen FreeRTOS, RTEMS und VxWorks.

85. Embedded Programming: Embedded Programming umfasst das Schreiben von Software für Mikrocontroller und andere eingebettete Geräte. Es erfordert Kenntnisse in niedrigschichtigen Programmiersprachen wie C und Assembler sowie Hardware-Schnittstellen und Optimierung.

86. Sensoren und Aktuatoren: Sensoren sind Geräte, die physikalische Eigenschaften wie Temperatur, Licht oder Bewegung erkennen, während Aktuatoren verwendet werden, um mit der physikalischen Welt zu interagieren, wie z. B. das Bewegen eines Motors oder das Steuern eines Ventils. Diese sind wesentliche Komponenten in IoT- und Automatisierungssystemen.

87. Schnittstellen: Eingebettete Systeme erfordern oft die Schnittstelle mit externen Komponenten wie Displays, Sensoren und Kommunikationsmodulen. Schnittstellentechniken umfassen I2C, SPI, UART und GPIO.

88. Strommanagement: Strommanagement ist in eingebetteten Systemen entscheidend, um den Energieverbrauch zu optimieren, insbesondere für batteriebetriebene Geräte. Techniken umfassen Stromsparmodi, Spannungsregler und effiziente Schaltungsdesigns.

---

### Leistungselektronik

89. Leistungsdioden: Leistungsdioden werden verwendet, um den Stromfluss in Hochleistungsanwendungen zu steuern, wie z. B. das Gleichrichten von Wechselstrom zu Gleichstrom. Sie sind so gestaltet, dass sie höhere Spannungen und Ströme als herkömmliche Dioden handhaben können.

90. Thyristoren: Ein Typ von Halbleiterbauelement, das zum Schalten und Steuern großer Mengen an Leistung verwendet wird. Thyristoren umfassen SCRs (Silicon-Controlled Rectifiers) und TRIACs, die häufig in Motorsteuerungen, Beleuchtung und Leistungsregelung verwendet werden.

91. Leistung-MOSFETs: Leistung-MOSFETs werden zum Schalten und Verstärken in Leistungselektronikschaltungen verwendet, insbesondere in Netzteilen, Motorantrieben und Wechselrichtern, aufgrund ihrer hohen Effizienz und schnellen Schalteigenschaften.

92. IGBTs (Bipolare Transistoren mit isolierter Gate): IGBTs kombinieren die Eigenschaften von BJTs und MOSFETs und werden in Hochleistungsanwendungen wie Wechselrichtern, Motorantrieben und Induktionsheizsystemen verwendet.

93. DC-DC-Wandler: DC-DC-Wandler werden verwendet, um eine DC-Spannungsebene in eine andere umzuwandeln, entweder durch Hochsetzen (Boost-Wandler) oder Heruntersetzen (Buck-Wandler) der Spannung, mit hoher Effizienz.

94. AC-DC-Wandler: Diese Wandler, auch als Gleichrichter bekannt, werden verwendet, um Wechselstrom (AC) in Gleichstrom (DC) umzuwandeln. Sie werden weit verbreitet in Netzteilen und in Anwendungen verwendet, in denen DC-Spannung erforderlich ist.

95. Wechselrichter: Wechselrichter wandeln Gleichstrom (DC) in Wechselstrom (AC) um und werden in erneuerbaren Energiesystemen, USV (Unterbrechungsfreien Stromversorgungen) und Elektrofahrzeugen verwendet.

96. Leistungssteuerung: Leistungssteuerung in elektronischen Systemen umfasst die Regelung von Spannungs- und Strompegeln für einen effizienten Energieeinsatz, oft durch Rückkopplungsschleifen, Modulation und Schaltregler.

---

### Automatisierung und Steuerungssysteme

97. Programmierbare Logikcontroller (PLCs): PLCs sind digitale Computer, die für die Automatisierung in industriellen Prozessen verwendet werden, wie z. B. Herstellung, Maschinensteuerung und Verwaltungssysteme wie Aufzüge oder Ampeln.

98. SCADA-Systeme: SCADA (Supervisory Control and Data Acquisition) Systeme werden zur Überwachung und Steuerung industrieller Prozesse verwendet, einschließlich Energieerzeugung, Wasseraufbereitung und Fertigungssysteme.

99. Industrielle Sensoren: Industrielle Sensoren werden verwendet, um physikalische Parameter wie Temperatur, Druck, Durchfluss und Füllstand in industriellen Automatisierungsanwendungen zu messen.

100. Motorsteuerung: Motorsteuerungssysteme werden verwendet, um Geschwindigkeit, Richtung und Betrieb von Motoren zu regulieren, einschließlich Gleichstrommotoren, Wechselstrommotoren und Schrittmotoren. Diese Systeme sind entscheidend für Automatisierung und Robotik.