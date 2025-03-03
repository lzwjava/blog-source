---
audio: false
generated: true
lang: fr
layout: post
title: Utiliser Azure DevOps Pipelines
translated: true
---

Décortiquons cela en deux parties : **l'utilisation des pipelines Azure DevOps** et **l'écriture de YAML pour les pipelines**. Je fournirai une explication claire et pratique pour les deux.

---

### **Comment utiliser les pipelines Azure DevOps**
Azure DevOps Pipelines est un outil CI/CD (Intégration Continue/Déploiement Continu) qui automatise la construction, le test et le déploiement du code. Voici comment commencer :

#### **1. Configurer un projet**
- Connectez-vous à Azure DevOps (dev.azure.com) avec votre organisation.
- Créez un nouveau projet (ou utilisez un projet existant) en cliquant sur "Nouveau projet", en lui donnant un nom et en définissant la visibilité (public/privé).

#### **2. Connecter votre code**
- Allez dans **Repos** de votre projet et poussez votre code vers un dépôt (GitHub, Azure Repos, Bitbucket, etc.).
- Alternativement, liez un dépôt externe sous **Pipelines > Nouveau pipeline > Connecter** et sélectionnez votre source.

#### **3. Créer un pipeline**
- Accédez à **Pipelines > Builds > Nouveau pipeline**.
- Choisissez votre dépôt et votre branche.
- Azure propose deux options :
  - **Éditeur classique** : Une approche basée sur l'interface graphique (pas de YAML nécessaire).
  - **YAML** : Un pipeline basé sur le code (recommandé pour la flexibilité et le contrôle de version).
- Pour YAML, sélectionnez "Pipeline de démarrage" ou configurez à partir d'un fichier existant dans votre dépôt.

#### **4. Définir le pipeline**
- Si vous utilisez YAML, vous écrirez un fichier `.yml` (par exemple, `azure-pipelines.yml`) à la racine de votre dépôt. (Plus de détails ci-dessous.)
- Ajoutez des déclencheurs (par exemple, exécuter à chaque push vers `main`), des étapes (par exemple, construire, tester) et des cibles de déploiement.

#### **5. Exécuter et surveiller**
- Enregistrez et validez le fichier YAML (ou enregistrez dans l'éditeur classique).
- Cliquez sur **Exécuter** pour déclencher manuellement le pipeline, ou laissez-le s'exécuter automatiquement en fonction des déclencheurs.
- Vérifiez les journaux sous **Pipelines > Builds** pour surveiller les progrès ou diagnostiquer les échecs.

#### **6. Déployer (Optionnel)**
- Ajoutez un **pipeline de release** (sous **Releases**) ou étendez votre YAML pour déployer vers des environnements comme Azure App Service, Kubernetes ou des machines virtuelles.

---

### **Comment écrire du YAML pour Azure Pipelines**
YAML (Yet Another Markup Language) est un format lisible par l'homme utilisé pour définir les configurations de pipeline. Voici un cours intensif :

#### **Structure de base**
```yaml
trigger:
  - main  # Exécuter le pipeline lorsque la branche 'main' est mise à jour

pool:
  vmImage: 'ubuntu-latest'  # Spécifier l'agent de construction (par exemple, Ubuntu, Windows, macOS)

steps:
  - script: echo Hello, world!  # Une commande simple à exécuter
    displayName: 'Exécuter un script en une ligne'
```

- **`trigger`** : Définit quand le pipeline s'exécute (par exemple, à chaque push vers `main`).
- **`pool`** : Spécifie l'image de la machine virtuelle pour l'agent de construction.
- **`steps`** : Liste les tâches à exécuter (scripts, tâches intégrées, etc.).

#### **Éléments courants**
1. **Variables** :
   ```yaml
   variables:
     buildConfiguration: 'Release'
   steps:
     - script: echo $(buildConfiguration)  # Affiche 'Release'
   ```

2. **Jobs** (grouper les étapes) :
   ```yaml
   jobs:
   - job: Build
     steps:
       - script: echo Building...
   - job: Test
     steps:
       - script: echo Testing...
   ```

3. **Tasks** (actions pré-construites) :
   ```yaml
   steps:
     - task: DotNetCoreCLI@2  # Exemple : Construire un projet .NET
       inputs:
         command: 'build'
         projects: '**/*.csproj'
   ```

4. **Conditions** :
   ```yaml
   steps:
     - script: echo This runs only on main
       condition: eq(variables['Build.SourceBranch'], 'refs/heads/main')
   ```

5. **Stages** (pour les pipelines à phases multiples) :
   ```yaml
   stages:
   - stage: Build
     jobs:
       - job: BuildJob
         steps:
           - script: echo Building...
   - stage: Deploy
     dependsOn: Build
     jobs:
       - job: DeployJob
         steps:
           - script: echo Deploying...
   ```

#### **Exemple du monde réel**
Voici un pipeline pour une application Node.js :
```yaml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

steps:
  - task: NodeTool@0  # Installer Node.js
    inputs:
      versionSpec: '16.x'
    displayName: 'Installer Node.js'

  - script: |
      npm install
      npm run build
    displayName: 'Installer et Construire'

  - task: CopyFiles@2  # Copier les artefacts de construction
    inputs:
      contents: 'dist/**'
      targetFolder: '$(Build.ArtifactStagingDirectory)'

  - task: PublishBuildArtifacts@1  # Publier les artefacts
    inputs:
      pathToPublish: '$(Build.ArtifactStagingDirectory)'
      artifactName: 'dist'
```

#### **Conseils pour écrire du YAML**
- Utilisez une indentation cohérente (2 espaces, pas de tabulations).
- Validez la syntaxe avec un éditeur (par exemple, VS Code avec l'extension "YAML").
- Faites référence au [schéma YAML des pipelines Azure](https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema) pour les options.
- Commencez simplement, puis ajoutez de la complexité (par exemple, des étapes, des variables) au besoin.

---

### **Étapes suivantes**
- **Essayez-le** : Créez un dépôt, ajoutez un fichier `azure-pipelines.yml` de base comme celui ci-dessus et exécutez-le dans Azure DevOps.
- **En savoir plus** : Consultez la documentation officielle de Microsoft [ici](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started) ou recherchez des pipelines d'exemple sur GitHub.
- **Demandez-moi** : Si vous rencontrez un problème ou si vous avez besoin d'un exemple spécifique (par exemple, Python, Java), faites-le moi savoir !

Dans quoi souhaitez-vous approfondir ? La configuration d'un pipeline, la syntaxe YAML ou autre chose ?