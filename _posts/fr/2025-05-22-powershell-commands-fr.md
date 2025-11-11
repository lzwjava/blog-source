---
audio: false
generated: true
lang: fr
layout: post
title: Guide des commandes PowerShell
translated: true
type: note
---

## Introduction à PowerShell
PowerShell est un framework d'automatisation des tâches et de gestion de configuration de Microsoft, composé d'un shell en ligne de commande et d'un langage de script. Il est construit sur le .NET Framework (et .NET Core dans les versions plus récentes), permettant aux administrateurs d'effectuer des tâches complexes sur les systèmes Windows, Linux et macOS.

Les commandes PowerShell, appelées **cmdlets** (prononcé "command-lets"), suivent une convention de dénomination `Verbe-Nom` (par exemple, `Get-Process`, `Set-Item`). Ce guide couvre les cmdlets essentielles, classées par fonctionnalité, avec des exemples pour illustrer leur utilisation.

---

## 1. Concepts de base de PowerShell
Avant de plonger dans les commandes, il est crucial de comprendre les concepts clés :
- **Cmdlets** : Commandes légères qui exécutent des fonctions spécifiques.
- **Pipelines** : Permettent de passer la sortie d'une cmdlet en entrée à une autre en utilisant l'opérateur `|`.
- **Modules** : Collections de cmdlets, scripts et fonctions qui étendent les fonctionnalités de PowerShell.
- **Fournisseurs (Providers)** : Interfaces pour accéder aux magasins de données (par exemple, le système de fichiers, le registre) comme s'il s'agissait de lecteurs.
- **Objets** : PowerShell travaille avec des objets, et non du texte brut, permettant une manipulation structurée des données.

---

## 2. Cmdlets essentielles par catégorie

### 2.1 Informations système
Ces cmdlets récupèrent des informations sur le système, les processus et les services.

| Cmdlet | Description | Exemple |
|--------|-------------|---------|
| `Get-ComputerInfo` | Récupère les détails du matériel et des logiciels du système. | `Get-ComputerInfo | Select-Object WindowsProductName, OsVersion` |
| `Get-Process` | Liste les processus en cours d'exécution. | `Get-Process | Where-Object {$_.CPU -gt 1000}` |
| `Get-Service` | Affiche les services sur le système. | `Get-Service | Where-Object {$_.Status -eq "Running"}` |
| `Get-HotFix` | Liste les mises à jour Windows installées. | `Get-HotFix | Sort-Object InstalledOn -Descending` |

**Exemple** : Lister tous les processus en cours d'exécution triés par utilisation du CPU.
```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object Name, CPU, Id -First 5
```

### 2.2 Gestion des fichiers et répertoires
PowerShell traite le système de fichiers comme un fournisseur, permettant une navigation similaire à un lecteur.

| Cmdlet | Description | Exemple |
|--------|-------------|---------|
| `Get-Item` | Récupère les fichiers ou répertoires. | `Get-Item C:\Users\*.txt` |
| `Set-Item` | Modifie les propriétés des éléments (par exemple, les attributs de fichier). | `Set-Item -Path C:\test.txt -Value "Nouveau contenu"` |
| `New-Item` | Crée un nouveau fichier ou répertoire. | `New-Item -Path C:\Docs -Name Report.txt -ItemType File` |
| `Remove-Item` | Supprime les fichiers ou répertoires. | `Remove-Item C:\Docs\OldFile.txt` |
| `Copy-Item` | Copie les fichiers ou répertoires. | `Copy-Item C:\Docs\Report.txt D:\Backup` |
| `Move-Item` | Déplace les fichiers ou répertoires. | `Move-Item C:\Docs\Report.txt C:\Archive` |

**Exemple** : Créer un répertoire et un fichier, puis le copier vers un autre emplacement.
```powershell
New-Item -Path C:\Temp -Name MyFolder -ItemType Directory
New-Item -Path C:\Temp\MyFolder -Name Test.txt -ItemType File
Copy-Item C:\Temp\MyFolder\Test.txt C:\Backup
```

### 2.3 Gestion du système
Cmdlets pour gérer les paramètres système, les services et les utilisateurs.

| Cmdlet | Description | Exemple |
|--------|-------------|---------|
| `Start-Service` | Démarre un service. | `Start-Service -Name "wuauserv"` |
| `Stop-Service` | Arrête un service. | `Stop-Service -Name "wuauserv"` |
| `Restart-Computer` | Redémarre le système. | `Restart-Computer -Force` |
| `Get-EventLog` | Récupère les entrées du journal des événements. | `Get-EventLog -LogName System -Newest 10` |
| `Set-ExecutionPolicy` | Définit la politique d'exécution des scripts. | `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` |

**Exemple** : Vérifier le statut du service Windows Update et le démarrer s'il est arrêté.
```powershell
$service = Get-Service -Name "wuauserv"
if ($service.Status -eq "Stopped") {
    Start-Service -Name "wuauserv"
}
```

### 2.4 Gestion du réseau
Cmdlets pour la configuration réseau et les diagnostics.

| Cmdlet | Description | Exemple |
|--------|-------------|---------|
| `Test-Connection` | Effectue un ping vers un hôte distant. | `Test-Connection google.com` |
| `Get-NetAdapter` | Liste les adaptateurs réseau. | `Get-NetAdapter | Select-Object Name, Status` |
| `Get-NetIPAddress` | Récupère les configurations d'adresse IP. | `Get-NetIPAddress -AddressFamily IPv4` |
| `Resolve-DnsName` | Résout les noms DNS. | `Resolve-DnsName www.google.com` |

**Exemple** : Effectuer un ping vers un serveur et vérifier sa résolution DNS.
```powershell
Test-Connection -ComputerName google.com -Count 2
Resolve-DnsName google.com
```

### 2.5 Gestion des utilisateurs et des groupes
Cmdlets pour gérer les utilisateurs et groupes locaux.

| Cmdlet | Description | Exemple |
|--------|-------------|---------|
| `New-LocalUser` | Crée un compte utilisateur local. | `New-LocalUser -Name "TestUser" -Password (ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force)` |
| `Remove-LocalUser` | Supprime un compte utilisateur local. | `Remove-LocalUser -Name "TestUser"` |
| `Get-LocalGroup` | Liste les groupes locaux. | `Get-LocalGroup | Select-Object Name` |
| `Add-LocalGroupMember` | Ajoute un utilisateur à un groupe local. | `Add-LocalGroupMember -Group "Administrators" -Member "TestUser"` |

**Exemple** : Créer un nouvel utilisateur local et l'ajouter au groupe Administrateurs.
```powershell
$password = ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force
New-LocalUser -Name "TestUser" -Password $password -FullName "Test User" -Description "Compte de test"
Add-LocalGroupMember -Group "Administrators" -Member "TestUser"
```

### 2.6 Scripting et automatisation
PowerShell excelle dans le scripting pour l'automatisation.

| Cmdlet | Description | Exemple |
|--------|-------------|---------|
| `Write-Output` | Envoie des données dans le pipeline. | `Write-Output "Hello, World!"` |
| `ForEach-Object` | Parcourt les éléments dans un pipeline. | `Get-Process | ForEach-Object { $_.Name }` |
| `Where-Object` | Filtre les objets en fonction de conditions. | `Get-Service | Where-Object { $_.Status -eq "Running" }` |
| `Invoke-Command` | Exécute des commandes sur des ordinateurs locaux ou distants. | `Invoke-Command -ComputerName Server01 -ScriptBlock { Get-Process }` |
| `New-ScheduledTask` | Crée une tâche planifiée. | `New-ScheduledTask -Action (New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-File C:\script.ps1") -Trigger (New-ScheduledTaskTrigger -Daily -At "3AM")` |

**Exemple** : Créer un script pour enregistrer les processus en cours d'exécution dans un fichier.
```powershell
$logPath = "C:\Logs\ProcessLog.txt"
Get-Process | Select-Object Name, CPU, StartTime | Export-Csv -Path $logPath -NoTypeInformation
```

### 2.7 Gestion des modules
Les modules étendent les fonctionnalités de PowerShell.

| Cmdlet | Description | Exemple |
|--------|-------------|---------|
| `Get-Module` | Liste les modules disponibles ou importés. | `Get-Module -ListAvailable` |
| `Import-Module` | Importe un module. | `Import-Module ActiveDirectory` |
| `Install-Module` | Installe un module à partir d'un référentiel. | `Install-Module -Name PSWindowsUpdate -Force` |
| `Find-Module` | Recherche des modules dans un référentiel. | `Find-Module -Name *Azure*` |

**Exemple** : Installer et importer le module PSWindowsUpdate pour gérer les mises à jour Windows.
```powershell
Install-Module -Name PSWindowsUpdate -Force
Import-Module PSWindowsUpdate
Get-WUList
```

---

## 3. Utilisation des pipelines
Le pipeline (`|`) permet d'enchaîner les cmdlets pour traiter les données séquentiellement. Par exemple :
```powershell
Get-Process | Where-Object { $_.WorkingSet64 -gt 100MB } | Sort-Object WorkingSet64 -Descending | Select-Object Name, WorkingSet64 -First 5
```
Cette commande :
1. Récupère tous les processus.
2. Filtre ceux utilisant plus de 100 Mo de mémoire.
3. Les trie par utilisation mémoire en ordre décroissant.
4. Sélectionne les 5 premiers processus, affichant leur nom et leur utilisation mémoire.

---

## 4. Variables, boucles et conditions
PowerShell prend en charge les constructions de script pour l'automatisation.

### Variables
```powershell
$path = "C:\Logs"
$services = Get-Service
Write-Output "Le chemin du journal est $path"
```

### Boucles
- **ForEach-Object** :
```powershell
Get-Service | ForEach-Object { Write-Output $_.Name }
```
- **Boucle For** :
```powershell
for ($i = 1; $i -le 5; $i++) { Write-Output "Itération $i" }
```

### Conditions
```powershell
$service = Get-Service -Name "wuauserv"
if ($service.Status -eq "Running") {
    Write-Output "Windows Update est en cours d'exécution."
} else {
    Write-Output "Windows Update est arrêté."
}
```

---

## 5. Gestion des erreurs
Utilisez `Try`, `Catch` et `Finally` pour des scripts robustes.
```powershell
Try {
    Get-Item -Path C:\NonExistentFile.txt -ErrorAction Stop
}
Catch {
    Write-Output "Erreur : $($_.Exception.Message)"
}
Finally {
    Write-Output "Opération terminée."
}
```

---

## 6. Gestion à distance
PowerShell prend en charge l'administration à distance en utilisant `Invoke-Command` et `Enter-PSSession`.

**Exemple** : Exécuter une commande sur un ordinateur distant.
```powershell
Invoke-Command -ComputerName Server01 -ScriptBlock { Get-Service | Where-Object { $_.Status -eq "Running" } }
```

**Exemple** : Démarrer une session interactive à distance.
```powershell
Enter-PSSession -ComputerName Server01
```

---

## 7. Exemple de script pratique
Voici un exemple de script pour surveiller l'espace disque et alerter si l'utilisation dépasse 80 %.

```powershell
$disks = Get-Disk
$threshold = 80

foreach ($disk in $disks) {
    $freeSpacePercent = ($disk.FreeSpace / $disk.Size) * 100
    if ($freeSpacePercent -lt (100 - $threshold)) {
        Write-Output "Avertissement : Le disque $($disk.Number) est à $("{0:N2}" -f (100 - $freeSpacePercent))% de capacité."
    }
}
```

---

## 8. Conseils pour une utilisation efficace de PowerShell
- **Utilisez les alias pour la rapidité** : Les alias courants comme `dir` (`Get-ChildItem`), `ls` (`Get-ChildItem`), ou `gci` (`Get-ChildItem`) font gagner du temps dans les sessions interactives.
- **Get-Help** : Utilisez `Get-Help <cmdlet>` pour une documentation détaillée (par exemple, `Get-Help Get-Process -Full`).
- **Update-Help** : Maintenez les fichiers d'aide à jour avec `Update-Help`.
- **Profils** : Personnalisez votre environnement PowerShell en modifiant `$PROFILE` (par exemple, `notepad $PROFILE`).
- **Complétion par tabulation** : Appuyez sur `Tab` pour auto-compléter les cmdlets, paramètres et chemins.
- **Utilisez la sortie verbeuse** : Ajoutez `-Verbose` aux cmdlets pour des informations d'exécution détaillées.

---

## 9. Ressources supplémentaires
- **Documentation officielle** : [Microsoft PowerShell Docs](https://docs.microsoft.com/en-us/powershell/)
- **PowerShell Gallery** : [PowerShell Gallery](https://www.powershellgallery.com/) pour les modules.
- **Communauté** : Consultez les publications sur X ou les forums comme Stack Overflow pour des astuces et scripts en temps réel.
- **Apprentissage** : Livres comme *PowerShell in Depth* ou *Learn PowerShell in a Month of Lunches*.

---

PowerShell est un langage de script puissant et un shell en ligne de commande développé par Microsoft. Il est largement utilisé pour l'automatisation des tâches et la gestion de configuration. Voici quelques commandes PowerShell couramment utilisées, outre `Get-NetTCPConnection` :

1. **Get-Process** : Récupère des informations sur les processus en cours d'exécution sur l'ordinateur local ou un ordinateur distant.

2. **Get-Service** : Obtient les services sur un ordinateur local ou distant.

3. **Get-EventLog** : Récupère les événements des journaux d'événements, y compris les journaux d'application, de sécurité et système.

4. **Get-ChildItem** : Obtient les éléments et les éléments enfants dans un ou plusieurs emplacements spécifiés (similaire à `dir` dans l'invite de commandes).

5. **Get-Content** : Obtient le contenu de l'élément à l'emplacement spécifié (similaire à `type` dans l'invite de commandes).

6. **Set-ExecutionPolicy** : Modifie la préférence de l'utilisateur pour la politique d'exécution PowerShell.

7. **Invoke-Command** : Exécute des commandes sur des ordinateurs locaux et distants.

8. **New-Item** : Crée un nouvel élément, tel qu'un fichier ou un répertoire.

9. **Remove-Item** : Supprime les éléments spécifiés.

10. **Copy-Item** : Copie un élément d'un emplacement à un autre.

11. **Move-Item** : Déplace un élément d'un emplacement à un autre.

12. **Rename-Item** : Renomme un élément dans un espace de noms de fournisseur PowerShell.

13. **Get-Help** : Affiche des informations sur les commandes et concepts PowerShell.

14. **Select-Object** : Sélectionne des propriétés spécifiées d'un objet ou d'un ensemble d'objets.

15. **Where-Object** : Sélectionne des objets d'une collection en fonction de leurs valeurs de propriété.

16. **Sort-Object** : Trie les objets par valeurs de propriété.

17. **Export-Csv** : Convertit des objets en une série de chaînes CSV et enregistre les chaînes dans un fichier.

18. **Import-Csv** : Importe un fichier CSV et le convertit en objets.

19. **Start-Process** : Démarre un ou plusieurs processus sur l'ordinateur local.

20. **Stop-Process** : Arrête un ou plusieurs processus en cours d'exécution.

Ces commandes ne sont que quelques exemples de ce que vous pouvez faire avec PowerShell. Le langage est hautement extensible, et vous pouvez créer des cmdlets et scripts personnalisés pour automatiser des tâches complexes.