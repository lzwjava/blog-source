---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Différences de structure des fichiers de vidage de Wikipédia
translated: true
type: note
---

La différence clé réside dans la manière dont le texte complet des articles Wikipédia est réparti entre plusieurs fichiers — spécifiquement si un fichier `.xml.bz2` contient un seul flux de révisions (non-multistream) ou de nombreux flux compressés regroupés (multistream).

### 1. Les dumps non-multistream (ancien style, ou les fichiers par défaut « pages-articles »)
Exemple de nom de fichier :  
`enwiki-20251101-pages-articles1.xml-p1p41242.bz2`

- Chaque fichier `.xml.bz2` contient une partie des pages (par exemple, pages 1–41242) dans l'ordre des ID de page.
- À l'intérieur du fichier, il y a exactement une séquence continue de `<page>` … `<page>` …
- Toutes les révisions d'une seule page sont regroupées à l'intérieur de cette balise page (la dernière révision + les plus anciennes si vous avez demandé « current + history »).
- Pour extraire un seul article, il suffit de décompresser et d'analyser le gros XML normalement avec n'importe quel outil XML/BZ2.
- `wget -c` fonctionne parfaitement de manière simple : il reprend exactement là où il s'est arrêté car le fichier est un seul flux bzip2.

### 2. Les dumps multistream (les fichiers qui contiennent « multistream » dans le nom)
Exemple de nom de fichier (celui que vous avez lié) :  
`enwiki-20251101-pages-articles-multistream1.xml-p1p41242.bz2`

- La même plage de pages (p1p41242) est couverte, mais le texte complet de chaque révision n'est plus stocké dans le fichier XML principal.
- À la place :
  - Le fichier XML principal ne contient que les métadonnées (titre, id, restrictions, horodatage de la dernière révision, etc.) et un pointeur (décalage d'octet + longueur) vers l'emplacement où se trouve le texte réel de la révision.
  - Les textes réels des révisions sont stockés séparément dans de nombreux petits flux compressés à l'intérieur du même fichier `.bz2` (d'où « multistream »).
- Il y a généralement un fichier compagnon `...-multistream-index1.txt.bz2` qui contient les décalages d'octets exacts pour chaque page/révision afin que les outils puissent sauter directement au flux compressé approprié et extraire uniquement ce texte sans décompresser l'intégralité du fichier de 10–30 Go.

### Pourquoi est-ce important pour `wget -c` ?

En pratique, les deux commandes :

```bash
wget -c https://.../enwiki-20251101-pages-articles1.xml-p1p41242.bz2
wget -c https://.../enwiki-20251101-pages-articles-multistream1.xml-p1p41242.bz2
```

se comportent exactement de la même manière du point de vue de wget : les deux sont des fichiers bzip2 uniques normaux, donc le téléchargement reprise avec `-c` fonctionne parfaitement dans les deux cas.

La différence n'apparaît que lorsque vous commencez à traiter le fichier téléchargé.

### Tableau récapitulatif

| Caractéristique                      | Non-multistream (régulier)                     | Multistream                                      |
|--------------------------------------|-------------------------------------------------|--------------------------------------------------|
| Le nom de fichier contient           | `-pages-articlesN.xml-...bz2`                  | `-pages-articles-multistreamN.xml-...bz2`        |
| Emplacement du texte de l'article    | Dans le XML `<page><revision><text>...</text></revision></page>` | En dehors du XML, dans des flux compressés séparés |
| Taille du fichier (pour la même plage de pages) | Beaucoup plus grand (souvent 2–3×)             | Beaucoup plus petit                              |
| Accès aléatoire / extraction d'une seule page | Très lent (doit décompresser tout le fichier) | Très rapide (avec le fichier d'index)            |
| Outils qui le comprennent directement | N'importe quel analyseur XML (SAX, xmltodict, etc.) | Outils wikimedia’s dump-generator, pywiki, mwxml, etc. |
| Nécessite un fichier d'index compagnon ? | Non                                            | Oui (`-multistream-index....txt.bz2`)            |
| Capacité de reprise `wget -c`        | Parfaite                                       | Parfaite (toujours un seul fichier bzip2)        |

### Alors, lequel devez-vous télécharger ?

- Si vous voulez juste effectuer une passe séquentielle complète une fois (par exemple pour entraîner un modèle de langage), les fichiers non-multistream sont plus simples.
- Si vous voulez un jour rechercher des pages individuelles rapidement, ou si vous vous souciez de l'espace disque et de la vitesse d'extraction, préférez toujours la paire multistream + index. Presque tous les outils de traitement sérieux de Wikimedia (WikiExtractor, WikiCorpus de gensim, scripts jawiki, etc.) attendent ou recommandent fortement la version multistream de nos jours.

Vous pouvez reprendre le téléchargement des deux fichiers avec `wget -c` sans aucun problème ; la partie « multistream » change seulement ce qu'il y a à l'intérieur du fichier, pas la façon dont HTTP/wget le voit.