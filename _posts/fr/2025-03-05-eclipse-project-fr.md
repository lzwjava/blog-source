---
audio: false
generated: true
lang: fr
layout: post
title: Fichiers de projet créés par Eclipse IDE
translated: true
---

### Pourquoi Existe-t-il des Fichiers `.project` et à Quoi Servent `filteredResources`, `filter` et `matcher` ?

Les fichiers `.project` existent pour stocker des paramètres et des configurations spécifiques au projet pour les environnements de développement. Plus précisément, dans le contexte de votre question, ils sont utilisés pour gérer la manière dont les ressources (fichiers et dossiers) sont affichées ou traitées dans un projet. Les éléments tels que `filteredResources`, `filter` et `matcher` font partie de cette configuration et jouent un rôle dans le **filtrage des ressources** — une fonctionnalité qui permet aux développeurs de masquer certains fichiers ou dossiers de la vue, tels que les sorties de construction, les fichiers temporaires ou d'autres ressources non pertinentes. Cela permet de garder l'espace de travail organisé et concentré sur les fichiers importants pour la tâche en cours.

- **`filteredResources`** : Cette section dans le fichier `.project` définit quelles ressources (fichiers ou répertoires) sont filtrées de la vue du projet.
- **`filter`** : Cela spécifie les règles ou conditions de filtrage, telles que les noms de fichiers, les motifs ou les types.
- **`matcher`** : Cela fonctionne avec le `filter` pour définir comment les critères de filtrage sont appliqués, comme les motifs de correspondance ou les exclusions.

Par exemple, si un projet génère des fichiers temporaires (par exemple, des fichiers `.class` ou des journaux), un développeur pourrait utiliser ces paramètres pour les exclure de l'explorateur de projet, rendant ainsi la navigation dans la base de code plus facile.

### Quel IDE Crée Ces Fichiers ?

L'**IDE Eclipse** est l'outil principal qui crée et utilise les fichiers `.project`, y compris les éléments `filteredResources`, `filter` et `matcher`. Eclipse s'appuie sur le fichier `.project` pour stocker des métadonnées sur un projet, telles que sa nature (par exemple, projet Java), les commandes de construction et les filtres de ressources. Lorsque vous configurez des filtres de ressources dans Eclipse (par exemple, via la vue Explorateur de projet), ces paramètres sont enregistrés dans le fichier `.project` afin qu'ils persistent entre les sessions et soient appliqués chaque fois que le projet est ouvert.

Bien qu'Eclipse soit l'IDE principal associé à ce format de fichier, d'autres outils comme **Maven** ou **Gradle** peuvent également générer des fichiers `.project`. Ces outils de construction les créent souvent pour assurer la compatibilité avec Eclipse, permettant aux projets d'être importés sans problème. Cependant, l'utilisation spécifique de `filteredResources`, `filter` et `matcher` est liée au système de gestion des ressources d'Eclipse.

### Résumé

- **But** : Les fichiers `.project` existent pour gérer les paramètres du projet, et `filteredResources`, `filter` et `matcher` sont utilisés par Eclipse pour filtrer les ressources non souhaitées de la vue du projet.
- **IDE** : Eclipse crée ces fichiers de manière native, bien que des outils comme Maven ou Gradle puissent également les générer pour la compatibilité avec Eclipse.

Cette configuration est particulièrement utile pour les développeurs travaillant sur des projets complexes où le désordre causé par des fichiers non pertinents pourrait autrement ralentir leur flux de travail.