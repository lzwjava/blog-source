---
audio: false
generated: true
lang: fr
layout: post
title: Organisation des Ordinateurs
translated: true
---

1. Définition : L'organisation des ordinateurs fait référence à la structure opérationnelle et à la mise en œuvre des systèmes informatiques, en se concentrant sur la manière dont les composants matériels interagissent pour exécuter des instructions.

2. Évolution historique : Trace le développement des premiers ordinateurs mécaniques aux processeurs multicœurs modernes.

3. Architecture de von Neumann : Un modèle de base où l'UC, la mémoire et les E/S sont interconnectés via un bus.

4. Architecture Harvard : Sépare les chemins de stockage et de signalisation pour les instructions et les données, améliorant les performances.

5. Composants de l'UC : Comprend l'Unité Arithmétique et Logique (UAL), l'Unité de Contrôle (UC) et les registres.

6. Fonctions de l'UAL : Effectue des opérations arithmétiques et logiques telles que l'addition, la soustraction, ET, OU.

7. Rôle de l'Unité de Contrôle : Dirige le fonctionnement du processeur en décodant les instructions et en générant des signaux de contrôle.

8. Registres : Petits emplacements de stockage rapides au sein de l'UC utilisés pour conserver temporairement des données et des instructions.

9. Mémoire cache : Mémoire à haute vitesse située près de l'UC pour réduire le temps d'accès aux données.

10. Hiérarchie de la mémoire : Organise la mémoire en niveaux en fonction de la vitesse et du coût, y compris les registres, la mémoire cache, la RAM et le stockage secondaire.

11. RAM (Mémoire à accès aléatoire) : Mémoire volatile utilisée pour stocker les données et le code machine actuellement utilisés.

12. ROM (Mémoire morte) : Mémoire non volatile utilisée pour stocker le micrologiciel et les instructions de démarrage du système.

13. Structure du bus : Un système de communication qui transfère des données entre les composants à l'intérieur ou à l'extérieur d'un ordinateur.

14. Bus de données : Transporte les données réelles en cours de traitement.

15. Bus d'adresses : Transporte des informations sur l'endroit où les données doivent être envoyées ou récupérées.

16. Bus de contrôle : Transporte les signaux de contrôle de l'UC vers les autres composants.

17. Architecture de jeu d'instructions (ISA) : Définit l'ensemble des instructions qu'un UC peut exécuter.

18. RISC (Calcul à jeu d'instructions réduit) : Une philosophie de conception ISA qui utilise un petit ensemble d'instructions hautement optimisées.

19. CISC (Calcul à jeu d'instructions complexe) : Une ISA avec un grand ensemble d'instructions, dont certaines peuvent exécuter des tâches complexes.

20. Pipelining : Une technique où plusieurs phases d'instructions se chevauchent pour améliorer le débit de l'UC.

21. Étapes du pipeline : Comprennent généralement la récupération, le décodage, l'exécution, l'accès à la mémoire et l'écriture.

22. Hazards dans le pipelining : Problèmes comme les hazards de données, les hazards de contrôle et les hazards structurels qui peuvent perturber le flux du pipeline.

23. Prédiction de branche : Une méthode pour deviner la direction des instructions de branche afin de maintenir le pipeline plein.

24. Architecture superscalaire : Permet à plusieurs instructions d'être traitées simultanément dans une seule étape de pipeline.

25. Traitement parallèle : Utilisation de plusieurs processeurs ou cœurs pour exécuter des instructions simultanément.

26. Processeurs multicœurs : UC avec plusieurs cœurs de traitement intégrés dans une seule puce.

27. SIMD (Instruction unique, données multiples) : Une architecture de traitement parallèle où une seule instruction agit sur plusieurs points de données simultanément.

28. MIMD (Instructions multiples, données multiples) : Une architecture parallèle où plusieurs processeurs exécutent différentes instructions sur différentes données.

29. Gestion de la mémoire : Techniques pour gérer et allouer la mémoire efficacement, y compris la pagination et la segmentation.

30. Mémoire virtuelle : Étend la mémoire physique sur le stockage disque, permettant aux systèmes de gérer des charges de travail plus importantes.

31. Pagination : Divise la mémoire en pages de taille fixe pour simplifier la gestion de la mémoire et réduire la fragmentation.

32. Segmentation : Divise la mémoire en segments de taille variable en fonction de divisions logiques comme les fonctions ou les structures de données.

33. Techniques de mappage de cache : Comprennent les caches direct-mapped, fully associative et set-associative.

34. Politiques de remplacement de cache : Détermine quelle entrée de cache remplacer, comme la plus récemment utilisée (LRU) ou la première entrée première sortie (FIFO).

35. Cohérence de cache : Assure la cohérence des données stockées dans plusieurs caches dans un système multiprocesseur.

36. Modèles de cohérence de la mémoire : Définit l'ordre dans lequel les opérations semblent s'exécuter pour maintenir la cohérence du système.

37. Systèmes d'entrée/sortie : Gère la communication entre l'ordinateur et les périphériques externes.

38. Classification des périphériques d'entrée/sortie : Comprend les périphériques d'entrée, les périphériques de sortie et les périphériques de stockage.

39. Interfaces d'entrée/sortie : Normes comme USB, SATA et PCIe qui définissent comment les périphériques communiquent avec la carte mère.

40. Accès direct à la mémoire (DMA) : Permet aux périphériques de transférer des données vers/à partir de la mémoire sans intervention de l'UC.

41. Interruptions : Signaux qui notifient l'UC des événements nécessitant une attention immédiate, permettant un traitement asynchrone.

42. Gestion des interruptions : Le processus par lequel l'UC répond aux interruptions, y compris la sauvegarde de l'état et l'exécution des routines de service d'interruption.

43. Contrôleurs DMA : Composants matériels qui gèrent les opérations DMA, libérant l'UC des tâches de transfert de données.

44. Pilotes de périphériques : Logiciel qui permet au système d'exploitation de communiquer avec les périphériques matériels.

45. Interconnexion des composants périphériques (PCI) : Une norme pour connecter les périphériques à la carte mère.

46. Communication série vs parallèle : La communication série envoie des données un bit à la fois, tandis que la communication parallèle envoie plusieurs bits simultanément.

47. Ports série : Interfaces comme RS-232 utilisées pour la communication série avec les périphériques.

48. Ports parallèles : Interfaces utilisées pour la communication parallèle, souvent avec des imprimantes et autres périphériques.

49. Arbitrage de bus : Le processus de gestion de l'accès au bus parmi plusieurs périphériques pour éviter les conflits.

50. Bus système vs bus périphérique : Les bus système connectent l'UC, la mémoire et les principaux composants, tandis que les bus périphériques connectent les périphériques externes.

51. Table des vecteurs d'interruption : Une structure de données utilisée pour stocker les adresses des routines de service d'interruption.

52. Contrôleurs d'interruption programmables : Matériel qui gère plusieurs demandes d'interruption et les priorise.

53. Largeur de bus : Le nombre de bits qui peuvent être transmis simultanément sur un bus.

54. Vitesse d'horloge : Le taux auquel un UC exécute des instructions, mesuré en GHz.

55. Cycle d'horloge : L'unité de temps de base dans laquelle un UC peut effectuer une opération de base.

56. Décalage d'horloge : Différences dans les temps d'arrivée du signal d'horloge dans différentes parties du circuit.

57. Distribution d'horloge : La méthode de distribution du signal d'horloge à tous les composants dans l'UC.

58. Dissipation de chaleur : Le processus d'élimination de la chaleur excessive de l'UC pour éviter la surchauffe.

59. Solutions de refroidissement : Comprennent les dissipateurs thermiques, les ventilateurs et les systèmes de refroidissement liquide utilisés pour gérer les températures de l'UC.

60. Blocs d'alimentation (PSU) : Fournissent l'alimentation nécessaire à tous les composants de l'ordinateur.

61. Régulateurs de tension : Assurent que des niveaux de tension stables sont fournis à l'UC et aux autres composants.

62. Architecture de la carte mère : La carte de circuit imprimé principale qui abrite l'UC, la mémoire et d'autres composants critiques.

63. Jeu de puces : Groupes de circuits intégrés qui gèrent le flux de données entre l'UC, la mémoire et les périphériques.

64. Micrologiciel : Logiciel permanent programmé dans une mémoire morte qui contrôle les fonctions matérielles.

65. BIOS/UEFI : Interfaces de micrologiciel qui initialisent le matériel pendant le processus de démarrage et fournissent des services d'exécution.

66. Processus de démarrage : La séquence d'opérations qui initialise le système lorsqu'il est allumé.

67. Étapes du pipeline d'instructions : Comprennent généralement la récupération, le décodage, l'exécution, l'accès à la mémoire et l'écriture.

68. Profondeur du pipeline : Le nombre d'étapes dans un pipeline, affectant le débit des instructions et la latence.

69. Équilibrage du pipeline : Assurer que chaque étape a un temps d'exécution à peu près égal pour maximiser l'efficacité.

70. Hazards de données : Situations où les instructions dépendent des résultats des instructions précédentes dans un pipeline.

71. Hazards de contrôle : Se produisent en raison des instructions de branche qui perturbent le flux du pipeline.

72. Hazards structurels : Se produisent lorsque les ressources matérielles sont insuffisantes pour supporter toutes les exécutions d'instructions possibles simultanément.

73. Transmission directe (bypass de données) : Une technique pour réduire les hazards de données en acheminant les données directement entre les étapes du pipeline.

74. Stoppage (bulle de pipeline) : Insertion de cycles inactifs dans le pipeline pour résoudre les hazards.

75. Exécution hors ordre : Exécution des instructions lorsque les ressources deviennent disponibles plutôt que dans l'ordre du programme original.

76. Exécution spéculative : Exécution des instructions avant de savoir si elles sont nécessaires, pour améliorer les performances.

77. Algorithmes de prédiction de branche : Techniques comme la prédiction statique, la prédiction dynamique et la prédiction adaptative à deux niveaux utilisées pour deviner les directions de branche.

78. Parallélisme au niveau des instructions (ILP) : La capacité d'exécuter plusieurs instructions simultanément au sein d'un seul cycle d'UC.

79. Déroulement de boucle : Une technique d'optimisation qui augmente le corps des boucles pour diminuer le surcoût de contrôle de boucle.

80. Superpipelining : Augmentation du nombre d'étapes de pipeline pour permettre des vitesses d'horloge plus élevées.

81. VLIW (Mot d'instruction très long) : Une architecture qui permet à plusieurs opérations d'être codées dans un seul mot d'instruction.

82. EPIC (Calcul d'instructions parallèles explicites) : Une architecture qui permet l'exécution parallèle d'instructions grâce à l'assistance du compilateur.

83. Renommage de registres : Une technique pour éliminer les dépendances de données fausses en allouant dynamiquement des registres.

84. Hyper-Threading : La technologie Intel qui permet à un seul cœur d'UC d'exécuter plusieurs threads simultanément.

85. Niveaux de mémoire cache : L1 (le plus proche de l'UC, le plus rapide), L2 et L3 caches avec une taille et une latence croissantes.

86. Caches à écriture traversante vs à écriture différée : Les caches à écriture traversante mettent à jour à la fois le cache et la mémoire simultanément, tandis que les caches à écriture différée mettent à jour uniquement le cache et reportent les mises à jour de la mémoire.

87. Associativité dans les caches : Détermine comment les lignes de cache sont mappées aux ensembles de cache, affectant les taux de réussite et les temps d'accès.

88. Préchargement : Chargement de données dans le cache avant qu'elles ne soient effectivement demandées pour réduire la latence d'accès.

89. Modèles d'accès à la mémoire : Accès séquentiel vs aléatoire et leur impact sur les performances du cache.

90. NUMA (Accès non uniforme à la mémoire) : Un design de mémoire où le temps d'accès à la mémoire varie en fonction de l'emplacement de la mémoire par rapport à un processeur.

91. SMP (Multiprocessing symétrique) : Un système où plusieurs processeurs partagent une mémoire centralisée unique.

92. Systèmes de mémoire distribuée : Systèmes où chaque processeur possède sa propre mémoire privée, communiquant via un réseau.

93. Réseaux d'interconnexion : La topologie et les protocoles utilisés pour connecter plusieurs processeurs et unités de mémoire.

94. Scalabilité : La capacité d'un système informatique à augmenter les performances en ajoutant plus de ressources.

95. Tolérance aux pannes : La capacité d'un système à continuer de fonctionner correctement en cas de défaillance de certains de ses composants.

96. Redondance : Incorporation de composants supplémentaires pour augmenter la fiabilité et la disponibilité.

97. Détection et correction des erreurs : Techniques comme les bits de parité, les sommes de contrôle et le code correcteur d'erreurs (ECC) pour identifier et corriger les erreurs de données.

98. Efficacité énergétique : Conception de systèmes pour minimiser la consommation d'énergie tout en maintenant les performances.

99. Puissance thermique de conception (TDP) : La quantité maximale de chaleur qu'un UC ou GPU est censé générer sous des charges de travail typiques.

100. Tendances futures : Exploration des avancées comme le calcul quantique, les architectures neuromorphiques et les processeurs photoniques façonnant l'avenir de l'organisation des ordinateurs.