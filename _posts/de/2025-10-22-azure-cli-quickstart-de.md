---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Azure CLI-Schnellstartanleitung
translated: true
type: note
---

Azure CLI (Command-Line Interface) ist ein plattformübergreifendes Toolset zur Verwaltung von Azure-Ressourcen über die Befehlszeile. Es eignet sich ideal zum Automatisieren von Aufgaben, Skripterstellung für Bereitstellungen und zur Interaktion mit Azure-Diensten, ohne das Webportal zu benötigen. Es unterstützt Bash, PowerShell und die Eingabeaufforderung unter Windows, macOS und Linux.

## Installation

1. **Voraussetzungen**: Stellen Sie sicher, dass Python 3.8 oder höher installiert ist (prüfen Sie mit `python --version`).

2. **Installation über einen Paketmanager** (Empfohlen):
   - **Windows**: Verwenden Sie Winget (`winget install Microsoft.AzureCLI`) oder Chocolatey (`choco install azure-cli`).
   - **macOS**: Verwenden Sie Homebrew (`brew install azure-cli`).
   - **Linux (Ubuntu/Debian)**: Führen Sie `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash` aus.
   - **Andere Linux-Distributionen**: Verwenden Sie RPM oder einen manuellen Download von der offiziellen Website.

3. **Installation überprüfen**: Öffnen Sie ein Terminal und führen Sie `az --version` aus. Sie sollten die CLI-Version sehen (z. B. 2.64.0 Stand Ende 2025).

Detaillierte, plattformspezifische Schritte finden Sie in der offiziellen Installationsdokumentation.

## Authentifizierung

Bevor Sie die Azure CLI verwenden, müssen Sie sich bei Ihrem Azure-Konto anmelden:

1. **Interaktive Anmeldung**: Führen Sie `az login` aus. Dies öffnet einen Browser für die Microsoft Entra ID-Authentifizierung. Folgen Sie den Anweisungen, um sich anzumelden.

2. **Dienstprinzipal (für Automatisierung)**: Erstellen Sie einen Dienstprinzipal mit `az ad sp create-for-rbac --name "MyApp" --role contributor --scopes /subscriptions/{subscription-id}`. Verwenden Sie dann `az login --service-principal -u <app-id> -p <password> --tenant <tenant-id>`.

3. **Anmeldung überprüfen**: Verwenden Sie `az account show`, um Ihr aktives Abonnement zu überprüfen.

4. **Abmelden**: `az logout`.

Multi-Faktor-Authentifizierung (MFA) wird unterstützt, und Sie können mehrere Abonnements mit `az account set --subscription <id>` verwalten.

## Grundlegende Befehle

Die Azure CLI verwendet den Befehl `az`, gefolgt von einer Gruppe (z. B. `vm`, `storage`) und Unterbefehlen. Verwenden Sie `az --help` für einen Überblick oder `az <group> --help` für spezifische Details.

### Häufige globale Optionen
- `--help` oder `-h`: Hilfe anzeigen.
- `--output table/json/yaml`: Formatieren der Ausgabe (Standard: Tabelle).
- `--query`: JMESPath-Abfrage zum Filtern der JSON-Ausgabe (z. B. `--query "[].name"`).

### Wichtige Beispiele
- **Abonnements auflisten**: `az account list --output table`
- **Ressourcengruppen abrufen**: `az group list --output table`
- **Ressourcengruppe erstellen**: `az group create --name "MyResourceGroup" --location "eastus"`

## Verwalten virtueller Maschinen (VMs)
Die Azure CLI eignet sich hervorragend für die Lebenszyklusverwaltung von VMs.

1. **VM erstellen**:
   ```
   az vm create \
     --resource-group "MyResourceGroup" \
     --name "MyVM" \
     --image Ubuntu2204 \
     --admin-username azureuser \
     --admin-password MyP@ssw0rd123! \
     --location "eastus"
   ```

2. **VMs auflisten**: `az vm list --output table`

3. **VM starten/stoppen**: `az vm start --name "MyVM" --resource-group "MyResourceGroup"` oder `az vm stop --name "MyVM" --resource-group "MyResourceGroup"`

4. **SSH-Verbindung zur VM**: `az vm ssh "MyVM" --resource-group "MyResourceGroup"`

5. **VM löschen**: `az vm delete --name "MyVM" --resource-group "MyResourceGroup" --yes`

## Verwalten von Speicherkonten
1. **Speicherkonto erstellen**:
   ```
   az storage account create \
     --name mystorageaccount \
     --resource-group "MyResourceGroup" \
     --location "eastus" \
     --sku Standard_LRS
   ```

2. **Blob hochladen**: Rufen Sie zuerst den Schlüssel mit `az storage account keys list --account-name mystorageaccount --resource-group "MyResourceGroup" --query "[0].value -o tsv"` ab. Dann: `az storage blob upload --account-name mystorageaccount --container-name mycontainer --name myfile.txt --file ./myfile.txt --auth-mode key`

## Weitere häufige Szenarien
- **ARM-Vorlagen bereitstellen**: `az deployment group create --resource-group "MyResourceGroup" --template-file template.json`
- **Ressourcen abfragen**: `az resource list --resource-group "MyResourceGroup" --output table`
- **CLI aktualisieren**: `az upgrade`
- **Erweiterungen**: Installieren Sie Erweiterungen wie `az extension add --name azure-devops` für zusätzliche Befehle.

Für die Skripterstellung können Sie sie mit Bash/PowerShell-Schleifen kombinieren oder die Azure CLI in CI/CD-Pipelines wie GitHub Actions verwenden.

## Tipps und Best Practices
- Verwenden Sie `--dry-run` für Vorschauen (wo unterstützt).
- Aktivieren Sie die Auto-Vervollständigung: Führen Sie unter Bash `az completion` aus.
- Fehlerbehandlung: Überprüfen Sie Exit-Codes (0 für Erfolg) und verwenden Sie `--debug` zur Problembehebung.
- Sicherheit: Vermeiden Sie das Hardcodieren von Anmeldeinformationen; verwenden Sie stattdessen Umgebungsvariablen oder Azure Key Vault.

## Referenzen
[Azure CLI installieren](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)  
[Azure CLI-Referenz](https://learn.microsoft.com/en-us/cli/azure/)  
[Schnellstart für Azure CLI](https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli)