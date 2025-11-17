---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Uso de hf-mirror.com en China
translated: true
type: note
---

### Comprender hf-mirror.com
hf-mirror.com es un espejo mantenido por la comunidad del Hugging Face Hub oficial (huggingface.co), diseñado específicamente para ayudar a los usuarios en China (incluyendo Guangzhou) a eludir las restricciones de red y descargar modelos/datasets de IA más rápido. Replica la estructura completa del repositorio, por lo que puedes acceder a modelos como GPT-2 o datasets como WikiText sin acceder directamente al sitio original, que a menudo es lento o está bloqueado. Dado que usas el proxy Clash a menudo, ten en cuenta que hf-mirror.com está alojado localmente y normalmente no requiere un proxy para el acceso—está optimizado para uso directo en China. Si ya estás proxyficando el tráfico a través de Clash, puedes dirigir el tráfico de hf-mirror.com directamente (para evitar saltos innecesarios) o mantenerlo proxyficado si lo prefieres.

### Configuración Básica: Usando el Espejo
La clave es establecer la variable de entorno `HF_ENDPOINT` para que apunte al espejo. Esto funciona globalmente para las herramientas de Hugging Face como la librería `transformers`, `huggingface-cli`, o `hfd` (un descargador más rápido). Haz esto **antes** de importar las librerías o ejecutar las descargas.

#### 1. Establecer la Variable de Entorno
- **En Linux/macOS (permanente)**: Añade a tu `~/.bashrc` o `~/.zshrc`:
  ```
  echo 'export HF_ENDPOINT=https://hf-mirror.com' >> ~/.bashrc
  source ~/.bashrc
  ```
- **En Windows (PowerShell, permanente)**: Ejecuta una vez:
  ```
  [System.Environment]::SetEnvironmentVariable('HF_ENDPOINT', 'https://hf-mirror.com', 'User')
  ```
  Luego reinicia tu terminal.
- **Temporal (cualquier SO)**: Prefija los comandos así:
  ```
  HF_ENDPOINT=https://hf-mirror.com tu_comando_aquí
  ```

Esto redirige todas las descargas de Hugging Face al espejo sin cambiar tu código.

#### 2. Instalar las Herramientas Requeridas
- Instala la CLI de Hugging Face Hub (para descargas):
  ```
  pip install -U huggingface_hub
  ```
- Para descargas aún más rápidas, obtén `hfd` (Hugging Face Downloader, usa aria2 para velocidades multi-hilo):
  ```
  wget https://hf-mirror.com/hfd/hfd.sh  # O descarga via navegador
  chmod +x hfd.sh
  ```

#### 3. Descargando Modelos o Datasets
- **Usando huggingface-cli** (soporta reanudación en interrupción):
  ```
  # Descargar un modelo (ej., GPT-2)
  huggingface-cli download gpt2 --resume-download --local-dir ./gpt2

  # Descargar un dataset (ej., WikiText)
  huggingface-cli download --repo-type dataset wikitext --resume-download --local-dir ./wikitext
  ```
- **Usando hfd** (más rápido, especialmente para archivos grandes):
  ```
  # Modelo
  ./hfd.sh gpt2

  # Dataset
  ./hfd.sh wikitext --dataset
  ```
- **En código Python** (ej., con la librería transformers):
  ```python
  import os
  os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'  # Establecer antes de los imports

  from transformers import AutoModel, AutoTokenizer
  model = AutoModel.from_pretrained('gpt2')  # Descarga desde el espejo automáticamente
  tokenizer = AutoTokenizer.from_pretrained('gpt2')
  ```
  Ejecutar con: `HF_ENDPOINT=https://hf-mirror.com python tu_script.py`

#### 4. Manejando Modelos con Acceso Restringido/Requieren Login
Algunos modelos (ej., Llama-2) requieren una cuenta y un token de Hugging Face:
- Inicia sesión en huggingface.co (usa tu proxy Clash si el sitio está bloqueado).
- Genera un token en https://huggingface.co/settings/tokens.
- Descarga con:
  ```
  huggingface-cli download --token hf_TuTokenAqui meta-llama/Llama-2-7b-hf --resume-download --local-dir ./Llama-2-7b-hf
  ```
  O para hfd:
  ```
  ./hfd.sh meta-llama/Llama-2-7b-hf --hf_username tu_usuario --hf_token hf_TuTokenAqui
  ```

### Integración con el Proxy Clash
Dado que hf-mirror.com es un espejo chino, debería ser accesible sin Clash (la conexión directa es más rápida). Sin embargo, si quieres proxyficarlo (ej., por consistencia o si encuentras algún problema), configura Clash para enrutar el tráfico a hf-mirror.com a través de tu grupo de proxy preferido. Clash no necesita una configuración especial "HF"—es a nivel del sistema.

#### Consejos Rápidos de Configuración de Clash
- Asegúrate de que Clash esté ejecutándose y configurado como tu proxy del sistema (en Clash: Ve a "General" > Activar "System Proxy").
- **Enrutar hf-mirror.com directamente (recomendado para velocidad)**: Edita tu archivo de configuración YAML de Clash (usualmente `config.yaml` en la carpeta de Clash). Añade una regla para omitir el proxy para el espejo:
  ```
  rules:
    # ... tus reglas existentes ...
    - DOMAIN-SUFFIX,hf-mirror.com,DIRECT  # Omite el proxy, va directo
    # ... resto de reglas ...
  ```
  Recarga la configuración en Clash (Profiles > Reload).
- **Proxyficarlo si es necesario**: Si prefieres enrutarlo a través de Clash, no añadas ninguna regla especial—seguirá tu regla por defecto (ej., `MATCH,Proxy`). Prueba haciendo ping a hf-mirror.com en un navegador con Clash activado/desactivado.
- Para descargas: Ejecuta comandos en una terminal donde el proxy del sistema esté activo (Clash lo maneja). Si usas Python, librerías como `requests` (usada por transformers) respetan las variables de entorno `HTTP_PROXY`/`HTTPS_PROXY` establecidas por Clash (ej., `http://127.0.0.1:7890` para el puerto HTTP).
- Prueba: Intenta descargar un modelo pequeño como `distilbert-base-uncased`. Si es lento, desactiva Clash para el tráfico de hf-mirror.com.

### Resolución de Problemas
- **¿Las descargas aún acceden a huggingface.co?** Asegúrate de que `HF_ENDPOINT` esté establecida **antes** de importar cualquier librería de HF (reinicia tu notebook/terminal).
- **¿Velocidades lentas?** Usa `hfd` con aria2 (soporta múltiples conexiones). O revisa tu red—los usuarios de Guangzhou a menudo obtienen 10-50MB/s en hf-mirror.com.
- **¿Errores con datasets?** Algunos tienen scripts personalizados; edítalos para usar `https://hf-mirror.com` como la URL base.
- **Específico de Windows**: Si usas Anaconda, establece la variable de entorno en el entorno base.
- Para alojar localmente un espejo avanzado (si quieres control total), revisa herramientas de código abierto como Olah o hf-mirror-site en GitHub, pero comienza con el espejo público.

Esta configuración debería permitirte descargar de manera confiable. Si encuentras errores específicos, comparte la salida para obtener más ayuda.

### Referencias
- [Guía Oficial de HF-Mirror](https://hf-mirror.com/)
- [Documentos de Hugging Face Hub sobre Endpoints](https://huggingface.co/docs/huggingface_hub/en/package_reference/environment_variables#huggingface_hub_constants.HF_ENDPOINT)
- [Descargador hfd](https://hf-mirror.com/hfd/hfd.sh)
- [Reglas de Configuración de Clash](https://github.com/Dreamacro/clash/wiki/Configuration#rules)
- [Stack Overflow: Descargando en China](https://stackoverflow.com/questions/77388822/how-to-download-huggingface-bert-base-uncased-in-china)