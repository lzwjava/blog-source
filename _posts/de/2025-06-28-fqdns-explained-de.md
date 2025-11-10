---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Grundlegendes zu vollqualifizierten Domänennamen
translated: true
type: note
---

### Was ist ein FQDN?

Ein Fully Qualified Domain Name (FQDN) ist die vollständige, absolute Adresse eines bestimmten Geräts oder Dienstes im Internet oder in einem lokalen Netzwerk. Er identifiziert einen Host (wie einen Computer oder Server) eindeutig innerhalb des Domain Name System (DNS), das menschenlesbare Namen in IP-Adressen übersetzt.

#### Wichtige Komponenten
Ein FQDN enthält alle Teile der Domain-Hierarchie, durch Punkte getrennt, in hierarchischer Reihenfolge (vom spezifischsten zum allgemeinsten):
- **Host/Hostname**: Der spezifische Name der Maschine (z.B. "www" oder "mail").
- **Subdomain**: Optionale Ebenen unterhalb der Top-Level-Domain (z.B. "google" in "www.google.com").
- **Domain-Name**: Der Hauptteil (z.B. "google").
- **Top-Level-Domain (TLD)**: Die höchste Ebene, wie ".com", ".org" oder Ländercodes wie ".uk".

Im Gegensatz zu einem relativen Domain-Namen (z.B. nur "google.com") endet ein FQDN immer mit einem Punkt (.), um anzuzeigen, dass er vollständig qualifiziert ist, obwohl der abschließende Punkt im alltäglichen Gebrauch oft weggelassen wird.

#### Warum wird er verwendet?
- **Eindeutigkeit**: Stellt sicher, dass es keine Mehrdeutigkeit gibt; er legt den exakten Standort im DNS-Baum fest.
- **DNS-Auflösung**: Hilft dabei, Datenverkehr korrekt zu routen, besonders in komplexen Setups wie Subdomains oder privaten Netzwerken.
- **Beispiele**:
  - `"www.example.com."` – Vollständig qualifiziert (beachte den abschließenden Punkt).
  - `"mail.google.com"` – Üblich ohne den Punkt in URLs.
  - In einem lokalen Netzwerk könnte es `"server.abt.firma.local."` sein, um einen Server in einer Abteilung zu spezifizieren.

Dieses Konzept ist von der Internet Engineering Task Force (IETF) in RFCs wie RFC 1035 standardisiert, die DNS definiert. FQDNs verhindern Konflikte, verbessern die Sicherheit in Konfigurationen und sind essenziell für Tools wie E-Mail-Server (z.B. SMTP) und Webbrowser. Wenn du einen spezifischen Kontext hast, wie Networking oder Webhosting, kann ich darauf näher eingehen!