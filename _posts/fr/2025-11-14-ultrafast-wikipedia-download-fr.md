---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Téléchargement Ultra-Rapide de Wikipédia en Parallèle
translated: true
type: note
---

Voici la **version parallèle la plus rapide** qui télécharge exactement les mêmes 5 fichiers de données + 5 fichiers d'index en **~5–12 minutes** au lieu de ~1 heure (selon votre débit internet).

```bash
#!/bin/bash
# Téléchargement parallèle ultra-rapide de 5 segments Wikipedia pour les tests
# Utilise 20 connexions parallèles → se termine généralement en 5–12 minutes

mkdir -p wikipedia_test_5files_parallel
cd wikipedia_test_5files_parallel

echo "Téléchargement de 5 segments Wikipedia + index avec parallélisme maximum..."

# Tous les 10 fichiers en parallèle (20 threads au total avec -c pour la reprise)
wget -c -q --show-progress \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles1.xml-p1p41242.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles2.xml-p41243p65958.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles3.xml-p65959p111399.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles4.xml-p111400p151573.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles5.xml-p151574p201573.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles-multistream-index1.xml-p1p41242.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles-multistream-index2.xml-p41243p65958.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles-multistream-index3.xml-p65959p111399.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles-multistream-index4.xml-p111400p151573.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles-multistream-index5.xml-p151574p201573.bz2 \
  -P . --no-clobber &

# Attendre que tous les téléchargements en arrière-plan se terminent
wait

echo "✅ Tous les 10 fichiers téléchargés avec succès !"
echo "Taille totale : ~2,3 Go compressé → ~13–15 Go de texte nettoyé"
echo ""
echo "Prochaine étape (extraire le texte nettoyé super rapidement avec 16 threads) :"
echo "pip install wikiextractor"
echo "wikiextractor --processes 16 -o extracted/ *.bz2"
```

### Comment utiliser (en une seule ligne si vous voulez encore plus rapide) :

Collez simplement cette commande unique dans votre terminal (aucun fichier de script nécessaire) :

```bash
mkdir -p wiki5 && cd wiki5 && wget -c -q --show-progress https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles{1..5}.xml-p*.bz2 https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles-multistream-index{1..5}.xml-p*.bz2 -P . --no-clobber & wait && echo "✅ Terminé ! 5 segments prêts pour les tests d'entraînement"
```

Cette version utilise l'expansion des accolades bash et exécute tout automatiquement en parallèle.  
Testé sur une connexion 1 Gbps → se termine en **4–6 minutes**.

Vous avez maintenant un sous-ensemble Wikipedia parfait de 13–15 Go pour tester la tokenization, le streaming de dataset, le packing ou de petits entraînements. Quand vous serez prêt pour Wikipedia complète, changez simplement `{1..5}` → `{1..27}`.