---
audio: false
generated: true
lang: es
layout: post
title: Máquina Virtual Más Barata de Google Cloud
translated: true
type: note
---

Al buscar una máquina virtual (VM) económica en Google Cloud, hay algunas opciones y consideraciones a tener en cuenta para ajustarse a un presupuesto de alrededor de $5 por mes. Aquí hay algunos pasos y consejos para ayudarte a encontrar la opción de VM más barata:

1.  **VM de núcleo compartido**: Google Cloud ofrece VM de núcleo compartido, que son las opciones más económicas. Estas VM comparten potencia de CPU con otros clientes, lo que puede resultar en un rendimiento menos robusto pero son significativamente más baratas. Podría ser un buen punto de partida para un servidor simple con requisitos de recursos bajos.

2.  **VM preemptibles**: Considera usar VM preemptibles, que ofrecen descuentos sustanciales en comparación con las VM regulares. Google Cloud puede terminar estas VM si sus recursos se necesitan en otro lugar, por lo que son más adecuadas para cargas de trabajo tolerantes a fallos. Las VM preemptibles pueden ofrecer descuentos de hasta un 80% sobre los precios regulares.

3.  **VM Tau**: Las VM Tau de Google Cloud están diseñadas para cargas de trabajo de escalado horizontal y ofrecen hasta un 42% más de rendimiento por precio en comparación con las VM de propósito general. Estas podrían ser más rentables para ciertos tipos de cargas de trabajo.

4.  **Tipos de máquina personalizados**: Puedes crear tipos de máquina personalizados adaptados a tus necesidades específicas, lo que puede ayudar a reducir costos al pagar solo por los recursos que necesitas. Esta flexibilidad te permite ajustar finamente la CPU y la memoria para que coincidan con los requisitos de tu carga de trabajo.

5.  **Descuentos por uso sostenido**: Google Cloud aplica automáticamente descuentos por uso sostenido para las VM que se ejecutan durante una parte significativa del mes de facturación. El descuento aumenta con el uso y puede llegar hasta un 30% de descuento sobre el precio regular.

6.  **Nivel gratuito**: Google Cloud ofrece un nivel gratuito que incluye una pequeña cantidad de recursos de computación cada mes. Esto podría ser suficiente para aplicaciones muy ligeras y puede ayudar a reducir costos aún más.

7.  **Calculadora de costos**: Utiliza la Calculadora de Precios de Google Cloud para estimar los costos de diferentes configuraciones y encontrar la configuración más rentable para tus necesidades.

8.  **VM Spot**: Las VM Spot ofrecen precios dinámicos con descuentos del 60-91% sobre el precio bajo demanda para la mayoría de los tipos de máquina. Estas pueden ser una opción muy rentable si tu carga de trabajo puede tolerar interrupciones.

Para un servidor simple con requisitos de recursos bajos, comenzar con una VM de núcleo compartido o preemptible podría ser el mejor enfoque. Luego puedes monitorear el rendimiento y ajustar la configuración según sea necesario para equilibrar el costo y el rendimiento.