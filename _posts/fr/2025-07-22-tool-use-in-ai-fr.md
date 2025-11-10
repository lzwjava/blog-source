---
audio: false
generated: true
lang: fr
layout: post
title: Utilisation des outils d'IA dans les API expliquée
translated: true
type: note
---

### Qu'est-ce que l'utilisation d'outils dans les API d'IA ?

L'utilisation d'outils, souvent appelée « appel d'outil » ou « appel de fonction », est une fonctionnalité des API d'IA qui permet aux grands modèles de langage (LLM) d'interagir avec des outils, fonctions ou API externes. Au lieu de générer des réponses uniquement basées sur leurs connaissances internes, le modèle peut décider d'appeler des fonctions prédéfinies pour récupérer des données en temps réel, effectuer des calculs ou exécuter des actions. Cela rend l'IA plus dynamique et utile pour des tâches telles que l'interrogation de la météo, la recherche dans des bases de données ou l'intégration avec d'autres services.

Le processus fonctionne généralement ainsi :
- Vous définissez des outils (fonctions) avec des descriptions et des paramètres au format JSON.
- Le modèle analyse la requête de l'utilisateur et, si nécessaire, produit un « appel d'outil » avec le nom de la fonction et ses arguments.
- Votre application exécute la fonction et renvoie le résultat au modèle.
- Le modèle génère ensuite une réponse finale intégrant le résultat de l'outil.

Cette approche est communément inspirée par l'API d'appel de fonction d'OpenAI, et de nombreux fournisseurs comme Mistral et DeepSeek prennent en charge des implémentations compatibles.

### Mistral ou DeepSeek pour l'utilisation d'outils ?

Mistral AI et DeepSeek AI prennent tous deux en charge l'appel d'outils dans leurs API, ce qui les rend adaptés à la création d'agents ou d'applications nécessitant des intégrations externes. Voici une comparaison rapide basée sur les informations disponibles :

- **Prise en charge de l'utilisation d'outils** :
  - Tous deux suivent une structure similaire à l'API d'OpenAI, permettant une intégration facile avec des outils via des schémas JSON.
  - Mistral la prend en charge sur des modèles comme Mistral Large et Medium, avec des options pour les flux de travail basés sur des agents.
  - DeepSeek la prend en charge principalement via son modèle « deepseek-chat » et est entièrement compatible avec le SDK d'OpenAI.

- **Avantages et Inconvénients** :
  - **Mistral** : Plus polyvalent pour les tâches générales, une inférence plus rapide dans certains benchmarks, et mieux adapté aux besoins de confidentialité des données européennes. Il excelle dans les réponses rapides et possède de solides capacités multilingues. Cependant, il peut être plus coûteux (par exemple, les coûts d'entrée/sortie sont plus élevés que ceux de DeepSeek).
  - **DeepSeek** : Significativement moins cher (jusqu'à 28 fois moins coûteux dans certaines comparaisons), performant dans les tâches de mathématiques, de codage et de raisonnement. Il est idéal pour les utilisateurs soucieux de leur budget ou pour une utilisation à grand volume. Les inconvénients incluent des performances potentiellement plus lentes dans les tâches non techniques et moins d'accent sur les fonctionnalités multimodales.
  - **Lequel choisir ?** Si le coût est une priorité et que votre cas d'usage implique du codage/des mathématiques avec des outils, optez pour DeepSeek. Pour des applications plus larges, des réponses plus rapides ou des fonctionnalités entreprises comme les agents, Mistral est meilleur. Les deux sont favorables à l'open source et performants, mais testez-les en fonction de vos besoins spécifiques.

En fin de compte, aucun n'est strictement « meilleur » pour l'utilisation d'outils – les deux fonctionnent bien. DeepSeek pourrait l'emporter pour les économies de coûts, tandis que Mistral offre des intégrations d'agents plus abouties.

### Comment utiliser l'utilisation d'outils

Pour utiliser l'appel d'outils, vous aurez besoin d'une clé API du fournisseur respectif (inscrivez-vous sur mistral.ai pour Mistral ou platform.deepseek.com pour DeepSeek). Les deux utilisent des SDK Python similaires à celui d'OpenAI. Vous trouverez ci-dessous des exemples étape par étape pour un outil simple de requête météo.

#### Utilisation d'outils avec Mistral AI
L'API de Mistral prend en charge l'appel d'outils via leur `MistralClient` dans les chat completions. Installez le SDK avec `pip install mistralai`.

**Exemple de code Python** (adapté de sources officielles et communautaires) :
```python
from mistralai import Mistral

# Initialiser le client avec votre clé API
api_key = "VOTRE_CLE_API_MISTRAL"
model = "mistral-large-latest"  # Prend en charge l'appel d'outils
client = Mistral(api_key=api_key)

# Définir les outils (fonctions)
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Obtenir la météo pour un lieu.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "La ville, par ex. Paris"}
                },
                "required": ["location"]
            }
        }
    }
]

# Message utilisateur
messages = [{"role": "user", "content": "Quel temps fait-il à Hangzhou ?"}]

# Premier appel API : Le modèle décide si un outil est nécessaire
response = client.chat.complete(
    model=model,
    messages=messages,
    tools=tools,
    tool_choice="auto"  # Décide automatiquement de l'utilisation de l'outil
)

# Vérifier les appels d'outils
tool_calls = response.choices[0].message.tool_calls
if tool_calls:
    # Ajouter la réponse du modèle aux messages
    messages.append(response.choices[0].message)
    
    # Simuler l'exécution de l'outil (dans du code réel, appelez une véritable API)
    tool_call = tool_calls[0]
    if tool_call.function.name == "get_weather":
        location = eval(tool_call.function.arguments)["location"]
        weather_result = "24°C et ensoleillé"  # Remplacer par un véritable appel de fonction
        
        # Ajouter le résultat de l'outil
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "name": tool_call.function.name,
            "content": weather_result
        })
    
    # Deuxième appel API : Le modèle génère la réponse finale
    final_response = client.chat.complete(model=model, messages=messages)
    print(final_response.choices[0].message.content)
else:
    print(response.choices[0].message.content)
```

Ce code envoie une requête, vérifie un appel d'outil, l'exécute (simulé ici) et obtient la réponse finale. Pour les configurations basées sur des agents, utilisez l'API beta agents de Mistral pour des flux de travail plus complexes.

#### Utilisation d'outils avec DeepSeek AI
L'API de DeepSeek est compatible avec OpenAI, vous pouvez donc utiliser le SDK Python d'OpenAI. Installez-le avec `pip install openai`.

**Exemple de code Python** (tiré de la documentation officielle) :
```python
from openai import OpenAI

# Initialiser le client avec l'URL de base DeepSeek et la clé API
client = OpenAI(
    api_key="VOTRE_CLE_API_DEEPSEEK",
    base_url="https://api.deepseek.com"
)

# Définir les outils
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Obtenir la météo d'un lieu, l'utilisateur doit d'abord fournir un lieu",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "La ville et l'état, par ex. Paris, France",
                    }
                },
                "required": ["location"]
            },
        }
    },
]

# Fonction pour envoyer des messages
def send_messages(messages):
    response = client.chat.completions.create(
        model="deepseek-chat",  # Prend en charge l'appel d'outils
        messages=messages,
        tools=tools
    )
    return response.choices[0].message

# Message utilisateur
messages = [{"role": "user", "content": "Quel temps fait-il à Hangzhou ?"}]
message = send_messages(messages)
print(f"Utilisateur>\t {messages[0]['content']}")

# Gérer l'appel d'outil
tool = message.tool_calls[0]
messages.append(message)

# Simuler l'exécution de l'outil (remplacer par une vraie fonction)
messages.append({"role": "tool", "tool_call_id": tool.id, "content": "24℃"})

# Obtenir la réponse finale
message = send_messages(messages)
print(f"Modèle>\t {message.content}")
```

Ceci suit le même flux : requête → appel d'outil → exécution → réponse finale. DeepSeek limite la longueur du contexte, gardez donc les messages concis.

Pour une utilisation avancée, vérifiez les limites de débit, les coûts et la documentation spécifique au modèle. Testez dans un environnement sandbox pour gérer les erreurs comme les paramètres invalides.

### Références
- [Documentation Mistral AI sur l'appel de fonction](https://docs.mistral.ai/agents/function_calling/)
- [Guide DeepSeek API sur l'appel de fonction](https://api-docs.deepseek.com/guides/function_calling)
- [Exemple d'appel de fonction Mistral AI avec code](https://medium.com/@jcrsch/mistral-ai-function-calling-a-simple-example-with-code-72f3a762550f)
- [DeepSeek vs. Mistral : Une comparaison complète des modèles d'IA](https://medium.com/ai-tools-tips-and-news/deepseek-vs-mistral-a-comprehensive-ai-models-comparison-f7d7b86f4b28)
- [Comparaison Mistral Large vs DeepSeek-V3](https://docsbot.ai/models/compare/mistral-large-2/deepseek-v3)