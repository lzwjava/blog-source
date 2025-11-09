---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Richtlinien zur Integration des Faster Payment Systems
translated: true
type: note
---

Das Faster Payment System (FPS) in Hongkong, betrieben von der Hong Kong Interbank Clearing Limited (HKICL) unter der Aufsicht der Hong Kong Monetary Authority (HKMA), bietet keine öffentlich zugängliche SDK für Banken zur Integration. Die Integration erfolgt durch direkte Anbindung an die FPS-Infrastruktur, wobei die technischen Spezifikationen im Onboarding-Prozess privat mit den teilnehmenden Banken (bekannt als Settlement Participants) geteilt werden. Diese Spezifikationen leiten Banken bei der Anpassung ihrer Systeme für den Zugang an, aber in der offiziellen Dokumentation werden keine fertigen SDKs oder Developer Kits erwähnt.

Was APIs betrifft, bietet FPS selbst derzeit keine dedizierten APIs für externe oder Drittanbieter-Integrationen. Es orientiert sich jedoch am breiteren Open API Framework der HKMA für den Hongkonger Bankensektor (eingeführt 2018 und in Phasen bis 2025 aktualisiert), das Banken dazu ermutigt, bestimmte Funktionen über APIs für Drittanbieter verfügbar zu machen (z.B. für Kontoinformationen oder Zahlungsinitiierung). FPS-Transaktionen können dieses Framework indirekt für Funktionen wie Zahlungsinitiierung nutzen, aber es sind noch keine FPS-spezifischen APIs verfügbar – der Zugang bleibt aus Sicherheits- und regulatorischen Gründen auf Basis von "Need-to-know" beschränkt. Die HKMA beobachtet die Entwicklung weiter und könnte die API-Unterstützung in Zukunft ausbauen.

### Wichtige Integrationsdetails für Banken
- **Anbindungsmethoden**: Banken verbinden sich im Echtzeit-Modus über IBM MQ Messaging zur sofortigen Verarbeitung oder im Stapel-Modus über Dateiübertragungen (z.B. über das sichere ICLNET-Netzwerk der HKICL). Das System läuft 24/7.
- **Messaging-Standards**: Alle Kommunikationen verwenden das ISO 20022-Format, das umfangreiche Daten, chinesische Zeichen und Interoperabilität unterstützt.
- **Onboarding-Prozess**: Banken melden sich bei der HKMA (für HKD) oder der Bank of China (Hong Kong) für RMB an, unterzeichnen FPS-Regelvereinbarungen, passen ihre Systeme an die bereitgestellten Spezifikationen an, durchlaufen Tests der HKICL und gehen live. Alle lizenzierten Banken müssen als direkte Settlementteilnehmer teilnehmen.
- **Weitere Funktionen**: Unterstützt Proxy-IDs (z.B. Telefon/E-Mail), QR-Codes (EMV-Standard) und Multi-Währungs-Transfers (HKD/RMB). Die Authentifizierung folgt den Zwei-Faktor-Richtlinien der HKMA, wobei die Banken ihre eigenen Transaktionslimits festlegen.

Für detaillierte technische Spezifikationen müssen sich Banken nach der Anmeldung direkt an die HKICL wenden, da diese nicht öffentlich herunterladbar sind.

[Faster Payment System (FPS) - HKMA](https://www.hkma.gov.hk/eng/key-functions/international-financial-centre/financial-market-infrastructure/faster-payment-system-fps/)  
[Scheme Documentation - HKICL FPS](https://fps.hkicl.com.hk/eng/fps/about_fps/scheme_documentation.php)  
[World Bank FPS Case Study: Hong Kong](https://fastpayments.worldbank.org/sites/default/files/2021-09/World_Bank_FPS_Hong_Kong_SAR_China_FPS_Case_Study.pdf)  
[Open API Framework for the Banking Sector - HKMA](https://www.hkma.gov.hk/eng/key-functions/international-financial-centre/fintech/open-application-programming-interface-api-for-the-banking-sector/)