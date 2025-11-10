---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Optimisateur de Matrice à Conscience Structurelle Muon
translated: true
type: note
---

« Muon » dans Kimi fait référence à un optimiseur avancé — plus précisément un **optimiseur structurellement conscient et orthogonalisant les matrices** utilisé pour entraîner le modèle de langage Kimi K2.

---

### Qu'est-ce que l'optimiseur Muon ?

1. **Optimisation Consciente des Matrices**
   Contrairement à AdamW ou SGD, Muon traite les matrices de poids comme des entités géométriques plutôt que comme des paramètres scalaires indépendants. Il applique des **itérations de Newton–Schulz** pour orthogonaliser le gradient moyenné par momentum, produisant des mises à jour bien conditionnées et équilibrées qui respectent à la fois la structure des lignes et des colonnes de la matrice ([Medium][1], [kellerjordan.github.io][2]).

2. **Orthogonalisation via Newton–Schulz**
   Au lieu d'effectuer une décomposition en valeurs singulières (SVD) coûteuse, Muon utilise une méthode itérative rapide (Newton–Schulz) pour approximer la matrice orthogonale la plus proche du gradient. Cela maintient la mise à jour sous **contraintes de norme spectrale**, préservant l'énergie et répartissant l'apprentissage de manière égale dans toutes les directions ([Medium][1], [kellerjordan.github.io][2]).

3. **Ajustement du Pipeline**
   Le flux de mise à jour standard — **Gradient → Momentum → Mise à jour des Paramètres** — est remplacé par :
   **Gradient → Momentum → Orthogonalisation de Newton–Schulz → Mise à jour des Paramètres**.
   Cette modification améliore l'efficacité et la stabilité de l'entraînement pour les matrices de paramètres 2D ([Medium][3], [kellerjordan.github.io][2]).

4. **Efficace en Pratique**
   Bien qu'ajoutant une petite surcharge computationnelle, Muon offre des accélérations significatives :

   * Détient des records en NanoGPT speedrunning, améliorant le temps d'entraînement d'environ \~35% ([kellerjordan.github.io][2]).
   * Passe bien à l'échelle dans l'entraînement de grands modèles de langage lorsqu'il est combiné avec la décroissance de poids et les ajustements RMS par paramètre ([arXiv][4]).

5. **Fondements Théoriques Solides**
   Des recherches récentes étayent les propriétés de convergence de Muon, les bénéfices de la décroissance de poids et le dimensionnement optimal des lots. Des études confirment des bornes théoriques plus serrées et une efficacité dans divers scénarios pratiques ([arXiv][5]).

---

### Rôle de Muon dans **Kimi K2**

Kimi K2 est le **modèle Mixture-of-Experts (MoE)** de Moonshot AI, avec **1 trillion de paramètres au total** (32B activés) optimisé pour des capacités agentiques. Il a atteint des performances exceptionnelles sur des benchmarks de connaissances, de raisonnement et de codage, en partie grâce à l'entraînement avec Muon (et une variante appelée **MuonClip**) ([Hugging Face][6], [Poe][7]).

* L'**optimiseur MuonClip** fait référence à l'application de Muon à très grande échelle tout en relevant les défis de stabilité intrinsèques à de tels grands modèles ([Hugging Face][6], [Poe][7]).
* L'optimiseur a été clé pour permettre **zéro instabilité pendant l'entraînement** sur un large jeu de données de tokens (\~15,5 billions de tokens) et pour obtenir des résultats de pointe ([Hugging Face][6]).

---

### En Résumé (Pas de Tableau, Comme Demandé)

* **Muon** = « Momen**t**Um Orthogonalized by Newton–Schulz » — un optimiseur qui remplace les mises à jour brutes du gradient par des mises à jour orthogonalisées, améliorant la dynamique d'apprentissage pour les paramètres matriciels.
* Il préserve la structure, assure des mises à jour équilibrées et reste efficace grâce à l'orthogonalisation itérative au lieu de décompositions coûteuses.
* **Kimi K2** tire parti de Muon (et MuonClip) pour repousser les limites de l'entraînement MoE à grande échelle, atteignant des performances maximales avec stabilité et efficacité computationnelle.

---

Faites-moi savoir si vous souhaitez une analyse plus approfondie — par exemple, comment Muon se compare à AdamW en termes de trajectoires d'entraînement, comment MuonClip modifie l'algorithme pour les MoE, ou comment la méthode de Newton–Schulz fonctionne en code !

[1]: https://medium.com/%40gauritr01/the-truth-about-kimi-k2-pretraining-muon-optimizer-moe-unpacked-43554527d94a?utm_source=chatgpt.com "The Truth About KIMI K2 Pretraining: Muon Optimizer ..."
[2]: https://kellerjordan.github.io/posts/muon/?utm_source=chatgpt.com "Muon: An optimizer for hidden layers in neural networks"
[3]: https://medium.com/%40jenwei0312/going-beyond-adamw-a-practical-guide-to-the-muon-optimizer-93d90e91dbd3?utm_source=chatgpt.com "Going Beyond AdamW: A Practical Guide to the Muon ..."
[4]: https://arxiv.org/html/2502.16982v1?utm_source=chatgpt.com "Muon is Scalable for LLM Training"
[5]: https://arxiv.org/abs/2507.01598?utm_source=chatgpt.com "Convergence Bound and Critical Batch Size of Muon Optimizer"
[6]: https://huggingface.co/moonshotai/Kimi-K2-Base?utm_source=chatgpt.com "moonshotai/Kimi-K2-Base"
[7]: https://poe.com/Kimi-K2?utm_source=chatgpt.com "Kimi-K2"