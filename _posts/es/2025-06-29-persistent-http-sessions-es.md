---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Uso de requests.Session para sesiones HTTP persistentes
translated: true
type: note
---

### Cómo funciona requests.Session

En la biblioteca `requests` de Python, `requests.Session` es una clase que te permite mantener una sesión persistente a través de múltiples solicitudes HTTP. Ofrece varios beneficios sobre hacer llamadas individuales como `requests.get()`:

- **Persistencia de cookies**: Por defecto, almacena y envía automáticamente las cookies recibidas del servidor en solicitudes posteriores. Esto permite interacciones basadas en sesión, como iniciar sesión una vez y mantener la autenticación.
- **Connection pooling**: Reutiliza las conexiones TCP subyacentes para el mismo host, mejorando el rendimiento al evitar la sobrecarga de establecer nuevas conexiones.
- **Configuraciones compartidas**: Puedes establecer cabeceras por defecto, autenticación, proxies u otros parámetros que se aplican a todas las solicitudes dentro de la sesión.
- **Detalles internos**: Utiliza la biblioteca `urllib3` para el manejo HTTP. Cuando creas una `Session`, inicializa atributos como `cookies` (una instancia de `RequestsCookieJar`), `headers`, y más. Por ejemplo, las cookies de una respuesta se incluyen automáticamente en la siguiente solicitud al mismo dominio.

Aquí hay un ejemplo básico de cómo crear y usar una sesión:

```python
import requests

# Crear una sesión
session = requests.Session()

# Establecer una cabecera por defecto para todas las solicitudes en esta sesión
session.headers.update({'User-Agent': 'MyApp/1.0'})

# Hacer múltiples solicitudes, compartiendo la sesión
response1 = session.get('https://example.com/login')
response2 = session.post('https://example.com/data', data={'key': 'value'})

# Acceder a las cookies almacenadas en la sesión
print(session.cookies)
```

Esto asegura que las cookies (como los IDs de sesión) se manejen de forma transparente sin intervención manual.

### Usar Python para llamar a APIs de proyectos Java/Spring

Para interactuar con APIs construidas usando Java/Spring (típicamente endpoints RESTful a través de Spring MVC o Spring Boot), usas `requests.Session` igual que con cualquier API HTTP. Los proyectos Spring a menudo exponen APIs sobre HTTP/HTTPS, y `requests` puede manejar autenticación, tokens CSRF o limitación de tasa si están implementados.

- **Autenticación**: Spring podría usar Spring Security con formularios, JWT u OAuth. Para autenticación basada en sesión (por ejemplo, a través de formularios de inicio de sesión), `requests.Session` automatiza el manejo de cookies después de una solicitud de login.
- **Realizar llamadas**: Usa métodos HTTP estándar como `GET`, `POST`, etc. Si la API de Spring requiere cargas útiles JSON, pasa `json=tus_datos`.

Ejemplo de inicio de sesión en una API autenticada con Spring y llamada a otro endpoint:

```python
import requests

session = requests.Session()

# Iniciar sesión (asumiendo un POST a /login con usuario/contraseña)
login_payload = {'username': 'user', 'password': 'pass'}
response = session.post('https://spring-api.example.com/login', data=login_payload)

if response.ok:
    # Ahora llamar a otro endpoint de la API, las cookies de sesión persisten
    data_response = session.get('https://spring-api.example.com/api/data')
    print(data_response.json())
else:
    print("Login failed")
```

Las APIs de Spring son sin estado por defecto pero pueden gestionar sesiones mediante almacenamiento en el servidor (por ejemplo, en Tomcat o servidores embebidos). Asegúrate de que tu cliente Python maneje cualquier CORS, CSRF o cabeceras personalizadas requeridas por Spring.

### Relación con JSESSIONID en el lado Java/Spring

- **¿Qué es JSESSIONID?**: En aplicaciones web Java (incluyendo Spring, que a menudo se ejecuta en contenedores Servlet como Tomcat), JSESSIONID es una cookie HTTP estándar utilizada por el contenedor para rastrear sesiones de usuario. Se establece cuando se crea una sesión (por ejemplo, después del inicio de sesión) y se envía de vuelta en las respuestas. En el lado del cliente, los navegadores (o clientes HTTP como `requests`) la incluyen en solicitudes posteriores para mantener el estado, como la autenticación del usuario o los datos del carrito de compras.
- **Cómo se relaciona con requests.Session**: `requests.Session` trata a JSESSIONID como cualquier otra cookie: la almacena automáticamente desde la cabecera "Set-Cookie" del servidor y la incluye en la cabecera "Cookie" de las solicitudes futuras. Esto permite una interacción fluida con las APIs stateful de Spring sin tener que analizar/extraer cookies manualmente.
- **Manejo en el servidor**: En el lado Java/Spring, el ServletContext gestiona las sesiones. Cuando tu cliente Python envía una solicitud con JSESSIONID, HttpSession de Spring recupera los datos asociados en el servidor. Si ha expirado o no es válida, Spring podría requerir una re-autenticación. Para sesiones seguras, asegúrate de que tu configuración use HTTPS, ya que JSESSIONID puede ser vulnerable al robo sobre HTTP.
- **Problemas potenciales**: Si Spring aplica tokens CSRF u otras protecciones, es posible que necesites extraerlos e incluirlos (por ejemplo, desde campos de formulario ocultos). Para APIs de Spring sin estado basadas en JWT, `requests.Session` aún ayuda al persistir tokens de autenticación en las cabeceras, pero JSESSIONID se vuelve menos relevante.

Si encuentras errores específicos (por ejemplo, 401 No autorizado) al llamar a una API de Spring, revisa los registros de red en busca de problemas con las cookies o habilita la depuración de `requests` con `import logging; logging.basicConfig(level=logging.DEBUG)`. Para más información sobre Spring Security, consulta su documentación oficial.