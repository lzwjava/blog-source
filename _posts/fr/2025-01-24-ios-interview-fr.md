---
audio: false
generated: false
lang: fr
layout: post
title: Entretien d'Ingénieur iOS
translated: true
type: note
---

### SwiftUI

1. Qu'est-ce que SwiftUI et en quoi diffère-t-il d'UIKit ?
   - SwiftUI est le framework moderne d'Apple pour créer des interfaces utilisateur, offrant une syntaxe déclarative par rapport à l'approche impérative d'UIKit. Il simplifie la création et la mise à jour de l'interface utilisateur.

2. Expliquez le concept d'interface utilisateur déclarative dans SwiftUI.
   - L'interface utilisateur déclarative décrit le résultat souhaité, pas les étapes pour l'atteindre. SwiftUI construit et met à jour l'interface utilisateur en fonction de l'état déclaré.

3. Comment créez-vous une vue personnalisée dans SwiftUI ?
   - Créez une nouvelle structure conforme au protocole `View` et définissez son contenu dans une propriété `body`.

4. Quels sont les avantages d'utiliser SwiftUI par rapport à UIKit ?
   - Les avantages incluent une syntaxe déclarative, une gestion d'état plus facile et une interface unifiée pour macOS, iOS et d'autres plateformes Apple.

5. Comment gérez-vous la gestion d'état dans SwiftUI ?
   - Utilisez `@State` pour l'état local, `@ObservedObject` pour les classes observables et `@EnvironmentObject` pour l'état global.

6. Expliquez la différence entre `@State` et `@Binding`.
   - `@State` est utilisé pour la gestion d'état local, tandis que `@Binding` est utilisé pour partager l'état entre les vues.

7. Comment utilisez-vous `@EnvironmentObject` dans SwiftUI ?
   - `@EnvironmentObject` est utilisé pour accéder à un objet qui est transmis à travers la hiérarchie des vues.

8. Quel est le but de `@ObservedObject` et `@StateObject` ?
   - `@ObservedObject` observe les changements dans un objet, tandis que `@StateObject` gère le cycle de vie d'un objet.

9. Comment gérez-vous les animations de vue dans SwiftUI ?
   - Utilisez des modificateurs d'animation comme `.animation()` ou `withAnimation {}` pour animer les changements d'interface utilisateur.

10. Quelle est la différence entre `ViewBuilder` et `@ViewBuilder` ?
    - `ViewBuilder` est un protocole pour construire des vues, tandis que `@ViewBuilder` est un wrapper de propriété pour les fonctions renvoyant des vues.

### CocoaPods et Dépendances

11. Qu'est-ce que CocoaPods et comment est-il utilisé dans le développement iOS ?
    - CocoaPods est un gestionnaire de dépendances pour les projets Cocoa Swift et Objective-C, simplifiant l'intégration de bibliothèques.

12. Comment installez-vous CocoaPods ?
    - Installez via la gemme Ruby : `sudo gem install cocoapods`.

13. Qu'est-ce qu'un Podfile et comment le configurez-vous ?
    - Un Podfile liste les dépendances du projet. Configurez-le en spécifiant les pods et leurs versions.

14. Comment ajoutez-vous une dépendance à votre projet en utilisant CocoaPods ?
    - Ajoutez le pod au Podfile et exécutez `pod install`.

15. Quelle est la différence entre `pod install` et `pod update` ?
    - `pod install` installe les dépendances comme spécifié, tandis que `pod update` met à jour vers les dernières versions.

16. Comment résolvez-vous les conflits entre différents pods ?
    - Utilisez des versions de pods compatibles ou spécifiez les versions dans le Podfile.

17. Qu'est-ce que Carthage et en quoi diffère-t-il de CocoaPods ?
    - Carthage est un autre gestionnaire de dépendances qui construit et lie des bibliothèques sans s'intégrer profondément dans le projet.

18. Comment gérez-vous différents pods pour différentes configurations de build ?
    - Utilisez des instructions conditionnelles dans le Podfile basées sur les configurations de build.

19. Qu'est-ce qu'un fichier podspec et comment est-il utilisé ?
    - Un fichier podspec décrit la version, la source, les dépendances et d'autres métadonnées d'un pod.

20. Comment dépanez-vous les problèmes avec CocoaPods ?
    - Vérifiez les versions des pods, nettoyez le projet et consultez le suivi des problèmes de CocoaPods.

### Disposition de l'Interface Utilisateur

21. Comment créez-vous une disposition responsive dans iOS ?
    - Utilisez Auto Layout et des contraintes pour adapter les vues à différentes tailles d'écran.

22. Expliquez la différence entre `Stack View` et `Auto Layout`.
    - Les Stack Views simplifient la disposition des vues en ligne ou en colonne, tandis qu'Auto Layout offre un contrôle précis du positionnement.

23. Comment utilisez-vous `UIStackView` dans iOS ?
    - Ajoutez des vues à une Stack View et configurez son axe, sa distribution et son alignement.

24. Quelle est la différence entre `frame` et `bounds` dans iOS ?
    - `frame` définit la position et la taille de la vue par rapport à sa superview, tandis que `bounds` définit le système de coordonnées propre à la vue.

25. Comment gérez-vous les différentes tailles d'écran et orientations dans iOS ?
    - Utilisez Auto Layout et les classes de taille pour adapter l'interface utilisateur à divers appareils et orientations.

26. Expliquez comment utiliser les contraintes `Auto Layout` dans iOS.
    - Définissez des contraintes entre les vues pour définir leurs relations et positions.

27. Quelle est la différence entre `leading` et `trailing` dans Auto Layout ?
    - Leading et trailing s'adaptent à la direction du texte, tandis que left et right ne le font pas.

28. Comment créez-vous une disposition personnalisée dans iOS ?
    - Sous-classez `UIView` et remplacez `layoutSubviews()` pour positionner manuellement les sous-vues.

29. Expliquez comment utiliser `UIPinchGestureRecognizer` et `UIRotationGestureRecognizer`.
    - Attachez des reconnaisseurs de gestes aux vues et gérez leurs actions dans les méthodes déléguées.

30. Comment gérez-vous les changements de disposition pour différents types d'appareils (iPhone, iPad) ?
    - Utilisez les classes de taille et les dispositions adaptatives pour ajuster l'interface utilisateur pour différents appareils.

### Swift

31. Quelles sont les principales différences entre Swift et Objective-C ?
    - Swift est plus sûr, plus concis et prend en charge les fonctionnalités de langage modernes comme les fermetures et la généricité.

32. Expliquez le concept d'optionnels dans Swift.
    - Les optionnels représentent des valeurs qui peuvent être `nil`, indiquant l'absence d'une valeur.

33. Quelle est la différence entre `nil` et `optional` ?
    - `nil` est l'absence d'une valeur, tandis qu'un optionnel peut soit contenir une valeur, soit être `nil`.

34. Comment gérez-vous les erreurs dans Swift ?
    - Utilisez des blocs `do-catch` ou propagez les erreurs en utilisant `throw`.

35. Expliquez la différence entre `let` et `var`.
    - `let` déclare des constantes, tandis que `var` déclare des variables qui peuvent être modifiées.

36. Quelle est la différence entre une classe et une structure dans Swift ?
    - Les classes prennent en charge l'héritage et sont des types référence, tandis que les structures sont des types valeur.

37. Comment créez-vous une énumération dans Swift ?
    - Définissez une énumération avec le mot-clé `enum` et des cas, qui peuvent avoir des valeurs associées.

38. Expliquez le concept de programmation orientée protocole dans Swift.
    - Les protocoles définissent des méthodes, des propriétés et des exigences que les types conformes doivent implémenter.

39. Quelle est la différence entre un protocole et un délégué ?
    - Les protocoles définissent des méthodes, tandis que les délégués implémentent les méthodes de protocole pour des interactions spécifiques.

40. Comment utilisez-vous la généricité dans Swift ?
    - Utilisez des types génériques pour écrire un code flexible et réutilisable qui fonctionne avec n'importe quel type de données.

### Réseau

41. Comment gérez-vous les requêtes réseau dans iOS ?
    - Utilisez URLSession pour les tâches réseau, ou des bibliothèques comme Alamofire pour des abstractions de plus haut niveau.

42. Qu'est-ce que URLSession ?
    - URLSession gère les requêtes réseau, fournissant des tâches de données, de téléchargement et de mise en ligne.

43. Comment gérez-vous l'analyse JSON dans Swift ?
    - Utilisez le protocole `Codable` pour décoder les données JSON en structures ou classes Swift.

44. Expliquez la différence entre les requêtes synchrones et asynchrones.
    - Les requêtes synchrones bloquent le thread appelant, tandis que les requêtes asynchrones ne le font pas.

45. Comment gérez-vous les requêtes réseau dans un thread d'arrière-plan ?
    - Utilisez GCD ou OperationQueue pour effectuer les requêtes en dehors du thread principal.

46. Qu'est-ce qu'Alamofire et en quoi diffère-t-il de URLSession ?
    - Alamofire est une bibliothèque réseau tierce qui simplifie les requêtes HTTP par rapport à URLSession.

47. Comment gérez-vous les erreurs réseau et les nouvelles tentatives ?
    - Implémentez la gestion des erreurs dans les gestionnaires d'achèvement et envisagez des mécanismes de nouvelle tentative pour les erreurs transitoires.

48. Expliquez comment utiliser les méthodes `URLSessionDataDelegate`.
    - Implémentez les méthodes déléguées pour gérer la progression des requêtes, l'authentification, et plus encore.

49. Quelle est la différence entre les requêtes GET et POST ?
    - GET récupère des données, tandis que POST envoie des données à un serveur pour créer ou mettre à jour des ressources.

50. Comment sécurisez-vous les communications réseau ?
    - Utilisez HTTPS pour chiffrer les données en transit et gérez correctement les certificats.

### Bonnes Pratiques et Résolution de Problèmes

51. Comment assurez-vous la qualité du code dans vos projets ?
    - Utilisez des outils de linting, écrivez des tests unitaires et suivez les normes de codage.

52. Expliquez comment vous débogueriez une vue SwiftUI.
    - Utilisez les outils de débogage de Xcode, le canevas de prévisualisation et les instructions d'impression pour identifier les problèmes.

53. Quelles stratégies utilisez-vous pour optimiser les performances des applications ?
    - Profilez l'application à l'aide d'Instruments, optimisez la récupération des données et réduisez le nombre de calques d'interface utilisateur.

54. Comment gérez-vous la gestion de la mémoire dans Swift ?
    - Utilisez ARC (Comptage de Référence Automatique) et évitez les cycles de rétention.

55. Expliquez comment vous aborderiez la refactorisation de code legacy.
    - Identifiez les odeurs de code, écrivez des tests et refactorisez de manière incrémentale.

56. Quelle est votre expérience avec les pipelines CI/CD ?
    - Mettez en place des pipelines à l'aide d'outils comme Jenkins, GitHub Actions ou Fastlane pour les builds et déploiements automatisés.

57. Comment restez-vous informé des derniers développements iOS ?
    - Suivez les ressources pour développeurs d'Apple, assistez à des conférences et participez aux communautés de développeurs.

58. Expliquez une fois où vous avez résolu un bug difficile dans votre projet.
    - Décrivez le processus d'identification, d'isolement et de correction du problème.

59. Quelle est votre approche du contrôle de version ?
    - Utilisez Git pour le branchement, la validation et la collaboration efficace.

60. Comment gérez-vous les délais et la pression dans un projet ?
    - Priorisez les tâches, communiquez efficacement et gérez le temps de manière efficiente.