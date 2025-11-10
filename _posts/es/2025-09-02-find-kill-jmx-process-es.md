---
audio: false
generated: true
image: false
lang: es
layout: post
title: Buscar y Matar el Proceso del Puerto JMX
translated: true
type: note
---

Entendido — quieres verificar qué programa Java en Windows ha abierto un **agente remoto JMX** en el puerto `9091`, y luego terminarlo si es necesario. Aquí te explico cómo hacerlo paso a paso:

---

### 1. Encontrar el Proceso que Usa el Puerto 9091

Abre el **Símbolo del sistema** (como Administrador si es posible) y ejecuta:

```cmd
netstat -ano | findstr :9091
```

Esto mostrará algo como:

```
  TCP    0.0.0.0:9091    0.0.0.0:0    LISTENING    12345
```

* La última columna (`12345` aquí) es el **PID (Identificador de Proceso)**.

---

### 2. Identificar a Qué Programa Pertenece ese PID

Ahora asigna el PID al programa real:

```cmd
tasklist /FI "PID eq 12345"
```

Esto mostrará algo como:

```
Image Name                     PID   Session Name        Mem Usage
========================= ======== ================ ============
java.exe                    12345 Console           200,000 K
```

Si es un proceso de Java, puedes obtener aún más detalle:

```cmd
wmic process where processid=12345 get CommandLine
```

Eso imprime la **línea de comandos** usada para iniciar la JVM — verás las banderas JMX (`-Dcom.sun.management.jmxremote.port=9091`), lo que confirma que es el agente remoto JMX.

---

### 3. Terminar el Proceso

Si has confirmado que es seguro detenerlo, puedes terminarlo:

```cmd
taskkill /PID 12345 /F
```

* `/PID` especifica el identificador del proceso.
* `/F` fuerza la terminación.

---

### 4. Alternativa con PowerShell

Si prefieres PowerShell, puedes ejecutar:

```powershell
Get-Process -Id (Get-NetTCPConnection -LocalPort 9091).OwningProcess
```

Para terminar directamente:

```powershell
Stop-Process -Id (Get-NetTCPConnection -LocalPort 9091).OwningProcess -Force
```

---

🔎 Resumen:

1. `netstat -ano | findstr :9091` → obtener el PID
2. `tasklist /FI "PID eq <PID>"` → ver qué programa es
3. `wmic process where processid=<PID> get CommandLine` → ver las banderas de la JVM
4. `taskkill /PID <PID> /F` → terminar

---

¿Quieres que también te muestre cómo **verificar múltiples JVMs a la vez** en busca de puertos de agentes JMX (para que puedas ver si hay otros ejecutándose en puertos como 9090, 9999, etc.)?