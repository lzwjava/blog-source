---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Überblick über Bank- und Anlagesysteme
translated: true
type: note
---

### Typische Finanzprojekte/Systeme im Bankwesen

In der Banken- und Finanzdienstleistungsbranche beziehen sich "Finanzprojekte" oft auf Kernbankensysteme, Vermögensverwaltungsplattformen oder spezielle Software für die Abwicklung von Anlagen wie Investmentfonds. Dabei handelt es sich typischerweise um Unternehmenslösungen, die Konten, Transaktionen, Compliance und Berichterstattung verwalten. Avaloq ist ein prominentes Beispiel für eine Kernbanken- und Vermögensverwaltungsplattform. Ich werde dies Schritt für Schritt aufschlüsseln, beginnend mit Avaloq, dann anderen gängigen Alternativen und schließlich solchen mit spezieller Unterstützung für Onshore-China (Festlandchina, reguliert durch Behörden wie die CSRC) oder Offshore-Investmentfonds (z. B. Hongkong, Singapur oder QDII/QFII-Systeme für grenzüberschreitende Fonds).

#### 1. **Avaloq-Überblick**
   - **Was es ist**: Avaloq ist eine schweizerische Kernbankenplattform mit Fokus auf Privatbanking, Vermögensverwaltung und Investment-Services. Sie ist modular und verarbeitet alles vom Front-Office (Kundenonboarding) bis zum Back-Office (Abrechnung, Compliance). Sie ist in Europa, dem Mittleren Osten und Asien für ihre Flexibilität bei der Unterstützung von Multi-Währungs- und regulatorischen Anforderungen beliebt.
   - **China-Unterstützung**: Avaloq hat starke Fähigkeiten für asiatische Märkte. Es unterstützt Onshore-Investmentfonds in China durch Integrationen mit lokalen Verwahrstellen (z. B. China Securities Depository and Clearing Co.) und verarbeitet RMB-denominierte Produkte. Für Offshore-Fonds (z. B. mit Sitz in Hongkong) integriert es sich mit globalen Abrechnungssystemen wie Euroclear oder HKEX und unterstützt QDII-Systeme (Qualified Domestic Institutional Investor) für Outbound-Investments. Avaloq hat Kunden in Hongkong und Partnerschaften für die Expansion im Festlandchina.

#### 2. **Andere typische Finanzprojekte/Systeme im Bankwesen**
Neben Avaloq sind hier einige weit verbreitete Alternativen aufgeführt. Diese werden oft als "Projekte" eingesetzt, die Implementierung, Anpassung und Integration mit Altsystemen umfassen. Die Auswahl hängt von der Größe der Bank, ihrem Fokus (Privatkunden, Investment oder Firmenkundengeschäft) und der Region ab.

   - **Temenos (T24/Transact)**:
     - Kernbankensuite für das Retail-, Corporate- und Islamic Banking. Hochskalierbar und Cloud-native Optionen verfügbar.
     - Globale Reichweite: Wird von über 3.000 Instituten in 150+ Ländern genutzt.
     - Warum typisch: Verarbeitet Zahlungen, Kredite, Einlagen und Vermögensverwaltung. Wird oft für Digital-Transformation-Projekte gewählt.

   - **Finacle (von Infosys)**:
     - Umfassende Digital-Banking-Plattform für Kernoperationen, Mobile Banking und Analytik.
     - Beliebt in Schwellenmärkten, einschließlich Asien und dem Mittleren Osten.
     - Warum typisch: Stark im Retail- und SME-Banking; unterstützt API-Integrationen für Fintech-Ökosysteme.

   - **Mambu**:
     - Cloud-basierte, komponierbare Banking-Plattform (moderner und agiler als Legacy-Systeme).
     - Fokus: Kreditvergabe, Einlagen und Zahlungen; ideal für Neobanken oder rein digitale Projekte.
     - Warum typisch: Wächst in der Popularität für schnelle Implementierungen ohne umfangreiche Anpassungen.

   - **Oracle FLEXCUBE**:
     - Universal Banking System für die Kernverarbeitung, Handelsfinanzierung und Risikomanagement.
     - Wird in groß angelegten Projekten für internationale Banken eingesetzt.
     - Warum typisch: Robust für Transaktionen mit hohem Volumen und Multi-Entity-Operationen.

   - **Thought Machine (Vault)**:
     - Cloud-native Kernbankenlösung für personalisierte Produkte und Echtzeitverarbeitung.
     - Aufstrebende Wahl für innovative Banken, die von monolithischen Systemen wechseln.

Für Vermögensverwaltungs- und investmentspezifische Projekte (über Kernbankensysteme hinaus) sind folgende gängig:
   - **Charles River IMS (State Street)**: Order Management und Trading für Fonds.
   - **SimCorp Dimension**: End-to-End Investment Management für Asset Manager.
   - **HiPortfolio (OFC Systems)**: Fondsbuchhaltung und NAV-Berechnung, beliebt für Investmentfonds.

Diese Projekte umfassen typischerweise Phasen wie Bewertung, Migration, Tests und Go-Live, kosten oft Millionen und dauern 1-3 Jahre.

#### 3. **Systeme mit spezieller Unterstützung für Onshore- oder Offshore-Investmentfonds in China**
Der chinesische Investmentfondsmarkt ist riesig (über 27 Billionen RMB AUM Stand 2023), mit strengen Vorschriften der CSRC (China Securities Regulatory Commission) für Onshore-Fonds und grenzüberschreitenden Regeln (z. B. Bond Connect, Stock Connect) für Offshore-Fonds. Systeme müssen RMB-Abwicklung, T+1 Handelszyklen und Compliance mit FATCA/CRS Reporting handhaben. Hier sind die wichtigsten mit China-Fokus:

   - **Avaloq (wie erwähnt)**: Hervorragend für beides. Onshore: Unterstützt CSRC Reporting und Integration mit China Clearing. Offshore: Verarbeitet von der Hongkonger SFC regulierte Fonds und RQFII-Kontingente (Renminbi Qualified Foreign Institutional Investor).

   - **Temenos**:
     - Starke China-Präsenz (Kunden wie Bank of China Filialen). Unterstützt Onshore-Investmentfonds über lokale API-Gateways und Verwahrstellen wie die Bank of Communications. Offshore: Integriert mit Hongkongs CCASS für die Investmentfonds-Verteilung.
     - Warum geeignet: Benutzerdefinierte Module für asiatische Vermögensverwaltung, einschließlich e-KYC für chinesische Kunden.

   - **Finastra (früher Misys)**:
     - Deren Fusion Invest Plattform unterstützt die Verarbeitung von Investmentfonds. In China handhabt sie Onshore-Fondssubscriptionen/-redemptionen und Offshore-QDII-Fonds (ermöglicht Investoren vom Festland den Kauf ausländischer Assets).
     - Wird von Banken in Hongkong und Singapur für China-bezogene Produkte genutzt.

   - **Calypso (jetzt Adenza/ION)**:
     - Trading- und Post-Trade-System für Derivate und Fonds. Unterstützt China Onshore über Konnektivität zu SHSE/SZSE Börsen. Offshore: Ideal für Hongkong-basierte Investmentfonds mit China-Exposure (z. B. A-Aktien-Zugang).
     - Warum geeignet: Echtzeit-Risikomanagement für volatile China-Märkte.

   - **SS&C Advent (einschließlich Geneva und AXYS)**:
     - Portfoliomanagement und -buchhaltung für Investmentfonds. Stark bei Offshore-China-Fonds (z. B. Hongkong UCITS-konforme Produkte, die Onshore-Fonds spiegeln). Onshore-Unterstützung durch Partnerschaften mit lokalen Firmen wie ChinaAMC.
     - Beliebt für Asset Manager, die China-fokussierte ETFs/Investmentfonds global vertreiben.

   - **China-spezifische oder lokalisierte Lösungen**:
     - **Kingdee oder UseTrust (Chinesische Anbieter)**: Für Onshore-Investmentfonds handhaben diese die CSRC-Compliance, Fondsregistrierung und NAV-Abstimmung. Oft in inländischen Projekten neben globalen Systemen eingesetzt.
     - **Bloomberg AIM oder Terminal-Integrationen**: Kein vollständiges Kernsystem, aber weit verbreitet in Projekten für Echtzeit-China-Fondsdaten, Onshore/Offshore-Preisgestaltung und regulatorische Einreichungen.
     - **HSBC oder Standard Chartered's interne Plattformen**: Banken mit starker China-Exposure (z. B. HSBC's Hexagon) unterstützen Investmentfonds über ihre globalen Systeme, mit benutzerdefinierten China-Modulen.

#### Wichtige Überlegungen für China-fokussierte Projekte
- **Regulatorische Hürden**: Onshore erfordert Datenlokalisierung (unter PIPL) und Genehmigung von SAFE (State Administration of Foreign Exchange). Offshore (z. B. Hongkong) ist flexibler, benötigt aber SFC-Lizenzen.
- **Integrationsbedarf**: Systeme müssen eine Verbindung zu CFETS (China Foreign Exchange Trade System) für RMB oder zur HKMA für Offshore herstellen können.
- **Trends**: Mit der Öffnung Chinas (z. B. Mutual Recognition of Funds System zwischen HK und dem Festland) betonen Projekte zunehmend grenzüberschreitende Fähigkeiten. Cloud-Implementierungen (z. B. Alibaba Cloud für Onshore) nehmen zu.
- **Herausforderungen**: Hoher Anpassungsbedarf für chinesische Zeichen, Feiertage und Abwicklungsregeln; Datensicherheit ist von größter Bedeutung.

Wenn Sie für ein bestimmtes Projekt bewerten (z. B. Implementierung in einer Bank), empfehle ich, die Anbieter-Fallstudien oder Beratungsfirmen wie Deloitte/Accenture für RFPs zu prüfen. Für weitere Details zu einem dieser Punkte, lassen Sie mich Ihren Fokusbereich wissen!