---
audio: false
generated: true
lang: fr
layout: post
title: Maven Plugin d'Aide à la Construction
translated: true
---

Le `builder-helper-maven-plugin`, désormais connu sous le nom de **Build Helper Maven Plugin**, est un outil polyvalent conçu pour aider à diverses tâches dans le cycle de vie de construction de Maven. Initialement hébergé sous Codehaus, il est maintenant maintenu par MojoHaus, bien que ses coordonnées Maven utilisent toujours le groupe ID `org.codehaus.mojo`. Ce plugin fournit un ensemble de buts pour aider aux opérations telles que l'ajout de répertoires sources supplémentaires, l'attachement d'artefacts supplémentaires, l'analyse des informations de version, et plus encore. Ci-dessous, je vais vous guider à travers l'utilisation de ce plugin dans votre projet Maven.

### Qu'est-ce que Maven ?
Avant de plonger dans le plugin, établissons le contexte. Maven est un outil d'automatisation de construction largement utilisé principalement pour les projets Java. Il simplifie et standardise le processus de construction en gérant les dépendances, en compilant le code, en empaquetant les applications, et plus encore, tout cela configuré à travers un fichier central appelé `pom.xml`.

### Étape 1 : Inclure le Plugin dans votre `pom.xml`
Pour utiliser le Build Helper Maven Plugin, vous devez l'ajouter au fichier `pom.xml` de votre projet Maven dans la section `<build><plugins>`. Voici comment faire :

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>build-helper-maven-plugin</artifactId>
            <version>3.6.0</version>
            <!-- Executions pour des buts spécifiques seront ajoutées ici -->
        </plugin>
    </plugins>
</build>
```

- **Group ID** : `org.codehaus.mojo` (refletant ses origines, même s'il est maintenant sous MojoHaus).
- **Artifact ID** : `build-helper-maven-plugin`.
- **Version** : À ma dernière mise à jour, `3.6.0` est la dernière version, mais vous devriez vérifier [Maven Central](https://mvnrepository.com/artifact/org.codehaus.mojo/build-helper-maven-plugin) pour la version la plus récente.

Cette déclaration rend le plugin disponible dans votre projet, mais il ne fera rien jusqu'à ce que vous configuriez des buts spécifiques.

### Étape 2 : Configurer les Executions pour des Buts Spécifiques
Le Build Helper Maven Plugin offre plusieurs buts, chacun conçu pour une tâche particulière. Vous configurez ces buts en ajoutant des blocs `<executions>` dans la déclaration du plugin, en spécifiant quand ils doivent s'exécuter (via une phase du cycle de vie de Maven) et comment ils doivent se comporter.

Voici quelques buts couramment utilisés et leurs objectifs :

- **`add-source`** : Ajoute des répertoires sources supplémentaires à votre projet.
- **`add-test-source`** : Ajoute des répertoires sources de tests supplémentaires.
- **`add-resource`** : Ajoute des répertoires de ressources supplémentaires.
- **`attach-artifact`** : Attache des artefacts supplémentaires (par exemple, des fichiers) à votre projet pour l'installation et le déploiement.
- **`parse-version`** : Analyse la version du projet et définit des propriétés (par exemple, les versions majeures, mineures, incrémentales).

Chaque but nécessite sa propre configuration, que vous définissez dans un bloc `<execution>`.

### Étape 3 : Exemple – Ajouter un Répertoire Source Supplémentaire
Un cas d'utilisation fréquent pour ce plugin est d'ajouter un répertoire source supplémentaire, car Maven supporte généralement un seul par défaut (`src/main/java`). Voici comment configurer le but `add-source` pour inclure un répertoire source supplémentaire :

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>build-helper-maven-plugin</artifactId>
            <version>3.6.0</version>
            <executions>
                <execution>
                    <id>add-source</id>
                    <phase>generate-sources</phase>
                    <goals>
                        <goal>add-source</goal>
                    </goals>
                    <configuration>
                        <sources>
                            <source>path/to/your/extra/source/directory</source>
                        </sources>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

- **`<id>`** : Un identifiant unique pour cette exécution (par exemple, `add-source`).
- **`<phase>`** : La phase du cycle de vie de Maven lorsque le but s'exécute (par exemple, `generate-sources` assure que le répertoire est ajouté tôt dans la construction).
- **`<goals>`** : Spécifie le but à exécuter (`add-source` dans ce cas).
- **`<configuration>`** : Définit le répertoire source supplémentaire (remplacez `path/to/your/extra/source/directory` par votre chemin réel, par exemple, `src/main/generated`).

Lorsque vous exécutez une commande Maven comme `mvn compile`, Maven inclura ce répertoire supplémentaire comme dossier source.

### Notes Supplémentaires
- **Compatibilité des Versions** : Depuis la version 3.0.0, le plugin nécessite Maven 3 ou supérieur. Si vous utilisez une version plus ancienne de Maven, vous devrez utiliser la version 1.12 du plugin ou une version antérieure.
- **Multiples Buts** : Vous pouvez définir plusieurs blocs `<execution>` dans le même plugin pour exécuter différents buts. Par exemple, vous pourriez ajouter à la fois des répertoires sources et des répertoires sources de tests en incluant des exécutions pour `add-source` et `add-test-source`.
- **Exécution du Plugin** : Une fois configuré, l'exécution d'une commande Maven (par exemple, `mvn clean install`) déclenchera les buts du plugin pendant les phases spécifiées.

### Ressources Supplémentaires
Pour plus de détails et d'exemples d'autres buts, consultez la [page d'utilisation officielle](https://www.mojohaus.org/build-helper-maven-plugin/usage.html). Cette page fournit une documentation complète et des configurations d'exemples pour tous les buts disponibles.

### Pensées Finales
Le Build Helper Maven Plugin est un ajout puissant à votre boîte à outils Maven, surtout pour les projets nécessitant des configurations de construction non standard. En l'incluant dans votre `pom.xml` et en configurant les buts appropriés, vous pouvez adapter votre processus de construction pour répondre à des besoins spécifiques. Bien qu'il ait été originellement sous Codehaus, son domicile actuel est MojoHaus, et il reste un choix fiable pour améliorer les constructions Maven.