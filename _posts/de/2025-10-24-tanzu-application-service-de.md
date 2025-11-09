---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: VMware Tanzu Application Service Überblick
translated: true
type: note
---

## Einführung in VMware Tanzu Application Service for VMs (TAS for VMs)

VMware Tanzu Application Service for VMs (TAS for VMs) ist eine kommerzielle Platform-as-a-Service (PaaS), die auf dem Open-Source-Projekt Cloud Foundry basiert. Sie wurde entwickelt, um die Bereitstellung, Skalierung und Verwaltung von Cloud-native Anwendungen zu vereinfachen, sodass sich Entwickler auf das Schreiben von Code konzentrieren können, anstatt sich mit der Infrastruktur zu befassen. TAS for VMs ermöglicht die schnelle Bereitstellung von Apps in verschiedenen Umgebungen, einschließlich On-Premises (wie vSphere) oder Public Clouds (AWS, Azure, GCP, OpenStack), und unterstützt sowohl selbst verwaltete Setups als auch zertifizierte kommerzielle Anbieter.

### Wichtige Funktionen
- **Open-Source-Grundlage**: Nutzt die Erweiterbarkeit von Cloud Foundry, um Vendor Lock-in zu vermeiden, und unterstützt mehrere Sprachen, Frameworks und Dienste.
- **Automatisierte Bereitstellung**: Pushen von Apps mit vertrauten Tools (z. B. CLI) ohne Codeänderungen; Apps werden in "Droplets" (vorcompilierte Bundles) verpackt, um sie schnell zu stagen und auszuführen.
- **Skalierbarkeit und Resilienz**: Verwendet Diego für intelligente Lastverteilung über VMs hinweg, automatische Skalierung und Fehlertoleranz, um Traffic-Spitzen oder Ausfälle zu bewältigen.
- **Benutzerverwaltung**: Organisiert Teams in "Organizations" und "Spaces" mit rollenbasiertem Zugriff (z. B. Admin, Developer) über UAA (User Account and Authentication) Server.
- **Service-Integration**: Einfaches Binden von Apps an Dienste wie Datenbanken oder APIs über Service Brokers, ohne den Anwendungscode zu ändern.
- **Monitoring und Logging**: Aggregiert Logs und Metriken via Loggregator in einen "Firehose"-Stream für Echtzeitanalyse, Alerting und Integration mit Tools.
- **Kleine Footprint-Option**: Eine leichtgewichtige Version, die mit nur 4 VMs läuft (vs. 13+ für Standard), ideal für kleinere Teams oder Tests, allerdings mit einigen Skalierungsbeschränkungen.
- **Flexible Infrastruktur**: Wird via BOSH (ein Automatisierungstool) bereitgestellt und mit Tanzu Operations Manager für eine optimierte Konfiguration verwaltet.

### Vorteile
TAS for VMs beschleunigt die Time-to-Market, indem es Apps ermöglicht, innerhalb von Minuten live zu gehen, mit automatischer Skalierung und globaler Verfügbarkeit. Es reduziert den Infrastrukturaufwand, erhöht die Sicherheit durch kompartimentierte Workspaces und fördert die Portabilität – Apps laufen konsistent in allen Umgebungen. Durch die Abstraktion des VM-Managements werden Kosten und Komplexität gesenkt, während die Cloud-Foundry-Community fortlaufende Innovation und Support sicherstellt.

### So funktioniert es
Im Kern agiert TAS for VMs als eine Multi-Tenant-PaaS:
1.  **Bereitstellung**: Verwenden Sie Tanzu Operations Manager, um die Plattform auf BOSH-verwalteten VMs zu konfigurieren und bereitzustellen.
2.  **App-Lebenszyklus**: Entwickler pushen Code via CLI; der Cloud Controller staged ihn mit Buildpacks (für sprachspezifisches Setup) in Droplets, dann ersteigert und startet Diego Instanzen auf den Host-VMs.
3.  **Routing und Zugriff**: Gorouter verwaltet eingehenden Traffic, extern load-balanced; UAA authentifiziert Benutzer.
4.  **Betrieb**: Interne Komponenten kommunizieren via NATS Messaging und BOSH DNS; Ressourcen wie Blobs und Konfigurationen werden in GitHub, Blobstores oder MySQL gespeichert.

TAS for VMs erweitert das Open-Source Cloud Foundry mit VMwares Enterprise-Features, Support und Zertifizierungen und macht es so zu einer robusten Wahl für Production-Workloads.

Weitere Details finden Sie in der offiziellen Dokumentation: [TAS for VMs Overview](https://techdocs.broadcom.com/us/en/vmware-tanzu/platform/tanzu-platform-for-cloud-foundry/6-0/tpcf/concepts-overview.html)