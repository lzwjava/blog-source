---
audio: false
generated: true
image: false
lang: de
layout: post
model: mistralai/mistral-medium-3.1
title: Effizientes Kürzen von JSON-Objekten
translated: true
type: note
---

Um die ersten `n` Schlüssel aus einem JSON-Objekt (egal ob Array oder Map) zu kürzen, können Sie den folgenden Ansatz verwenden. Dies ist besonders nützlich, wenn Sie mit großen JSON-Antworten arbeiten, die aufgrund von Kontextlimits gekürzt werden müssen, zum Beispiel wenn Sie ein LLM (Language Model) verwenden, um Testfälle zu generieren.

Hier ist eine Python-Funktion, die demonstriert, wie die ersten `n` Schlüssel aus einem JSON-Objekt gekürzt werden:

```python
import json

def truncate_json(json_obj, n):
    if isinstance(json_obj, list):
        # Kürze die ersten n Elemente aus der Liste
        return json_obj[n:]
    elif isinstance(json_obj, dict):
        # Kürze die ersten n Schlüssel aus dem Wörterbuch
        keys = list(json_obj.keys())
        for key in keys[:n]:
            del json_obj[key]
        return json_obj
    else:
        return json_obj

# Beispielverwendung
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
n = 2  # Anzahl der zu kürzenden Schlüssel

truncated_json = truncate_json(json_obj, n)
print(json.dumps(truncated_json, indent=4))
```

### Erklärung

1. **Funktionsdefinition**: Die `truncate_json` Funktion nimmt ein JSON-Objekt und eine ganze Zahl `n` als Eingabe.
2. **Listenbehandlung**: Wenn das JSON-Objekt eine Liste ist, gibt sie eine neue Liste zurück, bei der die ersten `n` Elemente entfernt wurden.
3. **Wörterbuchbehandlung**: Wenn das JSON-Objekt ein Wörterbuch ist, entfernt sie die ersten `n` Schlüssel aus dem Wörterbuch.
4. **Beispielverwendung**: Das Beispiel zeigt, wie die Funktion mit einem Beispiel-JSON-Objekt verwendet wird.

### Beispielausgabe

Für das gegebene Beispiel-JSON-Objekt und `n = 2` wird die Ausgabe wie folgt sein:

```json
{
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}
```

Dieser Ansatz stellt sicher, dass das JSON-Objekt angemessen gekürzt wird, was die Handhabung innerhalb der Kontextlimits eines LLM erleichtert.