---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Unzensierte große Sprachmodelle erklärt
translated: true
type: note
---

### Was sind unzensierte LLM-Modelle?

Unzensierte Large Language Models (LLMs) sind KI-Systeme, die ohne eingebaute Sicherheitsfilter oder „Guardrails“ entwickelt wurden, die Antworten zu sensiblen, kontroversen oder potenziell schädlichen Themen typischerweise einschränken. Im Gegensatz zu Standardmodellen zielen sie darauf ab, auf *jede* Anfrage – von harmlosen Fragen bis hin zu provokanten, unethischen oder illegalen – ohne Ablehnung, Wertung oder Umleitung zu antworten. Das macht sie attraktiv für Nutzer, die ungefilterte Kreativität, Forschung oder Rollenspiele suchen, birgt aber auch Risiken in Bezug auf Missbrauch.

#### Wie unterscheiden sie sich von zensierten Modellen wie ChatGPT?
Zensierte Modelle (z.B. ChatGPT, Gemini oder Claude) durchlaufen Reinforcement Learning from Human Feedback (RLHF) und Sicherheitstrainings, um sich an ethische Richtlinien, die oft in westlichen Kulturnormen verwurzelt sind, anzupassen. Das führt zu:
- **Ablehnungen**: Sie antworten möglicherweise mit „Ich kann dabei nicht helfen“ auf Anfragen zu Gewalt, expliziten Inhalten oder voreingenommenen Themen.
- **Bias-Minderung**: Antworten sind „politisch korrekt“, können sich aber restriktiv oder kulturell verzerrt anfühlen.

Unzensierte Modelle entfernen diese Schichten und priorisieren rohe Fähigkeiten und Nutzerabsicht. Sie können explizite Geschichten, Schritt-für-Schritt-Anleitungen für riskante Handlungen oder ungeschminkte Meinungen generieren, aber ohne die „Moral“ des Modells, die Grenzen durchsetzt.

#### Wie werden unzensierte LLMs gebaut?
Sie beginnen mit **Foundation-Modellen** – vortrainierten Transformer-Modellen wie Llama, Mistral oder Qwen –, die Text auf der Grundlage riesiger Datensätze vorhersagen. Diese werden dann **fine-getuned**:
- An unzensierten Frage-Antwort-Datensätzen (z.B. durch Entfernen aller „Ablehnungs“-Beispiele).
- Unter Verwendung von Techniken wie LoRA (Low-Rank Adaptation) für Effizienz.
- Anpassung der System-Prompts, um uneingeschränkte Ausgaben zu fördern, manchmal mit „Belohnungen“ für Befolgung.
- **Distillation** verkleinert größere Modelle (z.B. von 70B Parameter auf 7B), erhält dabei aber die Leistung, was sie auf Consumer-Hardware lauffähig macht.

Dieser Prozess erzeugt „abliterated“ oder „dolphinisierte“ Varianten (benannt nach Fine-Tuning-Datensätzen wie Dolphin).

#### Beliebte Beispiele
Sie haben Mistral, DeepSeek, Distill (wahrscheinlich bezogen auf distillierte Varianten) und Qwen erwähnt – dies sind alles starke Basen für unzensierte Fine-Tunes. Hier eine Aufschlüsselung:

- **Unzensierte Mistral-Varianten**:
  - **Dolphin Mistral 7B/24B**: Fine-getuned auf dem Dolphin 2.8-Datensatz für Null-Ablehnungen. Großartig für Rollenspiele, Coding und kreatives Schreiben. Unterstützt bis zu 32K Kontext-Tokens.
  - **Mistral 7B Dolphin Uncensored**: Ein leichtes (7B Parameter) Modell, das vollständig ungefiltert ist und oft lokal via Ollama läuft.

- **Unzensierte DeepSeek-Varianten**:
  - **DeepSeek-R1-Distill-Qwen Series** (z.B. 1.5B, 7B, 14B, 32B): Distilliert aus DeepSeeks massivem R1-Modell in Qwen-Basen. Diese glänzen in Mathematik/Logik (übertreffen in manchen Benchmarks GPT-4o) und gibt es in unzensierten Editionen wie UncensoredLM-DeepSeek-R1-Distill-Qwen-14B. Ideal für das Lösen von Problemen ohne Filter.

- **Unzensierte Qwen-Varianten**:
  - **Liberated Qwen**: Ein früher unzensierter Fine-Tune, der sich strikt an Prompts hält und in Benchmarks wie MT-Bench und HumanEval hoch punktet.
  - **Qwen 2.5-32B Uncensored**: Ein 32B-Parameter-Biest für anspruchsvolle Aufgaben; zugänglich via APIs oder lokalen Läufen.
  - **Qwen3 8B Uncensored**: Kleiner, effizient für Bildung/Forschung, mit „abliterated“-Versionen für totale Recall- und Coding-Fähigkeiten.

Weitere nennenswerte Beispiele sind Llama2-Uncensored oder Nous-Hermes (distilliert aus Llama), aber Ihre Beispiele passen zu den Open-Source-Kraftpaketen von Mistral AI, DeepSeek AI und Alibabas Qwen-Serie.

#### Vor- und Nachteile

| Aspekt | Vorteile | Nachteile |
|--------|------|------|
| **Flexibilität** | Beantwortet alles; großartig für unzensiertes Storytelling, unvoreingenommene Analyse oder Edge-Case-Tests. | Risiko schädlicher Ausgaben (z.B. Fehlinformationen, Hassrede oder illegale Ratschläge). |
| **Leistung** | Oft schneller/günstiger lokal lauffähig; weniger kulturelle Voreingenommenheit. | Kann ohne Sicherheitsnetze stark „halluzinieren“; schwieriger zu kontrollieren. |
| **Zugänglichkeit** | Kostenlos/Open-Source auf Hugging Face; läuft auf Laptops via Ollama oder LM Studio. | Ethische/rechtliche Probleme – Missbrauch könnte Gesetze verletzen; nicht für Kinder/Arbeitsplätze. |

#### Ethische Überlegungen
Obwohl empowernd, verstärken diese Modelle den Dual-Use-Charakter der KI: nützlich für freie Meinungsäußerung oder Red-Teaming-Sicherheitstests, aber gefährlich, wenn sie weaponized werden (z.B. für Betrug oder Extremismus). Entwickler betonen verantwortungsvolle Nutzung, aber das „Uncensored“-Label lädt zu Kontroversen ein – überprüfen Sie immer die Ausgaben.

#### Wie man darauf zugreift
- **Lokale Läufe**: Verwenden Sie Ollama (z.B. `ollama run dolphin-mistral`) oder Hugging Face für Downloads. Benötigt eine brauchbare GPU (z.B. 8GB VRAM für 7B-Modelle).
- **Cloud/APIs**: Plattformen wie OpenRouter oder Groks Ecosystem hosten Free-Tiers; Jarvislabs.ai für GPU-Mieten.
- Fangen Sie klein an: Probieren Sie Dolphin Mistral auf Ihrem Handy via Apps wie Private LLM.

Für tiefergehende Einblicke, sehen Sie sich diese Ressourcen an:

[Uncensored LLM Models: A Complete Guide](https://docs.jarvislabs.ai/blog/llm_uncensored)  
[DeepSeek-R1 Distilled Models Explained](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d)  
[Dolphin Mistral Uncensored Guide](https://www.youtube.com/watch?v=yqMBI_Q0_Yc)  
[Liberated Qwen Overview](https://venturebeat.com/ai/meet-liberated-qwen-an-uncensored-llm-that-strictly-adheres-to-system-prompts)  
[Uncensored Qwen 2.5-32B Trial](https://eduardo-rogers.medium.com/you-can-try-uncensored-qwen-2-5-32b-model-here-3560e31cc3b5)