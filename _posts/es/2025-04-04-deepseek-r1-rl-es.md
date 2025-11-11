---
audio: false
generated: true
lang: es
layout: post
title: DeepSeek R1
translated: true
type: note
---

DeepSeek R1 emplea un enfoque novedoso para el aprendizaje por refuerzo (RL) que enfatiza significativamente las **capacidades de razonamiento** en los modelos de lenguaje grandes (LLM). Su técnica se diferencia del Aprendizaje por Refuerzo con Retroalimentación Humana (RLHF) tradicional en varios aspectos clave.

Aquí hay un desglose de las técnicas que DeepSeek utilizó en el aprendizaje por refuerzo de R1:

**1. Aprendizaje por Refuerzo Puro (RL) para el Razonamiento Inicial (DeepSeek-R1-Zero):**

*   **No hay Fine-Tuning Supervisado (SFT) Inicial en Instrucciones:** A diferencia de muchos LLM que primero se someten a SFT en instrucciones escritas por humanos, DeepSeek-R1-Zero fue entrenado con **RL puro** directamente en el modelo base (DeepSeek-V3-Base).
*   **Optimización de Política Relativa Grupal (GRPO):** Utilizaron GRPO como su algoritmo de RL central. GRPO está diseñado para ser más eficiente que la Optimización de Política Proximal (PPO) al eliminar la necesidad de una red crítica separada. Estima las recompensas de referencia comparando un grupo de salidas generadas, asignando puntuaciones relativas basadas en su calidad. Esto incentiva al modelo a generar mejores respuestas en comparación con sus propios intentos anteriores.
*   **Sistema de Recompensa Basado en Reglas:** En lugar de depender únicamente de las preferencias humanas para la fase inicial de RL, DeepSeek-R1-Zero utilizó un **sistema de recompensa basado en reglas**. Este sistema se centró principalmente en:
    *   **Recompensas por Precisión:** Recompensar al modelo por proporcionar respuestas correctas, especialmente en tareas con soluciones verificables como problemas matemáticos (comprobando si la respuesta final es correcta).
    *   **Recompensas por Formato:** Recompensar al modelo por adherirse a un formato de salida específico, particularmente usando las etiquetas `` para encerrar su proceso de razonamiento. Esto fomentó la emergencia del razonamiento de cadena de pensamiento (chain-of-thought).
*   **Comportamientos de Razonamiento Emergentes:** Este enfoque de RL puro permitió a DeepSeek-R1-Zero desarrollar naturalmente habilidades de razonamiento impresionantes, incluyendo autoverificación, reflexión y la generación de explicaciones largas de cadena de pensamiento, sin demostraciones humanas explícitas para estos comportamientos.

**2. Entrenamiento Multi-Etapa para Capacidades Mejoradas de Legibilidad y Generales (DeepSeek-R1):**

Para abordar las limitaciones de DeepSeek-R1-Zero (como la mala legibilidad y la mezcla de idiomas), DeepSeek-R1 empleó una canalización de entrenamiento multi-etapa más completa:

*   **Fine-Tuning con Datos de Arranque en Frío (Cold-Start):** Antes de la fase principal de RL, el modelo base fue fine-tuneado en un pequeño conjunto de datos de alta calidad, escritos por humanos (o generados y refinados), con ejemplos largos de razonamiento de cadena de pensamiento. Estos datos de "arranque en frío" ayudaron a guiar al modelo hacia la producción de pasos de razonamiento más legibles y coherentes.
*   **Aprendizaje por Refuerzo Orientado al Razonamiento (Segunda Etapa de RL):** El modelo luego pasó por una segunda fase de RL a gran escala (similar a DeepSeek-R1-Zero) pero con una **recompensa adicional de consistencia de lenguaje**. Esta recompensa penalizaba al modelo por mezclar idiomas dentro de su proceso de razonamiento.
*   **Fine-Tuning Supervisado (SFT):** Después del RL orientado al razonamiento, el modelo fue fine-tuneado aún más en un conjunto de datos diverso que incluía tanto datos de razonamiento (sintetizados usando muestreo por rechazo del modelo RL, juzgados por DeepSeek-V3) como datos generales sin razonamiento (aumentados con cadena de pensamiento). Esta etapa SFT tuvo como objetivo mejorar la utilidad y la seguridad (harmlessness) del modelo mientras se preservaban sus fuertes habilidades de razonamiento.
*   **RL para Todos los Escenarios (Tercera Etapa de RL):** Se realizó una fase final de RL utilizando prompts de una gama más amplia de escenarios para refinar aún más las capacidades generales del modelo y su alineación con los comportamientos deseados.

**Diferencias Clave con el RLHF Tradicional:**

*   **Menor Dependencia de Datos Extensos de Preferencias Humanas:** Si bien alguna evaluación humana pudo estar involucrada en juzgar la calidad de los datos sintetizados, el entrenamiento central de RL en DeepSeek-R1 aprovechó en gran medida las recompensas basadas en reglas, especialmente en las etapas iniciales. Esto reduce el costo y la complejidad de recopilar grandes cantidades de comparaciones directas de preferencias humanas.
*   **Énfasis en el Razonamiento Emergente:** El enfoque de RL puro apuntó a incentivar al modelo para que *descubra* estrategias de razonamiento efectivas por sí mismo, en lugar de aprender únicamente de ejemplos de razonamiento proporcionados por humanos.
*   **Enfoque Multi-Etapa:** La canalización de DeepSeek implica una secuencia cuidadosamente orquestada de pre-entrenamiento, fine-tuning dirigido y múltiples etapas de RL con diferentes señales de recompensa para lograr tanto un razonamiento sólido como capacidades generales de lenguaje.

**Código para Mostrar el Aprendizaje por Refuerzo (Conceptual y Simplificado):**

Es un desafío proporcionar un ejemplo de código directo y ejecutable que replique completamente el proceso de entrenamiento de RL de DeepSeek debido a su complejidad y escala. Sin embargo, el siguiente fragmento conceptual similar a PyTorch ilustra la idea central de GRPO y una recompensa basada en reglas:

```python
import torch
import torch.optim as optim
from transformers import AutoModelForCausalLM, AutoTokenizer

# Supón que tienes un modelo de lenguaje pre-entrenado y un tokenizador
model_name = "gpt2"  # Reemplazar con un modelo base más adecuado
policy_model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
optimizer = optim.AdamW(policy_model.parameters(), lr=5e-6)
device = "cuda" if torch.cuda.is_available() else "cpu"
policy_model.to(device)

def generate_responses(prompt, num_responses=4, max_length=128):
    input_tokens = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = policy_model.generate(
        input_tokens.input_ids,
        max_length=max_length,
        num_return_sequences=num_responses,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        pad_token_id=tokenizer.eos_token_id
    )
    responses = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    return responses

def calculate_accuracy_reward(response):
    # Ejemplo simplificado para un problema matemático: "¿Cuánto es 2 + 2?"
    if "2 + 2" in response and "4" in response:
        return 1.0
    else:
        return 0.0

def calculate_format_reward(response):
    if "" in response:
        return 0.5
    else:
        return 0.0

def calculate_combined_reward(response):
    accuracy_reward = calculate_accuracy_reward(response)
    format_reward = calculate_format_reward(response)
    return accuracy_reward + format_reward

def train_step(prompt, num_samples=4):
    optimizer.zero_grad()
    responses = generate_responses(prompt, num_samples=num_samples)
    rewards = torch.tensor([calculate_combined_reward(resp) for resp in responses]).float().to(device)

    # Actualización simplificado tipo GRPO: Incentivar respuestas con mayor recompensa
    best_reward_index = torch.argmax(rewards)
    best_response = responses[best_reward_index]
    inputs = tokenizer(prompt + best_response, return_tensors="pt").to(device)
    outputs = policy_model(**inputs, labels=inputs.input_ids)
    loss = outputs.loss
    loss.backward()
    optimizer.step()
    return loss.item(), best_response, rewards.tolist()

# Bucle de entrenamiento (muy simplificado)
num_episodes = 10
training_prompts = ["Resuelve: 2 + 2 = ?", "Explica el concepto de gravedad