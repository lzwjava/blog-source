---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Construyendo un Servidor Meteorológico MCP Básico
translated: true
type: note
---

### ¿Qué es el Model Context Protocol (MCP)?

El Model Context Protocol (MCP) es un estándar abierto que define cómo las aplicaciones y los sistemas de IA (como los modelos de lenguaje grandes) intercambian contexto, como herramientas, recursos y prompts. Permite una integración perfecta entre los LLMs (por ejemplo, Claude) y servicios externos, facilitando la creación de agentes de IA extensibles. Esta guía se centra en configurar un servidor MCP básico usando Python plano (sin `uv`), basado en el tutorial de inicio rápido oficial para un servidor meteorológico simple que se conecta a la API del National Weather Service. Este servidor expone dos herramientas: `get_alerts` (para alertas meteorológicas por estado) y `get_forecast` (para pronósticos por ubicación).

### Prerrequisitos
- Conocimiento básico de Python y LLMs (por ejemplo, Claude).
- Python 3.10 o superior instalado.
- Acceso a una terminal (se recomienda macOS/Linux; las instrucciones para Windows son similares pero usan PowerShell).
- Para pruebas: la aplicación Claude for Desktop (disponible para macOS/Windows; no para Linux—use un cliente personalizado si es necesario).
- Nota: Los servidores MCP se comunican via JSON-RPC sobre stdio (stdin/stdout). Evite imprimir a stdout en su código para evitar la corrupción de mensajes; use logging a stderr en su lugar.

### Paso 1: Configurar su entorno
1. Cree un nuevo directorio de proyecto:
   ```
   mkdir weather
   cd weather
   ```

2. Cree y active un entorno virtual:
   ```
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```

3. Actualice pip (recomendado para confiabilidad):
   ```
   python -m pip install --upgrade pip
   ```

4. Instale las dependencias (MCP SDK y cliente HTTP):
   ```
   pip install "mcp[cli]" httpx
   ```

5. Cree el archivo del servidor:
   ```
   touch weather.py  # O use su editor para crearlo
   ```

### Paso 2: Construir el servidor MCP
Abra `weather.py` en su editor y agregue el siguiente código. Esto usa la clase `FastMCP` del MCP SDK, que genera automáticamente esquemas de herramientas a partir de hints de tipo y docstrings.

```python
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Inicializar el servidor MCP
mcp = FastMCP("weather")

# Constantes para la API del National Weather Service
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

async def make_nws_request(url: str) -> dict[str, Any] | None:
    """Hacer una solicitud a la API NWS con manejo adecuado de errores."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

def format_alert(feature: dict) -> str:
    """Formatear una característica de alerta en una cadena legible."""
    props = feature["properties"]
    return f"""
Evento: {props.get('event', 'Desconocido')}
Área: {props.get('areaDesc', 'Desconocida')}
Gravedad: {props.get('severity', 'Desconocida')}
Descripción: {props.get('description', 'No hay descripción disponible')}
Instrucciones: {props.get('instruction', 'No se proporcionaron instrucciones específicas')}
"""

@mcp.tool()
async def get_alerts(state: str) -> str:
    """Obtener alertas meteorológicas para un estado de EE. UU.

    Args:
        state: Código de estado de EE. UU. de dos letras (por ejemplo, CA, NY)
    """
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = await make_nws_request(url)

    if not data or "features" not in data:
        return "No se pueden obtener las alertas o no se encontraron alertas."

    if not data["features"]:
        return "No hay alertas activas para este estado."

    alerts = [format_alert(feature) for feature in data["features"]]
    return "\n---\n".join(alerts)

@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    """Obtener el pronóstico del tiempo para una ubicación.

    Args:
        latitude: Latitud de la ubicación
        longitude: Longitud de la ubicación
    """
    # Primero obtener el endpoint de la cuadrícula de pronóstico
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = await make_nws_request(points_url)

    if not points_data:
        return "No se pueden obtener los datos del pronóstico para esta ubicación."

    # Obtener la URL del pronóstico de la respuesta points
    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_nws_request(forecast_url)

    if not forecast_data:
        return "No se puede obtener el pronóstico detallado."

    # Formatear los periodos en un pronóstico legible
    periods = forecast_data["properties"]["periods"]
    forecasts = []
    for period in periods[:5]:  # Solo mostrar los próximos 5 periodos
        forecast = f"""
{period['name']}:
Temperatura: {period['temperature']}°{period['temperatureUnit']}
Viento: {period['windSpeed']} {period['windDirection']}
Pronóstico: {period['detailedForecast']}
"""
        forecasts.append(forecast)

    return "\n---\n".join(forecasts)

def main():
    # Ejecutar el servidor sobre stdio
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
```

- **Notas clave**:
  - Las herramientas se definen con decoradores `@mcp.tool()`. El host LLM (por ejemplo, Claude) las llamará según las consultas del usuario.
  - Este ejemplo utiliza funciones asíncronas para las llamadas API.
  - El manejo de errores garantiza fallos elegantes (por ejemplo, la falta de datos devuelve un mensaje amigable para el usuario).
  - Para producción, agregue logging (por ejemplo, a través del módulo `logging` a stderr) y limitación de tasa.

### Paso 3: Probar el servidor localmente
Ejecute el servidor:
```
python weather.py
```
Debería comenzar a escuchar en stdio sin salida (eso es normal). Para probar manualmente, necesitaría un cliente MCP, pero proceda a la integración para una prueba completa.

### Paso 4: Conectarse a un host (por ejemplo, Claude for Desktop)
1. Descargue e instale Claude for Desktop desde [claude.ai/download](https://claude.ai/download).

2. Configure la aplicación creando/editando `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) o el equivalente en Windows (`%APPDATA%\Claude\claude_desktop_config.json`):
   ```json
   {
     "mcpServers": {
       "weather": {
         "command": "python",
         "args": [
           "/RUTA/ABSOLUTA/A/weather/weather.py"  // Reemplace con la ruta de su proyecto (use pwd para encontrarla)
         ],
         "cwd": "/RUTA/ABSOLUTA/A/weather"  // Opcional: Establecer el directorio de trabajo si es necesario
       }
     }
   }
   ```
   - Use rutas absolutas (por ejemplo, `/Users/sunombre/weather/weather.py` en macOS).
   - En Windows, use barras diagonales `/` o dobles barras invertidas `\\`.
   - Asegúrese de que su entorno virtual esté activado cuando pruebe localmente, pero para Claude, este ejecuta el ejecutable de Python de su sistema (asegúrese de que los site-packages del venv sean accesibles o instale globalmente si lo prefiere—aunque se recomienda el venv).
   - Encuentre la ruta de Python con `which python` (macOS/Linux) o `where python` (Windows).

3. Reinicie completamente Claude for Desktop (cierre completamente, por ejemplo, Cmd+Q en macOS).

4. Pruebe en Claude:
   - Abra Claude y haga clic en el icono "Search and tools" (icono del control deslizante).
   - Debería ver `get_alerts` y `get_forecast` listados.
   - Ejemplos de consulta:
     - "¿Cuáles son las alertas meteorológicas activas en California?"
     - "¿Cuál es el pronóstico del tiempo para latitud 37.77, longitud -122.41?" (coordenadas de San Francisco).
   - Claude invocará las herramientas automáticamente e incorporará los resultados en su respuesta.
   - Nota: Esta API solo admite ubicaciones de EE. UU.

### Resolución de problemas
- **El servidor no aparece en Claude**: Verifique la sintaxis JSON, las rutas absolutas y el reinicio completo de la aplicación. Revise los registros en `~/Library/Logs/Claude/mcp*.log`.
- **Errores de herramientas**: Asegúrese de que el servidor se ejecute sin errores localmente. Agregue retardos para los límites de tasa de la API si es necesario.
- **Consultas fuera de EE. UU.**: La API NWS es solo para EE. UU.; extiéndala con otras API para soporte global.
- Para características avanzadas (recursos, prompts, notificaciones), consulte la documentación completa de MCP.

Esto configura un servidor MCP funcional usando Python plano. Para alternativas en TypeScript/Node.js o más ejemplos, consulte los recursos a continuación.

### Referencias
- [Build an MCP Server (Documentación Oficial)](https://modelcontextprotocol.io/docs/develop/build-server)
- [MCP Quickstart Guide](https://modelcontextprotocol.info/docs/quickstart/quickstart/)
- [Model Context Protocol Guide with Demo](https://www.datacamp.com/tutorial/mcp-model-context-protocol)
- [How the Model Context Protocol Works](https://www.freecodecamp.org/news/how-the-model-context-protocol-works/)
- [Practical Introduction to MCP](https://medium.com/@davidlfliang/guide-a-practical-introduction-to-model-context-protocol-mcp-2f63b636f510)