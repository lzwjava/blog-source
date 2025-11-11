---
audio: false
generated: true
lang: fr
layout: post
title: Fichiers de projet créés par Eclipse IDE
translated: true
type: note
---

### Pourquoi existe-t-il des fichiers .project, et à quoi servent `filteredResources`, `filter` et `matcher` ?

Les fichiers `.project` existent pour stocker les paramètres et configurations spécifiques à un projet dans les environnements de développement. Plus précisément, dans le contexte de votre question, ils sont utilisés pour gérer la façon dont les ressources (fichiers et dossiers) sont affichées ou traitées au sein d'un projet. Les éléments comme `filteredResources`, `filter` et `matcher` font partie de cette configuration et jouent un rôle dans le **filtrage des ressources** — une fonctionnalité qui permet aux développeurs de masquer certains fichiers ou dossiers de la vue, tels que les résultats de compilation, les fichiers temporaires ou d'autres ressources non pertinentes. Cela permet de garder l'espace de travail organisé et concentré sur les fichiers qui comptent pour la tâche en cours.

- **`filteredResources`** : Cette section dans le fichier `.project` définit quelles ressources (fichiers ou répertoires) sont filtrées de la vue du projet.
- **`filter`** : Cela spécifie les règles ou conditions pour le filtrage, comme les noms de fichiers, les modèles ou les types.
- **`matcher`** : Cela fonctionne avec le `filter` pour définir comment les critères de filtrage sont appliqués, comme les modèles de correspondance ou les exclusions.

Par exemple, si un projet génère des fichiers temporaires (par exemple, des fichiers `.class` ou des journaux), un développeur peut utiliser ces paramètres pour les exclure de l'explorateur de projets, facilitant ainsi la navigation dans la base de code.

### Quel IDE crée ces fichiers ?

L'**IDE Eclipse** est l'outil principal qui crée et utilise les fichiers `.project`, y compris les éléments `filteredResources`, `filter` et `matcher`. Eclipse s'appuie sur le fichier `.project` pour stocker les métadonnées d'un projet, telles que sa nature (par exemple, projet Java), les commandes de construction et les filtres de ressources. Lorsque vous configurez les filtres de ressources dans Eclipse (par exemple, via la vue Project Explorer), ces paramètres sont enregistrés dans le fichier `.project` afin qu'ils persistent d'une session à l'autre et soient appliqués chaque fois que le projet est ouvert.

Bien qu'Eclipse soit l'IDE principal associé à ce format de fichier, d'autres outils comme **Maven** ou **Gradle** peuvent également générer des fichiers `.project`. Ces outils de construction les créent souvent pour garantir la compatibilité avec Eclipse, permettant une importation transparente des projets. Cependant, l'utilisation spécifique de `filteredResources`, `filter` et `matcher` est liée au système de gestion des ressources d'Eclipse.

### Résumé

- **Objectif** : Les fichiers `.project` existent pour gérer les paramètres du projet, et `filteredResources`, `filter` et `matcher` sont utilisés par Eclipse pour filtrer les ressources indésirables de la vue du projet.
- **IDE** : Eclipse crée ces fichiers nativement, bien que des outils comme Maven ou Gradle puissent également les générer pour une compatibilité avec Eclipse.

Cette configuration est particulièrement utile pour les développeurs travaillant sur des projets complexes où l'encombrement dû à des fichiers non pertinents pourrait autrement ralentir leur flux de travail.