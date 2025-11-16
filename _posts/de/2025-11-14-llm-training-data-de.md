---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Beschaffung von LLM-Trainingsdaten
translated: true
type: note
---

### Wie man große Textdaten für das Training von Sprachmodellen erhält

Das Training großer Sprachmodelle (LLMs) erfordert riesige Mengen an vielfältigen, hochwertigen Textdaten – oft Billionen von Tokens aus Büchern, Websites, Code und mehr. Die größten Herausforderungen sind der Umfang (Terabytes bis Petabytes), die Qualität (Herausfiltern von Rauschen, Duplikaten und minderwertigen Inhalten) und die Legalität (Respektieren von Urheberrechten, Nutzung von Public Domain oder lizenzierten Daten). Hier ist eine Schritt-für-Schritt-Anleitung zur Beschaffung:

1.  **Beginnen Sie mit öffentlichen Web-Crawls**: Diese bilden das Rückgrat der meisten LLM-Trainings. Sie erfassen Momentaufnahmen des Internets.
    - Filtern Sie sauberen Text mit Tools wie CC-Net oder Dedup (Python-Bibliotheken über Hugging Face).
    - Verarbeiten Sie die Daten in Stücken, um die Größe zu bewältigen – nutzen Sie Cloud-Speicher (z.B. AWS S3) für Downloads.

2.  **Verwenden Sie kuratierte Datensätze**: Vorgefilterte Sammlungen von Forschungsgruppen. Laden Sie sie über APIs oder direkte Links herunter.
    - Konzentrieren Sie sich auf mehrsprachige, domänenspezifische Teilmengen (z.B. Code, Wissenschaft), die Ihren Bedürfnissen entsprechen.
    - Tools wie die Hugging Face `datasets`-Bibliothek machen das Laden einfach: `from datasets import load_dataset`.

3.  **Ergänzen Sie mit domänenspezifischen Quellen**:
    - Bücher: Project Gutenberg (Public Domain).
    - Wikipedia: Sprach-Dumps.
    - Code: GitHub-Archive (über BigCode).
    - Generieren Sie synthetische Daten: Verwenden Sie bestehende Modelle (z.B. über die OpenAI API), um Reasoning-Ketten zu erstellen, bereinigen Sie diese jedoch, um Kontamination zu vermeiden.

4.  **Rechtliche und ethische Tipps**:
    - Bleiben Sie bei offenen Lizenzen (z.B. CC-BY, MIT).
    - Deduplizieren Sie (Tools wie MinHash) und entfernen Sie PII (persönliche Informationen).
    - Beginnen Sie für benutzerdefiniertes Training klein (z.B. Fine-Tuning mit 1-10 GB), bevor Sie hochskalieren.
    - Rechenkosten: Rechnen Sie mit Hunderten von GPU-Stunden selbst für bescheidenes Training; nutzen Sie Colab oder RunPod für Tests.

5.  **Verarbeitungspipeline**:
    - Download → Bereinigen (HTML, Nicht-Text entfernen) → Tokenisieren (z.B. mit TikToken) → Trainieren.
    - Bibliotheken: Pandas für Stichproben, spaCy/NLTK für die Vorverarbeitung.

Öffentliche Datensätze sind kostenlos und massiv – ideal für Hobbyisten oder Forscher. Für den Produktionseinsatz lizenzieren Unternehmen oft proprietäre Daten.

### Trainingsdatenquellen für spezifische Modelle

Proprietäre Modelle wie die von OpenAI, Anthropic und DeepSeek halten ihre genauen Rezepte aus Wettbewerbsgründen geheim, haben aber über Papiere, Blogs und Leaks grobe Details geteilt. Open-Source-Modelle (z.B. Llama, Mistral) sind transparenter und veröffentlichen oft Datensatz-Blaupausen.

-   **OpenAI's GPT-Modelle (z.B. GPT-4o)**:
    Sie trainieren mit einer Mischung aus öffentlich verfügbaren Internetdaten (gefilterte Web-Crawls), Büchern, Artikeln und Code. Frühe GPTs nutzten Common Crawl intensiv; spätere legen Wert auf hochwertige STEM/Coding-Quellen. Gesamt: Billionen von Tokens, mit starker Deduplizierung. Sie beinhalten auch lizenzierte Daten und Nutzerinteraktionen (mit Opt-Outs). Keine vollständige Veröffentlichung, aber im Wesentlichen "das gesamte Internet" – gescrapt, gefiltert und erweitert.

-   **Anthropic's Modelle (z.B. Claude 3.5)**:
    Fokus auf sicheren, hilfreichen Daten: Öffentlicher Webtext, Bücher und synthetische Beispiele, die für Alignment generiert wurden (z.B. Constitutional AI). Sie nutzen User-Chats von Claude (Opt-Out verfügbar) und RLHF-Datensätze wie HH-RLHF. Betonung auf vielfältigen, nicht-toxischen Quellen; einige Kontroversen über gescrapte YouTube-Transkripte. Gesamtumfang: Ähnliche Billionen, aber stärker für Ethik kuratiert.

-   **DeepSeek-Modelle (z.B. DeepSeek-V3, R1)**:
    Chinesische, quasi-offene Modelle, die einfache Webseiten, E-Books und Code-Repos verwenden. V3 wurde mit 14,8T Tokens vortrainiert, ohne absichtliche synthetische Daten, aber R1 fügt 600K synthetische Reasoning-Beispiele via Rejection Sampling (generiert durch vorherige Modelle) hinzu. Quellen: Web-Crawls + technische Dokumentationen; proprietäre Mischung, aber in Papers transparent.

-   **Open-Source-Modelle (z.B. Llama 3, BLOOM, GPT-J)**:
    Diese nutzen explizit öffentliche Datensätze wie The Pile (800 GB mehrsprachige Mischung), C4 (Colossal Clean Crawled Corpus, 750 GB englischer Webtext) oder OSCAR (mehrsprachiger Common Crawl). BLOOM verwendete ROOTS (1,6 TB, 46 Sprachen). Sie vermeiden proprietäre Daten und konzentrieren sich auf Reproduzierbarkeit – prüfen Sie die Modellkarten auf Hugging Face für genaue Aufschlüsselungen.

Kurz gesagt: Alle verlassen sich auf Web-daten in großem Maßstab, aber Proprietäre fügen Filterung/Lizenzierung/Synthetisches für Qualität hinzu. Open-Source setzt auf community-kurierte öffentliche Daten.

### Download-Links für große öffentliche Textdatensätze

Hier sind die besten kostenlosen, herunterladbaren Quellen (Größen ungefähr; auf Updates prüfen). Beginnen Sie mit Teilmengen, wenn der Speicher begrenzt ist.

-   **Common Crawl**: Monatliche Web-Snapshots (Petabytes insgesamt). Filtern mit CC-MAIN-Indexen. [Common Crawl Archives](https://commoncrawl.org/get-started)
-   **The Pile**: 800 GB vielfältiger englischer Text (Bücher, Code, arXiv usw.). [EleutherAI The Pile auf Hugging Face](https://huggingface.co/datasets/EleutherAI/pile)
-   **C4 (Colossal Clean Crawled Corpus)**: 750 GB bereinigter englischer Webtext (verwendet für T5/GPT). [TensorFlow Datasets C4](https://www.tensorflow.org/datasets/catalog/c4)
-   **OSCAR (Open Super-large Crawled Aggregated coRpus)**: Mehrsprachiger Webtext (22 Sprachen, ~10 TB). [OSCAR auf Hugging Face](https://huggingface.co/datasets/oscar-corpus/OSCAR-2201)
-   **Wikipedia Dumps**: Volltextextrakte (Englisch: ~20 GB). [Wikimedia Downloads](https://dumps.wikimedia.org/enwiki/latest/)
-   **BooksCorpus/OpenWebText**: 11 GB Bücher + 40 GB Reddit/Web (GPT-2-Ära). [OpenWebText auf GitHub](https://github.com/jcpeterson/openwebtext)
-   **RedPajama**: 1T+ Tokens, repliziert aus Llama-Papers. [TogetherAI RedPajama auf HF](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T)
-   **LLMDataHub**: Kuratierte Liste von 100+ Datensätzen (Chat, Code usw.). [GitHub LLMDataHub](https://github.com/Zjh-819/LLMDataHub)

Für mehr, durchsuchen Sie den Hugging Face Datasets Hub: [Hugging Face Datasets](https://huggingface.co/datasets). Überprüfen Sie immer die Lizenzen!

**Referenzen**  
[Wie ChatGPT und unsere Foundation Models entwickelt werden](https://help.openai.com/en/articles/7842364-how-chatgpt-and-our-language-models-are-developed)  
[What GPT-oss Leaks About OpenAI's Training Data](https://www.lesswrong.com/posts/iY9584TRhqrzawhZg/what-gpt-oss-leaks-about-openai-s-training-data)  
[Anthropic Will Use Claude Chats for Training Data](https://www.wired.com/story/anthropic-using-claude-chats-for-training-how-to-opt-out/)  
[Anthropic's HH-RLHF Dataset](https://huggingface.co/datasets/Anthropic/hh-rlhf)  
[What went into training DeepSeek-R1?](https://epoch.ai/gradient-updates/what-went-into-training-deepseek-r1)  
[The Complete Guide to DeepSeek Models](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond)  
[LLMDataHub: Awesome Datasets for LLM Training](https://github.com/Zjh-819/LLMDataHub)  
[Open-Sourced Training Datasets for LLMs](https://kili-technology.com/large-language-models-llms/9-open-sourced-datasets-for-training-large-language-models)  
[LLM Training Data: The 8 Main Public Data Sources](https://oxylabs.io/blog/llm-training-data)