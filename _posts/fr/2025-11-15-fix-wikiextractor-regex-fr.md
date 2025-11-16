---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Corriger l'Erreur Regex de wikiextractor pour Python 3.13
translated: true
type: note
---

L'erreur que vous rencontrez est due à un problème de compatibilité dans le package `wikiextractor` avec la gestion plus stricte des drapeaux inline des expressions régulières par Python 3.13. Plus précisément, le drapeau `(?i)` dans le motif regex est interprété comme un drapeau global, mais il n'est pas positionné tout au début de l'expression, ce qui provoque le `re.PatternError`.

Pour corriger ceci, modifiez le fichier `/home/lzw/.local/lib/python3.13/site-packages/wikiextractor/extract.py` et changez la ligne 378 (ou la définition `ExtLinkBracketedRegex` à proximité) comme suit :

- Original : `'\\[(((?i)' + '|'.join(wgUrlProtocols) + ')' + EXT_LINK_URL_CLASS + r'+)\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\]',`
- Modifié : `'\\[(((?i:' + '|'.join(wgUrlProtocols) + ')' + EXT_LINK_URL_CLASS + r'+)\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\]',`

Ceci ajoute un `:` après `(?i`, le transformant en un drapeau inline local `(?i:...)` qui s'applique uniquement au groupe de correspondance du protocole, ce qui résout l'erreur d'analyse.

De plus, les avertissements `SyntaxWarning: invalid escape sequence '\\['` proviennent de chaînes non brutes contenant des séquences d'échappement que Python 3.13 traite de manière plus stricte (bien qu'ils ne causent pas l'échec principal). Vous pouvez les ignorer pour l'instant, ou mettre à jour ces chaînes en chaînes brutes (par exemple, `r'\\['`) dans le même fichier si elles vous dérangent.

Après la modification, relancez `wikiextractor *.bz2`. Si le package est obsolète, envisagez de vérifier les mises à jour via `pip install --upgrade wikiextractor` ou d'utiliser un environnement virtuel avec une ancienne version de Python (par exemple, 3.10) comme solution de contournement.