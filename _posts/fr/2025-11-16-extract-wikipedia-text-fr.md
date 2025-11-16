---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Extraction de texte à partir des archives Wikipédia
translated: true
type: note
---

Voici les méthodes les plus courantes et efficaces pour extraire du texte brut des fichiers dumps `.bz2` de Wikipédia comme le vôtre (`enwiki-latest-pages-articles1.xml-p1p41242.bz2`).

### Outils & Méthodes recommandés (du plus simple au plus efficace)

#### 1. Utiliser wikiextractor (le meilleur pour la plupart des gens – rapide et propre)
C'est l'outil standard utilisé par presque tout le monde en NLP/ML pour les dumps Wikipédia.

```bash
# Installation (une fois)
pip install wikiextractor

# Extraction du texte (supprime les modèles, tableaux, etc., donne un texte propre par article)
wikiextractor enwiki-latest-pages-articles1.xml-p1p41242.bz2 --output wiki_text
```

- Sortie : crée un dossier `wiki_text/` avec des sous-dossiers AA, AB, … contenant des fichiers `.bz2` de JSON/texte propre.
- Pour obtenir du texte brut (un article par ligne) :
```bash
wikiextractor enwiki-latest-pages-articles1.xml-p1p41242.bz2 --processes 8 -o wiki_text --json
# Puis convertir le JSON en texte brut si nécessaire
find wiki_text -name '*' -exec cat {} \; | grep '"text":' | sed 's/.*"text": "//;s/"$//' > all_text.txt
```

#### 2. Utiliser WikiCorpus de gensim (excellent si vous faites du NLP en Python)

```python
from gensim.corpora import WikiCorpus

# Cela gère automatiquement le .bz2 et extrait le texte + tokenise
wiki = WikiCorpus("enwiki-latest-pages-articles1.xml-p1p41242.bz2", dictionary=False)

# Itérer sur les articles
with open("output.txt", "w", encoding="utf-8") as f:
    for i, text in enumerate(wiki.get_texts()):
        f.write(" ".join(text) + "\n")
        if i % 10000 == 0:
            print(f"Processed {i} articles")
```

#### 3. Simple bzip2 + grep/awk (rapide & sale, pas de nettoyage)

```bash
# Juste décompresser et voir le XML brut
bzip2 -dc enwiki-latest-pages-articles1.xml-p1p41242.bz2 | less

# Extraire uniquement le contenu <text> (très rudimentaire, conserve le balisage wiki)
bzip2 -dc enwiki-latest-pages-articles1.xml-p1p41242.bz2 | \
  sed -n '/<text /,/<\/text>/p' | \
  sed 's/<text[^>]*>//g;s/<\/text>//g' > raw_text_with_markup.txt
```

#### 4. Si vous avez le dump complet et voulez tout rapidement (parallèle)
Votre fichier n'est que le premier segment (p1p41242), mais si vous avez tous les ~30+ segments plus tard :

```bash
# Tout extraire en parallèle
ls *.bz2 | xargs -P 8 -I {} wikiextractor {} --output wiki_extracted
```

### Résumé – Ce que je vous recommande maintenant :

```bash
pip install wikiextractor
wikiextractor enwiki-latest-pages-articles1.xml-p1p41242.bz2 -o extracted_wiki --bytes 1M --json
```

Cela vous donnera des articles propres et lisibles en quelques minutes (votre fichier ne fait que ~2-3 Go compressé, donc très gérable).

Dites-moi si vous voulez :
- Uniquement l'espace de noms principal (les vrais articles, pas les pages de discussion)
- Du texte brut au lieu du JSON
- Une sortie tokenisée
- Wikipédia en chinois à la place (zhwiki) – le processus est identique

Bonnes extractions ! 🚀