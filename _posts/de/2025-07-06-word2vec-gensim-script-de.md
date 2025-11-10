---
audio: false
generated: true
lang: de
layout: post
title: Word2Vec-Skript mit Gensim
translated: true
type: note
---

Um Ihnen ein Python-Skript für Word2Vec bereitzustellen, muss ich einige Annahmen darüber treffen, wonach Sie suchen, da "ein Skript über Word2Vec" recht breit gefasst sein kann. Ich biete zwei gängige Szenarien an:

1.  **Ein einfaches Skript mit `gensim` für Training und grundlegende Verwendung:** Dies ist die gebräuchlichste und praktischste Art, Word2Vec in Python zu verwenden.
2.  **Eine sehr grundlegende, konzeptionelle Implementierung von Grund auf:** Dies dient eher dem Verständnis der Kernalgorithmen, ist aber aufgrund der Komplexität und Optimierung weniger praktisch für den realen Einsatz.

Ihrem Wunsch entsprechend priorisiere ich den `gensim`-Ansatz, da dies das ist, was die meisten Leute verwenden würden.

-----

### Python-Skript für Word2Vec mit `gensim`

Dieses Skript wird demonstrieren:

  * Vorbereitung von Beispiel-Textdaten.
  * Training eines Word2Vec-Modells.
  * Finden der ähnlichsten Wörter.
  * Durchführen von Wortanalogien.
  * Speichern und Laden des Modells.

**Voraussetzungen:**

Sie müssen die `gensim`-Bibliothek installieren:

```bash
pip install gensim
```

**Python-Skript (`word2vec_gensim_example.py`):**

```python
import gensim
from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
import logging

# Logging konfigurieren, um den Trainingsfortschritt zu sehen
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# --- 1. Beispiel-Textdaten vorbereiten ---
# In einem realen Szenario würden Sie Ihre Textdaten aus Dateien laden.
# Hier verwenden wir eine einfache Liste von Sätzen.
raw_sentences = [
    "I love natural language processing.",
    "Word embeddings are a fascinating topic.",
    "Machine learning revolutionizes many industries.",
    "Deep learning is a subset of machine learning.",
    "Natural language processing uses various techniques.",
    "Computers understand human language better with word vectors.",
    "The quick brown fox jumps over the lazy dog.",
    "Dog and cat are common pets.",
    "King is to Queen as Man is to Woman."
]

# Sätze vorverarbeiten: Tokenisierung und Umwandlung in Kleinbuchstaben
# gensims simple_preprocess ist dafür praktisch
tokenized_sentences = [simple_preprocess(sentence) for sentence in raw_sentences]

print("\n--- Tokenisierte Sätze ---")
for sentence in tokenized_sentences:
    print(sentence)

# --- 2. Das Word2Vec-Modell trainieren ---
# Erklärte Parameter:
#   vector_size: Dimensionalität der Wortvektoren.
#   window: Maximale Entfernung zwischen dem aktuellen und dem vorhergesagten Wort innerhalb eines Satzes.
#   min_count: Ignoriert alle Wörter mit einer Gesamthäufigkeit niedriger als dieser Wert.
#   sg: Trainingsalgorithmus: 0 für CBOW, 1 für Skip-gram. Skip-gram ist im Allgemeinen besser für seltene Wörter.
#   workers: Verwendet so viele Worker-Threads zum Trainieren des Modells (=schnelleres Training).
#   epochs: Anzahl der Iterationen (Epochen) über das Korpus.
model = Word2Vec(
    sentences=tokenized_sentences,
    vector_size=100,      # Beispiel: 100-dimensionale Vektoren
    window=5,             # Kontext-Fenster von 5 Wörtern auf beiden Seiten
    min_count=1,          # Alle Wörter einschließen (für dieses kleine Beispiel)
    sg=1,                 # Skip-gram verwenden (sg=1)
    workers=4,            # 4 CPU-Kerne für das Training verwenden
    epochs=10             # Für 10 Epochen trainieren
)

print("\n--- Modell-Training abgeschlossen ---")

# --- 3. Das Modell erkunden ---

# Den Vektor für ein bestimmtes Wort abrufen
try:
    word_vector = model.wv['machine']
    print(f"\nVektor für 'machine' (erste 10 Dimensionen): {word_vector[:10]}")
    print(f"Vektor für 'machine' Form: {word_vector.shape}")
except KeyError:
    print("\n'machine' nicht im Vokabular gefunden.")

# Die ähnlichsten Wörter finden
print("\n--- Ähnlichste Wörter zu 'machine' ---")
try:
    similar_words = model.wv.most_similar('machine')
    for word, similarity in similar_words:
        print(f"{word}: {similarity:.4f}")
except KeyError:
    print("\n'machine' nicht im Vokabular gefunden.")

print("\n--- Ähnlichste Wörter zu 'dog' ---")
try:
    similar_words_dog = model.wv.most_similar('dog')
    for word, similarity in similar_words_dog:
        print(f"{word}: {similarity:.4f}")
except KeyError:
    print("\n'dog' nicht im Vokabular gefunden.")


# Wortanalogien durchführen (z.B. King - Man + Woman = Queen)
# Dies funktioniert mit sehr kleinen Datensätzen möglicherweise nicht perfekt, demonstriert aber das Konzept.
print("\n--- Wortanalogien (King - Man + Woman = ?) ---")
try:
    result = model.wv.most_similar(positive=['king', 'woman'], negative=['man'], topn=1)
    if result:
        print(f"King - Man + Woman ist ähnlich zu: {result[0][0]} (Ähnlichkeit: {result[0][1]:.4f})")
    else:
        print("Kein Ergebnis für die Analogie. Das Vokabular könnte zu klein sein.")
except KeyError as e:
    print(f"Ein oder mehrere Wörter für die Analogie nicht im Vokabular gefunden: {e}")
except Exception as e:
    print(f"Ein Fehler ist bei der Analogie aufgetreten: {e}")

# Ähnlichkeit zwischen zwei Wörtern überprüfen
print("\n--- Ähnlichkeit zwischen 'machine' und 'learning' ---")
try:
    similarity = model.wv.similarity('machine', 'learning')
    print(f"Ähnlichkeit: {similarity:.4f}")
except KeyError:
    print("Ein oder beide Wörter nicht im Vokabular gefunden.")

print("\n--- Ähnlichkeit zwischen 'dog' und 'cat' ---")
try:
    similarity_pets = model.wv.similarity('dog', 'cat')
    print(f"Ähnlichkeit: {similarity_pets:.4f}")
except KeyError:
    print("Ein oder beide Wörter nicht im Vokabular gefunden.")

print("\n--- Ähnlichkeit zwischen 'dog' und 'computer' ---")
try:
    similarity_diff = model.wv.similarity('dog', 'computer')
    print(f"Ähnlichkeit: {similarity_diff:.4f}")
except KeyError:
    print("Ein oder beide Wörter nicht im Vokabular gefunden.")

# --- 4. Modell speichern und laden ---
model_path = "word2vec_model.bin"
model.save(model_path)
print(f"\nModell gespeichert unter {model_path}")

# Modell zurückladen
loaded_model = Word2Vec.load(model_path)
print(f"Modell geladen von {model_path}")

# Geladenes Modell überprüfen
print("\n--- Geladenes Modell überprüfen (Ähnlichste Wörter zu 'machine' mit geladenem Modell) ---")
try:
    similar_words_loaded = loaded_model.wv.most_similar('machine')
    for word, similarity in similar_words_loaded:
        print(f"{word}: {similarity:.4f}")
except KeyError:
    print("\n'machine' nicht im Vokabular des geladenen Modells gefunden.")

print("\nSkript-Ausführung abgeschlossen.")
```

**So führen Sie das Skript aus:**

1.  Speichern Sie den obigen Code als Python-Datei (z.B. `word2vec_gensim_example.py`).
2.  Öffnen Sie Ihr Terminal oder Ihre Eingabeaufforderung.
3.  Navigieren Sie zu dem Verzeichnis, in dem Sie die Datei gespeichert haben.
4.  Führen Sie das Skript aus mit: `python word2vec_gensim_example.py`

-----

### Schlüsselkonzepte in Word2Vec (`gensim`-Implementierung)

  * **`gensim.models.Word2Vec`**: Die Hauptklasse für das Training.
  * **`sentences`**: Ein Iterable von Iterables, wobei das äußere Iterable das Korpus und die inneren Iterables Listen von Wörtern (tokenisierte Sätze) sind.
  * **`vector_size`**: Die Anzahl der Dimensionen für die Wortvektoren. Höhere Dimensionen können mehr Nuancen erfassen, erfordern aber mehr Daten und Rechenleistung.
  * **`window`**: Die maximale Entfernung zwischen dem aktuellen Wort und den Wörtern um es herum in einem Satz.
  * **`min_count`**: Wörter, die weniger oft als `min_count` vorkommen, werden ignoriert. Dies hilft, sehr seltene Wörter herauszufiltern, die möglicherweise keine aussagekräftigen Embeddings haben.
  * **`sg` (Skip-gram vs. CBOW)**:
      * `sg=0` (CBOW - Continuous Bag of Words): Sagt das aktuelle Wort basierend auf seinem Kontext vorher. Schneller zu trainieren.
      * `sg=1` (Skip-gram): Sagt die umgebenden Wörter basierend auf dem aktuellen Wort vorher. Im Allgemeinen besser für seltene Wörter.
  * **`workers`**: Anzahl der CPU-Kerne, die für das Training verwendet werden, um den Prozess zu beschleunigen.
  * **`epochs`**: Anzahl, wie oft der Algorithmus über den gesamten Datensatz iteriert. Mehr Epochen können zu besseren Embeddings führen, dauern aber auch länger.
  * **`model.wv`**: Das "Wortvektoren"-Objekt (`KeyedVectors`), das die trainierten Wort-Embeddings und Methoden wie `most_similar`, `similarity` etc. enthält. Sie können auch direkt auf Vektoren zugreifen, z.B. mit `model.wv['word']`.

-----

Dieses `gensim`-Skript bietet eine solide Grundlage für die Arbeit mit Word2Vec. Für reale Anwendungen würden Sie typischerweise ein viel größeres Korpus (z.B. Wikipedia, Common Crawl) verwenden und die Hyperparameter für eine optimale Leistung abstimmen.