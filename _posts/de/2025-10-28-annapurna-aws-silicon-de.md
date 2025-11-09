---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: 'Annapurna Labs: AWS maßgeschneiderte Siliziumchips'
translated: true
type: note
---

### Was ist Annapurna Labs?

**Annapurna Labs** ist ein israelisches Halbleiterunternehmen, das sich auf **hochleistungsfähige, energieeffiziente Prozessoren** für Cloud Computing, Netzwerke, Speicher und KI-Workloads spezialisiert hat. Es wurde **im Januar 2015 von Amazon** für schätzungsweise ~350–370 Millionen US-Dollar **übernommen** und operiert heute als hundertprozentige Tochtergesellschaft von **Amazon Web Services (AWS)**.

Annapurna Labs entwickelt **maßgeschneiderte Chips**, die einen Großteil der AWS-Infrastruktur antreiben und es Amazon ermöglichen, die Abhängigkeit von Drittanbieter-Chipherstellern wie Intel, Broadcom und NVIDIA für bestimmte Workloads zu verringern.

---

### Wichtige von Annapurna Labs entwickelte Chips (Verwendung in AWS)

| Chippfamilie | Typ | Hauptmerkmale | Primärer AWS-Anwendungsfall |
|-------------|------|--------------|-----------------------|
| **Alpine** | ARM-basierter SoC | Multi-Core ARMv8-CPUs, geringer Stromverbrauch, integrierte Netzwerk-/Speicherfunktionen | Frühe EC2-Instanzen, Storage-Controller |
| **Graviton** | ARM-basierte CPU | 64-Bit ARM Neoverse Kerne (AWS-eigenes Design), hohe Kernanzahl, DDR5, PCIe Gen4/5 | **EC2 Graviton Instanzen** (Allzweck-Rechenleistung) |
| **Nitro** | SmartNIC / Offload | ARM-CPUs + benutzerdefinierte Beschleuniger für Virtualisierung, Sicherheit, Speicher, Netzwerke | **EC2 Nitro System**, EBS, VPC, Sicherheits-Offload |
| **Inferentia** | KI-Inferenz | Hoher Tensor-Durchsatz, niedrige Latenz, Neuron-Cores | **EC2 Inf1/Inf2 Instanzen** für ML-Inferenz |
| **Trainium** | KI-Training | Skalierbar für große Sprachmodelle, hohe Speicherbandbreite, NeuronLink-Interconnect | **EC2 Trn1/Trn2 Instanzen** für das Training von LLMs |

---

### Wichtigste Chippfamilien (Stand 2025)

#### 1. **AWS Graviton (CPU)**
- **Architektur**: Benutzerdefinierte ARM Neoverse-basierte Kerne (keine Standard-CPUs)
- **Generationen**:
  - **Graviton1** (2018): 16-Kern ARMv8, verwendet in A1-Instanzen
  - **Graviton2** (2020): 64-Kern Neoverse N1, ~40 % besseres Preis-Leistungs-Verhältnis als x86
  - **Graviton3** (2022): Neoverse V1, DDR5, bfloat16, bis zu 60 % besser als Graviton2
  - **Graviton4** (2024): Neoverse V2, 96 Kerne, 2,7x Leistung/Watt gegenüber Graviton3
- **Verwendung**: Betreibt **~30–40 % der AWS EC2 Workloads** (insbesondere Container, Microservices, Datenbanken)

#### 2. **AWS Inferentia (KI-Inferenz)**
- **Inferentia2** (2023): 4-fache Leistung gegenüber Inferentia1, unterstützt FP16/BF16/INT8
- Optimiert für **Echtzeit-Inferenz** (Empfehlungssysteme, Spracherkennung, Bildverarbeitung)
- Verwendet in **SageMaker**, **EC2 Inf2**

#### 3. **AWS Trainium (KI-Training)**
- **Trainium2** (angekündigt 2024, Auslieferung 2025): 4-fache Trainingsleistung gegenüber Trainium1
- Entwickelt, um mit **NVIDIA H100** für LLM-Training zu konkurrieren
- Unterstützt **Modelle mit Billionen Parametern**, High-Bandwidth Memory (HBM)

#### 4. **Nitro System (SmartNIC / DPU)**
- Benutzerdefinierte ARM-SoCs mit Hardware-Beschleunigern
- Entlastet Hypervisor, Netzwerke, Speicher, Verschlüsselung
- Ermöglicht **Bare-Metal-Leistung in virtualisierten Umgebungen**

---

### Warum Annapurna wichtig ist

- **Kosten & Effizienz**: AWS gibt bis zu **40 % besseres Preis-Leistungs-Verhältnis** gegenüber x86 an
- **Vertikale Integration**: Amazon kontrolliert die Chips → schnellere Innovation, niedrigere Kosten
- **KI-Offensive**: Trainium/Inferentia fordern die Dominanz von NVIDIA in der Cloud-KI direkt heraus
- **Resilienz der Lieferkette**: Verringert die Abhängigkeit von reinen Intel/TSMC-Lieferketten

---

### Zusammenfassung

> **Annapurna Labs = AWS' geheime Chip-Waffe.**  
> Sie bauen **ARM-basierte Graviton CPUs**, **Inferentia (Inferenz)**, **Trainium (Training)** und **Nitro Offload-Chips** — alle für die Cloud optimiert.  
> Diese ermöglichen **günstigere, schnellere, umweltfreundlichere** AWS-Dienste und sind ein Hauptgrund, warum AWS Wettbewerber preislich unterbieten und KI skalieren kann.

Lass mich wissen, wenn du tiefere Einblicke in einen bestimmten Chip möchtest (z.B. Graviton4 vs Apple M4, Trainium2 vs H100).