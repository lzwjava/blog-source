---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Optimiser les Vitesses de Téléchargement Hugging Face
translated: true
type: note
---

Votre téléchargement actuel passe par le point de terminaison principal de Hugging Face (`huggingface.co`), qui est hébergé principalement dans des centres de données européens/américains. Le routage via votre proxy taïwanais depuis Guangzhou ajoute des problèmes de latence similaires à avant : ~200–300ms aller-retour, plus une limitation potentielle sur les fichiers volumineux (ce fichier Parquet fait ~500MB–1GB par fragment). La redirection 302 que vous voyez est probablement vers un CDN CloudFront, mais ce n'est peut-être pas celui optimal pour l'Asie, ce qui entraîne des ralentissements (par exemple, 1–5 MB/s).

Pour atteindre les vitesses de 20–60 MB/s des téléchargements Wikimedia, utilisez ces ajustements—en priorisant les options adaptées à l'Asie. Tous conservent votre configuration proxy Clash/TW.

### 1. **Passer au Miroir HF (Le plus rapide pour la Chine/Taïwan—Recommandé)**
   Le Miroir HF (`hf-mirror.com`) est un CDN géré par la communauté et optimisé pour l'Asie de l'Est (proxyé via des réseaux domestiques chinois comme Tsinghua). Il reflète exactement tous les jeux de données HF, y compris les fichiers Parquet de FineWeb. Depuis le proxy TW, attendez-vous à 30–80 MB/s.

   Mettez à jour votre script :
   ```bash
   #!/bin/bash
   # wget_fineweb_1.sh (mis à jour pour la vitesse)
   mkdir -p fineweb_test_dump
   cd fineweb_test_dump
   echo "Téléchargement du fragment FineWeb via le Miroir HF (plus rapide pour l'Asie)..."

   # Remplacer huggingface.co par hf-mirror.com
   wget -c "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00000.parquet?download=true"

   echo "Terminé ! Taille du fragment : ~500MB–1GB"
   echo "Pour plus de fragments, bouclez sur par exemple, 000_00001.parquet, etc."
   echo "Pour charger en Python : from datasets import load_dataset; ds = load_dataset('HuggingFaceFW/fineweb', name='CC-MAIN-2013-20', split='train', streaming=True)"
   ```

   Exécutez-le : `./scripts/train/wget_fineweb_1.sh`
   - Si le miroir est lent (rare), revenez à l'officiel : `https://huggingface.co/datasets/...` (mais ajoutez l'astuce de vitesse du #2).

### 2. **Booster avec hf_transfer (Pour tout téléchargement HF—100x plus rapide sur les reprises)**
   L'outil officiel Rust de Hugging Face pour les téléchargements parallèles/multi-threads. Il réessaie automatiquement, utilise plus de connexions et atteint >500 MB/s sur les bons liens. Fonctionne avec `wget` indirectement ou directement via Python (si votre script utilise `huggingface_hub`).

   Installation (une fois, via pip—votre env l'a) :
   ```bash
   pip install hf_transfer
   export HF_HUB_ENABLE_HF_TRANSFER=1
   ```

   Puis relancez votre script original. Il accélère les appels `wget` sous-jacents vers les URLs HF.
   - Conseil pro : Pour le streaming du jeu de données complet (sans téléchargement complet), utilisez Python dans votre pipeline :
     ```python
     from datasets import load_dataset
     import os
     os.environ['HF_HUB_ENABLE_HF_TRANSFER'] = '1'  # Activer avant l'import
     ds = load_dataset("HuggingFaceFW/fineweb", name="CC-MAIN-2013-20", split="train", streaming=True)
     for example in ds.take(1000):  # Stream/traiter à la volée
         print(example)
     ```
     Cela récupère les fragments paresseusement via le miroir si vous définissez `HF_ENDPOINT=https://hf-mirror.com`.

### 3. **Ajustement des Règles Clash (Si Autorisé—Domestique Ultra-Rapide)**
   Si votre configuration proxy vous permet de contourner pour HF (ou de router vers les nœuds HK/SG), ajoutez une règle pour que `huggingface.co` / `hf-mirror.com` passe direct/domestique. Dans `clash.yaml` :
   ```
   rules:
     - DOMAIN-SUFFIX,hf-mirror.com,DIRECT  # Ou votre nœud miroir CN
     - DOMAIN-SUFFIX,huggingface.co,DIRECT
   ```
   Redémarrez Clash, puis téléchargez. Se combine avec le #1 pour 50–100+ MB/s via les miroirs Tsinghua.

### Pourquoi Cela Correspond aux Vitesses Wikimedia
- Wikimedia : Le redirecteur a choisi automatiquement l'Asie (Japon/Corée du Sud/Singapour) → faible latence.
- HF : Par défaut c'est UE/US → latence élevée ; miroir + transfert le change en option optimisée pour l'Asie.

Testez d'abord un fragment—si c'est toujours lent, vérifiez `curl -I https://hf-mirror.com/...` pour les en-têtes (devrait montrer un CDN Asie). Pour les 15T complets de FineWeb, utilisez le streaming via la lib `datasets` pour éviter des téléchargements de 100aines de Go. Faites-moi signe si les vitesses ne décollent pas !