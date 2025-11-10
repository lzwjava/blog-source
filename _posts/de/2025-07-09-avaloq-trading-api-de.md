---
audio: false
generated: true
lang: de
layout: post
title: Erkundung der Avaloq-Handels-API-Details
translated: true
type: note
---

Basierend auf meinen Suchergebnissen kann ich Ihnen Informationen zur Implementierung von Aktienhandelsaufträgen in Avaloq geben, auch wenn spezifische technische Dokumentationen in öffentlichen Quellen begrenzt zu sein scheinen. Hier ist was ich gefunden habe:

## Avaloq Trading-Implementierung

### Handelsplattform-Überblick
Avaloq ermöglicht es Ihren Kunden, jedes Produkt, von börsengehandelt bis Over-the-Counter und Krypto, auf einer End-to-End-Plattform zu handeln. Die Plattform bietet umfassende Handelsfunktionen, die in das Kernbanksystem integriert sind.

### Pre-Trade-Compliance-Prüfungen
Die Software prüft Personen, Transaktionen und Wertpapierorders anhand vordefinierter Compliance-Regeln. Basierend auf diesen Regelsätzen entscheidet die ACTICO Compliance-Software automatisch, ob ein Compliance-Risiko besteht. Diese Integration zeigt, dass Avaloq Pre-Trade-Compliance durch Partnerschaften mit spezialisierten Compliance-Lösungen unterstützt.

Das Pre-Trade-Check-System validiert typischerweise:
- Client-Autorisierung und Berechtigungen
- Risikolimits und Exposure-Checks
- Regulatorische Compliance-Anforderungen
- Verfügbare Mittel und Kreditlimiten
- Marktzeit und Handelsbeschränkungen

### API-Integration
Das Account Management API-Modul umfasst verschiedene API-Endpunkte, die Konnektivität für Drittsysteme bieten, um einen einfachen Zugang zu spezifischen Funktionen zu ermöglichen. Avaloq stellt API-Zugang über seine avaloq.one-Plattform bereit, und es gibt ein GitHub-Repository mit Ressourcen für den Einstieg in Avaloqs Open APIs.

## Implementierungsansatz

### 1. Aktienorderplatzierung
Während spezifische XML-SOAP-Dokumentation in den Suchergebnissen nicht gefunden wurde, würde eine typische Implementierung beinhalten:

**Orderstruktur:**
- Order-ID und Client-Identifikation
- Wertpapieridentifikation (ISIN, Ticker, etc.)
- Ordertyp (Market, Limit, Stop, etc.)
- Mengen- und Preisparameter
- Time-in-Force-Spezifikationen
- Abwicklungsanweisungen

### 2. Pre-Trade-Check-Prozess
Die Pre-Trade-Validierung würde typischerweise diesem Ablauf folgen:
- Übermittlung der Orderdetails an die Compliance-Engine
- Validierung gegen Client-Profil und Limits
- Prüfung regulatorischer Anforderungen
- Verifizierung verfügbarer Mittel/Wertpapiere
- Rückgabe von Genehmigung/Ablehnung mit Gründen

### 3. XML-SOAP-API-Aufruf
Basierend auf Standardpraktiken der Finanzbranche und den verfügbaren Informationen würde die XML-SOAP-Integration wahrscheinlich beinhalten:

**Authentifizierung:**
- API-Zugangsdaten und Sicherheitstokens
- Client-Identifikation und Autorisierung

**Nachrichtenformat:**
- Standard-XML-Envelope-Struktur
- Avaloq-spezifische Schemas für Handelsoperationen
- Fehlerbehandlung und Antwortcodes

## Empfehlungen für die Implementierung

1. **Dokumentationszugriff**: Wenden Sie sich direkt an Avaloq oder über deren Partnernetzwerk, um auf detaillierte API-Dokumentation zuzugreifen, da diese anscheinend auf lizenzierte Kunden beschränkt ist.

2. **Sandbox-Umgebung**: Avaloq hat eine gute Grundlage geschaffen, um Unternehmen dabei zu unterstützen, den Test- und Integrationsprozess neuer Lösungen zu erleichtern, indem die Komplexitäten über verschiedene Phasen hinweg mit Avaloqs Sandbox-Lösung auf AWS-Basis verwaltet werden.

3. **Partnerintegration**: Ziehen Sie die Zusammenarbeit mit Avaloq-zertifizierten Implementierungspartnern in Betracht, die Erfahrung mit deren Handels-APIs haben und spezifische Anleitung zu XML-SOAP-Integrationsmustern bieten können.

4. **Compliance-Integration**: Die Avaloq Banking Suite arbeitet zuverlässig mit der ACTICO Compliance-Software über eine Standard-Schnittstelle, was auf etablierte Muster für die Compliance-Integration hindeutet.

Für detaillierte technische Spezifikationen, API-Schemas und Implementierungsbeispiele müssten Sie auf die offizielle Entwicklerdokumentation von Avaloq über deren Client-Portal zugreifen oder sich direkt an deren technischen Support wenden.