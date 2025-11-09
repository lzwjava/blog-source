---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Sincronización Automatizada de Git mediante Cron
translated: true
type: note
---

Para sincronizar automáticamente las actualizaciones de los `git push` de una laptop a un clon del mismo repositorio en otra laptop (sin un `git pull` manual), no puedes depender únicamente de Git para obtener actualizaciones "automáticas" en tiempo real entre máquinas—Git está diseñado para funcionar bajo un modelo basado en extracción (pull). Sin embargo, puedes configurar una tarea programada en la segunda laptop para buscar (fetch) y fusionar (merge) los cambios del repositorio remoto (GitHub en tu caso) periódicamente. Esta es la forma más simple y confiable para una configuración personal como la tuya.

Aquí te explicamos cómo hacerlo en tu Mac (ya que estás usando un MacBook Air). Usaremos `cron` para la programación, ya que está integrado y es ligero. Supongamos que ambas laptops tienen clones de `github.com:lzwjava/blog-source` y que estás en la rama `main`.

### Paso 1: Asegurar que el Repositorio en la Segunda Laptop esté Configurado Correctamente
En la segunda laptop:
1. Navega a tu repositorio: `cd /ruta/hacia/blog-source`
2. Asegúrate de que rastree el repositorio remoto: `git remote -v` (debería mostrar `origin` como tu repositorio de GitHub).
3. Si no es así, agrégalo: `git remote add origin git@github.com:lzwjava/blog-source.git`
4. Obtén el estado actual: `git fetch origin`
5. Cámbiate a main: `git checkout main`
6. Establece la rama upstream: `git branch --set-upstream-to=origin/main main`

Prueba una extracción manual: `git pull origin main`. Debería funcionar como en tu salida.

### Paso 2: Crear un Script para la Extracción Automatizada
Crea un script de shell simple para manejar la extracción de forma segura (hace fetch, verifica si hay conflictos y hace pull si está limpio).

1. En la raíz de tu repositorio, crea `auto-pull.sh`:
   ```bash:disable-run
   #!/bin/bash
   cd "$(dirname "$0")"  # Cambiar al directorio del repositorio
   git fetch origin
   if git diff HEAD origin/main --quiet; then
       git pull origin main
       echo "Auto-pull completado: $(date)"
   else
       echo "Advertencia: Se detectaron cambios locales. Omitiendo pull. Resuelve manualmente: $(date)"
       # Opcional: Enviar correo electrónico o notificación (ver más abajo)
   fi
   ```

2. Hazlo ejecutable: `chmod +x auto-pull.sh`

Este script:
- Obtiene (fetch) actualizaciones sin fusionar.
- Verifica si tu rama local está limpia (sin cambios sin confirmar).
- Hace pull solo si es seguro; de lo contrario, te advierte.

### Paso 3: Programarlo con Cron
Cron ejecuta trabajos periódicamente. Lo ejecutaremos cada 5 minutos (ajusta según sea necesario; por ejemplo, cada hora).

1. Abre el editor de crontab: `crontab -e` (usa nano si se solicita: `nano ~/.crontab`).

2. Agrega esta línea al final (para cada 5 minutos):
   ```
   */5 * * * * /ruta/hacia/blog-source/auto-pull.sh >> /ruta/hacia/blog-source/pull-log.txt 2>&1
   ```
   - Reemplaza `/ruta/hacia/blog-source` con la ruta real de tu repositorio (por ejemplo, `~/blog-source`).
   - El `>> pull-log.txt` registra la salida en un archivo para depuración.

3. Guarda y sale (Ctrl+O, Enter, Ctrl+X en nano).
4. Verifica: `crontab -l` (debería mostrar tu línea).
5. Prueba: Espera 5 minutos o ejecuta `crontab -e` nuevamente para agregar `* * * * *` temporalmente (cada minuto), luego revierte.

Cron se ejecuta como tu usuario, por lo que respeta tu clave SSH para la autenticación en GitHub (como en tu salida de pull).

### Mejoras Opcionales
- **Manejar Conflictos/Notificaciones**: Si el script detecta problemas, agrega una notificación. Edita `auto-pull.sh` para agregar:
  ```bash
  # Si hay advertencia, enviar notificación de macOS
  osascript -e 'display notification "Git pull omitido debido a cambios locales" with title "Blog Repo Sync"'
  ```
- **Ejecutar en Push (desde la Primera Laptop)**: Para una sincronización más similar a un "push", usa GitHub Actions en la primera laptop. Crea `.github/workflows/sync.yml`:
  ```yaml
  name: Auto Sync
  on: [push]
  jobs:
    sync:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
        - name: Notify (e.g., via webhook to second laptop)
          run: curl -X POST https://your-second-laptop-webhook-endpoint  # Configura un servidor simple en la segunda laptop
  ```
  Pero esto requiere un listener en la segunda máquina (por ejemplo, a través de ngrok + una pequeña aplicación Flask), lo cual es excesivo para la mayoría de los casos.
- **Compensaciones de Frecuencia**: Cada 5 minutos está bien para un repositorio de blog. Para tiempo real, considera herramientas como `watch` en una terminal (`watch -n 300 git pull`), pero cron no requiere supervisión.
- **Nota sobre Proxy**: Tu salida muestra proxies HTTP/HTTPS—cron los heredará, por lo que los pulls deberían funcionar tal cual.

Ahora, cuando hagas push desde la primera laptop (`git push origin main`), la segunda se sincronizará automáticamente cada 5 minutos. Revisa `pull-log.txt` para ver el historial.

Si encuentras problemas de autenticación/proxy en cron, agrega `export HTTP_PROXY=http://127.0.0.1:7890` etc. al script. Para Windows en la otra laptop, usa el Programador de tareas en su lugar.