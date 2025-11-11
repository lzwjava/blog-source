---
audio: false
generated: true
lang: fr
layout: post
title: Plugin de publication Maven
translated: true
type: note
---

Voici un guide complet sur l'utilisation du **Maven Release Plugin** pour gérer et automatiser le processus de publication de votre projet Maven.

---

### Qu'est-ce que le Maven Release Plugin ?

Le **Maven Release Plugin** est un outil qui automatise le processus de publication d'un projet Maven. Il gère des tâches telles que :

- La mise à jour des numéros de version dans le(s) fichier(s) POM de votre projet.
- La validation des changements dans votre système de contrôle de version (VCS), tel que Git.
- La création d'un tag pour la publication dans le VCS.
- La construction et le déploiement des artefacts de la publication.
- La préparation du projet pour le prochain cycle de développement en mettant à nouveau à jour les numéros de version.

Les deux objectifs principaux du plugin sont :

- **`release:prepare`** : Prépare le projet pour une publication en mettant à jour les versions, en validant les changements et en taguant la publication dans le VCS.
- **`release:perform`** : Construit et déploie la version publiée en utilisant le code tagué du VCS.

---

### Guide étape par étape pour utiliser le Maven Release Plugin

#### 1. Ajouter le Maven Release Plugin à votre fichier POM

Pour utiliser le plugin, vous devez l'inclure dans le `pom.xml` de votre projet. Ajoutez-le dans la section `<build><plugins>` comme suit :

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-release-plugin</artifactId>
            <version>2.5.3</version> <!-- Utilisez la dernière version stable -->
        </plugin>
    </plugins>
</build>
```

**Remarque** : Consultez la [page officielle du Maven Release Plugin](https://maven.apache.org/maven-release/maven-release-plugin/) pour la dernière version et remplacez `2.5.3` en conséquence.

#### 2. Configurer la section SCM (Source Control Management)

Le plugin interagit avec votre VCS (par exemple, Git) pour valider les changements et créer des tags. Vous devez spécifier les détails de votre VCS dans la section `<scm>` de votre `pom.xml`. Pour un dépôt Git hébergé sur GitHub, cela pourrait ressembler à ceci :

```xml
<scm>
    <connection>scm:git:git://github.com/username/project.git</connection>
    <developerConnection>scm:git:git@github.com:username/project.git</developerConnection>
    <url>https://github.com/username/project</url>
</scm>
```

- Remplacez `username` et `project` par votre nom d'utilisateur GitHub et le nom de votre dépôt.
- Ajustez les URLs si vous utilisez un autre service d'hébergement Git (par exemple, GitLab, Bitbucket).
- Assurez-vous d'avoir les identifiants nécessaires configurés (par exemple, clés SSH ou token d'accès personnel) pour pousser les changements vers le dépôt.

#### 3. Préparer votre projet pour la publication

Avant d'exécuter les commandes de publication, assurez-vous que votre projet est prêt :

- Tous les tests passent (`mvn test`).
- Il n'y a pas de changements non validés dans votre répertoire de travail (exécutez `git status` pour vérifier).
- Vous êtes sur la bonne branche (par exemple, `master` ou `main`) pour la publication.

#### 4. Exécuter `release:prepare`

L'objectif `release:prepare` prépare votre projet pour la publication. Exécutez la commande suivante dans votre terminal :

```bash
mvn release:prepare
```

**Ce qui se passe pendant `release:prepare`** :

- **Vérifie les changements non validés** : S'assure que votre répertoire de travail est propre.
- **Demande les versions** : Demande la version de publication et la prochaine version de développement.
  - Exemple : Si votre version actuelle est `1.0-SNAPSHOT`, il pourrait suggérer `1.0` pour la publication et `1.1-SNAPSHOT` pour la prochaine version de développement. Vous pouvez accepter les valeurs par défaut ou saisir des versions personnalisées (par exemple, `1.0.1` pour une publication de correctif).
- **Met à jour les fichiers POM** : Change la version vers la version de publication (par exemple, `1.0`), valide le changement et le tagge dans le VCS (par exemple, `project-1.0`).
- **Prépare pour le prochain cycle** : Met à jour le POM vers la prochaine version de développement (par exemple, `1.1-SNAPSHOT`) et la valide.

**Simulation optionnelle** : Pour tester le processus sans effectuer de changements, utilisez :

```bash
mvn release:prepare -DdryRun=true
```

Cela simule les étapes de préparation sans valider ou tagger.

#### 5. Exécuter `release:perform`

Après avoir préparé la publication, construisez et déployez-la avec :

```bash
mvn release:perform
```

**Ce qui se passe pendant `release:perform`** :

- Récupère la version taguée depuis le VCS.
- Construit le projet.
- Déploie les artefacts vers le dépôt spécifié dans la section `<distributionManagement>` de votre POM.

**Configurer `<distributionManagement>`** (si vous déployez vers un dépôt distant) :

```xml
<distributionManagement>
    <repository>
        <id>releases</id>
        <url>http://my-repository-manager/releases</url>
    </repository>
    <snapshotRepository>
        <id>snapshots</id>
        <url>http://my-repository-manager/snapshots</url>
    </snapshotRepository>
</distributionManagement>
```

- Remplacez les URLs par les adresses de votre gestionnaire de dépôt (par exemple, Nexus, Artifactory).
- Assurez-vous que les identifiants sont configurés dans votre fichier `~/.m2/settings.xml` sous `<servers>` avec des `id` correspondants.

#### 6. Vérifier la publication

Après `release:perform`, vérifiez la publication :

- Vérifiez dans votre gestionnaire de dépôt que les artefacts (par exemple, JARs, sources) sont déployés.
- Testez la version publiée dans un autre projet en l'ajoutant comme dépendance dans son POM.

---

### Configuration supplémentaire et conseils

#### Gestion des échecs

- **Nettoyage** : Si le processus de publication échoue, utilisez :
  ```bash
  mvn release:clean
  ```
  pour supprimer les fichiers temporaires créés par le plugin.
- **Annulation** : Pour annuler les changements effectués par `release:prepare` :
  ```bash
  mvn release:rollback
  ```
  Soyez prudent et vérifiez quels changements sont annulés.

#### Projets multi-modules

Pour les projets multi-modules, le plugin met à jour les versions de tous les modules de manière cohérente par défaut. Assurez-vous que le POM parent inclut la configuration du plugin et du SCM.

#### Mode batch pour l'automatisation

Pour exécuter la publication de manière non interactive (par exemple, dans un pipeline CI/CD), utilisez l'option `-B` et spécifiez les versions :

```bash
mvn release:prepare -B -DreleaseVersion=1.0 -DdevelopmentVersion=1.1-SNAPSHOT
mvn release:perform -B
```

#### Problèmes courants et solutions

- **Erreurs VCS** : Assurez-vous que les commandes Git (par exemple, `git commit`, `git push`) fonctionnent manuellement. Vérifiez l'authentification (clés SSH, tokens).
- **Échecs de construction** : Vérifiez que la construction réussit localement (`mvn clean install`) et que les dépendances se résolvent correctement.
- **Stratégie de version** : Personnalisez les versions pendant les invites ou via des propriétés si les valeurs par défaut ne conviennent pas à vos besoins.

---

### Récapitulatif des commandes

1. **Préparer la publication** :
   ```bash
   mvn release:prepare
   ```
2. **Exécuter la publication** :
   ```bash
   mvn release:perform
   ```
3. **Simulation optionnelle** :
   ```bash
   mvn release:prepare -DdryRun=true
   ```
4. **Nettoyage ou annulation si nécessaire** :
   ```bash
   mvn release:clean
   mvn release:rollback
   ```

---

### Conclusion

Le Maven Release Plugin simplifie le processus de publication en automatisant la gestion des versions, les interactions avec le VCS et le déploiement. En ajoutant le plugin à votre POM, en configurant votre SCM et en suivant les étapes `release:prepare` et `release:perform`, vous pouvez publier efficacement vos projets Maven. Testez toujours votre configuration avec une simulation et vérifiez les résultats pour garantir un processus de publication fluide.