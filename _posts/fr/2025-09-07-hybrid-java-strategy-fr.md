---
audio: false
date: 2025-09-07
generated: true
image: false
lang: fr
layout: post
title: Stratégie de développement Java hybride
translated: true
type: note
---

Avis concis : pour les gros codebases Java, un **hybride** fonctionne le mieux. Utilisez **VS Code** comme cockpit axé IA (Claude Code + Copilot = itération plus rapide et boilerplate), et gardez **IntelliJ IDEA** sous le coude pour la « chirurgie » (refactorisations profondes, inspections, assistants avancés Spring/Gradle/Maven). Vous n'avez pas à choisir une seule religion. 🙂

Voici comment je le vois — pas de tableaux, juste l'essentiel :

### Les points forts de VS Code

* **Workflow IA** : Les complétions inline de Copilot sont toujours meilleures dans VS Code, et le raisonnement au niveau du repo de Claude Code y est plus rapide. Idéal pour rédiger des services, des tests, des mappers, du SQL, et des redesigns rapides.
* **Léger et modulaire** : Vous ajoutez seulement ce dont vous avez besoin. Les démarrages à froid et l'utilisation de la mémoire sont plus sympathiques sur les gros monorepos.
* **« Jump to » + LSP** : Avec les extensions Java, « Aller à la Définition/Implémentation », la hiérarchie des types, la hiérarchie des appels et la recherche de symboles sont suffisamment solides pour le quotidien.

Extensions recommandées (recherchez par ID) :

* `vscjava.vscode-java-pack` (inclut la plupart des extensions ci-dessous)
* `redhat.java` (Language Support for Java)
* `vscjava.vscode-java-debug` / `vscjava.vscode-java-test`
* `vscjava.vscode-maven` / `vscjava.vscode-gradle`
* `vscjava.vscode-spring-boot-dashboard` + `vscjava.vscode-spring-initializr`
* `sonarsource.sonarlint-vscode` (vérifications statiques)
* `streetsidesoftware.code-spell-checker` (étonnamment utile dans les JavaDocs)
* Claude Code + GitHub Copilot

Réglages de performance pour les gros projets (à mettre dans `.vscode/settings.json`) :

```json
{
  "java.maxConcurrentBuilds": 4,
  "java.jdt.ls.vmargs": "-Xms512m -Xmx4g -XX:+UseG1GC -XX:+UseStringDeduplication",
  "java.errors.incompleteClasspath.severity": "ignore",
  "java.referencesCodeLens.enabled": false,
  "java.implementationsCodeLens.enabled": false,
  "files.watcherExclude": {
    "**/target/**": true,
    "**/.gradle/**": true,
    "**/node_modules/**": true
  }
}
```

Conseils :

* Importez en tant que projet **Gradle** ou **Maven** (évitez les builds mixtes si possible).
* Activez le **Spring Boot Dashboard** pour lancer/déboguer plusieurs services.
* Laissez Claude/Copilot rédiger les classes et les tests, mais utilisez **SonarLint** et vos tests unitaires comme garde-fous.

### Les domaines où IntelliJ IDEA reste imbattable

* **Profondeur et précision du refactoring** : Renommer/déplacer/extraire à travers de grandes hiérarchies, les APIs lourdes en génériques, Lombok, la config XML, même le wiring des beans Spring — le modèle sémantique d'IDEA est difficile à égaler.
* **Inspections et correctifs rapides** : Les inspections de code intégrées (et le rechercher/remplacer structurel) détectent plus de code smells subtils que la plupart des configurations VS Code.
* **UML et commodités de navigation** : Le flux de données vers/depuis ici, les diagrammes de dépendances et les périmètres de recherche avancés font gagner du temps dans les domaines complexes.

Modèle pratique :

* Faites **l'exploration, le scaffolding et les modifications répétitives** dans VS Code avec Claude/Copilot.
* Quand vous avez besoin d'une **refactorisation non triviale** (ex: diviser un module core, changer des contrats d'API sur 40 modules, migrer la config Spring), ouvrez le même repo dans IDEA, laissez-le s'indexer une fois, faites la refactorisation en sécurité, poussez, puis retournez dans VS Code.

### À propos de « Codex »

Les anciens modèles **Codex** d'OpenAI ont été mis hors service il y a quelque temps. Aujourd'hui, vous utiliserez principalement **GitHub Copilot** (alimenté par OpenAI en arrière-plan) et **Claude Code**. Considérez « Codex » comme historique — votre stack actuelle devrait être **Copilot + Claude Code**.

### Analyse statique et qualité dans VS Code

* **SonarLint** dans VS Code donne une sensation proche d'IDEA ; associez-le à une étape SonarQube/SonarCloud en CI.
* Ajoutez **SpotBugs** et **Checkstyle** via les plugins Gradle/Maven pour que la qualité soit vérifiée en CI (pas seulement en local).
* Utilisez l'explorateur de tests **JUnit** et l'extension **Coverage Gutters** pour maintenir un cycle red-green serré.

### Spécificités Spring/enterprise

* L'outillage **Spring** de VS Code est bon pour l'exécution/le débogage, les endpoints actuator et les indications sur les propriétés. Pour l'auto-configuration complexe ou les méta-annotations, IDEA résout encore les choses plus fièrement — utilisez-la quand les annotations semblent « mystérieuses ».
* Pour les monstres **Gradle** multi-modules : gardez le daemon + les builds parallèles activés, et envisagez les composite builds pour limiter la taille de l'espace de travail.

### Workflow IA qui passe à l'échelle

* **Copilot inline** pour les minuscules modifications en tapant.
* Le chat **Claude Code** pour le raisonnement à l'échelle du repo (« quels sont les effets de bord si je change le constructeur de `LedgerPosting` ? » / « rédigez une PR pour remplacer notre retry personnalisé par resilience4j »).
* Demandez au modèle de produire **des plans de refactoring + des checklists** ; puis appliquez les changements dans de petits commits pouvant être revus.
* Gardez **la sortie du modèle sous test** : exigez des diffs de tests unitaires/d'intégration dans la même PR que celle générée par l'IA.

### Alors… dans lequel vivre ?

* Si votre journée est **codage + itération + beaucoup d'assistants IA** → **VS Code** comme éditeur principal semble meilleur en ce moment.
* Si votre journée est **architecture + grosses refactorisations + débogage de cas limites des frameworks** → gardez **IntelliJ** ouvert pour ces moments.
* Beaucoup d'ingénieurs seniors naviguent entre les deux. Ce n'est pas de l'inefficacité ; c'est utiliser le bon outil pour le bon niveau de risque.

Si vous voulez, je peux générer une **configuration bootstrap VS Code Java** ponctuelle (extensions.json, settings.json, configurations de tâches/de lancement recommandées) ajustée pour votre monorepo — et un checklist IDEA court pour les moments « faites appel aux gros outils ».