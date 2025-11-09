---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide de démarrage rapide d’Azure CLI
translated: true
type: note
---

Azure CLI (Command-Line Interface) est un ensemble d'outils multiplateforme permettant de gérer les ressources Azure depuis la ligne de commande. Il est idéal pour automatiser des tâches, scripter des déploiements et interagir avec les services Azure sans avoir besoin du portail web. Il prend en charge Bash, PowerShell et Command Prompt sur Windows, macOS et Linux.

## Installation

1. **Prérequis** : Assurez-vous d'avoir Python 3.8 ou une version ultérieure installé (vérifiez avec `python --version`).

2. **Installation via le gestionnaire de paquets** (Recommandé) :
   - **Windows** : Utilisez Winget (`winget install Microsoft.AzureCLI`) ou Chocolatey (`choco install azure-cli`).
   - **macOS** : Utilisez Homebrew (`brew install azure-cli`).
   - **Linux (Ubuntu/Debian)** : Exécutez `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`.
   - **Autres distributions Linux** : Utilisez RPM ou le téléchargement manuel depuis le site officiel.

3. **Vérification de l'installation** : Ouvrez un terminal et exécutez `az --version`. Vous devriez voir la version de la CLI (par exemple, 2.64.0 fin 2025).

Pour des étapes détaillées spécifiques à chaque plateforme, reportez-vous à la documentation officielle d'installation.

## Authentification

Avant d'utiliser Azure CLI, connectez-vous à votre compte Azure :

1. **Connexion interactive** : Exécutez `az login`. Cela ouvre un navigateur pour l'authentification Microsoft Entra ID. Suivez les instructions pour vous connecter.

2. **Principal de service (pour l'automatisation)** : Créez un principal de service avec `az ad sp create-for-rbac --name "MyApp" --role contributor --scopes /subscriptions/{subscription-id}`. Puis utilisez `az login --service-principal -u <app-id> -p <password> --tenant <tenant-id>`.

3. **Vérifier la connexion** : Utilisez `az account show` pour vérifier votre abonnement actif.

4. **Déconnexion** : `az logout`.

L'authentification multifacteur (MFA) est prise en charge, et vous pouvez gérer plusieurs abonnements avec `az account set --subscription <id>`.

## Commandes de base

Azure CLI utilise la commande `az` suivie d'un groupe (par exemple, `vm`, `storage`) et de sous-commandes. Utilisez `az --help` pour un aperçu, ou `az <group> --help` pour les détails.

### Options globales courantes
- `--help` ou `-h` : Afficher l'aide.
- `--output table/json/yaml` : Formater la sortie (par défaut : table).
- `--query` : Requête JMESPath pour filtrer la sortie JSON (par exemple, `--query "[].name"`).

### Exemples clés
- **Lister les abonnements** : `az account list --output table`
- **Obtenir les groupes de ressources** : `az group list --output table`
- **Créer un groupe de ressources** : `az group create --name "MyResourceGroup" --location "eastus"`

## Gestion des machines virtuelles (VM)
Azure CLI excelle dans la gestion du cycle de vie des VM.

1. **Créer une VM** :
   ```
   az vm create \
     --resource-group "MyResourceGroup" \
     --name "MyVM" \
     --image Ubuntu2204 \
     --admin-username azureuser \
     --admin-password MyP@ssw0rd123! \
     --location "eastus"
   ```

2. **Lister les VM** : `az vm list --output table`

3. **Démarrer/Arrêter une VM** : `az vm start --name "MyVM" --resource-group "MyResourceGroup"` ou `az vm stop --name "MyVM" --resource-group "MyResourceGroup"`

4. **SSH dans la VM** : `az vm ssh "MyVM" --resource-group "MyResourceGroup"`

5. **Supprimer une VM** : `az vm delete --name "MyVM" --resource-group "MyResourceGroup" --yes`

## Gestion des comptes de stockage
1. **Créer un compte de stockage** :
   ```
   az storage account create \
     --name mystorageaccount \
     --resource-group "MyResourceGroup" \
     --location "eastus" \
     --sku Standard_LRS
   ```

2. **Téléverser un blob** : D'abord, obtenez la clé avec `az storage account keys list --account-name mystorageaccount --resource-group "MyResourceGroup" --query "[0].value -o tsv"`. Puis : `az storage blob upload --account-name mystorageaccount --container-name mycontainer --name myfile.txt --file ./myfile.txt --auth-mode key`

## Autres scénarios courants
- **Déployer des modèles ARM** : `az deployment group create --resource-group "MyResourceGroup" --template-file template.json`
- **Interroger les ressources** : `az resource list --resource-group "MyResourceGroup" --output table`
- **Mettre à jour la CLI** : `az upgrade`
- **Extensions** : Installez des extensions comme `az extension add --name azure-devops` pour des commandes supplémentaires.

Pour le scripting, combinez avec des boucles Bash/PowerShell ou utilisez Azure CLI dans des pipelines CI/CD comme GitHub Actions.

## Conseils et bonnes pratiques
- Utilisez `--dry-run` pour les prévisualisations (lorsque c'est pris en charge).
- Activez l'auto-complétion : Sur Bash, exécutez `az completion`.
- Gérez les erreurs : Vérifiez les codes de sortie (0 pour succès) et utilisez `--debug` pour le dépannage.
- Sécurité : Évitez de coder en dur les informations d'identification ; utilisez des variables d'environnement ou Azure Key Vault.

## Références
[Installer Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
[Référence Azure CLI](https://learn.microsoft.com/en-us/cli/azure/)
[Démarrage rapide Azure CLI](https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli)