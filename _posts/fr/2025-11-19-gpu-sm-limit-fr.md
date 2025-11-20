---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Limite de SM du GPU pour le Réglage Automatique Maximum
translated: true
type: note
---

L'avertissement "Not enough SMs to use max_autotune_gemm" provient du backend TorchInductor de PyTorch (utilisé avec `torch.compile` et `mode="max-autotune"` ou des modes d'auto-réglage agressifs similaires). Il indique que votre GPU a moins de *Streaming Multiprocessors* (SMs) que le seuil requis pour les options d'auto-réglage GEMM (multiplication matricielle) les plus exhaustives, qui recherchent parmi un vaste espace de configurations de noyaux Triton/CUTLASS pour obtenir des performances maximales.

PyTorch considère un GPU comme "suffisamment grand" seulement s'il possède un nombre substantiel de SMs (typiquement ≥68–80, selon la version exacte de PyTorch ; par exemple, RTX 3080/3090 sont à la limite, A100/H100/RTX 4090 sont confortablement au-dessus). Sur les GPU plus petits (par exemple, RTX 3060, 3070, 2080 Ti, T4, etc.), il désactive le chemin complet `max_autotune_gemm` pour éviter un temps de compilation excessif ou des choix sous-optimaux.

### Pourquoi cela se produit et l'impact
- L'auto-réglage évalue de nombreuses variantes de noyaux au moment de la compilation. L'auto-réglage GEMM complet nécessite suffisamment de parallélisme (SMs) pour que les modèles les plus agressifs en valent la peine.
- L'avertissement est **inoffensif** — la compilation réussit toujours, et vous obtenez de bonnes performances (mais pas le maximum absolu). Les autres auto-réglages (parties non-GEMM, recherche GEMM moins agressive) s'exécutent toujours.
- Cela ne signifie **pas** de remplissage ou d'inefficacité due à la taille du lot ou à l'architecture du modèle de la manière dont vous pourriez le penser. L'interprétation suggérée par l'utilisateur est proche mais pas tout à fait exacte ici — cet avertissement spécifique est purement lié à la taille du GPU, pas au remplissage des entrées/formes.

### Comment l'améliorer ou le contourner
1. **Utiliser un GPU avec plus de SMs** (meilleure solution pour des performances maximales) :
   - Minimum recommandé pour un `max_autotune_gemm` complet fiable : RTX 4090 (128 SMs), A100 (108 SMs), H100 (132+ SMs) ou des cartes datacenter plus récentes.
   - Les cartes grand public en dessous d'environ ~80 SMs (par exemple, RTX 3070 = 46 SMs, RTX 3080 = 68 SMs) déclencheront cela.

   | Exemple de GPU | Nombre de SMs | max_autotune_gemm complet ? |
   |----------------|---------------|------------------------------|
   | RTX 3060/3070  | 46–58        | Non                          |
   | RTX 3080/3090  | 68–82        | Limite (parfois oui)         |
   | RTX 4090       | 128          | Oui                          |
   | A100           | 108          | Oui                          |
   | H100           | 132+         | Oui                          |

2. **Changer le mode de torch.compile** (aucun changement matériel nécessaire) :
   - Utilisez `mode="max-autotune-no-cudagraphs"` — conserve la plupart des avantages de l'auto-réglage mais ignore les CUDA graphs et le chemin GEMM conditionné par les SMs. Souvent presque aussi rapide avec des temps de compilation bien plus courts sur les petits GPU.
   - Ou `mode="reduce-overhead"` — plus léger, utilise les CUDA graphs pour une faible latence, bon pour l'inférence.
   - Exemple :
     ```python
     compiled_model = torch.compile(model, mode="max-autotune-no-cudagraphs", fullgraph=True)
     ```

3. **Activer les matmuls de haute précision** (aide quel que soit le mode/GPU) :
   ```python
   torch.set_float32_matmul_precision("high")  # ou "highest"
   ```
   Cela permet TensorFloat-32 / de meilleurs noyaux cuBLAS.

4. **Forcer un réglage plus agressif malgré tout** (solution de contournement, non officiellement supportée) :
   - Modifier le contrôle dans le code source de PyTorch (éditer `torch/_inductor/utils.py` ou appliquer un correctif à l'exécution) pour abaisser le seuil de SMs. Risqué et peut nuire aux performances ou faire exploser le temps de compilation.

5. **Autres conseils généraux pour un meilleur alignement/efficacité** (sans rapport avec cet avertissement exact mais répond à votre préoccupation concernant le remplissage) :
   - Remplissez les dimensions de lot/séquence avec des multiples de 8/16/32 si possible (courant pour les Tensor Cores).
   - Augmentez la taille du lot si votre charge de travail le permet — les GEMM plus grands utilisent mieux le GPU.
   - Pour les charges de travail axées sur l'inférence, envisagez des alternatives comme vLLM, TensorRT-LLM ou Hugging Face Optimum si les limitations de `torch.compile` persistent.

Dans la plupart des cas réels, la différence de performance due à l'absence du `max_autotune_gemm` complet est faible (quelques pourcents), et `max-autotune-no-cudagraphs` vous permet d'atteindre 95%+ des performances sur les GPU grand public.

[Source PyTorch Inductor utils.py](https://github.com/pytorch/pytorch/blob/main/torch/_inductor/utils.py)
[Discussion sur l'avertissement Torch.compile](https://discuss.pytorch.org/t/torch-compile-warning-not-enough-sms-to-use-max-autotune-gemm-mode/184405)
[Dissecting torch.compile](https://themlsurgeon.substack.com/p/dissecting-torchcompile-surgical)