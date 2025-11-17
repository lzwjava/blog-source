---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Allgemeine Modelle übertreffen domänenspezifische KI
translated: true
type: note
---

Du stellst eine sehr gute und zeitgemäße Frage. Das Pendel in der KI-Branche ist tatsächlich zurück zu **allgemeinen Foundation-Modellen** geschwungen, die für die meisten Anwendungsfälle sinnvoller (und wirtschaftlich dominanter) sind als eng fokussierte, domänenspezifische Modelle. Hier ist der Grund, warum der Ansatz vom Typ „BloombergGPT / Med-PaLM / FinanceGPT / LawGPT“ in den Jahren 2024–2025 an Attraktivität verloren hat:

### 1. Datenkontamination und Überlappung sind massiv
Moderne Vor-Trainings-Korpora (RefinedWeb, FineWeb, Dolma, RedPajama v2, etc.) enthalten bereits enorme Mengen an Text aus den Bereichen Finanzen, Recht, Medizin und Code. Zum Beispiel:
- Common Crawl allein enthält Milliarden von SEC-Einreichungen, Gerichtsdokumenten, GitHub-Repositories, arXiv-Papers, Finanznachrichten etc.
- Ein allgemeines Modell, das mit 10–30B Token trainiert wurde, sieht fast genauso viele hochwertige Finanz-/Rechts-/Code-Daten wie ein „domänenspezifisches“ Modell, das mit 1B Token handverlesener Domänendaten trainiert wurde.

Ergebnis: Die Leistungslücke zwischen einem 100B–400B Allzweckmodell und einem 100B „FinanceGPT“ hat sich dramatisch verkleinert. BloombergGPT (2023) übertraf allgemeine Modelle bei Finanzaufgaben um ~10–20 %, aber Llama 3.1 405B oder Qwen2.5 72B erreichen heute oft die Werte von BloombergGPT oder übertreffen sie, ohne domänenspezifisches Training.

### 2. Domänengrenzen sind verschwommen und in Bewegung
Du hast es bereits perfekt auf den Punkt gebracht: Finanzen + KI, Krypto + Recht, Biotech + Finanzen, Programmierung + Mathematik + Physik etc. Wissen ist heute stark vernetzt.
- Ein reines „Finanz“-Modell scheitert bei DeFi/Smart-Contract-Fragen, weil es nicht genug Code gesehen hat.
- Ein reines „Rechts“-Modell tut sich schwer mit KI-Regulierungsfällen, die ein Verständnis von Transformern und Trainingsdaten erfordern.
- Ein reines „Programmier“-Modell ist schlecht im Schreiben von Handelsalgorithmen, die Wissen über Marktmikrostruktur benötigen.

Allgemeine Modelle bewältigen diese zusammengesetzten Domänen natürlich, weil sie alles vermischt gesehen haben – genau wie in der realen Welt.

### 3. MoE macht Spezialisierung fast kostenlos
Mixture-of-Experts (Mixtral, DeepSeek-V3, Qwen2.5-MoE, Grok-1.5, etc.) betreibt bereits intern ein leichtgewichtiges Domain-Routing. Einige Experten lernen, häufiger bei Code zu aktivieren, andere bei Finanzen, wieder andere bei biomedizinischen Texten usw., ohne dass jemand die Daten explizit trennen müsste. Man erhält den größten Teil des Vorteils von domänenspezifischem Routing ohne zusätzlichen Engineering- oder Vertriebsaufwand.

### 4. Wirtschaftlichkeit und Distribution haben sich geändert
Denken im Jahr 2023: „Trainiere ein 50B FinanceGPT auf proprietären Daten → verkaufe API-Zugang an Banken für 50–200 $ pro Million Token.“
Realität im Jahr 2025:
- Banken können einfach Claude 3.5 / GPT-4o / Llama 405B + RAG auf ihren internen Dokumenten verwenden und erreichen damit 95–98 % der Leistung für 1/50 der Kosten.
- Open-Source-Spitzenmodelle (Llama 3.1 405B, Qwen2.5 72B, DeepSeek-V3) sind jetzt gut genug, dass die meisten Unternehmen Fine-Tuning oder Context Injection bevorzugen, anstatt einen hohen Aufpreis für ein geschlossenes Domänenmodell zu zahlen.
- Hosting- und Inferenzkosten für ein dediziertes 70B–400B Domänenmodell sind sehr hoch, wenn die Kundenbasis klein ist.

### 5. Post-Training (SFT + RL) schließt fast die gesamte verbleibende Lücke
Selbst wenn ein allgemeines Modell nach dem Vor-Training bei reinem Domänenwissen leicht zurückliegt, werden 500–5000 hochwertige synthetische oder von Menschen geschriebene Beispiele im Supervised Fine-Tuning + DPO/RLHF, die auf diese Domäne abgestimmt sind, es trotzdem auf State-of-the-Art-Niveau bringen. Dies ist 100-mal billiger und schneller als das Sammeln und Bereinigen von Terabytes an Domänen-Vor-Trainingsdaten.

### Wann domänenspezifische Modelle noch sinnvoll sind (die wenigen verbleibenden Fälle)
- Extrem regulierte oder sicherheitskritische Umgebungen, in denen buchstäblich keine Daten an OpenAI/Anthropic/Meta gesendet werden dürfen (einige Verteidigungsbereiche, einige Zentralbanken, einige Gesundheitssysteme).
- Wenn man über massive proprietäre Daten verfügt, die sich wirklich nicht im öffentlichen Internet befinden (z. B. Billionen privater Handelsaufzeichnungen, Jahrzehnte interner Rechtsgutachten) und man nachweisen kann, dass den allgemeinen Modellen Signale fehlen.
- Winzige Modelle, die On-Device oder in luftgekoppelten Systemen laufen (z. B. Legal Co-Pilot, der vollständig innerhalb der Firewall einer Anwaltskanzlei mit <7B Parametern läuft).

Für 95 %+ der kommerziellen Anwendungsfälle im Jahr 2025 lautet die Antwort jedoch:
Allgemeines Spitzenmodell (offen oder geschlossen) + domänenspezifisches Post-Training / RAG / Tool Use >> dediziertes, domänenvortrainiertes Modell.

Ja, du liegst also genau richtig: Die Essenz des Transformers ist die Vorhersage von Text, unabhängig von der Domäne, und das Problem der Datenvermischung + Skalierungsgesetze + MoE + günstiges Post-Training haben rein domänenspezifische Modelle größtenteils zu einem Phänomen der Jahre 2022–2023 gemacht.