---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Modelos de IA de SenseTime se Retrasan Respecto a sus Rivales
translated: true
type: note
---

### Comprendiendo los Modelos DayDayNew y Riri Xin de SenseTime

SenseTime, uno de los "dragones de IA" de China, ha sido un líder en visión por computadora y reconocimiento facial desde 2014. En la era de la IA generativa, han girado hacia los modelos de lenguaje grande (LLM) bajo el paraguas de SenseNova. "DayDayNew" (a menudo estilizado como "日日新" en chino) se refiere a su plataforma de IA interactiva y serie de modelos, con el último DayDayNew 6.5 presentado en la Conferencia Mundial de Inteligencia Artificial (WAIC) a fines de octubre de 2025. Está diseñado para tareas multimodales como procesar texto, imágenes y videos, con un fuerte énfasis en aplicaciones empresariales, integraciones de API y vínculos con hardware (por ejemplo, las gafas de IA de Xiaomi). "Riri Xin" (modelo integrado 日日新) es un LLM multimodal ligero relacionado, lanzado a principios de 2025, que se centra en el razonamiento profundo, la generación cross-modal y la eficiencia para dispositivos de consumo.

Estos modelos apuntan a competir en el panorama de IA hipercompetitivo de China, pero de hecho se han quedado rezagados en los benchmarks de rendimiento bruto en comparación con actores de vanguardia como DeepSeek (DeepSeek-V3), Kimi (serie Kimi de Moonshot AI) y MiniMax (serie ABAB). Para contexto, a mediados de 2025, en los benchmarks SuperCLUE (una evaluación clave de LLM chinos para razonamiento, matemáticas y capacidades generales), DeepSeek-V3 encabezó las puntuaciones generales (~85/100), Kimi K2 alcanzó ~82, y MiniMax ABAB ~80, mientras que las variantes de SenseNova (incluidas las integraciones de Riri Xin) se mantuvieron alrededor de 70-75, perdiendo a menudo frente a MiniMax en tareas de razonamiento y codificación. Brechas similares aparecen en evaluaciones globales como MMLU o HumanEval, donde SenseTime prioriza lo multimodal sobre el razonamiento de texto puro.

### ¿Por qué el Rezago frente a DeepSeek, Kimi y MiniMax?

Varios factores explican esto, enraizados en el legado de SenseTime, la dinámica del mercado y las presiones externas:

1.  **Giro Tardío de la Visión por Computadora a los LLM**: SenseTime construyó su imperio sobre IA de percepción (por ejemplo, tecnología de vigilancia), ingresando completamente en los LLM generativos con SenseNova recién en 2023. Esto retrasó su escalado en comparación con las startups nativas de LLM. DeepSeek (fundada en 2023) y Moonshot AI (Kimi, 2023) comenzaron con un enfoque láser en modelos eficientes y de pesos abiertos, iterando rápidamente en arquitecturas como la atención dispersa para un entrenamiento rentable. MiniMax, a pesar de ser más joven (2021), se optimizó desde el primer día para aplicaciones de consumo como la generación de video (Hailuo).

2.  **Sanciones de la Lista de Entidades de EE.UU.**: Incluida en la lista negra de EE.UU. en 2019 por supuestos problemas de derechos humanos, SenseTime enfrenta un acceso restringido a chips avanzados (por ejemplo, GPUs de NVIDIA) y tecnología estadounidense. Esto dificulta el entrenamiento a la escala de sus rivales: DeepSeek utiliza chips nacionales Huawei Ascend de manera innovadora, mientras que Kimi y MiniMax aprovechan configuraciones híbridas sin las mismas restricciones de exportación. Resultado: actualizaciones de modelos más lentas y costos más altos, ampliando la brecha de rendimiento.

3.  **Startups Ágiles vs. Gigante Establecido**: SenseTime es una empresa pública (cotizada en HKEX) con ingresos de ~$1B+, que atiende a clientes empresariales (por ejemplo, bancos, gobiernos). Esto trae burocracia y un enfoque en soluciones multimodales y compatibles sobre benchmarks de última generación. En contraste:
    - DeepSeek enfatiza modelos "rápidos, baratos y abiertos", encabezando las listas de código abierto con bajos costos de inferencia.
    - Kimi sobresale en el razonamiento de contexto largo (hasta 200K tokens), rivalizando con el o1 de OpenAI.
    - MiniMax brilla en multimodal (texto a video) y eficiencia, a menudo superando a SenseTime cara a cara.

    Irónicamente, los fundadores de MiniMax (Yan Junjie y Zhou Yucong) son exingenieros de SenseTime que dirigieron cadenas de herramientas de aprendizaje profundo allí. Se fueron para construir una startup más ágil, llevando esa experiencia para superar a su antiguo empleador, lo que destaca cómo la movilidad de talento impulsa la carrera armamentística de IA en China.

4.  **Dinámica de Benchmarks e Hype**: Las evaluaciones chinas como SuperCLUE premian el razonamiento/matemáticas, áreas donde las startups se sobre-enfocan. La fortaleza de SenseTime es la integración (por ejemplo, la nube SenseCore para el ajuste fino), pero tienen un rendimiento inferior en pruebas de "vanguardia". Menos hype significa menos usuarios/datos para la iteración, creando un ciclo de retroalimentación. A partir de octubre de 2025, SenseTime posee ~14% de la cuota de mercado de AIGC (top 3), pero eso es en ingresos, no en capacidad.

### Noticias Recientes y Qué Ha Estado Haciendo SenseTime

Las noticias sobre SenseTime han sido más silenciosas que el frenesí de las startups (por ejemplo, el lanzamiento viral R1 de DeepSeek), pero están activos en el crecimiento empresarial/IA gen:

-   **Abril 2025**: Lanzaron SenseNova V6 Omni, el modelo multimodal "más avanzado" de China según sus afirmaciones, con actualizaciones a la infraestructura SenseCore 2.0 para una mejor comprensión del modelo.
-   **Junio 2025**: Se unieron a ByteDance/Alibaba en actualizaciones de modelos en medio de la carrera de IA, enfatizando APIs rentables.
-   **Agosto 2025**: La plataforma DayDayNew se integró con las gafas de IA de Xiaomi; los ingresos aumentaron un 21% interanual por la demanda de IA gen (servicios de entrenamiento/inferencia).
-   **Septiembre 2025**: Escindieron unidades no esenciales para agilizar el enfoque en IA gen, impulsando la rentabilidad.
-   **Octubre 2025**: DayDayNew 6.5 y la plataforma Mynie en la WAIC, impulsando la interacción multimodal (por ejemplo, la comprensión de video aumentó un 30%).

Están redoblando la apuesta por el B2B (por ejemplo, servicios en la nube, integración en dispositivos) en lugar de los chatbots de consumo, lo que explica la vibración de "sin noticias": menos demostraciones virales, más victorias empresariales silenciosas. Aún así, con las conversaciones sobre el alivio de sanciones y los avances en chips nacionales, podrían cerrar la brecha para 2026.

En resumen, el legado de SenseTime lo frena en una carrera de startups, pero su apuesta multimodal los posiciona para victorias prácticas por encima de la mera persecución de benchmarks.

[ChinAI #324: SuperCLUE Benchmarks —2025 Midyear Check-in](https://chinai.substack.com/p/chinai-324-superclue-large-model)  
[SenseTime's SenseNova Foundation Models Among Top Three](https://www.sensetime.com/en/news-detail/51169429?categoryId=1072)  
[An Overview of Chinese AI Tigers](https://www.topbots.com/chinese-ai-tigers-overview/)  
[China's SenseTime Reshapes to Focus on Generative AI Growth](https://www.reuters.com/technology/artificial-intelligence/chinas-sensetime-reshapes-focus-generative-ai-growth-2024-12-04/)  
[SenseTime Unveils DayDayNew 6.5 AI Model](https://forntend-test-5sqwmq-3a22a9-107-172-80-230.traefik.me/sensetime-unveils-daydaynew-6-5-ai-model-and-mynie-platform-1753705726167)