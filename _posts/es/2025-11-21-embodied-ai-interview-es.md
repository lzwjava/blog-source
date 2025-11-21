---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4.1-fast
title: Preguntas para Entrevistas de Ingeniero de IA Encarnada
translated: true
type: note
---

Aquí tienes un conjunto exhaustivo de preguntas de entrevista adaptadas para un rol de **Ingeniero de IA Encarnada**, con un fuerte enfoque en el aprendizaje de políticas visuomotoras modernas, especialmente **Diffusion Policy**, **RT-2**, **ACT (Action Chunking Transformer)**, y tecnologías generales de inteligencia encarnada.

### Fundamentos Generales de IA Encarnada y Robótica
1. ¿Cuáles son las diferencias clave entre la IA encarnada y los modelos grandes tradicionales de lenguaje/visión "desencarnados"?
2. ¿Por qué la transferencia de simulación a realidad es significativamente más difícil en la IA encarnada en comparación con las tareas de visión por computadora o PLN?
3. Compara los requisitos de datos y las leyes de escalamiento que has observado en la IA encarnada versus en los LLM o modelos fundacionales de visión.
4. ¿Cómo piensas en la seguridad y la robustez en el despliegue robótico del mundo real (por ejemplo, modos de fallo, comportamientos de recuperación)?

### Diffusion Policy (UC Berkeley, Chi et al., 2023–2025)
5. Explica la idea central de Diffusion Policy y por qué los modelos de difusión son particularmente adecuados para el control visuomotor.
6. Describe el proceso directo/inverso cuando se utiliza un modelo de difusión como política. ¿Cómo se condiciona la eliminación de ruido de las acciones sobre las observaciones visuales?
7. ¿Cuáles son las principales ventajas de Diffusion Policy sobre los métodos anteriores de aprendizaje por imitación (por ejemplo, clonación conductual con MSE, GCBC, Transformer BC)?
8. Diffusion Policy a menudo utiliza una columna vertebral U-Net con condicionamiento FiLM o atención cruzada. Compara estos dos métodos de condicionamiento visual en términos de rendimiento y velocidad de inferencia.
9. ¿Cómo funciona la guía libre de clasificador en Diffusion Policy y cómo afecta a la exploración versus la explotación en el momento de la prueba?
10. En las versiones de 2024–2025, Diffusion Policy se ha combinado con condicionamiento de grafos de escena o lenguaje. ¿Cómo añadirías objetivos de lenguaje de alto nivel a una política de difusión?
11. ¿Cuáles son los modos de fallo comunes que has visto con Diffusion Policy en despliegues con robots reales y cómo se mitigaron?

### RT-2 (Google DeepMind, 2023–2024)
12. ¿Qué es RT-2 y cómo ajusta conjuntamente un modelo de lenguaje y visión (PaLI-X / PaLM-E) para convertirlo en acciones robóticas?
13. Explica el esquema de tokenización utilizado en RT-2 para acciones continuas. ¿Por qué discretizar las acciones en contenedores (bins)?
14. RT-2 afirma capacidades emergentes (por ejemplo, razonamiento de cadena de pensamiento, aritmética, comprensión de símbolos) transferidas a la robótica. ¿Has reproducido u observado esto en la práctica?
15. Compara RT-2 con OpenVLA y Octo. ¿En qué escenarios preferirías RT-2 sobre los otros?
16. ¿Cómo maneja RT-2 las tareas de horizonte largo y la generalización multitarea en comparación con Diffusion Policy o ACT?

### ACT (Action Chunking Transformer, Tony Zhao et al., 2023)
17. ¿Qué problema resuelve la fragmentación de acciones (action chunking) en las políticas basadas en transformers y por qué es crítica para el control en tiempo real a 10–50 Hz?
18. Describe la arquitectura de ACT: ¿cómo se fragmentan las acciones, cómo se calcula el objetivo latente y cómo se modela la varianza?
19. Compara ACT con Diffusion Policy en términos de eficiencia muestral, velocidad de inferencia y tasa de éxito en tareas con mucho contacto.
20. ACT originalmente usaba CVAE para el modelado latente; las versiones posteriores usan flow-matching o difusión. ¿Qué beneficios aportaron las versiones más nuevas?

### Panorama General de las Políticas Visuomotoras
21. Compara las cuatro familias principales de políticas visuomotoras en 2024–2025:
   - Modelos de secuencia Transformer (ACT, Octo)
   - Familia Diffusion Policy
   - Modelos estilo VLA (RT-2, OpenVLA, Octo-Transformer)
   - Políticas de flow-matching (por ejemplo, MIMo, Aurora)
22. ¿Cuándo elegirías flow-matching sobre difusión para un robot en tiempo real (por ejemplo, un humanoide o un manipulador móvil)?
23. ¿Cómo combinan modelos recientes como Octo (UC Berkeley, 2024) y OpenVLA (Stanford/PMI, 2024) las fortalezas de ACT y RT-2?
24. ¿Qué papel ves que tienen los modelos fundacionales (por ejemplo, incrustar acciones en el mismo espacio que los tokens de lenguaje/imagen) en los próximos 2-3 años de la IA encarnada?

### Preguntas de Diseño de Sistemas e Ingeniería
25. Diseña una pipeline de entrenamiento completa para recopilar un conjunto de datos del mundo real de más de 100k episodios para un manipulador móvil bimanual utilizando Diffusion Policy o ACT.
26. ¿Cómo harías que una política visuomotora se ejecute en tiempo real (≥30 Hz) en una GPU periférica (por ejemplo, Jetson Orin) manteniendo una alta tasa de éxito?
27. Tienes una política que funciona perfectamente en simulación pero falla completamente en el robot real. ¿Lista de verificación sistemática para depuración?
28. ¿Cómo añadirías la sensación de fuerza/táctil como modalidades adicionales a un modelo Diffusion Policy o RT-2 existente que solo usa visión?
29. Explica cómo harías una adaptación rápida (few-shot o zero-shot) a una nueva instancia de objeto o a un nuevo fondo usando cualquiera de estos métodos.

### Investigación y Direcciones Futuras
30. ¿Dónde crees que estará el campo de la IA encarnada en 2027? ¿Tendremos robots domésticos generalistas? ¿Cuál es el mayor obstáculo hoy en día?
31. ¿Crees que el paradigma actual de aprendizaje por imitación + pre-entrenamiento a escala de internet (OpenVLA, Octo, etc.) es suficiente para una verdadera generalización, o todavía necesitamos aprendizaje por refuerzo o recolección activa de datos?

Estas preguntas van desde conocimientos fundamentales hasta detalles de investigación de vanguardia y desafíos de ingeniería práctica, perfectos para entrevistas de ingeniero o investigador de IA encarnada de nivel medio a senior en 2025. ¡Buena suerte con tus entrevistas!