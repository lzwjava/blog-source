---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Résolution des Dépendances dans un Projet Multi-Module Maven
translated: true
type: note
---

Oui, c'est exact — dans un projet multi-module Maven, lorsqu'un module (par exemple, un module EAR) dépend d'un autre (par exemple, un module WAR), Maven résout la dépendance depuis le `.m2/repository` local par défaut, et non directement depuis le répertoire `target/` de l'autre module. En effet, Maven traite les dépendances inter-modules comme des références d'artefacts standard (comme des librairies externes), donc l'artefact dépendant doit être installé (ou au moins empaqueté et découvrable via le réacteur de build).

### Pourquoi cela se produit
- **Résolution du Dépôt Local** : Le mécanisme de résolution des dépendances de Maven recherche d'abord les artefacts dans le dépôt local. Le répertoire `target/` n'est utilisé que temporairement pendant la construction d'un seul module, mais pour les références inter-modules, il s'attend à ce que l'artefact soit "publié" (installé).
- **Les Builds Reactor Aident, Mais Ne Suffisent Pas Toujours** : Si vous exécutez `mvn package` (ou `mvn install`) depuis la **racine du POM parent**, le réacteur de Maven construit automatiquement les modules dans l'ordre topologique. Il résout les dépendances inter-modules à la volée sans avoir besoin d'installations explicites, en récupérant la sortie fraîche du `target/` de l'autre module pendant la session. Mais si vous construisez le module dépendant (par exemple, EAR) **indépendamment** (par exemple, `cd ear-module && mvn package`), il ne verra pas le `target/` du WAR — il échouera à moins que l'artefact WAR ne soit déjà dans `.m2`.

### Pour l'Emballage WAR-vers-EAR Spécifiquement
Dans un projet EAR :
- Le plugin EAR (`maven-ear-plugin`) s'attend à ce que le WAR (et les autres modules) soient des artefacts résolus à inclure dans l'archive EAR (par exemple, via `<modules>` dans le POM EAR).
- Si le WAR n'est pas installé, vous obtiendrez des erreurs comme "Could not resolve dependencies" ou des modules manquants dans l'EAR.

**Solution** : Oui, vous devez généralement exécuter `mvn install` (ou au moins `mvn package` dans un build reactor complet) sur le module "original" (dépendance) en premier si vous construisez indépendamment. Les meilleures pratiques :
1. **Préféré : Construire depuis le Parent** : `mvn clean install` à la racine du projet. Cela installe tout dans `.m2` et gère l'ordre automatiquement.
2. **Si vous Construisez les Modules Séparément** :
   - `cd war-module && mvn clean install` (installe le JAR WAR dans `.m2`).
   - Puis `cd ear-module && mvn clean package` (ou `install` — les EARs n'ont souvent besoin que de `package`).
3. **Évitez les Références Directes à Target** : Ne contournez pas ce problème avec `<systemPath>` ou des chemins de fichiers vers `target/` — c'est fragile et ignore les checksums/transitivité de Maven.

Ce comportement n'a pas changé dans les versions récentes de Maven (jusqu'à 3.9.x en 2025). Pour plus de détails, consultez le guide officiel des multi-modules.

[Introduction to the Build Lifecycle - Multi-module Projects](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html#multi-module)
[Maven EAR Plugin Documentation](https://maven.apache.org/plugins/maven-ear-plugin/ear-mojo.html)