---
audio: false
generated: false
lang: fr
layout: post
title: Organisation des ordinateurs
translated: true
type: note
---

1. Définition : L'organisation des ordinateurs désigne la structure opérationnelle et la mise en œuvre des systèmes informatiques, en se concentrant sur la manière dont les composants matériels interagissent pour exécuter des instructions.

2. Évolution historique : Retrace le développement des premiers ordinateurs mécaniques aux processeurs multicœurs modernes.

3. Architecture de Von Neumann : Un modèle fondamental où l'unité centrale, la mémoire et les entrées/sorties sont interconnectées via un bus.

4. Architecture Harvard : Sépare le stockage et les chemins de signal pour les instructions et les données, améliorant ainsi les performances.

5. Composants de l'unité centrale : Incluent l'unité arithmétique et logique (UAL), l'unité de commande et les registres.

6. Fonctions de l'UAL : Effectue des opérations arithmétiques et logiques telles que l'addition, la soustraction, ET, OU.

7. Rôle de l'unité de commande : Dirige le fonctionnement du processeur en décodant les instructions et en générant des signaux de contrôle.

8. Registres : Petites unités de stockage rapides à l'intérieur de l'unité centrale utilisées pour contenir temporairement des données et des instructions.

9. Mémoire cache : Mémoire haute vitesse située près de l'unité centrale pour réduire le temps d'accès aux données.

10. Hiérarchie mémoire : Organise la mémoire en niveaux basés sur la vitesse et le coût, incluant les registres, le cache, la RAM et le stockage secondaire.

11. RAM (Mémoire à accès aléatoire) : Mémoire volatile utilisée pour stocker les données et le code machine actuellement utilisés.

12. ROM (Mémoire morte) : Mémoire non volatile utilisée pour stocker le firmware et les instructions d'amorçage du système.

13. Structure de bus : Un système de communication qui transfère des données entre les composants à l'intérieur ou à l'extérieur d'un ordinateur.

14. Bus de données : Transporte les données réelles en cours de traitement.

15. Bus d'adresse : Transporte des informations sur l'endroit où les données doivent être envoyées ou récupérées.

16. Bus de contrôle : Transporte les signaux de contrôle de l'unité centrale vers les autres composants.

17. Architecture de jeu d'instructions (ISA) : Définit l'ensemble des instructions qu'une unité centrale peut exécuter.

18. RISC (Calcul à jeu d'instructions réduit) : Une philosophie de conception d'ISA qui utilise un petit ensemble d'instructions hautement optimisées.

19. CISC (Calcul à jeu d'instructions complexe) : Un ISA avec un large ensemble d'instructions, dont certaines peuvent exécuter des tâches complexes.

20. Pipelinage : Une technique où plusieurs phases d'instruction se chevauchent pour améliorer le débit de l'unité centrale.

21. Étapes du pipeline : Incluent généralement l'extraction, le décodage, l'exécution, l'accès mémoire et la réécriture.

22. Aléas du pipelinage : Problèmes tels que les aléas de données, les aléas de contrôle et les aléas structurels qui peuvent perturber le flux du pipeline.

23. Prédiction de branchement : Une méthode pour deviner la direction des instructions de branchement afin de maintenir le pipeline plein.

24. Architecture superscalaire : Permet de traiter simultanément plusieurs instructions dans une seule étape du pipeline.

25. Traitement parallèle : Utiliser plusieurs processeurs ou cœurs pour exécuter des instructions simultanément.

26. Processeurs multicœurs : Unités centrales avec plusieurs cœurs de traitement intégrés sur une seule puce.

27. SIMD (Instruction unique, données multiples) : Une architecture de traitement parallèle où une seule instruction opère simultanément sur plusieurs points de données.

28. MIMD (Instructions multiples, données multiples) : Une architecture parallèle où plusieurs processeurs exécutent différentes instructions sur différentes données.

29. Gestion de la mémoire : Techniques pour gérer et allouer la mémoire efficacement, incluant la pagination et la segmentation.

30. Mémoire virtuelle : Étend la mémoire physique sur le stockage disque, permettant aux systèmes de gérer des charges de travail plus importantes.

31. Pagination : Divise la mémoire en pages de taille fixe pour simplifier la gestion de la mémoire et réduire la fragmentation.

32. Segmentation : Divise la mémoire en segments de taille variable basés sur des divisions logiques comme les fonctions ou les structures de données.

33. Techniques de mappage du cache : Incluent les caches à mappage direct, entièrement associatifs et associatifs par ensemble.

34. Politiques de remplacement du cache : Détermine quelle entrée du cache remplacer, comme Moins Récemment Utilisé (LRU) ou Premier Entré, Premier Sorti (FIFO).

35. Cohérence du cache : Garantit la cohérence des données stockées dans plusieurs caches dans un système multiprocesseur.

36. Modèles de cohérence de la mémoire : Définit l'ordre dans lequel les opérations semblent s'exécuter pour maintenir la cohérence du système.

37. Systèmes d'entrée/sortie : Gère la communication entre l'ordinateur et les périphériques externes.

38. Classification des périphériques d'E/S : Inclut les périphériques d'entrée, de sortie et les unités de stockage.

39. Interfaces d'E/S : Normes comme USB, SATA et PCIe qui définissent comment les périphériques communiquent avec la carte mère.

40. Accès direct à la mémoire (DMA) : Permet aux périphériques de transférer des données vers/depuis la mémoire sans l'intervention de l'unité centrale.

41. Interruptions : Signaux qui informent l'unité centrale d'événements nécessitant une attention immédiate, permettant un traitement asynchrone.

42. Gestion des interruptions : Le processus par lequel l'unité centrale répond aux interruptions, incluant la sauvegarde de l'état et l'exécution des routines de service d'interruption.

43. Contrôleurs DMA : Composants matériels qui gèrent les opérations DMA, libérant l'unité centrale des tâches de transfert de données.

44. Pilotes de périphériques : Logiciels qui permettent au système d'exploitation de communiquer avec les périphériques matériels.

45. Interconnexion de composants périphériques (PCI) : Une norme pour connecter des périphériques à la carte mère.

46. Communication série vs parallèle : La communication série envoie les données un bit à la fois, tandis que la communication parallèle envoie plusieurs bits simultanément.

47. Ports série : Interfaces comme RS-232 utilisées pour la communication série avec les périphériques.

48. Ports parallèles : Interfaces utilisées pour la communication parallèle, souvent avec les imprimantes et autres périphériques.

49. Arbitrage du bus : Le processus de gestion de l'accès au bus entre plusieurs périphériques pour éviter les conflits.

50. Bus système vs bus périphériques : Les bus système connectent l'unité centrale, la mémoire et les composants principaux, tandis que les bus périphériques connectent les périphériques externes.

51. Table des vecteurs d'interruption : Une structure de données utilisée pour stocker les adresses des routines de service d'interruption.

52. Contrôleurs d'interruption programmables : Matériel qui gère plusieurs demandes d'interruption et les priorise.

53. Largeur du bus : Le nombre de bits qui peuvent être transmis simultanément sur un bus.

54. Fréquence d'horloge : La vitesse à laquelle une unité centrale exécute les instructions, mesurée en GHz.

55. Cycle d'horloge : L'unité de temps de base pendant laquelle une unité centrale peut effectuer une opération de base.

56. Délai d'horloge : Différences dans les temps d'arrivée du signal d'horloge dans différentes parties du circuit.

57. Distribution de l'horloge : La méthode de distribution du signal d'horloge à tous les composants de l'unité centrale.

58. Dissipation thermique : Le processus d'élimination de l'excès de chaleur de l'unité centrale pour éviter la surchauffe.

59. Solutions de refroidissement : Incluent les dissipateurs thermiques, les ventilateurs et les systèmes de refroidissement liquide utilisés pour gérer les températures de l'unité centrale.

60. Unités d'alimentation (PSU) : Fournissent l'alimentation nécessaire à tous les composants de l'ordinateur.

61. Régulateurs de tension : Garantissent que des niveaux de tension stables sont fournis à l'unité centrale et aux autres composants.

62. Architecture de la carte mère : La carte de circuit principale qui abrite l'unité centrale, la mémoire et d'autres composants critiques.

63. Jeux de puces : Groupes de circuits intégrés qui gèrent le flux de données entre l'unité centrale, la mémoire et les périphériques.

64. Firmware : Logiciel permanent programmé dans une mémoire morte qui contrôle les fonctions matérielles.

65. BIOS/UEFI : Interfaces firmware qui initialisent le matériel pendant le processus d'amorçage et fournissent des services d'exécution.

66. Processus d'amorçage : La séquence d'opérations qui initialise le système lorsqu'il est mis sous tension.

67. Étapes du pipeline d'instructions : Incluent généralement l'extraction, le décodage, l'exécution, l'accès mémoire et la réécriture.

68. Profondeur du pipeline : Le nombre d'étapes dans un pipeline, affectant le débit des instructions et la latence.

69. Équilibrage du pipeline : S'assurer que chaque étape a un temps d'exécution à peu près égal pour maximiser l'efficacité.

70. Aléas de données : Situations où les instructions dépendent des résultats d'instructions précédentes dans un pipeline.

71. Aléas de contrôle : Se produisent en raison d'instructions de branchement qui perturbent le flux du pipeline.

72. Aléas structurels : Se produisent lorsque les ressources matérielles sont insuffisantes pour supporter toutes les exécutions d'instructions possibles simultanément.

73. Forwarding (Contournement des données) : Une technique pour réduire les aléas de données en acheminant les données directement entre les étapes du pipeline.

74. Blocage (Bulles de pipeline) : Insertion de cycles d'inactivité dans le pipeline pour résoudre les aléas.

75. Exécution dans le désordre : Exécution des instructions dès que les ressources deviennent disponibles plutôt que dans l'ordre du programme d'origine.

76. Exécution spéculative : Exécution d'instructions avant de savoir si elles sont nécessaires, pour améliorer les performances.

77. Algorithmes de prédiction de branchement : Techniques comme la prédiction statique, la prédiction dynamique et la prédiction adaptative à deux niveaux utilisées pour deviner les directions de branchement.

78. Parallélisme au niveau des instructions (ILP) : La capacité d'exécuter simultanément plusieurs instructions en un seul cycle d'unité centrale.

79. Déroulage de boucle : Une technique d'optimisation qui augmente le corps des boucles pour diminuer la surcharge du contrôle de boucle.

80. Superpipelinage : Augmentation du nombre d'étapes du pipeline pour permettre des vitesses d'horloge plus élevées.

81. VLIW (Mot d'instruction très long) : Une architecture qui permet d'encoder plusieurs opérations dans un seul mot d'instruction.

82. EPIC (Calcul parallèle explicite d'instructions) : Une architecture qui permet l'exécution parallèle d'instructions grâce à l'assistance du compilateur.

83. Renommage de registres : Une technique pour éliminer les fausses dépendances de données en allouant dynamiquement des registres.

84. Hyper-Threading : Technologie d'Intel qui permet à un seul cœur d'unité centrale d'exécuter simultanément plusieurs threads.

85. Niveaux de mémoire cache : Caches L1 (le plus proche de l'unité centrale, le plus rapide), L2 et L3 avec une taille et une latence croissantes.

86. Caches write-through vs write-back : Write-through met à jour simultanément le cache et la mémoire, tandis que write-back ne met à jour que le cache et reporte les mises à jour de la mémoire.

87. Associativité dans les caches : Détermine comment les lignes de cache sont mappées aux ensembles de cache, affectant les taux de succès et les temps d'accès.

88. Préchargement : Chargement des données dans le cache avant qu'elles ne soient réellement demandées pour réduire la latence d'accès.

89. Modèles d'accès mémoire : Accès séquentiel vs aléatoire et leur impact sur les performances du cache.

90. NUMA (Accès mémoire non uniforme) : Une conception de mémoire où le temps d'accès à la mémoire varie en fonction de l'emplacement de la mémoire par rapport à un processeur.

91. SMP (Multitraitement symétrique) : Un système où plusieurs processeurs partagent une mémoire unique et centralisée.

92. Systèmes à mémoire distribuée : Systèmes où chaque processeur a sa propre mémoire privée, communiquant via un réseau.

93. Réseaux d'interconnexion : La topologie et les protocoles utilisés pour connecter plusieurs processeurs et unités de mémoire.

94. Évolutivité : La capacité d'un système informatique à augmenter ses performances en ajoutant plus de ressources.

95. Tolérance aux pannes : La capacité d'un système à continuer de fonctionner correctement en cas de défaillance de certains de ses composants.

96. Redondance : Incorporation de composants supplémentaires pour augmenter la fiabilité et la disponibilité.

97. Détection et correction d'erreurs : Techniques comme les bits de parité, les sommes de contrôle et le code correcteur d'erreurs (ECC) pour identifier et corriger les erreurs de données.

98. Efficacité énergétique : Conception de systèmes pour minimiser la consommation d'énergie tout en maintenant les performances.

99. Puissance thermique de conception (TDP) : La quantité maximale de chaleur qu'une unité centrale ou un processeur graphique est censé générer sous des charges de travail typiques.

100. Tendances futures : Exploration des avancées comme l'informatique quantique, les architectures neuromorphiques et les processeurs photoniques qui façonnent l'avenir de l'organisation des ordinateurs.