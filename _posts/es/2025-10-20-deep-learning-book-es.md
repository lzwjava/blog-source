---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Libro de Aprendizaje Profundo de Goodfellow Bengio Courville
translated: true
type: note
---

**Ian Goodfellow**  
**Yoshua Bengio**  
**Aaron Courville**

## Contenidos

- Sitio web viii  
- Agradecimientos ix  
- Notación xiii  

### 1 Introducción 1

- 1.1 ¿Quién debería leer este libro? 8  
- 1.2 Tendencias históricas en Deep Learning 12  

## I Fundamentos de Matemáticas Aplicadas y Machine Learning 27

### 2 Álgebra Lineal 29

- 2.1 Escalares, Vectores, Matrices y Tensores 29  
- 2.2 Multiplicación de Matrices y Vectores 32  
- 2.3 Matrices Identidad e Inversa 34  
- 2.4 Dependencia Lineal y Rango 35  
- 2.5 Normas 37  
- 2.6 Tipos Especiales de Matrices y Vectores 38  
- 2.7 Descomposición en Autovalores 40  
- 2.8 Descomposición en Valores Singulares 42  
- 2.9 La Pseudoinversa de Moore-Penrose 43  
- 2.10 El Operador Traza 44  
- 2.11 El Determinante 45  
- 2.12 Ejemplo: Análisis de Componentes Principales 45  

### 3 Probabilidad y Teoría de la Información 51

- 3.1 ¿Por qué Probabilidad? 52  
- 3.2 Variables Aleatorias 54  
- 3.3 Distribuciones de Probabilidad 54  
- 3.4 Probabilidad Marginal 56  
- 3.5 Probabilidad Condicional 57  
- 3.6 Regla de la Cadena de Probabilidades Condicionales 57  
- 3.7 Independencia e Independencia Condicional 58  
- 3.8 Esperanza, Varianza y Covarianza 58  
- 3.9 Distribuciones de Probabilidad Comunes 60  
- 3.10 Propiedades Útiles de Funciones Comunes 65  
- 3.11 Regla de Bayes 68  
- 3.12 Detalles Técnicos de Variables Continuas 69  
- 3.13 Teoría de la Información 71  
- 3.14 Modelos Probabilísticos Estructurados 73  

### 4 Cálculo Numérico 78

- 4.1 Desbordamiento y Subdesbordamiento 78  
- 4.2 Mal Acondicionamiento 80  
- 4.3 Optimización Basada en Gradientes 80  
- 4.4 Optimización con Restricciones 91  
- 4.5 Ejemplo: Mínimos Cuadrados Lineales 94  

### 5 Fundamentos de Machine Learning 96

- 5.1 Algoritmos de Aprendizaje 97  
- 5.2 Capacidad, Sobreajuste y Subajuste 108  
- 5.3 Hiperparámetros y Conjuntos de Validación 118  
- 5.4 Estimadores, Sesgo y Varianza 120  
- 5.5 Estimación de Máxima Verosimilitud 129  
- 5.6 Estadística Bayesiana 133  
- 5.7 Algoritmos de Aprendizaje Supervisado 137  
- 5.8 Algoritmos de Aprendizaje No Supervisado 142  
- 5.9 Descenso de Gradiente Estocástico 149  
- 5.10 Construyendo un Algoritmo de Machine Learning 151  
- 5.11 Desafíos que Motivan el Deep Learning 152  

## II Redes Profundas: Prácticas Modernas 162

### 6 Redes Profundas de Propagación hacia Adelante 164

- 6.1 Ejemplo: Aprendiendo XOR 167  
- 6.2 Aprendizaje Basado en Gradientes 172  
- 6.3 Unidades Ocultas 187  
- 6.4 Diseño de Arquitectura 193  
- 6.5 Retropropagación y Otros Algoritmos de Diferenciación 200  
- 6.6 Notas Históricas 220  

### 7 Regularización para Deep Learning 224

- 7.1 Penalizaciones de Norma de Parámetros 226  
- 7.2 Penalizaciones de Norma como Optimización con Restricciones 233  
- 7.3 Regularización y Problemas Subdeterminados 235  
- 7.4 Aumento de Datos 236  
- 7.5 Robustez al Ruido 238  
- 7.6 Aprendizaje Semi-Supervisado 240  
- 7.7 Aprendizaje Multitarea 241  
- 7.8 Parada Temprana 241  
- 7.9 Vinculación y Compartición de Parámetros 249  
- 7.10 Representaciones Dispersas 251  
- 7.11 Bagging y Otros Métodos de Ensemble 253  
- 7.12 Dropout 255  
- 7.13 Entrenamiento Adversarial 265  
- 7.14 Distancia Tangente, Tangent Prop y el Clasificador de la Tangente de la Variedad 267  

### 8 Optimización para el Entrenamiento de Modelos Profundos 271

- 8.1 Cómo el Aprendizaje Difiere de la Optimización Pura 272  
- 8.2 Desafíos en la Optimización de Redes Neuronales 279  
- 8.3 Algoritmos Básicos 290  
- 8.4 Estrategias de Inicialización de Parámetros 296  
- 8.5 Algoritmos con Tasas de Aprendizaje Adaptativas 302  
- 8.6 Métodos de Segundo Orden Aproximados 307  
- 8.7 Estrategias de Optimización y Meta-Algoritmos 313  

### 9 Redes Convolucionales 326

- 9.1 La Operación de Convolución 327  
- 9.2 Motivación 329  
- 9.3 Agrupamiento 335  
- 9.4 Convolución y Agrupamiento como un Prior Infinitamente Fuerte 339  
- 9.5 Variantes de la Función de Convolución Básica 342  
- 9.6 Salidas Estructuradas 352  
- 9.7 Tipos de Datos 354  
- 9.8 Algoritmos de Convolución Eficientes 356  
- 9.9 Características Aleatorias o No Supervisadas 356  
- 9.10 Base Neurocientífica para las Redes Convolucionales 358  
- 9.11 Redes Convolucionales y la Historia del Deep Learning 365  

### 10 Modelado de Secuencias: Redes Recurrentes y Recursivas 367

- 10.1 Desplegando Grafos Computacionales 369  
- 10.2 Redes Neuronales Recurrentes 372  
- 10.3 RNNs Bidireccionales 388  
- 10.4 Arquitecturas Codificador-Decodificador Secuencia a Secuencia 390  
- 10.5 Redes Recurrentes Profundas 392  
- 10.6 Redes Neuronales Recursivas 394  
- 10.7 El Desafío de las Dependencias a Largo Plazo 396  
- 10.8 Redes de Eco 399  
- 10.9 Unidades con Fugas y Otras Estrategias para Múltiples Escalas de Tiempo 402  
- 10.10 La Memoria a Largo-Corto Plazo y Otras RNNs con Compuertas 404  
- 10.11 Optimización para Dependencias a Largo Plazo 408  
- 10.12 Memoria Explícita 412  

### 11 Metodología Práctica 416

- 11.1 Métricas de Rendimiento  
- 11.2 Modelos Base por Defecto  
- 11.3 Determinando si Recolectar Más Datos  
- 11.4 Seleccionando Hiperparámetros  
- 11.5 Estrategias de Depuración  
- 11.6 Ejemplo: Reconocimiento de Números de Múltiples Dígitos  

## III Investigación en Deep Learning 482

### 12 Modelos Lineales de Factores 485

- 12.1 PCA Probabilístico y Análisis Factorial  
- 12.2 Análisis de Componentes Independientes (ICA)  
- 12.3 Análisis de Características Lentas  
- 12.4 Codificación Dispersa  
- 12.5 Interpretación de Variedades del PCA  

### 13 Autoencoders 500

- 13.1 Autoencoders Subcompletos  
- 13.2 Autoencoders Regularizados  
- 13.3 Poder de Representación, Tamaño de Capa y Profundidad  
- 13.4 Codificadores y Decodificadores Estocásticos  
- 13.5 Autoencoders de Ruido  
- 13.6 Aprendiendo Variedades con Autoencoders  
- 13.7 Autoencoders Contráctiles  
- 13.8 Descomposición Dispersa Predictiva  
- 13.9 Aplicaciones de los Autoencoders  

### 14 Aprendizaje de Representaciones 525

- 14.1 Pretrenamiento No Supervisado Codicioso por Capas  
- 14.2 Transferencia de Aprendizaje y Adaptación de Dominio  
- 14.3 Disentanglement Semi-Supervisado de Factores Causales  
- 14.4 Representación Distribuida  
- 14.5 Ganancias Exponenciales de la Profundidad  
- 14.6 Proporcionando Pistas para Descubrir Causas Subyacentes  

### 15 Modelos Probabilísticos Estructurados para Deep Learning 540

- 15.1 El Desafío del Modelado No Estructurado  
- 15.2 Usando Grafos para Describir la Estructura del Modelo  
- 15.3 Muestreo de Modelos Gráficos  
- 15.4 Ventajas del Modelado Estructurado  
- 15.5 Aprendiendo sobre Dependencias  
- 15.6 Inferencia e Inferencia Aproximada  
- 15.7 El Enfoque del Deep Learning a los Modelos Probabilísticos Estructurados  

### 16 Métodos de Monte Carlo 557

- 16.1 Muestreo y Métodos de Monte Carlo  
- 16.2 Muestreo por Importancia  
- 16.3 Métodos de Monte Carlo basados en Cadenas de Markov  
- 16.4 Muestreo de Gibbs  
- 16.5 El Desafío de la Mezcla entre Modos Separados  

### 17 Enfrentando la Función de Partición 567

- 17.1 El Gradiente de la Log-Verisimilitud  
- 17.2 Máxima Verosimilitud Estocástica y Divergencia Contrastiva  
- 17.3 Pseudoverosimilitud  
- 17.4 Score Matching y Ratio Matching  
- 17.5 Denoising Score Matching  
- 17.6 Estimación por Contraste de Ruido  
- 17.7 Estimando la Función de Partición  

### 18 Inferencia Aproximada 579

- 18.1 Inferencia como Optimización  
- 18.2 Expectation Maximization  
- 18.3 Inferencia MAP y Codificación Dispersa  
- 18.4 Inferencia y Aprendizaje Variacional  
- 18.5 Inferencia Aproximada Aprendida  

### 19 Modelos Generativos Profundos 594

- 19.1 Máquinas de Boltzmann  
- 19.2 Máquinas de Boltzmann Restringidas  
- 19.3 Redes de Creencia Profundas  
- 19.4 Máquinas de Boltzmann Profundas  
- 19.5 Máquinas de Boltzmann para Datos de Valor Real  
- 19.6 Máquinas de Boltzmann Convolucionales  
- 19.7 Máquinas de Boltzmann para Salidas Estructuradas o Secuenciales  
- 19.8 Otras Máquinas de Boltzmann  
- 19.9 Retropropagación a través de Operaciones Aleatorias  
- 19.10 Redes Generativas Dirigidas  
- 19.11 Extrayendo Muestras de Autoencoders  
- 19.12 Redes Estocásticas Generativas  
- 19.13 Otros Esquemas de Generación  
- 19.14 Evaluando Modelos Generativos  
- 19.15 Conclusión  

[Índice de Contenidos de Deep Learning](https://www.deeplearningbook.org/contents/toc.html)