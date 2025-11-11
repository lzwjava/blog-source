---
audio: false
generated: true
lang: es
layout: post
title: Aprendizaje por Refuerzo con Retroalimentación Humana (RLHF) Explicado
translated: true
type: note
---

**Aprendizaje por Refuerzo con Retroalimentación Humana (RLHF)** es una técnica de aprendizaje automático utilizada para afinar modelos de IA, particularmente los grandes modelos de lenguaje (LLMs), para alinearlos mejor con las preferencias e instrucciones humanas. En lugar de depender únicamente de funciones de recompensa predefinidas, RLHF incorpora retroalimentación directa de humanos para guiar el proceso de aprendizaje.

**¿Por qué es importante RLHF?**

*   **Tareas Subjetivas:** RLHF sobresale en tareas donde el resultado deseado es difícil de definir con reglas explícitas o recompensas numéricas, como generar texto creativo, mantener conversaciones naturales o producir contenido útil e inofensivo.
*   **Matices y Alineación:** Ayuda a los modelos de IA a comprender y adherirse a preferencias humanas sutiles, consideraciones éticas y estilos de interacción deseados.
*   **Rendimiento Mejorado:** Los modelos entrenados con RLHF a menudo demuestran un rendimiento y una satisfacción del usuario significativamente mejorados en comparación con aquellos entrenados únicamente con aprendizaje por refuerzo tradicional o aprendizaje supervisado.

**Cómo funciona RLHF (Típicamente en tres etapas):**

1.  **Pre-entrenamiento y Ajuste Fino Supervisado (SFT):**
    *   Primero, un modelo de lenguaje base es pre-entrenado en un conjunto de datos masivo de texto y código para aprender comprensión y generación general del lenguaje.
    *   Este modelo pre-entrenado luego se afina a menudo usando aprendizaje supervisado en un conjunto de datos más pequeño de demostraciones de alta calidad del comportamiento deseado (por ejemplo, humanos escribiendo respuestas ideales a prompts). Este paso ayuda al modelo a entender el formato y estilo de las salidas esperadas.

2.  **Entrenamiento del Modelo de Recompensa:**
    *   Este es un paso crucial en RLHF. Se entrena un **modelo de recompensa** separado para predecir las preferencias humanas.
    *   Se presenta a anotadores humanos diferentes salidas del modelo SFT (o una versión posterior) para el mismo prompt de entrada. Ellos clasifican o califican estas salidas basándose en varios criterios (por ejemplo, utilidad, coherencia, seguridad).
    *   Estos datos de preferencia (por ejemplo, "la salida A es mejor que la salida B") se utilizan para entrenar el modelo de recompensa. El modelo de recompensa aprende a asignar una puntuación de recompensa escalar a cualquier salida del modelo, reflejando cuánto la preferiría un humano.

3.  **Ajuste Fino con Aprendizaje por Refuerzo:**
    *   El modelo de lenguaje original (inicializado desde el modelo SFT) se afina aún más usando aprendizaje por refuerzo.
    *   El modelo de recompensa entrenado en el paso anterior sirve como la función de recompensa del entorno.
    *   El agente de RL (el modelo de lenguaje) genera respuestas a los prompts, y el modelo de recompensa califica estas respuestas.
    *   El algoritmo de RL (a menudo Proximal Policy Optimization - PPO) actualiza la política del modelo de lenguaje (cómo genera texto) para maximizar las recompensas predichas por el modelo de recompensa. Esto incentiva al modelo de lenguaje a generar salidas que estén más alineadas con las preferencias humanas.
    *   Para evitar que el ajuste fino con RL se desvíe demasiado del comportamiento del modelo SFT (lo que podría conducir a resultados no deseados), a menudo se incluye un término de regularización (por ejemplo, una penalización de divergencia KL) en el objetivo de RL.

**Cómo hacer RLHF (Pasos simplificados):**

1.  **Recolectar Datos de Preferencia Humana:**
    *   Diseña prompts o tareas relevantes para el comportamiento de IA deseado.
    *   Genera múltiples respuestas a estos prompts usando tu modelo actual.
    *   Recluta anotadores humanos para comparar estas respuestas e indicar sus preferencias (por ejemplo, clasificarlas, elegir la mejor o calificarlas).
    *   Almacena estos datos como pares de (prompt, respuesta_preferida, respuesta_menos_preferida) o formatos similares.

2.  **Entrenar un Modelo de Recompensa:**
    *   Elige una arquitectura de modelo adecuada para tu modelo de recompensa (a menudo un modelo basado en transformer similar al modelo de lenguaje).
    *   Entrena el modelo de recompensa en los datos de preferencia humana recolectados. El objetivo es que el modelo de recompensa asigne puntuaciones más altas a las respuestas que los humanos prefirieron. Una función de pérdida común utilizada se basa en maximizar el margen entre las puntuaciones de las respuestas preferidas y menos preferidas.

3.  **Ajustar Fino el Modelo de Lenguaje con Aprendizaje por Refuerzo:**
    *   Inicializa tu modelo de lenguaje con los pesos del paso SFT (si realizaste uno).
    *   Utiliza un algoritmo de aprendizaje por refuerzo (como PPO).
    *   Para cada paso de entrenamiento:
        *   Muestra un prompt.
        *   Haz que el modelo de lenguaje genere una respuesta.
        *   Usa el modelo de recompensa entrenado para obtener una puntuación de recompensa para la respuesta generada.
        *   Actualiza los parámetros del modelo de lenguaje basándote en la señal de recompensa para incentivar acciones (generación de tokens) que conduzcan a recompensas más altas.
        *   Incluye un término de regularización (por ejemplo, divergencia KL) para mantener la política actualizada cerca de la política SFT.

**Ejemplo de Código (Conceptual y Simplificado usando PyTorch):**

Este es un ejemplo conceptual muy simplificado para ilustrar las ideas centrales. Una implementación completa de RLHF es significativamente más compleja e involucra bibliotecas como Hugging Face Transformers, Accelerate y bibliotecas de RL.

```python
import torch
import torch.nn as nn
import torch.optim as optim
from transformers import AutoModelForCausalLM, AutoTokenizer

# Supón que has recolectado datos de preferencia humana:
# Lista de tuplas: (prompt, respuesta_preferida, respuesta_menos_preferida)
preference_data = [
    ("Escribe una historia corta sobre un gato.", "Bigotes el gato vivía en una acogedora cabaña...", "Una historia de un gato. Fin."),
    ("Resume este artículo:", "El artículo discute...", "Resumen del artículo."),
    # ... más datos
]

# 1. Cargar modelo de lenguaje pre-entrenado y tokenizador
model_name = "gpt2"  # U otro modelo pre-entrenado adecuado
policy_model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
device = "cuda" if torch.cuda.is_available() else "cpu"
policy_model.to(device)

# 2. Definir un Modelo de Recompensa simple
class RewardModel(nn.Module):
    def __init__(self, base_model):
        super().__init__()
        self.base_model = base_model.transformer  # Usar las capas transformer
        self.v_head = nn.Linear(base_model.config.n_embd, 1)

    def forward(self, input_ids, attention_mask):
        outputs = self.base_model(input_ids=input_ids, attention_mask=attention_mask)
        last_hidden_states = outputs.last_hidden_state
        reward = self.v_head(last_hidden_states[:, -1])  # Obtener recompensa del último token
        return reward

reward_model = RewardModel(policy_model)
reward_model.to(device)
reward_optimizer = optim.AdamW(reward_model.parameters(), lr=1e-5)
reward_criterion = nn.MarginRankingLoss(margin=1.0) # Incentivar mayor recompensa para el preferido

# Entrenar el Modelo de Recompensa
num_reward_epochs = 3
for epoch in range(num_reward_epochs):
    for prompt, preferred, less_preferred in preference_data:
        preferred_tokens = tokenizer(prompt + preferred, return_tensors="pt", truncation=True, max_length=128).to(device)
        less_preferred_tokens = tokenizer(prompt + less_preferred, return_tensors="pt", truncation=True, max_length=128).to(device)

        preferred_reward = reward_model(**preferred_tokens)
        less_preferred_reward = reward_model(**less_preferred_tokens)

        labels = torch.ones(preferred_reward.size(0)).to(device) # Queremos preferred > less preferred
        loss = reward_criterion(preferred_reward, less_preferred_reward, labels)

        reward_optimizer.zero_grad()
        loss.backward()
        reward_optimizer.step()
    print(f"Época Recompensa {epoch+1}, Pérdida: {loss.item()}")

# 3. Ajuste Fino con Aprendizaje por Refuerzo (Conceptual - PPO es complejo)
policy_optimizer = optim.AdamW(policy_model.parameters(), lr=5e-6)

num_rl_episodes = 5
for episode in range(num_rl_episodes):
    for prompt in [data[0] for data in preference_data]: # Muestrear prompts
        input_tokens = tokenizer(prompt, return_tensors="pt").to(device)
        output_sequences = policy_model.generate(
            input_tokens.input_ids,
            max_length=60,
            num_return_sequences=1,
            do_sample=True,
            top_k=50,
            top_p=0.95,
        )
        generated_response = tokenizer.decode(output_sequences[0], skip_special_tokens=True)

        response_tokens = tokenizer(prompt + generated_response, return_tensors="pt", truncation=True, max_length=128).to(device)
        reward = reward_model(**response_tokens)

        # (Simplificado) Actualización de Política - En realidad, PPO usa métodos más sofisticados
        loss = -reward.mean() # Intentar maximizar la recompensa
        policy_optimizer.zero_grad()
        loss.backward()
        policy_optimizer.step()

    print(f"Episodio RL {episode+1}, Recompensa: {reward.item()}, Respuesta: {generated_response}")

print("¡Entrenamiento RLHF Terminado!")
```

**Desafíos Clave en RLHF:**

*   **Recolección de Datos:** Obtener datos de preferencia humana diversos y de alta calidad puede ser costoso y llevar mucho tiempo.
*   **Subjetividad y Sesgo:** Las preferencias humanas pueden ser subjetivas y pueden contener sesgos, que pueden ser aprendidos por el modelo de recompensa.
*   **Reward Hacking:** El agente de RL podría encontrar formas de explotar el modelo de recompensa que no se alineen con las verdaderas preferencias humanas.
*   **Escalabilidad:** Escalar RLHF a modelos y conjuntos de datos muy grandes requiere recursos computacionales significativos y una ingeniería cuidadosa.
*   **Inestabilidad:** Entrenar modelos RLHF puede ser inestable y requiere un ajuste cuidadoso de los hiperparámetros.

A pesar de estos desafíos, RLHF ha demostrado ser una técnica poderosa para alinear modelos de IA con valores humanos y es un componente clave en el desarrollo de modelos de lenguaje de vanguardia como ChatGPT y otros.