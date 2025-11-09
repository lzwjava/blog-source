---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Effiziente LLM-Inferenz mit vLLM
translated: true
type: note
---

### vLLM: Effiziente LLM-Inferenz und Bereitstellung

vLLM ist eine Open-Source-Bibliothek für schnelle, speichereffiziente Inferenz und Bereitstellung von Large Language Models (LLMs). Ursprünglich im Sky Computing Lab der UC Berkeley entwickelt, ist es heute ein community-getriebenes Projekt, das weit verbreitet in der Produktion für die Bereitstellung von LLMs wie Llama oder GPT-Varianten eingesetzt wird. Seine Kerninnovation ist **PagedAttention**, eine Technik, die den Key-Value (KV) Cache-Speicher wie virtuelle Speicherseiten behandelt, Verschwendung reduziert und durch dynamische Zuweisung nicht zusammenhängender Blöcke einen höheren Durchsatz ermöglicht.

#### So funktioniert es
- **Continuous Batching**: Im Gegensatz zu traditionellen Systemen, die auf vollständige Batches warten, fügt vLLM Anfragen dynamisch hinzu/entfernt sie während der Ausführung, um Leerlaufzeiten der GPU während des Decodierens zu minimieren.
- **Speicherverwaltung**: PagedAttention vermeidet Fragmentierung im KV-Cache (der mit der Sequenzlänge wächst) und unterstützt längere Kontexte ohne OOM-Fehler.
- **Optimierte Ausführung**: Verwendet CUDA/HIP Graphs für schnellere Kernel-Starts, ist integriert mit FlashAttention/FlashInfer für Attention-Berechnungen und unterstützt Quantisierung (z.B. AWQ, GPTQ, FP8), um den Speicherverbrauch um bis zu 4x zu reduzieren.
- **Erweiterte Funktionen**: Beinhaltet spekulatives Decoding (zum Erraten und Verifizieren von Tokens), Chunked Prefill (für lange Eingaben), Multi-LoRA (Anpassen von Modellen on-the-fly) und verteilten Parallelismus (Tensor, Pipeline, Expert).

vLLM bietet einen OpenAI-kompatiblen API-Server, integriert sich nahtlos mit Hugging Face Modellen und läuft auf verschiedener Hardware (NVIDIA/AMD/Intel GPUs, TPUs, CPUs). Es ist ideal für Hochdurchsatz-Szenarien und erreicht in Serving-Benchmarks 2-10x Beschleunigung gegenüber Baselines wie Hugging Face Transformers.

#### Wichtige Anwendungsfälle
- Online-Bereitstellung für Chatbots oder APIs mit Streaming-Ausgaben.
- Offline-Batch-Inferenz für Aufgaben wie Zusammenfassung.
- Skalierung auf Multi-GPU-Cluster ohne benutzerdefinierte Infrastruktur.

### Ray: Einheitliches Framework für die Skalierung von KI- und Python-Apps

Ray ist ein Open-Source-Framework für verteiltes Rechnen, das es einfach macht, Python-Code – insbesondere AI/ML-Workloads – von einem einzelnen Rechner auf massive Cluster zu skalieren. Entwickelt von Anyscale (mit Ursprüngen an der UC Berkeley), abstrahiert es die Komplexität verteilter Systeme wie Scheduling, Fehlertoleranz und Orchestrierung, sodass sich Entwickler auf die Logik konzentrieren können.

#### Hauptkomponenten
- **Ray Core**: Das Fundament – Pythonische Primitive für Tasks (parallele Funktionen), Actors (zustandsbehaftete Dienste) und Objects (verteilte Datenteilung). Es übernimmt automatisch Autoscaling, Wiederholungen und Ressourcenzuteilung.
- **Ray AI Libraries**: Domänenspezifische Tools, die auf Core aufbauen:
  - **Ray Data**: Skalierbarer ETL für die Vorverarbeitung von Datensätzen.
  - **Ray Train**: Verteiltes Training mit Integrationen (PyTorch, TensorFlow, Hugging Face).
  - **Ray Tune**: Hyperparameter-Optimierung im großen Maßstab.
  - **Ray Serve**: Modellbereitstellung für Inferenz, mit Routing, Batching und A/B-Testing.
  - **RLlib**: Toolkit für Reinforcement Learning.
- **Ray Clusters**: Verwaltete Infrastrukturschicht für die Bereitstellung in Clouds (AWS, GCP), Kubernetes oder On-Premise, mit Autoscaling basierend auf Nachfrage.

#### So funktioniert es
Ray läuft als Daemon auf Knoten und bildet einen Cluster mit einem Head-Knoten für die Koordination. Funktionen werden mit `@ray.remote` dekoriert für Parallelität, und Ray verteilt die Ausführung auf CPUs/GPUs. Für ML übernehmen Bibliotheken wie Serve HTTP-Endpunkte und Lastverteilung, während Core für fehlertolerantes Skalieren sorgt (z.B. Neustart fehlgeschlagener Tasks).

#### Wichtige Anwendungsfälle in ML/AI
- End-to-End-Pipelines: Datenladen → Training → Optimierung → Bereitstellung.
- Hyperparameter-Sweeps auf Hunderten von GPUs.
- Echtzeit-Inferenz-Flotten, wie in Empfehlungssystemen.
- Benutzerdefinierte verteilte Apps, z.B. Simulationen.

Rays Stärke ist seine einheitliche API: Einmal schreiben, überall skalieren, mit weniger Boilerplate-Code im Vergleich zu Spark oder Dask.

### Beziehung zwischen vLLM und Ray
In Systemen wie SLOs-Serve (aus unserer früheren Diskussion) übernimmt vLLM das Low-Level-LLM-Batching/Inferenz, während Ray Multi-Replica-Bereitstellungen orchestriert und Anfragen zur Lastbewältigung und Skalierung über Knoten hinweg routet.

[vLLM-Dokumentation](https://docs.vllm.ai/en/latest/)  
[Ray-Dokumentation](https://docs.ray.io/en/latest/ray-overview/index.html)