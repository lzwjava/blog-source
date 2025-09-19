---
audio: false
generated: false
image: true
lang: fr
layout: post
title: 'Problèmes de Markdown : Kramdown & XeLaTeX'
translated: true
---

Pour générer des PDFs pour mon blog Jekyll en utilisant Markdown, j'utilise la commande Pandoc suivante :

```python
command = [
    'pandoc',
    input_markdown_path,
    '-o', output_pdf_path,
    '-f', 'markdown',
    '--pdf-engine', 'xelatex',
    '--resource-path=.:assets',
    '-V', f'CJKmainfont={CJK_FONT}',
    '-V', f'CJKsansfont={CJK_FONT}',
    '-V', f'CJKmonofont={CJK_FONT}',
    '-V', f'geometry:{GEOMETRY}',
    '-V', 'classoption=16pt',
    '-V', 'CJKoptions=Scale=1.1',
    '-V', 'linestretch=1.5'
]
```

Prise en charge à la fois de Kramdown et XeLaTeX

Lors de l'écriture de Markdown qui doit fonctionner avec kramdown (pour la sortie HTML via Jekyll) et XeLaTeX (pour la sortie PDF via Pandoc), il y a quelques points à prendre en compte :

1. Compatibilité des chemins d'images
	•	Kramdown (HTML) : Préfère les chemins commençant par / pour référencer les ressources.
	•	XeLaTeX (PDF) : Préfère les chemins relatifs sans le / initial.

Solution : Utiliser des chemins relatifs qui fonctionnent pour les deux :

```
![](assets/images/chatgpt/block.jpg)
```

2. Gestion des attributs kramdown
	•	{:.responsive} est spécifique à kramdown pour styliser la sortie HTML.
	•	XeLaTeX ne prend pas en charge ces attributs et générera une erreur.

Solution : Supprimez les attributs spécifiques à kramdown dans le Markdown destiné à la génération de PDF. Par exemple :

```markdown
<!-- Spécifique à Kramdown -->
```
![](assets/images/chatgpt/block.jpg){: .responsive }
```

<!-- Compatible avec les deux -->
```
![](assets/images/chatgpt/block.jpg)
```

Si `{:.responsive}` est essentiel pour votre mise en page HTML Jekyll, envisagez de l'ajouter de manière sélective pour la sortie web tout en l'omettant lors du processus de génération de PDF.

Workflow pour une Compatibilité Double

1.	Écrivez du contenu en Markdown avec un minimum de dépendances sur les fonctionnalités spécifiques à kramdown.
2.	Pour un style avancé en HTML, appliquez des classes CSS directement dans vos modèles Jekyll plutôt qu'en ligne dans le Markdown.
3.	Utilisez les options de Pandoc pour contrôler la mise en forme du PDF tout en conservant la portabilité du Markdown.

En suivant ces pratiques, le contenu Markdown reste compatible entre le rendu HTML de Jekyll et la génération de PDF via XeLaTeX, garantissant un flux de travail fluide pour une publication multi-format.