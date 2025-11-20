---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Résoudre les erreurs de mémoire GPU
translated: true
type: note
---

Oui, vous rencontrez une erreur de mémoire insuffisante (OOM) car même le modèle de type nanoGPT "125M" avec vos paramètres actuels pousse les limites d'un GPU de 12 Go (par exemple, 3090/4090/3090 Ti/A6000). Décomposons exactement ce qui utilise la VRAM et ce que vous devriez modifier en premier.

### Estimation actuelle de la consommation VRAM (avec vos paramètres)
- Taille du modèle : véritablement ~124M de paramètres → ~500–550 Mo (en FP16/BF16)
- États de l'optimiseur (AdamW) : ~1–1,2 Go
- Gradients : ~500 Mo
- Activations (le plus gourmand) :
  - batch_size = 16
  - block_size = 1024
  - gradient_accumulation_steps = 32
  → Micro-lot de 16 séquences × 1024 tokens = 16 384 tokens par passe avant/arrière
  - Avec 12 couches, 768 dimensions, 12 têtes → les activations consomment facilement 9–11 Go rien que pour un micro-lot

Donc le total → vous êtes très proche ou au-delà de 12 Go, surtout une fois que la surcharge PyTorch, le cache de compilation, les graphes CUDA, etc., entrent en jeu.

### Que fait réellement `batch_size` ?
`batch_size` dans nanoGPT est la taille du micro-lot (le nombre de séquences traitées en une seule passe avant/arrière avant que les gradients ne soient appliqués).

Votre taille de lot effective (totale) est :

effective_batch_size = batch_size × gradient_accumulation_steps  
= 16 × 32 = 512 séquences

C'est ce 512 qui importe pour la qualité/le bruit du gradient. Le micro-lot (16) affecte principalement la VRAM et la vitesse.

### Meilleures solutions (classées par efficacité pour votre carte de 12 Go)

| Option | Nouvelles valeurs | Lot effectif | VRAM économisée | Effet sur l'entraînement | Recommandation |
|--------|-------------------|------------------|-----------------|--------------------------|----------------|
| 1. Réduire seulement le micro-lot | batch_size = 8<br>gradient_accumulation_steps = 64 | toujours 512 | ~40–50 % d'activations en moins → tient confortablement | Impact quasi nul sur le modèle final | MEILLEUR CHOIX |
| 2. Réduire un peu plus le micro-lot | batch_size = 4<br>gradient_accumulation_steps = 128 | toujours 512 | encore plus sûr, légèrement plus lent | Différence toujours négligeable | Si OOM persiste |
| 3. Réduire les deux (plus facile mais légèrement pire) | batch_size = 8<br>gradient_accumulation_steps = 32 | maintenant 256 | grande économie de VRAM | Gradients légèrement plus bruités, peut nécessiter 10–20 % d'étapes en plus pour converger | Acceptable |
| 4. Réduire la taille du modèle | n_layer=9 ou n_embd=512 | modèle plus petit | énorme économie de VRAM | Vous perdez de la capacité | Seulement si vous voulez des expériences très rapides |

### Configuration recommandée qui tiendra définitivement sur 12 Go
```python
batch_size = 8                    # ← changement principal (était 16)
gradient_accumulation_steps = 64  # ← augmenter pour garder un lot effectif de 512
block_size = 1024                 # garder
# tout le reste inchangé
```

Cela réduira la mémoire d'activation de près de moitié et vous donnera toujours la même qualité de gradient. L'entraînement sera ~10–15 % plus lent en temps réel (plus d'étapes d'accumulation = plus de surcharge Python), mais il fonctionnera au lieu de planter.

### Mode super sûr (si vous avez encore une OOM après ce qui précède)
```python
batch_size = 4
gradient_accumulation_steps = 128   # lot effectif toujours 512
# ou même batch_size=2 + 256 si vous êtes sur une carte strictement limitée à 12 Go
```

### Autres petits ajustements qui aident de quelques centaines de Mo
```python
compile = False          # la compilation peut utiliser 1–2 Go de cache supplémentaire lors de la première exécution
torch.set_float32_matmul_precision('medium')  # supprimer ou régler sur 'high' si vous l'avez
```

### TL;DR
Oui — changez batch_size à 8 et gradient_accumulation_steps à 64.  
Vous conservez la même taille de lot effective (512), la même qualité de modèle, le même nombre de tokens vus, mais la VRAM baisse suffisamment pour tenir confortablement sur 12 Go.

Vous serez tranquille après ce changement. Bon entraînement !