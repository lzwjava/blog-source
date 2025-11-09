---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Übersicht des DragonBoard 410c Kompaktcomputers
translated: true
type: note
---

Das Snapdragon 410 Board bezieht sich typischerweise auf das DragonBoard 410c, einen kompakten Single-Board-Computer (SBC), der von Qualcomm als Referenzplattform für IoT, Embedded Systems und Prototyping entwickelt wurde. Es wurde um 2015 veröffentlicht, ist Teil des 96Boards-Ökosystems und hat in etwa die Größe einer Kreditkarte. Wichtige Spezifikationen sind:

- **Prozessor**: Qualcomm Snapdragon 410 (MSM8916/APQ8016), ein Quad-Core ARM Cortex-A53 CPU mit bis zu 1,2 GHz Taktfrequenz.
- **GPU**: Adreno 306 bei 450 MHz, unterstützt 1080p-Videowiedergabe und einfache Grafiken.
- **Speicher**: 1 GB LPDDR3 RAM und 8 GB eMMC-Speicher (erweiterbar über microSD).
- **Konnektivität**: Dual-Band Wi-Fi 802.11ac, Bluetooth 4.1, GPS, USB 2.0, HDMI und GPIO-Pins für Hardware-Bastelarbeiten.
- **OS-Unterstützung**: Läuft mit Linux (z.B. Ubuntu), Android und Windows 10 IoT Core out of the box.

Es ist für Entwickler konzipiert, die stromsparende Geräte wie Smart-Home-Gadgets oder Industriesensoren bauen, mit starkem Fokus auf Drahtlosfunktionen und Erweiterbarkeit.

### Leistung
Der Snapdragon 410 ist ein Einsteiger-SoC aus der Mitte der 2010er Jahre, der in einem 28-nm-Prozess gefertigt wird. Das macht ihn stromsparend, aber nach Standards von 2025 veraltet. Er ist angemessen für grundlegende Aufgaben wie Webbrowsing, E-Mail, leichte Medienwiedergabe und einfache IoT-Apps, hinkt aber beim Multitasking, Gaming oder anspruchsvollen Berechnungen hinterher.

Wichtige Benchmark-Höhepunkte (von Geräten mit diesem Chip):
- **Geekbench 6**: Single-Core ~200–250, Multi-Core ~600–700 (vergleichbar mit sehr einfachen modernen Chips).
- **3DMark Ice Storm**: Rund 8.500–9.000 Punkte (Physik-/Grafiktests), geeignet für 2D-Oberflächen, aber kämpft mit 3D-Spielen.
- **AnTuTu v6**: Etwa 20.000–25.000 Gesamtpunktzahl, unterstreicht seine Budget-Positionierung.

Im realen Einsatz auf dem DragonBoard ist ein reibungsloser Betrieb für Entwicklungs-Scripting oder Sensorintegration zu erwarten, aber es kann unter anhaltender Last aufgrund thermischer Grenzen und begrenztem RAM drosseln. Er wird selbst von Mittelklasse-Chips aus dem Jahr 2020 übertroffen (z.B. 5–10x langsamer als ein Snapdragon 888 bei Multi-Core-Aufgaben), daher ist er am besten für Hobbyprojekte geeignet und nicht für Produktions-Hochleistungsanforderungen.

[DragonBoard 410c - 96Boards](https://www.96boards.org/product/dragonboard410c/)  
[Qualcomm Snapdragon 410 Benchmarks - NotebookCheck](https://www.notebookcheck.net/Qualcomm-Snapdragon-410-APQ8016-Benchmarks-and-Specs.142822.0.html)  
[CPU Benchmark - PassMark](https://www.cpubenchmark.net/cpu.php?cpu=Qualcomm%2BTechnologies%252C%2BInc%2BMSM8916&id=4009)