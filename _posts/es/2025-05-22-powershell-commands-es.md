---
audio: false
generated: true
lang: es
layout: post
title: Guía de Comandos de PowerShell
translated: true
type: note
---

## Introducción a PowerShell
PowerShell es un framework de automatización de tareas y gestión de configuración de Microsoft, que consiste en un shell de línea de comandos y un lenguaje de scripting. Está construido sobre .NET Framework (y .NET Core en versiones más recientes), permitiendo a los administradores realizar tareas complejas en sistemas Windows, Linux y macOS.

Los comandos de PowerShell, conocidos como **cmdlets** (pronunciado "command-lets"), siguen una convención de nomenclatura `Verbo-Sustantivo` (por ejemplo, `Get-Process`, `Set-Item`). Esta guía cubre cmdlets esenciales, categorizados por funcionalidad, con ejemplos para demostrar su uso.

---

## 1. Conceptos Básicos de PowerShell
Antes de profundizar en los comandos, es crucial entender conceptos clave:
- **Cmdlets**: Comandos ligeros que realizan funciones específicas.
- **Pipelines (Tuberías)**: Permiten que la salida de un cmdlet se pase como entrada a otro usando el operador `|`.
- **Módulos**: Colecciones de cmdlets, scripts y funciones que extienden la funcionalidad de PowerShell.
- **Proveedores**: Interfaces para acceder a almacenes de datos (por ejemplo, sistema de archivos, registro) como si fueran unidades.
- **Objetos**: PowerShell trabaja con objetos, no con texto plano, permitiendo la manipulación de datos estructurados.

---

## 2. Cmdlets Esenciales por Categoría

### 2.1 Información del Sistema
Estos cmdlets recuperan información sobre el sistema, procesos y servicios.

| Cmdlet | Descripción | Ejemplo |
|--------|-------------|---------|
| `Get-ComputerInfo` | Recupera detalles del hardware y software del sistema. | `Get-ComputerInfo | Select-Object WindowsProductName, OsVersion` |
| `Get-Process` | Enumera los procesos en ejecución. | `Get-Process | Where-Object {$_.CPU -gt 1000}` |
| `Get-Service` | Muestra los servicios en el sistema. | `Get-Service | Where-Object {$_.Status -eq "Running"}` |
| `Get-HotFix` | Enumera las actualizaciones de Windows instaladas. | `Get-HotFix | Sort-Object InstalledOn -Descending` |

**Ejemplo**: Listar todos los procesos en ejecución ordenados por uso de CPU.
```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object Name, CPU, Id -First 5
```

### 2.2 Gestión de Archivos y Directorios
PowerShell trata el sistema de archivos como un proveedor, permitiendo una navegación similar a una unidad.

| Cmdlet | Descripción | Ejemplo |
|--------|-------------|---------|
| `Get-Item` | Recupera archivos o directorios. | `Get-Item C:\Users\*.txt` |
| `Set-Item` | Modifica las propiedades de un elemento (por ejemplo, atributos de archivo). | `Set-Item -Path C:\test.txt -Value "Nuevo contenido"` |
| `New-Item` | Crea un nuevo archivo o directorio. | `New-Item -Path C:\Docs -Name Report.txt -ItemType File` |
| `Remove-Item` | Elimina archivos o directorios. | `Remove-Item C:\Docs\OldFile.txt` |
| `Copy-Item` | Copia archivos o directorios. | `Copy-Item C:\Docs\Report.txt D:\Backup` |
| `Move-Item` | Mueve archivos o directorios. | `Move-Item C:\Docs\Report.txt C:\Archive` |

**Ejemplo**: Crear un directorio y un archivo, luego copiarlo a otra ubicación.
```powershell
New-Item -Path C:\Temp -Name MyFolder -ItemType Directory
New-Item -Path C:\Temp\MyFolder -Name Test.txt -ItemType File
Copy-Item C:\Temp\MyFolder\Test.txt C:\Backup
```

### 2.3 Gestión del Sistema
Cmdlets para gestionar configuraciones del sistema, servicios y usuarios.

| Cmdlet | Descripción | Ejemplo |
|--------|-------------|---------|
| `Start-Service` | Inicia un servicio. | `Start-Service -Name "wuauserv"` |
| `Stop-Service` | Detiene un servicio. | `Stop-Service -Name "wuauserv"` |
| `Restart-Computer` | Reinicia el sistema. | `Restart-Computer -Force` |
| `Get-EventLog` | Recupera entradas del registro de eventos. | `Get-EventLog -LogName System -Newest 10` |
| `Set-ExecutionPolicy` | Establece la política de ejecución de scripts. | `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` |

**Ejemplo**: Verificar el estado del servicio Windows Update e iniciarlo si está detenido.
```powershell
$service = Get-Service -Name "wuauserv"
if ($service.Status -eq "Stopped") {
    Start-Service -Name "wuauserv"
}
```

### 2.4 Gestión de Red
Cmdlets para configuración y diagnóstico de red.

| Cmdlet | Descripción | Ejemplo |
|--------|-------------|---------|
| `Test-Connection` | Hace ping a un host remoto. | `Test-Connection google.com` |
| `Get-NetAdapter` | Enumera los adaptadores de red. | `Get-NetAdapter | Select-Object Name, Status` |
| `Get-NetIPAddress` | Recupera las configuraciones de direcciones IP. | `Get-NetIPAddress -AddressFamily IPv4` |
| `Resolve-DnsName` | Resuelve nombres DNS. | `Resolve-DnsName www.google.com` |

**Ejemplo**: Hacer ping a un servidor y verificar su resolución DNS.
```powershell
Test-Connection -ComputerName google.com -Count 2
Resolve-DnsName google.com
```

### 2.5 Gestión de Usuarios y Grupos
Cmdlets para gestionar usuarios y grupos locales.

| Cmdlet | Descripción | Ejemplo |
|--------|-------------|---------|
| `New-LocalUser` | Crea una cuenta de usuario local. | `New-LocalUser -Name "TestUser" -Password (ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force)` |
| `Remove-LocalUser` | Elimina una cuenta de usuario local. | `Remove-LocalUser -Name "TestUser"` |
| `Get-LocalGroup` | Enumera los grupos locales. | `Get-LocalGroup | Select-Object Name` |
| `Add-LocalGroupMember` | Agrega un usuario a un grupo local. | `Add-LocalGroupMember -Group "Administrators" -Member "TestUser"` |

**Ejemplo**: Crear un nuevo usuario local y agregarlo al grupo Administradores.
```powershell
$password = ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force
New-LocalUser -Name "TestUser" -Password $password -FullName "Test User" -Description "Cuenta de prueba"
Add-LocalGroupMember -Group "Administrators" -Member "TestUser"
```

### 2.6 Scripting y Automatización
PowerShell sobresale en scripting para automatización.

| Cmdlet | Descripción | Ejemplo |
|--------|-------------|---------|
| `Write-Output` | Envía datos a la tubería. | `Write-Output "¡Hola, Mundo!"` |
| `ForEach-Object` | Itera a través de los elementos en una tubería. | `Get-Process | ForEach-Object { $_.Name }` |
| `Where-Object` | Filtra objetos basándose en condiciones. | `Get-Service | Where-Object { $_.Status -eq "Running" }` |
| `Invoke-Command` | Ejecuta comandos en computadoras locales o remotas. | `Invoke-Command -ComputerName Server01 -ScriptBlock { Get-Process }` |
| `New-ScheduledTask` | Crea una tarea programada. | `New-ScheduledTask -Action (New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-File C:\script.ps1") -Trigger (New-ScheduledTaskTrigger -Daily -At "3AM")` |

**Ejemplo**: Crear un script para registrar los procesos en ejecución en un archivo.
```powershell
$logPath = "C:\Logs\ProcessLog.txt"
Get-Process | Select-Object Name, CPU, StartTime | Export-Csv -Path $logPath -NoTypeInformation
```

### 2.7 Gestión de Módulos
Los módulos extienden la funcionalidad de PowerShell.

| Cmdlet | Descripción | Ejemplo |
|--------|-------------|---------|
| `Get-Module` | Enumera los módulos disponibles o importados. | `Get-Module -ListAvailable` |
| `Import-Module` | Importa un módulo. | `Import-Module ActiveDirectory` |
| `Install-Module` | Instala un módulo desde un repositorio. | `Install-Module -Name PSWindowsUpdate -Force` |
| `Find-Module` | Busca módulos en un repositorio. | `Find-Module -Name *Azure*` |

**Ejemplo**: Instalar e importar el módulo PSWindowsUpdate para gestionar actualizaciones de Windows.
```powershell
Install-Module -Name PSWindowsUpdate -Force
Import-Module PSWindowsUpdate
Get-WUList
```

---

## 3. Trabajando con Tuberías (Pipelines)
La tubería (`|`) permite encadenar cmdlets para procesar datos secuencialmente. Por ejemplo:
```powershell
Get-Process | Where-Object { $_.WorkingSet64 -gt 100MB } | Sort-Object WorkingSet64 -Descending | Select-Object Name, WorkingSet64 -First 5
```
Este comando:
1. Recupera todos los procesos.
2. Filtra aquellos que usan más de 100MB de memoria.
3. Los ordena por uso de memoria en orden descendente.
4. Selecciona los 5 procesos principales, mostrando su nombre y uso de memoria.

---

## 4. Variables, Bucles y Condiciones
PowerShell soporta construcciones de scripting para automatización.

### Variables
```powershell
$path = "C:\Logs"
$services = Get-Service
Write-Output "La ruta del log es $path"
```

### Bucles
- **ForEach-Object**:
```powershell
Get-Service | ForEach-Object { Write-Output $_.Name }
```
- **Bucle For**:
```powershell
for ($i = 1; $i -le 5; $i++) { Write-Output "Iteración $i" }
```

### Condiciones
```powershell
$service = Get-Service -Name "wuauserv"
if ($service.Status -eq "Running") {
    Write-Output "Windows Update se está ejecutando."
} else {
    Write-Output "Windows Update está detenido."
}
```

---

## 5. Manejo de Errores
Usa `Try`, `Catch` y `Finally` para scripts robustos.
```powershell
Try {
    Get-Item -Path C:\NonExistentFile.txt -ErrorAction Stop
}
Catch {
    Write-Output "Error: $($_.Exception.Message)"
}
Finally {
    Write-Output "Operación completada."
}
```

---

## 6. Gestión Remota
PowerShell soporta administración remota usando `Invoke-Command` y `Enter-PSSession`.

**Ejemplo**: Ejecutar un comando en un equipo remoto.
```powershell
Invoke-Command -ComputerName Server01 -ScriptBlock { Get-Service | Where-Object { $_.Status -eq "Running" } }
```

**Ejemplo**: Iniciar una sesión remota interactiva.
```powershell
Enter-PSSession -ComputerName Server01
```

---

## 7. Ejemplo de Script Práctico
A continuación se muestra un script de ejemplo para monitorear el espacio en disco y alertar si el uso supera el 80%.

```powershell
$disks = Get-Disk
$threshold = 80

foreach ($disk in $disks) {
    $freeSpacePercent = ($disk.FreeSpace / $disk.Size) * 100
    if ($freeSpacePercent -lt (100 - $threshold)) {
        Write-Output "Advertencia: El disco $($disk.Number) está al $("{0:N2}" -f (100 - $freeSpacePercent))% de su capacidad."
    }
}
```

---

## 8. Consejos para un Uso Efectivo de PowerShell
- **Usa Alias para Mayor Velocidad**: Alias comunes como `dir` (`Get-ChildItem`), `ls` (`Get-ChildItem`) o `gci` (`Get-ChildItem`) ahorran tiempo en sesiones interactivas.
- **Get-Help**: Usa `Get-Help <cmdlet>` para documentación detallada (por ejemplo, `Get-Help Get-Process -Full`).
- **Update-Help**: Mantén los archivos de ayuda actualizados con `Update-Help`.
- **Perfiles**: Personaliza tu entorno de PowerShell editando `$PROFILE` (por ejemplo, `notepad $PROFILE`).
- **Autocompletado con Tab**: Presiona `Tab` para autocompletar cmdlets, parámetros y rutas.
- **Usa Salida Detallada**: Agrega `-Verbose` a los cmdlets para información detallada de ejecución.

---

## 9. Recursos Adicionales
- **Documentación Oficial**: [Microsoft PowerShell Docs](https://docs.microsoft.com/en-us/powershell/)
- **PowerShell Gallery**: [PowerShell Gallery](https://www.powershellgallery.com/) para módulos.
- **Comunidad**: Consulta publicaciones en X o foros como Stack Overflow para consejos y scripts en tiempo real.
- **Aprendizaje**: Libros como *PowerShell in Depth* o *Learn PowerShell in a Month of Lunches*.

---

PowerShell es un lenguaje de scripting y shell de línea de comandos potente desarrollado por Microsoft. Es ampliamente utilizado para la automatización de tareas y la gestión de configuración. Aquí hay algunos comandos de PowerShell comúnmente utilizados además de `Get-NetTCPConnection`:

1.  **Get-Process**: Recupera información sobre los procesos que se ejecutan en el equipo local o en un equipo remoto.
2.  **Get-Service**: Obtiene los servicios en un equipo local o remoto.
3.  **Get-EventLog**: Recupera eventos de los registros de eventos, incluidos los registros de aplicaciones, seguridad y sistema.
4.  **Get-ChildItem**: Obtiene los elementos y los elementos secundarios en una o más ubicaciones especificadas (similar a `dir` en el Símbolo del sistema).
5.  **Get-Content**: Obtiene el contenido del elemento en la ubicación especificada (similar a `type` en el Símbolo del sistema).
6.  **Set-ExecutionPolicy**: Cambia la preferencia del usuario para la política de ejecución de PowerShell.
7.  **Invoke-Command**: Ejecuta comandos en equipos locales y remotos.
8.  **New-Item**: Crea un nuevo elemento, como un archivo o directorio.
9.  **Remove-Item**: Elimina los elementos especificados.
10. **Copy-Item**: Copia un elemento de una ubicación a otra.
11. **Move-Item**: Mueve un elemento de una ubicación a otra.
12. **Rename-Item**: Cambia el nombre de un elemento en un espacio de nombres del proveedor de PowerShell.
13. **Get-Help**: Muestra información sobre comandos y conceptos de PowerShell.
14. **Select-Object**: Selecciona propiedades específicas de un objeto o conjunto de objetos.
15. **Where-Object**: Selecciona objetos de una colección basándose en sus valores de propiedad.
16. **Sort-Object**: Ordena objetos por valores de propiedad.
17. **Export-Csv**: Convierte objetos en una serie de cadenas CSV y guarda las cadenas en un archivo.
18. **Import-Csv**: Importa un archivo CSV y lo convierte en objetos.
19. **Start-Process**: Inicia uno o más procesos en el equipo local.
20. **Stop-Process**: Detiene uno o más procesos en ejecución.

Estos comandos son solo algunos ejemplos de lo que puedes hacer con PowerShell. El lenguaje es altamente extensible, y puedes crear cmdlets y scripts personalizados para automatizar tareas complejas.