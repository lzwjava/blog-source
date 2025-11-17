---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Soluciones para la Velocidad de Descarga de Hugging Face
translated: true
type: note
---

Tu problema es muy típico para personas en China continental (especialmente en el sur como Guangzhou) al descargar archivos grandes de Hugging Face.

### Por qué sin proxy → extremadamente lento (~200–300 KB/s)
- Aunque estés usando **hf-mirror.com** (el espejo chino oficial operado por HF + 01.AI), los archivos parquet grandes reales de FineWeb **no están almacenados en caché dentro de China**.
- hf-mirror.com solo te redirige a la CDN global (que ahora usa xet-bridge en AWS us-east-1).
- Desde Guangzhou sin proxy → tu tráfico pasa por puertas de enlace internacionales (backbone de China Telecom/Unicom/Mobile → AWS EE.UU.), y las descargas de archivos grandes son fuertemente limitadas o sujetas a QoS. Archivos de 2 GB fácilmente caen a < 500 KB/s, a veces incluso 100 KB/s.

### Por qué con proxy Clash → repentinamente muy rápido (a menudo 20–100 MB/s)
- Tu Clash casi seguro está usando un nodo en Hong Kong, Taiwán, Japón, Singapur o Corea (muy común para usuarios de Guangzhou).
- Estos nodos tienen:
  - Interconexión directa o conectividad muy buena con AWS us-east-1 (o Cloudflare que HF también usa)
  - Sin limitaciones del Gran Cortafuegos en el tráfico saliente
  - Ancho de banda mucho mayor
- Así que, aunque estés "desviándote" a través del proxy, la ruta real es mucho más rápida que la salida internacional directa desde China continental.

### En resumen
Directo (incluso vía hf-mirror.com) desde Guangzhou → lento porque el almacenamiento real sigue estando en EE.UU., y el ancho de banda China → EE.UU. para archivos grandes es terrible en 2025.
Proxy Clash (nodo HK/TW/JP/SG) → rápido porque esos nodos tienen excelente conectividad con AWS EE.UU.

### Soluciones recomendadas (de más rápida a más lenta)

1. **Sigue usando Clash (o v2rayN, Surge, etc.) con un nodo HK/TW/JP de baja latencia** — esta es actualmente la forma más rápida en China continental para FineWeb, RedPajama, The Stack, etc.

2. Usa **el endpoint acelerado oficial de HF en China** (funciona sin proxy para muchas personas en 2024-2025):
   ```bash
   export HF_ENDPOINT=https://hf-mirror.com
   ```
   Luego usa huggingface-cli o la biblioteca datasets directamente (no wget). Muchos usuarios en China reportan 50–200 MB/s de esta manera ahora porque HF ha comenzado a almacenar más fragmentos en caché en Aliyun/Tencent Cloud en 2025.

3. Usa **FastGit + hugger** o **espejos openi/pkulaw** (algunos fragmentos están en caché en China):
   Ejemplo:
   ```bash
   pip install hugger
   hugger download HuggingFaceFW/fineweb --revision main --include "CC-MAIN-2013-20/*.parquet"
   ```

4. Mantén wget + hf-mirror.com pero fórzalo a través de tu proxy Clash (lo que ya estás haciendo).

### Comando rápido de una línea para descargar cualquier fragmento de FineWeb rápido desde Guangzhou
```bash
# Establecer proxy HTTP de Clash (puerto usualmente 7890)
export https_proxy=http://127.0.0.1:7890

# Luego usar aria2 (mucho más rápido + reanudación que wget)
aria2c -x16 -s16 -k1M "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00000.parquet"
```

Conseguirás fácilmente 30–100 MB/s dependiendo de tu nodo proxy.

Así que, en conclusión: en China continental en 2025, para archivos >1 GB en Hugging Face, usar un proxy HK/TW/JP sigue siendo casi siempre más rápido que la conexión directa, incluso usando hf-mirror.com. Esta es simplemente la realidad del ancho de banda internacional desde China en este momento.