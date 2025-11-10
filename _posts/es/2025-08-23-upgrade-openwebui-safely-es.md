---
audio: false
generated: true
image: false
lang: es
layout: post
title: Actualización Segura de Open WebUI Ahora
translated: true
type: note
---

Entendido. Aquí tienes las formas seguras y directas de actualizar Open WebUI.

## Si lo instalaste con `pip` (tu caso)

```bash
# 1) (Recomendado) activa el entorno que usas para Open WebUI
#    ej. con conda:
conda activate open-webui
#    o con venv:
# source ~/open-webui-venv/bin/activate

# 2) Actualiza a la última versión
python3.11 -m pip install -U open-webui

# 3) (Opcional) si la caché de pip causa problemas
python3.11 -m pip cache purge
python3.11 -m pip install --no-cache-dir -U open-webui

# 4) Verifica lo que obtuviste
python3.11 -m pip show open-webui
```

La documentación oficial dice que solo `pip install -U open-webui` actualiza a la última versión. ([Open WebUI][1])

### Mantén tus datos/configuración persistentes

Cuando ejecutes el servidor, puedes fijar un directorio de datos para que las actualizaciones no lo afecten:

```bash
# macOS/Linux
DATA_DIR="$HOME/.open-webui" open-webui serve
# Windows (PowerShell)
$env:DATA_DIR="C:\open-webui\data"; open-webui serve
```

Esto refleja la guía de la documentación para establecer `DATA_DIR` (o usar `uvx … @latest serve` con la misma variable) para que tus chats/configuración residan fuera de la instalación del paquete. ([Open WebUI][2])

> Consejo: Si anteriormente ejecutaste sin `DATA_DIR`, comienza a usarlo ahora; Open WebUI usará esa carpeta de ahora en adelante.

## Si usaste Docker (para completar)

```bash
# detener y eliminar el contenedor antiguo (los datos están en el volumen nombrado)
docker rm -f open-webui

# obtener la imagen más reciente
docker pull ghcr.io/open-webui/open-webui:main

# iniciar nuevamente con tu volumen existente
docker run -d -p 3000:8080 \
  -v open-webui:/app/backend/data \
  --name open-webui \
  ghcr.io/open-webui/open-webui:main
```

Este es el flujo de actualización manual recomendado por el proyecto; tus datos persisten en el volumen de Docker `open-webui`. ([Open WebUI][3])

## Verifica qué es lo "más reciente"

Puedes confirmar la etiqueta más nueva desde GitHub Releases antes/después de actualizar. ([GitHub][4])

Si algo genera un error (ej., incompatibilidad de versión de Python), asegúrate de estar en Python 3.11 para el método pip, que el proyecto recomienda explícitamente. ([GitHub][5])

¿Quieres que revise tu entorno actual o interprete la salida de algún error de actualización? Pégala aquí y la solucionaré.

[1]: https://docs.openwebui.com/getting-started/quick-start/?utm_source=chatgpt.com "️ Inicio Rápido"
[2]: https://docs.openwebui.com/?utm_source=chatgpt.com "Open WebUI: Inicio"
[3]: https://docs.openwebui.com/getting-started/updating/?utm_source=chatgpt.com "Actualizando Open WebUI"
[4]: https://github.com/open-webui/open-webui/releases?utm_source=chatgpt.com "Lanzamientos · open-webui/open-webui"
[5]: https://github.com/open-webui/open-webui?utm_source=chatgpt.com "open-webui/open-webui: Interfaz de IA fácil de usar ..."