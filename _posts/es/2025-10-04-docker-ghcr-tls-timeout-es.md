---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Corrección del Error de Tiempo de Espera TLS de GHCR en Docker
translated: true
type: note
---

El error que estás encontrando, `Get "https://ghcr.io/v2/": net/http: TLS handshake timeout`, normalmente indica un problema de red cuando Docker intenta descargar imágenes del GitHub Container Registry (GHCR). Aquí hay algunos pasos para solucionar y arreglar el problema:

---

### 1. **Verifica tu conexión a Internet**
- Asegúrate de que tu máquina tiene una conexión a Internet estable.
- Intenta acceder a `https://ghcr.io` en tu navegador para confirmar que puedes llegar al sitio.

---

### 2. **Verifica el estado del demonio de Docker**
- Reinicia el demonio de Docker:
  ```bash
  sudo systemctl restart docker
  ```
- Verifica que Docker esté en ejecución:
  ```bash
  sudo systemctl status docker
  ```

---

### 3. **Configura el DNS de Docker**
- Si estás detrás de una red corporativa o un proxy, Docker podría necesitar configuraciones de DNS personalizadas.
- Edita o crea el archivo `/etc/docker/daemon.json`:
  ```json
  {
    "dns": ["8.8.8.8", "1.1.1.1"]
  }
  ```
- Reinicia Docker:
  ```bash
  sudo systemctl restart docker
  ```

---

### 4. **Verifica la configuración del Proxy**
- Si estás detrás de un proxy, configura Docker para que lo use:
  ```bash
  mkdir -p ~/.docker
  echo '{
    "proxies": {
      "default": {
        "httpProxy": "http://your-proxy-address:port",
        "httpsProxy": "http://your-proxy-address:port",
        "noProxy": "localhost,127.0.0.1"
      }
    }
  }' > ~/.docker/config.json
  ```
- Reemplaza `your-proxy-address:port` con los detalles reales de tu proxy.

---

### 5. **Reintenta descargar la imagen manualmente**
- Intenta descargar la imagen manualmente para ver si el problema persiste:
  ```bash
  docker pull ghcr.io/librechat/librechat:latest
  ```
- Si funciona, reintenta `docker-compose up -d`.

---

### 6. **Verifica restricciones de Firewall/Red**
- Asegúrate de que tu firewall o red no esté bloqueando el acceso a `ghcr.io`.
- Deshabilita temporalmente el firewall para probar:
  ```bash
  sudo ufw disable
  ```
  (Vuelve a activarlo después de la prueba si es necesario).

---

### 7. **Actualiza Docker y Docker-Compose**
- Asegúrate de usar las últimas versiones:
  ```bash
  sudo apt update && sudo apt upgrade docker-ce docker-compose-plugin
  ```

---

### 8. **Configura las variables de entorno UID/GID**
- Las advertencias sobre `UID` y `GID` no son críticas, pero puedes configurarlas en tu archivo `.env` o `docker-compose.yml` para suprimir las advertencias:
  ```bash
  echo "UID=$(id -u)" >> .env
  echo "GID=$(id -g)" >> .env
  ```

---

### 9. **Usa un espejo de registro diferente (Opcional)**
- Si GHCR es consistentemente inaccesible, puedes intentar usar un espejo (aunque esto no es recomendable para producción):
  ```json
  {
    "registry-mirrors": ["https://mirror.example.com"]
  }
  ```
  Añade esto a `/etc/docker/daemon.json` y reinicia Docker.

---

### 10. **Verifica la sincronización de la hora**
- Asegúrate de que la hora de tu sistema esté sincronizada:
  ```bash
  sudo apt install ntp
  sudo systemctl restart ntp
  ```

---

### Tabla resumen de comandos

| Paso | Comando/Acción |
|------|----------------|
| Reiniciar Docker | `sudo systemctl restart docker` |
| Verificar estado de Docker | `sudo systemctl status docker` |
| Configurar DNS | Editar `/etc/docker/daemon.json` |
| Descargar imagen manualmente | `docker pull ghcr.io/librechat/librechat:latest` |
| Configurar UID/GID | `echo "UID=$(id -u)" >> .env` |

---

Si el problema persiste después de intentar estos pasos, házmelo saber junto con la salida de:
```bash
docker info
```
y cualquier mensaje de error que veas al ejecutar los comandos anteriores. ¡Esto ayudará a diagnosticar más a fondo!