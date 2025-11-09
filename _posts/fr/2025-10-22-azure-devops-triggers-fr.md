---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Configuration des Déclencheurs de Branche Azure DevOps
translated: true
type: note
---

Les pipelines Azure DevOps vous permettent de configurer les branches qui déclenchent les builds et les déploiements. Cela se fait principalement via les **déclencheurs d'intégration continue (CI)** (pour les builds lors des pushes de code) et les **déclencheurs de demande de tirage (PR)**. La configuration diffère légèrement entre les pipelines YAML (recommandés pour le contrôle de version) et les pipelines classiques. Ci-dessous, je me concentrerai d'abord sur YAML, car c'est l'approche moderne, puis j'aborderai brièvement les pipelines classiques. Tous les exemples supposent un référentiel Git.

## Pipelines YAML : Configuration des déclencheurs de branche

Les pipelines YAML définissent les déclencheurs directement dans votre fichier `azure-pipelines.yml`. Par défaut, les pipelines se déclenchent sur les pushes vers **toutes les branches** (équivalent à `trigger: branches: include: - '*'`). Vous pouvez personnaliser cela pour un contrôle plus fin.

### Étape 1 : Configuration de base
1. Dans votre projet Azure DevOps, allez dans **Pipelines > Builds** (ou **Releases** pour CD).
2. Créez ou modifiez un pipeline et sélectionnez **YAML** comme modèle.
3. Dans l'éditeur YAML, ajoutez une section `trigger` au niveau racine.

### Étape 2 : Inclusions de branches simples
Utilisez une liste simple pour déclencher sur des branches ou modèles spécifiques :
```yaml
trigger:
- main          # Se déclenche sur les pushes vers 'main'
- develop       # Aussi sur 'develop'
- releases/*    # Toute branche commençant par 'releases/' (ex: releases/v1.0)
```
- Enregistrez et committez le fichier YAML dans votre repo. Le pipeline ne s'exécutera désormais que pour ces branches.
- Les caractères génériques comme `*` (zéro ou plusieurs caractères) et `?` (un seul caractère) sont pris en charge. Mettez entre guillemets les modèles commençant par `*` (ex: `"*-hotfix"`).

### Étape 3 : Inclusions/Exclusions avancées
Pour des exclusions ou plus de précision :
```yaml
trigger:
  branches:
    include:
    - main
    - releases/*
    - feature/*
    exclude:
    - releases/old-*     # Exclut 'releases/old-v1', etc.
    - feature/*-draft    # Exclut les fonctionnalités brouillon
```
- **Include** : Branches qui *peuvent* déclencher (commence par toutes si omis).
- **Exclude** : Filtre la liste d'inclusions (appliqué après les inclusions).
- Si vous spécifiez une clause `branches`, elle remplace la valeur par défaut (toutes les branches) — seules les inclusions explicites déclencheront.
- Pour les tags : Utilisez `refs/tags/v1.*` dans les inclusions.

### Étape 4 : Filtres de chemin (Optionnel)
Combinez avec les chemins de fichiers pour un contrôle granulaire :
```yaml
trigger:
  branches:
    include:
    - main
  paths:
    include:
    - src/*.cs          # Uniquement si changements dans le dossier 'src'
    exclude:
    - docs/*.md         # Ignore les changements de documentation
```
- Les chemins sont relatifs à la racine du repo et sensibles à la casse.

### Étape 5 : Traitement par lot et désactivation
- **Exécutions groupées (Batching)** : Pour regrouper plusieurs pushes en un seul build (réduit le bruit) :
  ```yaml
  trigger:
    batch: true
    branches:
      include:
      - main
  ```
- **Désactiver les déclencheurs** : Définissez `trigger: none` pour désactiver l'intégration continue.
- **Ignorer par commit** : Ajoutez `[skip ci]` ou `***NO_CI***` dans les messages de commit.

### Déclencheurs de demande de tirage (PR)
Pour les demandes de tirage, ajoutez une section `pr` :
```yaml
pr:
  branches:
    include:
    - main
    - develop
  paths:
    include:
    - src/*
```
- Ceci valide les PRs ciblant ces branches.

### Test
- Poussez vers une branche correspondante : Le pipeline s'exécute automatiquement.
- Consultez les exécutions dans **Pipelines > Runs** et vérifiez les détails du déclencheur.

## Pipelines Classiques : Configuration des déclencheurs de branche
Pour les pipelines classiques (basés sur l'interface utilisateur) :
1. Modifiez votre pipeline dans **Pipelines > Builds**.
2. Allez dans **Triggers > Continuous integration**.
3. Cochez **Enable continuous integration**.
4. Sous **Branch filters**, ajoutez des inclusions (ex: `main`) ou des exclusions (ex: `develop`).
5. Pour les chemins : Utilisez **Path filters** dans le même onglet.
6. Pour les PRs : Allez dans **Triggers > Pull request validation** et définissez les filtres de branche.

Passez à YAML pour une meilleure maintenabilité.

## Bonnes pratiques
- Commencez simplement : Déclenchez uniquement sur `main` et `develop`.
- Utilisez les exclusions pour les branches bruyantes comme `*-hotfix`.
- Sécurisez avec les politiques de branche (Repos > Branches > Policies) pour les relecteurs obligatoires.
- Surveillez : Utilisez les analytiques de pipeline pour la fréquence de déclenchement.

Pour les derniers détails, reportez-vous à la documentation officielle.

[Build Azure Repos Git repositories](https://learn.microsoft.com/en-us/azure/devops/pipelines/repos/azure-repos-git?view=azure-devops&tabs=yaml)  
[Triggers in Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/build/triggers?view=azure-devops&tabs=yaml)