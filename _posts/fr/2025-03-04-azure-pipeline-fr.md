---
audio: false
generated: true
lang: fr
layout: post
title: Utilisation des Pipelines Azure DevOps
translated: true
type: note
---

Décomposons cela en deux parties : **l'utilisation d'Azure DevOps Pipelines** et **l'écriture de YAML pour les pipelines**. Je vais fournir une explication claire et pratique pour les deux.

---

### **Comment Utiliser Azure DevOps Pipelines**
Azure DevOps Pipelines est un outil CI/CD (Intégration Continue/Déploiement Continu) qui automatise la construction, les tests et le déploiement du code. Voici comment commencer :

#### **1. Configurer un Projet**
- Connectez-vous à Azure DevOps (dev.azure.com) avec votre organisation.
- Créez un nouveau projet (ou utilisez un existant) en cliquant sur "Nouveau projet", en lui donnant un nom et en définissant sa visibilité (public/privé).

#### **2. Connecter Votre Code**
- Allez dans **Repos** de votre projet et poussez votre code vers un référentiel (GitHub, Azure Repos, Bitbucket, etc.).
- Sinon, liez un référentiel externe sous **Pipelines > Nouveau pipeline > Connecter** et sélectionnez votre source.

#### **3. Créer un Pipeline**
- Naviguez vers **Pipelines** > **Builds** > **Nouveau pipeline**.
- Choisissez votre référentiel et votre branche.
- Azure propose deux options :
  - **Éditeur Classique** : Une approche basée sur une interface graphique (pas besoin de YAML).
  - **YAML** : Un pipeline basé sur du code (recommandé pour sa flexibilité et le contrôle de version).
- Pour YAML, sélectionnez "Pipeline de démarrage" ou configurez à partir d'un fichier existant dans votre référentiel.

#### **4. Définir le Pipeline**
- Si vous utilisez YAML, vous écrirez un fichier `.yml` (par exemple, `azure-pipelines.yml`) à la racine de votre référentiel. (Plus de détails ci-dessous.)
- Ajoutez des déclencheurs (ex : exécution à chaque push sur `main`), des étapes (ex : build, test) et des cibles de déploiement.

#### **5. Exécuter et Surveiller**
- Enregistrez et committez le fichier YAML (ou enregistrez dans l'Éditeur Classique).
- Cliquez sur **Exécuter** pour déclencher le pipeline manuellement, ou laissez-le s'exécuter automatiquement en fonction des déclencheurs.
- Vérifiez les journaux sous **Pipelines > Builds** pour surveiller la progression ou résoudre les échecs.

#### **6. Déployer (Optionnel)**
- Ajoutez un **Pipeline de release** (sous **Releases**) ou étendez votre YAML pour déployer sur des environnements comme Azure App Service, Kubernetes, ou des machines virtuelles.

---

### **Comment Écrire du YAML pour Azure Pipelines**
YAML (Yet Another Markup Language) est un format lisible par l'homme utilisé pour définir les configurations de pipeline. Voici un cours accéléré :

#### **Structure de Base**
```yaml
trigger:
  - main  # Exécute le pipeline lorsque la branche 'main' est mise à jour

pool:
  vmImage: 'ubuntu-latest'  # Spécifie l'agent de build (ex : Ubuntu, Windows, macOS)

steps:
  - script: echo Hello, world!  # Une simple commande à exécuter
    displayName: 'Exécuter un script d''une ligne'
```

- **`trigger`** : Définit quand le pipeline s'exécute (ex : sur un push vers `main`).
- **`pool`** : Spécifie l'image de machine virtuelle pour l'agent de build.
- **`steps`** : Liste les tâches à exécuter (scripts, tâches intégrées, etc.).

#### **Éléments Courants**
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

3. **Tâches** (actions pré-construites) :
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
     - script: echo Ceci s'exécute seulement sur main
       condition: eq(variables['Build.SourceBranch'], 'refs/heads/main')
   ```

5. **Stages** (pour les pipelines multi-phases) :
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

#### **Exemple Concret**
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
    displayName: 'Installer et Builder'

  - task: CopyFiles@2  # Copier les artefacts de build
    inputs:
      contents: 'dist/**'
      targetFolder: '$(Build.ArtifactStagingDirectory)'

  - task: PublishBuildArtifacts@1  # Publier les artefacts
    inputs:
      pathToPublish: '$(Build.ArtifactStagingDirectory)'
      artifactName: 'dist'
```

#### **Conseils pour Écrire du YAML**
- Utilisez une indentation cohérente (2 espaces, pas de tabulations).
- Validez la syntaxe avec un éditeur (ex : VS Code avec l'extension "YAML").
- Référez-vous au [schéma YAML Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema) pour les options.
- Commencez simplement, puis ajoutez de la complexité (ex : stages, variables) au besoin.

---

### **Prochaines Étapes**
- **Essayez** : Créez un référentiel, ajoutez un `azure-pipelines.yml` basique comme celui ci-dessus et exécutez-le dans Azure DevOps.
- **Apprenez-en plus** : Consultez la [documentation officielle](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started) de Microsoft ou cherchez des exemples de pipelines sur GitHub.
- **Demandez-moi** : Si vous rencontrez un problème ou souhaitez un exemple spécifique (ex : Python, Java), faites-le moi savoir !

Dans quoi souhaitez-vous approfondir ? La configuration d'un pipeline, la syntaxe YAML, ou autre chose ?