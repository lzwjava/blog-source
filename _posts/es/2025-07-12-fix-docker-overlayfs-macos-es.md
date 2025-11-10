---
audio: false
generated: true
image: false
lang: es
layout: post
model: google/gemini-2.5-flash
title: Corrección de Corrupción de OverlayFS en Docker para macOS
translated: true
type: note
---

El error que estás viendo, `driver "overlay2" failed to remove root filesystem: readdirnames /var/lib/docker/overlay2/.../merged: readdirent merged: bad message`, indica una corrupción profunda dentro del mecanismo de almacenamiento de Docker (OverlayFS) que a menudo es causada por una operación interrumpida o un problema del sistema de archivos de la máquina host.

Como estás en **macOS** (que ejecuta Docker Desktop), el daemon de Docker y su almacenamiento se gestionan dentro de una **Máquina Virtual (VM) Linux** dedicada. No tienes acceso directo a `/var/lib/docker/overlay2` como lo tendrías en Linux nativo, lo que hace que la solución sea más simple y segura al centrarse en la propia aplicación Docker Desktop.

Aquí tienes la secuencia de pasos más segura y efectiva para resolver esto en macOS:

-----

## 1. Forzar la Detención y Eliminación del Contenedor

El contenedor que falló es `chat-mongodb` (ID: `ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18`). Primero, intenta una eliminación forzada usando su nombre o ID.

1.  **Detén todo el stack** (para asegurar que ningún proceso en segundo plano esté bloqueando un recurso):

    ```bash
    docker compose stop
    ```

2.  **Fuerza la eliminación del contenedor específico** usando la bandera `-f`:

    ```bash
    docker rm -f chat-mongodb
    # O usando el ID:
    # docker rm -f ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18
    ```

3.  **Intenta ejecutar tu comando original nuevamente** (`docker compose down` o equivalente). Si el error persiste, pasa al paso 2.

-----

## 2. Reiniciar Docker Desktop

Un simple reinicio a menudo soluciona problemas transitorios de bloqueo o estados corruptos dentro de la VM interna.

### Opción A: Usando la Barra de Menús (Recomendado)

1.  Haz clic en el **icono de la ballena de Docker** en la barra de menús de tu macOS.
2.  Selecciona **Restart**.

### Opción B: Usando la Terminal

Puedes forzar el cierre y reabrir la aplicación:

```bash
killall Docker && open /Applications/Docker.app
```

Después de que Docker se reinicie, espera unos 30 segundos para que se inicie completamente, luego intenta ejecutar tu comando original nuevamente.

-----

## 3. Limpiar la Caché y los Datos No Utilizados de Docker (Prune)

Si el reinicio falla, un comando de limpieza profunda a menudo puede resolver problemas de corrupción más graves al eliminar componentes no utilizados o "huérfanos" que podrían estar relacionados con el error.

**ADVERTENCIA:** Este comando elimina todos los contenedores detenidos, redes no utilizadas e imágenes huérfanas. Si tienes contenedores detenidos que quieres conservar (pero no eliminar), haz una copia de seguridad de ellos o omite este paso.

Ejecuta el siguiente comando en tu terminal:

```bash
docker system prune -a --volumes
```

  * **`-a`** (all) elimina todas las imágenes no utilizadas (no solo las huérfanas).
  * **`--volumes`** elimina los volúmenes anónimos no utilizados (que podrían ser la fuente de la corrupción de `overlay2`).

Se te pedirá que confirmes. Escribe `y` y presiona Enter. Después de que la limpieza termine, intenta ejecutar tu comando original nuevamente.

-----

## 4. Restablecer Docker Desktop de Fábrica

Este es el **último recurso**, ya que **eliminará todos tus contenedores, imágenes y volúmenes** (incluidos cualquier dato local que hayas almacenado en volúmenes no montados). Fuerza un reinicio completo de la VM interna de Docker.

1.  Haz clic en el **icono de la ballena de Docker** en la barra de menús de tu macOS.
2.  Ve a **Settings (o Preferences)** $\rightarrow$ **Troubleshoot**.
3.  Haz clic en **Reset to factory settings...**

Después del restablecimiento, Docker se reiniciará desde cero, y deberías poder ejecutar tu comando `docker compose up` para reconstruir tu entorno.