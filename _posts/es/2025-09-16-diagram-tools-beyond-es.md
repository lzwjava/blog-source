---
audio: false
generated: true
image: false
lang: es
layout: post
model: mistralai/mistral-medium-3.1
title: Herramientas de Diagramas Más Allá de Graphviz y NetworkX
translated: true
type: note
---

Excelentes opciones más allá de Graphviz y NetworkX, agrupadas por cómo te gusta trabajar.

**Texto/DSL "diagramas como código"**
- **PlantUML:** UML completo (secuencia, clases, componentes, despliegue), modelo C4, actividades; ecosistema enorme.
- **Mermaid:** Sintaxis ligera tipo Markdown; ideal para diagramas de flujo, secuencia, clases, ER, estados; se renderiza de forma nativa en GitHub/GitLab.
- **D2 (de Terrastruct):** DSL de diagramas de propósito general y limpio con buen diseño automático; soporta capas y diagramas grandes.
- **Structurizr (C4):** Modelo primero (C4) con un DSL; exporta a PlantUML/Mermaid; bueno para documentación de arquitectura.
- **C4-PlantUML:** Plantillas del modelo C4 sobre PlantUML.
- **nomnoml:** Sintaxis mínima, bocetos rápidos de clases y relaciones.
- **Kroki:** Servidor que renderiza muchos DSLs (PlantUML, Mermaid, Graphviz) para pipelines de documentación.

**Code-first (generar diagramas desde código/IaC)**
- **diagrams (mingrammer, Python):** Diagramas de arquitectura cloud programáticos (AWS/Azure/GCP/K8s).
- **Ayudantes de Terraform:** Inframap (dibujar desde el estado), Blast Radius (gráficos interactivos desde Terraform).
- **AWS CDK:** cdk-dia para diagramas de arquitectura desde apps CDK.
- **Librerías Go/TS:** GoDiagrams (Go), ts-graphviz (TypeScript) para generación basada en código.

**Librerías de visualización web (gráficos interactivos)**
- **Cytoscape.js:** Visualización de grafos grandes, algoritmos de diseño, buen rendimiento.
- **D3.js:** Potente pero de bajo nivel para visuales personalizados de grafos/diagramas.
- **vis-network (vis.js):** Gráficos de red fáciles con física.
- **Sigma.js:** Renderizado rápido para grafos grandes.
- **ECharts:** Gráficos generales con módulo de grafos; resultados rápidos.
- **pyvis (Python):** Gráficos de red interactivos simples a través de Vis.js.

**Herramientas de diagramación GUI (arrastrar y soltar)**
- **diagrams.net (draw.io):** Gratuito, fácil, grandes librerías de formas (UML, iconos de cloud).
- **yEd/yFiles:** Gran diseño automático; yFiles es un SDK comercial, yEd es escritorio gratuito.
- **Lucidchart/Miro:** Herramientas web colaborativas; buenas para equipos.
- **OmniGraffle (macOS), Visual Paradigm, StarUML, Enterprise Architect:** Herramientas para UML/arquitectura.

**Herramientas específicas de arquitectura y dominio**
- **Modelo C4:** Structurizr, C4-PlantUML, extensiones C4 para Mermaid.
- **SaaS de arquitectura cloud:** Cloudcraft (AWS), Hava, Lucidscale, CloudSkew; importan desde cloud/IaC.
- **BPMN/Procesos:** Camunda Modeler, bpmn.io.
- **Secuencia/tiempos:** WebSequenceDiagrams, WaveDrom (diagramas de tiempos).
- **Diagramas ER/BD:** dbdiagram.io, SchemaSpy.

**Selecciones rápidas por escenario**
- Docs-as-code en Markdown/READMEs: Mermaid.
- UML completo + C4 con plantillas: PlantUML o Structurizr.
- Arquitectura cloud desde código/IaC: diagrams (Python), Inframap/Blast Radius (Terraform), cdk-dia (AWS CDK).
- Gráficos interactivos para apps web: Cytoscape.js o vis-network; para visualización personalizada, D3.js.
- Dibujo GUI rápido: diagrams.net (draw.io); para diseño automático, yEd.

Si compartes tus preferencias (texto vs GUI, imágenes estáticas vs interactivas, lenguajes que usas y tipos de diagramas como secuencia/C4/cloud/ER), puedo recomendarte una lista corta y plantillas de inicio.