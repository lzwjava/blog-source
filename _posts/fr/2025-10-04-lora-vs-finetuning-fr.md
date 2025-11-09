---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Performances du réglage fin LoRA par rapport au réglage fin complet
translated: true
type: note
---

### Aperçu des performances de LoRA par rapport au Fine-Tuning Complet

D'après l'analyse empirique de Thinking Machines Lab, LoRA (Low-Rank Adaptation) offre un fine-tuning efficace en paramètres qui égale souvent le fine-tuning complet (FullFT) dans des scénarios à capacité limitée, comme les petits jeux de données ou l'apprentissage par renforcement (RL), mais ses performances se dégradent sur des jeux de données plus volumineux en raison de limitations intrinsèques de la dynamique d'entraînement.[1] Cette section détaille chaque constat, en expliquant les mécanismes, les preuves et les implications pratiques pour les développeurs de modèles.

### Équivalence sur les jeux de données de raisonnement et d'ajustement aux instructions de petite à moyenne taille

LoRA atteint une performance équivalente à FullFT lors du fine-tuning sur des jeux de données allant jusqu'à une taille modérée, tels que ceux utilisés pour le suivi d'instructions (par exemple, les jeux de données de style Alpaca) ou les tâches de raisonnement (par exemple, les problèmes mathématiques GSM8K). Cette équivalence survient parce que ces jeux de données contiennent typiquement entre 10 000 et 100 000 exemples, ce qui correspond bien à la capacité de paramétrisation de faible rang de LoRA. LoRA approxime les mises à jour des poids comme une décomposition matricielle de faible rang (ΔW = B A, où B et A sont des matrices de faible rang), ce qui suffit à capturer les changements comportementaux étroits nécessaires pour de telles tâches sans avoir besoin de l'expressivité totale offerte par la mise à jour de tous les paramètres.

En pratique, cela signifie que les développeurs peuvent utiliser LoRA pour effectuer le fine-tuning de grands modèles (par exemple, 70B+ paramètres) sur du matériel grand public ou des instances cloud à mémoire limitée, en atteignant les mêmes métriques en aval, comme la précision ou la perplexité, qu'avec FullFT. Par exemple, sur des jeux de données comme Dolly-15k pour les instructions, LoRA avec un rang de 8 à 16 donne des résultats indiscernables, économisant jusqu'à 99 % des paramètres entraînables et du temps d'entraînement.[1] Cependant, cela ne vaut que si le jeu de données n'exige pas une généralisation au-delà de la distribution d'entraînement—les risques de surapprentissage restent similaires à ceux de FullFT.

### Sous-performance sur les grands jeux de données dépassant la capacité de LoRA

Lorsque les jeux de données dépassent la capacité effective de LoRA (par exemple, des millions d'exemples pour l'adaptation à un domaine spécifique comme la génération de code sur The Stack), LoRA est à la traîne par rapport à FullFT. Le problème clé n'est pas un "plafond de capacité" dur où la perte stagne brusquement ; au lieu de cela, LoRA présente une efficacité d'entraînement réduite, avec une convergence de la perte plus lente liée à l'inadéquation entre le goulot d'étranglement de faible rang et l'échelle du jeu de données.

Cela découle du biais inductif de LoRA : la forme produit-de-matrices (W' = W + γ B A) contraint les mises à jour à un sous-espace, ce qui fonctionne pour des changements clairsemés et de faible dimension mais peine avec les signaux à haute variance des grands jeux de données. Empiriquement, les courbes de perte montrent que LoRA nécessite 2 à 5 fois plus d'étapes pour atteindre des niveaux proches de FullFT, et même alors, la performance finale peut être inférieure de 5 à 10 % sur des benchmarks comme HumanEval pour le codage.[1] La relation est paramétrique : l'efficacité diminue à mesure que la taille du jeu de données augmente plus vite que le rang de LoRA (r), ce qui suggère qu'augmenter r aide marginalement mais ne compense pas entièrement sans risquer le surapprentissage dans des régimes à faible quantité de données.

Les implications incluent la préférence pour FullFT (ou des hybrides comme QLoRA) pour les corpus massifs, tandis que LoRA brille dans le prototypage itératif. Cela souligne également la nécessité d'estimer la taille du jeu de données avant de choisir les méthodes—des outils comme les décomptes de tokens peuvent guider cette décision.

### Sensibilité aux grandes tailles de lot et effets de paramétrisation

LoRA montre une plus grande intolérance aux grandes tailles de lot par rapport à FullFT, avec des pénalités de perte apparaissant brusquement au-delà des points optimaux (par exemple, taille de lot > 512). Alors que le bruit du gradient de FullFT s'ajuste plus gracieusement, la configuration produit-de-matrices de LoRA amplifie la variance dans les mises à jour de faible rang, conduisant à une optimisation instable. Cette pénalité persiste même si le rang est augmenté, car elle est enracinée dans les propriétés différentes du Hessien de la forme bilinéaire par rapport à l'optimisation directe des poids.

Par exemple, dans des expériences sur des jeux de données de raisonnement, la perte de LoRA augmente 20 à 30 % plus vite avec des tailles de lot supérieures à 1000, alors que FullFT se stabilise via une moyenne des paramètres plus large.[1] Les stratégies d'atténuation incluent l'accumulation de gradients pour simuler des lots effectifs plus petits ou l'utilisation de techniques comme AdamW avec une planification minutieuse du taux d'apprentissage. Cette dynamique souligne le compromis de LoRA : l'efficacité en mémoire mais la fragilité dans la mise à l'échelle du parallélisme de calcul, le rendant moins idéal pour les clusters d'entraînement à haut débit.

### Avantages de l'application de LoRA à toutes les couches, en particulier les MLP et MoE

Même sur de petits jeux de données, l'application universelle de LoRA (aux couches d'attention, MLP et Mixture-of-Experts) surpasse les variantes limitées à l'attention, particulièrement lorsque le nombre de paramètres est égalisé via des rangs plus élevés. LoRA limité à l'attention, courant dans les premières implémentations, sous-performe de 3 à 7 % sur des tâches comme le raisonnement multi-sauts car il néglige les couches feed-forward (MLP/MoE), qui gèrent la plupart des transformations non linéaires et l'intégration des connaissances spécifiques au domaine.

LoRA sur toutes les couches exploite l'architecture du modèle de manière plus holistique : les MLP contribuent à environ 70 % des paramètres et capturent les calculs spécifiques aux tâches, tandis que les MoE (dans des modèles comme Mixtral) bénéficient d'adaptations spécifiques aux routes. Égaliser les paramètres en augmentant uniquement le rang de l'attention échoue en raison de la redondance dans les têtes d'attention, conduisant à des sous-espaces inefficaces. Bonnes pratiques : Utiliser un rang de 16 à 64 sur toutes les couches pour les petites données, produisant des gains en efficacité et en évaluations sans calcul supplémentaire.[1] Cette constatation encourage une adoption plus large dans des bibliothèques comme PEFT, réduisant la "taxe LoRA" dans les architectures spécialisées.

### Équivalence dans l'Apprentissage par Renforcement avec des rangs faibles

LoRA est équivalent à FullFT dans le fine-tuning en RL (par exemple, RLHF ou DPO sur des jeux de données de préférence), même à des rangs très faibles (r=4–8), en raison des exigences de capacité intrinsèquement faibles du RL. D'un point de vue informationnel, les mises à jour du RL se concentrent sur la modélisation de la récompense et les gradients de politique sur des trajectoires clairsemées, dépassant rarement la puissance de représentation des deltas de faible rang—contrairement aux prédictions de tokens denses de l'apprentissage supervisé.

Anticipé par la théorie, cela tient parce que les pertes en RL (par exemple, les clips PPO) mettent l'accent sur les changements directionnels du comportement, que le sous-espace de LoRA encode efficacement sans pleine paramétrisation. Les expériences confirment la parité sur des benchmarks comme HH-RLHF d'Anthropic, LoRA convergeant plus rapidement et utilisant 10 fois moins de mémoire.[1] Pour les praticiens, cela fait de LoRA un choix par défaut pour les pipelines RL, permettant l'alignement scalable de modèles à billions de paramètres sur un matériel modeste.

### Implications plus larges et recommandations

Ces insights révèlent LoRA comme un outil pragmatique pour la plupart des besoins post-entraînement, surtout dans des environnements aux ressources limitées, mais pas comme un remplacement universel pour FullFT sur des données expansives. Les travaux futurs pourraient explorer des rangs adaptatifs ou une mise à l'échelle spécifique aux couches pour combler les écarts. Les développeurs devraient évaluer les performances sur l'échelle de leur jeu de données et surveiller les effets de la taille des lots dès le début.[1] Globalement, LoRA démocratise le fine-tuning sans regret dans des scénarios ciblés, s'alignant sur la transition vers un développement d'IA efficace.

Citations :
[1] https://tinker-docs.thinkingmachines.ai/lora-primer