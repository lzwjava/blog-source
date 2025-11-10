---
audio: false
generated: true
image: false
lang: es
layout: post
title: Cambiar Puerto de Open WebUI
translated: true
type: note
---

Para cambiar el puerto al ejecutar Open WebUI usando el comando `open-webui serve` (normalmente después de instalar via pip), utiliza el flag `--port` seguido del número de puerto deseado. El puerto predeterminado es 8080.

### Pasos:
1. Asegúrate de que Open WebUI esté instalado:  
   ```
   pip install open-webui
   ```

2. Ejecuta el servidor en un puerto diferente (ej. 3000):  
   ```
   open-webui serve --port 3000
   ```

   - Esto hará que la WebUI sea accesible en `http://localhost:3000` (o la dirección IP de tu servidor con el nuevo puerto).
   - Nota: La variable de entorno `PORT` se ignora cuando se usa el comando `serve`; debes usar el flag `--port` en su lugar.

Si estás usando Docker en lugar de una instalación directa:
- Establece la variable de entorno `PORT`, ej. `docker run -e PORT=3000 ...`.
- Mapea el puerto externamente con `-p <puerto_host>:3000` (ajusta según sea necesario).

Para detalles completos de instalación y configuración, consult la documentación oficial.

[Configuración de Variables de Entorno | Open WebUI](https://docs.openwebui.com/getting-started/env-configuration/)  
[Inicio Rápido | Open WebUI](https://docs.openwebui.com/getting-started/quick-start/)