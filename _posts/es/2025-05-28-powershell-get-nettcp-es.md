---
audio: false
generated: true
lang: es
layout: post
title: 'PowerShell: Uso de Get-NetTCPConnection'
translated: true
type: note
---

El cmdlet `Get-NetTCPConnection` en PowerShell recupera información sobre las conexiones TCP en un sistema Windows. Es parte del módulo `NetTCPIP`, disponible en Windows 8/Windows Server 2012 y versiones posteriores. A continuación, se presenta una guía concisa sobre cómo usarlo:

### Uso Básico
Ejecuta `Get-NetTCPConnection` para listar todas las conexiones TCP activas:

```powershell
Get-NetTCPConnection
```

Esto devuelve detalles como LocalAddress, LocalPort, RemoteAddress, RemotePort, State y OwningProcess.

### Parámetros Comunes
- **-State**: Filtrar por estado de conexión (por ejemplo, Established, Listening, TimeWait).
  ```powershell
  Get-NetTCPConnection -State Established
  ```
- **-LocalPort**: Filtrar por número de puerto local.
  ```powershell
  Get-NetTCPConnection -LocalPort 80
  ```
- **-RemoteAddress**: Filtrar por dirección IP remota.
  ```powershell
  Get-NetTCPConnection -RemoteAddress 192.168.1.1
  ```
- **-RemotePort**: Filtrar por puerto remoto.
  ```powershell
  Get-NetTCPConnection -RemotePort 443
  ```
- **-OwningProcess**: Filtrar por el ID de proceso (PID) que posee la conexión.
  ```powershell
  Get-NetTCPConnection -OwningProcess 1234
  ```

### Combinar Filtros
Puedes combinar parámetros para obtener resultados más específicos:
```powershell
Get-NetTCPConnection -State Established -LocalPort 80
```

### Mostrar Propiedades Específicas
Usa `Select-Object` para mostrar solo las propiedades deseadas:
```powershell
Get-NetTCPConnection | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State
```

### Encontrar Detalles del Proceso
Para identificar el proceso detrás de una conexión, combínalo con `Get-Process`:
```powershell
Get-NetTCPConnection -LocalPort 80 | ForEach-Object { Get-Process -Id $_.OwningProcess }
```

### Ordenar y Formatear la Salida
Ordena los resultados (por ejemplo, por LocalPort) y formatea como una tabla:
```powershell
Get-NetTCPConnection | Sort-Object LocalPort | Format-Table LocalAddress, LocalPort, RemoteAddress, RemotePort, State
```

### Ejemplos Prácticos
1. **Listar todas las conexiones en escucha:**
   ```powershell
   Get-NetTCPConnection -State Listening
   ```
2. **Encontrar conexiones a un servidor remoto específico:**
   ```powershell
   Get-NetTCPConnection -RemoteAddress "8.8.8.8"
   ```
3. **Verificar qué proceso está usando un puerto específico:**
   ```powershell
   $connection = Get-NetTCPConnection -LocalPort 8080
   Get-Process -Id $connection.OwningProcess
   ```

### Notas
- **Privilegios de Administrador**: Algunos detalles (por ejemplo, OwningProcess para procesos del sistema) pueden requerir ejecutar PowerShell como Administrador.
- **IPv4/IPv6**: El cmdlet maneja tanto conexiones IPv4 como IPv6.
- **Exportar Resultados**: Guarda la salida en un archivo con `Export-Csv`:
  ```powershell
  Get-NetTCPConnection | Export-Csv -Path "tcp_connections.csv" -NoTypeInformation
  ```

Para más detalles, ejecuta:
```powershell
Get-Help Get-NetTCPConnection -Full
```

¡Si necesitas ejemplos específicos o tienes un caso de uso particular, házmelo saber!