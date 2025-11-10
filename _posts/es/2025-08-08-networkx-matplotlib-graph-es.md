---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Tutorial de Gráficos con NetworkX y Matplotlib
translated: true
type: note
---

### Instalación de las Librerías
Para usar NetworkX y Matplotlib para dibujar diagramas, instálalos si es necesario:
- NetworkX: Maneja la creación y manipulación de grafos.
- Matplotlib: Proporciona capacidades de trazado.

Instalar mediante pip:
```bash
pip install networkx matplotlib
```

Para una representación más rápida, Matplotlib recomienda instalar NumPy (`pip install numpy`).

### Configuración Básica y Ejemplo
1. **Importar las librerías**:  
   ```python
   import networkx as nx
   import matplotlib.pyplot as plt
   ```

2. **Crear un grafo**:  
   Usa NetworkX para construir un grafo simple no dirigido (puedes personalizarlo con grafos dirigidos, aristas ponderadas, etc.):
   ```python
   G = nx.Graph()  # Crear un grafo vacío
   G.add_nodes_from([1, 2, 3, 4, 5])  # Añadir nodos (ej. 5 nodos)
   G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])  # Añadir aristas (conexiones)
   ```

3. **Dibujar y mostrar el diagrama**:  
   Usa el backend de Matplotlib para la visualización:
   ```python
   nx.draw(G, with_labels=True)  # Dibujar el grafo con etiquetas en los nodos
   plt.show()  # Mostrar el gráfico
   ```

Esto produce un diseño circular básico del grafo (un ciclo con 5 nodos).

### Personalizaciones Avanzadas
- **Diseños (Layouts)**: Controla las posiciones de los nodos (ej. aleatorio, diseño spring):
  ```python
  pos = nx.spring_layout(G)  # Diseño dirigido por fuerzas para redes realistas
  nx.draw(G, pos=pos, with_labels=True, node_color='lightblue', edge_color='gray')
  plt.title("Diagrama de Red")
  plt.show()
  ```
- **Estilos de nodos y aristas**: Personaliza la apariencia:
  ```python
  nx.draw(G, pos=pos, node_size=500, node_color='red', edge_width=2, font_size=10)
  ```
- **Grafos dirigidos**: Para relaciones jerárquicas, usa `nx.DiGraph`.
  ```python
  DG = nx.DiGraph()
  DG.add_edges_from([('A', 'B'), ('B', 'C')])
  nx.draw(DG, with_labels=True, arrows=True)
  plt.show()
  ```
- **Guardar el diagrama**: Exporta a un archivo en lugar de mostrarlo:
  ```python
  plt.savefig('diagrama.png')
  ```

### Consejos y Recursos
- Documentación de NetworkX (networkx.org) para tipos de grafos como árboles o mallas.
- Documentación de Matplotlib (matplotlib.org) para incrustar en GUIs o subgráficos.
- Para grafos grandes (>100 nodos), usa `nx.draw_networkx` o herramientas externas como Graphviz para mejor rendimiento.
- Experimenta en un cuaderno Jupyter para un trazado interactivo. Si surgen problemas, los errores comunes provienen de backends faltantes (instala mediante `pip install pyqt5` o similar para ventanas interactivas).