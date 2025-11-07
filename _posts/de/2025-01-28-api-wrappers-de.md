---
audio: false
generated: false
image: false
lang: de
layout: post
title: Rohe Http-Anfragen und Wrapper
translated: true
type: post
---

```python
import requests
import json
import time

def translate_text(text, target_language, special=False):
    if not text or not text.strip():
        return ""
    if target_language == 'en':
        print(f"  Übersetzung wird für Englisch übersprungen: {text[:50]}...")
        return text
    print(f"  Übersetzung des Textes: {text[:50]}...")

    retries = 3
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": create_translation_prompt(target_language, special)},
                    {"role": "user", "content": text}
                ],
                stream=False
            )
            if not response or not response.choices or not response.choices[0].message.content:
                print(f"  Fehler: Übersetzungsantwort ist leer oder ungültig: {response}")
            if response and response.choices:
                translated_text = response.choices[0].message.content
                return translated_text
            else:
                print(f"  Übersetzung ist bei Versuch {attempt + 1} fehlgeschlagen.")
                if attempt == retries - 1:
                    return None
        except Exception as e:
            print(f"  Übersetzung ist mit Fehler bei Versuch {attempt + 1} fehlgeschlagen: {e}")
            if attempt == retries - 1:
                return None
            time.sleep(1)  # Warten, bevor erneut versucht wird
    return None
```

Fehler:

```bash
Übersetzung ist mit Fehler bei Versuch 1 fehlgeschlagen: Erwartete Wert: Zeile 5 Spalte 1 (Zeichen 4)
```

Dieser Fehler deutet darauf hin, dass die DeepSeek API eine Antwort zurückgibt, die kein gültiges JSON ist, möglicherweise HTML oder ein anderes Format. Dies ist unerwartet, da die API JSON zurückgeben sollte. Das Problem könnte durch ein temporäres API-Problem, Rate Limiting oder ein Problem mit dem Prompt verursacht werden. Es ist wichtig, dies fehlerfrei zu behandeln, indem der Fehler protokolliert und möglicherweise erneut versucht wird.