---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Optimierung der Hugging Face Download-Geschwindigkeiten
translated: true
type: note
---

Ihr aktueller Download erreicht den Haupt-Endpoint von Hugging Face (`huggingface.co`), der hauptsächlich in europäischen/US-amerikanischen Rechenzentren gehostet wird. Das Routing über Ihren Taiwan-Proxy von Guangzhou aus verursacht ähnliche Latenzprobleme wie zuvor: ~200–300 ms Round-Trip, plus potenzielle Drosselung bei großen Dateien (dieses Parquet ist ~500 MB–1 GB pro Shard). Die 302-Weiterleitung, die Sie sehen, führt wahrscheinlich zu einem CloudFront CDN Edge, aber möglicherweise nicht zum optimalen für Asien, was zu Geschwindigkeitseinbußen führt (z.B. 1–5 MB/s).

Um die 20–60 MB/s Geschwindigkeiten aus den Wikimedia-Downloads zu erreichen, verwenden Sie diese Anpassungen – mit Priorität auf asienfreundlichen Optionen. Alle behalten Ihr Clash/TW-Proxy-Setup bei.

### 1. **Zum HF Mirror wechseln (Schnellste für China/Taiwan—Empfohlen)**
   HF Mirror (`hf-mirror.com`) ist ein Community-betriebener CDN, der für Ostasien optimiert ist (proxied durch nationale CN-Netzwerke wie Tsinghua). Er spiegelt alle HF-Datasets exakt, einschließlich der FineWeb Parquet-Dateien. Vom TW-Proxy aus sind 30–80 MB/s zu erwarten.

   Aktualisieren Sie Ihr Skript:
   ```bash
   #!/bin/bash
   # wget_fineweb_1.sh (aktualisiert für Geschwindigkeit)
   mkdir -p fineweb_test_dump
   cd fineweb_test_dump
   echo "Lade FineWeb-Shard über HF Mirror herunter (schneller für Asien)..."

   # Ersetze huggingface.co mit hf-mirror.com
   wget -c "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00000.parquet?download=true"

   echo "Fertig! Shard-Größe: ~500MB–1GB"
   echo "Für weitere Shards, schleife z.B. über 000_00001.parquet, etc."
   echo "Zum Laden in Python: from datasets import load_dataset; ds = load_dataset('HuggingFaceFW/fineweb', name='CC-MAIN-2013-20', split='train', streaming=True)"
   ```

   Führen Sie es aus: `./scripts/train/wget_fineweb_1.sh`
   - Falls der Mirror Verzögerungen hat (selten), fallen Sie auf das offizielle zurück: `https://huggingface.co/datasets/...` (aber fügen Sie den Geschwindigkeitstipp aus #2 hinzu).

### 2. **Beschleunigen mit hf_transfer (Für jeden HF-Download—100x schneller bei Wiederaufnahme)**
   Hugging Face's offizielles Rust-Tool für parallele/mehrthreadige Downloads. Es wiederholt Versuche automatisch, verwendet mehr Verbindungen und erreicht >500 MB/s auf guten Links. Funktioniert indirekt mit `wget` oder direkt via Python (wenn Ihr Skript `huggingface_hub` verwendet).

   Installation (einmalig, via pip – Ihre Umgebung hat es):
   ```bash
   pip install hf_transfer
   export HF_HUB_ENABLE_HF_TRANSFER=1
   ```

   Führen Sie dann Ihr ursprüngliches Skript erneut aus. Es beschleunigt die zugrunde liegenden `wget`-Aufrufe zu HF-URLs.
   - Pro Tipp: Für vollständiges Dataset-Streaming (kein vollständiger Download), verwenden Sie Python in Ihrer Pipeline:
     ```python
     from datasets import load_dataset
     import os
     os.environ['HF_HUB_ENABLE_HF_TRANSFER'] = '1'  # Vor dem Import aktivieren
     ds = load_dataset("HuggingFaceFW/fineweb", name="CC-MAIN-2013-20", split="train", streaming=True)
     for example in ds.take(1000):  # Stream/Verarbeitung On-the-Fly
         print(example)
     ```
     Dies lädt Shards lazy via den Mirror, wenn Sie `HF_ENDPOINT=https://hf-mirror.com` setzen.

### 3. **Clash-Regel-Anpassung (Wenn erlaubt—Ultra-schnell Domestic)**
   Falls Ihre Proxy-Konfiguration Bypass für HF erlaubt (oder Routing zu HK/SG Nodes), fügen Sie eine Regel für `huggingface.co` / `hf-mirror.com` hinzu, um direct/domestic zu gehen. In `clash.yaml`:
   ```
   rules:
     - DOMAIN-SUFFIX,hf-mirror.com,DIRECT  # Oder Ihr CN Mirror Node
     - DOMAIN-SUFFIX,huggingface.co,DIRECT
   ```
   Starten Sie Clash neu und laden Sie dann herunter. Kombiniert mit #1 für 50–100+ MB/s via Tsinghua Mirrors.

### Warum dies die Wikimedia-Geschwindigkeiten erreicht
- Wikimedia: Der Redirector wählte automatisch Asien (Japan/KR/SG) aus → niedrige Latenz.
- HF: Standard ist EU/US → hohe Latenz; Mirror + Transfer ändert dies zu asien-optimiert.

Testen Sie zuerst einen Shard – falls es immer noch langsam ist, prüfen Sie `curl -I https://hf-mirror.com/...` für Header (sollte Asia CDN anzeigen). Für das volle 15T FineWeb, streamen Sie via `datasets` Bibliothek, um Downloads von 100en von GB zu vermeiden. Melden Sie sich, wenn die Geschwindigkeiten nicht sprunghaft ansteigen!