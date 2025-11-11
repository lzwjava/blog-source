---
audio: false
generated: true
lang: fr
layout: post
title: Exceptions Java
translated: true
type: note
---

Voici une liste exhaustive d'exceptions Java, classées en **Exceptions vérifiées, Exceptions non vérifiées (Runtime) et Erreurs**.

---

## **1. Exceptions vérifiées (Doivent être gérées ou déclarées avec `throws`)**
1.  **IOException** – Échec général d'E/S.
2.  **FileNotFoundException** – Fichier manquant ou inaccessible.
3.  **InterruptedException** – Interruption d'un thread.
4.  **SQLException** – Problèmes liés à l'accès à la base de données.
5.  **ParseException** – Erreur lors de l'analyse de formats de données.
6.  **MalformedURLException** – Format d'URL invalide.
7.  **ClassNotFoundException** – Classe introuvable au moment de l'exécution.
8.  **InstantiationException** – Impossible d'instancier une classe abstraite ou une interface.
9.  **IllegalAccessException** – Accès non autorisé à une classe, méthode ou champ.
10. **NoSuchMethodException** – La méthode n'existe pas.
11. **NoSuchFieldException** – Le champ n'existe pas dans la classe.
12. **TimeoutException** – Une opération bloquante a expiré.
13. **UnsupportedEncodingException** – L'encodage n'est pas pris en charge.
14. **URISyntaxException** – Syntaxe d'URI invalide.
15. **NotBoundException** – Nom non trouvé dans un registre RMI.
16. **AlreadyBoundException** – Nom déjà lié dans un registre RMI.
17. **CloneNotSupportedException** – L'objet n'implémente pas `Cloneable`.
18. **DataFormatException** – Format invalide dans des données compressées.
19. **EOFException** – Fin de fichier inattendue atteinte.
20. **NotSerializableException** – L'objet n'est pas sérialisable.
21. **LineUnavailableException** – Ligne audio indisponible.
22. **UnsupportedAudioFileException** – Format de fichier audio non pris en charge.
23. **PrinterException** – Échec de l'opération d'impression.
24. **ReflectiveOperationException** – Erreur de réflexion générale.
25. **ExecutionException** – Exception lors de l'exécution d'une tâche concurrente.
26. **ScriptException** – Problèmes lors de l'exécution de scripts.
27. **TransformerException** – Échec de la transformation XML.
28. **XPathExpressionException** – Expression XPath invalide.
29. **SAXException** – Problèmes d'analyse XML.
30. **JAXBException** – Problèmes de liaison XML.
31. **MarshalException** – Erreur lors du marshalling des données XML.
32. **UnmarshalException** – Erreur lors du unmarshalling des données XML.
33. **DatatypeConfigurationException** – Configuration de type de données XML invalide.
34. **GSSException** – Problèmes avec les opérations de sécurité GSS.
35. **KeyStoreException** – Problèmes avec le Java KeyStore.
36. **CertificateException** – Problèmes de traitement de certificat.
37. **InvalidKeyException** – Clé invalide dans les opérations cryptographiques.
38. **NoSuchAlgorithmException** – L'algorithme cryptographique demandé n'est pas disponible.
39. **NoSuchProviderException** – Le fournisseur de sécurité demandé n'est pas disponible.
40. **UnrecoverableKeyException** – Impossible de récupérer une clé du KeyStore.
41. **IllegalBlockSizeException** – Taille de bloc invalide pour le chiffrement.
42. **BadPaddingException** – Erreur de remplissage en cryptographie.

---

## **2. Exceptions non vérifiées (Exceptions d'exécution)**
43. **NullPointerException** – Accès à une référence d'objet `null`.
44. **ArrayIndexOutOfBoundsException** – Accès à un index de tableau invalide.
45. **StringIndexOutOfBoundsException** – Accès à un index de chaîne invalide.
46. **ArithmeticException** – Erreurs mathématiques comme une division par zéro.
47. **NumberFormatException** – Conversion d'une chaîne invalide en nombre.
48. **ClassCastException** – Cast de type invalide.
49. **IllegalArgumentException** – Argument invalide passé à une méthode.
50. **IllegalStateException** – Méthode appelée dans un état invalide.
51. **UnsupportedOperationException** – Méthode non prise en charge.
52. **ConcurrentModificationException** – Modification concurrente d'une collection.
53. **NoSuchElementException** – Tentative d'accès à un élément inexistant dans une collection.
54. **IllegalMonitorStateException** – Erreur de synchronisation des threads.
55. **NegativeArraySizeException** – Création d'un tableau avec une taille négative.
56. **StackOverflowError** – Récursion infinie entraînant un débordement de pile.
57. **OutOfMemoryError** – La JVM manque de mémoire.
58. **SecurityException** – Violation de sécurité détectée.
59. **MissingResourceException** – Bundle de ressources introuvable.
60. **EmptyStackException** – Tentative d'accès à un élément d'une pile vide.
61. **TypeNotPresentException** – Type introuvable au moment de l'exécution.
62. **EnumConstantNotPresentException** – Constante d'énumération invalide.
63. **UncheckedIOException** – Version non vérifiée de `IOException`.
64. **DateTimeException** – Erreurs liées à l'API date-heure de Java.
65. **InvalidClassException** – Problèmes de désérialisation d'une classe.
66. **IllegalCharsetNameException** – Nom de jeu de caractères invalide.
67. **UnsupportedCharsetException** – Le jeu de caractères n'est pas pris en charge.
68. **ProviderNotFoundException** – Le fournisseur de service requis est manquant.
69. **PatternSyntaxException** – Syntaxe d'expression régulière invalide.
70. **InvalidPathException** – Chemin de fichier invalide.
71. **ReadOnlyBufferException** – Tentative de modification d'un tampon en lecture seule.
72. **BufferUnderflowException** – Sous-débit de tampon.
73. **BufferOverflowException** – Débordement de tampon.
74. **FileSystemAlreadyExistsException** – Le système de fichiers existe déjà.
75. **FileSystemNotFoundException** – Système de fichiers introuvable.
76. **ClosedWatchServiceException** – Le service de surveillance est fermé.
77. **UncheckedExecutionException** – Problèmes lors de l'exécution de tâches concurrentes.

---

## **3. Erreurs (Problèmes graves qui ne doivent pas être attrapés)**
78. **StackOverflowError** – Trop d'appels de méthode récursifs.
79. **OutOfMemoryError** – La JVM manque de mémoire.
80. **VirtualMachineError** – Erreur critique de la JVM.
81. **InternalError** – Erreur interne inattendue de la JVM.
82. **UnknownError** – Erreur critique inconnue.
83. **AssertionError** – Échec d'assertion avec `assert`.
84. **NoClassDefFoundError** – Définition de classe manquante au moment de l'exécution.
85. **IncompatibleClassChangeError** – Changements incompatibles apportés à une classe.
86. **AbstractMethodError** – Méthode abstraite non implémentée.
87. **InstantiationError** – Échec de la création d'instance.
88. **IllegalAccessError** – Accès illégal à une classe ou méthode.
89. **NoSuchMethodError** – Méthode introuvable.
90. **NoSuchFieldError** – Champ introuvable.
91. **ClassFormatError** – Format de classe invalide.
92. **UnsupportedClassVersionError** – Classe Java compilée avec une version non prise en charge.
93. **AnnotationFormatError** – Problèmes avec les annotations Java.
94. **ExceptionInInitializerError** – Exception dans un bloc d'initialisation statique.
95. **ThreadDeath** – Thread terminé de force.
96. **ServiceConfigurationError** – Problème de configuration du fournisseur de service.
97. **BootstrapMethodError** – Erreur dans le support des langages dynamiques.
98. **VerifierError** – Échec de la vérification du bytecode.
99. **FactoryConfigurationError** – Erreur de configuration d'usine XML.

---

### **Conclusion**
Ceci est une liste complète des exceptions et erreurs Java. Si vous avez besoin de plus de détails sur une exception spécifique, faites-le-moi savoir ! 🚀