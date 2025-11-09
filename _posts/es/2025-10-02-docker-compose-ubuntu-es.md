---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast:free
title: Instalación de Docker Compose para Ubuntu
translated: true
type: note
---

Según la información de tu sistema, estás ejecutando **Ubuntu 24.04.2 LTS** en una arquitectura **x86_64**. Para descargar el binario de **Docker Compose** apropiado para tu sistema desde la versión de GitHub proporcionada (v2.39.4), debes seleccionar el binario compatible con Linux en x86_64.

### Descarga Recomendada
Deberías descargar el binario **docker-compose-linux-x86_64**, que no aparece explícitamente listado en los recursos proporcionados, pero se da por sentado como un binario estándar para sistemas Linux x86_64 en las versiones de Docker Compose. Sin embargo, de los recursos listados, la opción más cercana para tu sistema es:

- **docker-compose-linux-aarch64** **no** es adecuado porque es para la arquitectura ARM64 (aarch64), y tu sistema es x86_64.
- Los binarios **darwin** (ej. `docker-compose-darwin-x86_64`) son para macOS, no para Linux.
- Las opciones de código fuente (`Source code (zip)` o `Source code (tar.gz)`) requieren compilación manual, lo cual es innecesario ya que normalmente hay un binario precompilado disponible.

Dado que el binario **docker-compose-linux-x86_64** no está explícitamente listado en los recursos que proporcionaste, pero es estándar en las versiones de Docker Compose, es probable que lo encuentres en la lista completa de recursos en la página de la versión de GitHub. Si no está disponible, puedes usar el código fuente o instalar Docker Compose mediante un método alternativo (ej. el gestor de paquetes o pip).

### Pasos para Descargar e Instalar
1.  **Confirmar el Binario**: Visita la página de la versión para v2.39.4 para confirmar la disponibilidad de `docker-compose-linux-x86_64`. La página de la versión está típicamente en:
    [Docker Compose v2.39.4 Release](https://github.com/docker/compose/releases/tag/v2.39.4)

2.  **Descargar el Binario**:
    Si `docker-compose-linux-x86_64` está disponible, descárgalo. Por ejemplo:
    ```bash
    curl -L "https://github.com/docker/compose/releases/download/v2.39.4/docker-compose-linux-x86_64" -o docker-compose
    ```

3.  **Verificar la Descarga**:
    Usa la suma de comprobación proporcionada para verificar la integridad del archivo descargado. Por ejemplo, si el archivo `docker-compose-linux-x86_64.sha256` está disponible:
    ```bash
    echo "<sha256> docker-compose" | sha256sum --check
    ```
    Reemplaza `<sha256>` con el hash apropiado de los recursos de la versión (ej. `df7ff3dd8080134b851e1e49265028697d27de71f9bdc187e3d833357b934f36` para `docker-compose-darwin-x86_64.sha256`, pero necesitas el equivalente para Linux).

4.  **Instalar el Binario**:
    Mueve el binario a un directorio en tu PATH, como `/usr/local/bin`:
    ```bash
    chmod +x docker-compose
    sudo mv docker-compose /usr/local/bin/docker-compose
    ```

5.  **Verificar la Instalación**:
    Comprueba la versión instalada:
    ```bash
    docker-compose --version
    ```
    Debería mostrar `Docker Compose version v2.39.4`.

### Método de Instalación Alternativo
Si el binario `docker-compose-linux-x86_64` no está disponible o prefieres un método más simple, puedes instalar Docker Compose usando el gestor de paquetes o pip, ya que tu sistema tiene Python 3.13.4 instalado:

#### Mediante el Gestor de Paquetes (Recomendado para Ubuntu)
Docker Compose suele estar disponible en los repositorios de Ubuntu o en el repositorio oficial de Docker:
```bash
sudo apt update
sudo apt install docker-compose-plugin
```
Esto instala el plugin de Docker Compose, que es la forma moderna de usar Docker Compose (como `docker compose` en lugar de `docker-compose`). Ten en cuenta que la versión en el repositorio de Ubuntu podría no ser exactamente v2.39.4, así que compruébalo con:
```bash
docker compose version
```

#### Mediante pip (Python)
Como tienes Python 3.13.4, puedes instalar Docker Compose mediante pip:
```bash
pip3 install docker-compose==2.39.4
```
Esto instala la versión específica. Verifica con:
```bash
docker-compose --version
```

### Notas
- El archivo `checksums.txt` (SHA256: `1a9c3370b88825ab2b229bb90eda6f703d84018ea1d56b5ba573f8893c9ab6b4`) puede usarse para verificar la integridad de los archivos descargados.
- Si eliges compilar desde el código fuente (`Source code (zip)` o `Source code (tar.gz)`), necesitarás Go (no listado en la información de tu sistema) y configuración adicional, lo cual es más complejo y no se recomienda a menos que sea necesario.
- La versión incluye mejoras y correcciones (ej. soporte para `develop.watch.initial_sync`, volume ls sin un proyecto, y TLS para bake), que son relevantes si estás usando estas funciones.

Si necesitas ayuda para encontrar el binario exacto `docker-compose-linux-x86_64` o encuentras problemas, ¡házmelo saber y puedo guiarte más!

[Docker Compose v2.39.4 Release](https://github.com/docker/compose/releases/tag/v2.39.4)