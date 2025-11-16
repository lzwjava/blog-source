---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: YourKit Profiler s'intègre parfaitement à IntelliJ
translated: true
type: note
---

Oui, YourKit Java Profiler s'intègre très bien avec IntelliJ IDEA (les éditions Community et Ultimate), et c'est l'une des expériences de profilage les plus fluides disponibles pour Java.

Voici les principales fonctionnalités d'intégration que vous avez demandées :

- Lancement direct depuis IDEA  
  Une fois que vous avez installé le plugin YourKit (disponible sur le JetBrains Marketplace ou depuis le plugin de YourKit lui-même), vous obtenez de nouvelles configurations d'exécution comme "YourKit Snapshot", "YourKit Profiling (CPU)", "YourKit Profiling (Memory)", etc., juste à côté de vos boutons d'exécution Run/Debug habituels.

- Démarrage/arrêt du profilage directement depuis la barre d'outils de l'IDE  
  Vous pouvez démarrer le profilage en un clic, et l'arrêter + ouvrir automatiquement le snapshot capturé sans quitter IDEA.

- Cliquez dans l'interface du profileur → accédez instantanément au code source dans IDEA  
  YourKit détecte qu'IDEA est en cours d'exécution et configure automatiquement la navigation par décompilation/source. Lorsque vous double-cliquez sur n'importe quelle méthode, frame de pile, point chaud d'allocation, etc., dans l'interface de YourKit, cela ouvre la ligne exacte dans votre éditeur IDEA (cela fonctionne même si vous n'avez que le bytecode, grâce à la prise en charge intégrée du décompilateur).

- Snapshot de bienvenue à la fin de l'application  
  Vous pouvez configurer YourKit pour capturer un snapshot automatiquement lorsque votre application se termine, et IDEA l'ouvrira immédiatement.

Statut actuel (à partir de YourKit 2024.9, qui est la version stable la plus récente fin 2025) :
- Prise en charge complète d'IntelliJ IDEA 2023.3–2025.2+
- Fonctionne parfaitement avec Java 8–24 (y compris le profilage des virtual threads sur Java 21+)
- Prend également en charge Kotlin, Scala, Groovy, etc., et accède à la source correcte.

Étapes d'installation (rapide) :
1. Dans IDEA → Settings → Plugins → Marketplace → recherchez "YourKit"
2. Installez/redémarrez
3. L'agent YourKit est inclus avec le plugin, donc aucune installation séparée de YourKit n'est nécessaire pour une utilisation de base (bien que vous puissiez installer l'application autonome complète de YourKit si vous souhaitez l'interface plus riche en dehors d'IDEA).

La plupart des développeurs Java qui utilisent YourKit quotidiennement ne quittent jamais IDEA pour le profilage une fois ce plugin configuré.

Donc oui — le workflow que vous avez décrit fonctionne immédiatement et est très abouti.