---
audio: false
generated: true
lang: fr
layout: post
title: Frameworks iOS
translated: true
type: note
---

En plus d'UIKit, le système iOS fournit de nombreux autres frameworks essentiels que les développeurs utilisent couramment pour créer des applications. Ces frameworks gèrent divers aspects au-delà des simples éléments d'interface utilisateur. Voici quelques-uns des plus courants :

1.  **Foundation :** Il s'agit d'un framework fondamental qui fournit les types de données de base (comme les chaînes de caractères, les nombres, les tableaux, les dictionnaires), les types de collection, les services du système d'exploitation et les modèles de programmation de base. C'est le fondement de nombreux autres frameworks et il est presque toujours importé dans un projet iOS. Il inclut des composants essentiels comme `URLSession` pour la mise en réseau, `FileManager` pour les interactions avec le système de fichiers et `NotificationCenter` pour gérer les notifications au sein d'une application.

2.  **Core Data :** Ce framework offre un moyen robuste et flexible de gérer les objets de la couche modèle de votre application. Il vous permet de persister des données, de gérer des graphes d'objets et de gérer la synchronisation des données. Bien qu'il soit souvent décrit comme une technologie de base de données, il s'agit plus précisément d'un framework de gestion de graphe d'objets qui peut utiliser différents magasins persistants, tels que SQLite, des fichiers binaires ou un stockage en mémoire.

3.  **Core Animation :** Ce framework est utilisé pour créer des animations fluides et performantes ainsi que des effets visuels. Il fonctionne conjointement avec UIKit (ou AppKit sur macOS) pour afficher le contenu animé. Vous pouvez l'utiliser pour animer des vues, des calques et d'autres éléments graphiques, en créant des transitions et des effets complexes sans avoir à manipuler directement les pixels.

4.  **Core Graphics :** Également connu sous le nom de Quartz 2D, il s'agit d'un moteur de dessin basé sur C qui fournit des capacités de rendu 2D de bas niveau. Il vous permet de dessiner des points, des lignes, des chemins, des formes et des images avec une haute fidélité. Bien qu'UIKit fournisse des abstractions de plus haut niveau pour le dessin, Core Graphics est souvent utilisé pour les opérations de dessin personnalisées, la création de dégradés, la gestion de contextes et le travail direct avec des primitives graphiques.

5.  **AVFoundation :** Ce framework fournit un ensemble complet d'outils pour travailler avec des médias audiovisuels basés sur le temps. Vous pouvez l'utiliser pour lire, enregistrer et modifier de l'audio et de la vidéo. Il vous donne le contrôle sur les caméras, les microphones, les moteurs de lecture et les assets multimédias, ce qui le rend essentiel pour les applications impliquant du contenu multimédia.

6.  **Core Location :** Ce framework permet à votre application d'accéder aux services de localisation de l'appareil, tels que la position géographique actuelle de l'utilisateur, l'altitude et le cap. Il peut utiliser le GPS, le Wi-Fi et les signaux cellulaires pour déterminer la position et prend en charge des fonctionnalités comme la surveillance de régions et le géorepérage (geofencing).

7.  **UserNotifications :** Ce framework est utilisé pour planifier et gérer les notifications locales et distantes. Il permet à votre application d'informer les utilisateurs d'événements importants même lorsque l'application n'est pas active, en affichant des alertes, en jouant des sons ou en mettant à jour les badges sur l'icône de l'application.

8.  **SwiftUI :** Alors qu'UIKit est le framework traditionnel pour créer des interfaces utilisateur avec une approche impérative, SwiftUI est un framework plus récent et déclaratif introduit par Apple pour créer des interfaces utilisateur sur toutes les plateformes Apple. Il propose un paradigme différent pour le développement d'interface utilisateur et est de plus en plus courant dans le développement iOS moderne, souvent utilisé conjointement avec ou en alternative à UIKit, en particulier pour les nouveaux projets ou fonctionnalités.

Ces frameworks, ainsi que beaucoup d'autres comme Metal (pour l'accélération graphique), SpriteKit (pour les jeux 2D), SceneKit (pour les graphismes 3D) et Core ML (pour le machine learning), forment l'écosystème puissant que les développeurs iOS exploitent pour créer des applications diversifiées et riches en fonctionnalités.