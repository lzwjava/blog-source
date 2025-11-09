---
audio: false
date: 2025-09-13
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Neueste KI-Modelle und ihre Anwendungen
translated: true
type: note
---

Hier ist eine Zusammenfassung dessen, was wir *bis Mitte September 2025* über GPT-5, Gemini 2.5 Pro, GPT-5 mini und deren Nutzung, auch in Copilot / Premium-Modellen, wissen:

---

## GPT-5 (OpenAI)

* **Veröffentlicht**: 7. August 2025. ([OpenAI][1])
* **Was es ist**: Ein vereinheitlichtes LLM mit verbessertem Reasoning, weniger Halluzinationen, besserer Leistung in Coding, Mathematik, Schreiben, Gesundheit, visueller Wahrnehmung usw. Es beinhaltet eine Version "GPT-5 pro" für anspruchsvollere Aufgaben. ([OpenAI][1])
* **Reasoning / Denken**: GPT-5 hat einen internen Mechanismus ("schnell" vs. "tiefergehendes Reasoning") und Benutzer können "GPT-5 thinking" auswählen oder Prompts wie "think hard about this" geben, um eingehenderes Reasoning anzufordern. ([OpenAI][1])
* **Zugangsebenen / Einschränkungen**:

  * Alle ChatGPT-Nutzer haben Zugang (kostenlos + bezahlt). ([OpenAI][1])
  * Kostenlose Nutzer haben eine eingeschränktere Nutzung und werden nach einer bestimmten Nutzung möglicherweise auf eine leichtgewichtige Version ("GPT-5 mini") umgestellt. ([OpenAI][1])
  * Bezahlte Nutzer (Plus, Pro, Team, Enterprise, EDU) erhalten höhere Nutzungslimits; Pro-Nutzer erhalten "GPT-5 pro". ([OpenAI][1])

---

## Gemini 2.5 Pro (Google)

* **Veröffentlichung / Verfügbarkeit**:

  * Gemini 2.5 Pro (experimentell) wurde erstmals am 25. März 2025 angekündigt. ([blog.google][2])
  * Das stabile Gemini 2.5 Pro ("allgemeine Verfügbarkeit") wurde am 17. Juni 2025 veröffentlicht. ([Google Cloud][3])
* **Fähigkeiten**: Es ist das fortschrittlichste Modell von Google in der Gemini-2.5-Familie. Es verfügt über Funktionen wie ein großes Kontextfenster (1 Million Tokens), starkes Reasoning, Coding, mehrsprachige Unterstützung usw. ([blog.google][2])

---

## GPT-5 mini

* **Was / Wann**: GPT-5 mini ist eine leichtgewichtige/schnellere Version von GPT-5, die Mitte August 2025 in GitHub Copilot (Public Preview) verfügbar wurde. ([The GitHub Blog][4])
* **Wo und wie**: Es ist verfügbar in GitHub Copilot Chat (auf github.com), in VS Code, auf GitHub Mobile (iOS/Android). Es wird auch in der Modellauswahl für Benutzer erscheinen. ([The GitHub Blog][4])
* **Premium-Anfragen / Kosten**: Es verbraucht *keine* "Premium-Anfragen" in bezahlten GitHub Copilot-Plänen. Das bedeutet, die Nutzung von GPT-5 mini verbraucht nicht das "Premium-Anfragen"-Kontingent. ([The GitHub Blog][4])

---

## Wie diese in **Copilot / Premium / Microsoft / GitHub** genutzt werden

* **GitHub Copilot**:

  * Alle Copilot-Pläne (einschließlich Free) haben jetzt Zugang zu GPT-5 mini. ([The GitHub Blog][4])
  * GPT-5 (Vollversion) ist nur in bezahlten Copilot-Plänen verfügbar. ([The GitHub Blog][5])
  * Die Modellauswahl ermöglicht es Benutzern, je nach Plan und Organisationseinstellungen, zwischen GPT-5, GPT-5 mini usw. zu wählen. ([The GitHub Blog][4])

* **Microsoft Copilot / Copilot Studio / 365 Copilot**:

  * Microsoft unterstützt die Nutzung von GPT-5 in seinen Copilot-Produkten. Beispielsweise können Entwickler in Copilot Studio GPT-5 auswählen, und es gibt ein automatisches Routing zwischen verschiedenen GPT-5-Varianten (Chat vs. Reasoning) usw. ([Microsoft Developer][6])
  * Premium-Funktionen erfordern im Allgemeinen kostenpflichtige Abonnements. Die Nutzung von GPT-5 oder leistungsstärkerer Modelle mit mehr Reasoning ist oft auf zahlende Nutzer oder Enterprise-Ebenen beschränkt. ([OpenAI][1])

---

Falls gewünscht, kann ich auch **Leistungsvergleiche** (GPT-5 vs. Gemini 2.5 Pro etc.) oder **zukünftige/gerüchteweise Funktionen** recherchieren. Möchtest du das?

[1]: https://openai.com/index/introducing-gpt-5/?utm_source=chatgpt.com "Introducing GPT-5"
[2]: https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/?utm_source=chatgpt.com "Gemini 2.5: Our most intelligent AI model"
[3]: https://cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions?utm_source=chatgpt.com "Model versions and lifecycle | Generative AI on Vertex AI"
[4]: https://github.blog/changelog/2025-08-13-gpt-5-mini-now-available-in-github-copilot-in-public-preview/?utm_source=chatgpt.com "GPT-5 mini now available in GitHub Copilot in public preview"
[5]: https://github.blog/changelog/2025-09-09-openai-gpt-5-and-gpt-5-mini-are-now-generally-available-in-github-copilot/?utm_source=chatgpt.com "OpenAI GPT-5 and GPT-5 mini are now generally available ..."
[6]: https://developer.microsoft.com/blog/gpt-5-for-microsoft-developers?utm_source=chatgpt.com "GPT-5 for Microsoft Developers"