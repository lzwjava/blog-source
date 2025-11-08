---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: FlashAttention résout le goulot d’étranglement mémoire des Transformers
translated: true
type: note
---

### Contexte : Les défis de l'attention standard dans les Transformers

Les Transformers, qui sont à la base de modèles comme GPT et BERT, reposent fortement sur le mécanisme d'auto-attention pour traiter les séquences. Dans l'auto-attention, étant donné des séquences d'entrée représentées comme la matrice de requêtes \\(Q\\), la matrice de clés \\(K\\) et la matrice de valeurs \\(V\\) (chacune de forme \\(N \times d\\), où \\(N\\) est la longueur de la séquence et \\(d\\) est la dimension de tête, typiquement 64-128), la sortie d'attention \\(O\\) est calculée comme suit :

\\[
S = QK^T \in \mathbb{R}^{N \times N}, \quad P = \softmax(S) \in \mathbb{R}^{N \times N}, \quad O = PV \in \mathbb{R}^{N \times d},
\\]

où \\(\softmax\\) est appliqué ligne par ligne, et \\(S\\) est souvent mis à l'échelle par \\(\tau = 1 / \sqrt{d}\\) pour la stabilité. Des opérations supplémentaires comme le masquage causal (pour les modèles autorégressifs) et le dropout sont courantes.

Cette formulation est élégante mais coûteuse en calculs. Les matrices intermédiaires \\(S\\) et \\(P\\) sont de taille \\(N \times N\\), conduisant à une **complexité temporelle et mémoire quadratique** \\(O(N^2)\\) en fonction de la longueur de séquence \\(N\\). Pour des contextes longs (par exemple, \\(N = 4096\\) dans GPT-2 ou jusqu'à 128k dans les LLM modernes), cela devient un goulot d'étranglement sévère :

- **Gourmand en mémoire** : Sur les GPU, la mémoire haute bande passante (HBM) est le stockage principal, mais matérialiser \\(S\\) et \\(P\\) peut dépasser la HBM disponible (par exemple, 40-80 Go sur A100/H100). À \\(N=4096\\), \\(d=64\\), cela consomme à lui seul ~1-2 Go juste pour les intermédiaires, plus les entrées/sorties/activations, causant souvent des erreurs de mémoire insuffisante (OOM).
- **Limitations de vitesse** : L'attention est limitée par la mémoire, pas par le calcul. Les GPU modernes (par exemple, NVIDIA A100) ont une bande passante HBM de ~1,5 To/s mais une puissance de calcul de ~19 TFLOPS—pourtant, des opérations comme softmax nécessitent de lire/écrire la matrice complète \\(N^2\\) plusieurs fois (par exemple, 4-6 accès HBM par élément dans les passes avant/arrière). Il en résulte des temps d'exécution qui évoluent de manière quadratique : par exemple, passe avant ~36 ms à \\(N=4096\\) dans PyTorch, passe arrière ~88 ms.
- **Barrières en entraînement/génération** : Pendant l'entraînement, les gradients nécessitent de stocker \\(P\\) pour la passe arrière, doublant la mémoire. Pour l'inférence, les contextes longs (par exemple, 64k tokens) sont irréalisables sans approximations comme l'attention sparse ou les méthodes de faible rang (par exemple, Reformer, Linformer), qui échangent l'exactitude contre l'efficacité mais sous-performent souvent en raison de l'ignorance des coûts d'E/S.

FlashAttention (introduit en 2022 par Tri Dao et al.) résout ces problèmes en repensant l'algorithme pour être **conscient des E/S**, en tirant parti de la hiérarchie mémoire du GPU (SRAM rapide ~20 Mo vs. HBM lente) sans approximations.

### Idées principales : Tiling, Fusion de noyaux et Softmax en ligne

FlashAttention calcule une attention **exacte** (sans approximations) en :

1.  **Tiling (Découpage en tuiles)** : Au lieu de matérialiser les matrices complètes \\(N \times N\\), il divise \\(Q, K, V\\) en petits blocs qui tiennent dans la SRAM. \\(Q\\) est divisé en \\(T_r = \lceil N / B_r \rceil\\) blocs-lignes de taille \\(B_r \times d\\) (par exemple, \\(B_r \approx 64-256\\)), et \\(K, V\\) en \\(T_c = \lceil N / B_c \rceil\\) blocs-colonnes de taille \\(B_c \times d\\) (par exemple, \\(B_c \approx 128-1024\\)). Les tailles de blocs sont choisies dynamiquement en fonction de la capacité de la SRAM \\(M\\) (par exemple, \\(B_c \approx M / (4d)\\)) pour maximiser la réutilisation.

2.  **Fusion de noyaux** : Toutes les opérations (matmul pour \\(S\\), masquage, softmax, dropout, matmul pour \\(O\\)) sont fusionnées en un seul noyau CUDA. Cela évite d'écrire les intermédiaires dans la HBM, réduisant les E/S de ~50-70 %. Le noyau charge les blocs de la HBM vers la SRAM, calcule sur la puce et ne réécrit que les sommes partielles—par exemple, une lecture/écriture HBM par bloc au lieu de par élément.

3.  **Softmax en ligne avec statistiques** : Le softmax ne peut pas être calculé partiellement sans la ligne complète, donc FlashAttention utilise une **décomposition associative** pour un calcul incrémental. Pour une ligne divisée en blocs \\(x = [x^{(1)}; x^{(2)}]\\), suivre les statistiques courantes :
    - Max de ligne \\(m_i = \max_j S_{ij}\\),
    - Somme de ligne des exponentielles \\(\ell_i = \sum_j \exp(S_{ij} - m_i)\\).

    Mise à jour pour un nouveau bloc \\(x^{(t)}\\) avec les statistiques locales \\(\tilde{m}_t, \tilde{\ell}_t\\) :
    \\[
    m_i^{\new} = \max(m_i, \tilde{m}_t), \quad \ell_i^{\new} = e^{m_i - m_i^{\new}} \ell_i + e^{\tilde{m}_t - m_i^{\new}} \tilde{\ell}_t.
    \\]
    Le softmax partiel est alors \\(\tilde{P}_{ij} = \exp(S_{ij} - m_i^{\new})\\), et la sortie s'accumule comme \\(O_i \leftarrow \frac{\ell_i}{\ell_i^{\new}} e^{m_i - m_i^{\new}} O_i + \frac{\tilde{\ell}_t}{\ell_i^{\new}} e^{\tilde{m}_t - m_i^{\new}} \tilde{P}_{ij} V_j\\).

    Ceci est numériquement stable (correspond au softmax fusionné) et exact, comme prouvé par induction : après tous les blocs, \\(O = \softmax(S) V\\).

Ces idées réduisent la **mémoire à \\(O(N)\\)** (entrées + sortie + statistiques \\(O(N)\\) comme \\(m, \ell\\)) et les **accès HBM à \\(O(N^2 d / M)\\)**—sous-quadratique, car chaque élément \\(K/V\\) est lu une fois, et \\(Q/O\\) est lu \\(T_c \approx N d / M\\) fois.

### Passe avant : Calcul bloc par bloc

La passe avant (pseudocode dans l'algorithme 2 de l'article) itère sur les blocs-colonnes de \\(K, V\\) :

- Initialiser \\(O = 0^{N \times d}\\), \\(m = -\infty^N\\), \\(\ell = 0^N\\) dans la HBM.
- Pour chaque bloc-colonne \\(j = 1\\) à \\(T_c\\) :
  - Charger \\(K_j, V_j\\) dans la SRAM (réutilisation entre les lignes).
  - Pour chaque bloc-ligne \\(i = 1\\) à \\(T_r\\) :
    - Charger \\(Q_i, O_i, m_i, \ell_i\\) dans la SRAM.
    - Calculer le \\(S_{ij} = \tau Q_i K_j^T\\) local (\\(B_r \times B_c\\)).
    - Masquage : \\(S_{ij}^{\masked} = \mask(S_{ij})\\) (par exemple, causal : triangle inférieur à \\(-\infty\\)).
    - Statistiques softmax locales : \\(\tilde{m}_{ij} = \rowmax(S_{ij}^{\masked})\\), \\(\tilde{P}_{ij} = \exp(S_{ij}^{\masked} - \tilde{m}_{ij})\\), \\(\tilde{\ell}_{ij} = \rowsum(\tilde{P}_{ij})\\).
    - Mettre à jour les statistiques globales et la sortie en utilisant les formules ci-dessus, en appliquant le dropout à \\(\tilde{P}_{ij}\\).
    - Écrire les \\(O_i, m_i, \ell_i\\) mis à jour dans la HBM.

Ceci fusionne tout : le total des FLOPs reste \\(O(N^2 d)\\), mais les E/S chutent considérablement (par exemple, 9x moins d'accès que la version standard). Pour l'attention causale, le masquage est peu coûteux (vectorisé). Le dropout utilise un état RNG partagé \\(R\\) sauvegardé pour la passe arrière.

### Passe arrière : Calcul du gradient par recalcul

La passe arrière (Algorithme 4) est plus délicate, car les gradients dépendent de \\(P\\) :

\\[
dP = dO \cdot V^T, \quad dS = P \odot (dP - \rowsum(dO \odot O)), \quad dQ = dS \cdot K, \quad dK = Q^T \cdot dS, \quad dV = P^T \cdot dO.
\\]

Stocker \\(P\\) serait \\(O(N^2)\\), donc FlashAttention **recalcule les blocs à la volée** (recalcul sélectif, comme le point de contrôle mais en tuiles) :

- Itérer de manière similaire : pour chaque \\(j\\), charger \\(K_j, V_j\\) ; initialiser les \\(dK_j, dV_j = 0\\) locaux.
- Pour chaque \\(i\\) : recalculer \\(S_{ij}, P_{ij}\\) en utilisant les \\(m_i, \ell_i\\) sauvegardés ; régénérer le masque de dropout à partir de \\(R\\).
- Calculer les gradients locaux : \\(dV_j += P_{ij}^{dropped^T} dO_i\\), \\(dP_{ij} = dO_i V_j^T \odot Z_{ij}\\) (masque de dropout), \\(dS_{ij} = P_{ij} \odot (dP_{ij} - D_i)\\) où \\(D_i = \rowsum(dO_i \odot O_i)\\).
- Accumuler \\(dQ_i += \tau dS_{ij} K_j\\), \\(dK_j += \tau Q_i^T dS_{ij}\\).

Ceci utilise encore \\(O(N^2 d)\\) FLOPs mais seulement \\(O(N)\\) mémoire supplémentaire (pas de stockage de \\(P\\)). Total avant + arrière : ~2-3x les FLOPs de la version standard mais 2-4x plus rapide en raison des économies d'E/S.

### Conscience des E/S et optimisations GPU

Les GPU ont une hiérarchie : registres/SRAM (rapide, petit) >> HBM (lent, grand). L'attention standard sature la HBM avec \\(\Theta(N^2)\\) accès par passe. Le tiling de FlashAttention garantit :
- \\(K, V\\) chargés une fois (\\(O(N d)\\)).
- \\(Q, O\\) chargés \\(T_c \approx N / B_c \approx N d / M\\) fois (\\(O(N^2 d / M)\\)).
- Borne inférieure : Aucun algorithme exact ne bat \\(\Omega(N^2 d^2 / M)\\) pour la plage moyenne de \\(M\\).

Empirique : Sur A100, les blocages HBM dominent le temps d'exécution ; FlashAttention les réduit de 50 à 80 %, atteignant le régime limité par le calcul. Il prend en charge la parcimonie par blocs (ignorer les blocs de masque nuls) pour des gains encore plus importants (2-4x sur le dense).

### Avantages : Vitesse, Mémoire et Impact en aval

- **Mémoire** : Linéaire \\(O(N d)\\), permettant des séquences de 64k+ sur des GPU uniques (contre 2k-4k standard). Par exemple, 13 Go à \\(N=65k\\) contre 200+ Go standard.
- **Vitesse** : 2-4x de bout en bout sur l'entraînement GPT/BERT ; jusqu'à 7x sur l'attention brute. Par exemple, combiné fwd/bwd : 0,43 ms à \\(N=128\\) à 9s à \\(N=65k\\) (contre OOM PyTorch).
- **Qualité** : Exacte, donc pas de baisse de perplexité. Permet des contextes plus longs : gain de perplexité de 0,7 point sur GPT-2 à une longueur 4x ; état de l'art sur les tâches de documents longs (par exemple, 63 % sur Path-256 à 64k séquences).
- **Extensions** : FlashAttention-2 (2023) ajoute un meilleur parallélisme (jusqu'à 2x plus rapide) ; FlashAttention-3 (2024) utilise l'asynchronisme/la faible précision pour H100 (50 % plus rapide).

### Intégration PyTorch : Utilisation transparente

PyTorch 2.0+ intègre FlashAttention nativement via `torch.nn.functional.scaled_dot_product_attention(q, k, v)`, qui distribue automatiquement vers le noyau fusionné si les conditions sont remplies (par exemple, tenseurs contigus, dtypes supportés). Aucun CUDA personnalisé n'est nécessaire :

```python
import torch
from torch.nn.functional import scaled_dot_product_attention

q, k, v = torch.randn(1, 8, 1024, 64, device='cuda')  # batch, têtes, seq, dim
with torch.backends.cuda.sdp_kernel(enable_flash=True, enable_math=False):
    out = scaled_dot_product_attention(q, k, v, attn_mask=mask, dropout_p=0.1)
```

Cela gère le masquage/dropout ; revient au noyau mathématique si non supporté. Pour les modèles personnalisés, c'est un remplacement direct pour les boucles d'attention manuelles, offrant des accélérations de 2-3x immédiatement.

FlashAttention a révolutionné l'entraînement en contexte long, alimentant des modèles comme Llama-2 (4k→70B) et au-delà.

[FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135)  
[PyTorch 2.2: FlashAttention-v2 Integration](https://pytorch.org/blog/pytorch2-2/)  
[GitHub: Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention)