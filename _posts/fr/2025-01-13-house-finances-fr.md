---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Suivi de nos finances domestiques
translated: true
type: post
---

Récemment, j'ai créé un document markdown pour suivre les transactions financières de notre maison.

La maison appartient à ma femme et moi. Mes parents nous ont donné de l'argent, et nous avons emprunté de l'argent à ma sœur et à mon oncle maternel. Bien que mon oncle maternel m'ait envoyé de l'argent, mon père a ensuite remboursé cette somme.

Nous avons payé 50 % du prix total de notre maison comme acompte, et nous avons emprunté l'autre moitié à la Banque Agricole de Chine. Le contrat dure 20 ans, et le taux d'intérêt actuel est de 3,65 %.

Lorsque j'étais sans emploi, ma femme et mon père m'ont fourni des fonds pour couvrir les mensualités du prêt. Par conséquent, il y a de nombreuses transactions impliquées.

J'utilise China Merchants Bank comme banque principale. China Merchants Bank permet de filtrer les transactions selon qu'elles sont entrantes ou sortantes, et par un montant minimum. Elle prend également en charge le filtrage par mots-clés, ce qui est très utile.

Un autre aspect utile est la prévalence de l'IA. Elle peut également aider à cette tâche. En utilisant l'OCR alimenté par l'IA, spécifiquement Grok, j'ai pu extraire du texte des relevés de transactions avec le Bureau de l'Électricité de Guangzhou.

Comme le tableau ultérieur est basé sur des chiffres précédents, il est préférable de vérifier d'abord les chiffres pour s'assurer que tout est correct avant de continuer.

Le code ci-dessous aide à générer un PDF à partir du markdown. Il contient des paramètres spéciaux pour prendre en charge le rendu des caractères chinois dans le PDF.

```python
import os
import subprocess

# Configuration
CJK_FONT = "Heiti SC"
GEOMETRY = "margin=1in"
input_markdown_path = "mortgage.md"  # Remplacez par votre fichier Markdown d'entrée
output_pdf_path = "mortgage.pdf"    # Remplacez par votre fichier PDF de sortie souhaité

# Vérifier si le fichier d'entrée existe
if not os.path.exists(input_markdown_path):
    raise Exception(f"Le fichier d'entrée n'existe pas : {input_markdown_path}")

# Construire la commande Pandoc
command = [
    'pandoc',
    input_markdown_path,
    '-o', output_pdf_path,
    '-f', 'markdown',
    '--pdf-engine', 'xelatex',
    '-V', f'CJKmainfont={CJK_FONT}',
    '-V', f'CJKsansfont={CJK_FONT}',
    '-V', f'CJKmonofont={CJK_FONT}',
    '-V', f'geometry:{GEOMETRY}',
    '-V', 'classoption=16pt',
    '-V', 'CJKoptions=Scale=1.1',
    '-V', 'linestretch=1.5'
]

# Exécuter la commande Pandoc
try:
    subprocess.run(command, check=True)
    print(f"PDF généré avec succès : {output_pdf_path}")
except subprocess.CalledProcessError as e:
    print(f"Erreur lors de la génération du PDF : {e}")
```