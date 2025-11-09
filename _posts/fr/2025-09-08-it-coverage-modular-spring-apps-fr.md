---
audio: false
date: 2025-09-08
generated: true
image: false
lang: fr
layout: post
title: Couverture informatique pour les applications modulaires Spring
translated: true
type: note
---

### Évaluation globale de votre configuration

Votre configuration actuelle est solide pour un petit projet multi-module comme celui-ci, d'autant plus que vous avez déjà le flux principal fonctionnel : attacher l'agent JaCoCo à Jetty, exécuter des tests d'intégration Python externes via le Plugin Exec, et générer un rapport dans le module `PlaygroundWeb`. Cela capture la couverture d'exécution des points de terminaison d'API testés par `unittest` de Python, ce qui est exactement ce dont vous avez besoin pour la couverture des tests d'intégration (IT) dans une application web Spring.

Points forts :
- **Modulaire et lié aux phases** : L'utilisation des phases Maven (`pre-integration-test` pour le démarrage de Jetty, `integration-test` pour les tests Python, `post-integration-test` pour l'arrêt, `verify` pour le rapport) assure la fiabilité et la reproductibilité.
- **Attachement de l'agent** : L'argument JVM (`-javaagent:...`) sur Jetty instrumente correctement l'exécution, capturant la couverture dans `jacoco.it.exec`.
- **Intégration de tests externes** : Le Plugin Exec gère bien Python, et garder les tests à la racine du dépôt (`${project.parent.basedir}/tests`) les découple des modules Java.
- **Aucune duplication inutile** : Vous évitez d'exécuter Jetty/Python dans `PlaygroundUtils` (qui n'a pas de contrôleurs), ce qui est efficace.

Défis que vous avez identifiés :
- **Couverture pour les modules bibliothèque comme `PlaygroundUtils`** : Puisque le code des utils s'exécute dans la JVM `PlaygroundWeb` (en tant que dépendance dans le WAR), il est instrumenté et apparaît dans le `jacoco.it.exec` de `PlaygroundWeb`. Mais vos rapports sont spécifiques aux modules, donc la couverture de `PlaygroundUtils` n'est pas visible à moins d'être agrégée ou incluse.
- **La nature non autonome de JaCoCo** : Contrairement à Checkstyle/Spotless (qui analysent simplement des artefacts sources/statiques), JaCoCo a besoin de données d'exécution (fichiers `.exec`) provenant de tests externes et de l'attachement d'un agent. Cela le rend fragile pour les configurations multi-modules sans une coordination minutieuse.
- **Limitations du goal d'agrégation** : `jacoco:report-aggregate` s'attend à des fichiers `.exec` par module (par exemple, provenant de tests unitaires), mais votre couverture provient uniquement des IT dans un seul module. Forcer l'agrégation peut entraîner des rapports vides pour les bibliothèques comme `PlaygroundUtils`.
- **Évolutivité vers 10+ modules** : Dupliquer les configurations Jetty/Python sur tous les modules serait inefficace (serveurs/tests redondants). Les solutions de contournement approximatives comme copier les fichiers `.exec` ou tout exécuter deux fois (comme vous l'avez mentionné) introduisent une surcharge de maintenance et un gonflement du temps de build.

Votre solution de repli vers des rapports par module est pragmatique, mais nous pouvons optimiser pour l'inclusion de la couverture sans duplication.

### Stratégie recommandée
Concentrez-vous sur la **génération d'un seul rapport de couverture IT complet dans le module qui exécute l'application** (`PlaygroundWeb` ici), tout en **incluant les données de couverture pour les modules dépendants** comme `PlaygroundUtils`. Cela évite d'exécuter les tests plusieurs fois et tire parti du fait que tout le code s'exécute dans une seule JVM.

Pourquoi cela plutôt que l'agrégation ?
- L'agrégation (`report-aggregate`) est meilleure pour la couverture distribuée des tests unitaires entre les modules. Pour la couverture IT provenant d'un seul runtime (votre cas), c'est excessif et ne s'adapte pas naturellement.
- Un rapport unifié donne une vue holistique de la couverture de l'application, ce qui est souvent plus utile que des rapports cloisonnés par module (par exemple, "80 % globalement, mais la couche utils est à 60 %").
- Pour les projets plus importants, cela évolue en traitant le "module d'application" (WAR/EAR) comme le centre de couverture, en y intégrant les dépendances.

#### Mise en œuvre étape par étape pour votre projet à 2 modules
Commencez petit : Appliquez ceci à votre configuration actuelle (1 module app + 1 lib). Testez-la, puis développez.

1. **Gardez l'exécution des IT uniquement dans `PlaygroundWeb`** :
   - Aucun changement nécessaire ici. Jetty démarre le WAR (qui intègre `PlaygroundUtils`), les tests Python atteignent les endpoints, la couverture est capturée dans `${project.build.directory}/jacoco.it.exec`.
   - Confirmez que le code utils est exercé : Si vos tests Python appellent des endpoints qui utilisent les classes `PlaygroundUtils` (par exemple, `SystemUtils`), leur couverture sera dans le fichier `.exec`.

2. **Améliorez le rapport JaCoCo dans `PlaygroundWeb` pour inclure `PlaygroundUtils`** :
   - Utilisez `<additionalClassesDirectories>` et `<additionalSourceDirectories>` de JaCoCo dans le goal `report`. Cela indique à JaCoCo d'analyser les classes/sources de `PlaygroundUtils` par rapport au même fichier `.exec`.
   - Mettez à jour le POM de `PlaygroundWeb` (dans la configuration du `jacoco-maven-plugin`) :

     ```xml
     <plugin>
         <groupId>org.jacoco</groupId>
         <artifactId>jacoco-maven-plugin</artifactId>
         <executions>
             <!-- Préparation existante de l'agent -->
             <execution>
                 <id>prepare-agent</id>
                 <goals>
                     <goal>prepare-agent</goal>
                 </goals>
             </execution>
             <!-- Rapport amélioré : Inclure le module utils -->
             <execution>
                 <id>report-it</id>
                 <phase>verify</phase>
                 <goals>
                     <goal>report</goal>
                 </goals>
                 <configuration>
                     <dataFile>${jacoco.it.exec}</dataFile>
                     <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
                     <!-- Ajoutez ceci pour inclure la couverture de PlaygroundUtils -->
                     <additionalClassesDirectories>
                         <directory>${project.parent.basedir}/PlaygroundUtils/target/classes</directory>
                     </additionalClassesDirectories>
                     <additionalSourceDirectories>
                         <directory>${project.parent.basedir}/PlaygroundUtils/src/main/java</directory>
                     </additionalSourceDirectories>
                 </configuration>
             </execution>
         </executions>
     </plugin>
     ```

   - Cela génère un rapport (dans `PlaygroundWeb/target/site/jacoco-it`) couvrant les deux modules. Vous verrez le détail par package/classe, incluant `org.lzw` des utils.

3. **Désactivez/Supprimez JaCoCo de `PlaygroundUtils`** :
   - Comme il n'a pas ses propres IT, supprimez toute configuration/propriété JaCoCo (par exemple, `<jacoco.it.exec>`, `<it.report.skip>`). Il n'a pas besoin de générer son propre rapport—la couverture est gérée en amont.
   - Si vous avez des tests unitaires dans utils, gardez un `prepare-agent` + `report` séparé pour la couverture unitaire (par défaut `jacoco.exec`), mais isolez-le des IT.

4. **Build et Vérification** :
   - Exécutez `mvn clean verify` depuis le parent.
   - Jetty/Python ne s'exécutent qu'une seule fois (dans `PlaygroundWeb`).
   - Vérifiez `PlaygroundWeb/target/site/jacoco-it/index.html` : Il devrait montrer la couverture pour les classes des deux modules.
   - Si la couverture des utils est à 0 %, assurez-vous que vos tests Python exercent ces classes (par exemple, ajoutez un test qui déclenche `SystemUtils` via un endpoint).

5. **Optionnel : Appliquer des seuils de couverture** :
   - Ajoutez une exécution `check` dans le plugin JaCoCo de `PlaygroundWeb` pour faire échouer le build si la couverture descend en dessous d'un seuil (par exemple, 70 % de couverture des lignes globalement).
     ```xml
     <execution>
         <id>check-it</id>
         <goals>
             <goal>check</goal>
         </goals>
         <configuration>
             <dataFile>${jacoco.it.exec}</dataFile>
             <rules>
                 <rule>
                     <element>BUNDLE</element>
                     <limits>
                         <limit>
                             <counter>LINE</counter>
                             <value>COVEREDRATIO</value>
                             <minimum>0.70</minimum>
                         </limit>
                     </limits>
                 </rule>
             </rules>
         </configuration>
     </execution>
     ```

#### Passage à l'échelle pour un projet plus important (par exemple, 10 modules)
Pour 10+ modules (par exemple, plusieurs libs + 1-2 modules app/WAR), étendez l'approche ci-dessus pour éviter la complexité :

- **Centralisez les IT dans les modules d'application** : Si vous avez un WAR principal (comme `PlaygroundWeb`), faites-en le "centre de couverture". Ajoutez `<additionalClassesDirectories>` et `<additionalSourceDirectories>` pour toutes les bibliothèques dépendantes (par exemple, via une boucle ou des listes de propriétés dans le POM parent).
  - Exemple : Définissez les chemins dans les propriétés du parent :
    ```xml
    <properties>
        <lib1.classes>${project.basedir}/Lib1/target/classes</lib1.classes>
        <lib1.sources>${project.basedir}/Lib1/src/main/java</lib1.sources>
        <!-- Répétez pour 10 libs -->
    </properties>
    ```
  - Dans la configuration du rapport JaCoCo du WAR : Référencez-les dynamiquement.

- **Si plusieurs Apps/WARs** : Créez des modules IT dédiés (par exemple, `App1-IT`, `App2-IT`) qui dépendent du WAR, configurez Jetty/Exec/JaCoCo là-bas, et incluez uniquement les classes/sources des dépendances pertinentes. Cela garde les builds modulaires (par exemple, `mvn verify -pl App1-IT` pour une couverture ciblée).

- **Évitez la duplication des IT par module** : N'exécutez jamais Jetty/Python dans les modules de bibliothèque—c'est inefficace. Si une bibliothèque a besoin d'IT isolées (rare), donnez-lui son propre mini-serveur/suite de tests.

- **Agrégation pour les rapports (si nécessaire)** : Si vous insistez pour avoir des rapports séparés par module :
  - Générez le `.exec` dans le module d'application.
  - Utilisez `dependency:copy` de Maven ou un script personnalisé (via le Plugin Exec) dans le `post-integration-test` du parent pour copier le `.exec` dans le `target/` de chaque lib (par exemple, comme `jacoco-it.exec`).
  - Ensuite, configurez `report` dans chaque lib pour utiliser ce fichier copié.
  - Mais c'est plus complexe—préférez le rapport unifié sauf si les parties prenantes exigent des métriques par module.

- **Conseils d'outillage pour la mise à l'échelle** :
  - **Profils Maven** : Utilisez des profils (par exemple, `-Pcoverage`) pour activer/désactiver les IT/rapports pour des builds de développement plus rapides.
  - **Optimisation CI** : Dans l'intégration continue (par exemple, GitHub Actions), mettez en cache les dépendances Maven et exécutez les IT uniquement sur les changements des tests/endpoints.
  - **Alternatives si JaCoCo devient trop complexe** : Envisagez SonarQube pour l'analyse agrégée (il ingère les données JaCoCo entre les modules). Ou passez à des outils d'exécution comme OpenClover, mais JaCoCo convient si vous respectez l'approche du centre de couverture.
  - **Tester les tests** : Ajoutez un test de fumée en Python pour vérifier le démarrage du serveur (par exemple, interrogez `http://localhost:8080/health`).

Cette stratégie minimise les exécutions (un Jetty/Python par app), gère les dépendances de JaCoCo proprement, et évolue sans explosion. Si vous partagez plus de détails (par exemple, comment utils est utilisé dans les endpoints), je peux affiner les extraits de POM.