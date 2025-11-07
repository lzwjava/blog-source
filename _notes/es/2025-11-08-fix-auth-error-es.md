---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Corrección de Error de Autenticación de la API de Traducción
translated: true
---

### Análisis del Flujo de Trabajo y Causa del Error

Tu flujo de trabajo de GitHub Actions para "Translate Recent Notes" parece estar bien estructurado en general: está haciendo checkout del repositorio, configurando Python, instalando dependencias, ejecutando un script de traducción en las N publicaciones más recientes y confirmando los cambios en `_notes/`. Sin embargo, basándome en los registros que compartiste anteriormente (con los errores 401 durante la traducción a idiomas como ar, de, fr, etc.), el problema está en la autenticación para las llamadas a la API de traducción dentro de `scripts/translation/update_lang_notes.py`.

#### Causa Principal
- El error `"No cookie auth credentials found"` (HTTP 401) es específico de la **API de OpenRouter** (o de una biblioteca/cliente de Python que interactúa con ella, como LiteLLM o un SDK no oficial). Esto sucede cuando la solicitud a la API carece de los encabezados de autenticación adecuados.
- OpenRouter espera `Authorization: Bearer <tu_openrouter_api_key>` en las solicitudes. Si la clave no se pasa correctamente, algunos clientes recurren a (o malinterpretan como que se necesita) autenticación basada en cookies, desencadenando este error exacto.
- En tu flujo de trabajo:
  - Estás configurando `OPENROUTER_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}`, que pasa un valor secreto al entorno del script.
  - Pero es probable que el script no esté leyendo/usando correctamente esta variable de entorno. Coincidencias incorrectas comunes:
    - El script espera `OPENAI_API_KEY` (para endpoints compatibles con OpenAI como OpenRouter).
    - O está usando una biblioteca (por ejemplo, el SDK de Python `openai`) sin establecer la URL base a `https://openrouter.ai/api/v1`.
    - El secreto `DEEPSEEK_API_KEY` podría contener realmente tu **clave API de OpenRouter** (enrutada a modelos DeepSeek/Grok), pero si es una clave directa de DeepSeek, no funcionará para OpenRouter.
- Según los registros, el script está usando el modelo `'x-ai/grok-4-fast'` (Grok 4 vía OpenRouter), y está procesando el front matter/títulos exitosamente pero falla en la traducción del contenido por idioma.
- Esto no es un problema de GitHub Actions, está en la configuración del cliente API del script de Python. El flujo de trabajo continúa hasta el paso de commit (de ahí el registro `git config user.name "github-actions[bot]"`), pero sin las traducciones, solo se agregan los archivos en inglés.

#### Soluciones Recomendadas
1. **Actualizar las Variables de Entorno en el Flujo de Trabajo**:
   - Alínealo con las configuraciones comunes de OpenRouter (compatible con OpenAI). Cambia el bloque `env` en el paso "Translate posts" a:
     ```
     env:
       GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
       OPENAI_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}  # Renombrar var a lo que el script espera
       OPENAI_BASE_URL: https://openrouter.ai/api/v1   # Requerido para enrutar a OpenRouter
     ```
   - Si `DEEPSEEK_API_KEY` es tu clave de OpenRouter, perfecto. Si es una clave directa de DeepSeek, crea un nuevo secreto `OPENROUTER_API_KEY` en la configuración del repositorio con tu clave real de OpenRouter (obtén una en [openrouter.ai/keys](https://openrouter.ai/keys)).
   - Prueba: Añade `echo $OPENAI_API_KEY` (oculto) al paso de ejecución para depurar en los registros.

2. **Corregir el Script de Python (`update_lang_notes.py`)**:
   - Asegúrate de que inicialice el cliente OpenAI así (asumiendo la biblioteca `openai`):
     ```python
     import os
     from openai import OpenAI

     client = OpenAI(
         api_key=os.getenv("OPENAI_API_KEY"),
         base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")  # Por defecto usa OpenAI si no está configurado
     )

     # Luego usa client.chat.completions.create(..., model="x-ai/grok-4-fast")
     ```
   - Si usas LiteLLM (común para múltiples proveedores): Instálalo si no está en `requirements.txt`, y llama a `completion(model="openrouter/x-ai/grok-4-fast", api_key=os.getenv("OPENAI_API_KEY"), api_base="https://openrouter.ai/api/v1", ...)`.
   - Para el bucle de traducción: Añade manejo de errores por idioma (por ejemplo, `try/except` alrededor de las llamadas a la API, registra fallos, omite si es 401).
   - ¿Manejar cookies explícitamente? Es poco probable que sea necesario: usa claves API. Si el script tiene código de navegador/Selenium, elimínalo para la confiabilidad del CI.

3. **Mejoras en el Flujo de Trabajo**:
   - **Validación de Entrada**: Añade una comprobación para N=0 o `--n` inválido para evitar no procesar nada.
   - **Commit Condicional**: Tu `git diff --cached --quiet || git commit` es bueno, pero actualiza el mensaje para reflejar todos los idiomas: `-m "Add translated posts (ar, de, es, fr, hi, ja, zh, hant)"`.
   - **Caché**: Añade `actions/cache` para `pip` para acelerar las instalaciones.
   - **Modo Depuración**: Añade una entrada opcional `debug: true` y un flag `--debug` al script para registro detallado.
   - **Permisos**: Asegúrate de que el entorno `github-pages` tenga acceso de lectura/escritura si es necesario.
   - Fragmento YAML actualizado completo para el paso "Translate posts":
     ```
     - name: Translate posts
       run: |
         python scripts/translation/update_lang_notes.py --n ${{ inputs.n }}
       env:
         GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
         OPENAI_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}
         OPENAI_BASE_URL: https://openrouter.ai/api/v1
     ```

4. **Pasos de Prueba**:
   - **Prueba Local**: Ejecuta `python scripts/translation/update_lang_notes.py --n 1` localmente con las variables de entorno exportadas (por ejemplo, `export OPENAI_API_KEY=tu_clave`).
   - **Prueba del Flujo de Trabajo**: Actívalo con `workflow_dispatch` y N=1, revisa los registros para las llamadas a la API.
   - **Verificar Secreto**: En la configuración del repositorio > Secrets, confirma que `DEEPSEEK_API_KEY` tenga una clave válida de OpenRouter (que comience con `sk-or-...`).
   - Si sigue fallando, añade `--verbose` al script e inspecciona los encabezados de la solicitud (por ejemplo, vía `print(client.api_key)`).

Esto debería resolver los errores 401 y hacer que fluyan las traducciones. Si compartes fragmentos de `update_lang_notes.py` (por ejemplo, la inicialización del cliente API), puedo identificar el problema con más precisión.

#### Referencias
- [Inicio Rápido de OpenRouter (Configuración de Autenticación API)](https://openrouter.ai/docs/quickstart)
- [Integración de LiteLLM con OpenRouter](https://docs.litellm.ai/docs/providers/openrouter) (si se usa)
- [Incidencia en GitHub sobre Error de Autenticación Similar en OpenRouter](https://github.com/mendableai/firecrawl/issues/1352)
- [Hilo en Reddit sobre Errores 401 en OpenRouter](https://www.reddit.com/r/openrouter/comments/1oqiaol/error_401_no_cookie_auth_credentials_found/)