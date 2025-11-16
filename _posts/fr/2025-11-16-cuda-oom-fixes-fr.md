---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Corrections pour l'erreur de mémoire insuffisante CUDA
translated: true
type: note
---

### Analyse du problème
Le script d'entraînement de nanoGPT échoue avec une erreur CUDA Out of Memory (OOM) lors de l'estimation initiale de la perte (`estimate_loss()`) lors de la passe forward. Cela se produit juste après l'initialisation et la compilation du modèle. Le problème principal est l'épuisement de la mémoire lors de l'allocation d'un grand tampon pour les logits de sortie du modèle :

- **Détails du tampon** : Un tenseur de forme `(65536, 50304)` en `bfloat16` (2 octets par élément), soit ~6,14 Gio. Cela correspond à :
  - Taille du lot (batch size) : 64
  - Longueur de séquence (block_size) : 1024
  - Total de tokens : 64 × 1024 = 65 536
  - Taille du vocabulaire : 50 304 (valeur par défaut de GPT-2)
- **État du GPU** : Votre GPU (probablement un RTX 3060 ou similaire avec 12 Gio de VRAM) a une capacité totale de 11,69 Gio, mais seulement 2,68 Gio étaient libres au moment de l'allocation. Le processus utilisait déjà ~7,04 Gio (dont 6,78 Gio par PyTorch), laissant une marge insuffisante après prise en compte du modèle (~124M paramètres × 2 octets en bfloat16 ≈ 248 Mio), des états de l'optimiseur (~1-2 Gio pour AdamW), des caches de compilation, des activations et de la surcharge.

Ceci est courant pour les modèles de taille GPT-2 (124M paramètres) sur les GPU grand public lorsqu'on utilise de grandes tailles de lot ou de longues séquences, surtout avec `torch.compile` activé, ce qui peut temporairement augmenter l'utilisation de la mémoire pendant la capture et l'optimisation du graphe.

### Causes racines
1. **Taille de lot élevée (64)** : Combinée avec `block_size=1024`, cela crée des tenseurs intermédiaires massifs (par exemple, les logits, les sorties de l'attention). Le nombre effectif de tokens par itération (65 536) pousse les limites de la VRAM.
2. **Compilation du modèle** : `torch.compile` (activé par défaut) utilise Torch Inductor, qui génère des noyaux et des tampons CUDA temporaires. L'avertissement `[0/0] Not enough SMs to use max_autotune_gemm mode` suggère que les multiprocesseurs de flux (SMs) de votre GPU sont limités pour un réglage automatique agressif, augmentant potentiellement la fragmentation.
3. **Type de données et précision** : L'utilisation de `bfloat16` (via `torch.cuda.amp`), mais l'avertissement concernant `GradScaler` (déprécié) indique des inefficacités potentielles. D'autres processus ou des exécutions antérieures peuvent avoir fragmenté la VRAM.
4. **Surcharge de l'évaluation** : `estimate_loss()` exécute des passes forward sur les données d'évaluation (`eval_iters=200`, mais groupées en lots), aggravant le problème avant même le début de l'entraînement.
5. **Utilisation mémoire préexistante** : ~7 Gio déjà alloués suggèrent que le modèle, l'optimiseur et le chargeur de données ont consommé de l'espace dès le départ. La mémoire non-PyTorch (224,90 Mio par le processus) pourrait inclure le contexte CUDA ou des bibliothèques.

### Correctifs recommandés
Commencez par les changements les plus simples dans `config/train_openwebtext.py` (ou remplacez-les via la ligne de commande). Réexécutez après chaque ajustement pour isoler ce qui fonctionne. Objectif : Réduire la VRAM maximale à ~8-9 Gio tout en préservant la qualité de l'entraînement.

#### 1. **Réduire la taille du lot (Correctif principal)**
   - Définissez `batch_size = 4` (ou même 1-2 initialement) pour réduire le tampon des logits à ~0,38 Gio (pour batch=4).
   - Compensez avec `gradient_accumulation_steps = 16` (taille de lot effective=64, mais pic de mémoire plus faible).
   - **Pourquoi ?** La taille du lot augmente linéairement avec la mémoire pour la plupart des tenseurs. C'est le plus efficace contre les OOM sans trop ralentir l'entraînement.
   - Extrait de configuration mis à jour :
     ```
     batch_size = 4
     gradient_accumulation_steps = 16  # Ajuster pour correspondre au lot effectif d'origine
     ```
   - VRAM attendue : ~4-6 Gio au total.

#### 2. **Désactiver ou optimiser la compilation**
   - Ajoutez `compile = False` pour ignorer `torch.compile`, évitant ainsi la surcharge d'Inductor (~1-2 Gio de pic temporaire).
   - Si vous gardez la compilation, ajoutez `mode='reduce-overhead'` pour des noyaux plus rapides mais moins optimisés.
   - Configuration mise à jour :
     ```
     compile = False
     ```
   - **Alternative** : Exécutez avec `torch._dynamo.config.suppress_errors = True` dans le script pour le débogage, mais corrigez d'abord l'OOM.

#### 3. **Réduire la longueur de séquence**
   - Définissez `block_size = 512` (moitié du contexte) pour réduire les tokens par itération à ~32 768, divisant par deux la mémoire des logits (~3,07 Gio).
   - Compromis : Un contexte plus court peut légèrement nuire à la qualité du modèle, mais c'est récupérable avec plus d'entraînement.
   - Configuration :
     ```
     block_size = 512
     ```

#### 4. **Ajustements de gestion de la mémoire**
   - **Variable d'environnement pour la fragmentation** : Comme suggéré dans l'erreur, définissez `export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` avant l'exécution. Cela permet à PyTorch d'utiliser des segments mémoire extensibles sur CUDA 12+ (réduit le gaspillage des blocs réservés mais non utilisés).
   - **Vider le cache manuellement** : Ajoutez `torch.cuda.empty_cache()` après l'initialisation du modèle dans `train.py` (vers la ligne 100), mais ce n'est qu'une solution temporaire.
   - **Utiliser le déchargement CPU** : Pour l'évaluation uniquement, modifiez `estimate_loss()` pour utiliser des lots plus petits ou le CPU pour les parties non critiques, mais cela ralentit les opérations.
   - **Surveiller la VRAM** : Exécutez `nvidia-smi -l 1` dans un autre terminal pour observer l'utilisation en temps réel.

#### 5. **Autres ajustements de configuration**
   - Augmentez `eval_interval = 1000` et réduisez `eval_iters = 50` pour alléger la charge d'évaluation (moins de variation de mémoire au début).
   - Si vous êtes sur une configuration multi-GPU, activez DDP, mais cela semble être un seul GPU.
   - Pour les problèmes bfloat16 : Assurez-vous que votre GPU le prend en charge (Ampere+ comme les séries RTX 30). Sinon, forcez `dtype = 'float16'` dans le script.
   - Correction de l'avertissement de dépréciation : Dans `train.py` ligne 196, changez en `scaler = torch.amp.GradScaler('cuda', enabled=(dtype == 'float16'))`.

#### 6. **Vérifications Matériel/Configuration**
   - **Libérer de la VRAM** : Tuez les autres processus GPU (`nvidia-smi` pour lister les PIDs, puis `kill -9 <PID>`). Redémarrez votre terminal/session.
   - **Jeu de données** : Assurez-vous que `openwebtext_local` est chargé efficacement ; les grands jeux de données peuvent être préchargés en RAM/VRAM via DataLoader.
   - **Version PyTorch/CUDA** : Vérifiez la compatibilité (par exemple, PyTorch 2.4+ avec CUDA 12). Réinstallez si nécessaire : `pip install torch --index-url https://download.pytorch.org/whl/cu121`.
   - **Retour au CPU** : Pour les tests, ajoutez `device = 'cpu'` et `compile = False`, mais attendez-vous à un entraînement très lent (heures par itération contre secondes sur GPU).

### Résultat attendu
Avec `batch_size=4`, `gradient_accumulation_steps=16` et `compile=False`, vous devriez résoudre l'OOM et commencer l'entraînement. Le temps total d'exécution pour `max_iters=20 000` sera plus long à cause de l'accumulation, mais surveillez la perte via `log_interval=100`. Si cela échoue encore, réduisez davantage la taille du lot et augmentez-la plus tard.

Si ces correctifs ne résolvent pas le problème, partagez votre modèle de GPU (`nvidia-smi`), votre version de PyTorch (`torch.__version__`) et votre configuration/journal mis à jour pour des conseils plus ciblés.