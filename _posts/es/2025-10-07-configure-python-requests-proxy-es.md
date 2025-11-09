---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Configurar Proxy de Python Requests Mediante .env
translated: true
type: note
---

### Uso de un archivo `.env` para configurar proxies HTTP/HTTPS para Python Requests

La biblioteca `requests` en Python respeta automáticamente las variables de entorno estándar como `HTTP_PROXY` y `HTTPS_PROXY` para la configuración del proxy. Para gestionarlas de forma segura (por ejemplo, sin codificarlas directamente en tu script), puedes almacenarlas en un archivo `.env` y cargarlas usando la biblioteca `python-dotenv`. Esto mantiene los detalles sensibles del proxy fuera de tu código.

#### Paso 1: Instalar los Paquetes Requeridos
Necesitarás `requests` (si aún no está instalada) y `python-dotenv` para cargar el archivo `.env`.

```bash
pip install requests python-dotenv
```

#### Paso 2: Crear un archivo `.env`
En la raíz de tu proyecto, crea un archivo llamado `.env` (sin extensión) y añade tu configuración de proxy. Usa el formato `http://` o `https://` para la URL del proxy, incluyendo el nombre de usuario y contraseña si es necesario.

Contenido de ejemplo del archivo `.env`:
```
HTTP_PROXY=http://username:password@proxy-host:port
HTTPS_PROXY=https://username:password@proxy-host:port
NO_PROXY=localhost,127.0.0.1,example.com  # Opcional: Excluir dominios del proxy
```

- `HTTP_PROXY`: Para tráfico HTTP.
- `HTTPS_PROXY`: Para tráfico HTTPS (a menudo es el mismo que HTTP_PROXY).
- `NO_PROXY`: Lista separada por comas de hosts/IPs para excluir del proxy.
- Nota: Las variables de entorno no distinguen entre mayúsculas y minúsculas, pero es convencional usar mayúsculas.

Añade `.env` a tu archivo `.gitignore` para evitar subir información sensible.

#### Paso 3: Cargar el archivo `.env` en tu Script de Python
Al principio de tu script, carga las variables de entorno:

```python
from dotenv import load_dotenv
import requests

# Carga las variables desde el archivo .env
load_dotenv()  # Busca .env en el directorio actual por defecto

# Ahora realiza una petición – los proxies se aplican automáticamente
response = requests.get('https://httpbin.org/ip')
print(response.json())
```

- `load_dotenv()` lee el archivo `.env` y establece las variables en `os.environ`.
- `requests` detectará `HTTP_PROXY`/`HTTPS_PROXY` automáticamente—no es necesario pasar un diccionario `proxies` a menos que quieras anularlos.

#### Paso 4: Verificar el Uso del Proxy (Opcional)
Para confirmar que los proxies están funcionando, prueba con un servicio como httpbin.org:

```python
import requests
from dotenv import load_dotenv

load_dotenv()

proxies = requests.utils.get_environ_proxies('https://httpbin.org/ip')  # Inspecciona los proxies cargados
print("Proxies cargados:", proxies)

response = requests.get('https://httpbin.org/ip')
print("Tu IP a través del proxy:", response.json())
```

Esto debería mostrar la IP del servidor proxy si está configurado correctamente.

#### Problemas Comunes y Consejos
- **Autenticación del Proxy**: Incluye `username:password@` en la URL si es necesario.
- **Proxies SOCKS**: Usa el prefijo `socks5://` (requiere el extra `requests[socks]`: `pip install requests[socks]`).
- **Anulación por Petición**: Si necesitas proxies diferentes para una llamada específica, pasa un diccionario:
  ```python:disable-run
  proxies = {'http': 'http://custom-proxy:port', 'https': 'https://custom-proxy:port'}
  response = requests.get('url', proxies=proxies)
  ```
- **Entorno**: Funciona en Windows/Linux/macOS. En Windows, usa `set` en cmd o sus equivalentes en PowerShell.
- **Seguridad**: Nunca subas `.env` al control de versiones.

Esta configuración es simple, segura y sigue las mejores prácticas para la configuración basada en entorno.

[Documentación de Requests: Proxies](https://requests.readthedocs.io/en/latest/user/advanced/#proxies)  
[Documentación de python-dotenv](https://github.com/theskumar/python-dotenv)