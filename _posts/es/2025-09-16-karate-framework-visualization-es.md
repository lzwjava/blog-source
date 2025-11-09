---
audio: false
generated: true
image: false
lang: es
layout: post
model: mistralai/mistral-medium-3.1
title: Arquitectura de Visualización del Framework de Pruebas de Karate
translated: true
type: note
---

A continuación se presenta un script Python autocontenido que utiliza NetworkX y Matplotlib para dibujar una arquitectura/flujo de alto nivel de cómo funciona el framework de pruebas Karate. Agrupa los componentes por función (autoría, ejecución, runtime, protocolos/E/S, sistemas externos y reporting), y muestra el flujo típico desde los archivos de características (feature files) a través del motor hasta los protocolos y el reporting.

Instrucciones:
- pip install networkx matplotlib
- Opcionalmente, instala pygraphviz o pydot + graphviz si deseas un diseño más limpio; el script los detecta automáticamente y recurre a un diseño spring (spring_layout) como alternativa.

Código:

```python
import networkx as nx
import matplotlib.pyplot as plt

# Intenta usar Graphviz para un diseño más limpio si está disponible; de lo contrario, recurre a spring_layout.
def get_layout(G):
    try:
        # Prueba PyGraphviz
        from networkx.drawing.nx_agraph import graphviz_layout
        return graphviz_layout(G, prog="dot")
    except Exception:
        try:
            # Prueba pydot
            from networkx.drawing.nx_pydot import graphviz_layout
            return graphviz_layout(G, prog="dot")
        except Exception:
            # Alternativa: diseño spring
            return nx.spring_layout(G, k=1.2, seed=42)

G = nx.DiGraph()

# Definir nodos agrupados por categoría
nodes = {
    # Autoría
    "Feature files (.feature)": "Autoría",
    "Reusable features (call/read)": "Autoría",
    "karate-config.js / properties": "Autoría",
    "Test data (JSON/CSV)": "Autoría",

    # Ejecución
    "Runner (CLI/JUnit5/Maven/Gradle)": "Ejecución",
    "Parallel runner": "Ejecución",

    # Runtime
    "Karate engine (DSL interpreter)": "Runtime",
    "JS engine": "Runtime",
    "Variable/context": "Runtime",
    "Assertions & matchers": "Runtime",

    # Protocolos / E/S
    "HTTP/REST/SOAP/GraphQL": "Protocolos",
    "WebSocket": "Protocolos",
    "UI driver (web)": "Protocolos",
    "Mock server": "Protocolos",

    # Externo
    "External systems/services": "Externo",

    # Reporting
    "Reports (HTML, JUnit, JSON)": "Reporting",
    "CI/CD": "Reporting",
}

# Añadir nodos con atributo de categoría
for n, cat in nodes.items():
    G.add_node(n, category=cat)

# Definir bordes (u -> v) con etiquetas opcionales
edges = [
    # De Autoría a Ejecución
    ("Feature files (.feature)", "Runner (CLI/JUnit5/Maven/Gradle)", "execute"),
    ("karate-config.js / properties", "Runner (CLI/JUnit5/Maven/Gradle)", "configure"),
    ("Test data (JSON/CSV)", "Feature files (.feature)", "data-driven"),
    ("Reusable features (call/read)", "Feature files (.feature)", "reuse"),

    # De Ejecución a Runtime
    ("Runner (CLI/JUnit5/Maven/Gradle)", "Parallel runner", "optional"),
    ("Runner (CLI/JUnit5/Maven/Gradle)", "Karate engine (DSL interpreter)", "invoke"),
    ("Parallel runner", "Karate engine (DSL interpreter)", "parallelize"),

    # Internos del Runtime
    ("Karate engine (DSL interpreter)", "JS engine", "script expressions"),
    ("Karate engine (DSL interpreter)", "Variable/context", "manage state"),

    # Del Motor a los protocolos
    ("Karate engine (DSL interpreter)", "HTTP/REST/SOAP/GraphQL", "call APIs"),
    ("Karate engine (DSL interpreter)", "WebSocket", "send/receive"),
    ("Karate engine (DSL interpreter)", "UI driver (web)", "drive UI"),
    ("Karate engine (DSL interpreter)", "Mock server", "start/stub"),

    # De Protocolos a sistemas externos
    ("HTTP/REST/SOAP/GraphQL", "External systems/services", "requests"),
    ("WebSocket", "External systems/services", "messages"),
    ("UI driver (web)", "External systems/services", "browser/app"),
    ("Mock server", "External systems/services", "simulate"),

    # Respuestas que fluyen de vuelta al motor
    ("External systems/services", "Karate engine (DSL interpreter)", "responses"),

    # Aserciones y reporting
    ("Karate engine (DSL interpreter)", "Assertions & matchers", "verify"),
    ("Assertions & matchers", "Reports (HTML, JUnit, JSON)", "results"),
    ("Karate engine (DSL interpreter)", "Reports (HTML, JUnit, JSON)", "runtime logs"),
    ("Reports (HTML, JUnit, JSON)", "CI/CD", "publish"),
]

# Añadir bordes al grafo
for u, v, label in edges:
    G.add_edge(u, v, label=label)

# Colores por categoría
category_colors = {
    "Autoría": "#4C78A8",
    "Ejecución": "#F58518",
    "Runtime": "#B279A2",
    "Protocolos": "#54A24B",
    "Externo": "#9A9A9A",
    "Reporting": "#E45756",
}

# Construir lista de colores para los nodos
node_colors = [category_colors[G.nodes[n]["category"]] for n in G.nodes()]

# Calcular el diseño
pos = get_layout(G)

plt.figure(figsize=(14, 10))
# Dibujar nodos
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1600, alpha=0.9, linewidths=1.2, edgecolors="black")
# Dibujar bordes
nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle="-|>", arrowsize=16, width=1.2, connectionstyle="arc3,rad=0.06")
# Dibujar etiquetas
nx.draw_networkx_labels(G, pos, font_size=9, font_color="white")

# Dibujar un subconjunto de etiquetas de borde para reducir el desorden
important_edge_labels = {
    (u, v): d["label"]
    for u, v, d in G.edges(data=True)
    if d["label"] in {"execute", "invoke", "parallelize", "call APIs", "start/stub", "verify", "results", "publish"}
}
nx.draw_networkx_edge_labels(G, pos, edge_labels=important_edge_labels, font_size=8, label_pos=0.5, rotate=False)

# Leyenda
import matplotlib.patches as mpatches
legend_patches = [mpatches.Patch(color=col, label=cat) for cat, col in category_colors.items()]
plt.legend(handles=legend_patches, loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.05), frameon=False)

plt.title("Cómo Funciona el Framework de Pruebas Karate (Flujo de Alto Nivel)", fontsize=14)
plt.axis("off")
plt.tight_layout()
plt.show()
```

Lo que este diagrama transmite:
- **Autoría**: Escribes archivos .feature, puedes reutilizar otras características, configurar via karate-config, y alimentar con datos.
- **Ejecución**: Ejecutas via CLI/JUnit5/Maven/Gradle, opcionalmente en paralelo.
- **Runtime**: El motor de Karate interpreta el DSL, usa un motor JS para expresiones y gestiona el estado del escenario.
- **Protocolos/E/S**: El motor maneja HTTP (REST/SOAP/GraphQL), WebSocket y UI (via el driver de Karate). También puede iniciar un servidor mock (mock server) para simular dependencias.
- **Sistemas externos**: Los servicios reales o los simulados responden.
- **Reporting**: Las aserciones producen reportes (HTML, JUnit XML, JSON), que tu CI/CD puede publicar.

Si deseas que el diagrama se adapte a una parte específica (por ejemplo, solo pruebas de API, o enfatizando mocks o UI), avísame y ajustaré los nodos/bordes.