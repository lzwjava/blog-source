---
audio: true
lang: fr
layout: post
title: Préférez utiliser des requêtes HTTP brutes au lieu de wrappers
translated: true
---

```python
import requests
import json
import time
def traduire_texte(texte, langue_cible, special=False):
    if not texte or not texte.strip():
        return ""
    if langue_cible == 'en':
        print(f"  Sauter la traduction pour l'anglais: {texte[:50]}...")
        return texte
    print(f"  Traduction du texte: {texte[:50]}...")

    retries = 3
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": create_translation_prompt(langue_cible, special)},
                    {"role": "user", "content": texte}
                ],
                stream=False
            )
            if not response or not response.choices or not response.choices[0].message.content:
                print(f"  Erreur: La réponse de traduction est vide ou invalide: {response}")
            if response and response.choices:
                texte_traduit = response.choices[0].message.content
                return texte_traduit
            else:
                print(f"  La traduction a échoué lors de la tentative {attempt + 1}.")
                if attempt == retries - 1:
                    return None
        except Exception as e:
            print(f"  La traduction a échoué avec une erreur lors de la tentative {attempt + 1}: {e}")
            if attempt == retries - 1:
                return None
            time.sleep(1)  # Attendre avant de réessayer
    return None
```

Erreur:

```bash
 La traduction a échoué avec une erreur lors de la tentative 1: Expecting value: line 5 column 1 (char 4)
```

Cette erreur indique que l'API DeepSeek retourne une réponse qui n'est pas un JSON valide, probablement du HTML ou un autre format. Ceci est inattendu, car l'API est censée retourner du JSON. Le problème pourrait être dû à un problème temporaire de l'API, à une limitation de débit ou à un problème avec l'invite. Il est important de gérer cela de manière élégante en enregistrant l'erreur et en réessayant éventuellement.