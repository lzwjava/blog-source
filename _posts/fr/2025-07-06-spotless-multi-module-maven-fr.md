---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Impeccable dans les projets Maven multi-modules
translated: true
type: note
---

### Spotless dans les projets Maven multi-modules

Spotless est un plugin de formatage de code disponible pour Maven et Gradle. Étant donné que vous avez mentionné le flag `-pl` (liste de projets) de Maven, je suppose que vous utilisez le **plugin Spotless Maven** dans un projet Java multi-module. Cela vous permet d'exécuter les vérifications de formatage (par exemple, via `spotless:check`) ou d'appliquer les corrections (par exemple, via `spotless:apply`) de manière sélective sur des modules spécifiques, ce qui est efficace pour les grands projets où vous pourriez n'avoir besoin de formater que certains modules (par exemple, lors du développement sur un sous-module spécifique).

#### Prérequis
- Votre projet utilise Maven avec une structure multi-module (définie dans un `pom.xml` parent avec `<modules>...</modules>`).
- Le plugin Spotless Maven est configuré dans votre projet (généralement dans le POM parent ou les POMs des modules individuels). Si ce n'est pas le cas, ajoutez-le à votre POM :
  ```xml
  <build>
    <plugins>
      <plugin>
        <groupId>com.diffplug.spotless</groupId>
        <artifactId>spotless-maven-plugin</artifactId>
        <version>2.43.0</version>  <!-- Utilisez la dernière version -->
        <configuration>
          <!-- Vos règles de formatage ici, par exemple pour Java, Groovy -->
        </configuration>
      </plugin>
    </plugins>
  </build>
  ```
  - Les règles courantes incluent Google Java Format, Eclipse JDT pour Java, ou des personnalisations pour les imports, les espacements, etc.
  - Spotless prend en charge de nombreux types de fichiers (Java, Kotlin, XML, etc.) et s'intègre bien avec les outils d'intégration continue pour les hooks de pré-commit (via l'objectif `spotless:check`, qui fait échouer les builds en cas de code non formaté).

#### Utilisation de `-pl` pour contrôler le formatage des modules
Le flag `-pl` (liste de projets) de Maven vous permet de spécifier une liste de modules séparés par des virgules à inclure dans l'exécution du build/plugin. Par défaut, Maven s'exécute sur tous les modules, mais `-pl` restreint cette exécution, ce qui permet d'économiser du temps et d'éviter un travail inutile sur les modules non concernés.

- **Structure de commande de base** :
  - Pour vérifier le formatage (sans appliquer les modifications) : `mvn spotless:check -pl module1,module2`
  - Pour appliquer les corrections de formatage : `mvn spotless:apply -pl module1,module2`
  - Remplacez `module1,module2` par les noms réels des modules (par exemple, les chemins relatifs depuis la racine, comme `core,api`).

- **Exemples** :
  1. **Vérifier le formatage uniquement sur le module `core`** :
     ```
     mvn spotless:check -pl core
     ```
     - Cela analyse et valide uniquement les fichiers source de `core`. S'il existe des problèmes de formatage, le build échoue avec des détails (par exemple, "Veuillez exécuter `spotless:apply` pour corriger").

  2. **Appliquer le formatage à plusieurs modules (`api` et `utils`)** :
     ```
     mvn spotless:apply -pl api,utils
     ```
     - Cela modifie les fichiers sur place pour qu'ils correspondent à vos règles Spotless. Pensez toujours à valider les changements ensuite pour éviter des surprises dans le contrôle de version.

  3. **Exclure des modules spécifiques lors d'une exécution sur l'ensemble du projet** : Utilisez `-pl !moduleToSkip` pour exécuter sur tout *sauf* certains modules (Maven 3.2.1+ prend en charge la négation avec `!`).
     - Exemple : `mvn spotless:check -pl !legacy` (s'exécute sur tous les modules sauf `legacy`).

- **Conseils pour l'efficacité** :
  - **Exécution parallèle** : Ajoutez `-T 4` pour des builds multi-threads (par exemple, `mvn spotless:check -pl core,api -T 4`).
  - **Test à blanc** : Utilisez d'abord `spotless:check` pour prévisualiser les problèmes sans apporter de modifications — c'est idempotent et sûr.
  - **Intégration avec l'IDE/le contrôle de version** : Configurez Spotless pour qu'il s'exécute à l'enregistrement/au commit dans votre IDE (par exemple, IntelliJ via le plugin Spotless) ou utilisez-le comme un hook de pré-commit (via des outils comme pre-commit ou les hooks Git) pour des vérifications automatisées.
  - **Gestion de la résolution du réacteur** : Si les dépendances des modules sont complexes, Maven les résout automatiquement lors de l'utilisation de `-pl`, en s'assurant que les modules dépendants sont traités en premier si nécessaire.
  - **Problèmes courants** :
    - Si `-pl` ne fonctionne pas, assurez-vous que les modules sont définis dans `<modules>` et utilisez des chemins complètement qualifiés en cas d'ambiguïté (par exemple, `-pl :core` pour les configurations multi-dépôts).
    - Pour les utilisateurs de Gradle (si vous pensiez au plugin Spotless Gradle à la place), l'équivalent est `-p` pour les chemins de projet, mais votre requête spécifie `-pl`, donc Maven est supposé. Si c'est Gradle, passez à des plugins comme `gradle task -p submodule`.

Pour la documentation complète, reportez-vous à la [documentation du plugin Spotless Maven](https://github.com/diffplug/spotless/tree/v2.43.0/plugin-maven). Si votre configuration est différente (par exemple, Gradle), fournissez plus de détails pour un conseil personnalisé.