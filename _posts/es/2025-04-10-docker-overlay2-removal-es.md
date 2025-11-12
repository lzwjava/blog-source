---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Resolución de Errores al Eliminar Overlay2 de Docker
translated: true
type: note
---

Ese error significa que Docker no pudo eliminar el sistema de archivos overlay2 del contenedor — el kernel/VM devolvió un error de E/S de bajo nivel (`readdirent merged: bad message`). En macOS, esto suele ocurrir cuando la VM de Docker o el almacenamiento overlay están en un estado incorrecto. A continuación, se muestran pasos seguros y ordenados (de menos destructivos → más agresivos) que puedes probar para recuperarte.

**Importante:** algunos comandos a continuación pueden eliminar datos (imágenes/volúmenes). Marcaré los pasos destructivos y mostraré los comandos exactos para que puedas copiar/pegar si lo deseas.

---

# Comprobaciones rápidas (seguras)

En una terminal, ejecuta:

```bash
# mostrar el estado del contenedor y la ID del contenedor problemático
docker ps -a --no-trunc | grep ccd89a3f36a1528cb923c90de8755faeb36e229c || true

# intentar una eliminación forzada del contenedor
docker rm -f ccd89a3f36a1528cb923c90de8755faeb36e229c
```

Si `docker rm -f` tiene éxito, has terminado. Si falla con el mismo error de overlay, continúa.

---

# Reiniciar Docker (Docker Desktop para macOS) — siguiente paso recomendado (seguro)

Cierra Docker Desktop completamente (usa el icono de la ballena → Quit) y luego inícialo de nuevo. O desde la línea de comandos:

```bash
# macOS — reiniciar Docker Desktop via AppleScript
osascript -e 'quit app "Docker"'
open -a Docker
```

Después de que Docker se reinicie, intenta `docker compose down` o `docker rm -f <id>` de nuevo.

---

# Reiniciar el host (muy seguro)

Si es posible reiniciar, reiniciar macOS a menudo soluciona problemas del sistema de archivos de la VM:

* Reinicia el Mac, luego inicia Docker Desktop y vuelve a intentarlo.

---

# Si sigue fallando — usa las acciones de Troubleshoot de Docker Desktop (seguro / medio)

Abre Docker Desktop → Troubleshoot:

* Haz clic en **Restart Docker** (si aún no lo has hecho).
* Si eso falla, prueba **Clean / Purge data** o **Reset to factory defaults** — **advertencia**: estos eliminan imágenes/contenedores/volúmenes. Úsalos solo si puedes permitirte perder los datos locales de Docker.

---

# Si estás en Docker Engine (Linux) o te sientes cómodo con la limpieza manual (destructivo)

**Haz esto solo si entiendes el riesgo de pérdida de datos.** Detén el daemon de Docker, elimina el directorio overlay2 para la ID problemática, luego reinicia Docker.

```bash
# detener el daemon de docker (Linux)
sudo systemctl stop docker

# haz una copia de seguridad de la carpeta overlay2 primero (opcional, si tienes espacio)
sudo cp -a /var/lib/docker/overlay2/7acbf095f3537e4829397e10f2134499389c724d3378782a8882ff1299fc431f /root/overlay2-backup-7acbf095

# si se hizo la copia de seguridad / no es necesaria, elimina el directorio merged para ese overlay:
sudo rm -rf /var/lib/docker/overlay2/7acbf095f3537e4829397e10f2134499389c724d3378782a8882ff1299fc431f

# (opcionalmente) eliminar los metadatos del contenedor si es necesario
# ADVERTENCIA: elimina solo los archivos de los que estés seguro que corresponden al contenedor dañado
sudo rm -rf /var/lib/docker/containers/ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18

# iniciar docker
sudo systemctl start docker

# luego intenta limpiar elementos huérfanos
docker system prune -a --volumes
```

De nuevo: eliminar archivos bajo `/var/lib/docker` es destructivo y puede dañar otros contenedores si se hace incorrectamente. Úsalo solo si sabes lo que estás eliminando.

---

# Limpieza menos destructiva que a menudo ayuda

Si no puedes eliminar el overlay directamente o prefieres un enfoque más suave:

```bash
# intenta podar objetos no utilizados
docker system prune -f
docker volume prune -f

# eliminar imágenes/contenedores no utilizados (ten cuidado)
docker image prune -a -f
docker container prune -f
```

Esto puede liberar espacio y a veces permite que Docker vuelva a ejecutar operaciones de eliminación con éxito.

---

# Si el problema recurre y usas Docker Desktop para Mac

* Considera aumentar el tamaño del disco de la VM de Docker (Settings → Resources → Disk image size).
* Si dependes de datos locales importantes, exporta los volúmenes/contenedores primero (`docker export`, `docker save`) antes de usar Reset/Purge.

---

# Diagnósticos para recopilar (si quieres que te ayude más)

Si nada de lo anterior lo soluciona, comparte las salidas de estos comandos (no destructivos) y sugeriré próximos pasos específicos:

```bash
docker info
docker ps -a
docker compose version
docker version
# listar directorios overlay (Linux)
ls -lah /var/lib/docker/overlay2 | head -n 40
```

(Si estás en Docker Desktop para macOS, `ls /var/lib/docker` no mostrará el contenido de la VM — es preferible reiniciar Docker Desktop o usar la UI de Troubleshoot).

---

Si quieres, dime si estás ejecutando **Docker Desktop en macOS** (lo más probable) o **Docker Engine en Linux** — te daré una secuencia más corta y personalizada. Si lo prefieres, también puedo producir una lista de verificación de una línea que puedes ejecutar en orden.