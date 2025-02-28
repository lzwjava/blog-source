---
audio: false
lang: es
layout: post
title: ¿Por qué es Kafka rápido?
translated: true
---

### Puntos Clave
- Parece probable que el video "System Design: Why is Kafka fast?" explique la velocidad de Apache Kafka a través de su arquitectura y elecciones de diseño.
- La investigación sugiere que el rendimiento de Kafka se ve impulsado por registros de solo-apendice, principios de cero-copia, procesamiento por lotes y particionamiento eficiente.
- La evidencia indica que la velocidad de Kafka se debe a su diseño de plataforma de transmisión de eventos distribuida, con componentes clave como productores, brokers y consumidores.

### Introducción
Este artículo de blog se basa en el contenido del video de YouTube "System Design: Why is Kafka fast?" de ByteByteGo, con el objetivo de transformar sus ideas en un formato escrito para una lectura y referencia más fáciles. Apache Kafka es conocido por su alto rendimiento en el procesamiento de datos en tiempo real, y este artículo explora las razones detrás de su velocidad, haciéndolo accesible para aquellos nuevos en el tema.

### Componentes Principales de Kafka
Apache Kafka opera como una plataforma de transmisión de eventos distribuida con tres componentes principales:
- **Productores**: Aplicaciones que envían datos a temas de Kafka.
- **Brokers**: Servidores que almacenan y gestionan los datos, asegurando la replicación y distribución.
- **Consumidores**: Aplicaciones que leen y procesan los datos de los temas.

Esta estructura permite a Kafka manejar grandes volúmenes de datos de manera eficiente, contribuyendo a su velocidad.

### Capas Arquitectónicas y Optimizaciones de Rendimiento
La arquitectura de Kafka se divide en dos capas:
- **Capa de Cómputo**: Incluye APIs para productores, consumidores y procesamiento de flujos, facilitando la interacción.
- **Capa de Almacenamiento**: Comprende brokers que gestionan el almacenamiento de datos en temas y particiones, optimizados para el rendimiento.

Las optimizaciones clave incluyen:
- **Registros de Solo-Apendice**: Escribir datos secuencialmente al final de un archivo, lo cual es más rápido que las escrituras aleatorias.
- **Principio de Cero-Copia**: Transferir datos directamente del productor al consumidor, reduciendo la sobrecarga de la CPU.
- **Procesamiento por Lotes**: Manejar datos en lotes para reducir la sobrecarga por registro.
- **Replicación Asíncrona**: Permitir que el broker líder sirva solicitudes mientras las réplicas se actualizan, asegurando la disponibilidad sin pérdida de rendimiento.
- **Particionamiento**: Distribuir datos en múltiples particiones para procesamiento paralelo y alto rendimiento.

Estas elecciones de diseño, detalladas en un artículo de blog de apoyo de ByteByteGo ([Why is Kafka so fast? How does it work?](https://bytebytego.substack.com/p/why-is-kafka-so-fast-how-does-it)), explican por qué Kafka sobresale en velocidad y escalabilidad.

### Flujo de Datos y Estructura de Registros
Cuando un productor envía un registro a un broker, se valida, se anexa a un registro de compromiso en disco y se replica para durabilidad, con el productor notificado tras el compromiso. Este proceso está optimizado para E/S secuencial, mejorando el rendimiento.

Cada registro incluye:
- Marca de tiempo: Cuando se creó el evento.
- Clave: Para particionamiento y ordenación.
- Valor: Los datos reales.
- Encabezados: Metadatos opcionales.

Esta estructura, como se describe en el artículo de blog, asegura un manejo eficiente de datos y contribuye a la velocidad de Kafka.

---

### Nota de Encuesta: Análisis Detallado del Rendimiento de Apache Kafka

Esta sección proporciona una exploración exhaustiva del rendimiento de Apache Kafka, ampliando el video "System Design: Why is Kafka fast?" de ByteByteGo, y utilizando recursos adicionales para asegurar una comprensión completa. El análisis está estructurado para cubrir la arquitectura, componentes y optimizaciones específicas de Kafka, con explicaciones detalladas y ejemplos para mayor claridad.

#### Contexto y Antecedentes
Apache Kafka, desarrollado como una plataforma de transmisión de eventos distribuida, es famoso por su capacidad para manejar transmisión de datos de alto rendimiento y baja latencia, convirtiéndolo en un pilar en las arquitecturas de datos modernas. El video, publicado el 29 de junio de 2022 y parte de una lista de reproducción sobre diseño de sistemas, tiene como objetivo elucidar por qué Kafka es rápido, un tema de gran interés dado el crecimiento exponencial en las necesidades de transmisión de datos. Este análisis está informado por un artículo de blog detallado de ByteByteGo ([Why is Kafka so fast? How does it work?](https://bytebytego.substack.com/p/why-is-kafka-so-fast-how-does-it)), que complementa el contenido del video y proporciona información adicional.

#### Componentes Principales y Arquitectura de Kafka
La velocidad de Kafka comienza con sus componentes principales:
- **Productores**: Estas son aplicaciones o sistemas que generan y envían eventos a temas de Kafka. Por ejemplo, una aplicación web podría producir eventos para interacciones de usuarios.
- **Brokers**: Estos son los servidores que forman un clúster, responsables de almacenar datos, gestionar particiones y manejar la replicación. Una configuración típica podría involucrar múltiples brokers para tolerancia a fallos y escalabilidad.
- **Consumidores**: Aplicaciones que se suscriben a temas para leer y procesar eventos, como motores de análisis procesando datos en tiempo real.

La arquitectura posiciona a Kafka como una plataforma de transmisión de eventos, utilizando "evento" en lugar de "mensaje", distinguiéndolo de las colas de mensajes tradicionales. Esto es evidente en su diseño, donde los eventos son inmutables y ordenados por desplazamientos dentro de particiones, como se detalla en el artículo de blog.

| Componente       | Rol                                                                 |
|------------------|----------------------------------------------------------------------|
| Productor        | Envía eventos a temas, iniciando el flujo de datos.                        |
| Broker           | Almacena y gestiona datos, maneja replicación y sirve a consumidores.   |
| Consumidor       | Lee y procesa eventos de temas, habilitando análisis en tiempo real. |

El artículo de blog incluye un diagrama en [esta URL](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd3690db-87b8-4165-8798-37d1d083f837_1600x1527.png), ilustrando esta arquitectura, que muestra la interacción entre productores, brokers y consumidores en modo clúster.

#### Arquitectura en Capas: Cómputo y Almacenamiento
La arquitectura de Kafka está bifurcada en:
- **Capa de Cómputo**: Facilita la comunicación a través de APIs:
  - **API de Productor**: Utilizada por aplicaciones para enviar eventos.
  - **API de Consumidor**: Habilita la lectura de eventos.
  - **API de Kafka Connect**: Se integra con sistemas externos como bases de datos.
  - **API de Kafka Streams**: Soporta procesamiento de flujos, como crear un KStream para un tema como "orders" con Serdes para serialización, y ksqlDB para trabajos de procesamiento de flujos con una API REST. Un ejemplo proporcionado es suscribirse a "orders", agrupar por productos y enviar a "ordersByProduct" para análisis.
- **Capa de Almacenamiento**: Comprende brokers de Kafka en clústeres, con datos organizados en temas y particiones. Los temas son similares a tablas de bases de datos, y las particiones se distribuyen en nodos, asegurando escalabilidad. Los eventos dentro de particiones están ordenados por desplazamientos, son inmutables y de solo-apendice, con eliminación tratada como un evento, mejorando el rendimiento de escritura.

El artículo de blog detalla esto, notando que los brokers gestionan particiones, lecturas, escrituras y replicaciones, con un diagrama en [esta URL](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb869cd88-3d6e-43af-8fd0-26f3737d8f1f_1600x559.png) ilustrando la replicación, como la Partición 0 en "orders" con tres réplicas: líder en Broker 1 (desplazamiento 4), seguidores en Broker 2 (desplazamiento 2) y Broker 3 (desplazamiento 3).

| Capa             | Descripción                                                                 |
|------------------|-----------------------------------------------------------------------------|
| Capa de Cómputo   | APIs para interacción: Productor, Consumidor, Connect, Streams y ksqlDB.     |
| Capa de Almacenamiento | Brokers en clústeres, temas/particiones distribuidos, eventos ordenados por desplazamientos. |

#### Planos de Control y Datos
- **Plano de Control**: Gestiona metadatos del clúster, históricamente utilizando Zookeeper, ahora reemplazado por el módulo KRaft con controladores en brokers seleccionados. Esta simplificación elimina Zookeeper, haciendo la configuración más fácil y la propagación de metadatos más eficiente a través de un tema especial, como se nota en el artículo de blog.
- **Plano de Datos**: Maneja la replicación de datos, con un proceso donde los seguidores emiten FetchRequest, el líder envía datos y confirma registros antes de un cierto desplazamiento, asegurando consistencia. El ejemplo de la Partición 0 con desplazamientos 2, 3 y 4 destaca esto, con un diagrama en [esta URL](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe17a4454-a194-45f9-8a1f-f4882501657c_1095x1600.png).

#### Estructura de Registros y Operaciones de Broker
Cada registro, la abstracción de un evento, incluye:
- Marca de tiempo: Cuando se creó.
- Clave: Para ordenación, colocalización y retención, crucial para particionamiento.
- Valor: El contenido de datos.
- Encabezados: Metadatos opcionales.

Clave y valor son matrices de bytes, codificadas/decodificadas con serdes, asegurando flexibilidad. Las operaciones de broker involucran:
- Solicitud del productor aterrizando en el búfer de recepción de socket.
- Hilo de red moviéndose a una cola de solicitudes compartida.
- Hilo de E/S validando CRC, anexando al registro de compromiso (segmentos de disco con datos e índice).
- Solicitudes almacenadas en purgatorio para replicación.
- Respuesta encolada, hilo de red enviando a través del búfer de envío de socket.

Este proceso, optimizado para E/S secuencial, se detalla en el artículo de blog, con diagramas ilustrando el flujo, contribuyendo significativamente a la velocidad de Kafka.

| Componente de Registro | Propósito                                                                 |
|------------------------|-------------------------------------------------------------------------|
| Marca de tiempo        | Registra cuándo se creó el evento.                                     |
| Clave                  | Asegura ordenación, colocalización y retención para particionamiento.           |
| Valor                  | Contiene el contenido de datos real.                                       |
| Encabezados            | Metadatos opcionales para información adicional.                           |

#### Optimizaciones de Rendimiento
Varias decisiones de diseño mejoran la velocidad de Kafka:
- **Registros de Solo-Apendice**: Escribir secuencialmente al final de un archivo minimiza el tiempo de búsqueda del disco, similar a agregar entradas a un diario al final, más rápido que insertar en medio del documento.
- **Principio de Cero-Copia**: Transfiere datos directamente del productor al consumidor, reduciendo la sobrecarga de la CPU, como mover una caja de un camión a un almacén sin desempacar, ahorrando tiempo.
- **Procesamiento por Lotes**: Manejar datos en lotes reduce la sobrecarga por registro, mejorando la eficiencia.
- **Replicación Asíncrona**: El broker líder sirve solicitudes mientras las réplicas se actualizan, asegurando disponibilidad sin impacto en el rendimiento.
- **Particionamiento**: Distribuye datos en particiones para procesamiento paralelo, aumentando el rendimiento, un factor clave en el manejo de grandes volúmenes de datos.

Estas optimizaciones, como se explora en el artículo de blog, son por qué Kafka logra alto rendimiento y baja latencia, haciéndolo adecuado para aplicaciones en tiempo real.

#### Conclusión e Insights Adicionales
La velocidad de Apache Kafka es el resultado de su arquitectura meticulosamente diseñada y optimizaciones de rendimiento, aprovechando registros de solo-apendice, principios de cero-copia, procesamiento por lotes, replicación asíncrona y particionamiento eficiente. Este análisis, basado en el video y complementado por el artículo de blog, proporciona una visión completa, inesperada en su profundidad para aquellos que esperan una visión general simple, revelando el equilibrio intrincado de elecciones de diseño que hacen de Kafka un líder en transmisión de datos.

El artículo de blog también ofrece una prueba gratuita de 7 días para archivos completos, accesible en [este enlace de suscripción](https://blog.bytebytego.com/subscribe?simple=true&next=https%3A%2F%2Fblog.bytebytego.com%2Fp%2Fwhy-is-kafka-so-fast-how-does-it&utm_source=paywall-free-trial&utm_medium=web&utm_content=137028631&coupon=3920da80), proporcionando recursos adicionales para aquellos interesados.

Esta exploración detallada asegura una comprensión completa, alineándose con la intención del video de educar sobre el rendimiento de Kafka, e informada por la investigación y los insights recopilados de diversas fuentes, asegurando precisión y profundidad.

#### Citaciones Clave
- [System Design: Why is Kafka fast? Video de YouTube](https://www.youtube.com/watch?v=UNUz1-msbOM)
- [Why is Kafka so fast? How does it work? Artículo de blog de ByteByteGo](https://bytebytego.substack.com/p/why-is-kafka-so-fast-how-does-it)
- [Diagrama de arquitectura de Kafka de ByteByteGo](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd3690db-87b8-4165-8798-37d1d083f837_1600x1527.png)
- [Diagrama de replicación de Kafka de ByteByteGo](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb869cd88-3d6e-43af-8fd0-26f3737d8f1f_1600x559.png)
- [Diagrama de operaciones de broker de Kafka de ByteByteGo](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe17a4454-a194-45f9-8a1f-f4882501657c_1095x1600.png)
- [Suscripción al boletín de ByteByteGo para el artículo de Kafka](https://blog.bytebytego.com/subscribe?simple=true&next=https%3A%2F%2Fblog.bytebytego.com%2Fp%2Fwhy-is-kafka-so-fast-how-does-it&utm_source=paywall-free-trial&utm_medium=web&utm_content=137028631&coupon=3920da80)