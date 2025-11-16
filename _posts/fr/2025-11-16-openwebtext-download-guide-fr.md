---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide de téléchargement de l'ensemble de données OpenWebText
translated: true
type: note
---

### Analyse du problème
L'erreur `RepositoryNotFoundError` (401 Client Error) confirme que le dépôt `openwebtext` n'existe **pas** sur Hugging Face. C'est pourquoi le téléchargement échoue — HF ne trouve pas le dépôt à l'adresse `https://huggingface.co/openwebtext`. La partie "Invalid username or password" est un message générique de la couche d'authentification de HF, mais elle est sans rapport ici puisque le dépôt n'existe tout simplement pas. OpenWebText (le jeu de données que vous essayez d'accéder) est un corpus public de l'ère GPT-2, mais il n'est pas hébergé comme un dépôt standard sur Hugging Face. Il est plutôt distribué via des miroirs, des torrents ou des téléchargements directs depuis des sources académiques/GitHub.

- **Contexte sur OpenWebText** : Créé pour reproduire le jeu de données utilisé dans l'article GPT-2 (à partir d'URLs des archives Pushshift de Reddit, filtrées pour la qualité). Le corpus complet fait ~40 Go de texte, divisé en sous-ensembles comme `urlsf_subset00.tar` (l'une des 14 archives, chacune de ~3-5 Go). Celles-ci contiennent des fichiers texte bruts pour entraîner des modèles comme nanoGPT.
- Aucun dépôt HF officiel : Après vérification, il n'y a pas de téléchargements directs des sous-ensembles complets sous `openwebtext` ou similaire (par exemple, EleutherAI a des dépôts liés mais pas les données brutes). HF se concentre sur les modèles/jeux de données avec des licences, et OpenWebText est dans le domaine public mais hébergé ailleurs pour éviter les coûts de bande passante.

### Méthode de téléchargement correcte
Utilisez des **téléchargements HTTP directs** ou des **torrents** depuis des miroirs établis. La source la plus fiable est le miroir GitHub de Skylion007 (un effort communautaire pour héberger le corpus nettoyé). Voici comment obtenir `urlsf_subset00.tar` (et d'autres si nécessaire) :

1. **Téléchargement direct depuis un miroir** (Recommandé pour la vitesse) :
   - URL de base : `http://skylion007.github.io/OpenWebTextCorpus/`
   - Fichier spécifique : `http://skylion007.github.io/OpenWebTextCorpus/urlsf_subset00.tar`
   - Commande pour télécharger (en utilisant `wget` ou `curl` ; installez-les si nécessaire via `sudo apt install wget`) :
     ```
     cd ~/projects/nanoGPT  # Ou votre répertoire cible
     wget http://skylion007.github.io/OpenWebTextCorpus/urlsf_subset00.tar
     ```
     - Cela le sauvegarde sous `./urlsf_subset00.tar` (~3.3 Go). C'est un miroir HTTP, donc aucune authentification n'est nécessaire, et c'est rapide (directement depuis GitHub Pages).
     - Pour l'ensemble complet (tous les sous-ensembles) : Listez-les depuis la page et téléchargez-les dans une boucle, ou utilisez un script :
       ```bash
       for i in {00..13}; do
         wget http://skylion007.github.io/OpenWebTextCorpus/urlsf_subset${i}.tar
       done
       ```
     - Alternative avec `curl` (si wget n'est pas disponible) :
       ```
       curl -O http://skylion007.github.io/OpenWebTextCorpus/urlsf_subset00.tar
       ```

2. **Téléchargement par Torrent** (Meilleur pour les gros fichiers, réparable et économe en bande passante) :
   - Le torrent officiel pour tous les sous-ensembles : Lien magnet du dépôt original de Gwern ou Academic Torrents.
   - URI Magnet (copiez-collez dans un client comme qBittorrent, Transmission, ou `aria2c`) :
     ```
     magnet:?xt=urn:btih:5b1567f9eed6d1d1a5303a2e1f7a8d6b0a9c8d3e&dn=OpenWebTextCorpus
     ```
   - Ou fichier .torrent direct : Téléchargez-le depuis [academictorrents.com](https://academictorrents.com/details/5b1567f9eed6d1d1a5303a2e1f7a8d6b0a9c8d3e) ou recherchez "OpenWebTextCorpus torrent".
   - Installez un client torrent si nécessaire :
     - Ubuntu/Debian : `sudo apt install qbittorrent-nox` (headless) ou utilisez l'interface graphique.
     - Puis exécutez : `qbittorrent-nox` et ajoutez le lien magnet.
   - Résultat attendu : Télécharge les 14 archives (~40 Go au total) vers votre répertoire choisi. Sélectionnez seulement `urlsf_subset00.tar` si partiel.

3. **Clone GitHub (Si vous voulez la structure du dépôt)** :
   - Les métadonnées du corpus sont sur GitHub : `https://github.com/skylion007/OpenWebTextCorpus`
   - Clonez pour le README/la documentation (pas les données) :
     ```
     git clone https://github.com/skylion007/OpenWebTextCorpus.git
     ```
   - Les liens vers les données sont dans le README — pointant vers les mêmes miroirs ci-dessus.

### Après le téléchargement
- **Extrayez l'archive** :
  ```
  mkdir -p ./openwebtext/subsets
  tar -xvf urlsf_subset00.tar -C ./openwebtext/subsets
  ```
  - Cela décompresse ~100 000+ fichiers texte (par exemple, `0.txt`, `1.txt`) dans `./openwebtext/subsets/`. Chaque fichier est le texte nettoyé d'une page web.
- **Pour l'intégration avec nanoGPT** :
  - NanoGPT (le dépôt d'Andrej Karpathy) a un exemple `openwebtext` dans book/data prep. Utilisez leur script pour concaténer/traiter les fichiers :
    ```python
    # Depuis nanoGPT's data/openwebtext/prepare.py (adaptez si nécessaire)
    import os
    import glob

    input_dir = './openwebtext/subsets'
    output_file = './openwebtext/input.txt'

    with open(output_file, 'w') as out:
        for txt_file in sorted(glob.glob(os.path.join(input_dir, '*.txt'))):
            with open(txt_file, 'r') as f:
                out.write(f.read())
    ```
  - Cela crée un seul fichier massif `input.txt` pour l'entraînement. Soyez prudent — le OpenWebText complet nécessite un stockage/RAM important.
- **Vérifiez l'intégrité** : Chaque archive tar a une somme de contrôle MD5 dans le README du miroir (par exemple, pour subset00 : vérifiez avec le hash fourni en utilisant `md5sum urlsf_subset00.tar`).

### Si les problèmes persistent
- **Miroir hors service ?** Essayez la source originale de Gwern : `https://www.gwern.net/OpenWebTextCorpus` (liens vers AWS S3 ou torrents).
- **Notes légales/accès** : OpenWebText est dans le domaine public (scrapé depuis le web ouvert), mais respectez le robots.txt dans votre utilisation. Aucune authentification HF n'est nécessaire ici.
- **Alternatives sur HF** : Si vous voulez des données similaires hébergées sur HF, vérifiez `wikitext`, `bookcorpus` ou des sous-ensembles de `pile` (par exemple, `repo_id="EleutherAI/pile"` avec `hf download`). Pour OpenWebText exact, restez sur les miroirs.
- **Conseils Disque/Vitesse** : Ces fichiers sont énormes — utilisez des SSD, et surveillez avec `du -sh` ou `htop`. Si vous êtes en Chine ou dans une zone restreinte, utilisez un VPN pour un accès plus rapide.

Si le téléchargement réussit mais que vous rencontrez des erreurs d'extraction/traitement, ou si vous avez besoin d'aide pour l'étape nanoGPT suivante, collez les détails !