---
audio: false
generated: true
lang: de
layout: post
title: Behebung des llama.cpp Modellladefehlers
translated: true
type: note
---

Basierend auf dem Fehler `gguf_init_from_file_impl: failed to read key-value pairs` ist Ihre Modelldatei entweder **beschädigt**, **unvollständig** oder **inkompatibel** mit Ihrer llama.cpp-Version. So beheben Sie das Problem:

### 1. **Modell überprüfen und erneut herunterladen**
   ```bash
   # Aktuelle Dateigröße prüfen (Q6_K Quant sollte ~6,1 GB für ein 8B-Modell sein):
   ls -lh /home/lzw/Projects/llama.cpp/models/DeepSeek-R1-0528-Qwen3-8B-UD-Q6_K_XL.gguf

   # Erwartete Ausgabe:
   # -rw-r--r-- 1 lzw lzw 6.1G Jun  2 10:00 ...Q6_K_XL.gguf
   ```
   - Wenn die Größe < 6 GB ist, **laden Sie das Modell erneut herunter**:
     ```bash
     rm /home/lzw/Projects/llama.cpp/models/DeepSeek-R1-0528-Qwen3-8B-UD-Q6_K_XL.gguf
     # Erneut von der Originalquelle herunterladen (z.B. HuggingFace)
     ```

### 2. **llama.cpp aktualisieren**
Ihr Build (Commit `7675c555`) könnte veraltet sein:
```bash
cd ~/Projects/llama.cpp
git pull origin master          # Code aktualisieren
rm -rf build && mkdir build     # Clean Build
cd build
cmake .. -DLLAMA_CUBLAS=ON      # CUDA aktivieren
make -j                         # Neu kompilieren
```

### 3. **Modellintegrität validieren**
Testen Sie das Modell mit einer einfachen Inferenz:
```bash
~/Projects/llama.cpp/build/bin/main \
  -m /home/lzw/Projects/llama.cpp/models/DeepSeek-R1-0528-Qwen3-8B-UD-Q6_K_XL.gguf \
  -p "Hallo" -n 10
```
- Wenn dies fehlschlägt, ist die Modelldatei definitiv beschädigt.

### 4. **Ein anderes Modell testen (Plausibilitätsprüfung)**
Testen Sie mit einem bekannten, funktionierenden Modell (z.B. [TinyLlama](https://huggingface.co/TheBloke/TinyLlama-1.1B-1T-OpenOrca-GGUF)):
```bash
~/Projects/llama.cpp/build/bin/llama-server \
  -m /pfad/zu/tinyllama.Q8_0.gguf \
  --port 8000
```
- Wenn dies funktioniert, ist Ihre ursprüngliche Modelldatei das Problem.

### 5. **Modell erneut konvertieren (Fortgeschritten)**
Wenn das erneute Herunterladen fehlschlägt:
1. Holen Sie sich das originale Hugging Face-Modell:
   ```bash
   huggingface-cli download deepseek-ai/DeepSeek-R1-0528-Qwen3-8B --local-dir ./deepseek-original
   ```
2. Erneut in GGUF konvertieren:
   ```bash
   python3 ~/Projects/llama.cpp/convert-hf-to-gguf.py \
     ./deepseek-original \
     --outtype q6_k  # Passen Sie dies an Ihre Quantisierung an
   ```

### Häufige Lösungen im Überblick:

| Problem | Lösung |
|-------|----------|
| **Beschädigter Download** | Modell erneut herunterladen |
| **Veraltete llama.cpp** | `git pull` + neu kompilieren |
| **Inkompatibles GGUF** | Neueste `convert-hf-to-gguf.py` verwenden |
| **Dateiberechtigungen** | `chmod +r /pfad/zu/model.gguf` |

> 💡 **Hinweis:** Das DeepSeek-R1-Modell ist neu (veröffentlicht am 28. Mai 2024). Stellen Sie sicher, dass Ihre llama.cpp **innerhalb der letzten Woche aktualisiert** wurde, um Kompatibilität zu gewährleisten.

Beginnen Sie damit, das Modell erneut herunterzuladen und llama.cpp zu aktualisieren – dies löst 90 % solcher Probleme. Lassen Sie es mich wissen, wenn Sie weitere Hilfe benötigen!