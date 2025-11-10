---
audio: false
generated: true
lang: fr
layout: post
title: Annotations JetBrains pour la qualité du code
translated: true
type: note
---

La `<dependency>` que vous avez fournie spécifie la bibliothèque `org.jetbrains:annotations` dans un projets Maven. Voici de quoi il s'agit :

### Détails :
- **Group ID** : `org.jetbrains` (indique que la bibliothèque est fournie par JetBrains, les créateurs d'IntelliJ IDEA et d'autres outils).
- **Artifact ID** : `annotations` (le nom spécifique de la bibliothèque).
- **Objectif** : La bibliothèque `org.jetbrains:annotations` fournit un ensemble d'annotations Java utilisées pour améliorer la qualité du code, sa lisibilité et le support de l'IDE. Ces annotations sont principalement destinées à l'analyse statique du code et n'ont pas de dépendances ou de comportements à l'exécution.

### Annotations Clés :
La bibliothèque inclut des annotations comme :
- **`@NotNull`** : Indique qu'un paramètre de méthode, une valeur de retour ou un champ ne peut pas être `null`. Les IDE comme IntelliJ IDEA l'utilisent pour avertir d'une utilisation potentielle de `null` pendant le développement.
  - Exemple : `public void process(@NotNull String input) { ... }`
- **`@Nullable`** : Indique qu'un paramètre, une valeur de retour ou un champ peut être `null`, aidant les développeurs à éviter des suppositions non vérifiées sur la nullité.
  - Exemple : `@Nullable String getOptionalValue() { return null; }`
- **`@Contract`** : Spécifie un contrat pour le comportement d'une méthode (par exemple, les relations entrée-sortie) pour aider l'analyse statique.
  - Exemple : `@Contract("null -> fail")` indique qu'une méthode lance une exception si on lui donne `null`.
- **`@Unmodifiable`** : Marque une collection comme non modifiable pour indiquer qu'elle ne doit pas être changée.
- Autres : `@Range`, `@NonNls`, etc., pour des cas d'utilisation spécifiques comme les contraintes de valeur ou la localisation.

### Cas d'Utilisation Courants :
- **Analyse de Code** : Améliore les inspections de l'IDE (par exemple, dans IntelliJ IDEA) pour détecter des bogues potentiels comme les exceptions de pointeur nul au moment du développement.
- **Documentation du Code** : Rend l'intention du code plus claire (par exemple, si `null` est autorisé).
- **Interopérabilité** : Fonctionne avec des outils comme IntelliJ IDEA, FindBugs, ou SpotBugs pour une meilleure analyse statique.
- **Aucune Surcharge à l'Exécution** : Les annotations sont uniquement des métadonnées et n'ont généralement aucun impact sur le code compilé, sauf si elles sont explicitement traitées par un outil.

### Exemple de Dépendance Maven :
Pour inclure la bibliothèque dans votre `pom.xml`, vous spécifiez généralement une version (puisque votre extrait l'omet) :
```xml
<dependency>
    <groupId>org.jetbrains</groupId>
    <artifactId>annotations</artifactId>
    <version>24.1.0</version> <!-- Utilisez la dernière version, par exemple depuis Maven Central -->
    <scope>provided</scope> <!-- Optionnel, car les annotations ne sont généralement pas nécessaires à l'exécution -->
</dependency>
```
- **Version** : Vérifiez [Maven Central](https://mvnrepository.com/artifact/org.jetbrains/annotations) pour la dernière version (par exemple, `24.1.0` selon les données récentes).
- **Scope** : Souvent défini sur `provided` ou `compile` car les annotations sont utilisées pendant le développement mais pas requises à l'exécution.

### Pourquoi l'Utiliser ?
- Améliore la sécurité du code en détectant les problèmes potentiels tôt grâce aux avertissements de l'IDE.
- Améliore la clarté du code en documentant explicitement la nullabilité et autres contraintes.
- Largement utilisée dans les projets développés avec les outils JetBrains ou nécessitant une analyse statique robuste.

Si vous avez une question sur un cas d'utilisation spécifique, une configuration ou une intégration avec des outils, faites-le moi savoir pour une explication plus personnalisée !

La bibliothèque `org.jetbrains:annotations` **n'est pas obsolète** et reste activement maintenue par JetBrains. Elle est compatible avec les versions supérieures du JDK et largement utilisée pour l'inspection de code, la documentation et l'amélioration de l'analyse statique dans les projets Java et Kotlin, en particulier avec IntelliJ IDEA et d'autres outils JetBrains.

### Points Clés sur la Pertinence et la Compatibilité :
- **Maintenance Active** : La bibliothèque est régulièrement mise à jour. Selon les données récentes, la dernière version est `26.0.2` (GitHub - JetBrains/java-annotations). JetBrains continue de publier des mises à jour pour supporter les pratiques modernes de développement Java.[](https://github.com/JetBrains/java-annotations)
- **Compatibilité JDK** :
  - L'artefact `annotations` nécessite **JDK 1.8 ou supérieur**. Pour les projets utilisant des versions plus anciennes du JDK (1.5, 1.6 ou 1.7), JetBrains fournit un artefact legacy `annotations-java5`, qui n'est plus mis à jour.[](https://github.com/JetBrains/java-annotations)
  - Il est entièrement compatible avec les versions supérieures du JDK, y compris **JDK 17, 21, et au-delà**, car celles-ci sont supportées par IntelliJ IDEA pour le développement. La bibliothèque fonctionne parfaitement avec les fonctionnalités Java modernes comme les lambdas, les streams et les modules introduits dans JDK 8 et versions ultérieures.[](https://www.jetbrains.com/help/idea/supported-java-versions.html)
- **Objectif et Utilisation** : Les annotations (par exemple, `@NotNull`, `@Nullable`, `@Contract`) améliorent l'analyse statique dans les IDE, détectant des erreurs potentielles comme les exceptions de pointeur nul au moment de la conception. Elles sont uniquement des métadonnées, ce qui signifie qu'elles n'ont pas de dépendance à l'exécution et sont compatibles entre les versions du JDK sans affecter le comportement à l'exécution.[](https://www.jetbrains.com/help/idea/annotating-source-code.html)
- **Intégration avec IntelliJ IDEA** : IntelliJ IDEA reconnaît ces annotations nativement et peut les inférer même si elles ne sont pas explicitement ajoutées, garantissant la compatibilité avec les projets Java modernes. L'IDE supporte également la configuration d'annotations personnalisées et peut insérer automatiquement des annotations de nullabilité.[](https://www.jetbrains.com/help/idea/annotating-source-code.html)
- **Aucune Obsolescence** : Contrairement à certaines fonctionnalités Java (par exemple, les applets ou les modules Java EE legacy), rien n'indique que les annotations JetBrains soient dépréciées ou obsolètes. Elles sont essentielles à l'écosystème JetBrains, y compris ReSharper et Rider pour le développement .NET.[](https://medium.com/%40Brilworks/whats-changed-in-java-versions-new-features-and-deprecation-bbad0414bfe6)[](https://www.nuget.org/packages/JetBrains.Annotations/)

### Spécificités pour les JDK Supérieurs :
- **Fonctionnalités JDK 8+** : Les annotations fonctionnent avec les fonctionnalités Java modernes (par exemple, les lambdas, les annotations de type, les streams) introduites dans JDK 8 et versions ultérieures, car celles-ci sont supportées par IntelliJ IDEA.[](https://www.jetbrains.com/help/idea/supported-java-versions.html)
- **Traitement des Annotations** : Le traitement des annotations d'IntelliJ IDEA supporte `org.jetbrains:annotations` dans les projets utilisant des JDK supérieurs, garantissant la compatibilité avec la génération de code et la validation au moment de la compilation.[](https://www.jetbrains.com/help/idea/annotation-processors-support.html)
- **Aucun Impact à l'Exécution** : Puisque les annotations sont effacées des métadonnées par défaut (sauf si le symbole de compilation `JETBRAINS_ANNOTATIONS` est défini), elles n'introduisent pas de problèmes de compatibilité avec aucune version du JDK.[](https://www.nuget.org/packages/JetBrains.Annotations/)

### Pourquoi Elle N'est Pas Obsolète :
- **Pertinence Continue** : Les annotations améliorent la sécurité et la maintenabilité du code, en particulier pour les vérifications de nullité, qui restent critiques dans le développement Java moderne. Elles complètent des frameworks comme Spring et Lombok, qui utilisent également des annotations à des fins similaires.[](https://www.jetbrains.com/help/idea/annotating-source-code.html)
- **Support de l'Écosystème** : Les outils JetBrains (IntelliJ IDEA, Android Studio, etc.) s'appuient sur ces annotations pour l'analyse avancée du code, et le JetBrains Runtime (un fork d'OpenJDK) supporte l'exécution d'applications Java modernes.[](https://github.com/JetBrains/JetBrainsRuntime)[](https://developer.android.com/build/jdks)
- **Utilisation par la Communauté** : La bibliothèque est largement adoptée dans les projets Java et Kotlin, comme en témoigne son inclusion dans des dépôts GitHub populaires et des packages NuGet pour .NET.[](https://www.nuget.org/packages/JetBrains.Annotations/)

### Recommandations :
- **Utilisez la Dernière Version** : Incluez la dernière version de `org.jetbrains:annotations` (par exemple, `26.0.2`) dans votre `pom.xml` ou votre fichier de build Gradle pour garantir la compatibilité avec les dernières fonctionnalités d'IntelliJ IDEA et les versions du JDK :
  ```xml
  <dependency>
      <groupId>org.jetbrains</groupId>
      <artifactId>annotations</artifactId>
      <version>26.0.2</version>
      <scope>provided</scope>
  </dependency>
  ```
- **Vérifiez le JDK du Projet** : Assurez-vous que votre projet est configuré pour utiliser **JDK 8 ou supérieur** pour éviter d'avoir besoin de l'artefact legacy `annotations-java5**. Les paramètres de projet d'IntelliJ IDEA vous permettent de spécifier la version du JDK (Fichier | Structure de projet | SDKs).[](https://www.jetbrains.com/help/idea/sdk.html)
- **Activez le Traitement des Annotations** : Dans IntelliJ IDEA, activez le traitement des annotations (Paramètres | Build, Execution, Deployment | Compiler | Annotation Processors) pour tirer pleinement parti des capacités de la bibliothèque.[](https://www.jetbrains.com/help/idea/annotation-processors-support.html)
- **JDK Supérieurs** : Si vous utilisez JDK 17 ou 21 (courants dans les projets modernes), les annotations sont entièrement compatibles. Par exemple, le JetBrains Runtime d'Android Studio (basé sur OpenJDK) supporte ces annotations pour le développement Android avec JDK 17+.[](https://developer.android.com/build/jdks)

### Conclusion :
La bibliothèque `org.jetbrains:annotations` n'est pas obsolète et est entièrement compatible avec les versions supérieures du JDK (8 et au-dessus, y compris 17, 21, et au-delà). Elle reste un outil précieux pour améliorer la qualité du code et l'intégration avec l'IDE, en particulier dans l'écosystème JetBrains. Si vous utilisez un JDK moderne et IntelliJ IDEA, vous pouvez inclure cette dépendance en toute confiance sans vous soucier de l'obsolescence.

Si vous avez une version spécifique du JDK ou une configuration de projet en tête, faites-le moi savoir pour des conseils plus personnalisés !