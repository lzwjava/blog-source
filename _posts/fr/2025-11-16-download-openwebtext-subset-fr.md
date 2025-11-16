---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Téléchargement du sous-ensemble OpenWebText via Hugging Face
translated: true
type: note
---

L'ensemble de données auquel vous faites référence est hébergé sur Hugging Face sous l'identifiant de dépôt `Skylion007/openwebtext`. Le fichier spécifique `subsets/urlsf_subset00.tar` est accessible publiquement (aucune authentification requise), vous pouvez donc le télécharger en utilisant l'outil CLI Hugging Face (`huggingface-cli`). Voici comment procéder :

### Prérequis
- Installez le Hugging Face Hub CLI si vous ne l'avez pas déjà fait :
  ```
  pip install huggingface_hub
  ```
- (Optionnel) Si vous avez la commande `huggingface-cli` aliasée en `hf` (commun sur certains systèmes), vous pouvez utiliser ce raccourci. Sinon, utilisez le préfixe complet `huggingface-cli`.

### Commande de Téléchargement
Exécutez ceci dans votre terminal :
```
huggingface-cli download Skylion007/openwebtext subsets/urlsf_subset00.tar --local-dir ./openwebtext
```
- Cela téléchargera le fichier vers `./openwebtext/subsets/urlsf_subset00.tar` (en créant le sous-répertoire `subsets` si nécessaire).
- Le fichier est assez volumineux (~1,5 Go décompressé, mais c'est une archive tar), assurez-vous d'avoir assez d'espace disque et une connexion stable.
- Si vous souhaitez le télécharger sans la structure du dépôt (directement dans le répertoire courant), ajoutez `--repo-type dataset` (bien que cela soit implicite ici) ou ajustez `--local-dir`.

### Utilisation de Python (Alternative)
Si vous préférez le script en Python (par exemple, via la bibliothèque `huggingface_hub`) :
```python
from huggingface_hub import hf_hub_download

# Télécharger vers le répertoire courant
hf_hub_download(
    repo_id="Skylion007/openwebtext",
    filename="subsets/urlsf_subset00.tar",
    local_dir="./openwebtext",  # Optionnel : spécifie le répertoire de base
    repo_type="dataset"
)
```
Installez d'abord la librairie : `pip install huggingface_hub`.

### Notes
- Ceci est un sous-ensemble de OpenWebText (un large corpus web). Après le téléchargement, vous devrez extraire le fichier `.tar` (par exemple, `tar -xvf subsets/urlsf_subset00.tar`).
- Si le téléchargement échoue (par exemple, à cause de problèmes de réseau), réessayez ou utilisez `--cache-dir` pour spécifier un emplacement de cache personnalisé.
- Pour l'ensemble de données complet ou d'autres sous-ensembles, consultez la page du dépôt : https://huggingface.co/datasets/Skylion007/openwebtext.

Si vous rencontrez des erreurs, partagez le résultat pour le débogage !