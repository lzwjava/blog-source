---
audio: false
generated: true
image: false
lang: es
layout: post
title: Sesiones HTTP persistentes con Python Requests
translated: true
type: note
---

Una `Session` en la biblioteca `requests` de Python es una forma de persistir ciertos parámetros, como cookies, headers y autenticación, a través de múltiples solicitudes HTTP. Proporciona una interfaz conveniente para realizar solicitudes repetidas al mismo servidor o endpoints relacionados, manteniendo el estado, mejorando la eficiencia y simplificando el código. A continuación, explicaré cómo funciona `requests.Session`, sus características clave y proporcionaré ejemplos para ilustrar su uso.

## ¿Qué es un `requests.Session`?

La biblioteca `requests` es ampliamente utilizada para realizar solicitudes HTTP en Python. Si bien puedes usar funciones independientes como `requests.get()` o `requests.post()`, un objeto `Session` te permite crear una sesión persistente que retiene configuraciones (por ejemplo, cookies, headers o credenciales de autenticación) a través de múltiples solicitudes. Esto es particularmente útil para interactuar con sitios web o APIs que requieren interacciones con estado, como mantener una sesión de inicio de sesión o reutilizar conexiones TCP.

Un objeto `Session`:
- Persiste las cookies entre solicitudes.
- Reutiliza las conexiones TCP subyacentes (mediante agrupación de conexiones) para un mejor rendimiento al realizar múltiples solicitudes al mismo host.
- Te permite establecer parámetros predeterminados (por ejemplo, headers, timeouts) que se aplican a todas las solicitudes realizadas con la sesión.
- Admite autenticación y configuraciones personalizadas.

## ¿Cómo funciona `Session`?

Cuando creas un objeto `Session`, actúa como un contenedor para tus solicitudes HTTP. Aquí tienes un desglose de cómo funciona:

1. **Cookies Persistentes**: Cuando realizas una solicitud con una `Session`, cualquier cookie establecida por el servidor (por ejemplo, cookies de sesión después de iniciar sesión) se almacena en la sesión y se envía automáticamente en solicitudes posteriores. Esto es clave para mantener el estado, como permanecer conectado.

2. **Agrupación de Conexiones**: Para solicitudes al mismo host, la `Session` reutiliza la misma conexión TCP, reduciendo la latencia y la sobrecarga en comparación con crear nuevas conexiones para cada solicitud.

3. **Parámetros Predeterminados**: Puedes establecer atributos como headers, autenticación o timeouts en el objeto `Session`, y se aplicarán a todas las solicitudes realizadas con esa sesión a menos que se anulen.

4. **Personalizable**: Puedes configurar proxies, verificación SSL o incluso montar adaptadores personalizados (por ejemplo, para reintentos o transporte personalizado) para controlar cómo se manejan las solicitudes.

## Uso Básico

Aquí tienes un ejemplo simple de cómo usar `requests.Session`:

```python
import requests

# Crear una sesión
session = requests.Session()

# Establecer headers predeterminados para todas las solicitudes en esta sesión
session.headers.update({'User-Agent': 'MyApp/1.0'})

# Hacer una solicitud GET
response1 = session.get('https://api.example.com/data')
print(response1.json())

# Hacer otra solicitud; las cookies y headers se reutilizan
response2 = session.post('https://api.example.com/submit', data={'key': 'value'})
print(response2.json())

# Cerrar la sesión para liberar recursos
session.close()
```

En este ejemplo:
- Se crea una `Session` y se establece un header `User-Agent` personalizado para todas las solicitudes.
- La sesión maneja las cookies automáticamente, por lo que si `response1` establece una cookie, se envía con `response2`.
- La sesión reutiliza la conexión a `api.example.com`, mejorando el rendimiento.

## Características Clave y Ejemplos

### 1. **Persistir Cookies**
Las sesiones son particularmente útiles para sitios web que usan cookies para mantener el estado, como las sesiones de inicio de sesión.

```python
import requests

# Crear una sesión
session = requests.Session()

# Iniciar sesión en un sitio web
login_data = {'username': 'user', 'password': 'pass'}
response = session.post('https://example.com/login', data=login_data)

# Acceder a una página protegida; la sesión envía automáticamente la cookie de inicio de sesión
protected_page = session.get('https://example.com/protected')
print(protected_page.text)

# Cerrar la sesión
session.close()
```

Aquí, la sesión almacena la cookie de autenticación de la solicitud de inicio de sesión y la envía con la solicitud posterior a la página protegida.

### 2. **Establecer Parámetros Predeterminados**
Puedes establecer headers predeterminados, autenticación u otros parámetros para todas las solicitudes en la sesión.

```python
import requests

session = requests.Session()

# Establecer headers predeterminados
session.headers.update({
    'Authorization': 'Bearer my_token',
    'Accept': 'application/json'
})

# Establecer timeout predeterminado
session.request = functools.partial(session.request, timeout=5)

# Hacer solicitudes; los headers y el timeout se aplican automáticamente
response1 = session.get('https://api.example.com/endpoint1')
response2 = session.get('https://api.example.com/endpoint2')

session.close()
```

### 3. **Agrupación de Conexiones**
Al realizar múltiples solicitudes al mismo host, `Session` reutiliza las conexiones, lo que es más eficiente que las solicitudes independientes.

```python
import requests
import time

# Sin sesión
start = time.time()
for _ in range(5):
    requests.get('https://api.example.com/data')
print(f"Sin sesión: {time.time() - start} segundos")

# Con sesión
session = requests.Session()
start = time.time()
for _ in range(5):
    session.get('https://api.example.com/data')
print(f"Con sesión: {time.time() - start} segundos")
session.close()
```

Las solicitudes basadas en sesión suelen ser más rápidas porque reutilizan la conexión TCP.

### 4. **Autenticación**
Las sesiones simplifican el manejo de la autenticación, como HTTP Basic Auth o autenticación personalizada basada en tokens.

```python
import requests
from requests.auth import HTTPBasicAuth

session = requests.Session()
session.auth = HTTPBasicAuth('user', 'pass')

# Todas las solicitudes incluirán Basic Auth
response = session.get('https://api.example.com/protected')
print(response.json())

session.close()
```

### 5. **Adaptadores Personalizados**
Puedes montar adaptadores personalizados para controlar cosas como reintentos o el comportamiento de la agrupación de conexiones.

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()

# Configurar reintentos
retries = Retry(total=3, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
session.mount('https://', HTTPAdapter(max_retries=retries))

# Hacer una solicitud con lógica de reintento
response = session.get('https://api.example.com/unstable_endpoint')
print(response.json())

session.close()
```

Este ejemplo configura reintentos automáticos para códigos de error HTTP específicos.

## Cuándo Usar `Session`

Usa `requests.Session` cuando:
- Necesites mantener el estado (por ejemplo, cookies) a través de múltiples solicitudes, como para autenticación.
- Estés realizando múltiples solicitudes al mismo host y quieras beneficiarte de la agrupación de conexiones.
- Quieras aplicar configuraciones consistentes (headers, timeouts, etc.) en todas las solicitudes.
- Estés interactuando con APIs o sitios web que requieran interacciones basadas en sesión.

Si estás haciendo una sola solicitud o no necesitas persistir el estado, `requests.get()` o `requests.post()` independientes son suficientes.

## Cerrar una Sesión

Siempre cierra una sesión cuando hayas terminado para liberar recursos (por ejemplo, conexiones):

```python
session.close()
```

Alternativamente, usa una sesión como administrador de contexto para asegurarte de que se cierre automáticamente:

```python
with requests.Session() as session:
    session.headers.update({'User-Agent': 'MyApp/1.0'})
    response = session.get('https://api.example.com/data')
    print(response.json())
# La sesión se cierra automáticamente cuando sale del bloque
```

## Notas Avanzadas
- **Seguridad en Hilos**: Los objetos `Session` no son seguros para hilos. Si estás usando múltiples hilos, crea una `Session` separada para cada hilo.
- **Proxies**: Puedes establecer proxies en una sesión con `session.proxies = {'http': 'http://proxy.com', 'https': 'https://proxy.com'}`.
- **Verificación SSL**: Por defecto, `Session` verifica los certificados SSL. Para desactivarlo (no recomendado para producción), usa `session.verify = False`.

## Referencias
[Requests Documentation](https://requests.readthedocs.io/en/latest/)  
[Requests Session Objects](https://requests.readthedocs.io/en/latest/user/advanced/#session-objects)