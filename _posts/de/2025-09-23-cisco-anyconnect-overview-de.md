---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Cisco AnyConnect Netzwerkzugriffsmanager Übersicht
translated: true
type: note
---

Cisco AnyConnect Secure Mobility Client ist eine Suite von Softwaremodulen, die sicheren VPN-Zugang, Netzwerksicherheit und richtlinienbasierte Endpunkt-Features bieten. Eines der optionalen Module in dieser Suite ist **Cisco Network Access Manager (NAM).**

### Funktionen von Cisco AnyConnect NAM
- **Verwaltung von Netzwerkverbindungen**: NAM ersetzt die nativen Windows-Manager für drahtlose und kabelgebundene Netzwerke. Es konfiguriert, verbindet und sichert sowohl kabelgebundene als auch drahtlose Netzwerke.
- **Erweiterte 802.1X-Unterstützung**: Bietet umfassende **802.1X-Authentifizierung** für kabelgebundene und drahtlose Netzwerkverbindungen (EAP-TLS, PEAP, EAP-FAST, etc.), die häufig in Unternehmensumgebungen eingesetzt wird, wo zertifikatbasierte Authentifizierung oder Endpunkt-Statusüberprüfung erforderlich ist.
- **Richtlinienumsetzung**: Administratoren können Richtlinien definieren, die festlegen, wie Endgeräte eine Verbindung zu Netzwerken herstellen – mit Priorisierung von Sicherheitsanforderungen, Definition erlaubter SSIDs oder Einschränkung unsicherer Verbindungen.
- **Konsistentes Verhalten über Plattformen hinweg**: Es bietet zentrale Kontrolle, sodass Benutzer unabhängig vom verwendeten PC die gleiche Netzwerkzugriffserfahrung erhalten.

### Wichtige Hinweise
- **Plattformunterstützung**: Historisch wurde NAM nur unter Windows unterstützt. Cisco hat die NAM-Unterstützung beginnend mit späteren AnyConnect-Versionen (ab v4.9) eingestellt, da die nativen Betriebssystem-Netzwerkmanager (Windows Native Wi-Fi, macOS Supplicant, etc.) robuster wurden.
- **Typische Verwendung**: Wird primär in Unternehmen, Universitäten oder Regierungsnetzwerken eingesetzt, die eine sichere, zertifikatbasierte Anmeldung am WLAN oder kabelgebundenen LAN vor oder während der Systemanmeldung erfordern.

👉 Kurz gesagt: **Cisco AnyConnect NAM (Network Access Manager)** ist ein erweiterter Netzwerkverbindungs-Manager, der den nativen Windows-Supplicant ersetzt, um sichere kabelgebundene/drahtlose Verbindungen mittels 802.1X-Authentifizierung und unternehmensdefinierten Richtlinien zu handhaben.

---

Möchten Sie, dass ich auch erkläre, **wie NAM im Vergleich zum häufiger verwendeten AnyConnect VPN-Modul** einzuordnen ist (da die meisten Leute heute nur den VPN-Teil kennen)?