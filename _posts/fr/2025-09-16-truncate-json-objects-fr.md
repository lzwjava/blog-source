---
audio: false
generated: true
image: false
lang: fr
layout: post
model: mistralai/mistral-medium-3.1
title: Tronquer efficacement les objets JSON
translated: true
type: note
---

Pour tronquer les `n` premières clés d'un objet JSON (qu'il s'agisse d'un tableau ou d'une map), vous pouvez utiliser l'approche suivante. Ceci est particulièrement utile lorsque vous traitez de grandes réponses JSON qui doivent être tronquées en raison de limites de contexte, comme lors de l'utilisation d'un LLM (Language Model) pour générer des cas de test.

Voici une fonction Python qui montre comment tronquer les `n` premières clés d'un objet JSON :

```python
import json

def truncate_json(json_obj, n):
    if isinstance(json_obj, list):
        # Tronquer les n premiers éléments de la liste
        return json_obj[n:]
    elif isinstance(json_obj, dict):
        # Tronquer les n premières clés du dictionnaire
        keys = list(json_obj.keys())
        for key in keys[:n]:
            del json_obj[key]
        return json_obj
    else:
        return json_obj

# Exemple d'utilisation
json_str = '''
{
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}
'''

json_obj = json.loads(json_str)
n = 2  # Nombre de clés à tronquer

truncated_json = truncate_json(json_obj, n)
print(json.dumps(truncated_json, indent=4))
```

### Explication

1. **Définition de la fonction** : La fonction `truncate_json` prend un objet JSON et un entier `n` en entrée.
2. **Gestion des listes** : Si l'objet JSON est une liste, elle retourne une nouvelle liste avec les `n` premiers éléments supprimés.
3. **Gestion des dictionnaires** : Si l'objet JSON est un dictionnaire, elle supprime les `n` premières clés du dictionnaire.
4. **Exemple d'utilisation** : L'exemple montre comment utiliser la fonction avec un exemple d'objet JSON.

### Exemple de sortie

Pour l'objet JSON donné et `n = 2`, la sortie sera :

```json
{
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}
```

Cette approche garantit que l'objet JSON est tronqué de manière appropriée, le rendant plus facile à gérer dans les limites de contexte d'un LLM.