---
audio: false
generated: false
lang: fr
layout: post
title: Fondamentaux de l'électronique
translated: true
type: note
---

### Composants électroniques de base

1. Types de résistances : Les résistances limitent le flux de courant dans un circuit. Les types incluent les résistances fixes, qui ont une valeur de résistance fixe, et les résistances variables comme les potentiomètres, qui permettent une résistance ajustable.

2. Types de condensateurs : Les condensateurs stockent et libèrent de l'énergie électrique. Les types incluent les condensateurs céramiques, couramment utilisés pour les applications haute fréquence, et les condensateurs électrolytiques, qui ont des valeurs de capacité plus élevées mais sont polarisés.

3. Bobines (Inductances) : Les bobines stockent l'énergie dans un champ magnétique et s'opposent aux changements de courant. Elles sont utilisées dans les applications de filtrage et d'accord.

4. Diodes : Les diodes permettent au courant de circuler dans une seule direction. Les diodes Zener sont utilisées pour la régulation de tension, tandis que les LED émettent de la lumière lorsqu'elles sont polarisées en direct.

5. Transistors : Les transistors, tels que les BJT, agissent comme des interrupteurs ou des amplificateurs électroniques, les types NPN et PNP contrôlant le flux de courant dans les circuits.

6. Transistor à effet de champ (FET) : Les FET contrôlent le flux de courant en appliquant une tension à la grille, les MOSFET étant largement utilisés pour la commutation et l'amplification.

7. Photodiodes : Ces diodes génèrent un courant lorsqu'elles sont exposées à la lumière, utilisées dans les applications optiques telles que les capteurs de lumière.

8. Optocoupleurs : Utilisés pour isoler différentes parties d'un circuit, les optocoupleurs transmettent des signaux électriques par la lumière pour maintenir l'isolation électrique.

9. Redresseurs : Les diodes sont utilisées dans les circuits redresseurs pour convertir l'AC en DC. Les redresseurs demi-onde utilisent une seule diode, tandis que les redresseurs pleine onde utilisent deux diodes ou plus pour convertir les deux alternances de l'onde AC.

10. Thermistors : Ce sont des résistances sensibles à la température. Les thermistors à coefficient de température négatif (NTC) voient leur résistance diminuer lorsque la température augmente, tandis que les thermistors à coefficient de température positif (PTC) voient leur résistance augmenter avec des températures plus élevées.

---

### Théorie des circuits électroniques

11. Loi d'Ohm : La loi d'Ohm relie la tension (V), le courant (I) et la résistance (R) dans un circuit linéaire : \\(V = I \times R\\). Elle constitue la base de la plupart des analyses de circuits électriques.

12. Lois de Kirchhoff : La loi des nœuds de Kirchhoff (KCL) stipule que la somme des courants entrant dans un nœud est égale à la somme des courants qui en sortent, tandis que la loi des mailles de Kirchhoff (KVL) stipule que la somme des tensions dans une maille fermée est nulle.

13. Théorème de Thévenin : Ce théorème simplifie un réseau de résistances et de sources en une source de tension et une résistance équivalentes pour une analyse plus facile.

14. Théorème de Norton : Similaire à celui de Thévenin, le théorème de Norton simplifie un réseau en une source de courant et une résistance en parallèle pour une analyse plus facile des circuits pilotés par le courant.

15. Théorème de superposition : Dans les circuits à sources multiples, ce théorème permet d'analyser chaque source indépendamment puis de combiner les résultats.

16. Analyse des mailles : Une méthode utilisée pour trouver les courants inconnus dans un circuit en utilisant les courants de maille, souvent appliquée dans les circuits planaires.

17. Méthode des potentiels de nœud : Une méthode utilisée pour résoudre les circuits en assignant des tensions aux nœuds (jonctions) et en résolvant les inconnues.

18. Impédance et admittance : L'impédance est l'opposition totale au courant dans les circuits AC, combinant la résistance et la réactance. L'admittance est l'inverse de l'impédance, décrivant la facilité avec laquelle le courant traverse un composant.

19. Puissance dans les circuits AC : Dans les circuits AC, la puissance est divisée en puissance active (réelle), puissance réactive et puissance apparente. Le facteur de puissance représente le rapport de la puissance active sur la puissance apparente.

20. Résonance : La résonance se produit dans les circuits LC lorsque la réactance inductive et la réactance capacitive sont égales en magnitude mais opposées en phase, permettant un transfert d'énergie maximal.

---

### Circuits à diodes

21. Théorie de base des diodes : Les diodes permettent au courant de circuler uniquement en condition de polarisation directe (positif sur l'anode, négatif sur la cathode) et bloquent le courant en polarisation inverse.

22. Circuits redresseurs : Les redresseurs demi-onde utilisent une seule diode, tandis que les redresseurs pleine onde utilisent deux ou quatre diodes pour convertir l'AC en DC. Les ponts redresseurs sont courants dans les circuits d'alimentation.

23. Circuits écrêteurs (Clipping) : Ces circuits limitent le niveau de tension en coupant (écrêtant) la forme d'onde à un certain seuil. Ils sont utilisés dans le façonnage des signaux et la protection des signaux.

24. Circuits clampeurs (Clamping) : Ces circuits décalent le niveau de tension d'une forme d'onde, souvent utilisés pour définir une tension de base ou éliminer les oscillations négatives dans un signal.

25. Diode Zener : Les diodes Zener sont conçues pour fonctionner en claquage inverse, maintenant une tension constante sur une large plage de courants, couramment utilisées pour la régulation de tension.

26. LED : Les diodes électroluminescentes émettent de la lumière lorsque le courant les traverse. Elles sont largement utilisées dans les affichages, les indicateurs et le rétroéclairage.

27. Applications des diodes : Les diodes sont utilisées dans la détection de signaux, le redressement de puissance, la régulation de tension et dans les systèmes de communication comme modulateurs ou démodulateurs.

---

### Circuits à transistors

28. Caractéristiques des BJT : Les BJT ont trois régions : émetteur, base et collecteur. Le courant circulant depuis la base contrôle le courant plus important entre l'émetteur et le collecteur.

29. Polarisation des transistors : La polarisation d'un transistor établit un point de fonctionnement dans la région active. Les méthodes courantes incluent la polarisation fixe, la polarisation par diviseur de tension et la stabilisation par l'émetteur.

30. Amplificateur émetteur commun : C'est l'une des configurations d'amplificateur à transistor les plus utilisées, offrant un bon gain en tension mais avec une inversion de phase.

31. Amplificateur collecteur commun : Également appelé suiveur d'émetteur, ce circuit a un gain de tension unitaire et une haute impédance d'entrée, utile pour l'adaptation d'impédance.

32. Amplificateur base commune : Typiquement utilisé dans les applications haute fréquence, offrant un gain de tension élevé mais une faible impédance d'entrée.

33. Circuits de commutation : Les transistors peuvent être utilisés comme des interrupteurs numériques, activant et désactivant des dispositifs dans les circuits logiques et les systèmes numériques.

34. Paire Darlington : Une combinaison de deux transistors qui fournit un gain de courant élevé. Elle est souvent utilisée lorsqu'une amplification de courant élevée est nécessaire.

35. Régions de saturation et de blocage : Un transistor fonctionne en saturation lorsqu'il est complètement passant (agit comme un interrupteur fermé) et en blocage lorsqu'il est complètement bloqué (agit comme un interrupteur ouvert).

---

### Circuits à transistors à effet de champ

36. Caractéristiques du JFET : Le transistor à effet de champ à jonction (JFET) est contrôlé par la tension à la grille, le courant circulant entre la source et le drain. La grille est polarisée en inverse, et le courant de drain dépend de la tension grille-source.

37. Types de MOSFET : Les MOSFET (Transistors à Effet de Champ Métal-Oxyde-Semiconducteur) sont couramment utilisés pour la commutation et l'amplification. Ils existent en deux types : mode d'enrichissement (normalement bloqué) et mode de déplétion (normalement passant).

38. Fonctionnement du MOSFET : Le MOSFET fonctionne en créant un canal conducteur entre la source et le drain, contrôlé par la tension appliquée à la grille.

39. Amplificateur source commune : Cette configuration est utilisée pour l'amplification de tension, offrant un gain élevé et une impédance d'entrée/sortie modérée.

40. Amplificateur drain commun : Connu sous le nom de suiveur de source, cet amplificateur offre une faible impédance de sortie, le rendant adapté à l'adaptation d'impédance.

41. Amplificateur grille commune : Cette configuration est utilisée dans les applications haute fréquence, offrant une faible impédance d'entrée et une impédance de sortie élevée.

42. Polarisation des FET : Les FET sont généralement polarisés à l'aide de résistances et de sources de tension pour s'assurer qu'ils fonctionnent dans la région souhaitée (par exemple, la région de pincement pour les MOSFET).

43. Applications des FET : Les FET sont largement utilisés dans les amplificateurs à faible bruit, les applications RF et comme résistances commandées en tension dans les circuits analogiques.

---

### Amplificateurs

44. Types d'amplificateurs : Les amplificateurs peuvent être classés en fonction de leur fonctionnement comme amplificateurs de tension (amplifiant la tension), amplificateurs de courant (amplifiant le courant) et amplificateurs de puissance (amplifiant les deux).

45. Amplificateurs à transistor : Les trois configurations principales — émetteur commun, collecteur commun et base commune — offrent chacune des caractéristiques d'impédance et de gain uniques.

46. Amplificateurs opérationnels (Op-Amps) : Les Op-Amps sont des amplificateurs polyvalents à gain élevé. Les applications courantes incluent l'amplification différentielle, le filtrage de signaux et les opérations mathématiques.

47. Gain des amplificateurs : Le gain d'un amplificateur indique dans quelle mesure le signal d'entrée est amplifié. Il peut être défini en termes de gain en tension, en courant ou en puissance, selon l'application.

48. Contre-réaction dans les amplificateurs : La contre-réaction dans les amplificateurs peut être soit négative (réduisant le gain et stabilisant le système) soit positive (augmentant le gain et pouvant conduire à l'instabilité).

49. Contre-réaction tension et courant : Les amplificateurs à contre-réaction de tension ajustent la sortie en fonction de la tension d'entrée, tandis que les amplificateurs à contre-réaction de courant ajustent la sortie en fonction du courant d'entrée, affectant la bande passante et le slew rate.

50. Bande passante des amplificateurs : Les amplificateurs montrent généralement un compromis entre la bande passante et le gain. Un gain plus élevé conduit souvent à une bande passante réduite et vice versa.

51. Amplificateurs de puissance : Ils sont utilisés pour amplifier les signaux à un niveau adapté pour piloter des haut-parleurs, des moteurs ou d'autres dispositifs gourmands en puissance. Les classes A, B, AB et C définissent différentes caractéristiques d'efficacité et de linéarité.

52. Adaptation d'impédance : Cela assure un transfert de puissance maximal entre les composants en adaptant les impédances de la source et de la charge.

---

### Oscillateurs

53. Oscillateurs sinusoïdaux : Ces oscillateurs génèrent des formes d'onde sinusoïdales, couramment utilisées dans les applications radiofréquence (RF) et audio. Les exemples incluent les oscillateurs Colpitts et Hartley.

54. Oscillateurs de relaxation : Ils sont utilisés pour générer des formes d'onde non sinusoïdales, généralement des ondes carrées ou en dents de scie, et sont utilisés dans les applications de temporisation et d'horloge.

55. Oscillateurs à cristal : Les oscillateurs à cristal utilisent un cristal de quartz pour générer une fréquence très stable. Ils sont largement utilisés dans les horloges, les radios et les systèmes GPS.

56. Boucle à verrouillage de phase (PLL) : Une PLL est utilisée pour la synthèse et la synchronisation de fréquence, souvent utilisée dans les systèmes de communication pour moduler et démoduler les signaux.

---

### Alimentations

57. Régulateurs linéaires : Ces régulateurs maintiennent une tension de sortie constante en dissipant l'excès de tension sous forme de chaleur. Ils sont simples mais moins efficaces pour les applications de forte puissance.

58. Régulateurs à découpage (Switching) : Les régulateurs à découpage (abaisseur 'buck', élévateur 'boost' et abaisseur-élévateur 'buck-boost') convertissent la tension d'entrée en une tension de sortie souhaitée avec une efficacité plus élevée que les régulateurs linéaires.

59. Redresseurs et filtres : Les alimentations incluent souvent des redresseurs pour convertir l'AC en DC, suivis de filtres (par exemple, des condensateurs) pour lisser la sortie.

60. Techniques de régulation : La régulation de tension maintient une tension de sortie stable malgré les variations de charge ou de tension d'entrée. Les régulateurs linéaires utilisent un transistor de passage, tandis que les régulateurs à découpage utilisent des composants inductifs et capacitifs.

61. Correction du facteur de puissance (PFC) : Cette technique est utilisée dans les alimentations pour réduire le déphasage entre la tension et le courant, améliorant l'efficacité et réduisant la distorsion harmonique.

---

### Circuits de communication

62. Modulation d'amplitude (AM) : L'AM est une technique où l'amplitude d'une onde porteuse est variée proportionnellement au signal modulant, couramment utilisée dans la radiodiffusion.

63. Modulation de fréquence (FM) : La FM implique de varier la fréquence d'une onde porteuse en fonction du signal d'entrée, couramment utilisée pour la radiodiffusion haute fidélité.

64. Modulation de phase (PM) : En PM, la phase de l'onde porteuse est variée en réponse au signal d'entrée.

65. Modulation par impulsions codées (PCM) : La PCM est une méthode utilisée pour représenter numériquement des signaux analogiques en échantillonnant et en quantifiant le signal en valeurs discrètes.

66. Multiplexage par répartition en fréquence (FDM) : Le FDM consiste à diviser le spectre de fréquence disponible en sous-bandes plus petites, chacune transportant un signal différent, largement utilisé dans les systèmes de télécommunication.

67. Multiplexage par répartition dans le temps (TDM) : Le TDM divise le temps en intervalles discrets et alloue chaque intervalle à un signal différent, permettant à plusieurs signaux de partager le même support de transmission.

68. Circuits modulateur et démodulateur : Ces circuits modulent un signal d'entrée pour la transmission et démodulent les signaux reçus vers leur forme originale.

---

### Traitement du signal

69. Filtres : Les filtres sont utilisés pour supprimer les composants indésirables d'un signal. Les types incluent les filtres passe-bas, passe-haut, passe-bande et coupe-bande, chacun conçu pour laisser passer certaines fréquences tout en en atténuant d'autres.

70. Amplification : L'amplification de signal augmente l'intensité d'un signal sans altérer ses composantes fréquentielles. Les amplificateurs peuvent être utilisés dans diverses configurations, telles que les préamplificateurs, les amplificateurs de puissance et les amplificateurs différentiels.

71. Traitement numérique du signal (DSP) : Le DSP est la manipulation de signaux à l'aide de techniques numériques. Il implique l'échantillonnage, la quantification et l'application d'algorithmes comme les transformées de Fourier, la convolution et le filtrage pour traiter les signaux.

72. Conversion analogique-numérique (ADC) : Les CAN convertissent les signaux analogiques continus en données numériques discrètes. Ils sont essentiels pour l'interfaçage de capteurs analogiques avec des systèmes numériques.

73. Conversion numérique-analogique (DAC) : Les CNA effectuent l'opération inverse des CAN, convertissant les données numériques discrètes en signaux analogiques continus pour une utilisation dans les actionneurs et autres dispositifs analogiques.

74. Transformée de Fourier : La transformée de Fourier est une technique mathématique utilisée pour analyser le contenu fréquentiel d'un signal. Elle est largement utilisée dans le traitement du signal, les communications et les systèmes de contrôle.

75. Théorème de l'échantillonnage : Le théorème d'échantillonnage de Nyquist-Shannon stipule que pour reconstruire fidèlement un signal, il doit être échantillonné au moins deux fois la fréquence la plus élevée présente dans le signal.

---

### Communication sans fil

76. Techniques de modulation : La modulation consiste à faire varier un signal porteur en fonction du signal d'information. Les techniques courantes incluent la modulation d'amplitude (AM), la modulation de fréquence (FM), la modulation de phase (PM) et des schémas plus avancés comme la modulation d'amplitude en quadrature (QAM) utilisée dans les communications numériques.

77. Antennes : Les antennes sont utilisées pour transmettre et recevoir des ondes électromagnétiques. Les types d'antennes incluent les antennes dipôles, les antennes boucles, les antennes paraboliques et les antennes patch, chacune adaptée à différentes applications dans les systèmes de communication sans fil.

78. Communication radiofréquence (RF) : La communication RF implique la transmission de données via des ondes radio. Les systèmes RF sont utilisés dans les réseaux cellulaires, le Wi-Fi, le Bluetooth et la communication par satellite, avec des fréquences allant de quelques MHz à plusieurs GHz.

79. Réseaux sans fil : Les réseaux sans fil connectent des appareils sans câbles physiques. Les technologies incluent le Wi-Fi, le Bluetooth, le Zigbee et la 5G, chacune avec des cas d'utilisation spécifiques pour la communication à courte ou longue portée, le transfert de données à haute vitesse et les applications IoT.

80. Étalement de spectre (Spread Spectrum) : L'étalement de spectre est une technique utilisée en communication sans fil pour étaler un signal sur une large bande de fréquences, augmentant la résistance aux interférences et améliorant la sécurité. Les techniques incluent l'étalement de spectre à séquence directe (DSSS) et l'étalement de spectre à sauts de fréquence (FHSS).

81. Communication micro-ondes : La communication micro-ondes utilise des ondes radio haute fréquence (généralement de 1 GHz à 100 GHz) pour la communication point à point, y compris les liaisons par satellite, les systèmes radar et les liaisons de données à haute vitesse.

82. Protocoles sans fil : Les protocoles sans fil définissent comment les données sont transmises dans un réseau sans fil. Les exemples incluent IEEE 802.11 (Wi-Fi), IEEE 802.15 (Bluetooth) et Zigbee, chacun ayant des caractéristiques différentes de débit, de portée et de consommation d'énergie.

---

### Systèmes embarqués

83. Microcontrôleurs : Les microcontrôleurs sont de petits ordinateurs intégrés sur une seule puce, utilisés dans les systèmes embarqués pour contrôler des dispositifs comme des capteurs, des moteurs et des affichages. Les microcontrôleurs populaires incluent l'Arduino, le Raspberry Pi et les microcontrôleurs PIC.

84. Systèmes d'exploitation temps réel (RTOS) : Un RTOS est un système d'exploitation conçu pour les applications temps réel où les tâches doivent être accomplies dans des contraintes de temps strictes. Les exemples incluent FreeRTOS, RTEMS et VxWorks.

85. Programmation embarquée : La programmation embarquée consiste à écrire des logiciels pour les microcontrôleurs et autres dispositifs embarqués. Elle nécessite la connaissance de langages de programmation de bas niveau comme le C et l'assembleur, ainsi que l'interfaçage matériel et l'optimisation.

86. Capteurs et actionneurs : Les capteurs sont des dispositifs qui détectent des propriétés physiques comme la température, la lumière ou le mouvement, tandis que les actionneurs sont utilisés pour interagir avec le monde physique, comme déplacer un moteur ou contrôler une vanne. Ce sont des composants essentiels dans les systèmes IoT et d'automatisation.

87. Interfaçage : Les systèmes embarqués nécessitent souvent un interfaçage avec des composants externes comme des affichages, des capteurs et des modules de communication. Les techniques d'interfaçage incluent I2C, SPI, UART et GPIO.

88. Gestion de l'alimentation : La gestion de l'alimentation est cruciale dans les systèmes embarqués pour optimiser la consommation d'énergie, en particulier pour les appareils alimentés par batterie. Les techniques incluent les modes d'économie d'énergie, les régulateurs de tension et la conception de circuits efficaces.

---

### Électronique de puissance

89. Diodes de puissance : Les diodes de puissance sont utilisées pour contrôler le flux de courant dans les applications haute puissance, comme le redressement de l'AC en DC. Elles sont conçues pour supporter des tensions et des courants plus élevés que les diodes ordinaires.

90. Thyristors : Un type de dispositif semi-conducteur utilisé pour la commutation et le contrôle de grandes quantités de puissance. Les thyristors incluent les SCR (Redresseurs Commandés au Silicium) et les TRIAC, couramment utilisés dans le contrôle de moteurs, l'éclairage et la régulation de puissance.

91. MOSFET de puissance : Les MOSFET de puissance sont utilisés pour la commutation et l'amplification dans les circuits d'électronique de puissance, en particulier dans les alimentations, les entraînements de moteur et les onduleurs, en raison de leur haute efficacité et de leurs caractéristiques de commutation rapides.

92. IGBT (Transistors Bipolaires à Grille Isolée) : Les IGBT combinent les caractéristiques des BJT et des MOSFET et sont utilisés dans les applications haute puissance comme les onduleurs, les entraînements de moteur et les systèmes de chauffage par induction.

93. Convertisseurs DC-DC : Les convertisseurs DC-DC sont utilisés pour convertir un niveau de tension DC en un autre, soit en augmentant (convertisseurs élévateurs 'boost') soit en abaissant (convertisseurs abaisseurs 'buck') la tension, avec une haute efficacité.

94. Convertisseurs AC-DC : Ces convertisseurs, également appelés redresseurs, sont utilisés pour convertir le courant alternatif (AC) en courant continu (DC). Ils sont largement utilisés dans les alimentations et dans les applications où une tension DC est requise.

95. Onduleurs (Inverters) : Les onduleurs convertissent le DC en AC et sont utilisés dans les systèmes d'énergie renouvelable, les UPS (Alimentations sans interruption) et les véhicules électriques.

96. Contrôle de puissance : Le contrôle de puissance dans les systèmes électroniques implique la régulation des niveaux de tension et de courant pour une utilisation efficace de l'énergie, souvent par des boucles de contre-réaction, de la modulation et des régulateurs à découpage.

---

### Automatisation et systèmes de contrôle

97. Automates programmables industriels (PLC) : Les PLC sont des ordinateurs numériques utilisés pour l'automatisation des processus industriels, tels que la fabrication, le contrôle des machines et la gestion de systèmes comme les ascenseurs ou les feux de signalisation.

98. Systèmes SCADA : Les systèmes SCADA (Supervisory Control and Data Acquisition) sont utilisés pour surveiller et contrôler les processus industriels, y compris la production d'énergie, le traitement de l'eau et les systèmes de fabrication.

99. Capteurs industriels : Les capteurs industriels sont utilisés pour mesurer des paramètres physiques tels que la température, la pression, le débit et le niveau dans les applications d'automatisation industrielle.

100. Contrôle de moteur : Les systèmes de contrôle de moteur sont utilisés pour réguler la vitesse, la direction et le fonctionnement des moteurs, y compris les moteurs DC, les moteurs AC et les moteurs pas à pas. Ces systèmes sont cruciaux dans l'automatisation et la robotique.