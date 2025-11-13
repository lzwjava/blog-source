---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: L'écart entre la performance théorique et la performance réelle
translated: true
type: note
---

L'écart s'explique car le **pic théorique de FLOPS** (opérations en virgule flottante par seconde) mesure le débit arithmétique brut dans des conditions idéales—supposant une utilisation parfaite de toutes les unités d'exécution, aucune goulot d'étranglement mémoire et une bande passante infinie. Dans les charges de travail réelles (surtout en IA/entraînement/inférence), la performance est limitée par **les inefficacitités du sous-système mémoire**, et pas seulement par la puissance de calcul. Les GPU Fermi de 2010 (par exemple, la GTX 480) étaient particulièrement mauvais à ce niveau, gonflant l'écart "attendu" par rapport aux cartes modernes comme la RTX 4090.

### Raisons Clés de la Sous-Utilisation des FLOPS Théoriques par Fermi
1. **Hiérarchie de cache médiocre et coalescence mémoire**  
   - Fermi n'avait que 64 Ko de cache L1 par SM (partagé avec les registres) et un minuscule cache L2 de 768 Ko (pour la puce entière).  
   - Aucune cohérence de cache appropriée ; les accès à la mémoire globale n'étaient pas coalescés → **bande passante effective d'environ 10–30 %** dans les noyaux réels.  
   - Les GPU modernes (Ampere/Ada) ont **un cache L1 massif (192 Ko/SM)**, **des caches de texture dédiés** et **une prélecture agressive**, atteignant 70–90 % de la bande passante théorique.

2. **DDR5/GDDR5 ECC à haute latence et faible bande passante**  
   - Fermi : ~170 Go/s GDDR5, **bus 384 bits mais pénalité ECC** → effectif ~130 Go/s.  
   - RTX 4090 : **1 To/s GDDR6X**, 384 bits mais **pas de taxe ECC en mode consommateur**, plus **une meilleure compression**.  
   - Les noyaux d'IA réels sont **limités par la mémoire** (par exemple, GEMM avec de grandes matrices) ; les FLOPS n'ont pas d'importance si les données sont en attente.

3. **Fichier de registres et ordonnancement de warp inefficaces**  
   - Fermi : 32k registres 32 bits/SM → **max 1536 threads** mais seulement **~50 % d'occupation** en pratique à cause du déversement de registres.  
   - Ada : Fichier de registres de 256 Ko → **2048 threads/SM**, occupation proche de 100 %.  
   - Moins de divergence, meilleure extraction de l'ILP.

4. **L'imbrication puissance/thermique**  
   - GTX 480 : TDP 250 W, **forte imbrication sous charge soutenue** (les horloges baissaient de 10–20 %).  
   - RTX 4090 : 450 W mais **~3x meilleures perf/W** grâce au procédé 4nm, DLSS et boost dynamique.

### Gains Réels Mesurés (Charges de Travail IA)

| Métrique | GTX 480 (Fermi, 2010) | RTX 4090 (Ada, 2022) | Accélération |
|--------|------------------------|----------------------|---------|
| TFLOPS FP32 (pic) | 1,35 | 82,6 | **61x** |
| TFLOPS FP16 (pic) | ~0,7 (émulé) | 330 (Tensor) | **>400x** |
| **Entraînement ResNet-50 (img/s)** | ~60 | ~1 050 | **~17x** |
| **Inférence GPT-2 (tokens/s)** | ~8 | ~140 | **~17x** |
| **Stable Diffusion (it/s)** | <0,1 | ~1,6 | **>16x** |

*Sources : Documents NVIDIA, benchmarks MLPerf, AnandTech.*

### Conclusion
Les FLOPS théoriques supposaient que Fermi pouvait maintenir ~70 % d'utilisation—ce n'était pas le cas (réel ~15–25 %). Les architectures modernes réduisent cet écart à **~70–90 %**, donc **le calcul effectif s'aligne mieux sur la loi de Moore + les améliorations architecturales** (~10–17x sur 12 ans), et non sur les 60x+ suggérés par le pic de FLOPS. Le reste est de la « performance sur le papier ».