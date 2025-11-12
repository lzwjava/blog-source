---
audio: false
generated: false
lang: fr
layout: post
title: Apprentissage Automatique, Apprentissage Profond et GPT
translated: true
type: note
---

1. Le Machine Learning (ML) est un domaine de l'informatique qui permet aux systèmes d'apprendre à partir de données et d'améliorer leurs performances sans programmation explicite.

2. Le Deep Learning (DL) est un sous-domaine du ML qui utilise des réseaux de neurones multicouches pour modéliser des motifs complexes dans les données.

3. Les Réseaux de Neurones sont des modèles computationnels inspirés du cerveau humain, composés de nœuds interconnectés (neurones) qui traitent l'information en couches.

4. Les Données d'Entraînement sont l'ensemble de données étiquetées ou non étiquetées utilisé pour apprendre à un modèle de machine learning à effectuer une tâche.

5. L'Apprentissage Supervisé consiste à entraîner un modèle sur des données étiquetées, où chaque exemple a une entrée et une sortie correcte associée.

6. L'Apprentissage Non Supervisé utilise des données non étiquetées, permettant au modèle de découvrir des motifs ou des regroupements cachés sans instruction explicite.

7. L'Apprentissage par Renforcement (RL) entraîne des agents à prendre des décisions en récompensant les comportements souhaités et en pénalisant les indésirables.

8. Les Modèles Génératifs apprennent à produire de nouvelles données similaires à leurs exemples d'entraînement (par exemple, du texte, des images).

9. Les Modèles Discriminatifs se concentrent sur la classification des entrées en catégories ou sur la prédiction de résultats spécifiques.

10. Le Transfer Learning permet à un modèle entraîné sur une tâche d'être réutilisé ou affiné sur une tâche connexe.

11. GPT (Generative Pre-trained Transformer) est une famille de grands modèles de langage développés par OpenAI qui peuvent générer du texte de type humain.

12. ChatGPT est une variante interactive de GPT, affinée pour la conversation et les tâches de suivi d'instructions.

13. L'Architecture Transformer a été introduite dans l'article « Attention Is All You Need », révolutionnant le traitement du langage naturel en s'appuyant sur des mécanismes d'attention.

14. Les mécanismes d'Auto-Attention permettent au modèle de pondérer différentes parties de la séquence d'entrée lors de la construction d'une représentation de sortie.

15. L'Encodage Positionnel dans les Transformers aide le modèle à identifier l'ordre des tokens dans une séquence.

16. Le Pré-entraînement est la phase initiale où un modèle apprend des caractéristiques générales à partir de données à grande échelle avant d'être affiné sur des tâches spécifiques.

17. L'Affinage (Fine-tuning) est le processus qui consiste à prendre un modèle pré-entraîné et à l'adapter à une tâche plus spécifique en utilisant un jeu de données plus petit et propre à la tâche.

18. La Modélisation du Langage est la tâche de prédire le token suivant (mot ou sous-mot) dans une séquence, fondamentale pour les modèles de type GPT.

19. L'Apprentissage Zero-shot permet à un modèle de gérer des tâches sans exemples d'entraînement explicites, en s'appuyant sur des connaissances générales apprises.

20. L'Apprentissage Few-shot tire parti d'un nombre limité d'exemples spécifiques à une tâche pour guider les prédictions ou les comportements du modèle.

21. Le RLHF (Reinforcement Learning from Human Feedback) est utilisé pour aligner les sorties du modèle sur les préférences et valeurs humaines.

22. Le Retour Humain peut inclure des classements ou des étiquettes qui guident la génération du modèle vers des réponses plus souhaitées.

23. L'Ingénierie des Prompts est l'art de concevoir des requêtes ou des instructions d'entrée pour guider efficacement les grands modèles de langage.

24. La Fenêtre de Contexte fait référence à la quantité maximale de texte que le modèle peut traiter en une seule fois ; les modèles GPT ont une longueur de contexte limitée.

25. L'Inférence est l'étape où un modèle entraîné fait des prédictions ou génère des sorties à partir de nouvelles entrées.

26. Le Nombre de Paramètres est un facteur clé de la capacité du modèle ; les modèles plus grands peuvent capturer des motifs plus complexes mais nécessitent plus de calcul.

27. Les techniques de Compression de Modèle (par exemple, l'élagage, la quantification) réduisent la taille d'un modèle et accélèrent l'inférence avec une perte de précision minimale.

28. Les Têtes d'Attention dans les Transformers traitent différents aspects de l'entrée en parallèle, améliorant la puissance de représentation.

29. La Modélisation du Langage Masqué (par exemple, dans BERT) consiste à prédire les tokens manquants dans une phrase, aidant le modèle à apprendre le contexte.

30. La Modélisation du Langage Causal (par exemple, dans GPT) consiste à prédire le token suivant sur la base de tous les tokens précédents.

31. L'Architecture Encodeur-Décodeur (par exemple, T5) utilise un réseau pour encoder l'entrée et un autre pour la décoder en une séquence cible.

32. Les Réseaux de Neurones Convolutifs (CNNs) excellent dans le traitement des données en grille (par exemple, les images) via des couches convolutionnelles.

33. Les Réseaux de Neurones Récurrents (RNNs) traitent les données séquentielles en faisant passer des états cachés le long des pas de temps, mais ils peuvent avoir du mal avec les dépendances à long terme.

34. Le LSTM (Long Short-Term Memory) et le GRU sont des variantes de RNN conçues pour mieux capturer les dépendances à long terme.

35. La Normalisation par Lots aide à stabiliser l'entraînement en normalisant les sorties des couches intermédiaires.

36. Le Dropout est une technique de régularisation qui « désactive » aléatoirement des neurones pendant l'entraînement pour éviter le surapprentissage.

37. Les Algorithmes d'Optimisation comme la Descente de Gradient Stochastique (SGD), Adam et RMSProp mettent à jour les paramètres du modèle sur la base des gradients.

38. Le Taux d'Apprentissage est un hyperparamètre qui détermine à quel point les poids sont mis à jour de manière drastique pendant l'entraînement.

39. Les Hyperparamètres (par exemple, la taille du lot, le nombre de couches) sont des paramètres de configuration choisis avant l'entraînement pour contrôler le déroulement de l'apprentissage.

40. Le Surapprentissage (Overfitting) du modèle se produit lorsqu'un modèle apprend trop bien les données d'entraînement et échoue à généraliser sur de nouvelles données.

41. Les Techniques de Régularisation (par exemple, la décroissance de poids L2, le dropout) aident à réduire le surapprentissage et à améliorer la généralisation.

42. L'Ensemble de Validation est utilisé pour régler les hyperparamètres, tandis que l'Ensemble de Test évalue la performance finale du modèle.

43. La Validation Croisée divise les données en plusieurs sous-ensembles, en entraînant et en validant systématiquement pour obtenir une estimation de performance plus robuste.

44. Les problèmes de Gradient Explosant et de Gradient Disparaissant se produisent dans les réseaux profonds, rendant l'entraînement instable ou inefficace.

45. Les Connexions Résiduelles (skip connections) dans des réseaux comme ResNet aident à atténuer les gradients disparaissants en créant des chemins de raccourci pour les données.

46. Les Lois d'Échelle suggèrent qu'augmenter la taille du modèle et les données conduit généralement à de meilleures performances.

47. L'Efficacité de Calcul est critique ; l'entraînement de grands modèles nécessite du matériel optimisé (GPU, TPU) et des algorithmes.

48. Les Considérations Éthiques incluent les biais, l'équité et les dommages potentiels — les modèles de ML doivent être soigneusement testés et surveillés.

49. L'Augmentation de Données étend artificiellement les jeux de données d'entraînement pour améliorer la robustesse du modèle (surtout dans les tâches liées à l'image et à la parole).

50. Le Prétraitement des Données (par exemple, la tokenisation, la normalisation) est essentiel pour un entraînement efficace du modèle.

51. La Tokenisation divise le texte en tokens (mots ou sous-mots), les unités fondamentales traitées par les modèles de langage.

52. Les Embeddings Vectoriels représentent les tokens ou les concepts sous forme de vecteurs numériques, en préservant les relations sémantiques.

53. Les Embeddings Positionnels ajoutent des informations sur la position de chaque token pour aider un Transformer à comprendre l'ordre des séquences.

54. Les Poids d'Attention révèlent comment un modèle répartit son attention sur différentes parties de l'entrée.

55. La Recherche en Faisceau (Beam Search) est une stratégie de décodage dans les modèles de langage qui conserve plusieurs candidats à chaque étape pour trouver la meilleure séquence globale.

56. La Recherche Gloutonne (Greedy Search) choisit le token le plus probable à chaque étape, mais peut conduire à des sorties finales sous-optimales.

57. La Température dans l'échantillonnage ajuste la créativité de la génération de langage : température plus élevée = plus de hasard.

58. Les méthodes d'échantillonnage Top-k et Top-p (Nucleus) restreignent les tokens candidats aux k plus probables ou à une probabilité cumulative p, équilibrant diversité et cohérence.

59. La Perplexité mesure la performance d'un modèle probabiliste à prédire un échantillon ; une perplexité plus faible indique une meilleure performance prédictive.

60. La Précision et le Rappel sont des métriques pour les tâches de classification, se concentrant respectivement sur l'exactitude et l'exhaustivité.

61. Le Score F1 est la moyenne harmonique de la précision et du rappel, équilibrant les deux métriques en une seule valeur.

62. L'Exactitude (Accuracy) est la fraction des prédictions correctes, mais elle peut être trompeuse dans des jeux de données déséquilibrés.

63. L'Aire sous la Courbe ROC (AUC) mesure la performance d'un classificateur à travers différents seuils.

64. La Matrice de Confusion montre les décomptes des vrais positifs, faux positifs, faux négatifs et vrais négatifs.

65. Les méthodes d'Estimation de l'Incertitude (par exemple, Monte Carlo Dropout) évaluent la confiance d'un modèle dans ses prédictions.

66. L'Apprentissage Actif consiste à interroger de nouveaux exemples de données sur lesquels le modèle est le moins confiant, améliorant l'efficacité des données.

67. L'Apprentissage en Ligne met à jour le modèle de manière incrémentale à l'arrivée de nouvelles données, plutôt que de le réentraîner à partir de zéro.

68. Les Algorithmes Évolutifs et les Algorithmes Génétiques optimisent les modèles ou les hyperparamètres en utilisant la mutation et la sélection bio-inspirées.

69. Les Méthodes Bayésiennes intègrent des connaissances a priori et mettent à jour les croyances avec les données entrantes, utiles pour la quantification de l'incertitude.

70. Les Méthodes d'Ensemble (par exemple, Random Forest, Gradient Boosting) combinent plusieurs modèles pour améliorer les performances et la stabilité.

71. Le Bagging (Bootstrap Aggregating) entraîne plusieurs modèles sur différents sous-ensembles des données, puis moyenne leurs prédictions.

72. Le Boosting entraîne itérativement de nouveaux modèles pour corriger les erreurs commises par les modèles précédemment entraînés.

73. Les Arbres de Décision à Gradient Boosté (GBDTs) sont puissants pour les données structurées, surpassant souvent les réseaux de neurones simples.

74. Les Modèles Autoregressifs prédisent la valeur (ou le token) suivante sur la base des sorties précédentes dans une séquence.

75. L'Autoencodeur est un réseau de neurones conçu pour encoder les données en une représentation latente puis les décoder, apprenant des représentations compressées des données.

76. L'Autoencodeur Variationnel (VAE) introduit une touche probabiliste pour générer de nouvelles données qui ressemblent à l'ensemble d'entraînement.

77. Le Réseau Antagoniste Génératif (GAN) oppose un générateur à un discriminateur, produisant des images, du texte ou d'autres données réalistes.

78. L'Apprentissage Auto-Supervisé tire parti de grandes quantités de données non étiquetées en créant des tâches d'entraînement artificielles (par exemple, prédire les parties manquantes).

79. Les Modèles de Fondation (Foundation Models) sont de grands modèles pré-entraînés qui peuvent être adaptés à un large éventail de tâches en aval.

80. L'Apprentissage Multimodal intègre des données provenant de multiples sources (par exemple, texte, images, audio) pour créer des représentations plus riches.

81. L'Étiquetage des Données est souvent la partie la plus chronophage du ML, nécessitant une annotation minutieuse pour la précision.

82. L'Informatique en Périmètre (Edge Computing) rapproche l'inférence ML de la source de données, réduisant la latence et l'utilisation de la bande passante.

83. L'Apprentissage Fédéré entraîne des modèles sur des appareils ou serveurs décentralisés détenant des échantillons de données locaux, sans les échanger.

84. Le ML Préservant la Vie Privée inclut des techniques comme la vie privée différentielle et le chiffrement homomorphe pour protéger les données sensibles.

85. L'IA Explicable (XAI) vise à rendre les décisions des modèles complexes plus interprétables pour les humains.

86. Les Biais et l'Équité dans le ML nécessitent une surveillance attentive, car les modèles peuvent apprendre et amplifier involontairement des biais sociétaux.

87. La Dérive de Concept se produit lorsque les propriétés statistiques de la variable cible changent au fil du temps, impactant la performance du modèle.

88. Les Tests A/B comparent deux versions ou plus d'un modèle pour voir laquelle performe le mieux dans un environnement réel.

89. L'Accélération GPU exploite le calcul parallèle sur les cartes graphiques pour accélérer considérablement l'entraînement ML.

90. Les TPU (Tensor Processing Units) sont des accélérateurs matériels spécialisés par Google pour les charges de travail efficaces de deep learning.

91. Les Frameworks Open Source (par exemple, TensorFlow, PyTorch) fournissent des blocs de construction et des outils pour le développement de modèles ML.

92. Le Service de Modèles (Model Serving) est la pratique qui consiste à déployer des modèles entraînés afin qu'ils puissent gérer des prédictions en temps réel ou par lots.

93. L'Évolutivité (Scalability) est cruciale pour gérer de grands jeux de données ou un trafic important, nécessitant des stratégies d'entraînement et d'inférence distribuées.

94. Le MLOps combine le développement ML avec les pratiques opérationnelles, en se concentrant sur la reproductibilité, les tests et l'intégration continue.

95. Le Contrôle de Version pour les données et les modèles assure un suivi d'expérience et une collaboration cohérents.

96. Les Stratégies de Déploiement (par exemple, les conteneurs, les microservices) organisent la façon dont les modèles sont empaquetés et servis à l'échelle.

97. La Surveillance (Monitoring) suit les performances du modèle après le déploiement, en surveillant les dégradations ou les anomalies.

98. Le Réentraînement et les Mises à Jour de Modèle maintiennent les modèles à jour face aux nouvelles données et aux conditions changeantes.

99. La Complexité Temporelle (notation O) mesure comment le temps d'exécution d'un algorithme évolue avec la taille de l'entrée ; O(1) dénote un temps constant.

100. L'Avenir du ML promet des modèles de plus en plus sophistiqués et généraux, mais doit aborder les considérations éthiques, sociales et environnementales.