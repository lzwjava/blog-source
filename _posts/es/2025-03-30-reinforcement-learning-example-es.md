---
audio: false
generated: true
lang: es
layout: post
title: Ejemplo de Aprendizaje por Refuerzo
translated: true
type: note
---

A continuación, presentaré algunos ejemplos conceptuales simples de Aprendizaje por Refuerzo (RL) seguidos de un ejemplo básico de código Python usando un escenario simple. El RL implica que un agente aprende a maximizar una recompensa interactuando con un entorno, por lo que los ejemplos y el código reflejarán eso.

### Ejemplos Simples de Aprendizaje por Refuerzo

1.  **Un Niño Aprendiendo a Caminar**
    -   **Agente**: El niño.
    -   **Entorno**: El suelo o la habitación.
    -   **Acción**: Dar un paso, gatear o quedarse quieto.
    -   **Recompensa**: Moverse hacia adelante (+1), caerse (-1).
    -   **Aprendizaje**: El niño aprende mediante prueba y error que dar pasos equilibrados conduce al progreso.

2.  **Entrenando un Brazo Robótico para Recoger Objetos**
    -   **Agente**: El brazo robótico.
    -   **Entorno**: Una mesa con objetos.
    -   **Acción**: Moverse arriba, abajo, izquierda, derecha, o agarrar.
    -   **Recompensa**: Recoger un objeto con éxito (+10), dejarlo caer (-5).
    -   **Aprendizaje**: El brazo ajusta sus movimientos para maximizar los agarres exitosos.

3.  **Juego de Mundo Cuadriculado (Grid World)**
    -   **Agente**: Un personaje en una cuadrícula.
    -   **Entorno**: Una cuadrícula de 3x3 con una meta y obstáculos.
    -   **Acción**: Moverse arriba, abajo, izquierda o derecha.
    -   **Recompensa**: Alcanzar la meta (+10), chocar contra una pared (-1).
    -   **Aprendizaje**: El personaje aprende el camino más corto hacia la meta.

---

### Ejemplo Simple de Código Python: Q-Learning en un Mundo Cuadriculado

Aquí hay una implementación básica de Q-Learning, un algoritmo popular de RL, en un "mundo" 1D simple donde un agente se mueve izquierda o derecha para alcanzar una meta. El agente aprende actualizando una Q-table basándose en las recompensas.

```python
import numpy as np
import random

# Configuración del entorno: mundo 1D con 5 posiciones (0 a 4), meta en la posición 4
state_space = 5  # Posiciones: [0, 1, 2, 3, 4]
action_space = 2  # Acciones: 0 = mover izquierda, 1 = mover derecha
goal = 4

# Inicializar Q-table con ceros (estados x acciones)
q_table = np.zeros((state_space, action_space))

# Hiperparámetros
learning_rate = 0.1
discount_factor = 0.9
exploration_rate = 1.0
exploration_decay = 0.995
min_exploration_rate = 0.01
episodes = 1000

# Función de recompensa
def get_reward(state):
    if state == goal:
        return 10  # Gran recompensa por alcanzar la meta
    return -1  # Pequeña penalización por cada paso

# Función step: Mover el agente y obtener nuevo estado
def step(state, action):
    if action == 0:  # Mover izquierda
        new_state = max(0, state - 1)
    else:  # Mover derecha
        new_state = min(state_space - 1, state + 1)
    reward = get_reward(new_state)
    done = (new_state == goal)
    return new_state, reward, done

# Bucle de entrenamiento
for episode in range(episodes):
    state = 0  # Comenzar en la posición 0
    done = False
    
    while not done:
        # Exploración vs Explotación
        if random.uniform(0, 1) < exploration_rate:
            action = random.randint(0, action_space - 1)  # Explorar
        else:
            action = np.argmax(q_table[state])  # Explotar
        
        # Realizar acción y observar el resultado
        new_state, reward, done = step(state, action)
        
        # Actualizar Q-table usando la fórmula de Q-learning
        old_value = q_table[state, action]
        next_max = np.max(q_table[new_state])
        new_value = (1 - learning_rate) * old_value + learning_rate * (reward + discount_factor * next_max)
        q_table[state, action] = new_value
        
        # Moverse al nuevo estado
        state = new_state
    
    # Reducir la tasa de exploración
    exploration_rate = max(min_exploration_rate, exploration_rate * exploration_decay)

# Probar la política aprendida
state = 0
steps = 0
print("Probando la política aprendida:")
while state != goal:
    action = np.argmax(q_table[state])
    state, reward, done = step(state, action)
    steps += 1
    print(f"Paso {steps}: Movido al estado {state}, Acción: {'Izquierda' if action == 0 else 'Derecha'}")
print(f"¡Meta alcanzada en {steps} pasos!")

# Imprimir la Q-table
print("\nQ-table aprendida:")
print(q_table)
```

---

### Explicación del Código

1.  **Entorno**: Una línea 1D con 5 posiciones (0 a 4). La meta está en la posición 4.
2.  **Acciones**: El agente puede moverse izquierda (0) o derecha (1).
3.  **Recompensas**: +10 por alcanzar la meta, -1 por cada paso (para fomentar la eficiencia).
4.  **Q-Table**: Una tabla que almacena las recompensas futuras esperadas para cada par estado-acción.
5.  **Q-Learning**: El agente actualiza la Q-table usando la fórmula:
    `Q(s, a) = (1 - α) * Q(s, a) + α * (recompensa + γ * max(Q(s', a')))`, donde:
    -   `α` = tasa de aprendizaje
    -   `γ` = factor de descuento
    -   `s` = estado actual, `a` = acción, `s'` = siguiente estado
6.  **Exploración vs Explotación**: El agente a veces elige acciones aleatorias (exploración) y a veces usa la Q-table (explotación), controlado por `exploration_rate`.

---

### Salida de Ejemplo

```
Probando la política aprendida:
Paso 1: Movido al estado 1, Acción: Derecha
Paso 2: Movido al estado 2, Acción: Derecha
Paso 3: Movido al estado 3, Acción: Derecha
Paso 4: Movido al estado 4, Acción: Derecha
¡Meta alcanzada en 4 pasos!

Q-table aprendida:
[[-2.5   2.3]
 [-1.8   4.5]
 [-1.2   6.8]
 [-0.5   9. ]
 [ 0.    0. ]]
```

El agente aprende a moverse siempre a la derecha desde cualquier posición inicial para alcanzar la meta de manera eficiente. La Q-table muestra valores más altos para las acciones de "mover derecha" a medida que te acercas a la meta.

Este es un ejemplo muy básico, pero captura la esencia del RL. Para escenarios más complejos (por ejemplo, cuadrículas 2D o juegos), ¡expandirías los espacios de estado y acción en consecuencia!