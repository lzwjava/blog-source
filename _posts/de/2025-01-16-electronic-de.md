---
audio: false
generated: false
lang: de
layout: post
title: Grundlagen der Elektronik
translated: true
type: note
---

### Grundlegende elektronische Bauteile

1. **Widerstandstypen**: Widerstände begrenzen den Stromfluss in einem Stromkreis. Typen umfassen Festwiderstände, die einen festen Widerstandswert haben, und variable Widerstände wie Potentiometer, die eine einstellbare Widerstand ermöglichen.

2. **Kondensatortypen**: Kondensatoren speichern und geben elektrische Energie ab. Typen umfassen Keramikkondensatoren, die häufig für Hochfrequenzanwendungen verwendet werden, und Elektrolytkondensatoren, die höhere Kapazitätswerte haben, aber gepolt sind.

3. **Spulen**: Spulen speichern Energie in einem Magnetfeld und wirken Änderungen des Stroms entgegen. Sie werden in Filter- und Abstimmungsanwendungen eingesetzt.

4. **Dioden**: Dioden lassen Strom nur in einer Richtung fließen. Zenerdioden werden zur Spannungsregelung verwendet, während LEDs Licht emittieren, wenn sie in Durchlassrichtung betrieben werden.

5. **Transistoren**: Transistoren, wie BJTs, fungieren als elektronische Schalter oder Verstärker, wobei NPN- und PNP-Typen den Stromfluss in Schaltungen steuern.

6. **Feldeffekttransistor (FET)**: FETs steuern den Stromfluss durch Anlegen einer Spannung an das Gate, wobei MOSFETs weit verbreitet für Schalt- und Verstärkungsanwendungen sind.

7. **Fotodioden**: Diese Dioden erzeugen einen Strom, wenn sie Licht ausgesetzt werden, und werden in optischen Anwendungen wie Lichtsensoren verwendet.

8. **Optokoppler**: Optokoppler werden zur Isolierung verschiedener Teile einer Schaltung verwendet und übertragen elektrische Signale durch Licht, um die elektrische Trennung aufrechtzuerhalten.

9. **Gleichrichter**: Dioden werden in Gleichrichterschaltungen verwendet, um Wechselstrom in Gleichstrom umzuwandeln. Einweggleichrichter verwenden eine einzelne Diode, während Zweiweggleichrichter zwei oder mehr Dioden verwenden, um beide Halbwellen des AC-Signals umzuwandeln.

10. **Thermistoren**: Dies sind temperaturabhängige Widerstände. Heißleiter (NTC-Thermistoren) verringern ihren Widerstand mit steigender Temperatur, während Kaltleiter (PTC-Thermistoren) ihren Widerstand mit höheren Temperaturen erhöhen.

---

### Theorie der elektronischen Schaltungen

11. **Ohmsches Gesetz**: Das Ohmsche Gesetz beschreibt den Zusammenhang zwischen Spannung (V), Strom (I) und Widerstand (R) in einer linearen Schaltung: \\(V = I \times R\\). Es bildet die Grundlage für die meisten Analysen elektrischer Schaltungen.

12. **Kirchhoffsche Gesetze**: Der Kirchhoffsche Knotensatz (KCL) besagt, dass die Summe der in einen Knotenpunkt eintretenden Ströme gleich der Summe der austretenden Ströme ist, während der Kirchhoffsche Maschensatz (KVL) besagt, dass die Summe der Spannungen in einer geschlossenen Masche null ist.

13. **Thevenin-Theorem**: Dieses Theorem vereinfacht ein Netzwerk aus Widerständen und Quellen in eine äquivalente Spannungsquelle und einen Widerstand, um die Analyse zu erleichtern.

14. **Norton-Theorem**: Ähnlich wie das Thevenin-Theorem vereinfacht das Norton-Theorem ein Netzwerk in eine Stromquelle und einen Parallelwiderstand, um die Analyse von stromgesteuerten Schaltungen zu erleichtern.

15. **Überlagerungssatz**: In Schaltungen mit mehreren Quellen ermöglicht dieser Satz die unabhängige Analyse jeder Quelle und die anschließende Kombination der Ergebnisse.

16. **Maschenstromanalyse**: Eine Methode zur Ermittlung unbekannter Ströme in einer Schaltung unter Verwendung von Maschenströmen, die häufig in planaren Schaltungen angewendet wird.

17. **Knotenspannungsanalyse**: Eine Methode zum Lösen von Schaltungen durch Zuweisen von Spannungen zu Knoten (Verbindungspunkten) und Lösen nach den Unbekannten.

18. **Impedanz und Admittanz**: Impedanz ist der gesamte Wechselstromwiderstand in AC-Schaltungen, der Widerstand und Blindwiderstand kombiniert. Admittanz ist der Kehrwert der Impedanz und beschreibt, wie leicht Strom durch eine Komponente fließt.

19. **Leistung in Wechselstromkreisen**: In Wechselstromkreisen wird die Leistung in Wirkleistung, Blindleistung und Scheinleistung unterteilt. Der Leistungsfaktor stellt das Verhältnis von Wirkleistung zu Scheinleistung dar.

20. **Resonanz**: Resonanz tritt in LC-Schaltungen auf, wenn der induktive Blindwiderstand und der kapazitive Blindwiderstand gleich groß, aber entgegengesetzt in der Phase sind, was einen maximalen Energieübertrag ermöglicht.

---

### Diodenschaltungen

21. **Grundlegende Diodentheorie**: Dioden lassen Strom nur in der Durchlassrichtung fließen (positiv zur Anode, negativ zur Kathode) und blockieren den Strom in Sperrrichtung.

22. **Gleichrichterschaltungen**: Einweggleichrichter verwenden eine einzelne Diode, während Zweiweggleichrichter zwei oder vier Dioden verwenden, um AC in DC umzuwandeln. Brückengleichrichter sind in Stromversorgungsschaltungen üblich.

23. **Begrenzerschaltungen**: Diese Schaltungen begrenzen den Spannungspegel, indem sie die Wellenform bei einem bestimmten Schwellenwert abschneiden (clippen). Sie werden in der Wellenformgebung und zum Schutz von Signalen verwendet.

24. **Klemmerschaltungen**: Diese Schaltungen verschieben den Spannungspegel einer Wellenform und werden häufig verwendet, um eine Basisspannung festzulegen oder negative Ausschläge in einem Signal zu eliminieren.

25. **Zenerdiode**: Zenerdioden sind für den Betrieb im Sperrbereich ausgelegt und halten eine konstante Spannung über einen weiten Strombereich aufrecht. Sie werden häufig zur Spannungsregelung verwendet.

26. **LEDs**: Lichtemittierende Dioden emittieren Licht, wenn Strom durch sie fließt. Sie werden weit verbreitet in Displays, Anzeigen und Hintergrundbeleuchtung eingesetzt.

27. **Diodenanwendungen**: Dioden werden in der Signaldetektion, Leistungsgleichrichtung, Spannungsregelung und in Kommunikationssystemen als Modulatoren oder Demodulatoren verwendet.

---

### Transistorschaltungen

28. **BJT-Eigenschaften**: BJTs haben drei Bereiche: Emitter, Basis und Kollektor. Der Strom, der von der Basis fließt, steuert den größeren Strom zwischen Emitter und Kollektor.

29. **Transistorvorspannung**: Die Transistorvorspannung legt einen Arbeitspunkt im aktiven Bereich fest. Gängige Methoden umfassen Festspannungsvorspannung, Spannungsteilervorspannung und Emitterstabilisierung.

30. **Common-Emitter-Verstärker**: Dies ist eine der am weitesten verbreiteten Transistorverstärker-Konfigurationen, die eine gute Spannungsverstärkung bietet, jedoch mit einer Phasenumkehr.

31. **Common-Collector-Verstärker**: Auch bekannt als Emitterfolger, hat diese Schaltung eine Spannungsverstärkung von etwa 1 und eine hohe Eingangsimpedanz, was sie für die Impedanzanpassung nützlich macht.

32. **Common-Base-Verstärker**: Wird typischerweise in Hochfrequenzanwendungen eingesetzt und bietet eine hohe Spannungsverstärkung, aber eine niedrige Eingangsimpedanz.

33. **Schaltschaltungen**: Transistoren können als digitale Schalter verwendet werden, um Geräte in Logikschaltungen und digitalen Systemen ein- und auszuschalten.

34. **Darlington-Paar**: Eine Kombination aus zwei Transistoren, die eine hohe Stromverstärkung bietet. Es wird oft verwendet, wenn eine hohe Stromverstärkung benötigt wird.

35. **Sättigungs- und Sperrbereich**: Ein Transistor arbeitet in Sättigung, wenn er vollständig eingeschaltet ist (wirkt wie ein geschlossener Schalter), und im Sperrbereich, wenn er vollständig ausgeschaltet ist (wirkt wie ein offener Schalter).

---

### Feldeffekttransistor-Schaltungen

36. **JFET-Eigenschaften**: Der Junction Field-Effect Transistor (JFET) wird durch die Spannung am Gate gesteuert, wobei Strom zwischen Source und Drain fließt. Das Gate ist in Sperrrichtung vorgespannt, und der Drain-Strom hängt von der Gate-Source-Spannung ab.

37. **MOSFET-Typen**: MOSFETs (Metall-Oxid-Halbleiter-Feldeffekttransistoren) werden häufig für Schalt- und Verstärkungsanwendungen verwendet. Es gibt zwei Typen: Enhancement-Mode (normalerweise ausgeschaltet) und Depletion-Mode (normalerweise eingeschaltet).

38. **MOSFET-Betrieb**: Der MOSFET arbeitet, indem er einen leitfähigen Kanal zwischen Source und Drain erzeugt, der durch die am Gate angelegte Spannung gesteuert wird.

39. **Common-Source-Verstärker**: Diese Konfiguration wird zur Spannungsverstärkung verwendet und bietet eine hohe Verstärkung und eine moderate Ein-/Ausgangsimpedanz.

40. **Common-Drain-Verstärker**: Bekannt als Sourcefolger, bietet dieser Verstärker eine niedrige Ausgangsimpedanz, was ihn für die Impedanzanpassung geeignet macht.

41. **Common-Gate-Verstärker**: Diese Konfiguration wird in Hochfrequenzanwendungen verwendet und bietet eine niedrige Eingangsimpedanz und eine hohe Ausgangsimpedanz.

42. **FET-Vorspannung**: FETs werden typischerweise mit Widerständen und Spannungsquellen vorgespannt, um sicherzustellen, dass sie im gewünschten Bereich arbeiten (z.B. Pinch-Off-Bereich für MOSFETs).

43. **FET-Anwendungen**: FETs werden weit verbreitet in rauscharmen Verstärkern, HF-Anwendungen und als spannungsgesteuerte Widerstände in analogen Schaltungen eingesetzt.

---

### Verstärker

44. **Verstärkertypen**: Verstärker können nach ihrer Funktion als Spannungsverstärker (verstärken Spannung), Stromverstärker (verstärken Strom) und Leistungsverstärker (verstärken beides) klassifiziert werden.

45. **Transistorverstärker**: Die drei Hauptkonfigurationen – Common-Emitter, Common-Collector und Common-Base – bieten jeweils einzigartige Impedanz- und Verstärkungseigenschaften.

46. **Operationsverstärker (Op-Amps)**: Op-Amps sind vielseitige Verstärker mit hoher Verstärkung. Häufige Anwendungen umfassen Differenzverstärkung, Signalfilterung und mathematische Operationen.

47. **Verstärkung von Verstärkern**: Die Verstärkung eines Verstärkers bezieht sich darauf, wie stark das Eingangssignal verstärkt wird. Sie kann als Spannungs-, Strom- oder Leistungsverstärkung definiert werden, abhängig von der Anwendung.

48. **Rückkopplung in Verstärkern**: Die Rückkopplung in Verstärkern kann entweder negativ (reduziert die Verstärkung und stabilisiert das System) oder positiv (erhöht die Verstärkung und kann zu Instabilität führen) sein.

49. **Spannungs- und Stromrückkopplung**: Spannungsrückkopplungsverstärker passen den Ausgang basierend auf der Eingangsspannung an, während Stromrückkopplungsverstärker den Ausgang basierend auf dem Eingangsstrom anpassen, was Bandbreite und Anstiegsgeschwindigkeit beeinflusst.

50. **Bandbreite von Verstärkern**: Verstärker zeigen typischerweise einen Kompromiss zwischen Bandbreite und Verstärkung. Höhere Verstärkung führt oft zu reduzierter Bandbreite und umgekehrt.

51. **Leistungsverstärker**: Diese werden verwendet, um Signale auf ein Niveau zu verstärken, das für den Antrieb von Lautsprechern, Motoren oder anderen leistungsstarken Geräten geeignet ist. Die Klassen A, B, AB und C definieren unterschiedliche Effizienz- und Linearitätseigenschaften.

52. **Impedanzanpassung**: Dies stellt durch Anpassung der Quellen- und Lastimpedanzen eine maximale Leistungsübertragung zwischen Komponenten sicher.

---

### Oszillatoren

53. **Sinusoszillatoren**: Diese Oszillatoren erzeugen sinusförmige Wellenformen und werden häufig in Hochfrequenz- (RF) und Audioanwendungen eingesetzt. Beispiele umfassen Colpitts- und Hartley-Oszillatoren.

54. **Kippschwingungen (Relaxationsoszillatoren)**: Diese werden verwendet, um nicht-sinusförmige Wellenformen, typischerweise Rechteck- oder Sägezahnwellen, zu erzeugen, und werden in Timing- und Taktanwendungen verwendet.

55. **Quarzoszillatoren**: Quarzoszillatoren verwenden einen Quarzkristall, um eine hochstabile Frequenz zu erzeugen. Sie werden weit verbreitet in Uhren, Radios und GPS-Systemen eingesetzt.

56. **Phase-Locked Loop (PLL)**: Eine PLL wird zur Frequenzsynthese und Synchronisation verwendet und häufig in Kommunikationssystemen zum Modulieren und Demodulieren von Signalen eingesetzt.

---

### Stromversorgungen

57. **Lineare Regler**: Diese Regler halten eine konstante Ausgangsspannung aufrecht, indem sie überschüssige Spannung als Wärme abführen. Sie sind einfach, aber weniger effizient für Hochleistungsanwendungen.

58. **Schaltregler**: Schaltregler (Buck-, Boost- und Buck-Boost-Wandler) wandeln die Eingangsspannung in eine gewünschte Ausgangsspannung um und sind im Vergleich zu linearen Reglern effizienter.

59. **Gleichrichter und Filter**: Stromversorgungen enthalten oft Gleichrichter zur Umwandlung von AC in DC, gefolgt von Filtern (z.B. Kondensatoren), um die Ausgangsspannung zu glätten.

60. **Regelungstechniken**: Die Spannungsregelung hält eine stabile Ausgangsspannung trotz Schwankungen in Last oder Eingangsspannung aufrecht. Lineare Regler verwenden einen Durchgangstransistor, während Schaltregler induktive und kapazitive Komponenten verwenden.

61. **Leistungsfaktorkorrektur (PFC)**: Diese Technik wird in Stromversorgungen verwendet, um die Phasendifferenz zwischen Spannung und Strom zu reduzieren, was die Effizienz verbessert und harmonische Verzerrungen reduziert.

---

### Kommunikationsschaltungen

62. **Amplitudenmodulation (AM)**: AM ist eine Technik, bei der die Amplitude einer Trägerwelle proportional zum Modulationssignal variiert wird. Sie wird häufig im Rundfunk verwendet.

63. **Frequenzmodulation (FM)**: FM beinhaltet die Variation der Frequenz einer Trägerwelle entsprechend dem Eingangssignal und wird häufig für hochwertigeren Rundfunk verwendet.

64. **Phasenmodulation (PM)**: Bei PM wird die Phase der Trägerwelle als Reaktion auf das Eingangssignal variiert.

65. **Puls-Code-Modulation (PCM)**: PCM ist eine Methode zur digitalen Darstellung analoger Signale durch Abtastung und Quantisierung des Signals in diskrete Werte.

66. **Frequenzmultiplex (FDM)**: FDM teilt das verfügbare Frequenzspektrum in kleinere Teilbänder auf, die jeweils ein unterschiedliches Signal tragen. Es wird weit verbreitet in Telekommunikationssystemen eingesetzt.

67. **Zeitmultiplex (TDM)**: TDM teilt die Zeit in diskrete Zeitschlitze auf und weist jedem Schlitz ein anderes Signal zu, wodurch mehrere Signale dasselbe Übertragungsmedium teilen können.

68. **Modulator- und Demodulator-Schaltungen**: Diese Schaltungen modulieren ein Eingangssignal für die Übertragung und demodulieren empfangene Signale zurück in ihre ursprüngliche Form.

---

### Signalverarbeitung

69. **Filter**: Filter werden verwendet, um unerwünschte Komponenten aus einem Signal zu entfernen. Typen umfassen Tiefpass-, Hochpass-, Bandpass- und Bandsperrenfilter, die jeweils bestimmte Frequenzen durchlassen und andere dämpfen.

70. **Verstärkung**: Die Signalverstärkung erhöht die Stärke eines Signals, ohne seine Frequenzkomponenten zu verändern. Verstärker können in verschiedenen Konfigurationen verwendet werden, wie z.B. in Vorverstärkern, Leistungsverstärkern und Differenzverstärkern.

71. **Digitale Signalverarbeitung (DSP)**: DSP ist die Manipulation von Signalen mit digitalen Techniken. Sie umfasst Abtastung, Quantisierung und die Anwendung von Algorithmen wie Fourier-Transformationen, Faltung und Filterung zur Signalverarbeitung.

72. **Analog-Digital-Umsetzung (ADC)**: ADCs wandeln kontinuierliche analoge Signale in diskrete digitale Daten um. Sie sind essentiell für die Verbindung analoger Sensoren mit digitalen Systemen.

73. **Digital-Analog-Umsetzung (DAC)**: DACs führen die Umkehrung von ADCs durch und wandeln diskrete digitale Daten zurück in kontinuierliche analoge Signale für die Verwendung in Aktoren und anderen analogen Geräten.

74. **Fourier-Transformation**: Die Fourier-Transformation ist eine mathematische Technik zur Analyse des Frequenzinhalts eines Signals. Sie wird weit verbreitet in der Signalverarbeitung, Kommunikation und Regelungstechnik eingesetzt.

75. **Abtasttheorem**: Das Nyquist-Shannon-Abtasttheorem besagt, dass ein Signal mit mindestens der doppelten Frequenz seiner höchsten vorkommenden Frequenz abgetastet werden muss, um es genau rekonstruieren zu können.

---

### Drahtlose Kommunikation

76. **Modulationstechniken**: Modulation bezieht sich auf die Variation eines Trägersignals entsprechend dem Informationssignal. Gängige Techniken umfassen Amplitudenmodulation (AM), Frequenzmodulation (FM), Phasenmodulation (PM) und fortschrittlichere Schemata wie Quadratur-Amplitudenmodulation (QAM), die in der digitalen Kommunikation verwendet werden.

77. **Antennen**: Antennen werden zum Senden und Empfangen elektromagnetischer Wellen verwendet. Antennentypen umfassen Dipolantennen, Rahmenantennen, Parabolantennen und Patch-Antennen, die jeweils für verschiedene Anwendungen in drahtlosen Kommunikationssystemen geeignet sind.

78. **Hochfrequenz (HF)-Kommunikation**: HF-Kommunikation beinhaltet die Übertragung von Daten über Funkwellen. HF-Systeme werden in Mobilfunknetzen, Wi-Fi, Bluetooth und Satellitenkommunikation eingesetzt, mit Frequenzen von wenigen MHz bis zu mehreren GHz.

79. **Drahtlose Netzwerke**: Drahtlose Netzwerke verbinden Geräte ohne physische Kabel. Technologien umfassen Wi-Fi, Bluetooth, Zigbee und 5G, jeweils mit spezifischen Anwendungsfällen für Kurzstrecken- oder Langstreckenkommunikation, Hochgeschwindigkeits-Datenübertragung und IoT-Anwendungen.

80. **Spreizspektrum**: Spreizspektrum ist eine Technik in der drahtlosen Kommunikation, um ein Signal über ein breites Frequenzband zu verteilen, was die Störungsresistenz erhöht und die Sicherheit verbessert. Techniken umfassen Direct Sequence Spread Spectrum (DSSS) und Frequency Hopping Spread Spectrum (FHSS).

81. **Mikrowellenkommunikation**: Mikrowellenkommunikation verwendet hochfrequente Funkwellen (typischerweise 1 GHz bis 100 GHz) für Punkt-zu-Punkt-Kommunikation, einschließlich Satellitenverbindungen, Radarsystemen und Hochgeschwindigkeits-Datenlinks.

82. **Drahtlose Protokolle**: Drahtlose Protokolle definieren, wie Daten in einem drahtlosen Netzwerk übertragen werden. Beispiele umfassen IEEE 802.11 (Wi-Fi), IEEE 802.15 (Bluetooth) und Zigbee, jeweils mit unterschiedlichen Merkmalen für Datenrate, Reichweite und Stromverbrauch.

---

### Eingebettete Systeme

83. **Mikrocontroller**: Mikrocontroller sind kleine Computer, die in einem einzigen Chip integriert sind und in eingebetteten Systemen zur Steuerung von Geräten wie Sensoren, Motoren und Displays verwendet werden. Beliebte Mikrocontroller umfassen Arduino, Raspberry Pi und PIC-Mikrocontroller.

84. **Echtzeitbetriebssysteme (RTOS)**: Ein RTOS ist ein Betriebssystem, das für Echtzeitanwendungen entwickelt wurde, bei denen Aufgaben innerhalb strenger Zeitvorgaben abgeschlossen werden müssen. Beispiele umfassen FreeRTOS, RTEMS und VxWorks.

85. **Embedded Programming**: Embedded Programming umfasst das Schreiben von Software für Mikrocontroller und andere eingebettete Geräte. Es erfordert Kenntnisse in Low-Level-Programmiersprachen wie C und Assembler sowie Hardware-Schnittstellen und Optimierung.

86. **Sensoren und Aktoren**: Sensoren sind Geräte, die physikalische Eigenschaften wie Temperatur, Licht oder Bewegung erfassen, während Aktoren verwendet werden, um mit der physischen Welt zu interagieren, z.B. um einen Motor zu bewegen oder ein Ventil zu steuern. Dies sind wesentliche Komponenten in IoT- und Automatisierungssystemen.

87. **Schnittstellen**: Eingebettete Systeme erfordern oft die Verbindung mit externen Komponenten wie Displays, Sensoren und Kommunikationsmodulen. Schnittstellentechniken umfassen I2C, SPI, UART und GPIO.

88. **Energiemanagement**: Das Energiemanagement ist in eingebetteten Systemen entscheidend, um den Energieverbrauch zu optimieren, insbesondere für batteriebetriebene Geräte. Techniken umfassen Energiesparmodi, Spannungsregler und effiziente Schaltungsdesigns.

---

### Leistungselektronik

89. **Leistungsdioden**: Leistungsdioden werden verwendet, um den Stromfluss in Hochleistungsanwendungen zu steuern, z.B. beim Gleichrichten von AC- zu DC-Leistung. Sie sind dafür ausgelegt, höhere Spannungen und Ströme als normale Dioden zu handhaben.

90. **Thyristoren**: Eine Art von Halbleiterbauelement, das für das Schalten und Steuern großer Leistungsmengen verwendet wird. Thyristoren umfassen SCRs (Silizium-gesteuerte Gleichrichter) und TRIACs, die häufig in der Motorsteuerung, Beleuchtung und Leistungsregelung eingesetzt werden.

91. **Leistungs-MOSFETs**: Leistungs-MOSFETs werden für Schalt- und Verstärkungsanwendungen in leistungselektronischen Schaltungen verwendet, insbesondere in Stromversorgungen, Motorantrieben und Wechselrichtern, aufgrund ihrer hohen Effizienz und schnellen Schalteigenschaften.

92. **IGBTs (Bipolare Transistoren mit isoliertem Gate)**: IGBTs kombinieren die Eigenschaften von BJTs und MOSFETs und werden in Hochleistungsanwendungen wie Wechselrichtern, Motorantrieben und Induktionsheizsystemen eingesetzt.

93. **DC-DC-Wandler**: DC-DC-Wandler werden verwendet, um eine DC-Spannungsebene in eine andere umzuwandeln, entweder herauf (Boost-Wandler) oder herab (Buck-Wandler) zu setzen, mit hoher Effizienz.

94. **AC-DC-Wandler**: Diese Wandler, auch bekannt als Gleichrichter, werden verwendet, um Wechselstrom (AC) in Gleichstrom (DC) umzuwandeln. Sie werden weit verbreitet in Stromversorgungen und in Anwendungen eingesetzt, wo DC-Spannung benötigt wird.

95. **Wechselrichter**: Wechselrichter wandeln DC- in AC-Leistung um und werden in erneuerbaren Energiesystemen, USV (unterbrechungsfreie Stromversorgungen) und Elektrofahrzeugen eingesetzt.

96. **Leistungssteuerung**: Die Leistungssteuerung in elektronischen Systemen umfasst die Regelung von Spannungs- und Strompegeln für eine effiziente Energienutzung, oft durch Rückkopplungsschleifen, Modulation und Schaltregler.

---

### Automatisierungs- und Steuerungssysteme

97. **Speicherprogrammierbare Steuerungen (SPS)**: SPS sind digitale Computer, die für die Automatisierung in industriellen Prozessen verwendet werden, wie in der Fertigung, zur Steuerung von Maschinen und zur Verwaltung von Systemen wie Aufzügen oder Ampeln.

98. **SCADA-Systeme**: SCADA (Supervisory Control and Data Acquisition) Systeme werden zur Überwachung und Steuerung industrieller Prozesse eingesetzt, einschließlich Energieerzeugung, Wasseraufbereitung und Fertigungssystemen.

99. **Industrielle Sensoren**: Industrielle Sensoren werden verwendet, um physikalische Parameter wie Temperatur, Druck, Durchfluss und Füllstand in industriellen Automatisierungsanwendungen zu messen.

100. **Motorsteuerung**: Motorsteuerungssysteme werden verwendet, um die Geschwindigkeit, Richtung und den Betrieb von Motoren zu regeln, einschließlich Gleichstrommotoren, Wechselstrommotoren und Schrittmotoren. Diese Systeme sind entscheidend in der Automatisierung und Robotik.