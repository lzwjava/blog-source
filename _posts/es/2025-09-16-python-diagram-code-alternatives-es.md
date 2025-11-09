---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Alternativas de Herramientas de Diagrama como Código en Python
translated: true
type: note
---

Aquí tienes opciones compatibles con Python (más allá de Graphviz y NetworkX) que hacen que generar diagramas de diseño/arquitectura de software sea sencillo. Las he agrupado por caso de uso e incluido notas rápidas y pequeños ejemplos.

**Diagrama-como-código (UML, C4, diagramas de flujo, secuencias)**
- PlantUML (vía python-plantuml o JAR local)
  - Excelente para UML: clases, secuencias, componentes, estados, actividades, despliegue.
  - Funciona bien en CI y con documentación.
  - Ejemplo:
    @startuml
    class User
    class Order
    User "1" --> "*" Order
    @enduml
- Mermaid (usa CLI o un servidor Kroki; Python puede llamar al renderizador)
  - Sintaxis simple para secuencias, clases, diagramas de flujo, ER, estados, etc.
  - Se renderiza bien en muchas herramientas de documentación y wikis.
  - Ejemplo:
    flowchart LR
      API --> DB
- Familia BlockDiag (blockdiag, seqdiag, actdiag, nwdiag)
  - Herramientas en Python puro para generar diagramas de bloques, secuencias, actividades y redes a partir de texto simple.
  - Ejemplo (seqdiag):
    seqdiag {
      Client -> API [label = "GET /users"];
      API -> DB [label = "query"];
    }
- Structurizr (modelo C4; cliente Python comunitario)
  - Modela la arquitectura de software (Contexto, Contenedor, Componente) y renderiza mediante Structurizr/PlantUML.
  - Fuerte para documentación de arquitectura multi-vista y flujos de trabajo ADR.
- Kroki (diagrama-como-servicio; disponible cliente Python)
  - Renderiza muchos DSLs (PlantUML, Mermaid, Graphviz, BPMN, etc.) mediante una única API HTTP desde Python.

**Arquitectura de nube e infraestructura**
- Diagrams (por mingrammer)
  - Diagrama-como-código para arquitectura de nube/sistema con iconos oficiales de proveedores (AWS, Azure, GCP, K8s, on-prem).
  - Muy popular para vistas generales de arquitectura.
  - Ejemplo:
    from diagrams import Diagram
    from diagrams.aws.compute import EC2
    from diagrams.aws.database import RDS
    with Diagram("Web Service", show=False):
        EC2("api") >> RDS("db")

**Visualizaciones interactivas de red/grafos (útiles para mapas de sistema, dependencias)**
- PyVis (vis.js)
  - Código mínimo para producir grafos HTML interactivos.
  - Ejemplo:
    from pyvis.network import Network
    net = Network(); net.add_nodes(["API","DB"]); net.add_edge("API","DB"); net.show("arch.html")
- Dash Cytoscape / ipycytoscape (Cytoscape.js)
  - Para grafos interactivos y personalizables en apps Dash o Jupyter. Bueno para explorar dependencias y flujos.
- Plotly
  - Construye diagramas nodo-enlace interactivos con estilos personalizados; fácil de embeber/compartir.
- Bokeh / HoloViews
  - Gráficos interactivos con soporte para redes; bueno para dashboards centrados en Python.
- python-igraph
  - Librería de grafos rápida con trazado integrado; adecuada cuando necesitas algoritmos de diseño más diagramas exportables.

**Integraciones con documentación (mantén los diagramas cerca de tu docs)**
- Extensiones de Sphinx: sphinxcontrib-plantuml, sphinxcontrib-mermaid, sphinxcontrib-blockdiag
  - Escribe diagramas en línea en reStructuredText/Markdown y constrúyelos en tu pipeline de documentación.
- Plugins de MkDocs (para Mermaid/PlantUML)
  - Conveniente para sitios estáticos modernos.

**Ingeniería inversa de código y arquitectura**
- pyreverse de pylint
  - Genera diagramas UML de clases y paquetes a partir de código Python (a menudo se renderiza via Graphviz, pero el flujo de trabajo es simple).
- pydeps
  - Crea grafos de importación/dependencia de paquetes Python, útil para mapas de arquitectura en codebases grandes.

**Diagramas especializados**
- SchemDraw
  - Diagramas de circuitos/lógica/flujo programáticos en Python; salida vectorial limpia.
- railroad-diagrams
  - Genera diagramas de sintaxis/gramática (útil para documentación de protocolos/especificaciones).

**Consejos para elegir**
- Documentación rápida UML/secuencias: PlantUML o Mermaid.
- Pósters de arquitectura de nube/sistema: Diagrams (mingrammer).
- Exploración interactiva y compartición: PyVis o Dash Cytoscape.
- Modelo C4 y documentación de arquitectura viva: Structurizr (con PlantUML/Mermaid vía exportación).
- Diagramas automáticos desde código: pyreverse, pydeps.

Si me dices tus tipos de diagrama objetivo (clases UML, secuencias, C4, nube, flujo de datos, dependencias de paquetes) y formato de salida (PNG/SVG/HTML/embebido en docs), puedo sugerirte una configuración mínima y una plantilla de inicio.