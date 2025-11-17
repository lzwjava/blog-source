---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Lösungen für die Download-Geschwindigkeit von Hugging Face
translated: true
type: note
---

Ihr Problem ist sehr typisch für Nutzer aus dem chinesischen Festland (insbesondere Südchina wie Guangzhou) beim Herunterladen großer Dateien von Hugging Face.

### Warum ohne Proxy → extrem langsam (~200–300 KB/s)
- Obwohl Sie **hf-mirror.com** (den offiziellen chinesischen Mirror von HF + 01.AI) verwenden, sind die eigentlichen großen Parquet-Dateien von FineWeb **nicht in China gecached**.
- hf-mirror.com leitet Sie nur zum globalen CDN weiter (jetzt mit xet-bridge auf AWS us-east-1).
- Von Guangzhou ohne Proxy → Ihr Verkehr läuft über internationale Gateways (China Telecom/Unicom/Mobile Backbone → US AWS), und Downloads großer Dateien werden stark gedrosselt oder QoS-limitiert. 2 GB Dateien fallen leicht auf < 500 KB/s, manchmal sogar 100 KB/s.

### Warum mit Clash Proxy → plötzlich sehr schnell (oft 20–100 MB/s)
- Ihr Clash verwendet mit sehr hoher Wahrscheinlichkeit einen Hongkong-, Taiwan-, Japan-, Singapur- oder Korea-Node (sehr verbreitet bei Guangzhou-Nutzern).
- Diese Nodes haben:
  - Direktes Peering oder sehr gute Konnektivität zu AWS us-east-1 (oder Cloudflare, das HF ebenfalls nutzt)
  - Keine Drosselung des ausgehenden Verkehrs durch die GFW
  - Viel höhere Bandbreite
- Selbst wenn Sie also den "Umweg" über den Proxy nehmen, ist der tatsächliche Pfad viel schneller als der direkte internationale Ausgang vom chinesischen Festland.

### Kurz gesagt
Direkt (selbst via hf-mirror.com) von Guangzhou → langsam, weil der echte Speicherort immer noch in den USA ist und die China → USA Bandbreite für große Dateien 2025 miserabel ist.  
Clash Proxy (HK/TW/JP Node) → schnell, weil diese Nodes exzellente Konnektivität zu US AWS haben.

### Empfohlene Lösungen (von schnellste zu langsamste)

1. **Weiterhin Clash (oder v2rayN, Surge, etc.) mit einem Low-Latency HK/TW/JP Node verwenden** — dies ist derzeit der schnellste Weg im chinesischen Festland für FineWeb, RedPajama, The Stack, etc.

2. **HF's offiziellen beschleunigten Endpunkt in China** nutzen (funktioniert für viele Nutzer 2024-2025 ohne Proxy):
   ```bash
   export HF_ENDPOINT=https://hf-mirror.com
   ```
   Dann huggingface-cli oder die datasets library direkt verwenden (nicht wget). Viele Nutzer in China berichten auf diese Weise von 50–200 MB/s, da HF 2025 begonnen hat, mehr Shards auf Aliyun/Tencent Cloud zu cachen.

3. **FastGit + hugger** oder **openi/pkulaw Mirrors** verwenden (einige Shards sind in China gecached):
   Beispiel:
   ```bash
   pip install hugger
   hugger download HuggingFaceFW/fineweb --revision main --include "CC-MAIN-2013-20/*.parquet"
   ```

4. wget + hf-mirror.com weiter verwenden, aber Erzwingen des Routings durch Ihren Clash Proxy (was Sie bereits tun).

### Quick One-Liner zum schnellen Herunterladen beliebiger FineWeb-Shards von Guangzhou
```bash
# Clash HTTP Proxy setzen (Port normalerweise 7890)
export https_proxy=http://127.0.0.1:7890

# Dann aria2 verwenden (viel schneller + Resume-Funktion gegenüber wget)
aria2c -x16 -s16 -k1M "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00000.parquet"
```

Sie erreichen problemlos 30–100 MB/s, abhängig von Ihrem Proxy-Node.

Fazit: Im chinesischen Festland ist 2025 für >1 GB Dateien auf Hugging Face die Verwendung eines HK/TW/JP Proxys fast immer noch schneller als eine direkte Verbindung, selbst bei Nutzung von hf-mirror.com. Das ist einfach die Realität der internationalen Bandbreite aus China derzeit.