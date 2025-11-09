---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Codificadores Rotativos Miden Rotación
translated: true
type: note
---

### ¿Qué es un Codificador Rotatorio?

Un **codificador rotatorio** es un tipo de sensor electromecánico utilizado para detectar y medir la posición angular o la rotación de un eje (como en perillas, diales o ruedas) en dispositivos mecánicos. Convierte el movimiento rotacional en señales digitales o analógicas, permitiendo a los dispositivos rastrear cuánto y en qué dirección algo ha girado. Son comunes en todo, desde las perillas de volumen en equipos de audio hasta los volantes en robótica y maquinaria industrial.

#### Tipos Clave
Existen dos tipos principales, según cómo manejan el seguimiento de la posición:

| Tipo              | Descripción | Mejor Para |
|-------------------|-------------|----------|
| **Incremental**  | Genera pulsos (o "ticks") por cada pequeño cambio en la rotación, contando pasos relativos a un punto de inicio. La posición se calcula rastreando estos cambios en el tiempo. | Movimiento gradual y continuo, como ruedas de desplazamiento o retroalimentación de motores, donde la posición absoluta no es crítica. |
| **Absoluto**     | Proporciona un código digital único para cada posible posición angular, por lo que conoce la ubicación exacta incluso después de una pérdida de energía. | Aplicaciones de precisión como ascensores o máquinas CNC, donde es esencial conocer la posición "inicial" sin necesidad de reiniciar. |

#### Cómo Funciona (Simplificado)
- **Óptico**: Una fuente de luz brilla a través de un disco con patrones (con ranuras o marcas) unido al eje giratorio. Un sensor detecta las interrupciones en la luz para generar señales.
- **Magnético**: Utiliza imanes y sensores de efecto Hall para detectar cambios en los campos magnéticos a medida que gira el eje.
- **Mecánico**: Estilo más antiguo con contactos directos, pero menos confiable debido al desgaste.

Los "cambios de posición graduales" que mencionaste se alinean perfectamente con los codificadores rotatorios incrementales, ya que son excelentes para detectar rotaciones suaves e incrementales sin necesidad de reiniciar.

Si esto no es exactamente lo que querías decir con "¿qué es?" (por ejemplo, si estás pensando en un dispositivo específico o una comparación), ¡no dudes en aclararlo!