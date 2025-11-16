---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Correction de l'Erreur Regex dans Python 3.13
translated: true
type: note
---

L'erreur que vous voyez est causée par **Python 3.13** qui est plus strict concernant la syntaxe des expressions régulières que les versions précédentes.

Plus précisément, cette ligne dans `wikiextractor/extract.py` (autour de la ligne 378) est maintenant invalide dans Python 3.13 :

```python
ExtLinkBracketedRegex = re.compile(
    '\\[(((?i)' + '|'.join(wgUrlProtocols) + ')' + EXT_LINK_URL_CLASS + r'+)\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\]',
    re.S | re.U)
```

Le problème est le flag inline `(?i)` placé au milieu de la chaîne après la concaténation de chaînes. À partir de Python 3.12/3.13, **les flags inline comme `(?i)` ne sont plus autorisés nulle part sauf tout au début du motif de l'expression régulière**.

### Correction rapide (fonctionne sur Python 3.13)

Modifiez le fichier :

```bash
~/.local/lib/python3.13/site-packages/wikiextractor/extract.py
```

Allez à la ligne ~378 et remplacez le bloc cassé par cette version corrigée :

```python
# Ancienne méthode cassée (échoue sur Python 3.13)
# ExtLinkBracketedRegex = re.compile(
#     '\\[(((?i)' + '|'.join(wgUrlProtocols) + ')' + EXT_LINK_URL_CLASS + r'+)\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\]',
#     re.S | re.U)

# Version corrigée – déplacer le flag de non-sensibilité à la casse vers les flags de re.compile
protocol_pattern = '|'.join(wgUrlProtocols)
ExtLinkBracketedRegex = re.compile(
    r'\\['
    r'(((' + protocol_pattern + r')' + EXT_LINK_URL_CLASS + r'+)'
    r'\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\])',
    re.IGNORECASE | re.DOTALL | re.UNICODE
)
```

Ou encore plus propre (recommandé) :

```python
ExtLinkBracketedRegex = re.compile(
    r'\\['
    r'(((' + '|'.join(wgUrlProtocols) + r')' + EXT_LINK_URL_CLASS + r'+)'
    r'\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\])',
    re.I | re.S | re.U
)
```

`re.I` est identique à `re.IGNORECASE`, et il peut être passé comme un flag au lieu d'être intégré via `(?i)` dans le motif.

### Solutions alternatives

1. Utilisez Python 3.11 ou 3.12 (plus simple si vous ne voulez pas patcher)
   ```bash
   python3.11 -m pip install wikiextractor
   # puis exécutez avec python3.11 wikiextractor ...
   ```

2. Utilisez le fork maintenu qui corrige déjà la compatibilité Python 3.13 :
   ```bash
   pip uninstall wikiextractor
   pip install git+https://github.com/attardi/wikiextractor.git
   ```

   Le fork de Giuseppe Attardi a été mis à jour pour Python 3.12+ et fonctionne parfaitement sur 3.13.

3. Utilisez l'alternative moderne très rapide (fortement recommandé pour les gros dumps) :
   ```bash
   pip install wikiextractor-ng   # ou "wiki-dump-tools", "wikitextprocessor", etc.
   ```

Après avoir appliqué le correctif ou être passé au fork corrigé, votre commande fonctionnera à nouveau :

```bash
wikiextractor *.bz2
```

Faites-moi savoir si vous souhaitez un correctif en une seule ligne ou la commande `sed` exacte pour le corriger automatiquement.