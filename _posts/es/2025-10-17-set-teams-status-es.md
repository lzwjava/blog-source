---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Establecer estado de equipos mediante PowerShell
translated: true
type: note
---

No, Microsoft Teams no tiene una utilidad oficial independiente de línea de comandos (como un simple ejecutable `teams --status offline`) para establecer tu estado de presencia. Los comandos de barra diagonal integrados (por ejemplo, `/away` o `/offline`) solo funcionan dentro de la interfaz de la aplicación Teams, no desde una terminal.

Sin embargo, puedes lograr esto mediante la línea de comandos usando PowerShell y Microsoft Graph API. Esto requiere instalar el SDK de Microsoft Graph PowerShell, autenticarte con tu cuenta de Microsoft y ejecutar un cmdlet para actualizar tu presencia. Aquí tienes una guía paso a paso:

### Prerrequisitos
1. Instala PowerShell (si aún no está disponible; viene integrado en Windows 10+).
2. Abre PowerShell como administrador e instala el módulo:
   ```
   Install-Module Microsoft.Graph -Scope CurrentUser
   ```

### Establece tu Estado
1. Conéctate a Microsoft Graph (esto solicitará autenticación a través del navegador):
   ```
   Connect-MgGraph -Scopes "Presence.ReadWrite"
   ```

2. Ejecuta el cmdlet para establecer tu estado. Reemplaza `YourUserId` con tu ID de usuario de Microsoft Entra ID (Azure AD) (puedes obtenerlo mediante `Get-MgUser -UserId tu.correo@dominio.com`). Los valores de estado comunes incluyen:
   - `Available` (Disponible)
   - `Away` (Ausente)
   - `Busy` (Ocupado)
   - `DoNotDisturb` (No molestar)
   - `Offline` (Aparece como fuera de línea para otros)

   Ejemplo para establecer a fuera de línea:
   ```
   Set-MgUserPresence -UserId "YourUserId" -Presence "Offline"
   ```

   Ejemplo para establecer a ausente:
   ```
   Set-MgUserPresence -UserId "YourUserId" -Presence "Away"
   ```

3. Para desconectarte cuando termines:
   ```
   Disconnect-MgGraph
   ```

### Notas
- Esto actualiza tu presencia inmediatamente, pero puede restablecerse en función de tu actividad (por ejemplo, el tiempo de inactividad activa el estado "Ausente").
- Para automatización (por ejemplo, scripts para alternar el estado según una programación), envuelve lo anterior en un archivo `.ps1` y ejecútalo mediante el Programador de tareas.
- Si también deseas establecer un mensaje de estado personalizado (por ejemplo, "Salí a almorzar"), usa `Set-MgUserPresenceStatusMessage`.
- Esto funciona para uso personal pero requiere los permisos apropiados; los administradores podrían necesitar habilitar el acceso a Graph API.

Para mantener tu estado como "Disponible" durante períodos de inactividad (solución común), existen scripts que simulan actividad (por ejemplo, alternar Bloq Num cada pocos minutos), pero no son configuradores de estado verdaderos.

Referencias:  
[Manage Presence Status in Microsoft Teams Using MS Graph PowerShell](https://m365scripts.com/microsoft-teams/manage-presence-status-in-microsoft-teams-using-ms-graph-powershell/)  
[Set-MgUserPresence PowerShell Cmdlet Docs](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.users.actions/set-mguserpresence)  
[Reddit Thread on Teams Status via API/CLI](https://www.reddit.com/r/teams/comments/1h5wee9/teams_status_with_api_command_line/)