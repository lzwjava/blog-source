---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: 'Telegraf: Open-Source-Metriken-Sammelagent'
translated: true
---

Telegraf ist ein quelloffener, plugin-gesteuerter Agent, der von InfluxData entwickelt wurde, um Metriken, Logs und andere Telemetriedaten aus verschiedenen Quellen zu sammeln, zu verarbeiten, zu aggregieren und zu schreiben. Er ist leichtgewichtig, läuft als einzelne Binärdatei und unterstützt über 300 Input-Plugins (z.B. für Systemstatistiken, Datenbanken wie MySQL/PostgreSQL, Cloud-Dienste wie AWS und Anwendungen wie Apache Kafka) und mehr als 50 Output-Plugins (z.B. nach InfluxDB, Prometheus, Kafka oder Elasticsearch).

### Wichtige Funktionen
- **Agent-basierte Architektur**: Einfache Bereitstellung auf Servern, Containern oder IoT-Geräten ohne schwerwiegende Abhängigkeiten.
- **Erweiterbar durch Plugins**: Geschrieben in Go, ermöglicht bei Bedarf die Erstellung benutzerdefinierter Plugins.
- **Teil des TICK-Stacks**: Nahtlose Integration mit InfluxDB für die Speicherung von Zeitreihendaten, Chronograf für die Visualisierung und Kapacitor für Warnmeldungen.
- **Anwendungsfälle**: Häufig im DevOps-Bereich für die Infrastrukturüberwachung, Anwendungsleistungsverfolgung und die Erfassung von IoT-Sensordaten.

Es ist kostenlos unter der MIT-Lizenz und wird aktiv gepflegt, wobei das letzte stabile Release Ende 2025 v1.29.x ist. Für die Einrichtung siehe die offizielle Dokumentation unter [telegraf.influxdata.com](https://docs.influxdata.com/telegraf/). Falls dies nicht das von Ihnen gemeinte Telegraf ist (z.B. eine Marke oder ein Begriff in einem anderen Kontext), geben Sie bitte weitere Details an!