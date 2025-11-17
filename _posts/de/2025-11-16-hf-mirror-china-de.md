---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Nutzung von hf-mirror.com in China
translated: true
type: note
---

### hf-mirror.com verstehen
hf-mirror.com ist ein von der Community gepflegter Mirror des offiziellen Hugging Face Hubs (huggingface.co), der speziell dafür entwickelt wurde, Nutzern in China (einschließlich Guangzhou) zu helfen, Netzwerkbeschränkungen zu umgehen und KI-Modelle/Datensätze schneller herunterzuladen. Er repliziert die vollständige Repository-Struktur, sodass Sie auf Modelle wie GPT-2 oder Datensätze wie WikiText zugreifen können, ohne die ursprüngliche Seite direkt aufzurufen, die oft langsam oder blockiert ist. Da Sie oft Clash Proxy verwenden, beachten Sie, dass hf-mirror.com in China gehostet wird und typischerweise keinen Proxy für den Zugriff benötigt – er ist für die direkte Nutzung in China optimiert. Wenn Sie Ihren Datenverkehr bereits über Clash leiten, können Sie den Datenverkehr für hf-mirror.com entweder direkt routen (um unnötige Hops zu vermeiden) oder, wenn bevorzugt, weiterhin über den Proxy leiten.

### Grundlegende Einrichtung: Verwendung des Mirrors
Der Schlüssel liegt darin, die Umgebungsvariable `HF_ENDPOINT` so zu setzen, dass sie auf den Mirror verweist. Dies funktioniert global für Hugging Face-Tools wie die `transformers`-Bibliothek, `huggingface-cli` oder `hfd` (ein schnellerer Downloader). Führen Sie dies **vor** dem Importieren von Bibliotheken oder dem Starten von Downloads durch.

#### 1. Setzen der Umgebungsvariable
- **Unter Linux/macOS (permanent)**: Fügen Sie dies zu Ihrer `~/.bashrc` oder `~/.zshrc` hinzu:
  ```
  echo 'export HF_ENDPOINT=https://hf-mirror.com' >> ~/.bashrc
  source ~/.bashrc
  ```
- **Unter Windows (PowerShell, permanent)**: Führen Sie dies einmal aus:
  ```
  [System.Environment]::SetEnvironmentVariable('HF_ENDPOINT', 'https://hf-mirror.com', 'User')
  ```
  Starten Sie dann Ihr Terminal neu.
- **Temporär (beliebiges Betriebssystem)**: Stellen Sie Befehlen ein Präfix voran:
  ```
  HF_ENDPOINT=https://hf-mirror.com your_command_here
  ```

Dies leitet alle Hugging Face-Downloads zum Mirror um, ohne Ihren Code zu ändern.

#### 2. Erforderliche Tools installieren
- Installieren Sie die Hugging Face Hub CLI (für Downloads):
  ```
  pip install -U huggingface_hub
  ```
- Für noch schnellere Downloads, holen Sie sich `hfd` (Hugging Face Downloader, verwendet aria2 für multithreaded Geschwindigkeit):
  ```
  wget https://hf-mirror.com/hfd/hfd.sh  # Oder über den Browser herunterladen
  chmod +x hfd.sh
  ```

#### 3. Modelle oder Datensätze herunterladen
- **Verwendung von huggingface-cli** (unterstützt Fortsetzen bei Unterbrechung):
  ```
  # Ein Modell herunterladen (z.B. GPT-2)
  huggingface-cli download gpt2 --resume-download --local-dir ./gpt2

  # Einen Datensatz herunterladen (z.B. WikiText)
  huggingface-cli download --repo-type dataset wikitext --resume-download --local-dir ./wikitext
  ```
- **Verwendung von hfd** (schneller, besonders bei großen Dateien):
  ```
  # Modell
  ./hfd.sh gpt2

  # Datensatz
  ./hfd.sh wikitext --dataset
  ```
- **In Python-Code** (z.B. mit der transformers-Bibliothek):
  ```python
  import os
  os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'  # Vor Imports setzen

  from transformers import AutoModel, AutoTokenizer
  model = AutoModel.from_pretrained('gpt2')  # Lädt automatisch vom Mirror herunter
  tokenizer = AutoTokenizer.from_pretrained('gpt2')
  ```
  Ausführen mit: `HF_ENDPOINT=https://hf-mirror.com python your_script.py`

#### 4. Umgang mit geschützten/angemeldeten Modellen
Einige Modelle (z.B. Llama-2) erfordern einen Hugging Face-Account und einen Token:
- Melden Sie sich auf huggingface.co an (verwenden Sie Ihren Clash Proxy, falls die Seite blockiert ist).
- Generieren Sie einen Token unter https://huggingface.co/settings/tokens.
- Laden Sie herunter mit:
  ```
  huggingface-cli download --token hf_YourTokenHere meta-llama/Llama-2-7b-hf --resume-download --local-dir ./Llama-2-7b-hf
  ```
  Oder für hfd:
  ```
  ./hfd.sh meta-llama/Llama-2-7b-hf --hf_username your_username --hf_token hf_YourTokenHere
  ```

### Integration mit Clash Proxy
Da hf-mirror.com ein chinesischer Mirror ist, sollte er ohne Clash erreichbar sein (Direktverbindung ist schneller). Wenn Sie ihn jedoch dennoch über den Proxy leiten möchten (z.B. aus Konsistenzgründen oder bei Problemen), konfigurieren Sie Clash so, dass der Datenverkehr zu hf-mirror.com über Ihre bevorzugte Proxy-Gruppe geroutet wird. Clash benötigt keine spezielle "HF"-Konfiguration – es ist systemweit.

#### Schnelle Clash-Einrichtungstipps
- Stellen Sie sicher, dass Clash läuft und als Systemproxy eingestellt ist (in Clash: Gehen Sie zu "General" > Aktiviere "System Proxy").
- **hf-mirror.com direkt routen (empfohlen für Geschwindigkeit)**: Bearbeiten Sie Ihre Clash-Konfigurations-YAML (normalerweise `config.yaml` im Clash-Ordner). Fügen Sie eine Regel hinzu, um den Proxy für den Mirror zu umgehen:
  ```
  rules:
    # ... Ihre bestehenden Regeln ...
    - DOMAIN-SUFFIX,hf-mirror.com,DIRECT  # Umgeht den Proxy, geht direkt
    # ... restliche Regeln ...
  ```
  Laden Sie die Konfiguration in Clash neu (Profiles > Reload).
- **Über Proxy leiten falls nötig**: Wenn Sie die Route über Clash bevorzugen, fügen Sie keine spezielle Regel hinzu – es folgt Ihrer Standardeinstellung (z.B. `MATCH,Proxy`). Testen Sie, indem Sie hf-mirror.com in einem Browser mit Clash an/aus pingen.
- Für Downloads: Führen Sie Befehle in einem Terminal aus, in dem der Systemproxy aktiv ist (Clash kümmert sich darum). Wenn Sie Python verwenden, respektieren Bibliotheken wie `requests` (von transformers verwendet) die von Clash gesetzten `HTTP_PROXY`/`HTTPS_PROXY` Umgebungsvariablen (z.B. `http://127.0.0.1:7890` für den HTTP-Port).
- Test: Versuchen Sie, ein kleines Modell wie `distilbert-base-uncased` herunterzuladen. Wenn es langsam ist, schalten Sie Clash für den hf-mirror.com-Datenverkehr aus.

### Problembehandlung
- **Downloads erreichen immer noch huggingface.co?** Stellen Sie sicher, dass `HF_ENDPOINT` gesetzt ist, **bevor** Sie HF-Bibliotheken importieren (starten Sie Ihr Notebook/Terminal neu).
- **Langsame Geschwindigkeiten?** Verwenden Sie `hfd` mit aria2 (es unterstützt mehrere Verbindungen). Oder überprüfen Sie Ihr Netzwerk – Nutzer in Guangzhou erreichen oft 10-50 MB/s auf hf-mirror.com.
- **Fehler bei Datensätzen?** Einige haben benutzerdefinierte Skripte; bearbeiten Sie diese, um `https://hf-mirror.com` als Basis-URL zu verwenden.
- **Windows-spezifisch**: Wenn Sie Anaconda verwenden, setzen Sie die Umgebungsvariable in der Basis-Umgebung.
- Für fortgeschrittenes Self-Hosting eines lokalen Mirrors (wenn Sie volle Kontrolle wollen), sehen Sie sich Open-Source-Tools wie Olah oder hf-mirror-site auf GitHub an, aber beginnen Sie mit dem öffentlichen Mirror.

Dieses Setup sollte Ihnen zuverlässige Downloads ermöglichen. Wenn Sie auf spezifische Fehler stoßen, teilen Sie die Ausgabe für weitere Hilfe!

### Referenzen
- [HF-Mirror Offizieller Guide](https://hf-mirror.com/)
- [Hugging Face Hub Docs zu Endpoints](https://huggingface.co/docs/huggingface_hub/en/package_reference/environment_variables#huggingface_hub_constants.HF_ENDPOINT)
- [hfd Downloader](https://hf-mirror.com/hfd/hfd.sh)
- [Clash Config Rules](https://github.com/Dreamacro/clash/wiki/Configuration#rules)
- [Stack Overflow: Herunterladen in China](https://stackoverflow.com/questions/77388822/how-to-download-huggingface-bert-base-uncased-in-china)