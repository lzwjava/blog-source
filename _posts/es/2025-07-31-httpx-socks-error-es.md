---
audio: false
generated: true
image: false
lang: es
layout: post
title: Esquema de Proxy No Compatible
translated: true
type: note
---

El error indica que la librería `httpx`, utilizada por el cliente `openai` en tu script `gitmessageai.py`, está intentando configurar un proxy con la URL `socks://127.0.0.1:7891/`, pero el esquema `socks` no es compatible o no es reconocido, resultando en un `ValueError: Unknown scheme for proxy URL`. Esto sugiere que se está recogiendo una configuración de proxy de tu entorno o código, y está usando un esquema de proxy SOCKS no soportado.

Desglosemos de dónde podría venir el proxy y cómo solucionarlo.

### ¿De Dónde Viene el Proxy?

La configuración del proxy (`socks://127.0.0.1:7891/`) probablemente proviene de uno de los siguientes lugares:

1. **Variables de Entorno**
   - La librería `httpx` verifica automáticamente la configuración de proxy en variables de entorno como `HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`, o sus equivalentes en minúsculas (`http_proxy`, `https_proxy`, `all_proxy`).
   - Un valor como `socks://127.0.0.1:7891/` sugiere que se estableció un proxy SOCKS (común para herramientas como Shadowsocks o VPNs) en una de estas variables.
   - Para verificar si estas variables están establecidas, ejecuta lo siguiente en tu terminal:
     ```bash
     env | grep -i proxy
     ```
     Busca variables como `HTTP_PROXY=socks://127.0.0.1:7891` o `HTTPS_PROXY=socks://127.0.0.1:7891`.

2. **Configuración de Proxy a Nivel del Sistema**
   - Si estás usando un sistema Linux, la configuración del proxy podría estar configurada globalmente (por ejemplo, en `/etc/environment`, `/etc/profile`, o tu configuración de shell como `~/.bashrc`, `~/.zshrc`, o `~/.profile`).
   - Revisa estos archivos en busca de líneas como:
     ```bash
     export HTTP_PROXY="socks://127.0.0.1:7891"
     export HTTPS_PROXY="socks://127.0.0.1:7891"
     ```
   - Puedes ver estos archivos con:
     ```bash
     cat ~/.bashrc | grep -i proxy
     cat ~/.zshrc | grep -i proxy
     cat /etc/environment | grep -i proxy
     ```

3. **Configuración de Proxy en una Herramienta de Proxy**
   - La dirección `127.0.0.1:7891` es comúnmente utilizada por herramientas de proxy o VPN como Shadowsocks, V2Ray o Clash, que a menudo usan por defecto proxies SOCKS5 en puertos como 7890 o 7891.
   - Si has instalado o configurado una herramienta así, podría haber establecido automáticamente variables de entorno o configuraciones de proxy del sistema.

4. **Proxy Explícito en el Código**
   - Aunque es menos probable, tu script `gitmessageai.py` o una librería que use podría estar configurando explícitamente un proxy. Dado que el error ocurre en `httpx`, verifica si tu script pasa un proxy al cliente `OpenAI` o al cliente `httpx`.
   - Busca en tu script términos como `proxy`, `proxies`, o `httpx.Client`:
     ```bash
     grep -r -i proxy /home/lzwjava/bin/gitmessageai.py
     ```

5. **Configuración de la Librería Python**
   - Algunas librerías de Python (por ejemplo, `requests` o `httpx`) podrían heredar la configuración de proxy desde un archivo de configuración o una configuración previa. Sin embargo, `httpx` depende principalmente de variables de entorno o código explícito.

### ¿Por Qué `socks://` Está Causando un Problema?

- La librería `httpx` (utilizada por `openai`) no soporta de forma nativa el esquema `socks` (proxies SOCKS4/SOCKS5) a menos que se instalen dependencias adicionales como `httpx-socks`.
- El error `Unknown scheme for proxy URL` ocurre porque `httpx` espera proxies con esquemas como `http://` o `https://`, no `socks://`.

### Cómo Solucionar el Problema

Tienes dos opciones: **eliminar o evitar el proxy** si no es necesario, o **soportar el proxy SOCKS** si tienes la intención de usarlo.

#### Opción 1: Eliminar o Evitar el Proxy

Si no necesitas un proxy para la API de DeepSeek, puedes deshabilitar o evitar la configuración del proxy.

1. **Anular Variables de Entorno**
   - Si el proxy está establecido en las variables de entorno, anúlalas para tu sesión:
     ```bash
     unset HTTP_PROXY
     unset HTTPS_PROXY
     unset ALL_PROXY
     unset http_proxy
     unset https_proxy
     unset all_proxy
     ```
   - Para hacer esto permanente, elimina las líneas `export` correspondientes de `~/.bashrc`, `~/.zshrc`, `/etc/environment`, u otros archivos de configuración del shell.

2. **Ejecutar el Script Sin Proxy**
   - Ejecuta temporalmente tu script sin la configuración de proxy:
     ```bash
     HTTP_PROXY= HTTPS_PROXY= ALL_PROXY= python3 /home/lzwjava/bin/gitmessageai.py
     ```
   - Si esto funciona, el proxy era el problema.

3. **Evitar el Proxy en el Código**
   - Modifica tu script `gitmessageai.py` para deshabilitar explícitamente los proxies en el cliente `OpenAI`:
     ```python
     from openai import OpenAI
     import httpx

     def call_deepseek_api(prompt):
         api_key = os.getenv("DEEPSEEK_API_KEY")
         if not api_key:
             raise ValueError("DEEPSEEK_API_KEY environment variable is not set")
         client = OpenAI(
             api_key=api_key,
             base_url="https://api.deepseek.com",
             http_client=httpx.Client(proxies=None)  # Deshabilitar proxies
         )
         # Tu lógica de llamada a la API aquí
         response = client.chat.completions.create(
             model="deepseek",  # Reemplazar con el modelo correcto
             messages=[{"role": "user", "content": prompt}]
         )
         return response.choices[0].message.content
     ```
   - Establecer `proxies=None` asegura que `httpx` ignore cualquier configuración de proxy del entorno.

#### Opción 2: Soportar el Proxy SOCKS

Si necesitas usar el proxy SOCKS (por ejemplo, para acceder a la API de DeepSeek a través de una VPN o servidor proxy), debes añadir soporte SOCKS a `httpx`.

1. **Instalar `httpx-socks`**
   - Instala el paquete `httpx-socks` para habilitar el soporte para proxies SOCKS4/SOCKS5:
     ```bash
     pip install httpx-socks
     ```
   - Esto extiende `httpx` para manejar esquemas `socks://` y `socks5://`.

2. **Actualizar Tu Código**
   - Modifica tu script para usar el proxy SOCKS explícitamente:
     ```python
     from openai import OpenAI
     import httpx
     from httpx_socks import SyncProxyTransport

     def call_deepseek_api(prompt):
         api_key = os.getenv("DEEPSEEK_API_KEY")
         if not api_key:
             raise ValueError("DEEPSEEK_API_KEY environment variable is not set")
         # Configurar proxy SOCKS5
         proxy_transport = SyncProxyTransport.from_url("socks5://127.0.0.1:7891")
         client = OpenAI(
             api_key=api_key,
             base_url="https://api.deepseek.com",
             http_client=httpx.Client(transport=proxy_transport)
         )
         # Tu lógica de llamada a la API aquí
         response = client.chat.completions.create(
             model="deepseek",  # Reemplazar con el modelo correcto
             messages=[{"role": "user", "content": prompt}]
         )
         return response.choices[0].message.content
     ```
   - Reemplaza `socks5://` con `socks4://` si tu proxy usa SOCKS4.

3. **Verificar el Servidor Proxy**
   - Asegúrate de que el servidor proxy en `127.0.0.1:7891` esté ejecutándose. Si estás usando una herramienta como Clash o Shadowsocks, verifica su estado:
     ```bash
     netstat -tuln | grep 7891
     ```
   - Si ningún proceso está escuchando en el puerto 7891, inicia tu herramienta de proxy o corrige el puerto en la URL del proxy.

### Pasos Adicionales de Depuración

- **Verificar la Configuración de la Herramienta de Proxy**
  - Si estás usando una herramienta de proxy como Clash o Shadowsocks, verifica su archivo de configuración (por ejemplo, `~/.config/clash/config.yaml`) para confirmar que esté configurado para usar `127.0.0.1:7891` para SOCKS5.
  - Asegúrate de que la herramienta esté ejecutándose y sea accesible.

- **Probar la Conectividad del Proxy**
  - Prueba el proxy con una herramienta como `curl` (requiere `curl` compilado con soporte SOCKS):
    ```bash
    curl --socks5 127.0.0.1:7891 https://api.deepseek.com
    ```
  - Si esto falla, el servidor proxy no está funcionando o está mal configurado.

- **Registrar el Uso del Proxy**
   - Añade registro a tu script para confirmar qué proxy se está usando:
     ```python
     import logging
     logging.basicConfig(level=logging.DEBUG)
     ```

### Solución Recomendada

Si no necesitas el proxy, la solución más simple es deshabilitarlo anulando las variables de entorno y ejecutando:
```bash
HTTP_PROXY= HTTPS_PROXY= ALL_PROXY= python3 /home/lzwjava/bin/gitmessageai.py
```

Si necesitas el proxy, instala `httpx-socks` y actualiza tu código para usar `SyncProxyTransport` como se mostró anteriormente.

### Referencias
- [Documentación de httpx](https://www.python-httpx.org/advanced/#proxy-support)
- [httpx-socks GitHub](https://github.com/romis2012/httpx-socks)
- [Documentación de la API de DeepSeek](https://platform.deepseek.com/docs)