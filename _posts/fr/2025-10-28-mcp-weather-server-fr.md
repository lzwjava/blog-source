---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Construction d'un Serveur Météo MCP de Base
translated: true
type: note
---

### Qu'est-ce que le Model Context Protocol (MCP) ?

Le Model Context Protocol (MCP) est un standard ouvert qui définit comment les applications et les systèmes d'IA (comme les grands modèles de langage) échangent du contexte, tel que des outils, des ressources et des invites. Il permet une intégration transparente entre les LLM (par exemple, Claude) et les services externes, facilitant ainsi la création d'agents IA extensibles. Ce guide se concentre sur la configuration d'un serveur MCP de base en utilisant Python pur (sans `uv`), basé sur le tutoriel de démarrage officiel pour un serveur météo simple qui se connecte à l'API du National Weather Service. Ce serveur expose deux outils : `get_alerts` (pour les alertes météorologiques par état) et `get_forecast` (pour les prévisions par localisation).

### Prérequis
- Connaissance basique de Python et des LLM (par exemple, Claude).
- Python 3.10 ou une version supérieure installé.
- Accès à un terminal (macOS/Linux recommandé ; instructions similaires pour Windows mais utilisez PowerShell).
- Pour les tests : application Claude pour Desktop (disponible pour macOS/Windows ; pas pour Linux — utilisez un client personnalisé si nécessaire).
- Note : Les serveurs MCP communiquent via JSON-RPC sur stdio (stdin/stdout). Évitez d'écrire sur stdout dans votre code pour éviter la corruption des messages ; utilisez plutôt la journalisation vers stderr.

### Étape 1 : Configurer votre environnement
1. Créez un nouveau répertoire de projet :
   ```
   mkdir weather
   cd weather
   ```

2. Créez et activez un environnement virtuel :
   ```
   python -m venv .venv
   source .venv/bin/activate  # Sur Windows : .venv\Scripts\activate
   ```

3. Mettez à niveau pip (recommandé pour la fiabilité) :
   ```
   python -m pip install --upgrade pip
   ```

4. Installez les dépendances (SDK MCP et client HTTP) :
   ```
   pip install "mcp[cli]" httpx
   ```

5. Créez le fichier du serveur :
   ```
   touch weather.py  # Ou utilisez votre éditeur pour le créer
   ```

### Étape 2 : Construire le serveur MCP
Ouvrez `weather.py` dans votre éditeur et ajoutez le code suivant. Celui-ci utilise la classe `FastMCP` du SDK MCP, qui génère automatiquement les schémas d'outils à partir des indications de type et des docstrings.

```python
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialiser le serveur MCP
mcp = FastMCP("weather")

# Constantes pour l'API du National Weather Service
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

async def make_nws_request(url: str) -> dict[str, Any] | None:
    """Effectue une requête vers l'API NWS avec une gestion d'erreur appropriée."""
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
    """Formate une fonctionnalité d'alerte en une chaîne lisible."""
    props = feature["properties"]
    return f"""
Événement : {props.get('event', 'Inconnu')}
Zone : {props.get('areaDesc', 'Inconnue')}
Sévérité : {props.get('severity', 'Inconnue')}
Description : {props.get('description', 'Aucune description disponible')}
Instructions : {props.get('instruction', 'Aucune instruction spécifique fournie')}
"""

@mcp.tool()
async def get_alerts(state: str) -> str:
    """Obtient les alertes météorologiques pour un état des États-Unis.

    Args:
        state: Code d'état américain à deux lettres (par exemple CA, NY)
    """
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = await make_nws_request(url)

    if not data or "features" not in data:
        return "Impossible de récupérer les alertes ou aucune alerte trouvée."

    if not data["features"]:
        return "Aucune alerte active pour cet état."

    alerts = [format_alert(feature) for feature in data["features"]]
    return "\n---\n".join(alerts)

@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    """Obtient les prévisions météorologiques pour un lieu.

    Args:
        latitude: Latitude du lieu
        longitude: Longitude du lieu
    """
    # D'abord, obtenir le point de terminaison de la grille de prévision
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = await make_nws_request(points_url)

    if not points_data:
        return "Impossible de récupérer les données de prévision pour ce lieu."

    # Obtenir l'URL de prévision à partir de la réponse points
    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_nws_request(forecast_url)

    if not forecast_data:
        return "Impossible de récupérer les prévisions détaillées."

    # Formater les périodes en une prévision lisible
    periods = forecast_data["properties"]["periods"]
    forecasts = []
    for period in periods[:5]:  # Afficher seulement les 5 prochaines périodes
        forecast = f"""
{period['name']} :
Température : {period['temperature']}°{period['temperatureUnit']}
Vent : {period['windSpeed']} {period['windDirection']}
Prévision : {period['detailedForecast']}
"""
        forecasts.append(forecast)

    return "\n---\n".join(forecasts)

def main():
    # Exécuter le serveur sur stdio
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
```

- **Notes clés** :
  - Les outils sont définis avec les décorateurs `@mcp.tool()`. L'hôte LLM (par exemple, Claude) les appellera en fonction des requêtes de l'utilisateur.
  - Cet exemple utilise des fonctions asynchrones pour les appels d'API.
  - La gestion des erreurs assure des échecs gracieux (par exemple, l'absence de données retourne un message convivial).
  - Pour la production, ajoutez la journalisation (par exemple, via le module `logging` vers stderr) et la limitation du débit.

### Étape 3 : Tester le serveur localement
Exécutez le serveur :
```
python weather.py
```
Il devrait commencer à écouter sur stdio sans sortie (c'est normal). Pour tester manuellement, vous auriez besoin d'un client MCP, mais passez à l'intégration pour un test complet.

### Étape 4 : Se connecter à un hôte (par exemple, Claude pour Desktop)
1. Téléchargez et installez Claude pour Desktop depuis [claude.ai/download](https://claude.ai/download).

2. Configurez l'application en créant/modifiant `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) ou l'équivalent sur Windows (`%APPDATA%\Claude\claude_desktop_config.json`) :
   ```json
   {
     "mcpServers": {
       "weather": {
         "command": "python",
         "args": [
           "/CHEMIN/ABSOLU/VERS/weather/weather.py"  // Remplacez par le chemin de votre projet (utilisez pwd pour le trouver)
         ],
         "cwd": "/CHEMIN/ABSOLU/VERS/weather"  // Optionnel : Définir le répertoire de travail si nécessaire
       }
     }
   }
   ```
   - Utilisez des chemins absolus (par exemple, `/Users/votrenom/weather/weather.py` sur macOS).
   - Sur Windows, utilisez des barres obliques `/` ou des doubles barres obliques inverses `\\`.
   - Assurez-vous que votre environnement virtuel est activé lors des tests locaux, mais pour Claude, il exécute l'exécutable Python de votre système (assurez-vous que les site-packages du venv sont accessibles ou installez globalement si vous préférez — bien que le venv soit recommandé).
   - Trouvez le chemin de Python avec `which python` (macOS/Linux) ou `where python` (Windows).

3. Redémarrez complètement Claude pour Desktop (quittez complètement, par exemple, Cmd+Q sur macOS).

4. Testez dans Claude :
   - Ouvrez Claude et cliquez sur l'icône "Recherche et outils" (icône de curseur).
   - Vous devriez voir `get_alerts` et `get_forecast` listés.
   - Exemples de requêtes :
     - "Quelles sont les alertes météorologiques actives en Californie ?"
     - "Quelles sont les prévisions météo pour la latitude 37.77, la longitude -122.41 ?" (coordonnées de San Francisco).
   - Claude invoquera les outils automatiquement et incorporera les résultats dans sa réponse.
   - Note : Cette API ne prend en charge que les localisations aux États-Unis.

### Dépannage
- **Le serveur n'apparaît pas dans Claude** : Vérifiez la syntaxe JSON, les chemins absolus et le redémarrage complet de l'application. Vérifiez les journaux dans `~/Library/Logs/Claude/mcp*.log`.
- **Erreurs d'outil** : Assurez-vous que le serveur s'exécute sans erreur localement. Ajoutez des délais pour les limites de débit de l'API si nécessaire.
- **Requêtes en dehors des États-Unis** : L'API NWS est réservée aux États-Unis ; étendez avec d'autres API pour une prise en charge globale.
- Pour les fonctionnalités avancées (ressources, invites, notifications), consultez la documentation complète du MCP.

Ceci configure un serveur MCP fonctionnel en utilisant Python pur. Pour les alternatives TypeScript/Node.js ou plus d'exemples, consultez les ressources ci-dessous.

### Références
- [Build an MCP Server (Official Docs)](https://modelcontextprotocol.io/docs/develop/build-server)
- [MCP Quickstart Guide](https://modelcontextprotocol.info/docs/quickstart/quickstart/)
- [Model Context Protocol Guide with Demo](https://www.datacamp.com/tutorial/mcp-model-context-protocol)
- [How the Model Context Protocol Works](https://www.freecodecamp.org/news/how-the-model-context-protocol-works/)
- [Practical Introduction to MCP](https://medium.com/@davidlfliang/guide-a-practical-introduction-to-model-context-protocol-mcp-2f63b636f510)