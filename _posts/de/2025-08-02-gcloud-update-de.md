---
audio: false
generated: true
image: false
lang: de
layout: post
title: Google Cloud CLI Update
translated: true
type: note
---

% gcloud components update
Aktualisierung wird gestartet. Dieser Vorgang kann einige Minuten dauern.


Ihre aktuelle Google Cloud CLI Version ist: 507.0.0
Sie werden auf Version aktualisiert: 532.0.0

┌─────────────────────────────────────────────────────────────────────────────┐
│                      Diese Komponenten werden aktualisiert.                 │
├─────────────────────────────────────────────────────┬────────────┬──────────┤
│                         Name                        │  Version   │   Größe  │
├─────────────────────────────────────────────────────┼────────────┼──────────┤
│ BigQuery Command Line Tool                          │     2.1.21 │  1.8 MiB │
│ BigQuery Command Line Tool (Platform Specific)      │     2.1.17 │  < 1 MiB │
│ Cloud Storage Command Line Tool                     │       5.35 │ 12.4 MiB │
│ Cloud Storage Command Line Tool (Platform Specific) │       5.34 │  < 1 MiB │
│ Google Cloud CLI Core Libraries                     │ 2025.07.25 │ 22.1 MiB │
│ Google Cloud CLI Core Libraries (Platform Specific) │ 2025.05.23 │  < 1 MiB │
│ Google Cloud CRC32C Hash Tool (Platform Specific)   │      1.0.0 │  1.4 MiB │
│ gcloud cli dependencies                             │ 2025.04.18 │ 16.1 MiB │
└─────────────────────────────────────────────────────┴────────────┴──────────┘

Seit Ihrer letzten Aktualisierung hat sich viel geändert. Die neuesten vollständigen Release Notes finden Sie unter:
  https://cloud.google.com/sdk/release_notes

Wenn Sie diesen Vorgang abbrechen, nachdem er gestartet wurde, könnte Ihre SDK-Installation in einem inkonsistenten Zustand verbleiben.

Möchten Sie fortfahren (J/n)?  J

Durchführung der direkten Aktualisierung...

╔════════════════════════════════════════════════════════════╗
╠═ Herunterladen: BigQuery Command Line Tool               ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Herunterladen: BigQuery Command Line Tool (Platform Spe... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Herunterladen: Cloud Storage Command Line Tool          ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Herunterladen: Cloud Storage Command Line Tool (Platfor... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Herunterladen: Google Cloud CLI Core Libraries          ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Herunterladen: Google Cloud CLI Core Libraries (Platfor... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Herunterladen: Google Cloud CRC32C Hash Tool (Platform ... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Herunterladen: gcloud cli dependencies                  ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Deinstallieren: BigQuery Command Line Tool              ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Deinstallieren: BigQuery Command Line Tool (Platform Sp... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Deinstallieren: Cloud Storage Command Line Tool         ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Deinstallieren: Cloud Storage Command Line Tool (Platfo... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Deinstallieren: Google Cloud CLI Core Libraries         ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Deinstallieren: Google Cloud CLI Core Libraries (Platfo... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Deinstallieren: Google Cloud CRC32C Hash Tool (Platform... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Deinstallieren: gcloud cli dependencies                 ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Installieren: BigQuery Command Line Tool                ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Installieren: BigQuery Command Line Tool (Platform Spec... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Installieren: Cloud Storage Command Line Tool           ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Installieren: Cloud Storage Command Line Tool (Platform... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Installieren: Google Cloud CLI Core Libraries           ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Installieren: Google Cloud CLI Core Libraries (Platform... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Installieren: Google Cloud CRC32C Hash Tool (Platform S... ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Installieren: gcloud cli dependencies                   ═╣
╚════════════════════════════════════════════════════════════╝

Durchführung der Nachbearbeitungsschritte...abgeschlossen.

Aktualisierung abgeschlossen!

Um Ihre CLI auf die zuvor installierte Version zurückzusetzen, können Sie folgenden Befehl ausführen:
  $ gcloud components update --version 507.0.0