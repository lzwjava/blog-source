---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: NanoChat Kompaktes Full-Stack-LLM
translated: true
type: note
---

### Was ist NanoChat?

NanoChat ist eine kompakte, Full-Stack-Implementierung eines großen Sprachmodell-Systems (LLM), ähnlich wie ChatGPT, aufgebaut in einer einzigen, minimalen Codebasis, die leicht zu hacken ist und nur wenige Abhängigkeiten erfordert. Erstellt von Andrej Karpathy (bekannt für seine Arbeit im Bereich KI, wie nanoGPT), ist es dafür konzipiert, die komplette LLM-Pipeline auszuführen – von Tokenisierung und Pre-Training über Fine-Tuning, Evaluation, Inferenz bis hin zu einer einfachen Web-UI für das Chatten mit Ihrem Modell – auf erschwinglicher Hardware wie einem einzelnen 8xH100 GPU-Node.

Es positioniert sich als der "beste ChatGPT, den 100 US-Dollar kaufen können" und dient als Baseline für kostengünstige LLM-Entwicklung (unter 1.000 US-Dollar gesamt). Damit ist es ein Abschlussprojekt für Karpathys bevorstehenden LLM101n-Kurs von Eureka Labs, das Einfachheit gegenüber komplexen Konfigurationen betont.

### Hauptmerkmale
- **End-to-End-Pipeline**: Verarbeitet alles in ~2.000 Codezeilen (mit einer winzigen `uv.lock`-Datei für Abhängigkeiten). Trainiert ein leistungsfähiges Modell mit 4e19 FLOPs in etwa 4 Stunden auf einem 8xH100-Setup, das ~24 US-Dollar/Stunde kostet.
- **ChatGPT-ähnliche UI**: Nach dem Training können Sie einen Webserver starten, um mit Ihrem Modell zu interagieren, genau wie beim echten ChatGPT.
- **Evaluierungsbericht**: Erzeugt automatisch einen `report.md` mit Benchmark-Scores für Aufgaben wie ARC-Challenge, GSM8K, HumanEval, MMLU und mehr. Ein Beispiel-Lauf für 100 US-Dollar zeigt beispielsweise fortschreitende Verbesserungen über die Stadien hinweg (BASE, MID, SFT, RL):

| Metric        | BASE   | MID    | SFT    | RL     |
|---------------|--------|--------|--------|--------|
| CORE          | 0.2219 | -      | -      | -      |
| ARC-Challenge | -      | 0.2875 | 0.2807 | -      |
| ARC-Easy      | -      | 0.3561 | 0.3876 | -      |
| GSM8K         | -      | 0.0250 | 0.0455 | 0.0758 |
| HumanEval     | -      | 0.0671 | 0.0854 | -      |
| MMLU          | -      | 0.3111 | 0.3151 | -      |
| ChatCORE      | -      | 0.0730 | 0.0884 | -      |

(Gesamtzeit: ~3h51m für den kompletten Lauf.)
- **Hardware-Flexibilität**: Funktioniert auf Ampere 8xA100 (langsamer), einzelnen GPUs (mit automatischer Gradient-Akkumulation) oder Setups mit geringerem VRAM durch Anpassen der Batch-Größen. Verwendet Vanilla PyTorch; anpassbar für andere Geräte mit Tweaks.
- **Datenquellen**: Bezieht Daten aus Hugging Face Datasets wie FineWeb und SmolTalk.
- **Extras**: Beinhaltet Tests (z.B. für den Rust-basierten Tokenizer), und es ist einfach, das gesamte Repo (~330KB) zu packen, um es mit anderen LLMs abzufragen.

Es ist inspiriert von Karpathys früherem nanoGPT-Projekt und modded-nanoGPT, aber hochskaliert für eine vollständige Chat-Erfahrung.

### Erste Schritte
Der schnellste Weg ist das `speedrun.sh`-Skript, das das 100-US-Dollar-Modell End-to-End auf einem 8xH100 (z.B. via Lambda Labs) abwickelt:

1.  Starten Sie eine 8xH100-Instanz und klonen Sie das Repo.
2.  Führen Sie aus:
    ```
    bash speedrun.sh
    ```
    (Oder in einer Screen-Session für Logging: `screen -L -Logfile speedrun.log -S speedrun bash speedrun.sh`. Trennen Sie sich mit Strg+A+D und verfolgen Sie das Log mit `tail`.)

3.  Sobald es fertig ist (~4 Stunden), aktivieren Sie die Umgebung (`source .venv/bin/activate`) und starten Sie die UI:
    ```
    python -m scripts.chat_web
    ```
    Öffnen Sie die lokale URL (z.B. http://ihre-ip:8000), um mit Ihrem Modell zu chatten. Prüfen Sie `report.md` für die Ergebnisse.

Für größere Modelle (z.B. 300-US-Dollar-Tier in ~12 Stunden, das GPT-2 bei einigen Scores schlägt), bearbeiten Sie `speedrun.sh`, um mehr Data Shards herunterzuladen und die Tiefe/Batch-Größen anzupassen. Führen Sie Tests aus wie `python -m pytest tests/test_rustbpe.py -v -s`.

Es ist MIT-lizenziert und offen für Beiträge, um Micro-Modelle weiter voranzutreiben. Für eine detaillierte Anleitung lesen Sie die Discussions im Repo.

[nanoChat GitHub Repo](https://github.com/karpathy/nanochat)