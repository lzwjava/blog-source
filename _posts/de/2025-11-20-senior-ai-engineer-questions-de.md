---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Interviewfragen für Senior AI Engineers 2024-2025
translated: true
type: note
---

Hier sind die häufigsten und typischsten Interviewfragen, auf die du für eine **Senior AI/Agent/LLM Engineer** Rolle in 2024–2025 treffen wirst, insbesondere bei Top-Unternehmen (FAANG-tier, AI-Labs wie Anthropic/OpenAI/xAI, Scale-ups wie Adept, Imbue, etc.).

Sie sind nach Kategorie und Schwierigkeitsgrad gruppiert (die meisten sind Senior-Level und erwarten tiefes Verständnis + Produktionserfahrung).

### System Design & Architektur
1. Entwirf ein skalierendes LLM-Inference-Serversystem, das 10k+ QPS mit einer p99-Latenz von <200ms verarbeiten kann.
2. Wie würdest du einen Echtzeit-AI-Agenten entwerfen, der im Web surfen, Tools nutzen und ein Langzeitgedächtnis pflegen kann?
3. Entwirf eine Retrieval-Augmented Generation (RAG) Pipeline von Grund auf (Vektor-DB-Auswahl, Chunking, Reranking, Hybrid-Suche, Evaluation).
4. Wie reduzierst du die Inferenzkosten eines 70B-Modells um das 5–10-fache, während der Qualitätsverlust <2% bleibt?
5. Entwirf einen Evaluierungsrahmen für offene Agenten-Aufgaben (z.B. Online-Shopping, Recherche).
6. Wie würdest du ein Multi-Agenten-System aufbauen, in dem Agenten zusammenarbeiten (Debatte, Hierarchie, etc.)?

### LLM Grundlagen & Erweiterte Anwendung
- Erkläre, wie Attention von Grund auf funktioniert (einschließlich Rotary Positional Embeddings, Grouped-Query Attention, Sliding Window Attention).
- Warum verwendet Llama 3/4 RoPE anstelle von ALiBi? Vor- und Nachteile.
- Leite die Scaling Laws her (Kaplan, Hoffmann "Chinchilla", DeepMind "Emergent Abilities").
- Was verursacht "Lost in the Middle" in Long-Context-Modellen? Wie behebst du es?
- Vergleiche Mixture-of-Experts (MoE) Architekturen (Mixtral, DeepSeek, Grok-1, Qwen-2.5-MoE). Warum ist Aktivierungs-Sparsity in der Praxis schwierig?
- Wie funktioniert Quantisierung (GPTQ, AWQ, SmoothQuant, bitsandbytes) tatsächlich? Trade-offs zwischen 4-Bit, 3-Bit, 2-Bit.
- Was ist der Unterschied zwischen RLHF, DPO, KTO, PPO, GRPO und wann würdest du welches verwenden?

### Agenten & Tool Use
- Wie implementierst du zuverlässiges Tool Calling / Function Calling mit JSON-Modus vs. ReAct vs. OpenAI Tools?
- Erkläre ReAct, Reflexion, ReWOO, Toolformer, DEPS, Chain-of-Verification.
- Wie verhinderst du Endlosschleifen in der Agenten-Ausführung?
- Wie evaluierst du die Agenten-Leistung auf Benchmarks wie GAIA, WebArena, AgentBench?
- Wie würdest du einem Agenten Langzeitgedächtnis hinzufügen (Vektor-Store vs. Key-Value-Store vs. episodisches Gedächtnis)?

### Training, Fine-tuning & Alignment
- Gehe den kompletten Fine-Tuning-Stack durch: LoRA, QLoRA, DoRA, LoftQ, LLaMA-Adapter, IA³.
- Wie funktioniert QLoRA unter der Haube (NF4, Double Quantization, Pagined Optimizers)?
- Du hast 10k hochwertige Instruction-Beispiele und möchtest ein 70B-Modell auf 8×H100s fine-tunen. Gib das genaue Rezept.
- Erkläre Constitutional AI, RLAIF, Self-Critique, Process vs. Outcome Supervision.
- Wie erkennst und milderst du Reward Hacking in RLHF?

### Coding & Implementierung (Live Coding oder Take-Home)
- Implementiere einen einfachen ReAct-Agenten von Grund auf (Python).
- Implementiere effiziente Sliding-Window-Attention mit Flash-Attention-Style-Caching.
- Baue ein einfaches RAG-System mit LangChain / LlamaIndex (die Architektur wird bewertet).
- Optimiere einen Transformer-Forward-Pass für 128k Context (Memory Efficient).
- Schreibe eine benutzerdefinierte PyTorch-Autograd-Funktion für einen neuen Quantization-Kernel.

### ML Grundlagen (fragen sie auch bei Seniors)
- Warum funktioniert AdamW besser als Adam? Leite die Weight-Decay-Formulierung her.
- Erkläre Label Smoothing, Teacher Forcing, Sequence-Level vs. Token-Level Trainingsziele.
- Was ist der Unterschied zwischen BLEU, ROUGE, BERTScore, LLM-as-a-Judge, G-Eval?
- Leite die Transformer-Loss-Funktion her und erkläre, warum wir Padding-Tokens ignorieren.

### Produktion & MLOps
- Wie überwachst du LLM-Outputs in der Produktion (Drift, Toxizität, PII-Leakage, Prompt Injection)?
- Dir fällt auf, dass 5% deiner User das Model jailbreaken. Wie erkennst und verteidigst du das?
- Vergleiche vLLM, TGI, TensorRT-LLM, lmdeploy, Outlines, Guidance hinsichtlich Inferenzgeschwindigkeit.
- Wie führst du kontinuierliches Fine-Tuning / Online Learning sicher durch?

### Behavioral / Erfahrung
- Erzähle mir von dem schwierigsten Produktionsproblem, das du mit LLMs behoben hast.
- Wie hast du ein Agenten-Produkt ausgeliefert, das echte User geliebt haben?
- Beschreibe eine Situation, in der du die Inferenzkosten um >50% reduziert hast.
- Was war die schlimmste Halluzinations-Katastrophe, die du gesehen hast, und wie hast du sie behoben?

### Aktuelle Hot Topics (2025)
- Wie funktionieren Test-Time-Scaling-Methoden (DeepSeek R1, o1-Style Reasoning, Process Reward Models)?
- Vergleiche Chain-of-Thought, Tree-of-Thought, Graph-of-Thought, Process vs. Outcome Reward.
- Was sind die derzeit besten Open-Source Reasoning-Modelle (Llama-3.1-405B, Qwen-2.5-72B-Instruct, DeepSeek-V3, Gemma-2-27B)?
- Gedanken zu Synthetic Data Generation Loops (Self-Refine, STaR, Quiet-STaR, MCTS-basierte Data Synth).

Unternehmen, die derzeit die schwierigsten Fragen stellen: OpenAI, Anthropic, xAI, Adept, Scale AI, Helion, Imbue, Character.AI, Cohere, Mistral.

Bereite dich darauf vor, System-Design am Whiteboard zu entwerfen und auf einem Laptop zu coden (ohne Internet). Die meisten Senior-Interviewprozesse bestehen aus 5–7 Runden mit starkem Fokus auf System-Design und Deep-Dive-Coding.

Viel Glück!