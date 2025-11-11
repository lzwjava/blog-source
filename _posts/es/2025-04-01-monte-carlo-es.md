---
audio: false
generated: true
lang: es
layout: post
title: Búsqueda en Árbol de Montecarlo
translated: true
type: note
---

Adentrémonos en una guía completa sobre **Monte Carlo Tree Search (MCTS)**, un algoritmo poderoso ampliamente utilizado en problemas de toma de decisiones, especialmente en juegos e inteligencia artificial. Lo desglosaré paso a paso, cubriendo sus orígenes, conceptos fundamentales, mecánica, implementación, fortalezas, debilidades y aplicaciones—todo lo que necesitas para comprenderlo a fondo.

---

### ¿Qué es Monte Carlo Tree Search?

Monte Carlo Tree Search es un algoritmo de búsqueda heurística que combina la precisión de la búsqueda en árbol con la aleatoriedad de los métodos de Monte Carlo. Es particularmente efectivo para problemas con espacios de decisión grandes y complejos donde explorar exhaustivamente todas las posibilidades (como en minimax) no es factible. MCTS construye un árbol de búsqueda parcial de forma incremental, utilizando simulaciones aleatorias para guiar su exploración hacia movimientos prometedores.

- **Orígenes**: MCTS surgió a mediados de la década de 2000, con contribuciones significativas de Rémi Coulom (2006) y otros. Ganó fama cuando impulsó la IA para jugar Go, notablemente en AlphaGo, revolucionando cómo las computadoras abordan juegos con vastos espacios de estados.
- **Caso de Uso Clave**: Juegos como Go, Chess, Poker, e incluso problemas del mundo real como planificación u optimización.

---

### Conceptos Fundamentales

MCTS opera en un **árbol** donde:
- **Nodos** representan estados del juego o puntos de decisión.
- **Aristas** representan acciones o movimientos que conducen a nuevos estados.
- La **raíz** es el estado actual desde el cual se toman las decisiones.

El algoritmo equilibra **exploración** (probar nuevos movimientos) y **explotación** (centrarse en movimientos buenos conocidos) utilizando un enfoque estadístico. No requiere una función de evaluación perfecta, solo una forma de simular resultados.

---

### Las Cuatro Fases de MCTS

MCTS itera a través de cuatro pasos distintos en cada ciclo de simulación:

#### 1. **Selección**
- Comienza en la raíz y recorre el árbol hasta un nodo hoja (un nodo no completamente expandido o un estado terminal).
- Utiliza una **política de selección** para elegir nodos hijos. La más común es la fórmula **Upper Confidence Bound applied to Trees (UCT)**:
  \\[
  UCT = \bar{X}_i + C \sqrt{\frac{\ln(N)}{n_i}}
  \\]
  - \\(\bar{X}_i\\): Recompensa promedio (tasa de victorias) del nodo.
  - \\(n_i\\): Número de visitas al nodo.
  - \\(N\\): Número de visitas al nodo padre.
  - \\(C\\): Constante de exploración (típicamente \\(\sqrt{2}\\) o ajustada por problema).
- UCT equilibra la explotación (\\(\bar{X}_i\\)) y la exploración (el término \\(\sqrt{\frac{\ln(N)}{n_i}}\\)).

#### 2. **Expansión**
- Si el nodo hoja seleccionado no es terminal y tiene hijos no visitados, expándelo añadiendo uno o más nodos hijos (que representan movimientos no probados).
- Típicamente, solo se añade un hijo por iteración para controlar el uso de memoria.

#### 3. **Simulación (Rollout)**
- Desde el nodo recién expandido, ejecuta una **simulación aleatoria** (o rollout) hasta un estado terminal (por ejemplo, victoria/derrota/empate).
- La simulación utiliza una política ligera—a menudo movimientos aleatorios uniformes—ya que evaluar cada estado con precisión es demasiado costoso.
- El resultado (por ejemplo, +1 para una victoria, 0 para un empate, -1 para una derrota) se registra.

#### 4. **Retropropagación**
- Propaga el resultado de la simulación hacia arriba en el árbol, actualizando las estadísticas para cada nodo visitado:
  - Incrementa el contador de visitas (\\(n_i\\)).
  - Actualiza la recompensa total (por ejemplo, suma de victorias o promedio de tasa de victorias).
- Esto refina el conocimiento del árbol sobre qué caminos son prometedores.

Repite estos pasos durante muchas iteraciones (por ejemplo, miles), luego elige el mejor movimiento desde la raíz basándose en el hijo más visitado o la recompensa promedio más alta.

---

### Cómo Funciona MCTS: Un Ejemplo

Imagina un juego simple de tres en raya:
1. **Raíz**: Estado actual del tablero (por ejemplo, turno de X con un tablero parcialmente lleno).
2. **Selección**: UCT elige un movimiento prometedor (por ejemplo, colocar X en el centro) basado en simulaciones previas.
3. **Expansión**: Añade un nodo hijo para un movimiento no probado (por ejemplo, la respuesta de O en una esquina).
4. **Simulación**: Juega movimientos aleatorios hasta que el juego termina (por ejemplo, gana X).
5. **Retropropagación**: Actualiza estadísticas—el movimiento al centro obtiene +1 de recompensa, el contador de visitas aumenta.

Después de miles de iteraciones, el árbol revela que colocar X en el centro tiene una alta tasa de victorias, por lo que se elige.

---

### Pseudocódigo

Aquí hay una implementación básica de MCTS:

```python
class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.reward = 0

def mcts(root, iterations):
    for _ in range(iterations):
        node = selection(root)
        if not node.state.is_terminal():
            node = expansion(node)
        reward = simulation(node.state)
        backpropagation(node, reward)
    return best_child(root)

def selection(node):
    while node.children and not node.state.is_terminal():
        node = max(node.children, key=uct)
    return node

def expansion(node):
    untried_moves = node.state.get_untried_moves()
    if untried_moves:
        move = random.choice(untried_moves)
        new_state = node.state.apply_move(move)
        child = Node(new_state, parent=node)
        node.children.append(child)
        return child
    return node

def simulation(state):
    current = state.clone()
    while not current.is_terminal():
        move = random.choice(current.get_moves())
        current.apply_move(move)
    return current.get_result()

def backpropagation(node, reward):
    while node:
        node.visits += 1
        node.reward += reward
        node = node.parent

def uct(child):
    if child.visits == 0:
        return float('inf')  # Explorar nodos no visitados
    return (child.reward / child.visits) + 1.41 * math.sqrt(math.log(child.parent.visits) / child.visits)

def best_child(node):
    return max(node.children, key=lambda c: c.visits)  # O usar reward/visits
```

---

### Fortalezas de MCTS

1. **Algoritmo Anytime**: Detenlo en cualquier momento y obtén un movimiento razonable basado en las estadísticas actuales.
2. **No Necesita Función de Evaluación**: Se basa en simulaciones, no en heurísticas específicas del dominio.
3. **Escalable**: Funciona en espacios de estados enormes (por ejemplo, Go con \\(10^{170}\\) posiciones posibles).
4. **Adaptativo**: Se centra naturalmente en ramas prometedoras a medida que aumentan las iteraciones.

---

### Debilidades de MCTS

1. **Computacionalmente Intensivo**: Requiere muchas simulaciones para buenos resultados, lo que puede ser lento sin optimización.
2. **Exploración Superficial**: Puede perder estrategias profundas si las iteraciones son limitadas.
3. **Dependencia de la Aleatoriedad**: Políticas de rollout deficientes pueden sesgar los resultados; la calidad depende de la precisión de la simulación.
4. **Uso de Memoria**: El crecimiento del árbol puede ser un cuello de botella en entornos con memoria limitada.

---

### Mejoras y Variaciones

Para abordar las debilidades, MCTS a menudo se mejora:
- **Heurísticas en Rollouts**: Usar conocimiento del dominio (por ejemplo, preferir movimientos centrales en tres en raya) en lugar de pura aleatoriedad.
- **Paralelización**: Ejecutar múltiples simulaciones concurrentemente (paralelización de raíz o de árbol).
- **RAVE (Rapid Action Value Estimation)**: Compartir estadísticas entre movimientos similares para acelerar la convergencia.
- **Integración con Redes Neuronales**: Como en AlphaGo, usar redes neuronales para guiar la selección (policy network) y evaluar estados (value network).

---

### Aplicaciones

1. **Juegos**:
   - Go (el avance de AlphaGo).
   - Chess (combinado con redes neuronales en motores como Leela Chess Zero).
   - Poker (maneja información imperfecta con adaptaciones).
2. **Robótica**: Planificación de rutas en entornos inciertos.
3. **Optimización**: Resolver problemas combinatorios como programación o asignación de recursos.
4. **Estrategia en Tiempo Real**: Toma de decisiones en escenarios dinámicos e impredecibles.

---

### Consejos Prácticos para la Implementación

- **Ajusta \\(C\\)**: Ajusta la constante de exploración UCT según tu problema (\\(C = \sqrt{2}\\) es un punto de partida).
- **Limita el Crecimiento del Árbol**: Poda nodos o limita la expansión para gestionar la memoria.
- **Optimiza los Rollouts**: Usa simulaciones ligeras o heurísticas para ahorrar tiempo.
- **Prueba Iteraciones**: Experimenta con 100, 1,000 o 10,000 iteraciones para equilibrar velocidad y calidad.

---

### Conclusión

MCTS es un algoritmo versátil y elegante que brilla en dominios donde los métodos de búsqueda tradicionales fallan. Su belleza radica en su simplicidad—simulaciones aleatorias guiadas por un árbol en crecimiento—aún así, escala para abordar algunos de los problemas más difíciles en IA. Ya sea que estés programando una IA para juegos o resolviendo una tarea de planificación, MCTS ofrece un punto de partida robusto, especialmente cuando se combina con mejoras modernas como las redes neuronales.

Si lo deseas, puedo guiarte a través de una implementación específica (por ejemplo, para tres en raya) o explorar un aspecto particular—como el ajuste de UCT o MCTS paralelo—con más detalle. ¿Qué opinas?