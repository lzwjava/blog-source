---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Alternativen zu kleinen hochwertigen Datensätzen
translated: true
type: note
---

Ja, OpenWebText ist riesig (~9B Tokens, 17GB uint16-Datei) und die Vorverarbeitung dauert lange und benötigt viel Speicherplatz. Hier sind viel kleinere, hochwertige Alternativen, die häufig für Tests, Debugging oder das schnelle Training kleiner Modelle verwendet werden:

| Datensatz                 | Ungefähre Tokens | Endgröße .bin (uint16) | Warum er beliebt ist                                                                 | Wie man ihn schnell erhält                                  |
|---------------------------|------------------|------------------------|--------------------------------------------------------------------------------------|-------------------------------------------------------------|
| **OpenWebText-10k**       | ~40M             | ~80MB                  | Exakt gleiche Verteilung wie das vollständige OpenWebText, nur die ersten 10k Dokumente | `load_dataset("openwebtext", split="train[:10k]")`          |
| **OpenWebText-100k**      | ~400M            | ~800MB                 | Immer noch sehr repräsentativ, Tokenisierung dauert nur wenige Minuten               | `split="train[:100k]"`                                      |
| **FineWeb-Edu Sample**    | 50M–1B           | 100MB–2GB              | Höhere Qualität als OWT (LLama-style Filterung), derzeit sehr beliebt                | `load_dataset("HuggingFaceFW/fineweb-edu", name="sample-10BQ", split="train")` → ~50M Tokens |
| **Shakespeare**           | ~1M              | ~2MB                   | Klassischer, winziger Datensatz, perfekt für schnelle Plausibilitätschecks           | `load_dataset("tiny_shakespeare")` oder einfach die einzelne .txt-Datei herunterladen |
| **PG-19 (Bücher)**        | Vollständig 2.8B | ~5.5GB                 | Sehr saubere Public-Domain-Bücher, man kann aber auch nur einen Ausschnitt nehmen    | `load_dataset("pg19", split="train[:5%]")` → ~140M Tokens   |
| **C4 (Teilmenge)**        | variabel         | variabel               | Common Crawl, bereinigt vom T5-Team, nur Englisch                                    | `load_dataset("allenai/c4", "en", split="train[:1%]")` streaming=True |
| **RedPajama Sample**      | 5M–200M          | 10MB–400MB             | Mix aus Quellen (CommonCrawl, Wikipedia, Bücher, etc.), gleiche Rezeptur wie LLaMA   | `load_dataset("togethercomputer/RedPajama-Data-1T", name="sample", split="train")` |

### Meine persönlichen Empfehlungen je nach Ziel

1. Möchten Sie etwas, das in < 5 Minuten läuft und überall passt → **tiny_shakespeare**  
   (nanoGPT-Nutzer lieben diesen)

2. Möchten Sie etwas, das immer noch "echter Internet-Text" ist, aber winzig → OpenWebText erste 10k Dokumente  
   ```python
   dataset = load_dataset("openwebtext", split="train[:10000]")
   ```

3. Möchten Sie den hochwertigsten kleinen Datensatz derzeit (2025) → FineWeb-Edu 10B-Token Sample  
   (~50M Tokens, aber viel sauberer als OWT, nahezu identische Qualität zu der, die Top-Labore verwenden)

   ```python
   dataset = load_dataset(
       "HuggingFaceFW/fineweb-edu",
       name="sample-10BQ",  # 10 Milliarden Tokens gesampelt, ~50M pro Shard, wenn man einen Ausschnitt nimmt
       split="train"
   )
   ```

4. Möchten Sie etwas < 500MB, das aber dennoch vielfältig ist → RedPajama Sample (200M Tokens Version)  
   ```python
   dataset = load_dataset("togethercomputer/RedPajama-Data-1T", name="sample-200M", split="train")
   ```

Alle diese können ohne jegliche Änderungen in Ihr exakt gleiches Vorverarbeitungsskript übernommen werden (ersetzen Sie einfach die load_dataset-Zeile).

Für schnelle Iterationen behalte ich normalerweise drei Binärdateien auf der Festplatte:
- `shakespeare.bin`   (~2MB)   → Overfit-Tests
- `owt_10k.bin`       (~80MB)  → Debugging von neuem Code
- `fineweb_edu_1B.bin` (~2GB) → Training kleiner Modelle

Lassen Sie mich wissen, wie groß es sein soll, und ich kann Ihnen die exakte One-Liner-Zeile geben!