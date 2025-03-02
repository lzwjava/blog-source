---
audio: false
generated: true
lang: fr
layout: post
title: Requêtes Http Brutes et Enveloppeurs
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
        print(f"  Ignorer la traduction pour l'anglais: {texte[:50]}...")
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
                print(f"  La traduction a échoué à la tentative {attempt + 1}.")
                if attempt == retries - 1:
                    return None
        except Exception as e:
            print(f"  Échec de la traduction avec erreur à la tentative {attempt + 1}: {e}")
            if attempt == retries - 1:
                return None
            time.sleep(1)  # Attendre avant de retenter
    return None
```

Erreur:

```bash
Échec de la traduction avec erreur à la tentative 1: Attente de valeur: ligne 5 colonne 1 (caractère 4)
```

Cette erreur indique que l'API DeepSeek renvoie une réponse qui n'est pas un JSON valide, probablement du HTML ou un autre format. C'est inattendu, car l'API est censée renvoyer du JSON. Le problème pourrait être dû à un problème temporaire de l'API, à la limitation des taux, ou à un problème avec le prompt. Il est important de gérer cela de manière élégante en enregistrant l'erreur et en envisageant de réessayer.