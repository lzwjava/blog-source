---
audio: false
generated: true
lang: es
layout: post
title: Problema con la API de Hetzner
translated: true
type: note
---

Analicemos el error que estás encontrando y expliquemos qué está sucediendo con tu código:

### Error:
```
Error creating snapshot for server sg5: cannot perform operation because server is locked (locked, f21b9dc9d1535310)
```

Este error proviene de la API de Hetzner Cloud (a través del SDK de Python `hcloud`) e indica que la operación para crear un snapshot del servidor llamado `sg5` falló porque el servidor está **bloqueado**. Un servidor bloqueado significa que otra operación (por ejemplo, un snapshot anterior, un reinicio o un cambio de tamaño) está actualmente en progreso, y el servidor está temporalmente restringido para aceptar nuevas operaciones hasta que ese proceso se complete.

### Desglose del Código:
Aquí está tu script con explicaciones y dónde se origina el error:

```python
from hcloud import Client
import os

# Obtener el token de API de la variable de entorno
api_token = os.environ.get('HERTZNER_API_KEY')

if not api_token:
    print("Error: HERTZNER_API_KEY environment variable not set.")
    exit(1)

# Crear una instancia del cliente
client = Client(token=api_token)

def create_snapshot(server):
    try:
        response = client.servers.create_image(server, description=f"{server.name}-snapshot", type="snapshot")
        print(f"Snapshot created for server {server.name} with ID: {response.image.id}")
    except Exception as e:
        print(f"Error creating snapshot for server {server.name}: {e}")

# Listar todos los servidores
servers = client.servers.get_all()

# Imprimir detalles del servidor y crear snapshots
for server in servers:
    print(f"Server ID: {server.id}")
    print(f"Server Name: {server.name}")
    print(f"Server Status: {server.status}")
    print(f"Server IPv4: {server.public_net.ipv4.ip}")
    print(f"Server IPv6: {server.public_net.ipv6.ip}")
    print(f"Server Type: {server.server_type.name}")
    print(f"Server Location: {server.datacenter.location.name}")
    print("----------------------------------")
    create_snapshot(server)
```

1. **Configuración del Token de API**:
   - El script recupera la clave API de Hetzner de una variable de entorno (`HERTZNER_API_KEY`). Si no está configurada, sale con un error.

2. **Inicialización del Cliente**:
   - Se crea una instancia de `Client` usando el token API para interactuar con la API de Hetzner Cloud.

3. **Función `create_snapshot`**:
   - Esta función intenta crear un snapshot de un servidor dado usando `client.servers.create_image()`.
   - Parámetros:
     - `server`: El objeto servidor del cual hacer el snapshot.
     - `description`: Un nombre para el snapshot (ej., `sg5-snapshot`).
     - `type="snapshot"`: Especifica que el tipo de imagen es un snapshot (a diferencia de un backup o ISO).
   - Si tiene éxito, imprime el ID del snapshot; de lo contrario, captura e imprime cualquier excepción (como la que estás viendo).

4. **Listado de Servidores**:
   - `client.servers.get_all()` recupera una lista de todos los servidores asociados con tu cuenta de Hetzner.
   - El script itera a través de ellos, imprime sus detalles (ID, nombre, estado, IPs, etc.) y llama a `create_snapshot()` para cada uno.

5. **Dónde Ocurre el Error**:
   - Dentro de la función `create_snapshot()`, la llamada `client.servers.create_image()` falla para el servidor `sg5` porque está bloqueado. El mensaje de excepción (`cannot perform operation because server is locked`) es generado por la librería `hcloud` basándose en la respuesta de la API.

### ¿Por Qué Está Bloqueado el Servidor?
Un servidor se bloquea cuando una operación ya está en progreso. Las razones comunes incluyen:
- Se está creando otro snapshot.
- El servidor se está reiniciando, cambiando de tamaño o reconstruyendo.
- Una operación anterior no se ha completado todavía.

El ID de bloqueo (`f21b9dc9d1535310`) en el mensaje de error es un identificador único para la acción en curso que está bloqueando el servidor.

### Cómo Solucionarlo:
Aquí hay pasos para resolver el problema y mejorar tu script:

#### 1. **Verificar el Estado de Bloqueo Antes de Proceder**
Modifica el script para omitir la creación del snapshot si el servidor está bloqueado. Puedes verificar las acciones actuales del servidor usando `client.actions.get_all()` o esperar a que se despeje el bloqueo.

Función `create_snapshot` actualizada:
```python
def create_snapshot(server):
    try:
        # Verificar si el servidor está bloqueado mirando sus acciones
        actions = client.actions.get_all(server=server)
        for action in actions:
            if action.status == "running":
                print(f"Skipping snapshot for {server.name}: Server is locked by action {action.id}")
                return
        # Si no hay acciones en ejecución, proceder con el snapshot
        response = client.servers.create_image(server, description=f"{server.name}-snapshot", type="snapshot")
        print(f"Snapshot created for server {server.name} with ID: {response.image.id}")
    except Exception as e:
        print(f"Error creating snapshot for server {server.name}: {e}")
```

#### 2. **Esperar a que se Despeje el Bloqueo**
Si prefieres esperar en lugar de omitir, puedes sondear las acciones del servidor hasta que desaparezca el bloqueo:
```python
import time

def wait_for_unlock(server):
    while True:
        actions = client.actions.get_all(server=server)
        running = any(action.status == "running" for action in actions)
        if not running:
            break
        print(f"Waiting for server {server.name} to unlock...")
        time.sleep(5)  # Esperar 5 segundos antes de verificar nuevamente

def create_snapshot(server):
    try:
        wait_for_unlock(server)
        response = client.servers.create_image(server, description=f"{server.name}-snapshot", type="snapshot")
        print(f"Snapshot created for server {server.name} with ID: {response.image.id}")
    except Exception as e:
        print(f"Error creating snapshot for server {server.name}: {e}")
```

#### 3. **Investigar el Bloqueo Manualmente**
- Usa la Consola de Hetzner Cloud o la API para verificar el estado de la acción con ID `f21b9dc9d1535310`.
- Ejemplo de llamada API (vía Python):
  ```python
  action = client.actions.get_by_id("f21b9dc9d1535310")
  print(f"Action Status: {action.status}, Command: {action.command}")
  ```
- Si está atascada, es posible que necesites contactar al soporte de Hetzner.

#### 4. **Ejecutar el Script Nuevamente**
Una vez que el servidor ya no esté bloqueado (la acción se complete o la resuelvas manualmente), vuelve a ejecutar el script.

### Notas Adicionales:
- **Límites de Tasa**: Crear snapshots para muchos servidores en un bucle podría alcanzar los límites de tasa de la API de Hetzner. Agrega un retraso (ej., `time.sleep(1)`) entre las solicitudes si es necesario.
- **Manejo de Errores**: El script actual se detiene en el primer error. Si quieres que continúe para otros servidores, asegúrate de que la excepción no detenga el bucle (en tu caso no lo hace, lo cual es bueno).

¡Avísame si necesitas ayuda implementando alguna de estas soluciones o para depurar más a fondo!