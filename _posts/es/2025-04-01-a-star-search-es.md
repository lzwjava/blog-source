---
audio: false
generated: true
lang: es
layout: post
title: Algoritmo de Búsqueda A* (A-estrella)
translated: true
type: note
---

El algoritmo de búsqueda **A* (A-estrella)** es un popular algoritmo de búsqueda de caminos y recorrido de grafos utilizado en informática e inteligencia artificial. Se usa ampliamente para encontrar la ruta más corta desde un punto de inicio (o nodo) a un objetivo (o meta) en un grafo, mientras explora de manera eficiente las rutas posibles.

A* combina elementos del **Algoritmo de Dijkstra** (que garantiza el camino más corto) y de la **Búsqueda Voraz del Mejor Primero** (que intenta encontrar el objetivo lo más rápido posible). La característica clave de A* es que utiliza tanto el coste real para llegar a un nodo (desde el nodo de inicio) como una heurística que estima el coste desde ese nodo hasta el objetivo.

### Cómo funciona A*:
1.  **Comenzar con una lista abierta**: La lista abierta contiene nodos que aún no han sido explorados. Inicialmente, solo el nodo de inicio está en esta lista.
2.  **Calcular puntuaciones**: A cada nodo en la lista abierta se le asigna una puntuación basada en dos factores:
    - **g(n)**: El coste para llegar al nodo actual desde el nodo de inicio.
    - **h(n)**: Una estimación heurística del coste para llegar al objetivo desde el nodo actual (esto es específico del dominio, como la distancia en línea recta o la distancia euclidiana).
    - **f(n) = g(n) + h(n)**: El coste total estimado, utilizado para priorizar nodos. Los nodos con la f(n) más baja se exploran primero.
3.  **Expandir el nodo más prometedor**: Se elige el nodo con la puntuación f(n) más baja para explorarlo. Se mueve a una "lista cerrada" de nodos ya explorados.
4.  **Comprobar los vecinos**: El algoritmo examina los vecinos del nodo actual. Si un vecino no ha sido visitado o se puede alcanzar con un coste menor, se añade a la lista abierta.
5.  **Repetir** hasta que se alcanza el objetivo o la lista abierta está vacía (lo que indica que no existe una ruta).

### Componentes clave:
- **g(n)**: El coste real desde el nodo de inicio hasta el nodo actual.
- **h(n)**: La estimación heurística desde el nodo actual hasta el objetivo (puede variar dependiendo del problema).
- **f(n) = g(n) + h(n)**: El coste total que prioriza los nodos para su exploración.

### Heurísticas:
La función heurística es crítica para la eficiencia de A*. Una heurística común para la búsqueda de caminos basada en cuadrículas es la **distancia Manhattan** (suma de distancias horizontales y verticales) o la **distancia euclidiana** (distancia en línea recta) para espacios continuos.

### Casos de uso de ejemplo:
- **Sistemas de navegación** (GPS)
- **Videojuegos e IA** (búsqueda de caminos para personajes o agentes)
- **Robótica** (para planificar rutas eficientes)

En resumen, A* es un algoritmo altamente eficiente porque explora sistemáticamente las rutas basándose tanto en el coste conocido como en el coste futuro estimado, asegurando que encuentra la solución óptima cuando es posible.