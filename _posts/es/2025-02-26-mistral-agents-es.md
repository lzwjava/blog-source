---
audio: false
generated: true
lang: es
layout: post
title: Agentes de Mistral AI
translated: true
---

Los agentes de Mistral AI son sistemas autónomos impulsados por grandes modelos de lenguaje (LLMs) diseñados para ejecutar tareas complejas basadas en instrucciones de alto nivel. Al aprovechar el procesamiento avanzado del lenguaje natural, estos agentes pueden entender y llevar a cabo objetivos específicos, lo que los hace adecuados para una amplia gama de aplicaciones como soporte al cliente, análisis de datos, automatización de flujos de trabajo y asistencia de codificación. Pueden planificar, utilizar herramientas, tomar acciones e incluso colaborar para lograr objetivos específicos, ofreciendo un nuevo nivel de automatización e inteligencia.

---

## Creación de Agentes

Mistral AI proporciona dos métodos principales para crear agentes: **La Plateforme Agent Builder** y **Agent API**.

### 1. La Plateforme Agent Builder
El Agent Builder ofrece una interfaz de usuario amigable para crear agentes sin conocimientos técnicos extensivos. Para crear un agente:

- Navega al Agent Builder en [https://console.mistral.ai/build/agents/new](https://console.mistral.ai/build/agents/new).
- Personaliza el agente seleccionando un modelo, configurando la temperatura y proporcionando instrucciones opcionales.
- Una vez configurado, el agente puede ser desplegado y accedido a través de la API o Le Chat.

### 2. Agent API
Para desarrolladores, la Agent API permite la creación y la integración programática de agentes en flujos de trabajo existentes. A continuación, se muestran ejemplos de cómo crear y usar un agente a través de la API:

#### Ejemplo en Python
```python
import os
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
client = Mistral(api_key=api_key)

chat_response = client.agents.complete(
    agent_id="your-agent-id",
    messages=[{"role": "user", "content": "¿Cuál es el mejor queso francés?"}],
)
print(chat_response.choices[0].message.content)
```

#### Ejemplo en JavaScript
```javascript
import { Mistral } from '@mistralai/mistralai';

const apiKey = process.env.MISTRAL_API_KEY;
const client = new Mistral({ apiKey: apiKey });

const chatResponse = await client.agents.complete({
    agentId: "your-agent-id",
    messages: [{ role: 'user', content: '¿Cuál es el mejor queso francés?' }],
});
console.log('Chat:', chatResponse.choices[0].message.content);
```

---

## Personalización de Agentes

Los agentes de Mistral AI pueden personalizarse para satisfacer necesidades específicas a través de varias opciones:

- **Selección del Modelo**: Elige el modelo que impulsa al agente. Las opciones incluyen:
  - "Mistral Large 2" (predeterminado, `mistral-large-2407`)
  - "Mistral Nemo" (`open-mistral-nemo`)
  - "Codestral" (`codestral-2405`)
  - Modelos ajustados

- **Temperatura**: Ajusta la temperatura de muestreo (entre 0.0 y 1.0) para controlar la aleatoriedad de las respuestas del agente. Valores más altos hacen que las salidas sean más creativas, mientras que valores más bajos las hacen más enfocadas y deterministas.

- **Instrucciones**: Proporciona instrucciones opcionales para imponer comportamientos específicos en todas las interacciones. Por ejemplo, puedes crear un agente que solo hable francés o genere código Python sin explicaciones.

### Ejemplo: Creación de un Agente que Hable en Francés
Para crear un agente que solo responda en francés:
- Configura el modelo en "Mistral Large 2".
- Usa instrucciones como: "Siempre responde en francés, independientemente del idioma de la entrada."
- Proporciona ejemplos de pocos disparos para reforzar el comportamiento.

---

## Casos de Uso

Los agentes de Mistral AI pueden aplicarse en diversas industrias y tareas. Algunos casos de uso notables incluyen:

- **Soporte al Cliente**: Automatiza respuestas a consultas comunes, maneja preguntas frecuentes y escala problemas complejos a agentes humanos.
- **Análisis de Datos**: Crea agentes que analicen conjuntos de datos, generen informes o realicen cálculos basados en entradas de usuario.
- **Automatización de Flujos de Trabajo**: Integra agentes con herramientas como correo electrónico, sistemas CRM o procesamiento de pagos para automatizar tareas repetitivas.
- **Asistencia de Codificación**: Diseña agentes para generar código, proporcionar sugerencias de depuración o crear pruebas unitarias.

### Ejemplos Específicos
- **Agente que Hable en Francés**: Un agente configurado para responder solo en francés, útil para empresas que atienden a clientes francófonos.
- **Generador de Código Python**: Un agente que genera fragmentos de código Python sin explicaciones, ideal para desarrolladores que necesitan código rápido y limpio.

---

## Despliegue

Una vez creado un agente, puede ser desplegado y accedido de dos maneras:

- **Integración de API**: Usa la API de Mistral AI para integrar el agente en tus aplicaciones. Consulta los ejemplos de código en la sección "Creación de Agentes" para obtener detalles.
- **Le Chat**: Activa la opción para chatear directamente con el agente en la plataforma Le Chat de Mistral.

Los agentes pueden compartirse fácilmente dentro de las organizaciones, y con las capacidades avanzadas de razonamiento de modelos como Mistral Large 2, puedes construir flujos de trabajo complejos que involucren múltiples agentes.

---

Esta documentación proporciona una guía completa para entender, crear, personalizar y desplegar agentes de Mistral AI, basada en la documentación oficial en [https://docs.mistral.ai/capabilities/agents/](https://docs.mistral.ai/capabilities/agents/). Al aprovechar estas herramientas, puedes automatizar tareas, mejorar la productividad y desbloquear nuevos niveles de eficiencia en tus flujos de trabajo. Para obtener más detalles, explora la [documentación de Mistral AI](https://docs.mistral.ai/capabilities/agents/).