---
audio: false
generated: true
lang: es
layout: post
title: Acceso a Claude a través de OpenRouter
translated: true
type: note
---

### Cómo usar los modelos Claude con OpenRouter (Para usuarios chinos sin acceso a la API de Anthropic)

Como usuario chino, puedes enfrentar restricciones para acceder directamente a la API de Claude de Anthropic debido a bloqueos regionales. Sin embargo, OpenRouter es una alternativa confiable que actúa como una puerta de enlace de API unificada para múltiples proveedores de IA, incluidos los modelos Claude de Anthropic. OpenRouter es accesible en China (tanto el sitio web como los endpoints de la API no están bloqueados), lo que te permite enrutar solicitudes a Claude sin necesidad de una cuenta o clave API directa de Anthropic. Es de pago por uso (necesitarás agregar un método de pago), pero registrarse es gratuito y admite un nivel gratuito para uso limitado.

La API de OpenRouter es compatible con el formato de OpenAI, por lo que puedes usar bibliotecas familiares como el SDK de Python de OpenAI. A continuación, describiré los pasos para comenzar y proporcionaré ejemplos de código para usar Claude en Python.

#### Paso 1: Regístrate en OpenRouter
1. Visita el sitio web de OpenRouter: https://openrouter.ai.
2. Haz clic en "Sign Up" o "Get Started" (generalmente en la parte superior derecha).
3. Crea una cuenta usando tu correo electrónico (o inicio de sesión con GitHub/Google si está disponible). No se necesita VPN, ya que el sitio funciona en China.
4. Después de registrarte, verifica tu correo electrónico si es necesario.
5. Ve al panel de control y agrega un método de pago (por ejemplo, tarjeta de crédito) para financiar tu cuenta. OpenRouter cobra según el uso de tokens, pero puedes comenzar con un depósito pequeño. Consulta su página de precios para obtener detalles sobre los modelos Claude.

#### Paso 2: Genera una Clave API
1. En tu panel de control de OpenRouter, navega a la sección "API Keys" o "Keys".
2. Crea una nueva clave API (se verá como una cadena larga, por ejemplo, `sk-or-v1-...`).
3. Cópiala y guárdala de forma segura: trátala como una contraseña. La usarás en tu código en lugar de una clave de Anthropic.

#### Paso 3: Elige un Modelo Claude
OpenRouter enumera los modelos Claude de Anthropic con ID como:
- `anthropic/claude-3.5-sonnet` (recomendado para la mayoría de las tareas; equilibrado y capaz).
- `anthropic/claude-3-opus` (más potente pero más caro).
- Las versiones más nuevas (por ejemplo, Claude 3.7 si está disponible en 2025) se enumerarán en https://openrouter.ai/models?providers=anthropic.

Puedes navegar por la página de modelos para ver costos, límites de contexto y disponibilidad.

#### Paso 4: Configura tu Entorno
- Instala Python si no lo tienes (versión 3.8+ recomendada).
- Instala la biblioteca de OpenAI: Ejecuta `pip install openai` en tu terminal.

#### Paso 5: Usa Claude en Código
Usa el SDK de OpenAI con la URL base de OpenRouter (`https://openrouter.ai/api/v1`). Especifica el ID del modelo Claude en tus solicitudes.

Aquí tienes un ejemplo simple de Python para chatear con Claude 3.5 Sonnet:

```python
from openai import OpenAI

# Inicializa el cliente con el endpoint de OpenRouter y tu clave API
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="TU_CLAVE_API_DE_OPENROUTER_AQUÍ",  # Reemplaza con tu clave real
)

# Realiza una solicitud a Claude
completion = client.chat.completions.create(
    model="anthropic/claude-3.5-sonnet",  # Usa el ID del modelo Claude
    messages=[
        {"role": "system", "content": "Eres un asistente útil."},
        {"role": "user", "content": "Hola, ¿cuál es la capital de China?"}
    ],
    temperature=0.7,  # Opcional: Ajusta para la creatividad (0-1)
    max_tokens=150    # Opcional: Limita la longitud de la respuesta
)

# Imprime la respuesta
print(completion.choices[0].message.content)
```

- **Explicación**: Esto envía un mensaje de sistema y un mensaje de usuario a Claude, obtiene una respuesta y la imprime. Reemplaza la clave API y ajusta los parámetros según sea necesario.
- **Si prefieres solicitudes HTTP sin procesar** (sin la biblioteca de OpenAI):

```python
import requests
import json

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer TU_CLAVE_API_DE_OPENROUTER_AQUÍ",
        "Content-Type": "application/json"
    },
    data=json.dumps({
        "model": "anthropic/claude-3.5-sonnet",
        "messages": [
            {"role": "system", "content": "Eres un asistente útil."},
            {"role": "user", "content": "Hola, ¿cuál es la capital de China?"}
        ]
    })
)

# Analiza e imprime la respuesta
data = response.json()
print(data['choices'][0]['message']['content'])
```

- **Consejos**:
  - Agrega encabezados opcionales como `"HTTP-Referer": "tu-url-del-sitio"` y `"X-Title": "El Nombre de Tu Aplicación"` para atribuir el uso (ayuda con las tablas de clasificación y posibles créditos gratuitos).
  - Monitorea el uso en tu panel de control de OpenRouter para evitar costos inesperados.
  - Para respuestas en streaming o funciones avanzadas (por ejemplo, herramientas), consulta la documentación completa de OpenRouter.
  - Si encuentras límites de tasa o errores, verifica tu saldo o prueba con un modelo diferente.

#### Resolución de Problemas
- **Errores de API**: Asegúrate de que tu clave sea correcta y esté financiada. Prueba primero con un modelo barato.
- **Problemas Regionales**: Si ocurre algún bloqueo (poco probable), usa una VPN, pero OpenRouter está diseñado para evitar tales restricciones para los modelos admitidos.
- **Alternativas Gratuitas**: Para acceso gratuito limitado, explora proxies como Puter.js (pero pueden tener limitaciones).

Esta configuración te permite usar Claude de manera programática sin acceso directo a Anthropic. Si necesitas integración con herramientas específicas (por ejemplo, Cursor IDE o Make.com), busca tutoriales sobre ellas.

Referencias:  
[Documentación de OpenRouter](https://openrouter.ai/docs)  
[Anthropic Claude en OpenRouter](https://openrouter.ai/anthropic/claude-3.5-sonnet)  
[Usar OpenRouter en China](https://medium.com/ai-simplified-in-plain-english/not-re-inventing-the-wheel-in-ai-2ec3e76ae2bd)  
[Cómo usar Claude en China](https://www.comparitech.com/blog/vpn-privacy/how-to-use-claude-in-china/)