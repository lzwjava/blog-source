---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Produktion von Ladestationen für Elektrofahrzeuge in China
translated: true
type: note
---

### Ladesäulen für Elektrofahrzeuge in China: Überblick und interne Struktur

China führt tatsächlich weltweit bei der Ladeinfrastruktur für Elektrofahrzeuge. Mitte 2025 verfügt das Land über mehr als 10 Millionen öffentliche Ladepunkte, angetrieben durch staatliche Vorgaben, Subventionen und massive heimische Produktion. Dieses Netzwerk unterstützt das schnelle Wachstum der Elektrofahrzeuge, mit Stationen überall, von Autobahnen bis zu städtischen Gehwegen. Diese Stationen werden in großen Stückzahlen von Unternehmen wie State Grid, TELD und Star Charge produziert und verwenden standardisierte GB/T-Stecker (ähnlich wie Europas Typ 2, aber für Gleichstrom-Hochleistung optimiert).

#### Wie werden sie hergestellt?
Ladesäulen für Elektrofahrzeuge werden wie modulare Elektronikschränke montiert, die Standard- und kundenspezifische Komponenten in Fabriken kombinieren. Der Prozess umfasst:
- Beschaffung von Leistungselektronik (z.B. Halbleiter von Lieferanten wie Infineon).
- Integration von Software für Smart-Grid-Kompatibilität.
- Tests auf Sicherheit (z.B. IP65 Wetterschutz und UL/IEC-Zertifizierungen).
- Unterbringung aller Komponenten in einem robusten Metall- oder Verbundgehäuse für den Außeneinsatz.
Chinas Vorteil sind die niedrigen Kosten und die hohe Stückzahl – Stationen können für AC-Modelle nur 500–2.000 US-Dollar pro Einheit kosten, mit steigenden Kosten für DC-Schnelllader.

#### AC- und DC-Wandler: Ja, und sie handhaben hohe Spannungen
Die meisten Stationen unterstützen sowohl AC- (langsamer, Level 1/2) als auch DC- (schnell, Level 3) Laden:
- **AC-Lader** nehmen Wechselstrom aus dem Netz (z.B. 220–240V einphasig oder 380–480V dreiphasig) und leiten ihn direkt zum onboard-Wandler des E-Fahrzeugs weiter. Keine aufwändige Umwandlung in der Station – nur Regelung.
- **DC-Schnelllader** (in China auf Autobahnen üblich) haben eingebaute AC-DC-Wandler (Gleichrichter und Wechselrichter mit IGBTs/MOSFETs). Diese wandeln den Hochspannungs-Wechselstromeingang in einen einstellbaren Gleichstromausgang um (400–1.000V, bis zu 250kW+), umgehen den Wandler des Autos für schnelleres Laden (z.B. 80 % in 20–30 Minuten).
Sie handhaben „große Volt“ mittels robuster Leistungselektronik, die für 480V AC-Eingang und Spannungsspitzen bis zu 1.500V ausgelegt ist, mit Schutz vor Überspannungen. Chinas Netz unterstützt dies mit stabilem Drehstrom, und Stationen beinhalten oft Energiespeicher (BESS) für Lastspitzenabdeckung.

#### Was befindet sich in der großen Box (Ladeschrank)?
Die „große Box“ ist das wetterfeste Podest oder wandmontierte Gehäuse (typischerweise 1–2 m hoch, Stahl/Aluminium mit IP65-Schutzart). Hier ist die Ladebuchse (Kabel mit GB/T-Stecker) untergebracht. Im Inneren ist sie vollgepackt mit Elektronik, Kühlung und Steuerung – vergleichbar mit einem kleinen Kraftwerk. Wichtige Komponenten sind:

| Komponente | Beschreibung | Rolle beim Laden |
|------------|--------------|------------------|
| **Leistungs-/Lademodul** | Kern-AC-DC-Gleichrichter, DC-DC-Wandler und Halbleiter (z.B. IGBTs). Nimmt ~50 % des Platzes/Kosten ein. | Wandelt Netz-AC in Hochspannungs-Gleichstrom um; passt die Ausgabe an die Batteriebedürfnisse an (z.B. 200–800V). |
| **Steuereinheit** | Mikroprozessor-/PLC-Platine mit Software. | Verwaltet die Kommunikation (OCPP-Protokoll), überwacht den Batteriezustand und regelt die Leistung sicher hoch. |
| **Sicherheitssysteme** | FI-Schutzschalter, Überstrom-/Überspannungsrelais, Temperatursensoren. | Verhindert Stromschläge, Überlastung oder Brände; schaltet bei Fehlern automatisch ab. |
| **Kühlsystem** | Lüfter, Kühlkörper oder Klimaanlagen (2–5kW). | Führt Wärme aus dem Hochleistungsbetrieb ab (bis zu 47°C Umgebungstemperatur). |
| **Mess- & Kommunikationstechnik** | Energiezähler und WiFi/4G-Module. | Verfolgt die Nutzung für die Abrechnung; verbindet sich mit Apps/Cloud für Fernüberwachung. |
| **Kabelmanagement** | Interne Kabeltrommeln oder Anschlüsse für die Ladebuchse (5–7 m Kabel). | Lagert und bedient die Ladebuchse; beinhaltet Zugentlastung. |
| **Benutzeroberfläche** | LCD-Bildschirm, RFID/QR-Code-Zahlungsleser. | Zeigt Status an, akzeptiert Zahlungen (WeChat/Alipay in China üblich). |

Der Schrank verfügt auch über Anschlussklemmen für den Netzanschluss und EMV-Abschirmung zur Geräuschreduzierung. Für Ultra-Schnellmodelle (z.B. 200kW+ in Städten wie Shanghai) könnte er eine kleine Batterie für die Speicherung außerhalb der Spitzenlastzeiten enthalten.

Dieser Aufbau macht Chinas Ladesäulen zuverlässig und skalierbar und versorgt über 20 Millionen Elektrofahrzeuge mit Strom. Wenn Sie an einem bestimmten Modell oder einer bestimmten Installation interessiert sind, lassen Sie es mich wissen!

[What Are The Main Components Of EV Chargers](https://sinoevse.com/what-are-the-main-components-of-ev-chargers/)  
[Key Components of DC Fast Charging Stations](https://www.franklingrid.com/en/this-is-franklin-grid/blog/key-components-of-dc-fast-charging-stations/)  
[Electric Vehicle Charging Station Cabinets: Types and Solutions 2025](https://linkwellelectrics.com/electric-vehicle-charging-station-cabinets/)  
[Overview of AC/DC Converters for Fast-Charging Stations](https://www.powerelectronicsnews.com/overview-of-ac-dc-converters-for-fast-charging-stations/)  
[EV Charging Connector Types: A Complete Guide](https://www.power-sonic.com/ev-charging-connector-types/)