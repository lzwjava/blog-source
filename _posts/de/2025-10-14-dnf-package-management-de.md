---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: DNF-Paketverwaltung in RHEL
translated: true
type: note
---

### Einführung in DNF in Red Hat Enterprise Linux

DNF (Dandified YUM) ist das primäre Paketverwaltungstool in Red Hat Enterprise Linux (RHEL), beginnend mit RHEL 8 und fortgesetzt in RHEL 9. Es dient als Nachfolger des älteren YUM (Yellowdog Updater, Modified) Tools und bietet verbesserte Leistung, eine bessere Abhängigkeitsauflösung und Unterstützung für modulare Inhalte. In RHEL verwaltet DNF die Installation, Aktualisierung und Entfernung von Softwarepaketen, die über RPM (Red Hat Package Manager) Repositories verteilt werden. Es gewährleistet den Zugang zu essenziellen Inhaltsgruppen wie BaseOS (für Kern-OS-Funktionalität) und AppStream (für User-Space-Anwendungen, Laufzeitumgebungen und Tools), die alle über Ihr RHEL-Abonnement verwaltet werden.

Der Zweck von DNF ist es, die Verwaltung des Software-Lebenszyklus zu vereinfachen und gleichzeitig die Systemstabilität aufrechtzuerhalten. Es ermöglicht Administratoren und Benutzern, mit traditionellen RPM-Paketen neben modernen modularen Formaten zu arbeiten, bei denen Komponenten wie Sprachen oder Datenbanken mehrere parallele Versionen (genannt "Streams") haben können, ohne das Basis-Betriebssystem zu beeinträchtigen.

#### Wichtige Funktionen
- **Unterstützung für modulare Inhalte**: Verwaltet Module (Gruppen verwandter RPMs), Streams (versionsspezifische Repositories) und Profile (vorkonfigurierte Paketsätze für spezifische Anwendungsfälle, z.B. Webserver oder Entwicklungsumgebung).
- **Repository-Verwaltung**: Ermöglicht das Suchen, Aktivieren/Deaktivieren von Repos und das Konfigurieren von Quellen wie BaseOS, AppStream und ergänzenden Repositories.
- **Installation und Updates**: Löst Abhängigkeiten automatisch auf beim Installieren von Paketen, Gruppen oder ganzen Modulen; unterstützt die Überprüfung auf Updates, das Upgraden bestimmter Pakete oder des gesamten Systems.
- **Entfernung und Rollback**: Entfernt Software sicher und bietet Transaktionsverlauf zum Rückgängigmachen von Änderungen.
- **Anpassung und Automatisierung**: Konfigurierbar über `/etc/dnf/dnf.conf` für Ausschlüsse, Plugins oder Caching; integriert sich mit Tools wie DNF Automatic für geplante Updates.
- **Abwärtskompatibilität**: Der Befehl `yum` ist in RHEL ein Alias für `dnf`, was den Übergang von älteren Versionen erleichtert.

Für den Einstieg gehören zu den grundlegenden Befehlen `dnf install <Paket>` für die Installation, `dnf update` für Upgrades und `dnf search <Begriff>` für die Softwaresuche. Für fortgeschrittene Verwendungszwecke konsultieren Sie bitte die offizielle Dokumentation.

[Red Hat Enterprise Linux 9: Managing Software with the DNF Tool](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/managing_software_with_the_dnf_tool/index)