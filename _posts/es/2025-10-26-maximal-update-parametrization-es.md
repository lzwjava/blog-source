---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Parametrización de Actualización Maximal para Redes Neuronales
translated: true
type: note
---

### ¿Qué es μP (Maximal Update Parametrization)?

μP, abreviatura de Maximal Update Parametrization, es una técnica de parametrización de redes neuronales desarrollada por Greg Yang, un matemático e investigador de IA que ahora está en xAI (anteriormente en Microsoft Research). Introducida en su artículo de 2022 "Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer", esta técnica reparametriza los pesos de los modelos de aprendizaje profundo para hacerlos más escalables y eficientes para el entrenamiento.

#### Propósito
El objetivo principal de μP es estabilizar la sintonización de hiperparámetros (HP) en diferentes tamaños de modelo. En las configuraciones tradicionales (como la parametrización estándar, o SP), los hiperparámetros como las tasas de aprendizaje necesitan ser reajustados cada vez que se escala un modelo—por ejemplo, de millones a miles de millones de parámetros—porque los gradientes y las actualizaciones se vuelven inestables (a menudo escalando cuadráticamente con el ancho o la profundidad del modelo). μP soluciona esto transformando los parámetros para que la "actualización máxima" (el paso de gradiente más grande posible) se mantenga consistente independientemente de la escala. Esto permite **μTransfer**, un flujo de trabajo donde se ajustan los HP en un pequeño modelo "proxy" y se aplican directamente a un modelo objetivo masivo sin necesidad de ajustes posteriores.

#### Beneficios Clave
- **Ahorro de Costos Dramático**: Ajustar en modelos pequeños es barato. Por ejemplo, transferir HP desde un proxy de 13M parámetros superó los resultados publicados de BERT-large (350M parámetros), con un costo total de ajuste equivalente a solo una ejecución de preentrenamiento de BERT-large. Para GPT-3 (6.7B parámetros), una transferencia desde un proxy de 40M superó a los baselines con solo el 7% del costo total de preentrenamiento.
- **Escalabilidad para Modelos Grandes**: Funciona bien en arquitecturas como Transformers y ResNets, haciéndolo ideal para entrenar redes neuronales enormes (por ejemplo, las usadas en xAI). Asegura "óptimos invariantes a la escala", lo que significa que el panorama de la función de pérdida no se deforma de manera impredecible a medida que los modelos crecen.
- **Facilidad de Uso**: Disponible como una librería para PyTorch (`pip install mup`), y ha sido integrada en pipelines de entrenamiento en producción para grandes modelos de IA.

#### Intuición Matemática Rápida
En SP, la varianza de los pesos crece de forma inestable, conduciendo a gradientes que explotan o desaparecen. μP reparametriza los pesos (por ejemplo, para una capa lineal, escalando por el fan-in) para normalizar la matriz de información de Fisher, asegurando que los flujos de gradiente se mantengan equilibrados. Esto mantiene los HP óptimos (como las tasas de aprendizaje) aproximadamente constantes a través de las escalas, evitando la necesidad de reajustes por cada tamaño.

μP se basa en el marco más amplio de "Tensor Programs" de Yang para entender los límites de ancho/profundidad infinitos en las redes neuronales, y todavía está evolucionando—trabajos recientes (a partir de 2025) enfatizan su papel en el aprendizaje máximo de características más allá de solo la transferencia de HP.

**Referencias**  
- [Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer](https://arxiv.org/abs/2203.03466)  
- [The Practitioner's Guide to the Maximal Update Parameterization](https://www.cerebras.ai/blog/the-practitioners-guide-to-the-maximal-update-parameterization)  
- [How To Scale (Blog on μP and Scaling)](https://howtoscalenn.github.io/)  
- [Greg Yang's Professional Page](https://thegregyang.com/)