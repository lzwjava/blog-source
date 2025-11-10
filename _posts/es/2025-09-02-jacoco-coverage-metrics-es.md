---
audio: false
generated: true
image: false
lang: es
layout: post
title: Métricas de Cobertura de JaCoCo Explicadas
translated: true
type: note
---

Sí — **JaCoCo proporciona múltiples niveles de métricas de cobertura**, incluyendo las que mencionaste:

* **Cobertura de Archivo/Clase**
  Realiza un seguimiento de la cobertura a nivel de clase, mostrando cuánto de cada clase se ejecutó durante las pruebas.

* **Cobertura de Paquete**
  Agrega la cobertura de todas las clases en un paquete, permitiéndote ver la completitud de las pruebas para módulos de más alto nivel.

* **Cobertura de Método/Función**
  Mide si se han invocado métodos individuales (funciones) y si sus instrucciones/ramas fueron cubiertas.

* **Cobertura de Instrucción y Rama**
  Al nivel más granular, muestra qué instrucciones de bytecode y ramas condicionales fueron ejecutadas.

Cuando generas un reporte HTML de JaCoCo, normalmente verás una vista de árbol:

* Nodo superior = cobertura general del proyecto.
* Siguiente = cobertura por paquete.
* Luego = cobertura por clase.
* Dentro de cada clase = cobertura por método, con resaltado línea por línea.

👉 Entonces, respondiendo a tu pregunta: sí, JaCoCo soporta **cobertura de archivo (clase), paquete y función (método)** directamente.

¿Te gustaría que detalle **cómo calcula JaCoCo cada métrica** (por ejemplo, la diferencia entre cobertura de instrucción, rama, línea, método) para que tengas una imagen más clara de lo que realmente se mide?