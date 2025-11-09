---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: HashiCorp Vault Überblick
translated: true
type: note
---

### Was ist HashiCorp Vault?

HashiCorp Vault ist ein Open-Source-Tool, das für die sichere Verwaltung, Speicherung und den Zugriff auf sensible Daten entwickelt wurde, oft auch als „Secrets“ bezeichnet. Dazu gehören API-Schlüssel, Passwörter, Zertifikate, Token und Verschlüsselungsschlüssel. Es fungiert als zentrales System für identitätsbasierte Secrets-Management, Verschlüsselung als Dienst und privilegierte Zugriffskontrolle und hilft Organisationen, sensible Informationen in dynamischen, Multi-Cloud- oder Hybrid-Umgebungen zu schützen.

#### Wichtige Funktionen
- **Secrets Management**: Vault verwaltet sowohl statische Secrets (wie langlebige Passwörter) als auch dynamische Secrets (kurzlebige, bedarfsgerecht generierte Anmeldeinformationen, z. B. Datenbank-Benutzer, die automatisch ablaufen).
- **Verschlüsselung und Auditierung**: Alle Daten werden im Ruhezustand und während der Übertragung verschlüsselt, mit umfassender Protokollierung und Auditierung zur Nachverfolgung von Zugriffen und Änderungen.
- **Identitätsbasierter Zugriff**: Es integriert sich mit Identitätsanbietern (z. B. LDAP, OIDC), um Benutzer und Systeme zu authentifizieren und erzwingt feingranulare Richtlinien dafür, wer auf was zugreifen darf.
- **Dynamische Anmeldeinformationen und Leasing**: Secrets werden für eine begrenzte Zeit geleast, was das Risiko einer langfristigen Exposition verringert.
- **Cloud-Agnostisch und Self-Hosted**: Funktioniert in jeder Infrastruktur, mit Optionen für On-Premises-Bereitstellung oder Managed Services.

#### Wie es funktioniert
Vault operiert als Client-Server-Anwendung. Clients (Anwendungen oder Benutzer) authentifizieren sich beim Vault-Server, der Anfragen dann basierend auf Richtlinien autorisiert. Nach der Genehmigung kann Vault gespeicherte Secrets abrufen, neue generieren oder den Zugriff widerrufen. Beispielsweise könnte eine App temporäre Datenbank-Anmeldeinformationen anfordern, diese nutzen und sie automatisch ablaufen lassen. Die Architektur umfasst ein Storage-Backend (z. B. Consul, PostgreSQL) für Persistenz und unterstützt Hochverfügbarkeit durch Clustering.

Es wird häufig in DevOps-, Sicherheits- und Compliance-Szenarien eingesetzt, um die manuelle Handhabung von Secrets zu ersetzen und so die Risiken von Sicherheitsverletzungen in Umgebungen mit geringem Vertrauen zu verringern.

#### Referenzen
- [What is Vault? | Vault - HashiCorp Developer](https://developer.hashicorp.com/vault/docs/about-vault/what-is-vault)
- [HashiCorp Vault | Identity-based secrets management](https://www.hashicorp.com/en/products/vault)
- [hashicorp/vault: A tool for secrets management, encryption ... - GitHub](https://github.com/hashicorp/vault)
- [What Is HashiCorp Vault & How Does Vault Work? - KodeKloud](https://kodekloud.com/blog/what-is-hashicorp-vault/)