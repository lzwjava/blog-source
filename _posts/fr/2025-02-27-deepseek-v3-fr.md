---
audio: false
generated: true
lang: fr
layout: post
title: DeepSeek V3
translated: true
type: note
---

### Aperçu et points clés
1. **Nom du modèle** : DeepSeek-V3, un modèle de langage de type Mixture-of-Experts (MoE) avec 671 milliards de paramètres, dont 37 milliards sont activés par token.
2. **Jeu de données d'entraînement** : Pré-entraîné sur 14,8 billions de tokens diversifiés et de haute qualité.
3. **Innovations principales** : Intègre les architectures Multi-Head Latent Attention (MLA) et DeepSeekMoE avec un équilibrage de charge sans perte auxiliaire pour l'efficacité.
4. **Efficacité de l'entraînement** : Atteint un entraînement complet avec seulement 2,788 millions d'heures GPU H800.
5. **Efficacité des coûts** : Le coût de l'entraînement est estimé à 5,576 millions USD, en supposant 2 USD par heure GPU.

---

### Innovations architecturales
6. **Cadre basé sur Transformer** : Conserve l'architecture Transformer pour l'évolutivité et la flexibilité.
7. **Multi-Head Latent Attention (MLA)** : Réduit la mémoire d'inférence en compressant les caches clé-valeur sans perte de performance.
8. **DeepSeekMoE** : Utilise une combinaison d'experts partagés et routés pour un entraînement rentable et une haute efficacité computationnelle.
9. **Équilibrage de charge sans perte auxiliaire** : Introduit des termes de biais pour maintenir des charges d'experts équilibrées sans compromettre les performances.
10. **Prédiction multi-tokens (MTP)** : Prédit séquentiellement plusieurs tokens par position, améliorant l'efficacité des données et la pré-planification des représentations.

---

### Cadre d'entraînement
11. **Entraînement en précision mixte FP8** : Exploite la quantification fine et le stockage en faible précision pour optimiser la mémoire et le calcul.
12. **Algorithme DualPipe** : Chevauche les phases de calcul et de communication, réduisant les bulles de pipeline et améliorant le parallélisme.
13. **Communication inter-nœuds efficace** : Utilise des noyaux optimisés pour les opérations all-to-all, exploitant les bandes passantes NVLink et InfiniBand.
14. **États de l'optimiseur en faible précision** : Stocke les états de l'optimiseur en BF16, réduisant la consommation mémoire sans perte de performance.
15. **Techniques d'optimisation de la mémoire** : Recalcule certaines opérations (par exemple, RMSNorm) pendant la rétropropagation pour économiser la mémoire.

---

### Détails du pré-entraînement
16. **Processus d'entraînement stable** : Aucun pic de perte irrécupérable ou retour en arrière ne s'est produit pendant le pré-entraînement.
17. **Extension de la longueur de contexte** : Longueur de contexte étendue à 32K puis à 128K en deux étapes.
18. **Coûts d'entraînement** : Le pré-entraînement a requis 2,664M d'heures GPU, l'extension de contexte 119K heures GPU et le post-entraînement 5K heures GPU.
19. **Efficacité des tokens** : L'efficacité de l'entraînement assurée en minimisant les heures GPU par billion de tokens.
20. **Données de haute qualité** : Jeu de données de pré-entraînement organisé pour la diversité et la pertinence.

---

### Améliorations post-entraînement
21. **Affinage supervisé (SFT)** : Aligne les sorties du modèle avec les préférences humaines.
22. **Apprentissage par renforcement (RL)** : Utilise Group Relative Policy Optimization pour l'affinage.
23. **Distillation des connaissances** : Intègre les capacités de raisonnement des modèles DeepSeek-R1.
24. **Contrôle du style de sortie** : Équilibre la précision avec la longueur et le style de génération.
25. **Affinage des performances** : Le post-entraînement améliore encore les résultats des benchmarks.

---

### Performances sur les benchmarks
26. **MMLU (Benchmarks éducatifs)** : Atteint 88,5, surpassant les autres modèles open source.
27. **GPQA (Connaissances générales)** : Score de 59,1, comparable à GPT-4o et Claude-3.5-Sonnet.
28. **Benchmarks mathématiques** : Performance de pointe dans les tâches de raisonnement mathématique.
29. **Compétitions de code** : Excelle dans les benchmarks de codage tels que LiveCodeBench.
30. **Connaissances factuelles** : Démontre des résultats supérieurs dans les benchmarks de factualité en anglais et chinois.

---

### Inférence et déploiement
31. **Étape de pré-remplissage** : Combine le parallélisme de tenseurs (TP4), le parallélisme de séquences (SP) et le parallélisme d'experts (EP32) pour l'efficacité.
32. **Étape de décodage** : Utilise EP320 avec IBGDA pour une communication à faible latence.
33. **Redondance dynamique** : Ajuste dynamiquement les charges des experts pour optimiser l'utilisation des ressources.
34. **Séparation des étapes** : Les étapes de pré-remplissage et de décodage sont séparées pour améliorer le débit.
35. **Utilisation du matériel** : Optimisé pour les GPU H800 avec interconnexions NVLink et InfiniBand.

---

### Innovations dans l'équilibrage de charge et le décodage
36. **Routage basé sur le biais** : Introduit des termes de biais pour assurer dynamiquement des charges d'experts équilibrées.
37. **Décodage spéculatif** : Améliore la latence de génération en utilisant les modules MTP.
38. **Experts redondants** : Duplique les experts à charge élevée pour équilibrer les charges de travail GPU.
39. **Routage limité aux nœuds** : Restreint le routage des tokens à un maximum de 4 nœuds pour réduire la surcharge de communication.
40. **Aucun abandon de token** : Garantit que tous les tokens sont conservés pendant l'entraînement et l'inférence.

---

### Détails techniques
41. **Configuration du cluster** : Entraîné sur un cluster avec 2048 GPU NVIDIA H800.
42. **Parallélisme de pipeline** : Utilise un schéma de parallélisme à 16 voies pour l'évolutivité.
43. **Empreinte mémoire** : Évite le parallélisme de tenseurs coûteux en optimisant l'utilisation de la mémoire.
44. **Noyaux personnalisés** : Développe des noyaux de communication spécialisés pour gérer efficacement les opérations inter-nœuds.
45. **Optimisation en précision mixte** : Combine les formats FP8 et BF16 pour une dynamique d'entraînement optimale.

---

### Évaluation et résultats
46. **Benchmarks complets** : Évalué dans divers domaines incluant l'éducation, le codage et le raisonnement.
47. **Leadership open source** : Se positionne comme le modèle de base open source le plus puissant dans sa catégorie.
48. **Comparaison avec les modèles privateurs** : Performance comparable à GPT-4o et Claude-3.5-Sonnet.
49. **Force dans les connaissances chinoises** : Surpasse les modèles leaders dans les benchmarks de factualité chinois.
50. **Gestion des contextes longs** : Excelle dans les tâches nécessitant un traitement de contexte étendu.

---

### Orientations futures
51. **Exploration de la redondance dynamique** : Investigation de stratégies de redondance plus adaptatives.
52. **Expansion du décodage spéculatif** : Exploration des utilisations supplémentaires de MTP pour l'accélération de l'inférence.
53. **Co-conception matérielle** : Adaptation aux GPU de nouvelle génération pour des performances accrues.
54. **Couverture élargie des benchmarks** : Extension des évaluations à des tâches plus diversifiées.
55. **Durabilité** : Réduction supplémentaire des coûts d'entraînement via des optimisations algorithmiques et matérielles.

---

Ce document fournit un résumé complet de DeepSeek-V3, incluant son architecture, ses méthodologies d'entraînement, ses performances sur les benchmarks et ses perspectives futures. Faites-moi savoir si vous avez besoin de plus de détails sur des sections spécifiques ou des points supplémentaires !