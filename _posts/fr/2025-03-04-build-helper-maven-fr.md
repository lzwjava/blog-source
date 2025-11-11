---
audio: false
generated: true
lang: fr
layout: post
title: Plugin Maven d'aide à la construction
translated: true
type: note
---

Le `builder-helper-maven-plugin`, maintenant appelé **Build Helper Maven Plugin**, est un outil polyvalent conçu pour aider dans diverses tâches du cycle de vie de build Maven. Initialement hébergé sous Codehaus, il est maintenant maintenu par MojoHaus, bien que ses coordonnées Maven utilisent toujours le group ID `org.codehaus.mojo`. Ce plugin fournit un ensemble de goals pour aider à des opérations telles que l'ajout de répertoires de sources supplémentaires, l'attachement d'artefacts supplémentaires, l'analyse des informations de version, et plus encore. Ci-dessous, je vais vous guider sur la façon d'utiliser ce plugin dans votre projet Maven.

### Qu'est-ce que Maven ?
Avant de plonger dans le plugin, posons le contexte. Maven est un outil d'automatisation de build largement utilisé, principalement pour les projets Java. Il simplifie et standardise le processus de build en gérant les dépendances, en compilant le code, en empaquetant les applications, et plus encore, le tout étant configuré via un fichier central appelé `pom.xml`.

### Étape 1 : Inclure le Plugin dans Votre `pom.xml`
Pour utiliser le Build Helper Maven Plugin, vous devez l'ajouter à votre projet Maven dans le fichier `pom.xml`, dans la section `<build><plugins>`. Voici comment procéder :

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>build-helper-maven-plugin</artifactId>
            <version>3.6.0</version>
            <!-- Les executions pour des goals spécifiques seront ajoutées ici -->
        </plugin>
    </plugins>
</build>
```

- **Group ID** : `org.codehaus.mojo` (reflétant ses origines, même s'il est maintenant sous MojoHaus).
- **Artifact ID** : `build-helper-maven-plugin`.
- **Version** : Lors de ma dernière mise à jour, `3.6.0` était la dernière version, mais vous devriez vérifier [Maven Central](https://mvnrepository.com/artifact/org.codehaus.mojo/build-helper-maven-plugin) pour la version la plus récente.

Cette déclaration rend le plugin disponible dans votre projet, mais il ne fera rien tant que vous n'aurez pas configuré de goals spécifiques.

### Étape 2 : Configurer les Executions pour des Goals Spécifiques
Le Build Helper Maven Plugin offre plusieurs goals, chacun conçu pour une tâche particulière. Vous configurez ces goals en ajoutant des blocs `<executions>` dans la déclaration du plugin, en spécifiant quand ils doivent s'exécuter (via une phase du cycle de vie Maven) et comment ils doivent se comporter.

Voici quelques goals couramment utilisés et leurs objectifs :

- **`add-source`** : Ajoute des répertoires de sources supplémentaires à votre projet.
- **`add-test-source`** : Ajoute des répertoires de sources de test supplémentaires.
- **`add-resource`** : Ajoute des répertoires de ressources supplémentaires.
- **`attach-artifact`** : Attache des artefacts supplémentaires (par exemple, des fichiers) à votre projet pour l'installation et le déploiement.
- **`parse-version`** : Analyse la version du projet et définit des propriétés (par exemple, les versions majeure, mineure, incrémentale).

Chaque goal nécessite sa propre configuration, que vous définissez dans un bloc `<execution>`.

### Étape 3 : Exemple – Ajouter un Répertoire de Source Supplémentaire
Un cas d'utilisation fréquent de ce plugin est l'ajout d'un répertoire de source supplémentaire, car Maven