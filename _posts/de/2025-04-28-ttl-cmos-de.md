---
audio: false
generated: true
lang: de
layout: post
title: TTL- und CMOS-Integrierte Schaltkreise
translated: true
type: note
---

## TTL (Transistor-Transistor Logic)

TTL wurde in den frühen 1960er Jahren von Texas Instruments entwickelt, wobei die 1964 eingeführte 7400er-Serie zu einem Industriestandard wurde. TTL stellte einen bedeutenden Fortschritt gegenüber früheren Technologien wie DTL (Diode-Transistor-Logik) dar.

Wichtige Entwicklungen in der Geschichte von TTL:
- Ursprünglich 1961 von James L. Buie bei TRW entwickelt
- Kommerzialisiert von Texas Instruments mit ihrer 5400/7400-Serie
- Standard-TTL entwickelte sich zu verbesserten Varianten weiter:
  - High-speed TTL (74H-Serie)
  - Low-power TTL (74L-Serie)
  - Schottky-TTL (74S-Serie), die die Laufzeitverzögerung reduzierte
  - Low-power Schottky (74LS-Serie)
  - Advanced Low-power Schottky (74ALS-Serie)
  - Fast (74F-Serie)

TTL dominierte von den späten 1960er Jahren bis durch die 1970er Jahre die digitale Logik und wurde in frühen Mikrocomputern, Taschenrechnern und verschiedenen Industrieanlagen verwendet. Ihre weite Verbreitung war auf Standardisierung, Zuverlässigkeit und relativ niedrige Kosten zurückzuführen.

## CMOS (Complementary Metal-Oxide-Semiconductor)

Die CMOS-Technologie wurde 1963 von Frank Wanlass bei Fairchild Semiconductor erfunden. Die Technologie erlangte in den 1970er Jahren kommerzielle Bedeutung und übertraf schließlich TTL.

Wichtige Entwicklungen in der Geschichte von CMOS:
- Patent von Frank Wanlass im Jahr 1963 eingereicht
- RCA entwickelte die 4000er-Serie CMOS-Logikfamilie in den frühen 1970er Jahren
- Anfangs langsamer als TTL, bot aber einen deutlich geringeren Stromverbrauch
- Die in den 1980er Jahren eingeführte High-Density CMOS (HC/HCT)-Serie verbesserte die Geschwindigkeit
- Advanced CMOS (AC/ACT) verbesserte die Leistung in den späten 1980er Jahren weiter

CMOS wurde schließlich aus mehreren Gründen zur dominanten Technologie:
- Viel geringerer Stromverbrauch, insbesondere im Ruhezustand
- Bessere Störfestigkeit
- Größerer Betriebsspannungsbereich
- Höhere Integrationsdichte
- Fertigungsskalierbarkeit, die es ermöglichte, das Mooresche Gesetz fortzusetzen

Bis in die 1990er Jahre war CMOS die Grundlage für nahezu alle digitalen ICs, von einfachen Logikgattern bis hin zu komplexen Mikroprozessoren. Die heutigen fortschrittlichen Prozessoren, Speicherchips und ASICs basieren fast ausschließlich auf CMOS, wenn auch mit erheblichen Verbesserungen der Basistechnologie.

Möchten Sie spezifischere Informationen zu einem bestimmten Aspekt der TTL- oder CMOS-Geschichte?

---

# Wie TTL- und CMOS-Integrierte Schaltkreise funktionieren

## TTL (Transistor-Transistor Logic)

TTL arbeitet mit Bipolartransistoren (BJTs) und funktioniert durch eine spezielle Anordnung dieser Transistoren:

1. **Eingangsstufe**: Verwendet einen Multi-Emitter-Transistor, bei dem jeder Emitter als Eingang dient.

2. **Funktionsprinzip**:
   - Wenn alle Eingänge HIGH (~5V) sind, ist die Basis-Kollektor-Strecke des Eingangstransistors in Durchlassrichtung gepolt und seine Kollektor-Emitter-Strecke in Sperrrichtung, wodurch der Ausgangstransistor AUSgeschaltet wird.
   - Wenn ein Eingang LOW (~0V) wird, sättigt der Eingangstransistor und schaltet den Ausgangstransistor EIN.

3. **Ausgangsstufe**: Verwendet typischerweise eine "Totem-Pole"-Anordnung mit zwei Transistoren. Der obere Transistor fungiert als Pull-Up (Quellenstrom), und der untere Transistor fungiert als Pull-Down (Senkenstrom).

4. **Eigenschaften**:
   - Arbeitet mit einer 5V-Versorgungsspannung
   - Robuste Störfestigkeit (typischerweise 0,8V für LOW, 2,0V für HIGH)
   - Kann mehr Strom senken als quellen
   - Aktive Pull-Up- und Pull-Down-Komponenten

## CMOS (Complementary Metal-Oxide-Semiconductor)

CMOS arbeitet mit komplementären Paaren von MOSFETs (Metall-Oxid-Halbleiter-Feldeffekttransistoren):

1. **Grundstruktur**: Jedes Logikgatter enthält komplementäre Paare von P-Kanal- (PMOS) und N-Kanal- (NMOS) Transistoren.

2. **Funktionsprinzip**:
   - Wenn der Eingang LOW (0V) ist, schaltet der PMOS-Transistor EIN, während der NMOS-Transistor AUSschaltet.
   - Wenn der Eingang HIGH (Versorgungsspannung) ist, schaltet der PMOS-Transistor AUS, während der NMOS-Transistor EINschaltet.
   - Dies erzeugt eine komplementäre Schaltwirkung, bei der jeweils nur ein Transistor EINgeschaltet ist.

3. **Stromverbrauchseigenschaften**:
   - Nahezu null statischer Stromverbrauch (Strom wird nur beim Schalten verbraucht)
   - Strom fließt nur kurz während Zustandsänderungen, wenn beide Transistoren teilweise leitend sind
   - Der Stromverbrauch steigt mit der Schaltfrequenz

4. **Hauptmerkmale**:
   - Großer Betriebsspannungsbereich (typischerweise 3-15V für ältere CMOS, 1,8-5V für moderne Varianten)
   - Hohe Störfestigkeit (typischerweise 30-40% der Versorgungsspannung)
   - Nahezu gleiche Quell- und Senkfähigkeiten
   - Sehr hoher Eingangswiderstand

Der grundlegende Unterschied zwischen TTL und CMOS besteht darin, dass TTL stromgesteuerte Bipolartransistoren verwendet, während CMOS spannungsgesteuerte Feldeffekttransistoren verwendet, was zu dem deutlich geringeren Stromverbrauch von CMOS führt, aber traditionell langsamere Schaltgeschwindigkeiten mit sich brachte (obwohl moderne CMOS diese Einschränkung überwunden hat).