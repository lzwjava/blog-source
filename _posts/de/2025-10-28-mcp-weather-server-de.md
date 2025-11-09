---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Aufbau eines grundlegenden MCP-Wetter-Servers
translated: true
type: note
---

### Was ist das Model Context Protocol (MCP)?

Das Model Context Protocol (MCP) ist ein offener Standard, der definiert, wie Anwendungen und KI-Systeme (wie große Sprachmodelle) Kontext austauschen, beispielsweise Tools, Ressourcen und Prompts. Es ermöglicht eine nahtlose Integration zwischen LLMs (z.B. Claude) und externen Diensten und erleichtert so den Bau erweiterbarer KI-Agenten. Diese Anleitung konzentriert sich auf die Einrichtung eines grundlegenden MCP-Servers mit reinem Python (ohne `uv`), basierend auf dem offiziellen Quickstart-Tutorial für einen einfachen Wetterserver, der eine Verbindung zur National Weather Service API herstellt. Dieser Server stellt zwei Tools zur Verfügung: `get_alerts` (für Wetterwarnungen des Bundesstaates) und `get_forecast` (für Standortvorhersagen).

### Voraussetzungen
- Grundlegende Kenntnisse in Python und LLMs (z.B. Claude).
- Python 3.10 oder höher installiert.
- Zugang zu einem Terminal (macOS/Linux empfohlen; Windows-Anweisungen ähnlich, aber PowerShell verwenden).
- Zum Testen: Claude for Desktop App (verfügbar für macOS/Windows; nicht für Linux – ggf. einen benutzerdefinierten Client verwenden).
- Hinweis: MCP-Server kommunizieren via JSON-RPC über stdio (stdin/stdout). Vermeiden Sie das Drucken auf stdout in Ihrem Code, um eine Beschädigung der Nachrichten zu verhindern; verwenden Sie stattdessen logging nach stderr.

### Schritt 1: Richten Sie Ihre Umgebung ein
1. Erstellen Sie ein neues Projektverzeichnis:
   ```
   mkdir weather
   cd weather
   ```

2. Erstellen und aktivieren Sie eine virtuelle Umgebung:
   ```
   python -m venv .venv
   source .venv/bin/activate  # Unter Windows: .venv\Scripts\activate
   ```

3. Führen Sie ein Upgrade von pip durch (für Zuverlässigkeit empfohlen):
   ```
   python -m pip install --upgrade pip
   ```

4. Installieren Sie die Abhängigkeiten (MCP SDK und HTTP-Client):
   ```
   pip install "mcp[cli]" httpx
   ```

5. Erstellen Sie die Server-Datei:
   ```
   touch weather.py  # Oder verwenden Sie Ihren Editor, um sie zu erstellen
   ```

### Schritt 2: Bauen Sie den MCP-Server
Öffnen Sie `weather.py` in Ihrem Editor und fügen Sie den folgenden Code hinzu. Dies verwendet die `FastMCP`-Klasse aus dem MCP SDK, die Tool-Schemata automatisch aus Type Hints und Docstrings generiert.

```python
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialisiere den MCP-Server
mcp = FastMCP("weather")

# Konstanten für die National Weather Service API
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

async def make_nws_request(url: str) -> dict[str, Any] | None:
    """Mache eine Anfrage an die NWS API mit ordnungsgemäßer Fehlerbehandlung."""
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
    """Formatiere eine Warnungs-Feature in einen lesbaren String."""
    props = feature["properties"]
    return f"""
Ereignis: {props.get('event', 'Unbekannt')}
Gebiet: {props.get('areaDesc', 'Unbekannt')}
Schweregrad: {props.get('severity', 'Unbekannt')}
Beschreibung: {props.get('description', 'Keine Beschreibung verfügbar')}
Anweisungen: {props.get('instruction', 'Keine spezifischen Anweisungen vorhanden')}
"""

@mcp.tool()
async def get_alerts(state: str) -> str:
    """Hole Wetterwarnungen für einen US-Bundesstaat.

    Args:
        state: Zwei-Buchstaben-Code des US-Bundesstaates (z.B. CA, NY)
    """
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = await make_nws_request(url)

    if not data or "features" not in data:
        return "Warnungen konnten nicht abgerufen werden oder es wurden keine Warnungen gefunden."

    if not data["features"]:
        return "Keine aktiven Warnungen für diesen Bundesstaat."

    alerts = [format_alert(feature) for feature in data["features"]]
    return "\n---\n".join(alerts)

@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    """Hole die Wettervorhersage für einen Standort.

    Args:
        latitude: Breitengrad des Standorts
        longitude: Längengrad des Standorts
    """
    # Zuerst den Forecast Grid Endpunkt holen
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = await make_nws_request(points_url)

    if not points_data:
        return "Vorhersagedaten für diesen Standort konnten nicht abgerufen werden."

    # Hole die Forecast-URL aus der Points-Antwort
    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_nws_request(forecast_url)

    if not forecast_data:
        return "Detaillierte Vorhersage konnte nicht abgerufen werden."

    # Formatiere die Perioden in eine lesbare Vorhersage
    periods = forecast_data["properties"]["periods"]
    forecasts = []
    for period in periods[:5]:  # Zeige nur die nächsten 5 Perioden an
        forecast = f"""
{period['name']}:
Temperatur: {period['temperature']}°{period['temperatureUnit']}
Wind: {period['windSpeed']} {period['windDirection']}
Vorhersage: {period['detailedForecast']}
"""
        forecasts.append(forecast)

    return "\n---\n".join(forecasts)

def main():
    # Starte den Server über stdio
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
```

- **Wichtige Hinweise**:
  - Tools werden mit `@mcp.tool()`-Dekoratoren definiert. Der LLM-Host (z.B. Claude) ruft sie basierend auf Benutzeranfragen auf.
  - Dieses Beispiel verwendet asynchrone Funktionen für API-Aufrufe.
  - Die Fehlerbehandlung stellt einen sanften Fehlerfall sicher (z.B. gibt es bei fehlenden Daten eine benutzerfreundliche Meldung zurück).
  - Für die Produktion sollten Logging (z.B. über das `logging`-Modul nach stderr) und Ratenbegrenzung hinzugefügt werden.

### Schritt 3: Testen Sie den Server lokal
Starten Sie den Server:
```
python weather.py
```
Er sollte ohne Ausgabe auf stdio lauschen (das ist normal). Zum manuellen Testen bräuchten Sie einen MCP-Client, fahren Sie für den vollständigen Test mit der Integration fort.

### Schritt 4: Verbindung zu einem Host herstellen (z.B. Claude for Desktop)
1. Laden Sie Claude for Desktop von [claude.ai/download](https://claude.ai/download) herunter und installieren Sie es.

2. Konfigurieren Sie die App, indem Sie `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) oder das Äquivalent unter Windows (`%APPDATA%\Claude\claude_desktop_config.json`) erstellen/bearbeiten:
   ```json
   {
     "mcpServers": {
       "weather": {
         "command": "python",
         "args": [
           "/ABSOLUTER/PFAD/ZU/weather/weather.py"  // Ersetzen Sie dies durch Ihren Projektpfad (verwenden Sie pwd, um ihn zu finden)
         ],
         "cwd": "/ABSOLUTER/PFAD/ZU/weather"  // Optional: Arbeitsverzeichnis setzen, falls benötigt
       }
     }
   }
   ```
   - Verwenden Sie absolute Pfade (z.B. `/Users/ihrname/weather/weather.py` auf macOS).
   - Unter Windows verwenden Sie Schrägstriche `/` oder doppelte Backslashes `\\`.
   - Stellen Sie sicher, dass Ihre virtuelle Umgebung aktiviert ist, wenn Sie lokal testen, aber für Claude wird die Python-Executable Ihres Systems ausgeführt (stellen Sie sicher, dass die site-packages des venv zugänglich sind oder installieren Sie global, wenn bevorzugt – venv wird jedoch empfohlen).
   - Finden Sie den Python-Pfad mit `which python` (macOS/Linux) oder `where python` (Windows).

3. Starten Sie Claude for Desktop vollständig neu (komplett beenden, z.B. Cmd+Q auf macOS).

4. Testen Sie in Claude:
   - Öffnen Sie Claude und klicken Sie auf das "Search and tools"-Symbol (Schieberegler-Symbol).
   - Sie sollten `get_alerts` und `get_forecast` aufgelistet sehen.
   - Beispielanfragen:
     - "Was sind die aktiven Wetterwarnungen in Kalifornien?"
     - "Wie ist die Wettervorhersage für den Breitengrad 37.77, Längengrad -122.41?" (San Francisco Koordinaten).
   - Claude wird die Tools automatisch aufrufen und die Ergebnisse in seine Antwort einbauen.
   - Hinweis: Diese API unterstützt nur US-Standorte.

### Problembehebung
- **Server erscheint nicht in Claude**: Überprüfen Sie die JSON-Syntax, absoluten Pfade und den vollständigen Neustart der App. Überprüfen Sie die Logs unter `~/Library/Logs/Claude/mcp*.log`.
- **Tool-Fehler**: Stellen Sie sicher, dass der Server lokal fehlerfrei läuft. Fügen Sie bei Bedarf Verzögerungen für API-Ratenbegrenzungen hinzu.
- **Nicht-US-Anfragen**: Die NWS API ist nur für die USA; erweitern Sie sie mit anderen APIs für globale Unterstützung.
- Für erweiterte Funktionen (Ressourcen, Prompts, Benachrichtigungen) siehe die vollständige MCP-Dokumentation.

Dies richtet einen funktionalen MCP-Server mit reinem Python ein. Für TypeScript/Node.js-Alternativen oder weitere Beispiele sehen Sie sich die folgenden Ressourcen an.

### Referenzen
- [Build an MCP Server (Official Docs)](https://modelcontextprotocol.io/docs/develop/build-server)
- [MCP Quickstart Guide](https://modelcontextprotocol.info/docs/quickstart/quickstart/)
- [Model Context Protocol Guide with Demo](https://www.datacamp.com/tutorial/mcp-model-context-protocol)
- [How the Model Context Protocol Works](https://www.freecodecamp.org/news/how-the-model-context-protocol-works/)
- [Practical Introduction to MCP](https://medium.com/@davidlfliang/guide-a-practical-introduction-to-model-context-protocol-mcp-2f63b636f510)