---
audio: false
generated: true
image: false
lang: de
layout: post
title: DeepSeek V3.1 Hybride Modi Erklärt
translated: true
type: note
---

So geht die **DeepSeek V3.1 API** mit ihrer neuen hybriden Inferenz-Architektur um („Think“ vs. „Non‑Think“ Modi):

---

### Überblick über die API-Änderungen

#### 1. **Zwei verschiedene Endpunkte (Modi)**

* **`deepseek-chat`** entspricht dem **Non‑Thinking Modus** – optimiert für schnelle Antworten.
* **`deepseek-reasoner`** entspricht dem **Thinking Modus** – entwickelt für überlegtere, mehrstufige Reasoning-Aufgaben.
  Beide Endpunkte operieren nun auf demselben V3.1-Modell mit einem 128K Token Kontextfenster. ([DeepSeek API Docs][1], [Data Science Dojo][2])

#### 2. **Erweiterte Kontextunterstützung**

* Beide Modi unterstützen den erweiterten 128K Token Kontext, ein bedeutendes Upgrade, das die Verarbeitung sehr langer Eingaben ermöglicht. ([DeepSeek API Docs][1], [Hugging Face][3])

#### 3. **Verbessertes Format & Fähigkeiten**

* **Anthropic API-Kompatibilität** wird nun unterstützt, was die Integration von DeepSeek mit Anthropic-style Client-Bibliotheken erleichtert. ([DeepSeek API Docs][1])
* **Strict Function Calling** wird unterstützt (in Beta), was robustere und validierte Tool-Aufrufe über die API ermöglicht. ([DeepSeek API Docs][1])

#### 4. **UI-Umschalter vs. API-Aufruf**

* In ihrer Web-UI („DeepThink“-Button) können Benutzer interaktiv zwischen den Modi wechseln.
* In der **API** müssen Sie den Modus explizit wählen, indem Sie den `model`-Parameter entweder auf `"deepseek-chat"` (für non‑thinking) oder `"deepseek-reasoner"` (für thinking) setzen. ([DeepSeek API Docs][1])

#### 5. **Weitere Verbesserungen**

* **Mehr API-Ressourcen** und ein insgesamt flüssigeres Developer Experience wurden eingeführt. ([DeepSeek API Docs][1])
* Der zugrundeliegende Tokenizer und die Chat-Templates wurden aktualisiert, um modusbasiertes Verhalten zu unterstützen (z.B. das Einfügen von `` Tokens). ([Hugging Face][3])

---

### Zusammenfassung: Was hat sich geändert — Ohne Tabelle

* **Neue Namensgebung**:

  * `deepseek-chat` → Non‑Thinking Modus
  * `deepseek-reasoner` → Thinking Modus

* **Gemeinsame Architektur**: Beide basieren auf demselben 671B-Parameter-Modell mit einem langen 128K-Token-Kontextfenster.

* **Erweiterte Integrationsoptionen**:

  * Unterstützt Anthropic-style APIs.
  * Bietet strict function calling (Beta), ermöglicht sicherere, schema-basierte Tool-Interaktionen.

* **Template-Updates**: Die API verwendet nun spezielle Tokens (``) in Prompts, um die Modi zu unterscheiden, und hat die Chat-Templating-Logik überarbeitet.

* **Developer Experience**: Die Plattform umfasst mehr Ressourcen, aktualisierte Dokumentation und einen insgesamt glatteren Integrationsprozess.

---

### Beispielnutzung (Python/HTTP)

**Non-Thinking (schnelle Antworten):**

```python
import openai  # or DeepSeek-compatible SDK
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role":"user","content":"Tell me a joke."}],
)
```

**Thinking (tiefgehendes Reasoning):**

```python
response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[{"role":"user","content":"Explain why the sky is blue."}],
)
```

**Function Calling (strict mode, beta):**
Sie können Funktionen (Tools) mit JSON-Schemas definieren und das Modell diese aufrufen lassen, wobei Sie strukturierte Aufrufe erhalten, die Sie ausführen und zurückfüttern können – ideal für den Bau autonomer Agenten. ([DeepSeek API Docs][1], [Reddit][4], [apidog][5])

---

Lassen Sie mich wissen, wenn Sie Hilfe bei der Erstellung von Prompts für Tool Use, der Optimierung für Kosten oder Geschwindigkeit oder der Erkundung der Anthropic-kompatiblen Schnittstelle benötigen!

[1]: https://api-docs.deepseek.com/news/news250821?utm_source=chatgpt.com "DeepSeek-V3.1 Release"
[2]: https://datasciencedojo.com/blog/deep-seek-v3-1/?utm_source=chatgpt.com "Deep Seek v3.1: The Next Leap in Open-Source Large ..."
[3]: https://huggingface.co/deepseek-ai/DeepSeek-V3.1?utm_source=chatgpt.com "deepseek-ai/DeepSeek-V3.1"
[4]: https://www.reddit.com/r/LocalLLaMA/comments/1munvj6/the_new_design_in_deepseek_v31/?utm_source=chatgpt.com "The new design in DeepSeek V3.1 : r/LocalLLaMA"
[5]: https://apidog.com/blog/deepseek-v3-1-api/?utm_source=chatgpt.com "How to Use DeepSeek-V3.1 API ?"