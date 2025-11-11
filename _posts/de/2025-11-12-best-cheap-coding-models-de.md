---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Beste günstige Codierungsmodelle über OpenRouter
translated: true
type: note
---

### Beste günstige Modelle für Coding mit Codex CLI über OpenRouter

Basierend auf aktuellen Benchmarks, Nutzerdiskussionen und Modellrankings von 2025 sind hier einige der besten und kostengünstigsten Alternativen zu GPT-5-Codex für Coding-Aufgaben in Codex CLI aufgeführt. GPT-5-Codex ist in der Tat teuer (oft im Bereich von 20-50 $ Input / 60-150 $ Output pro Million Tokens, je nach Anbieter), daher konzentrieren sich diese auf kosteneffiziente Optionen mit starker Coding-Leistung. OpenRarters nutzungsbasiertes Abrechnungsmodell bedeutet, dass Sie nur für verarbeitete Tokens bezahlen, und viele haben kostenlose Kontingente oder sehr niedrige Sätze (unter 1 $ pro Million Tokens kombiniert für Input/Output).

Ich habe Modelle priorisiert, die hohe Werte in Coding-Benchmarks wie SWE-Bench, HumanEval oder Aider erreichen, während sie günstig oder kostenlos sind. Modell-IDs sind für die einfache Verwendung in Ihrer `config.toml` formatiert (z.B. `model = "anbieter/modell-name"`). Für die genauen aktuellen Preise sollten Sie die Modelle-Seite von OpenRouter überprüfen, da die Sätze leicht schwanken können.

#### Top-Empfehlungen:
- **Grok Code Fast (xAI)**  
  Modell-ID: `xai/grok-code-fast`  
  Warum: Führt OpenRarters LLM-Rankings für Coding an, überzeugt durch Geschwindigkeit und agentenbasierte Aufgaben (z.B. Platz 1 in der Internationalen Informatik-Olympiade). Oft kostenlos für die Grundnutzung, was es zum am häufigsten genutzten Modell auf der Plattform macht. Großartig für iterative Coding-Workflows.  
  Preis: Kostenlos oder ~0,50 $/2,00 $ pro 1 Mio. Tokens (Input/Output). Kontext: 128K Tokens.

- **Kat Coder Pro (KwaiPilot)**  
  Modell-ID: `kwaipilot/kat-coder-pro:free`  
  Warum: Spezialisiertes Coding-Modell mit 73,4 % auf SWE-Bench Verified, nahe an den besten proprietären Modellen. Für eine begrenzte Zeit kostenlos, ideal für komplexes Reasoning und Code-Generierung.  
  Preis: Kostenlos (Aktion). Kontext: 256K Tokens, Ausgabe bis zu 32K.

- **DeepSeek Coder V3 (DeepSeek)**  
  Modell-ID: `deepseek/deepseek-coder-v3`  
  Warum: Hervorragendes Preis-Leistungs-Verhältnis mit ~71 % auf Aider-Coding-Scores, stark in Implementierung und Debugging. Wird in Foren häufig für Budget-Coding empfohlen.  
  Preis: Sehr günstig (~0,14 $/0,28 $ pro 1 Mio.). Kontext: 128K Tokens.

- **Llama 4 Maverick (Meta)**  
  Modell-ID: `meta/llama-4-maverick`  
  Warum: Bester im kostenlosen Kontingent für Coding-Qualität und VS Code-Integration (z.B. mit Tools wie RooCode). Leistungsstark bei realen Code-Aufgaben.  
  Preis: Kostenloses Kontingent verfügbar oder niedrige Kosten (~0,20 $/0,80 $ pro 1 Mio.). Kontext: 128K Tokens.

- **Mistral Devstral Small (Mistral)**  
  Modell-ID: `mistral/devstral-small`  
  Warum: Für den Preis optimiert, hoher Durchsatz und gut bei der Code-Implementierung. Wird oft mit größeren Modellen für hybride Workflows kombiniert.  
  Preis: Günstig (~0,25 $/1,00 $ pro 1 Mio.). Kontext: 128K Tokens.

- **Qwen3 235B (Qwen)**  
  Modell-ID: `qwen/qwen3-235b`  
  Warum: Hohe Leistung in Coding-Benchmarks, empfohlen für kostenoptimierte Setups. Verarbeitet großangelegte Code-Projekte gut.  
  Preis: Erschwinglich (~0,50 $/2,00 $ pro 1 Mio.). Kontext: 128K Tokens.

- **Gemini 2.5 Flash (Google)**  
  Modell-ID: `google/gemini-2.5-flash`  
  Warum: Platz 3 in den Rankings, schnell und kostengünstig für iteratives Coding. Gut für multimodale Aufgaben, wenn Ihr Code Datenvisualisierung beinhaltet.  
  Preis: Günstig (~0,35 $/1,05 $ pro 1 Mio.). Kontext: 1 Mio. Tokens.

Diese Modelle sind OpenAI-kompatibel und funktionieren daher nahtlos in Codex CLI, nachdem Sie den Anbieter auf "openrouter" und Ihren API-Schlüssel eingestellt haben. Beginnen Sie mit kostenlosen Modellen wie Grok Code Fast oder Kat Coder zum Testen. Für coding-spezifische Anwendungen sollten Sie auf die SWE-Bench-Scores achten – höher bedeutet besser bei der Lösung realer GitHub-Issues. Wenn Sie mehr Kontext oder Geschwindigkeit benötigen, kombinieren Sie dies mit OpenRarters Routing für automatisches Fallback auf günstigere Modelle.

Zur Integration: Fügen Sie in Ihrer `config.toml` ein Profil hinzu wie `[profiles cheap-coder]` mit `model_provider = "openrouter"` und `model = "eine-der-obigen-IDs"`.

[Top AI-Modelle auf OpenRouter 2025: Leistung vs. Kosten Leitfaden](https://www.teamday.ai/blog/top-ai-models-openrouter-2025)  
[Beste Budget-Coding-LLMs 2025: DeepSeek R1 vs Gemini vs GPT](https://llmx.de/blog/budget-coding-llms-2025/)  
[Was sind die besten auf OpenRouter verfügbaren LLMs für Coding?](https://medium.com/@okreitz/what-are-the-best-llms-available-on-openrouter-to-use-for-coding-with-kilo-ca04e75a84ee)  
[Beste kostenlose KI-Modelle, die Sie auf OpenRouter nutzen können](https://apidog.com/blog/free-ai-models/)  
[Top KI-Coding-Modelle in 2025](https://www.veerotech.net/blog/top-ai-coding-models-in-2025-boost-your-development-workflow-with-these-game-changers/)  
[LLM-Rankings - OpenRouter](https://openrouter.ai/rankings)  
[Top 5 KI-Coding-Modelle im März 2025](https://dev.to/apipie-ai/top-5-ai-coding-models-of-march-2025-5f04)  
[Modelle - OpenRouter](https://openrouter.ai/models)  
[Was ist das beste Coding-Modell auf OpenRouter? - Reddit](https://www.reddit.com/r/RooCode/comments/1kdu7we/whats_the_best_coding_model_on_openrouter/)