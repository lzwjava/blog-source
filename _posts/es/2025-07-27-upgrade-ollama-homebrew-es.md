---
audio: false
generated: true
image: false
lang: es
layout: post
title: Actualizar Ollama con Homebrew
translated: true
type: note
---

Para actualizar Ollama a la versión más reciente (actualmente v0.10.0 a julio de 2025) usando Homebrew en macOS, sigue estos pasos:

1. Actualiza las fórmulas de Homebrew para asegurarte de que conoce las últimas versiones disponibles:
   ```
   brew update
   ```

2. Actualiza Ollama específicamente:
   ```
   brew upgrade ollama
   ```

3. Verifica la actualización comprobando la versión:
   ```
   ollama --version
   ```

Si estás ejecutando Ollama como un servicio en segundo plano, reinícialo después de la actualización:
```
brew services restart ollama
```

Alternativamente, si lo ejecutas manualmente, detén cualquier proceso existente e inícialo de nuevo con tu comando preferido (por ejemplo, de las notas en la salida de tu instalación):
```
OLLAMA_FLASH_ATTENTION="1" OLLAMA_KV_CACHE_TYPE="q8_0" /opt/homebrew/opt/ollama/bin/ollama serve
```

No se necesitan instrucciones especiales de actualización más allá de este proceso estándar.

[Lanzamientos de Ollama](https://github.com/ollama/ollama/releases)