---
audio: false
generated: true
lang: de
layout: post
title: Mistral AI Embeddings
translated: true
type: note
---

Um Embedding-Beispiele mit Mistral AI zu liefern, können Sie deren Embeddings-API nutzen, um numerische Repräsentationen (Embeddings) von Text zu erzeugen, die semantische Bedeutung erfassen. Diese Embeddings sind nützlich für Aufgaben wie Ähnlichkeitserkennung, Clustering, Klassifikation oder Suche. Im Folgenden zeige ich, wie man Embeddings für einen Satz von Sätzen erzeugt und ihre Ähnlichkeiten berechnet, indem man den Mistral AI Embeddings-Endpunkt nutzt. Dieses Beispiel baut auf der Struktur des bereitgestellten Codes auf, passt ihn jedoch speziell für Embeddings an, wie in der Dokumentation umrissen: [Mistral AI Embeddings](https://docs.mistral.ai/capabilities/embeddings/).

### Voraussetzungen

Bevor Sie das Beispiel ausführen, stellen Sie sicher, dass Sie Folgendes haben:
1.  **API-Schlüssel**: Einen gültigen Mistral AI API-Schlüssel, gespeichert in der Umgebungsvariable `MISTRAL_API_KEY`.
2.  **Abhängigkeiten**: Die benötigten Python-Pakete sind installiert. Sie können sie mit folgendem Befehl installieren:
    ```bash
    pip install requests numpy
    ```

### Beispielcode

Hier ist ein vollständiges Python-Skript, das Embeddings für drei Sätze erzeugt und ihre paarweisen Ähnlichkeiten berechnet:

```python
import os
import requests
import numpy as np

def call_mistral_embeddings_api(texts, model="mistral-embed"):
    """
    Ruft die Mistral AI Embeddings-API auf, um Embeddings für eine Liste von Texten zu erzeugen.

    Args:
        texts (list): Liste von Zeichenketten, die eingebettet werden sollen.
        model (str): Das zu verwendende Embedding-Modell (Standard: "mistral-embed").

    Returns:
        list: Liste von Embedding-Vektoren oder None, wenn die Anfrage fehlschlägt.
    """
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("Error: MISTRAL_API_KEY environment variable not set.")
        return None

    url = "https://api.mistral.ai/v1/embeddings"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": model,
        "input": texts
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        if response_json and "data" in response_json:
            embeddings = [item["embedding"] for item in response_json["data"]]
            return embeddings
        else:
            print(f"Mistral Embeddings API Error: Invalid response format: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral Embeddings API Error: {e}")
        if e.response:
            print(f"Response status code: {e.response.status_code}")
            print(f"Response content: {e.response.text}")
        return None

def calculate_similarity(emb1, emb2):
    """
    Berechnet die Ähnlichkeit zwischen zwei Embeddings mittels Skalarprodukt.

    Args:
        emb1 (list): Erster Embedding-Vektor.
        emb2 (list): Zweiter Embedding-Vektor.

    Returns:
        float: Ähnlichkeits-Score (Skalarprodukt, äquivalent zur Kosinus-Ähnlichkeit für normalisierte Vektoren).
    """
    return np.dot(emb1, emb2)

if __name__ == "__main__":
    # Beispieltexte zum Einbetten
    texts = [
        "I love programming in Python.",
        "Python is a great programming language.",
        "The weather is sunny today."
    ]

    # Embeddings erzeugen
    embeddings = call_mistral_embeddings_api(texts)
    if embeddings:
        # Embedding-Dimension ausgeben
        print(f"Embedding dimension: {len(embeddings[0])}")

        # Paarweise Ähnlichkeiten berechnen
        sim_12 = calculate_similarity(embeddings[0], embeddings[1])
        sim_13 = calculate_similarity(embeddings[0], embeddings[2])
        sim_23 = calculate_similarity(embeddings[1], embeddings[2])

        # Ergebnisse anzeigen
        print(f"\nSimilarity Results:")
        print(f"Text 1: '{texts[0]}'")
        print(f"Text 2: '{texts[1]}'")
        print(f"Text 3: '{texts[2]}'")
        print(f"\nSimilarity between Text 1 and Text 2: {sim_12:.4f}")
        print(f"Similarity between Text 1 and Text 3: {sim_13:.4f}")
        print(f"Similarity between Text 2 and Text 3: {sim_23:.4f}")
```

### Ausführung

1.  **API-Schlüssel setzen**:
    ```bash
    export MISTRAL_API_KEY="your_api_key_here"
    ```

2.  **Speichern und Ausführen**:
    Speichern Sie das Skript (z.B. als `embedding_example.py`) und führen Sie es aus:
    ```bash
    python embedding_example.py
    ```

### Erwartete Ausgabe

Vorausgesetzt der API-Aufruf ist erfolgreich, sehen Sie eine Ausgabe ähnlich dieser (die genauen Werte hängen von den zurückgegebenen Embeddings ab):
```
Embedding dimension: 1024

Similarity Results:
Text 1: 'I love programming in Python.'
Text 2: 'Python is a great programming language.'
Text 3: 'The weather is sunny today.'

Similarity between Text 1 and Text 2: 0.9200
Similarity between Text 1 and Text 3: 0.6500
Similarity between Text 2 and Text 3: 0.6700
```

### Erklärung

-   **API-Endpunkt**: Die Funktion `call_mistral_embeddings_api` sendet eine POST-Anfrage an `https://api.mistral.ai/v1/embeddings`, übergibt eine Liste von Texten und das Modell `"mistral-embed"`. Die API gibt eine JSON-Antwort zurück, die die Embeddings unter dem Schlüssel `"data"` enthält.

-   **Embeddings**: Jedes Embedding ist ein 1024-dimensionaler Vektor (laut Mistral-Dokumentation), der den semantischen Inhalt des Eingabetexts repräsentiert. Die Embeddings sind auf eine Norm von 1 normalisiert.

-   **Ähnlichkeitsberechnung**: Da die Embeddings normalisiert sind, entspricht das Skalarprodukt (`np.dot`) zwischen zwei Embeddings ihrer Kosinus-Ähnlichkeit. Höhere Werte zeigen eine größere semantische Ähnlichkeit an:
    -   **Text 1 und Text 2**: Beide handeln vom Programmieren in Python, daher sollte ihre Ähnlichkeit hoch sein (z.B. ~0,92).
    -   **Text 1 und Text 3**: Einer handelt vom Programmieren, der andere vom Wetter, daher sollte ihre Ähnlichkeit niedriger sein (z.B. ~0,65).
    -   **Text 2 und Text 3**: Ähnliches Muster, geringere Ähnlichkeit aufgrund unterschiedlicher Themen.

### Zusätzliche Anwendungsfälle

Embeddings von Mistral AI können über die reine Ähnlichkeitserkennung hinaus angewendet werden:
-   **Clustering**: Gruppieren Sie ähnliche Texte mit Algorithmen wie K-means (erfordert `scikit-learn`).
    ```python
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=2).fit(np.array(embeddings))
    print(kmeans.labels_)
    ```
-   **Suche**: Betten Sie eine Abfrage ein und finden Sie den ähnlichsten Text:
    ```python
    query = "Tell me about Python."
    query_emb = call_mistral_embeddings_api([query])[0]
    similarities = [calculate_similarity(query_emb, emb) for emb in embeddings]
    most_similar = texts[np.argmax(similarities)]
    print(f"Most similar text: '{most_similar}'")
    ```
-   **Klassifikation**: Verwenden Sie Embeddings als Features in einem Machine-Learning-Modell.

### Hinweise

-   **Modell**: Das Modell `"mistral-embed"` ist für Embeddings optimiert. Prüfen Sie die [Dokumentation](https://docs.mistral.ai/capabilities/embeddings/) auf Updates oder zusätzliche Modelle.
-   **Batching**: Die API verarbeitet mehrere Texte in einem Aufruf, was die Effizienz steigert.
-   **Erweiterte Anwendungen**: Für umfangreiche Ähnlichkeitssuchen, integrieren Sie sie mit Vektor-Datenbanken wie Faiss oder Milvus.

Dieses Beispiel bietet eine praktische Einführung in die Verwendung von Mistral AI Embeddings, die an die Struktur des bereitgestellten Chat-Completion-Codes angepasst werden kann, indem der Endpunkt und das Datenformat geändert werden.