---
audio: true
lang: de
layout: post
title: Verwenden Sie lieber rohe HTTP-Anfragen anstatt Wrapper.
translated: true
---

python
import requests
import json
import time
def translate_text(text, target_language, special=False):
    if not text or not text.strip():
        return ""
    if target_language == 'en':
        print(f"  Übersetzen für Englisch überspringen: {text[:50]}...")
        return text
    print(f"  Text übersetzen: {text[:50]}...")

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
                print(f"  Übersetzung fehlgeschlagen bei Versuch {attempt + 1}.")
                if attempt == retries - 1:
                    return None
        except Exception as e:
            print(f"  Übersetzung fehlgeschlagen mit Fehler bei Versuch {attempt + 1}: {e}")
            if attempt == retries - 1:
                return None
            time.sleep(1)  # Warten vor erneutem Versuch
    return None


Fehler:

bash
 Übersetzung fehlgeschlagen mit Fehler bei Versuch 1: Erwarteter Wert: Zeile 5 Spalte 1 (Zeichen 4)


Dieser Fehler zeigt an, dass die DeepSeek-API eine Antwort zurückgibt, die kein gültiges JSON ist, möglicherweise HTML oder ein anderes Format. Dies ist unerwartet, da von der API eine JSON-Antwort erwartet wird. Das Problem könnte auf ein vorübergehendes API-Problem, eine Ratenbegrenzung oder ein Problem mit der Eingabeaufforderung zurückzuführen sein. Es ist wichtig, dies elegant zu behandeln, indem der Fehler protokolliert und möglicherweise ein erneuter Versuch unternommen wird.