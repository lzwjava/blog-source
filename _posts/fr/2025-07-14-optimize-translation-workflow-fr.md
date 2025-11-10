---
audio: false
generated: true
lang: fr
layout: post
title: Optimisation de la traduction par hachage de paragraphes
translated: true
type: note
---

### Réflexions sur l'optimisation de votre flux de travail de traduction

Votre objectif est clair : minimiser l'utilisation de tokens d'IA pour traduire des articles de blog Jekyll (écrits en Markdown) dans 8 langues en ne retraduisant que les paragraphes modifiés ou nouveaux, tout en mettant en cache ceux qui sont inchangés. Vous souhaitez rester avec Markdown pour l'édition, éviter les bases de données/JSON/YAML pour le contenu principal et gérer les éléments spéciaux comme les blocs de code (qui ne doivent pas être traduits). Une approche basée sur les paragraphes est logique car elle correspond à votre façon d'écrire et de modifier—les traductions peuvent être plus précises contextuellement à ce niveau que par phrases.

Défis clés :
- **Identifier les changements** : Sans les différences (diffs) du contrôle de version, vous avez besoin d'un moyen de détecter ce qui est nouveau/modifié/inchangé. Le hachage des paragraphes (par exemple, en utilisant SHA-256 sur le texte anglais normalisé) est efficace et sans état—pas besoin de stocker les anciennes versions complètes.
- **Gérer la structure Markdown** : Vous ne pouvez pas simplement diviser sur `\n\n` car les blocs de code, les en-têtes, les listes ou d'autres syntaxes pourraient tout casser. Un séparateur simple basé sur les expressions régulières pourrait fonctionner pour des articles basiques, mais un analyseur Markdown léger est préférable pour préserver la structure et ignorer les parties non traduisibles.
- **Mise en cache** : Gardez-la basée sur des fichiers et simple (par exemple, un fichier JSON ou un répertoire de fichiers) pour éviter les bases de données. Cache par hachage de paragraphe, par langue.
- **Économie de tokens** : Pour les articles longs, cela pourrait réduire l'utilisation de 80 à 90 % pour les modifications mineures, car seuls les paragraphes concernés sollicitent l'API d'IA.
- **Cas particuliers** : Paragraphes ajoutés/supprimés (gérez-les en recalculant les hachages) ; ajustements mineurs (par exemple, corrections de fautes de frappe) déclencheront une retraduction sauf si vous normalisez les espaces/ponctuation ; les blocs de code ou le code en ligne doivent être exclus ; si les paragraphes sont réordonnés, les hachages ne correspondront pas, mais c'est acceptable si vous les traitez comme "nouveaux".
- **Intégration** : Exécutez ceci comme un script de pré-build dans votre flux de travail Jekyll (par exemple, via un script bash ou un hook Git). Pas besoin de plugins Jekyll si vous générez des fichiers Markdown traduits séparément.

Ceci est préférable au niveau de la phrase (contexte moins précis pour l'IA) ou à l'article complet (pas d'économie). YAML/JSON serait en effet fastidieux pour écrire des idées—restez sur Markdown.

### Méthode optimale proposée : Hachage par paragraphe avec mise en cache et analyse prenant en compte Markdown

Utilisez un script Python pour :
1. Analyser le Markdown anglais en "unités traduisibles" (paragraphes, en excluant les blocs de code, les en-têtes si souhaité, etc.).
2. Hacher le texte anglais de chaque unité (normalisé, par exemple, en supprimant les espaces superflus).
3. Vérifier dans un cache basé sur des fichiers l'existence de traductions par hachage/langue.
4. Traduire les manquants via votre outil d'IA (par exemple, l'API DeepSeek/Mistral).
5. Mettre en cache les nouvelles traductions.
6. Reconstruire les fichiers Markdown traduits, en préservant les parties non traduisibles.

**Pourquoi c'est la meilleure méthode** :
- **Simple et léger** : Pas de base de données, juste des fichiers. Fonctionne localement/hors ligne sauf pour les appels IA.
- **Flexible** : Gère les blocs de code en les ignorant. Extensible à d'autres éléments Markdown (par exemple, ne pas traduire les en-têtes s'ils sont courts).
- **Rentable** : Ne paie que pour les paragraphes nouveaux/modifiés. Pour un article de 10 paragraphes, en modifier un économise ~90 % des tokens.
- **Maintenable** : Modifiez le Markdown anglais naturellement ; le script gère le reste.
- **Outils nécessaires** : Python (vous l'avez probablement). Bibliothèques : `hashlib` (intégré pour le hachage), `markdown` ou `mistune` pour l'analyse (si nécessaire ; commencez simplement avec des regex pour votre cas "sans syntaxe spéciale").

#### Mise en œuvre étape par étape

1. **Configuration** :
   - Créez un fichier `translations_cache.json` (ou un répertoire comme `cache/` avec des fichiers hash.json pour l'évolutivité).
   - Structure : `{ "hash1": { "fr": "texte traduit", "es": "...", ... }, "hash2": { ... } }`
   - Stockez-le dans votre dépôt de blog (git-ignore si sensible) ou dans un répertoire séparé.
   - Listez vos 8 langues dans le script (par exemple, ['fr', 'es', 'de', ...]).

2. **Analyse du Markdown** :
   - Pour les cas simples (paragraphes + blocs de code) : Utilisez un traitement ligne par ligne pour détecter les blocs de code délimités (``````` ou `~~~`) et le code en retrait (>3 espaces).
   - Collectez les "paragraphes" comme des blocs de lignes consécutives non-code, non-vides.
   - Mieux : Utilisez la bibliothèque `markdown` de Python pour convertir en HTML, puis extrayez le texte, mais c'est destructeur pour la reconstruction. Utilisez plutôt `mistune` (un analyseur Markdown rapide) pour obtenir un AST (arbre de syntaxe abstraite), qui vous permet de parcourir et de modifier les nœuds traduisibles (par exemple, les nœuds 'paragraph').
   - Installez `mistune` si nécessaire (mais votre environnement a les bases ; supposez que vous pouvez le pip localement).

3. **Hachage** :
   - Normalisez : `text.strip().lower()` ou juste `.strip()` pour ignorer les changements d'espaces si souhaité (mais cela pourrait manquer des modifications intentionnelles).
   - Hachez : `hashlib.sha256(normalized.encode()).hexdigest()`

4. **Traduction** :
   - Utilisez votre wrapper d'API d'IA (par exemple, pour DeepSeek : envoyez une invite comme "Traduis ce paragraphe en français : {text}").
   - Traitez par lots si possible, mais comme les paragraphes sont petits, le traitement séquentiel est acceptable.

5. **Reconstruction** :
   - Reconstruisez le Markdown en remplaçant les blocs traduisibles par les traductions en cache/nouvelles, en gardant le code/les en-têtes intacts.

6. **Exécution du script** :
   - Exécutez : `python translate_blog.py chemin/vers/anglais.md`
   - Sorties : `chemin/vers/fr.md`, `chemin/vers/es.md`, etc.
   - Pour Jekyll : Placez-les dans `_posts/` avec des préfixes de langue, ou utilisez un plugin multilingue comme `jekyll-polyglot` pour gérer.

#### Exemple de script Python

Voici une version basique utilisant l'analyse ligne par ligne (pas de librairies externes au-delà des modules intégrés). Elle suppose un Markdown simple : paragraphes séparés par des lignes vides, blocs de code délimités. Passez à `mistune` pour une syntaxe complexe.

```python
import hashlib
import json
import os
import sys
# Supposez que vous avez une fonction de traduction IA ; remplacez par votre appel API DeepSeek/Mistral
def ai_translate(text, lang):
    # Remplaçant : retourne le résultat de l'appel API
    return f"Traduit en {lang} : {text}"  # Remplacez par l'API réelle

CACHE_FILE = 'translations_cache.json'
LANGUAGES = ['fr', 'es', 'de', 'it', 'pt', 'zh', 'ja', 'ko']  # Vos 8 langues

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f, indent=4)

def compute_hash(text):
    normalized = text.strip()  # Personnalisez la normalisation
    return hashlib.sha256(normalized.encode('utf-8')).hexdigest()

def parse_markdown(md_text):
    lines = md_text.splitlines()
    blocks = []
    current_block = []
    in_code = False
    for line in lines:
        if line.strip().startswith('```') or line.strip().startswith('~~~'):
            in_code = not in_code
            if current_block:
                blocks.append(('text', '\n'.join(current_block)))
                current_block = []
            blocks.append(('code', line))
            continue
        if in_code:
            blocks.append(('code', line))
        else:
            if line.strip():  # Non vide
                current_block.append(line)
            else:
                if current_block:
                    blocks.append(('text', '\n'.join(current_block)))
                    current_block = []
    if current_block:
        blocks.append(('text', '\n'.join(current_block)))
    return blocks

def translate_post(english_md_path):
    with open(english_md_path, 'r') as f:
        md_text = f.read()
    
    blocks = parse_markdown(md_text)
    cache = load_cache()
    
    for lang in LANGUAGES:
        translated_blocks = []
        for block_type, content in blocks:
            if block_type == 'code':
                translated_blocks.append(content)
            else:  # text
                h = compute_hash(content)
                if h not in cache:
                    cache[h] = {}
                if lang not in cache[h]:
                    translation = ai_translate(content, lang)
                    cache[h][lang] = translation
                translated_blocks.append(cache[h][lang])
        
        # Reconstruire avec des sauts de ligne
        translated_md = '\n\n'.join(translated_blocks)  # Ajustez pour le formatage Markdown
        output_path = english_md_path.replace('.md', f'_{lang}.md')
        with open(output_path, 'w') as f:
            f.write(translated_md)
    
    save_cache(cache)
    print("Traductions mises à jour.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Utilisation : python script.py chemin/vers/anglais.md")
    else:
        translate_post(sys.argv[1])
```

**Comment l'utiliser** :
- Remplacez `ai_translate` par votre logique d'API.
- Exécutez sur votre fichier d'article après modifications.
- Pour les en-têtes/listes : Étendez `parse_markdown` pour les détecter (par exemple, les lignes commençant par `#` ou `-` comme blocs séparés).
- Si les articles ont des images/liens : Ils restent inchangés puisqu'ils sont dans des blocs de texte.
- Astuce de normalisation : Si vous voulez ignorer les changements de ponctuation mineurs, utilisez des regex pour les supprimer avant le hachage.

#### Améliorations
- **Intégration Git** : Utilisez `git diff` pour pré-identifier les lignes modifiées, mais le hachage est plus simple.
- **Traduction par lots** : Si l'API le supporte, envoyez plusieurs nouveaux paragraphes à la fois.
- **Gestion des erreurs** : Réessayez les appels d'API échoués ; validez les traductions.
- **Analyse avancée** : Pip `mistune` et utilisez son moteur de rendu pour personnaliser (par exemple, ignorez les nœuds 'code_block').
- **Tests** : Les collisions de hachage sont rares avec SHA-256 ; testez sur des exemples d'articles.

Cela devrait vous faire économiser des tokens sans compliquer votre flux de travail. Si votre Markdown est plus complexe, commencez par ceci et itérez. Faites-moi savoir si vous avez besoin d'ajustements ou d'aide pour l'intégration de l'API !