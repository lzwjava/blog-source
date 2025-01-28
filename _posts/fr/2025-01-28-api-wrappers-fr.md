---
audio: true
lang: fr
layout: post
title: Préférez utiliser des requêtes HTTP brutes plutôt que des wrappers.
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
        print(f"  Skipping translation for English: {text[:50]}...")
        return text
    print(f"  Translating text: {text[:50]}...")

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
                print(f"  Error: Translation response is empty or invalid: {response}")
            if response and response.choices:
                translated_text = response.choices[0].message.content
                return translated_text
            else:
                print(f"  Translation failed on attempt {attempt + 1}.")
                if attempt == retries - 1:
                    return None
        except Exception as e:
            print(f"  Translation failed with error on attempt {attempt + 1}: {e}")
            if attempt == retries - 1:
                return None
            time.sleep(1)  # Wait before retrying
    return None


Erreur :

bash
 Translation failed with error on attempt 1: Expecting value: line 5 column 1 (char 4)


Cette erreur indique que l'API DeepSeek retourne une réponse qui n'est pas un JSON valide, probablement du HTML ou un autre format. Cela est inattendu, car l'API est censée retourner du JSON. Le problème pourrait être dû à un problème temporaire de l'API, à une limitation de débit ou à un problème avec l'invite. Il est important de gérer cela avec élégance en enregistrant l'erreur et en réessayant éventuellement.