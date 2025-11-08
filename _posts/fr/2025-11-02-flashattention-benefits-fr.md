---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Algorithme FlashAttention et ses avantages
translated: true
type: note
---

# Explication approfondie de FlashAttention (Tri Dao et al., 2022)

Court résumé au préalable : FlashAttention élimine le besoin d'allouer la matrice d'attention complète \\(N\times N\\) dans la DRAM du GPU (HBM) en calculant l'attention **bloc par bloc** dans la SRAM embarquée (registres / mémoire partagée), en fusionnant l'ensemble du pipeline d'attention en un seul noyau et en utilisant une accumulation softmax bloc par bloc numériquement correcte. Cela réduit considérablement le trafic HBM et la mémoire de \\(O(N^2)\\) à effectivement \\(O(N)\\), et en pratique offre des accélérations significatives en temps réel sur les GPU pour les longues séquences. citeturn0search0turn0search9

---

## Le problème : pourquoi l'attention standard est limitée par les E/S
L'attention auto-attention du Transformer (produit scalaire mis à l'échelle) est généralement implémentée en trois étapes :

1. calculer les scores \\(S = Q K^\top\\) (taille \\(N\times N\\)) ;  
2. calculer le softmax par ligne \\(P = \mathrm{softmax}(S)\\) ;  
3. calculer la sortie \\(O = P V\\).

Naïvement, on matérialise \\(S\\) (et souvent \\(P\\)) dans la DRAM du GPU. Pour une longueur de séquence \\(N\\), cela utilise une mémoire \\(O(N^2)\\) et conduit à deux problèmes d'E/S :
- une empreinte DRAM importante (souvent la première chose à saturer la mémoire GPU), et  
- de nombreuses lectures/écritures entre la DRAM (HBM) et la SRAM embarquée/les registres — et ces transferts HBM↔SRAM sont le véritable goulot d'étranglement sur les GPU modernes.

FlashAttention reformule l'attention comme un **problème d'E/S**, pas seulement un problème de FLOP, et vise à réduire les accès HBM. citeturn0search0

---

## Idées principales (haut niveau)
1. **Découper les matrices** \\(Q, K, V\\) en blocs qui tiennent dans la SRAM embarquée (mémoire partagée / registres).  
2. **Traiter l'attention bloc par bloc** : pour un bloc \\(Q\\) donné et un ensemble de blocs \\(K,V\\) en flux, calculer les contributions partielles à la sortie et les accumuler immédiatement — ne jamais matérialiser la matrice de scores complète \\(N\times N\\) dans la DRAM.  
3. **Tout fusionner en un seul noyau** : le noyau charge les blocs dans la SRAM, calcule \\(QK^\top\\) pour cette paire de blocs, applique la logique softmax et multiplie par le bloc \\(V\\), et écrit les sorties partielles — le tout sans allers-retours de grandes matrices intermédiaires vers la DRAM. La fusion de noyaux réduit la surcharge d'instructions et de mémoire.  
4. **Accumulation softmax bloc par bloc numériquement stable** : parce que le softmax sur toute la ligne a besoin du max et de la somme globaux, FlashAttention utilise un max courant / une somme courante (style log-sum-exp) pour combiner les contributions softmax de multiples blocs \\(K\\) exactement et stablement sans stocker toute la ligne de scores.  
5. **Rétropropagation par recalcul** : au lieu de stocker de grands intermédiaires pour la rétropropagation, recalculer l'attention avant pour chaque bloc pendant la passe arrière (échange des FLOP supplémentaires contre beaucoup moins d'E/S DRAM). Les E/S DRAM économisées donnent généralement une accélération nette puisque les E/S DRAM dominent. citeturn0search2turn0search10

Ces idées combinées produisent à la fois une réduction de la mémoire et des améliorations de vitesse en temps réel. citeturn0search0

---

## Algorithme bloc par bloc — étape par étape (avant)
Considérons une seule tête d'attention avec une longueur de séquence \\(N\\) et une dimension de tête \\(d\\). Choisissez une taille de bloc \\(B\\) pour qu'un bloc de scores \\(B\times B\\) et les blocs \\(Q\\), \\(K\\), \\(V\\) correspondants tiennent dans la SRAM.

Pour chaque bloc de requêtes \\(Q_{i}\\) (lignes \\(iB:(i+1)B\\)) :

1. Initialiser un accumulateur de sortie \\(O_i \leftarrow 0\\).  
2. Initialiser l'état de normalisation courant : `row_max` (par ligne de requête) à \\(-\infty\\), `row_sum` à 0. Ceux-ci suivent le dénominateur numériquement stable pour le softmax sur plusieurs blocs K.  
3. Pour chaque bloc clé/valeur \\(K_{j}, V_{j}\\) (colonnes \\(jB:(j+1)B\\)) :
   - Charger \\(Q_i\\), \\(K_j\\), \\(V_j\\) dans la SRAM.  
   - Calculer le bloc de scores bruts \\(S_{ij} = Q_i K_j^\top / \sqrt{d}\\) (forme \\(B\times B\\) sous forme vectorisée).
   - Pour chaque ligne dans \\(S_{ij}\\), calculer le max local de la ligne \\(m_{ij}\\) et les valeurs exponentialisées \\(\exp(S_{ij} - m_{ij})\\).  
   - Fusionner les exponentielles de ce bloc dans la normalisation courante de la ligne en utilisant l'astuce log-sum-exp :
     - Soit \\(M = \max(\text{row\_max}, m_{ij})\\).
     - Mettre à jour `row_sum` := `row_sum` · exp(row_max − M) + local_sum · exp(m_{ij} − M).
     - Définir `row_max` := \\(M\\).
   - Calculer la contribution du bloc à l'accumulateur avec les exponentielles correctement mises à l'échelle : accumuler \\(O_i \mathrel{+}= \text{(softmax-du-bloc)} \times V_j\\). (Tout est fait dans la SRAM.)
4. Après avoir traité tous les blocs K, finaliser la normalisation en utilisant row_sum et row_max pour produire les sorties softmax correctes ; écrire \\(O_i\\) dans la DRAM.

Point clé : aucune matrice \\(N\times N\\) n'est jamais écrite dans la DRAM ; seuls de petits blocs et les sorties finales le sont. L'accumulation numériquement correcte utilisant le max courant + la somme est ce qui permet aux morceaux de softmax par bloc de se combiner exactement en le même résultat qu'un softmax complet sur la ligne. citeturn0search2turn0search10

---

## Pourquoi la fusion de noyaux et le découpage SRAM gagnent en pratique
- **Moins d'accès HBM :** L'attention standard lit/écrit \\(O(N^2)\\) éléments dans la DRAM (scores, softmax). FlashAttention lit chaque élément \\(Q,K,V\\) un nombre constant de fois, et toutes les valeurs temporaires de scores/softmax ne vivent que dans la SRAM. L'analyse des E/S dans l'article montre moins d'accès HBM et des plages où FlashAttention est optimal en E/S étant donné la taille de la SRAM. citeturn0search0  
- **Les limites de latence et de bande passante comptent plus que les FLOPs :** Les GPU sont extrêmement rapides pour les multiplications-accumulations en virgule flottante ; lorsque le trafic DRAM domine le temps d'exécution, réduire les transferts DRAM compte plus que réduire les FLOPs. La fusion de noyaux supprime le trafic DRAM intermédiaire et réduit la surcharge de lancement des noyaux. citeturn0search0  
- **Compromis de la passe arrière :** Recalculer les blocs avant pendant la passe arrière augmente les FLOPs mais évite de stocker de grands intermédiaires dans la DRAM. Parce que le recalcul se produit dans la SRAM et limite le trafic DRAM, c'est un gain net en temps réel dans de nombreux cas. citeturn0search10

Les résultats empiriques de l'article et des travaux suivants montrent des accélérations multiples (par exemple, 2–7× dans leurs benchmarks rapportés selon le modèle et la longueur de séquence) et de grandes réductions de la mémoire de pointe. citeturn0search0turn0search10

---

## Détails d'implémentation importants & compromis

- **Sélection de la taille de bloc :** Le bloc \\(B\\) doit être choisi pour que l'ensemble de travail (blocs de Q, K, V, tampons de scores, accumulateurs partiels, plus de l'espace supplémentaire) tienne dans la SRAM embarquée par bloc de threads. Le \\(B\\) optimal dépend de la dimension de tête, des types de données (FP16/FP32/FP8) et de l'architecture GPU (quantité de mémoire partagée / registres). Trop petit réduit l'efficacité du calcul ; trop grand ne tiendra pas dans la SRAM. citeturn0search2

- **Stabilité numérique :** L'algorithme utilise un max courant et une somme courante par ligne (fusion log-sum-exp) pour garantir que le softmax final est égal au softmax de la matrice complète. Cela est crucial : FlashAttention est une **attention exacte** (pas une approximation) grâce à cette accumulation stable. citeturn0search0

- **Masquage & causalité :** Le masquage causal (autoregressif) est géré en ignorant simplement ou en mettant à zéro les contributions des positions masquées dans les blocs en flux et en mettant à jour la normalisation courante en conséquence. La logique bloc par bloc fonctionne toujours mais peut nécessiter un ordonnancement minutieux des blocs pour garantir que les éléments masqués ne contaminent pas les accumulateurs. citeturn0search2

- **Passe arrière et disposition mémoire :** FlashAttention stocke uniquement des métadonnées minimales (par exemple, row_max/row_sum par bloc) et recalcule les produits de blocs avant pendant la passe arrière. Les implémentations réorganisent soigneusement le travail pour maximiser la réutilisation et minimiser la pression sur les registres. citeturn0search10

- **Précision & types de données :** L'utilisation de FP16/FP8 affecte les choix de mise en mémoire tampon des blocs et d'accumulation. Certains travaux ultérieurs (FlashAttention-2 / FlashAttention-3) ajoutent des optimisations pour la précision mixte et les nouvelles fonctionnalités GPU (Hopper, H100) pour pousser plus loin l'utilisation et le débit FP. citeturn0search4turn0search11

- **Mappage du parallélisme :** Le noyau mappe les warps/blocs CTA aux blocs de requêtes ; au sein d'un CTA, les warps coopèrent pour charger les blocs K/V et calculer le matmul de blocs et les réductions. Les réductions efficaces au niveau du warp et l'utilisation d'instructions fused multiply-add sont importantes pour le débit de pointe. citeturn0search2

---

## FlashAttention vs. méthodes d'attention longue approximatives
FlashAttention conserve la sémantique d'attention **exacte** (même résultat numérique que l'attention complète jusqu'à l'arrondi en virgule flottante), tandis que de nombreuses méthodes d'attention longue approximent l'attention (parcimonie, faible rang, FAVOR+, etc.) et échangent la qualité contre de la mémoire/du temps. FlashAttention réduit plutôt le coût mémoire/E/S tout en préservant le calcul exact, donc la qualité du modèle est inchangée tandis que le débit/la mémoire s'améliorent. C'est pourquoi il est largement attrayant : aucun compromis de précision, juste un meilleur noyau bas niveau. citeturn0search0

---

## Disponibilité pratique & écosystème
- Les auteurs ont publié une implémentation (CUDA) et un dépôt maintenu avec FlashAttention et plus tard FlashAttention-2. De nombreux frameworks (Hugging Face Transformers, fourches XLA/PyTorch, implémentations basées sur Triton) appellent soit l'opérateur flash-attn, soit fournissent des noyaux fusionnés similaires. Vous pouvez utiliser l'opérateur `flash_attn` ou les bibliothèques qui l'exposent ; dans PyTorch, les versions récentes incluent également des primitives d'attention efficaces en mémoire, et les packages tiers `flash_attn` offrent une amélioration de vitesse/mémoire clé en main pour de nombreuses charges de travail. Consultez le dépôt officiel pour les installateurs et les exemples d'API. citeturn0search9turn0search4

Mise en garde : « Pas besoin de noyaux personnalisés » n'est que partiellement vrai — FlashAttention *est* un noyau fusionné personnalisé (le travail dans le dépôt) que les frameworks appellent. Les versions modernes de PyTorch peuvent inclure en interne des noyaux fusionnés comparables ou déléguer aux bibliothèques du vendeur, mais l'idée centrale nécessite une implémentation de noyau fusionné (que ce soit en CUDA, Triton ou code vendeur). La leçon importante : vous (en tant qu'utilisateur de modèle) n'avez pas à écrire ces noyaux vous-même — utilisez l'opérateur fourni. citeturn0search9turn0search7

---

## Extensions et travaux suivants
- **FlashAttention-2 (2023) :** améliore le parallélisme, le partitionnement du travail et la mise à l'échelle multicœur pour obtenir une utilisation et un débit GPU encore meilleurs. citeturn0search4  
- **FlashAttention-3 et autres travaux d'ingénierie (2024+) :** ajustements supplémentaires pour le nouveau matériel (Hopper/H100), FP8, et une utilisation TFLOP encore plus élevée. Ceux-ci poursuivent la tendance des noyaux d'attention fusionnés conscients du matériel. citeturn0search11

---

## Quand FlashAttention aide le plus (règles empiriques)
- **Longues séquences** (plusieurs milliers) ou grandes tailles de lot/tête — économise le plus de mémoire et donne les plus grandes accélérations.  
- **Lorsque la bande passante DRAM est le goulot d'étranglement** — par exemple, les grands modèles avec un grand \\(N\\) où l'attention naïve saturerait la DRAM.  
- **L'entraînement avec de grands contextes** puisque la rétropropagation adaptée au recalcul réduit la mémoire de pointe (permet des lots/contextes plus grands). citeturn0search0

---

## Pseudocode rapide (conceptuel)
```
pour chaque bloc de requêtes Qi :
    row_max = -inf (par ligne)
    row_sum = 0    (par ligne)
    out_acc = 0    (B x d_v)
    pour chaque bloc clé/valeur Kj, Vj :
        charger Qi, Kj, Vj dans SRAM
        S = Qi @ Kj.T / sqrt(d)
        m = max_ligne(S)
        expS = exp(S - m)      # exponentielles locales
        local_sum = somme_ligne(expS)
        # fusionner les normaliseurs stablement :
        M = max(row_max, m)
        row_sum = row_sum * exp(row_max - M) + local_sum * exp(m - M)
        row_max = M
        # accumuler la sortie partielle avec expS mise à l'échelle :
        out_acc += (expS / (row_sum après fusion)) @ Vj
    écrire out_acc dans DRAM
```
(L'implémentation stocke plus de métadonnées et organise la mise à l'échelle exacte soigneusement ; ci-dessus est conceptuel.) citeturn0search2

---

## Références / où lire ensuite
- Article original FlashAttention (Tri Dao et al., 2022) — algorithme, analyse E/S, benchmarks. citeturn0search0turn0search2  
- GitHub officiel avec les noyaux CUDA et les bindings PyTorch. citeturn0search9  
- Article FlashAttention-2 (Tri Dao, 2023) et notes d'ingénierie sur les versions ultérieures. citeturn0search4turn0search11

---

Si vous voulez, je peux :
- montrer une comparaison ligne par ligne d'une boucle d'attention naïve vs. le pseudocode FlashAttention bloc par bloc (pas de tableaux larges),  
- esquisser l'organisation du noyau CUDA/Triton et le budget registres/mémoire-partagée pour un exemple concret (par exemple, dimension de tête 64, bloc 128), ou  
- vous indiquer l'appel API PyTorch exact et un exemple d'extrait de code pour remplacer `torch.nn.functional.scaled_dot_product_attention` par FlashAttention. Qu'est-ce qui serait le plus utile ensuite ?