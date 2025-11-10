---
audio: false
generated: true
lang: es
layout: post
title: 'Gimnasio: El Gimnasio Moderno para el Aprendizaje por Refuerzo'
translated: true
type: note
---

La biblioteca Gym se refiere a un popular kit de herramientas de Python originalmente desarrollado por OpenAI para el aprendizaje por refuerzo (RL), un subcampo del aprendizaje automático donde los agentes aprenden a tomar decisiones interactuando con entornos para maximizar las recompensas. Proporciona una API estandarizada y una colección de entornos de referencia (como juegos, simulaciones robóticas y problemas clásicos de control) para desarrollar, probar y comparar algoritmos de RL. Esto facilita que investigadores y desarrolladores prototipen sin tener que construir entornos desde cero.

Características principales incluyen:
- **Entornos**: Tareas preconstruidas como CartPole (equilibrar un poste), juegos de Atari o simulaciones físicas MuJoCo.
- **Sencillez de la API**: Creas un entorno con `gym.make("NombreDelEntorno")`, y luego usas métodos como `reset()` para comenzar, `step(acción)` para interactuar y obtener observaciones/recompensas, y `render()` para visualizar.
- **Extensibilidad**: Los usuarios pueden crear entornos personalizados creando subclases de las clases base de Gym.
- **Integración**: Funciona bien con bibliotecas como Stable Baselines, RLlib o PyTorch/TensorFlow para implementar agentes de RL.

Sin embargo, el OpenAI Gym original ya no se mantiene activamente y quedó obsoleto desde aproximadamente 2021. Se recomienda usar **Gymnasium**, que es un fork directo y su continuación por parte de la Farama Foundation. Gymnasium es totalmente compatible (puedes importarlo como `import gymnasium as gym`), añade mejoras como mejores entornos vectorizados para entrenamiento en paralelo, comprobación de tipos más estricta y actualizaciones continuas. La instalación es mediante `pip install gymnasium`, con extras como `pip install gymnasium[atari]` para entornos específicos.

Ejemplo de uso básico en Python:
```python
import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset(seed=42)

for _ in range(1000):
    action = env.action_space.sample()  # Acción aleatoria (un agente aprendería mejores)
    observation, reward, terminated, truncated, info = env.step(action)
    
    if terminated or truncated:
        observation, info = env.reset()

env.close()
```

Si estás empezando con RL, Gymnasium es la opción recomendada hoy en día para la mayoría de proyectos.

[OpenAI Gym GitHub](https://github.com/openai/gym)  
[Gymnasium Documentation](https://gymnasium.farama.org/)  
[Gym Documentation (Legacy)](https://www.gymlibrary.dev/)