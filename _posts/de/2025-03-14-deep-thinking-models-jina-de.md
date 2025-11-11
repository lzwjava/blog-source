---
audio: false
generated: true
lang: de
layout: post
title: Tiefdenkende Modelle
translated: true
type: note
---

Diese Informationen basieren auf einer Abfrage von https://search.jina.ai.

---

Hier ist eine Aufschlüsselung von Deep-Reasoning-Modellen und deren API-Verfügbarkeit, die entwickelt wurde, um ein tieferes Verständnis zu vermitteln und Ihnen bei der Auswahl des richtigen Modells für Ihre Bedürfnisse zu helfen:

*   **OpenAI o-series Modelle (o1, o3-mini, etc.)**: Diese Modelle, die über den Azure OpenAI Service verfügbar sind [^1], sind für komplexes Reasoning konzipiert und zeichnen sich in den Bereichen Wissenschaft, Coding und Mathematik aus. Das `o1`-Modell verfügt beispielsweise über ein Kontextfenster von 200.000 Tokens und kann mit dem Parameter `reasoning_effort` feinabgestimmt werden, um die Verarbeitungszeit anzupassen [^2].

    *   **API-Zugriff:** Zugänglich über die Azure OpenAI Service API mit der API-Version `2024-12-01-preview` [^1].
    *   **Preisgestaltung:** Die Azure OpenAI Preisgestaltung variiert je nach Modell und Nutzung. Weitere Informationen finden Sie auf der Preisgestaltungsseite für den Azure OpenAI Service.
    *   **Ratenbegrenzungen:** Die Ratenbegrenzungen hängen vom Azure OpenAI-Tarif und der Region ab. Einzelheiten finden Sie in der Azure OpenAI-Dokumentation.
    *   **Unterstützte Funktionen:** Function calling, JSON-Modus, anpassbare Sicherheitseinstellungen [^3].
    *   **Code-Beispiel (Python):**
        ```python
        from openai import AzureOpenAI
        client = AzureOpenAI(
          azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
          api_key=os.getenv("AZURE_OPENAI_API_KEY"),
          api_version="2024-12-01-preview"
        )
        response = client.chat.completions.create(
            model="o1-new", # Ersetzen Sie dies durch den Modell-Bereitstellungsnamen Ihrer o1-Bereitstellung.
            messages=[
                {"role": "user", "content": "Über welche Schritte sollte ich nachdenken, wenn ich meine erste Python-API schreibe?"},
            ],
            max_completion_tokens = 5000
        )
        print(response.model_dump_json(indent=2))
        ```
*   **DeepSeek R1**: Bekannt dafür, in Reasoning-Benchmarks mit OpenAIs o1 zu rivalisieren, bietet DeepSeek sein R1-Modell über eine API an [^4]. Die API bietet Zugang zum Chain of Thought (CoT)-Inhalt, der vom Modell generiert wird, und ermöglicht es Benutzern, den Denkprozess des Modells zu beobachten [^5]. DeepSeek bietet auch eine kostengünstige Alternative zu OpenAI, wobei die komplette R1-API zu einem Bruchteil der Kosten angeboten wird [^6]. Die DeepSeek-V3-API ist ebenfalls verfügbar und bietet eine Leistung, die mit führenden Closed-Source-Modellen vergleichbar ist [^7].

    *   **API-Zugriff:** DeepSeek API, kompatibel mit dem OpenAI API-Format [^8].
    *   **Preisgestaltung:** Input-Tokens \$0,14 pro 1 Mio. Tokens, Output-Tokens \$0,55 pro 1 Mio. Tokens [^9].
    *   **Ratenbegrenzungen:** Informationen zu spezifischen Ratenbegrenzungen finden Sie in der DeepSeek-API-Dokumentation.
    *   **Unterstützte Funktionen:** Chat Completion, Chat Prefix Completion (Beta) [^10].
    *   **Code-Beispiel (Python):**
        ```python
        from openai import OpenAI
        client = OpenAI(api_key="<DeepSeek API Key>", base_url="https://api.deepseek.com")
        messages = [{"role": "user", "content": "9.11 und 9.8, was ist größer?"}]
        response = client.chat.completions.create(
            model="deepseek-reasoner",
            messages=messages
        )
        print(response.choices[^0].message.content)
        ```
        
*   **Grok (xAI)**: xAIs Grok-Modelle, einschließlich Grok-3 und Grok-3 mini, sind mit starken Reasoning-Fähigkeiten ausgestattet. Während Grok-1.5 für frühe Tester verfügbar war, wird Grok 3 demnächst via API erscheinen [^11]. Die Grok 3 (Think)- und Grok 3 mini (Think)-Modelle wurden mit Reinforcement Learning trainiert, um ihren Chain-of-Thought-Prozess zu verfeinern, was fortschrittliches Reasoning auf dateneffiziente Weise ermöglicht [^12].

    *   **API-Zugriff:** Die Grok 3 API wird voraussichtlich in Kürze veröffentlicht [^11].
    *   **Preisgestaltung:** Preisdetails sind noch nicht öffentlich verfügbar. Bitte prüfen Sie die Website von xAI auf Updates.
    *   **Ratenbegrenzungen:** Ratenbegrenzungen sind noch nicht öffentlich verfügbar. Bitte prüfen Sie die Website von xAI auf Updates.
    *   **Unterstützte Funktionen:** Tool use, code execution und erweiterte Agent-Fähigkeiten sind für die Enterprise API geplant [^12].
*   **Gemini 1.5 Pro**: Als Google-Modell zeichnet sich Gemini 1.5 Pro im Reasoning über große Informationsmengen aus und ist für eine breite Palette von Reasoning-Aufgaben optimiert [^13]. Es ist ein multimodales Modell und bietet stärkere Reasoning-Fähigkeiten, einschließlich des Denkprozesses in den Antworten [^14]. Die Gemini API bietet Entwicklern Zugang zu einem Kontextfenster von 2 Millionen Tokens [^15].

    *   **API-Zugriff:** Verfügbar über die Gemini API [^15].
    *   **Preisgestaltung:** Weitere Informationen finden Sie auf der Preisgestaltungsseite von Google AI Studio.
    *   **Ratenbegrenzungen:** 1.500 Anfragen pro Minute für Text Embedding [^16]. Informationen zu anderen Ratenbegrenzungen finden Sie in der Dokumentation von Google AI Studio.
    *   **Unterstützte Funktionen:** Function calling, code execution, anpassbare Sicherheitseinstellungen, JSON-Modus [^17].

**Vergleichende Einblicke:**

| Merkmal           | OpenAI o-series | DeepSeek R1      | Grok (xAI)       | Gemini 1.5 Pro   |
| :---------------- | :-------------- | :--------------- | :--------------- | :--------------- |
| Leistung          | Stärken in MINT | Entspricht/übertrifft o1-mini | Starkes Reasoning | Starke Gesamtleistung |
| API-Zugriff       | Azure OpenAI    | DeepSeek API     | Kommt demnächst  | Gemini API       |
| Kosten            | Variiert        | Kostengünstig    | Noch nicht verfügbar | Siehe Google AI Studio |
| Kontextfenster    | 200K Tokens     | 64K Tokens       | 1M Tokens        | 2M Tokens        |
| Zielanwendungen   | Komplexe Aufgaben | Mathe, Code      | Breites Reasoning | Datenanalyse     |

**Einschränkungen:**

*   **OpenAI o-series:** Erzeugt standardmäßig möglicherweise keine Markdown-Formatierung [^1].
*   **DeepSeek R1:** Die Leistung kann bei Nicht-Englisch/Chinesisch-Anfragen nachlassen [^18].
*   **Grok (xAI):** API noch nicht veröffentlicht; begrenzte Informationen zu spezifischen Fähigkeiten.
*   **Gemini 1.5 Pro:** Experimentelle Modelle sind nicht für den Produktionseinsatz bestimmt [^19].

[^1]: Azure OpenAI o-series Modelle sind darauf ausgelegt, Reasoning- und Problemlösungsaufgaben mit erhöhtem Fokus und gesteigerter Fähigkeit zu bewältigen [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/reasoning)

[^2]: Reasoning-Modelle haben Reasoning-Tokens als Teil der Completion-Tokens, Details sind in der Modellantwort enthalten [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/reasoning)

[^3]: JSON-Modus wird unterstützt [ai.google.dev](https://ai.google.dev/models/gemini)

[^4]: Unsere API bietet Benutzern Zugang zum CoT-Inhalt, der vom deepseek reasoner generiert wird, und ermöglicht es ihnen, diesen anzuzeigen, darzustellen und zu destillieren [searchenginejournal.com](https://www.searchenginejournal.com/googles-ai-search-is-improving-but-still-lags-behind-human-quality-results/508459/)

[^5]: Zu viel geringeren Kosten und mit höherer Leistungsfähigkeit DeepSeek bietet seine vollständige R1 API im Vergleich zu OpenAI zu einem Bruchteil der Kosten an [seo-kueche.de](https://www.seo-kueche.de/blog/google-stellt-gemini-vor-das-kann-der-neue-ki-chatbot/)

[^6]: 全系模型均经过高精度微调 指令遵循强化 对于复杂语言理解 深度推理 文本生成 均有优秀的结果表现 [cloud.baidu.com](https://cloud.baidu.com/doc/wenxinworkshop/s/jlil5u56k)

[^7]: xAI Grok 3 API wird in den kommenden Wochen gestartet [t.me](https://t.me/s/GPT4Telegram)

[^8]: Heute kündigen wir zwei Beta-Reasoning-Modelle an: Grok 3 Think und Grok 3 mini Think [x.ai](https://x.ai/blog/grok-3)

[^9]: Gemini 1.5 Pro ist ein mittelgroßes multimodales Modell, das für eine breite Palette von Reasoning-Aufgaben optimiert ist [ai.google.dev](https://ai.google.dev/models/gemini)

[^10]: Bietet stärkere Reasoning-Fähigkeiten und schließt den Denkprozess in den Antworten ein [youtube.com](https://www.youtube.com/watch?v=YQAydVlHV7c)

[^11]: Input-Token-Limit 2.097.152 [ai.google.dev](https://ai.google.dev/models/gemini)

[^12]: Wenn Reasoning ausgeschaltet ist, liefert Grok 3 sofortige, hochwertige Antworten [x.ai](https://x.ai/blog/grok-3)

[^13]: Gemini 1.5 Pro ist ein mittelgroßes multimodales Modell, das für eine breite Palette von Reasoning-Aufgaben optimiert ist. 1.5 Pro kann große Datenmengen auf einmal verarbeiten [ai.google.dev](https://ai.google.dev/models/gemini)

[^14]: Standardmäßig werden die Modelle o3 mini und o1 nicht versuchen, eine Ausgabe zu erzeugen, die Markdown-Formatierung enthält [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/reasoning)

[^15]: DeepSeek R1 ist für Englisch und Chinesisch optimiert, aber seine Leistung kann bei Anfragen in anderen Sprachen nachlassen [datacamp.com](https://datacamp.com/blog/deepseek-r1)

[^16]: Die API bietet experimentelle Modelle, die als Preview gemäß den Nutzungsbedingungen verfügbar sind, was bedeutet, dass die Modelle nicht für den Produktionseinsatz bestimmt sind [ai.google.dev](https://ai.google.dev/models/gemini)

[^17]: API-Zugriff, Custom AI Development für Entwickler: xAI plant, den API-Zugriff auf Grok 3 freizugeben, um Entwicklern die Integration zu ermöglichen [medium.com](https://medium.com/@gerardnico/a-timeline-to-grok-3-the-race-to-catch-up-54e0c0d1886c)

[^18]: Wir stellen DeepSeek R1 vor, das Cold-Start-Daten vor dem RL einbezieht. DeepSeek R1 erreicht eine Leistung, die mit OpenAI o1 in den Bereichen Mathe, Code und [vergleichbar ist api-docs.deepseek.com](https://api-docs.deepseek.com/guides/reasoning_model)

[^19]: Gemini 1.5 Pro ist ein mittelgroßes multimodales Modell, das für eine breite Palette von Reasoning-Aufgaben optimiert ist [ai.google.dev](https://ai.google.dev/models/gemini)