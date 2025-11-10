---
audio: false
generated: true
lang: es
layout: post
title: Optimización de Llamadas a Herramientas de IA con Ejecución en el Servidor
translated: true
type: note
---

Sí, la naturaleza de ida y vuelta de las llamadas tradicionales a herramientas o funciones en chatbots (donde el modelo de IA genera una llamada, la envía al cliente o a otro servicio, espera la ejecución y luego recibe los resultados) puede introducir latencia, especialmente en aplicaciones en tiempo real. Esto suele deberse a la sobrecarga de red, la serialización/deserialización y la necesidad de múltiples viajes de ida y vuelta a la API. Tu sugerencia de usar funciones lambda o diseñar una API que acepte código Python para su ejecución en el servidor es una forma inteligente de mitigar esto—esencialmente, trasladando la computación al servidor para minimizar las interacciones cliente-servidor. Voy a desglosar esto conceptualmente, discutir la viabilidad, las implementaciones potenciales y las compensaciones.

### Por qué las Llamadas a Herramientas Tradicionales Pueden Ser Lentas
En muchos frameworks de IA (por ejemplo, LangChain, la función de llamadas de OpenAI, o las herramientas de Anthropic):
- El modelo genera una llamada estructurada a una herramienta (por ejemplo, JSON con el nombre de la función y los argumentos).
- El cliente (o agente) ejecuta la función localmente o a través de otra API.
- Los resultados se añaden al historial de la conversación y se envían de vuelta al modelo para el siguiente paso de inferencia.
Este ciclo puede añadir segundos de retraso por ciclo, lo que se acumula en tareas complejas como el análisis de datos o el razonamiento de múltiples pasos.

### Usar Funciones Lambda o Ejecución de Código en el Servidor
Tu idea se alinea con los modelos de ejecución "sin servidor" o "en espacio aislado" (sandboxed), donde la IA genera código (o un fragmento similar a una lambda) que se ejecuta directamente en el servidor que aloja el modelo. Esto mantiene todo en un mismo entorno, reduciendo los viajes de ida y vuelta a potencialmente solo una llamada API desde el usuario.

- **Enfoque de Funciones Lambda**: Servicios como AWS Lambda, Google Cloud Functions o Azure Functions permiten ejecutar pequeños fragmentos de código Python efímeros bajo demanda sin gestionar servidores. En un contexto de IA:
  - El backend del chatbot podría envolver el modelo de IA (por ejemplo, a través de la API de OpenAI) e integrar Lambda como una herramienta.
  - El modelo genera una expresión lambda o una función corta, que se invoca en el servidor.
  - Pros: Escalable, pago por uso y inicio rápido (a menudo <100 ms de inicio en frío).
  - Contras: Tiempo de ejecución limitado (por ejemplo, 15 minutos máximo en AWS), y necesitarías gestionar el estado si la tarea abarca múltiples invocaciones.
  - Ejemplo: Un agente de IA podría generar una lambda para procesar datos (por ejemplo, `lambda x: sum(x) if isinstance(x, list) else 0`), enviarla a un endpoint de Lambda y obtener los resultados en línea.

- **Diseñar una API para Aceptar y Ejecutar Código Python**:
  - Sí, esto es absolutamente posible y ya existe en sistemas de producción. La clave es el **espacio aislado** (sandboxing) para prevenir riesgos de seguridad como la ejecución de código arbitrario (por ejemplo, eliminar archivos o realizar llamadas de red).
  - Cómo funciona: El endpoint de la API recibe un fragmento de código (como una cadena), lo ejecuta en un entorno aislado, captura la salida/errores y devuelve los resultados. El modelo de IA puede generar y "llamar" a este código de forma iterativa sin salir del servidor.
  - Beneficios:
    - Reduce la latencia: La ejecución ocurre en el mismo centro de datos que el modelo, a menudo en milisegundos.
    - Permite tareas complejas: Como procesamiento de datos, simulaciones matemáticas o manejo de archivos sin herramientas externas.
    - Sesiones con estado: Algunas implementaciones mantienen un entorno similar a un REPL a lo largo de las llamadas.
  - Medidas de Seguridad:
    - Usar contenedores (Docker), micro-VMs (Firecracker) o intérpretes de Python restringidos (por ejemplo, PyPy sandboxing o globales restringidos).
    - Limitar recursos: Cuotas de CPU/tiempo, sin acceso a red, módulos en lista blanca (por ejemplo, numpy, pandas, pero no os o subprocess).
    - Bibliotecas como `restrictedpython` o herramientas como E2B/Firecracker proporcionan espacios aislados listos para usar.

### Ejemplos del Mundo Real e Implementaciones
Varias plataformas de IA ya admiten esto en diversos grados:
- **Assistants API de OpenAI con Code Interpreter**: Permite al modelo escribir y ejecutar código Python en un entorno aislado en los servidores de OpenAI. El modelo puede subir archivos, ejecutar código e iterar sobre los resultados—todo en el servidor. No es necesaria la ejecución en el cliente.
- **Ejecución de Código de la API Gemini de Google**: Proporciona un espacio aislado de Python integrado donde el modelo genera y ejecuta código de forma iterativa, aprendiendo de los resultados sin llamadas externas.
- **Soluciones Personalizadas**:
  - **E2B Sandbox**: Un SDK/API para crear espacios aislados basados en la nube con kernels de Jupyter. Los agentes de IA pueden enviar código para ejecutar de forma segura, ideal para herramientas de análisis de datos.
  - **Modal Sandboxes**: Una plataforma para ejecutar código generado por IA en entornos aislados, a menudo utilizada para agentes LLM.
  - **SandboxAI (código abierto)**: Un runtime específicamente para ejecutar Python generado por IA en espacios aislados.
  - Para DIY: Construye un servidor FastAPI o Flask que acepte código via POST, use `exec()` en un espacio de nombres restringido, o inicie un contenedor Docker por petición.

En términos de código, un endpoint de API simple podría verse así (pseudocódigo para ilustrar):

```python
from fastapi import FastAPI
import restrictedpython  # Para ejecución segura

app = FastAPI()

@app.post("/execute")
def execute_code(code: str):
    safe_globals = {"__builtins__": restrictedpython.safe_builtins}  # Entorno restringido
    try:
        result = {}
        exec(code, safe_globals, result)  # Ejecutar código
        return {"output": result.get("output")}
    except Exception as e:
        return {"error": str(e)}
```

Integra esto con tu chatbot: La IA genera código basado en la entrada del usuario, llama al endpoint internamente e incorpora los resultados.

### Posibles Desventajas y Mejores Prácticas
- **Riesgos de Seguridad**: La ejecución de código arbitrario es peligrosa—siempre usa espacios aislados. Evítalo si manejas usuarios no confiables.
- **Coste y Escalabilidad**: La ejecución en el servidor usa más computación; monitoriza con herramientas como New Relic para optimizar.
- **Depuración**: Los errores en el código generado pueden crear bucles si no se manejan bien.
- **Alternativas para la Optimización**:
  - Llamadas a herramientas por lotes: Agrupa múltiples funciones en un solo viaje de ida y vuelta al servidor.
  - Streaming: Usa APIs que transmitan respuestas mientras ejecutan herramientas en paralelo.
  - Lado del cliente si es tolerante a la latencia: Para tareas no sensibles, ejecuta localmente.
- Si estás construyendo desde cero, comienza con frameworks como LangChain o Vercel's AI SDK, que admiten herramientas personalizadas y pueden configurarse para ejecuciones en el servidor.

Este enfoque puede hacer que los chatbots sean mucho más rápidos y capaces, especialmente para tareas computacionales. Si estás implementando esto, considera comenzar con las funciones integradas de OpenAI o Gemini para obtener resultados rápidos.

[Building a Sandboxed Environment for AI generated Code Execution](https://anukriti-ranjan.medium.com/building-a-sandboxed-environment-for-ai-generated-code-execution-e1351301268a)  
[substratusai/sandboxai: Run AI generated code in isolated sandboxes](https://github.com/substratusai/sandboxai)  
[Build AI data analyst with sandboxed code execution using TS ... - E2B](https://e2b.dev/blog/build-ai-data-analyst-with-sandboxed-code-execution-using-typescript-and-gpt-4o)  
[Code execution | Gemini API](https://ai.google.dev/gemini-api/docs/code-execution)  
[Assistants Code Interpreter - OpenAI API](https://platform.openai.com/docs/assistants/tools/code-interpreter)  
[Modal Sandboxes](https://modal.com/use-cases/sandboxes)  
[Optimizing AI chatbot performance with New Relic AI monitoring](https://newrelic.com/blog/how-to-relic/optimizing-ai-chatbot-performance)