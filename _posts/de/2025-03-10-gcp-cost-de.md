---
audio: false
generated: true
lang: de
layout: post
title: GCP-Kostenschätzung für VPN in Taipeh
translated: true
type: note
---

Um die Kosten für die Nutzung eines Taipei-Servers als VPN mit Google Cloud abzuschätzen, unter der Annahme, dass Sie in Guangzhou leben und 50 GB Netzwerkdaten pro Monat mit einer E2 Micro Instanz erwarten, müssen wir die Kosten in mehrere Komponenten aufteilen: die virtuelle Maschine (VM), den ausgehenden Netzwerkverkehr (Egress) und den persistenten Speicher. Hier ist eine detaillierte Berechnung basierend auf der Preisgestaltung von Google Cloud für die Region `asia-east1` (Taipei), in der Ihr Server gehostet wird.

### 1. VM-Instanz-Kosten (E2 Micro in Taipei)
Bei E2 Micro handelt es sich um einen Maschinentyp mit geteilten Kernen, mit 0,25 vCPU und 1 GB Arbeitsspeicher. Laut der Preisgestaltung von Google Cloud für Compute Engine in der Region `asia-east1`:
- **Stundensatz für E2 Micro**: 0,0084 $ pro Stunde.
- **Stunden in einem Monat**: Unter der Annahme, dass ein typischer Monat 730 Stunden hat (eine Standardapproximation basierend auf 365 Tage ÷ 12 Monate ≈ 30,42 Tage × 24 Stunden).
- **Monatliche Kosten**:  
  0,0084 $/Stunde × 730 Stunden ≈ 6,132 $.

Die durchgehende Ausführung der E2 Micro Instanz über einen Monat kostet also ungefähr **6,13 $**.

### 2. Kosten für ausgehenden Netzwerkverkehr (Egress)
Da Sie den Taipei-Server als VPN von Guangzhou aus nutzen, beinhaltet Ihr Setup das Betreiben eines VPN-Servers (z.B. OpenVPN) auf der E2 Micro Instanz, nicht den Google Cloud Cloud VPN Service. Ihre 50 GB monatlicher Netzwerkdaten repräsentieren den gesamten über das VPN verarbeiteten Datenverkehr. So fließt der Datenverkehr:
- **Von Ihrem Gerät in Guangzhou zum VPN-Server**: Dies ist eingehender Verkehr (Eingang/Ingress) zu Google Cloud (kostenlos).
- **Vom VPN-Server ins Internet**: Dies ist ausgehender Verkehr (Ausgang/Egress) (kostenpflichtig).
- **Vom Internet zurück zum VPN-Server**: Dies ist eingehender Verkehr (Eingang/Ingress) (kostenlos).
- **Vom VPN-Server zurück zu Ihrem Gerät**: Dies ist ausgehender Verkehr (Ausgang/Egress) (kostenpflichtig).

Wenn sich Ihre 50 GB auf den gesamten VPN-Tunnel-Datenverkehr beziehen (vom Gerät gesendete Daten plus empfangene Daten), dann umfasst der von Google Cloud berechnete Egress-Verkehr:
- Vom VPN-Server ins Internet gesendete Daten.
- Vom VPN-Server zurück zu Ihrem Gerät gesendete Daten.

Unter der Annahme, dass die 50 GB die gesamte übertragene Datenmenge darstellen (z.B. Sie senden Anfragen und empfangen Antworten, wie beim Browsen oder Streaming), beträgt der gesamte Egress-Verkehr ungefähr 50 GB. Dies vereinfacht die Schätzung, da die genaue Aufteilung zwischen gesendeten und empfangenen Daten vom Nutzungsverhalten abhängt (z.B. Streaming hat mehr empfangene Daten, während Uploads mehr gesendete Daten haben). Für die allgemeine Internetnutzung behandeln wir die 50 GB als gesamten Egress.

Google Cloud berechnet für Internet-Egress basierend auf der Quellregion (`asia-east1` für Taipei):
- **Preisstufe**: Für Asien (ausschließlich China, Indien, Indonesien und den Philippinen) beträgt der Satz 0,12 $ pro GiB für die ersten 1 TB monatlichen Egress.
- **Umrechnung**: Google Cloud verwendet GiB (1 GiB = 1024³ Bytes), während Sie 50 GB (1 GB = 1000³ Bytes) angegeben haben. Genau genommen entspricht 1 GB ≈ 0,931 GiB, also 50 GB ≈ 46,55 GiB. Der Einfachheit halber und in der gängigen Praxis für grobe Schätzungen approximieren wir jedoch 50 GB ≈ 50 GiB, da der Unterschied bei kleinen Volumen gering ist.
- **Egress-Kosten**:  
  50 GiB × 0,12 $/GiB = 6,00 $.

Somit belaufen sich die Egress-Kosten auf ungefähr **6,00 $** pro Monat.

### 3. Kosten für persistenten Speicher
Die E2 Micro Instanz benötigt eine Startfestplatte (Boot Disk). Während die Google Cloud Free Tier 30 GB Standard Persistent Disk Storage in bestimmten US-Regionen bietet, ist Taipei (`asia-east1`) nicht enthalten, daher fallen Kosten an:
- **Festplattengröße**: Unter der Annahme einer typischen 30 GB Standard Persistent Disk (Sie könnten weniger verwenden, z.B. 10 GB, aber 30 GB ist für eine grundlegende VM üblich).
- **Preis**: 0,040 $ pro GB pro Monat in `asia-east1` für eine Standard Persistent Disk.
- **Monatliche Kosten**:  
  30 GB × 0,040 $/GB = 1,20 $.

Der persistente Speicher fügt **1,20 $** pro Monat hinzu.

### 4. Externe IP-Adresse
Ihr VPN-Server benötigt eine externe IP-Adresse, um von Guangzhou aus erreichbar zu sein. Für Compute Engine VMs gilt:
- Wenn die IP an eine laufende VM angehängt ist, fallen keine zusätzlichen Gebühren an.
- Wenn sie reserviert, aber ungenutzt ist, fällt eine kleine Gebühr an (hier nicht anwendbar, da die VM durchgehend läuft).

Da Ihre E2 Micro Instanz die externe IP-Adresse nutzt, sind diese Kosten **im VM-Preis enthalten**.

### Geschätzte Gesamtkosten
Zusammenzählung aller Komponenten:
- **VM-Instanz**: 6,13 $
- **Egress-Datenverkehr**: 6,00 $
- **Persistenter Speicher**: 1,20 $
- **Externe IP**: 0,00 $ (enthalten)

**Gesamt**: 6,13 $ + 6,00 $ + 1,20 $ = **13,33 $ pro Monat**.

### Zusätzliche Hinweise
- **Eingehender Datenverkehr (Ingress)**: Kostenlos, Daten, die in die VM eingehen (von Ihnen oder aus dem Internet), verursachen keine Kosten.
- **Keine Free Tier-Vorteile**: Der E2 Micro Free Tier gilt nur für bestimmte US-Regionen (nicht Taipei), und das 1 GB kostenlose Egress-Volumen gilt von Nordamerika aus (nicht Asien) und schließt Ziele in China aus, daher ist es hier nicht anwendbar.
- **Nutzungsannahmen**: Die 13,33 $ gehen davon aus, dass 50 GB der gesamte Egress-Datenverkehr ist. Wenn es sich nur um gesendete oder empfangene Daten handelt, passen Sie die Egress-Kosten entsprechend an (z.B. wenn 50 GB empfangene Daten sind, betragen die Egress-Kosten zu Ihnen 6,00 $, aber die Egress-Kosten ins Internet könnten geringer sein).
- **Kein Cloud VPN**: Da Sie Ihre eigene VPN-Software (z.B. OpenVPN) betreiben, fallen keine zusätzlichen Gebühren für Cloud VPN Gateway oder Tunnel an.

### Endergebnis
Die geschätzten Kosten für die Nutzung eines Taipei-Servers (`asia-east1`) als VPN auf Google Cloud mit einer E2 Micro Instanz, 50 GB monatlichem Netzwerkdatenverkehr und einer 30 GB Festplatte belaufen sich auf ungefähr **13,33 $ pro Monat**. Dies beinhaltet die VM-Instanz (6,13 $), den Egress-Datenverkehr ins Internet und zu Ihrem Gerät (6,00 $) sowie den persistenten Speicher (1,20 $).