---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4.1-fast
title: Questions d'entretien pour ingénieur en IA incarnée
translated: true
type: note
---

Voici un ensemble complet de questions d'entretien conçues pour un poste d'**Ingénieur en IA Incarnée**, avec un accent particulier sur l'apprentissage de politiques visuomotrices modernes, notamment **Diffusion Policy**, **RT-2**, **ACT (Action Chunking Transformer)**, et les technologies générales d'intelligence incarnée.

### Fondements de l'IA Incarnée et Robotique
1. Quelles sont les principales différences entre l'IA incarnée et les modèles de langage/vision "désincarnés" traditionnels ?
2. Pourquoi le transfert sim-to-real est-il considérablement plus difficile dans l'IA incarnée que dans les tâches de vision par ordinateur ou de TAL ?
3. Comparez les besoins en données et les lois d'échelle que vous avez observés en IA incarnée par rapport aux LLMs ou aux modèles de fondation en vision.
4. Comment abordez-vous les questions de sécurité et de robustesse dans un déploiement robotique réel (p. ex., modes de défaillance, comportements de récupération) ?

### Diffusion Policy (UC Berkeley, Chi et al., 2023–2025)
5. Expliquez l'idée centrale de Diffusion Policy et pourquoi les modèles de diffusion sont particulièrement adaptés au contrôle visuomoteur.
6. Parcourez le processus direct/inverse lors de l'utilisation d'un modèle de diffusion comme politique. Comment le débruitage des actions est-il conditionné par les observations visuelles ?
7. Quels sont les principaux avantages de Diffusion Policy par rapport aux méthodes d'apprentissage par imitation précédentes (p. ex., cloning comportemental avec MSE, GCBC, Transformer BC) ?
8. Diffusion Policy utilise souvent un backbone U-Net avec conditionnement FiLM ou une cross-attention. Comparez ces deux méthodes de conditionnement visuel en termes de performance et de vitesse d'inférence.
9. Comment fonctionne le classifier-free guidance dans Diffusion Policy et comment affecte-t-il l'exploration par rapport à l'exploitation au moment du test ?
10. Dans les versions 2024-2025, Diffusion Policy a été combiné à du conditionnement par graphe de scène ou par langage. Comment ajouteriez-vous des objectifs de haut niveau en langage à une politique par diffusion ?
11. Quels sont les modes de défaillance courants que vous avez observés avec Diffusion Policy dans des déploiements sur robots réels et comment ont-ils été atténués ?

### RT-2 (Google DeepMind, 2023–2024)
12. Qu'est-ce que RT-2 et comment procède-t-il au co-fine-tuning d'un modèle vision-langage (PaLI-X / PaLM-E) pour en faire un générateur d'actions robotiques ?
13. Expliquez le schéma de tokenisation utilisé dans RT-2 pour les actions continues. Pourquoi discrétiser les actions en bins ?
14. RT-2 revendique des capacités émergentes (p. ex., raisonnement en chaîne, arithmétique, compréhension des symboles) transférées à la robotique. Les avez-vous reproduites ou observées en pratique ?
15. Comparez RT-2 avec OpenVLA et Octo. Dans quels scénarios préféreriez-vous RT-2 par rapport aux autres ?
16. Comment RT-2 gère-t-il les tâches à long horizon et la généralisation multi-tâches par rapport à Diffusion Policy ou ACT ?

### ACT (Action Chunking Transformer, Tony Zhao et al., 2023)
17. Quel problème le chunking d'actions résout-il dans les politiques basées sur les transformers, et pourquoi est-il critique pour le contrôle en temps réel à 10-50 Hz ?
18. Décrivez l'architecture d'ACT : comment les actions sont-elles chunkées, comment la cible latente est-elle calculée et comment la variance est-elle modélisée ?
19. Comparez ACT avec Diffusion Policy en termes d'efficacité des échantillons, de vitesse d'inférence et de taux de réussite sur des tâches riches en contacts.
20. ACT utilisait à l'origine un CVAE pour la modélisation latente ; les versions ultérieures utilisent le flow-matching ou la diffusion. Quels avantages les nouvelles versions ont-elles apportés ?

### Paysage Élargi des Politiques Visuomotrices
21. Comparez les quatre grandes familles de politiques visuomotrices en 2024-2025 :
   - Modèles séquentiels de type Transformer (ACT, Octo)
   - La famille Diffusion Policy
   - Les modèles de type VLA (RT-2, OpenVLA, Octo-Transformer)
   - Les politiques par flow-matching (p. ex., MIMo, Aurora)
22. Quand choisiriez-vous le flow-matching plutôt que la diffusion pour un robot en temps réel (p. ex., un humanoïde ou un manipulateur mobile) ?
23. Comment des modèles récents comme Octo (UC Berkeley, 2024) et OpenVLA (Stanford/PMI, 2024) combinent-ils les forces d'ACT et de RT-2 ?
24. Quel rôle voyez-vous pour les modèles de fondation (p. ex., l'intégration d'actions dans le même espace que les tokens de langage ou d'image) dans les 2 à 3 prochaines années de l'IA incarnée ?

### Questions de Conception Système et d'Ingénierie
25. Concevez un pipeline d'entraînement complet pour collecter un jeu de données de plus de 100 000 épisodes dans le monde réel pour un manipulateur mobile bimanuel en utilisant Diffusion Policy ou ACT.
26. Comment feriez-vous pour qu'une politique visuomotrice fonctionne en temps réel (≥30 Hz) sur un GPU embarqué (p. ex., Jetson Orin) tout en conservant un taux de réussite élevé ?
27. Vous avez une politique qui fonctionne parfaitement en simulation mais qui échoue complètement sur le robot réel. Quelle est votre checklist systématique de débogage ?
28. Comment ajouteriez-vous la détection de force/tactile comme modalités supplémentaires à un modèle Diffusion Policy ou RT-2 existant, basé uniquement sur la vision ?
29. Expliquez comment vous procéderiez pour une adaptation rapide (few-shot ou zero-shot) à une nouvelle instance d'objet ou à un nouvel arrière-plan en utilisant l'une de ces méthodes.

### Recherche et Directions Futures
30. Où pensez-vous que le domaine de l'IA incarnée sera en 2027 — aurons-nous des robots domestiques généralistes ? Quel est le plus grand blocage aujourd'hui ?
31. Pensez-vous que le paradigme actuel d'apprentissage par imitation + pré-entraînement à l'échelle d'Internet (OpenVLA, Octo, etc.) est suffisant pour une vraie généralisation, ou avons-nous encore besoin d'apprentissage par renforcement ou de collecte active de données ?

Ces questions couvrent un large éventail, allant des connaissances fondamentales aux détails de recherche de pointe en passant par les défis d'ingénierie pratique — parfait pour des entretiens pour des postes d'ingénieur ou de chercheur en IA incarnée de niveau intermédiaire à senior en 2025. Bonne chance pour vos entretiens !