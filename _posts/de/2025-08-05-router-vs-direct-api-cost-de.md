---
audio: false
generated: true
image: false
lang: de
layout: post
title: OpenRouter vs. direkte API-Kosten
translated: true
type: note
---

Ja, die Verwendung von OpenRouter-APIs für den Zugriff auf die gleichen Modelle ist in der Regel teurer als die direkte Nutzung der offiziellen APIs von Anbietern wie DeepSeek, Mistral, Google (für Gemini) oder xAI (für Grok). OpenRouter gibt an, die Preise des zugrunde liegenden Anbieters ohne Aufschlag auf die Inferenzkosten selbst weiterzugeben, berechnet jedoch zusätzliche Gebühren, die die Gesamtkosten erhöhen:

- Eine Gebühr von 5,5 % (mit einem Minimum von 0,80 $) beim Kauf von Credits über Standardzahlungsmethoden, plus zusätzliche 5 % für Kryptozahlungen.
- Selbst wenn Sie Ihre eigenen API-Schlüssel (BYOK) für unterstützte Anbieter mitbringen, zieht OpenRouter eine Gebühr von 5 % (basierend auf ihren geschätzten Modellkosten) von Ihren OpenRouter-Credits ab.

Diese Gebühren machen OpenRouter effektiv um 5–5,5 % teurer als der direkte Weg, zuzüglich etwaiger fester Mindestbeträge, abhängig von Ihrer Nutzung und Zahlungsmethode. Der direkte Zugriff vermeidet diese Extras, da Sie nur die Token-Preise des Anbieters zahlen.

### Kostenvergleich Beispiele
Hier ist ein grober Vergleich basierend auf verfügbaren Preisdaten (in USD pro Million Tokens; beachten Sie, dass die Sätze je nach Modellversion, Tageszeit, Caching oder Region variieren können – überprüfen Sie immer die offiziellen Seiten für die neuesten Details). Die Basis-Token-Preise von OpenRouter entsprechen denen der Anbieter (Durchreichung), addieren aber die oben genannten Gebühren.

- **DeepSeek**:
  - Direkt: Input ~$0,14–$0,55 (Cache Treffer/Fehlschlag), Output ~$1,10–$2,19 (variiert je nach Modell und Rabattperioden).
  - OpenRouter: Gleiche Basissätze + 5–5,5 % Gebühren.

- **Mistral**:
  - Direkt: Input ~$2,00 (für Large 2), Output ~$6,00 (geschätzt basierend auf gemischten Sätzen; ältere Modelle wie Small waren ~$0,15 Input/$0,50 Output).
  - OpenRouter: Gleiche Basissätze + 5–5,5 % Gebühren.

- **Gemini (Google)**:
  - Direkt: Variiert stark je nach Modell (z.B. Gemini 1.5 Pro: Input $1,25–$2,50, Output $5,00–$10,00; Gemini 1.5 Flash: Input $0,075–$0,15, Output $0,30–$0,60).
  - OpenRouter: Gleiche Basissätze + 5–5,5 % Gebühren (BYOK wird für Google möglicherweise unterstützt).

- **Grok (xAI)**:
  - Details zur Grok-API-Preisgestaltung und zum Zugriff finden Sie unter https://x.ai/api. Basierend auf öffentlichen Informationen liegen die Sätze bei etwa Input $3,00/Output $15,00 für Grok-3/Grok-4, oder Input $0,30/Output $0,50 für Grok-3-mini.
  - OpenRouter: Gleiche Basissätze + 5–5,5 % Gebühren (BYOK wird für xAI typischerweise nicht erwähnt).

Bei hohem Nutzungsvolumen summieren sich die prozentualen Gebühren schnell. Für geringe Nutzung oder Tests könnte der Unterschied minimal sein, aber der direkte Zugriff ist immer noch günstiger. Der Wert von OpenRouter liegt in seiner vereinheitlichten API und Routing-Funktionen, was die zusätzlichen Kosten für den Komfort rechtfertigen könnte.

[OpenRouter FAQ](https://openrouter.ai/docs/faq)  
[DeepSeek API Preisgestaltung](https://api-docs.deepseek.com/quick_start/pricing)  
[Mistral AI Preisgestaltung](https://mistral.ai/pricing)  
[Google Gemini API Preisgestaltung](https://ai.google.dev/pricing)  
[xAI API](https://x.ai/api)  
[Mistral Large 2 Analyse](https://artificialanalysis.ai/models/mistral-large-2)  
[DeepSeek Preisgestaltung Leitfaden](https://team-gpt.com/blog/deepseek-pricing/)