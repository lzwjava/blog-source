---
audio: false
generated: true
lang: de
layout: post
title: Claude für Programmieraufgaben
translated: true
type: note
---

### So verwenden Sie Claude für Programmieraufgaben (über OpenRouter)

Da Sie auf Claude-Modelle über OpenRouter zugreifen (wie zuvor besprochen), können Sie Claudes starke Programmierfähigkeiten für Aufgaben wie Code-Generierung, Debugging, Erklärung von Konzepten, Refactoring oder sogar den Bau kleiner Projekte nutzen. Claude 3.5 Sonnet oder Opus sind aufgrund ihrer Fähigkeiten im logischen Denken und Code-Verständnis besonders gut für die Programmierung geeignet. Im Folgenden führe ich Sie Schritt für Schritt an die effektive Nutzung heran.

#### 1. **Richten Sie Ihre Umgebung ein**
   - Verwenden Sie das OpenRouter-API-Setup von zuvor. Stellen Sie sicher, dass das OpenAI Python SDK installiert ist (`pip install openai`).
   - Wählen Sie für die meisten Programmieraufgaben ein Modell wie `anthropic/claude-3.5-sonnet` – es ist effizient und verarbeitet Sprachen wie Python, JavaScript, Java, C++ etc.
   - Wenn Sie neu im Erstellen von Prompts für Code sind, beginnen Sie mit einfachen Anfragen und iterieren Sie.

#### 2. **Best Practices für das Prompting von Claude in der Programmierung**
   - **Seien Sie spezifisch**: Geben Sie Kontext, Sprache, Einschränkungen und Beispiele an. Claude ist hervorragend im schrittweisen Denken, also bitten Sie es, zunächst "laut nachzudenken", bevor es Code generiert.
   - **Verwenden Sie System-Prompts**: Weisen Sie eine Rolle wie "Sie sind ein erfahrener Python-Entwickler" zu, um die Antworten zu fokussieren.
   - **Behandeln Sie Fehler**: Wenn der Code nicht funktioniert, geben Sie die Fehlermeldung zurück und bitten Sie um Korrekturen.
   - **Iterieren Sie**: Verwenden Sie Folge-Nachrichten in einer Konversation, um den Code zu verfeinern.
   - **Sicherheitshinweis**: Teilen Sie keinen sensiblen Code oder Daten, da API-Aufrufe über OpenRouter gehen.
   - **Unterstützte Sprachen**: Claude beherrscht die meisten gängigen Sprachen (Python, JS, HTML/CSS, SQL, etc.). Für Nischensprachen, geben Sie diese klar an.
   - **Token-Limits**: Halten Sie Prompts innerhalb des Kontextfensters des Modells (z.B. 200K Token für Claude 3.5 Sonnet), um Abschneiden zu vermeiden.

#### 3. **Beispiel: Code generieren**
   So können Sie Claude verwenden, um eine einfache Python-Funktion zu generieren. Verwenden Sie dies in Ihrem Code:

   ```python
   from openai import OpenAI

   client = OpenAI(
       base_url="https://openrouter.ai/api/v1",
       api_key="YOUR_OPENROUTER_API_KEY_HERE",  # Ersetzen Sie mit Ihrem Schlüssel
   )

   # Prompten Sie Claude, um Code zu generieren
   response = client.chat.completions.create(
       model="anthropic/claude-3.5-sonnet",
       messages=[
           {"role": "system", "content": "You are an expert Python programmer. Provide clean, efficient code with comments."},
           {"role": "user", "content": "Write a Python function to calculate the factorial of a number using recursion. Include error handling for negative inputs."}
       ],
       temperature=0.2,  # Niedrige Temperatur für deterministischen Code
       max_tokens=500
   )

   # Extrahieren und drucken Sie den generierten Code
   generated_code = response.choices[0].message.content
   print(generated_code)
   ```

   **Erwartete Ausgabe (Beispiel)**:
   ```
   def factorial(n):
       """
       Calculate the factorial of a non-negative integer using recursion.
       
       Args:
       n (int): The number to calculate factorial for.
       
       Returns:
       int: The factorial of n.
       
       Raises:
       ValueError: If n is negative.
       """
       if n < 0:
           raise ValueError("Factorial is not defined for negative numbers.")
       if n == 0 or n == 1:
           return 1
       return n * factorial(n - 1)
   ```

#### 4. **Beispiel: Debugging von Code**
   Geben Sie fehlerhaften Code an Claude und bitten Sie um Korrekturen.

   **Prompt-Beispiel** (Zur `messages`-Liste hinzufügen):
   ```
   {"role": "user", "content": "Debug this Python code: def add(a, b): return a + c. Error: NameError: name 'c' is not defined. Fix it and explain."}
   ```

   Claude könnte antworten: "The error is due to 'c' not being defined. Change to 'return a + b'. Explanation: Typo in variable name."

#### 5. **Beispiel: Konzepte erklären**
   Fragen Sie zum Lernen nach Erklärungen mit Codeausschnitten.

   **Prompt-Beispiel**:
   ```
   {"role": "user", "content": "Explain how decorators work in Python, with a simple example."}
   ```

   Dies könnte eine detaillierte Antwort mit Code, wie z.B. einem Logging-Decorator, liefern.

#### 6. **Erweiterte Nutzung: Ein Projekt aufbauen**
   - Starten Sie eine Konversation, indem Sie den Nachrichtenverlauf beibehalten. Hängen Sie vorherige Antworten zur `messages`-Liste für Kontext hinzu.
   - Beispiel: Zuerst nach einem Umriss für einen Web-Scraper prompten, dann mit "Add error handling to the code you provided." verfeinern.
   - Integration mit Tools: Verwenden Sie Claude, um Code zu generieren, den Sie lokal oder über andere APIs testen können.

#### 7. **Tipps für chinesische Nutzer**
   - Sie können auf Chinesisch prompten: Claude unterstützt mehrsprachige Eingabe. Z.B.: {"role": "user", "content": "用Python写一个计算阶乘的函数，包括负数错误处理。"} (Es wird auf Chinesisch antworten, wenn danach gefragt).
   - Kosten: Programmier-Prompts verbrauchen viele Token, überwachen Sie also Ihr OpenRouter-Guthaben. Beginnen Sie mit kurzen Prompts.
   - Alternativen falls nötig: Wenn Sie auf OpenRouter-Limits stoßen, ziehen Sie kostenlose Stufen anderer Plattformen in Betracht, diese leiten jedoch möglicherweise nicht zu Claude weiter.

Wenn Sie eine spezifische Programmieraufgabe oder Sprache angeben, kann ich ein maßgeschneidertes Beispiel geben!

[OpenRouter Dokumentation](https://openrouter.ai/docs)
[Anthropic Prompting Guide für Coding](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)
[Claude 3.5 Sonnet Model Card](https://www.anthropic.com/news/claude-3-5-sonnet)