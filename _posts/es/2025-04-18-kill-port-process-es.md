---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Matar Proceso en Puerto con Psutil
translated: true
type: note
---

### Usar psutil para Detectar y Terminar un Proceso en un Puerto Específico (Windows)

Psutil es una biblioteca de Python multiplataforma para obtener información sobre procesos en ejecución y utilización del sistema. Puedes usarla para encontrar procesos que estén escuchando en un puerto específico (por ejemplo, identificar si algo como un servidor de desarrollo de npm se está ejecutando en ese puerto) y luego terminar el proceso. Esto funciona en Windows, pero ten en cuenta:

- **Permisos**: En Windows, terminar procesos a menudo requiere privilegios de administrador (ejecuta tu script de Python como administrador). Si no lo haces, puede generar una excepción `AccessDenied`.
- **Detección de Puerto**: Nos centraremos en conexiones TCP con el tipo "inet" (que cubre IPv4 e IPv6). Esto es común para servidores web como los iniciados por `npm run dev` o similares.
- **Suposiciones**: Suponemos que quieres comprobar un puerto en escucha (servidor) (por ejemplo, algo vinculado localmente). Si te refieres a conexiones salientes a un puerto, el enfoque es ligeramente diferente—avísame si necesitas aclaración.

#### Paso 1: Instalar psutil
Si aún no lo tienes:
```bash
pip install psutil
```

#### Paso 2: Código de Ejemplo para Detectar y Terminar
Aquí hay un script completo de Python. Define una función para encontrar el PID del proceso que escucha en un puerto dado (usando `kind='inet'` como especificaste), luego lo termina. En Windows, `terminate()` es preferible sobre `kill()` ya que permite un cierre ordenado (equivalente a SIGTERM en Unix).

```python
import psutil
import time  # Para un retraso opcional

def get_pid_listening_on_port(port, kind='inet'):
    """
    Escanea las conexiones de red en busca de procesos que escuchan en el puerto especificado.
    Devuelve una lista de PIDs (normalmente uno, pero podrían ser varios en casos raros).
    """
    pids = []
    for conn in psutil.net_connections(kind=kind):
        # Comprueba si es una conexión en escucha (status='LISTEN') y el puerto de la dirección local coincide
        if conn.status == 'LISTEN' and conn.laddr and conn.laddr.port == port:
            if conn.pid:
                pids.append(conn.pid)
    return pids

def kill_process_on_port(port, kind='inet'):
    """
    Encuentra y termina el proceso que escucha en el puerto especificado.
    Si hay múltiples procesos, los termina a todos (con una advertencia).
    """
    pids = get_pid_listening_on_port(port, kind)
    if not pids:
        print(f"No se encontró ningún proceso escuchando en el puerto {port}.")
        return
    
    for pid in pids:
        try:
            proc = psutil.Process(pid)
            print(f"Terminando el proceso {proc.name()} (PID {pid}) en el puerto {port}...")
            # Usa terminate() para un cierre ordenado; envía una señal similar a SIGTERM
            proc.terminate()
            # Opcional: Espera un poco y fuerza la terminación si no sale
            gone, still_alive = psutil.wait_procs([proc], timeout=3)
            if still_alive:
                print(f"Forzando la terminación del PID {pid}...")
                still_alive[0].kill()
        except psutil.AccessDenied:
            print(f"Acceso denegado: No se puede terminar el PID {pid}. ¿Ejecutar como administrador?")
        except psutil.NoSuchProcess:
            print(f"El proceso {pid} ya no existe.")

# Ejemplo de uso: Reemplaza 3000 con tu puerto objetivo (por ejemplo, los servidores de desarrollo de npm suelen usar 3000)
if __name__ == "__main__":
    kill_process_on_port(3000)  # Ajusta kind si es necesario (por ejemplo, 'inet4' solo para IPv4)
```

#### Explicaciones Clave
- **`psutil.net_connections(kind='inet')`**: Esto recupera las conexiones de red del tipo 'inet' (que abarca IPv4 e IPv6). Cada conexión es una namedtuple con campos como:
  - `laddr`: Dirección local (por ejemplo, ('0.0.0.0', 8080) – IP y puerto).
  - `status`: 'LISTEN' para servidores que esperan conexiones.
  - `pid`: ID del proceso propietario.
  - Filtramos por `status == 'LISTEN'` para encontrar servidores (como el puerto de desarrollo de npm), no conexiones de cliente.
- **Obtención del PID**: El script obtiene directamente el PID de la tupla de conexión. Si solo quieres detectar sin terminar, usa `get_pid_listening_on_port(port)` que devuelve el/los PID(s).
- **Terminar el Proceso**:
  - `psutil.Process(pid).terminate()`: Envía una señal de terminación. En Windows, esto es como CTRL+C.
  - Si no sale, opcionalmente forzamos la terminación con `kill()` (equivalente a SIGKILL).
  - `wait_procs()` de Psutil espera a que el proceso muera.
- **Especificidad del Tipo 'inet'**: 'inet' incluye tanto IPv4 como IPv6. Si sabes que es IPv4, cambia a `kind='inet4'`. ESTENOMBRE aborda tu solicitud de "tipo inet" directamente.
- **Notas Específicas de Windows**:
  - Psutil maneja bien los internos de Windows, pero la información de red puede requerir privilegios elevados en algunos casos.
  - Para puertos por debajo de 1024 (privilegiados), solo los servicios del sistema pueden vincularse, pero la detección aún debería funcionar.
- **Manejo de Errores**: Se añadieron comprobaciones básicas para cuando no hay proceso o hay problemas de acceso.
- **Pruebas**: Ejecuta algo como `npm run dev` para ocupar el puerto 3000, luego ejecuta este script.

Si esto no coincide exactamente con tu necesidad (por ejemplo, si "npm run port" significa algo diferente o quieres detectar conexiones que no estén en escucha), ¡proporciona más detalles para refinar! Por seguridad, asegúrate de que solo estás terminando los procesos deseados.