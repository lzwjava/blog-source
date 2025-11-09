---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Définir le statut d'équipe via PowerShell
translated: true
type: note
---

Non, Microsoft Teams ne dispose pas d'utilitaire en ligne de commande autonome officiel (comme un simple exécutable `teams --status offline`) pour définir votre statut de présence. Les commandes barre oblique intégrées (par exemple, `/away` ou `/offline`) fonctionnent uniquement dans l'interface de l'application Teams, pas depuis un terminal.

Cependant, vous pouvez y parvenir en ligne de commande en utilisant PowerShell et l'API Microsoft Graph. Cela nécessite d'installer le SDK Microsoft Graph PowerShell, de s'authentifier avec votre compte Microsoft et d'exécuter une cmdlet pour mettre à jour votre présence. Voici un guide étape par étape :

### Prérequis
1. Installez PowerShell (s'il n'est pas déjà disponible ; il est intégré à Windows 10+).
2. Ouvrez PowerShell en tant qu'administrateur et installez le module :
   ```
   Install-Module Microsoft.Graph -Scope CurrentUser
   ```

### Définir votre statut
1. Connectez-vous à Microsoft Graph (cela demandera une authentification via le navigateur) :
   ```
   Connect-MgGraph -Scopes "Presence.ReadWrite"
   ```

2. Exécutez la cmdlet pour définir votre statut. Remplacez `YourUserId` par votre ID d'utilisateur Microsoft Entra ID (Azure AD) (vous pouvez l'obtenir via `Get-MgUser -UserId your.email@domain.com`). Les valeurs de statut courantes incluent :
   - `Available` (Disponible)
   - `Away` (Absent)
   - `Busy` (Occupé)
   - `DoNotDisturb` (Ne pas déranger)
   - `Offline` (Apparaît comme hors ligne pour les autres)

   Exemple pour se mettre hors ligne :
   ```
   Set-MgUserPresence -UserId "YourUserId" -Presence "Offline"
   ```

   Exemple pour se mettre absent :
   ```
   Set-MgUserPresence -UserId "YourUserId" -Presence "Away"
   ```

3. Pour vous déconnecter une fois terminé :
   ```
   Disconnect-MgGraph
   ```

### Notes
- Cela met à jour votre présence immédiatement, mais elle peut se réinitialiser en fonction de votre activité (par exemple, le temps d'inactivité déclenche le statut "Absent").
- Pour l'automatisation (par exemple, des scripts pour basculer le statut selon un planning), intégrez les commandes ci-dessus dans un fichier `.ps1` et exécutez-le via le Planificateur de tâches.
- Si vous souhaitez également définir un message de statut personnalisé (par exemple, "En pause déjeuner"), utilisez `Set-MgUserPresenceStatusMessage`.
- Cela fonctionne pour un usage personnel mais nécessite des autorisations appropriées ; les administrateurs devront peut-être activer l'accès à l'API Graph.

Pour maintenir votre statut "Disponible" pendant les périodes d'inactivité (solution de contournement courante), il existe des scripts qui simulent une activité (par exemple, basculer Verr Num toutes les quelques minutes), mais ce ne sont pas de véritables outils de définition de statut.

Références :  
[Manage Presence Status in Microsoft Teams Using MS Graph PowerShell](https://m365scripts.com/microsoft-teams/manage-presence-status-in-microsoft-teams-using-ms-graph-powershell/)  
[Set-MgUserPresence PowerShell Cmdlet Docs](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.users.actions/set-mguserpresence)  
[Reddit Thread on Teams Status via API/CLI](https://www.reddit.com/r/teams/comments/1h5wee9/teams_status_with_api_command_line/)