---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Autores y Contribuciones del Transformer de Visión
translated: true
type: note
---

### Introducción a los autores de "Una imagen vale 16x16 palabras: Transformers para el reconocimiento de imágenes a escala"

El innovador artículo "Una imagen vale 16x16 palabras: Transformers para el reconocimiento de imágenes a escala", presentado en 2020 por Alexey Dosovitskiy y sus colegas de Google, marcó un cambio pivotal en la visión por computadora. Propuso el Vision Transformer (ViT), un modelo que aplica arquitecturas transformer—originalmente diseñadas para el procesamiento del lenguaje natural—directamente a parches de imagen, logrando un rendimiento de vanguardia en conjuntos de datos a gran escala como ImageNet cuando se pre-entrena con datos masivos (por ejemplo, JFT-300M). Este trabajo demostró que los transformers puros podían superar a las redes neuronales convolucionales (CNN) en eficiencia y precisión con suficiente capacidad de cálculo y datos, influyendo en avances posteriores en IA multimodal y modelos de visión escalables.

El artículo fue un esfuerzo colaborativo de 12 investigadores, principalmente del equipo de Zúrich de Google Brain, que combinó experiencia en aprendizaje profundo, modelado de secuencias y entrenamiento a gran escala. A continuación, se presenta una descripción general de los autores clave, destacando sus antecedentes y contribuciones al campo. (En aras de la brevedad, me he centrado en los contribuyentes más prominentes; la lista completa incluye a Dirk Weissenborn, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly y Jakob Uszkoreit—todos exalumnos de Google con profundas raíces en transformers, optimización e integración visión-lenguaje).

#### Autores clave y sus antecedentes

- **Alexey Dosovitskiy** (Autor Principal): Como la fuerza impulsora detrás de ViT, Dosovitskiy conceptualizó la idea central de tratar las imágenes como secuencias de parches. Posee una Maestría y un Doctorado en matemáticas de la Universidad Estatal Lomonósov de Moscú, seguidos de un trabajo postdoctoral en la Universidad de Friburgo sobre aprendizaje de características no supervisado. Al unirse a Google Brain en 2019, lideró el desarrollo de ViT antes de mudarse a Inceptive (una empresa de IA con sede en Berlín) en 2021. Su trabajo abarca la visión por computadora, modelos generativos y ML inspirado en la biología, con más de 136,000 citas.

- **Lucas Beyer**: Beyer desempeñó un papel crucial en la implementación práctica de ViT, la evaluación en benchmarks y las optimizaciones de eficiencia. De origen belga, estudió ingeniería mecánica en la Universidad RWTH de Aquisgrán, obteniendo un doctorado en robótica e IA en 2018 con un enfoque en IA para juegos y aprendizaje por refuerzo. Se unió a Google Brain en Zúrich después de su doctorado, ascendiendo a científico investigador senior en Google DeepMind. En 2025, se convirtió en una de las principales contrataciones de IA de Meta, continuando el trabajo en vision transformers y ML centrado en datos.

- **Alexander Kolesnikov**: Kolesnikov contribuyó a los experimentos de escalado de ViT y a las ideas de transfer learning, enfatizando su rendimiento en conjuntos de datos de tamaño medio. Obtuvo una maestría en matemáticas de la Universidad Estatal de Moscú y un doctorado en aprendizaje automático/visión por computadora del Institute of Science and Technology Austria (ISTA) en 2018. Comenzando en Google Brain en 2018, avanzó a roles senior en DeepMind antes de unirse a OpenAI y, en 2025, a Meta—donde fue reclutado por su experiencia en modelos de visión eficientes.

- **Xiaohua Zhai**: Zhai se centró en las estrategias de pre-entrenamiento de ViT y sus extensiones multimodales, basándose en su trabajo en aprendizaje de representaciones. Posee un doctorado en ingeniería electrónica de la Universidad de Pekín y se unió a Google como ingeniero de software en 2015, pasando a la investigación en Google Brain en 2017 y en DeepMind en 2023. Ahora investigador en Meta (a través de OpenAI Zúrich en 2025), sus contribuciones unen la visión, el lenguaje y el aprendizaje auto-supervisado, con más de 100,000 citas.

- **Neil Houlsby** (Autor Senior): Como líder de equipo, Houlsby supervisó el diseño arquitectónico de ViT y las implicaciones más amplias para las leyes de escalado en visión. Recibió una Beca Doctoral Europea de Google alrededor de 2010 y completó su doctorado en aprendizaje automático. Investigador de Google desde hace mucho tiempo, desde sus días de pasante, gestionó equipos en Google Brain y DeepMind sobre arquitecturas neuronales y modelos visión-lenguaje. En 2025, se unió a Anthropic para dirigir su nueva oficina en Zúrich, centrándose en el escalado seguro de la IA.

Esta colaboración de Google Brain (mayoritariamente con sede en Zúrich) aprovechó la proximidad del equipo a los TPU para realizar experimentos masivos—más de 25,000 días-TPU—demostrando la viabilidad de los transformers más allá del texto. Muchos autores se han trasladado desde entonces a laboratorios líderes de IA como Meta, OpenAI y Anthropic, lo que refleja el impacto duradero de ViT en el campo.

#### Referencias

- [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (arXiv)](https://arxiv.org/abs/2010.11929)
- [Alexey Dosovitskiy Google Scholar Profile](https://scholar.google.com/citations?user=FXNJRDoAAAAJ)
- [Lucas Beyer Google Scholar Profile](https://scholar.google.com/citations?user=p2gwhK4AAAAJ)
- [Alexander Kolesnikov Google Scholar Profile](https://scholar.google.com/citations?user=H9I0CVwAAAAJ)
- [Xiaohua Zhai Google Scholar Profile](https://scholar.google.com/citations?user=8gruapYAAAAJ)
- [Neil Houlsby Google Scholar Profile](https://scholar.google.com/citations?user=sm1-TZMAAAAJ)
- [From Ph.D. Detour to Meta's Top AI Hire: Lucas Beyer (Times of India)](https://timesofindia.indiatimes.com/education/news/lucas-beyer-educational-qualification-from-ph-d-detour-and-google-rejection-to-becoming-metas-top-ai-hire/articleshow/122158414.cms)
- [Zuckerberg Poaches Alexander Kolesnikov from OpenAI (Times of India)](https://timesofindia.indiatimes.com/education/news/zuckerberg-poached-alexander-kolesnikov-from-sam-altmans-openai-where-did-this-ai-genius-study/articleshow/122158654.cms)
- [Anthropic Poaches Neil Houlsby from Google DeepMind (Euronews)](https://www.euronews.com/next/2025/02/13/anthropic-poaches-google-deepmind-talent-to-lead-new-european-office)