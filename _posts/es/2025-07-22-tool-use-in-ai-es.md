---
audio: false
generated: true
lang: es
layout: post
title: Uso de Herramientas de IA en API Explicado
translated: true
type: note
---

### ¿Qué es el Uso de Herramientas en las APIs de IA?

El uso de herramientas, a menudo denominado "tool calling" o "function calling", es una característica en las APIs de IA que permite a los grandes modelos de lenguaje (LLMs) interactuar con herramientas, funciones o APIs externas. En lugar de generar respuestas basándose únicamente en su conocimiento interno, el modelo puede decidir llamar a funciones predefinidas para obtener datos en tiempo real, realizar cálculos o ejecutar acciones. Esto hace que la IA sea más dinámica y útil para tareas como consultar el clima, buscar en bases de datos o integrarse con otros servicios.

El proceso típicamente funciona así:
- Defines herramientas (funciones) con descripciones y parámetros en formato JSON.
- El modelo analiza la consulta del usuario y, si es necesario, genera una "llamada a herramienta" con el nombre de la función y los argumentos.
- Tu aplicación ejecuta la función y devuelve el resultado al modelo.
- El modelo luego genera una respuesta final incorporando la salida de la herramienta.

Esto comúnmente está inspirado en la API de llamadas a funciones de OpenAI, y muchos proveedores como Mistral y DeepSeek admiten implementaciones compatibles.

### ¿Mistral o DeepSeek para el Uso de Herramientas?

Tanto Mistral AI como DeepSeek AI admiten el tool calling en sus APIs, lo que las hace adecuadas para construir agentes o aplicaciones que requieren integraciones externas. Aquí hay una comparación rápida basada en la información disponible:

- **Soporte para Uso de Herramientas**:
  - Ambos siguen una estructura similar a la API de OpenAI, permitiendo una integración fácil con herramientas a través de esquemas JSON.
  - Mistral lo soporta en modelos como Mistral Large y Medium, con opciones para flujos de trabajo basados en agentes.
  - DeepSeek lo soporta principalmente a través de su modelo "deepseek-chat" y es totalmente compatible con el SDK de OpenAI.

- **Pros y Contras**:
  - **Mistral**: Más versátil para tareas generales, inferencia más rápida en algunos benchmarks, y mejor adaptado a las necesidades de privacidad de datos europeas. Sobresale en respuestas rápidas y tiene sólidas capacidades multilingües. Sin embargo, puede ser más caro (por ejemplo, los costos de entrada/salida son más altos en comparación con DeepSeek).
  - **DeepSeek**: Significativamente más económico (hasta 28 veces menos costoso en algunas comparaciones), fuerte en matemáticas, codificación y tareas de razonamiento. Es ideal para usuarios conscientes del presupuesto o uso de alto volumen. Las desventajas incluyen un rendimiento potencialmente más lento en tareas no técnicas y menos énfasis en características multimodales.
  - **¿Cuál elegir?** Si el costo es una prioridad y tu caso de uso implica codificación/matemáticas con herramientas, elige DeepSeek. Para aplicaciones más amplias, respuestas más rápidas o características empresariales como agentes, Mistral es mejor. Ambos son amigables con el código abierto y tienen buen rendimiento, pero prueba con tus necesidades específicas.

En última instancia, ninguno es estrictamente "mejor" para el uso de herramientas: ambos funcionan bien. DeepSeek podría destacarse por el ahorro de costos, mientras que Mistral ofrece integraciones de agentes más pulidas.

### Cómo Usar el Uso de Herramientas

Para usar tool calling, necesitarás una clave API del proveedor respectivo (regístrate en mistral.ai para Mistral o platform.deepseek.com para DeepSeek). Ambos utilizan SDKs de Python similares al de OpenAI. A continuación se muestran ejemplos paso a paso para una herramienta simple de consulta del clima.

#### Usando Tool Use con Mistral AI
La API de Mistral admite tool calling a través de su `MistralClient` en las finalizaciones de chat. Instala el SDK con `pip install mistralai`.

**Código Python de Ejemplo** (adaptado de fuentes oficiales y de la comunidad):
```python
from mistralai import Mistral

# Inicializar cliente con tu clave API
api_key = "TU_CLAVE_API_MISTRAL"
model = "mistral-large-latest"  # Admite tool calling
client = Mistral(api_key=api_key)

# Definir herramientas (funciones)
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Obtener el clima de una ubicación.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "La ciudad, ej. San Francisco"}
                },
                "required": ["location"]
            }
        }
    }
]

# Mensaje del usuario
messages = [{"role": "user", "content": "¿Qué tiempo hace en Hangzhou?"}]

# Primera llamada API: El modelo decide si se necesita una herramienta
response = client.chat.complete(
    model=model,
    messages=messages,
    tools=tools,
    tool_choice="auto"  # Decide automáticamente el uso de herramientas
)

# Verificar si hay llamadas a herramientas
tool_calls = response.choices[0].message.tool_calls
if tool_calls:
    # Añadir la respuesta del modelo a los mensajes
    messages.append(response.choices[0].message)
    
    # Simular ejecutar la herramienta (en código real, llamar a una API real)
    tool_call = tool_calls[0]
    if tool_call.function.name == "get_weather":
        location = eval(tool_call.function.arguments)["location"]
        weather_result = "24°C y soleado"  # Reemplazar con llamada a función real
        
        # Añadir resultado de la herramienta
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "name": tool_call.function.name,
            "content": weather_result
        })
    
    # Segunda llamada API: El modelo genera la respuesta final
    final_response = client.chat.complete(model=model, messages=messages)
    print(final_response.choices[0].message.content)
else:
    print(response.choices[0].message.content)
```

Este código envía una consulta, verifica si hay una llamada a herramienta, la ejecuta (simulada aquí) y obtiene la respuesta final. Para configuraciones basadas en agentes, usa la API de agentes beta de Mistral para flujos de trabajo más complejos.

#### Usando Tool Use con DeepSeek AI
La API de DeepSeek es compatible con OpenAI, por lo que puedes usar el SDK de Python de OpenAI. Instálalo con `pip install openai`.

**Código Python de Ejemplo** (de la documentación oficial):
```python
from openai import OpenAI

# Inicializar cliente con la URL base de DeepSeek y la clave API
client = OpenAI(
    api_key="TU_CLAVE_API_DEEPSEEK",
    base_url="https://api.deepseek.com"
)

# Definir herramientas
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Obtener el clima de una ubicación, el usuario debe proporcionar una ubicación primero",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "La ciudad y estado, ej. San Francisco, CA",
                    }
                },
                "required": ["location"]
            },
        }
    },
]

# Función para enviar mensajes
def send_messages(messages):
    response = client.chat.completions.create(
        model="deepseek-chat",  # Admite tool calling
        messages=messages,
        tools=tools
    )
    return response.choices[0].message

# Mensaje del usuario
messages = [{"role": "user", "content": "¿Cómo está el clima en Hangzhou?"}]
message = send_messages(messages)
print(f"Usuario>\t {messages[0]['content']}")

# Manejar llamada a herramienta
tool = message.tool_calls[0]
messages.append(message)

# Simular ejecución de herramienta (reemplazar con función real)
messages.append({"role": "tool", "tool_call_id": tool.id, "content": "24℃"})

# Obtener respuesta final
message = send_messages(messages)
print(f"Modelo>\t {message.content}")
```

Este sigue el mismo flujo: consulta → llamada a herramienta → ejecutar → respuesta final. DeepSeek limita la longitud del contexto, así que mantén los mensajes concisos.

Para uso avanzado, consulta los límites de tasa, costos y documentación específica del modelo. Prueba en un entorno de pruebas para manejar errores como parámetros no válidos.

### Referencias
- [Documentación de Llamadas a Funciones de Mistral AI](https://docs.mistral.ai/agents/function_calling/)
- [Guía de Llamadas a Funciones de la API de DeepSeek](https://api-docs.deepseek.com/guides/function_calling)
- [Ejemplo de Llamadas a Funciones de Mistral AI con Código](https://medium.com/@jcrsch/mistral-ai-function-calling-a-simple-example-with-code-72f3a762550f)
- [DeepSeek vs. Mistral: Una Comparación Integral de Modelos de IA](https://medium.com/ai-tools-tips-and-news/deepseek-vs-mistral-a-comprehensive-ai-models-comparison-f7d7b86f4b28)
- [Comparación Mistral Large vs DeepSeek-V3](https://docsbot.ai/models/compare/mistral-large-2/deepseek-v3)