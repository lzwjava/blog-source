---
audio: false
generated: true
lang: de
layout: post
title: Avaloq API Fehlerbehebungsleitfaden
translated: true
type: note
---

## Umfassender Leitfaden zu Avaloq API-Fehlern

### Häufige System-Level-Fehler

**1. Avaloq Agent-Ausführungsfehler**
Fehler auf dem Avaloq-System oder auf Oracle bei der Ausführung des Codes des Avaloq Agent. Diese Fehler können auftreten, wenn der Job, der auf dem Avaloq-System ausgeführt wird, mit Fehlern endet.

**Fehlerbehebung:**
- Oracle-Datenbankverbindung prüfen
- Avaloq Agent-Konfiguration überprüfen
- Systemprotokolle auf datenbankbezogene Probleme überprüfen
- Sicherstellen, dass der ausführende Benutzer über die richtigen Berechtigungen verfügt

**2. Job-Abbruchfehler**
Die folgende Zeile im Protokoll bedeutet, dass der Job aufgrund eines internen Fehlers auf dem Avaloq-System abgebrochen wurde. Der Endstatus des Jobs ist für den Avaloq Agent gültig: YYYY-MM-DD hh:mm:ss Job 642 Execute: Job did complete with failures.

**Fehlerbehebung:**
- Job-Protokolle auf spezifische Fehlerursachen überprüfen
- Systemressourcenverfügbarkeit prüfen
- Job-Parameter und Abhängigkeiten überprüfen
- Systemleistung während der Ausführung überwachen

### Standard-HTTP-API-Fehler im Bankenkontext

**1. 400 Bad Request**
Häufige Ursachen in Avaloq-Umgebungen:
- Ungültige Kontonummern oder Client-IDs
- Fehlerhafte Transaktionsbeträge
- Fehlende Pflichtfelder in Handelsaufträgen
- Ungültige Datumsformate oder -bereiche

**Fehlerbehebung:**
- URL prüfen, um sicherzustellen, dass gültige Datenparameter mit den Anfragen gesendet werden und die korrekten Header verwendet werden
- Alle Eingabeparameter gegen Avaloqs Schema-Anforderungen validieren
- Währungscodes und Formatierung prüfen
- Kontostatus und Berechtigungen überprüfen

**2. 401 Unauthorized**
Bankenspezifische Ursachen:
- Ungültige API-Anmeldedaten
- Abgelaufene Authentifizierungstokens
- Unzureichende Benutzerberechtigungen für bestimmte Operationen
- Client-Beziehungsbeschränkungen

**Fehlerbehebung:**
- Gültigkeit von API-Schlüssel und Secret überprüfen
- Token-Ablaufzeiten prüfen
- Bestätigen, dass der Benutzer über angemessene Bankberechtigungen verfügt
- Client-Berater-Zuordnungen überprüfen

**3. 403 Forbidden**
Vermögensverwaltungskontext:
- Zugriff auf bestimmte Client-Konten verweigert
- Regulatorische Beschränkungen für Operationen
- Compliance-Regelverstöße
- Jurisdiktionsbasierte Einschränkungen

**Fehlerbehebung:**
- Benutzerzugriffsrechte und Rollen überprüfen
- Compliance-Regeln und Beschränkungen prüfen
- Regulatorische Berechtigungen überprüfen
- Grenzüberschreitende Transaktionserlaubnisse bestätigen

**4. 404 Not Found**
Bankenspezifische Szenarien:
- Nicht existierende Kontonummern
- Ungültige Portfolio-IDs
- Fehlende Transaktionsreferenzen
- Gelöschte oder archivierte Client-Datensätze

**Fehlerbehebung:**
- Endpunkt überprüfen und sicherstellen, dass er korrekt geschrieben ist
- Kontexistenz und Status überprüfen
- Auf archivierte oder inaktive Konten prüfen
- Korrekte URL-Konstruktion bestätigen

**5. 500 Internal Server Error**
System-Level-Probleme:
- Datenbankverbindungsprobleme
- Core Banking-Systemausfälle
- Integrationsdienst-Ausfälle
- Speicher- oder Leistungsprobleme

**Fehlerbehebung:**
- System-Health-Dashboards prüfen
- Datenbankverbindungspools überprüfen
- Systemressourcennutzung überwachen
- Verfügbarkeit abhängiger Dienste überprüfen

### Avaloq-spezifische Fehlerkategorien

**1. Business Unit-Fehler**
RA Avaloq Jobs, die sich auf eine Business Unit beziehen, die nicht auf dem Avaloq-System existiert, können ausgeführt werden

**Häufige Probleme:**
- Ungültige Business Unit-Referenzen
- Inaktive oder gelöschte Business Units
- Falsche Organisationshierarchie-Zuordnung

**2. Integrationsfehler**
Basierend auf Avaloqs Integrationsfähigkeiten:
- API-Versionskonflikte
- Schema-Validierungsfehler
- Nachrichtenformat-Inkompatibilitäten
- Timeout-Probleme mit externen Systemen

**3. Compliance und regulatorische Fehler**
- Pre-Trade-Prüfungsfehler
- AML/KYC-Validierungsfehler
- Probleme mit regulatorischen Meldungen
- Grenzüberschreitende Transaktionsbeschränkungen

### Best Practices für Fehlerbehandlung

**1. Protokollierung und Überwachung**
- Umfassende Protokollierung für alle API-Aufrufe implementieren
- Alarme für kritische Fehlermuster einrichten
- API-Antwortzeiten und Erfolgsquoten überwachen
- Geschäftsspezifische Fehlermuster verfolgen

**2. Fehlerantwort-Struktur**
Typische Avaloq-Fehlerantworten sollten enthalten:
- Fehlercode und Kategorie
- Menschenlesbare Fehlermeldung
- Zeitstempel und Request-ID
- Vorgeschlagene Lösungsschritte

**3. Wiederholungslogik**
- Exponentielles Backoff für vorübergehende Fehler implementieren
- Wiederholungen bei Authentifizierungsfehlern vermeiden
- Maximale Wiederholungslimits setzen
- Circuit Breaker-Muster für Systemfehler verwenden

**4. Testing und Validierung**
Avaloq hat eine gute Grundlage geschaffen, um Unternehmen dabei zu helfen, die Reise des Testens und Integrierens neuer Lösungen zu erleichtern, indem die Komplexitäten über verschiedene Phasen hinweg mithilfe der Avaloq Sandbox-Lösung auf AWS-Basis verwaltet werden.

**Empfohlener Testansatz:**
- Avaloq Sandbox-Umgebung für Tests verwenden
- Fehlerszenarien systematisch testen
- Fehlerbehandlung über verschiedene Benutzerrollen hinweg validieren
- Integrationspunkte mit externen Systemen testen

### Fehlervermeidungsstrategien

**1. Eingabevalidierung**
- Alle Eingabeparameter vor API-Aufrufen validieren
- Richtige Datentypen und Formate verwenden
- Client-seitige Validierung wo möglich implementieren
- Geschäftsregeln vor der Übermittlung prüfen

**2. Verbindungsmanagement**
- Richtiges Connection Pooling implementieren
- Timeouts angemessen behandeln
- Health Checks für abhängige Dienste verwenden
- API-Ratenlimits überwachen

**3. Sicherheitsüberlegungen**
- Richtige Authentifizierungsbehandlung implementieren
- Sichere Kommunikationskanäle verwenden
- Sicherheitsrelevante Fehler angemessen protokollieren
- Sensible Daten in Fehlermeldungen sorgfältig behandeln

Für spezifische Fehlercodes und detaillierte Fehlerbehebungsverfahren konsultieren Sie bitte Ihre Avaloq-Systemdokumentation oder wenden Sie sich direkt an den Avaloq-Support, da viele Fehlerdetails spezifisch für Ihre Implementierung und Konfiguration sind.