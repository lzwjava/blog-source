---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Évolution des performances des GPU NVIDIA
translated: true
type: note
---

### Cartes graphiques NVIDIA : Les modèles phares DirectX 11 de 2010 face aux cartes RTX modernes

Vers 2010, les cartes graphiques grand public haut de gamme de NVIDIA supportant DirectX 11 étaient la **GeForce GTX 480** (lancée en mars 2010, première carte DX11) et la **GTX 580** (novembre 2010, la plus rapide de son époque). Elles étaient basées sur l'architecture Fermi, avec 480 à 512 cœurs CUDA, 1,5 Go de mémoire GDDR5 et une TDP d'environ 250 W.

Comparaisons modernes : **RTX 3090** (Ampere, 2020), **RTX 4070** (Ada Lovelace, 2023) et **RTX 4090** (Ada Lovelace, 2022). **Aucun RTX 4090 Ti n'a jamais été commercialisé** — il a été rumeur en 2023 mais annulé, sans aucune mise à jour même jusqu'en 2025.

#### TFLOPS FP32 (Performance théorique de crête en simple précision)
Cela mesure la puissance de calcul brute des shaders (plus élevé = meilleurs TFLOPS théoriques).

| Carte graphique | Architecture | TFLOPS FP32 | Multiplicateur vs. GTX 480 |
|-----------------|--------------|-------------|----------------------------|
| GTX 480         | Fermi        | 1,345       | 1x                         |
| GTX 580         | Fermi 2.0    | 1,581       | 1,18x                      |
| RTX 4070        | Ada          | 29,15       | 21,7x                      |
| RTX 3090        | Ampere       | 35,58       | 26,5x                      |
| RTX 4090        | Ada          | 82,58       | 61,4x                      |

Les cartes modernes offrent **20 à 60 fois** plus de FLOPS bruts, grâce à des nombres de cœurs massifs (5 888 à 16 384 shaders), des fréquences d'horloge plus élevées et une efficacité architecturale.

#### Performance en situation réelle (Relative à RTX 4090 = 100 %)
- **Performance Relative TechPowerUp** : Moyenne sur plus de 1 000 jeux/benchmarks (centrés sur le rasterization 1080p/1440p). Les architectures plus récentes excellent davantage dans les charges réelles grâce à une meilleure planification, la mise en cache et des fonctionnalités comme le DLSS/RT.
- **PassMark G3D Mark** : Benchmark synthétique agrégé (moyenne des scores soumis par les utilisateurs).

| Carte graphique | Performance Relative TechPowerUp (RTX 4090 = 100 %) | PassMark G3D Mark (Moy.) | Multiplicateur vs. GTX 480 (PassMark) |
|-----------------|-----------------------------------------------------|--------------------------|---------------------------------------|
| GTX 480         | 6 %                                                 | ~4 075                   | 1x                                    |
| GTX 580         | ~7 %                                                | ~4 500                   | ~1,1x                                 |
| RTX 4070        | 53 %                                                | ~26 900                  | ~6,6x                                 |
| RTX 3090        | 58 %                                                | ~26 600                  | ~6,5x                                 |
| RTX 4090        | 100 %                                               | ~38 400                  | ~9,4x                                 |

- **Points clés à retenir** :
  - **Les FLOPS théoriques surestiment les gains** : La performance réelle n'est "que" **10 à 17 fois** plus rapide pour la RTX 4090 par rapport aux cartes de 2010, en raison des inefficacités de Fermi (mauvaise mise en cache, puissance/chaleur élevées).
  - Dans les jeux modernes (1440p/4K, DX12 Ultimate, lancer de rayons) : Les multiplicateurs sont **20 à 50 fois+** plus élevés, car les anciennes cartes peinent avec les limites de VRAM (1,5 Go vs 12–24 Go) et l'absence de RT/DLSS.
  - Efficacité énergétique : La RTX 4090 (450 W) offre environ 4 fois plus de performance par watt que la GTX 480 (250 W).
  - Exemple de jeu : Dans les titres de 2010, la GTX 480 atteignait ~60 FPS en 1080p haute qualité. La RTX 4090 fait aujourd'hui du 4K ultra + RT à plus de 200 FPS.

**Références**:
- [TechPowerUp GTX 480 Specs](https://www.techpowerup.com/gpu-specs/geforce-gtx-480.c268)
- [TechPowerUp GTX 580 Specs](https://www.techpowerup.com/gpu-specs/geforce-gtx-580.c270)
- [TechPowerUp RTX 3090 Specs](https://www.techpowerup.com/gpu-specs/geforce-rtx-3090.c3622)
- [TechPowerUp RTX 4070 Specs](https://www.techpowerup.com/gpu-specs/geforce-rtx-4070.c3924)
- [TechPowerUp RTX 4090 Specs](https://www.techpowerup.com/gpu-specs/geforce-rtx-4090.c3889)
- [PassMark Video Card Benchmarks](https://www.videocardbenchmark.net)