---
audio: false
generated: true
lang: es
layout: post
title: ¿Por qué Kafka es rápido?
translated: true
type: note
---

### Puntos Clave
- Es probable que el video "System Design: Why is Kafka fast?" explique la velocidad de Apache Kafka a través de su arquitectura y decisiones de diseño.
- La investigación sugiere que el rendimiento de Kafka se ve impulsado por los registros de solo adición (append-only logs), los principios de cero copia (zero-copy), el procesamiento por lotes y la partición eficiente.
- La evidencia se inclina a que la velocidad de Kafka se debe al diseño de su plataforma distribuida de streaming de eventos, con componentes clave como productores, brokers y consumidores.

### Introducción
Esta entrada de blog se basa en el contenido del video de YouTube "System Design: Why is Kafka fast?" de ByteByteGo, con el objetivo de transformar sus ideas a un formato escrito para facilitar su lectura y consulta. Apache Kafka es conocido por su alto rendimiento en el procesamiento de datos en tiempo real, y esta publicación explora las razones detrás de su velocidad, haciéndolo accesible para quienes son nuevos en el tema.

### Componentes Principales de Kafka
Apache Kafka opera como una plataforma distribuida de streaming de eventos con tres componentes principales:
- **Productores (Producers)**: Aplicaciones que envían datos a los temas (topics) de Kafka.
- **Brokers**: Servidores que almacenan y gestionan los datos, asegurando la replicación y distribución.
- **Consumidores (Consumers)**: Aplicaciones que leen y procesan los datos de los temas.

Esta estructura permite a Kafka manejar grandes volúmenes de datos de manera eficiente, contribuyendo a su velocidad.

### Capas Arquitectónicas y Optimizaciones de Rendimiento
La arquitectura de Kafka se divide en dos capas:
- **Capa de Cómputo (Compute Layer)**: Incluye APIs para productores, consumidores y procesamiento de flujos (stream processing), facilitando la interacción.
- **Capa de Almacenamiento (Storage Layer)**: Comprende brokers que gestionan el almacenamiento de datos en temas y particiones, optimizado para el rendimiento.

Las optimizaciones clave incluyen:
- **Registros de Solo Adición (Append-Only Logs)**: Escribir datos secuencialmente al final de un archivo, lo cual es más rápido que las escrituras aleatorias.
- **Principio de Cero Copia (Zero-Copy Principle)**: Transferir datos directamente del productor al consumidor, reduciendo la carga de la CPU.
- **Procesamiento por Lotes (Batch Processing)**: Manejar datos en lotes para reducir la sobrecarga por registro.
- **Replicación Asíncrona (Asynchronous Replication)**: Permitir que el broker líder atienda solicitudes mientras las réplicas se actualizan, asegurando disponibilidad sin pérdida de rendimiento.
- **Particionado (Partitioning)**: Distribuir datos a través de múltiples particiones para el procesamiento paralelo y alto rendimiento.

Estas decisiones de diseño, detalladas en una entrada de blog de apoyo de ByteByteGo ([Why is Kafka so fast? How does it work?](https://bytebytego.substack.com/p/why-is-kafka-so-fast-how-does-it)), explican por qué Kafka sobresale en velocidad y escalabilidad.

### Flujo de Datos y Estructura del Registro
Cuando un productor envía un registro a un broker, este se valida, se añade a un registro de confirmaciones (commit log) en el disco y se replica para durabilidad, notificándose al productor una vez confirmado. Este proceso está optimizado para E/S secuencial, mejorando el rendimiento.

Cada registro incluye:
- Marca de tiempo (Timestamp): Cuándo se creó el evento.
- Clave (Key): Para el particionado y ordenación.
- Valor (Value): Los datos reales.
- Cabeceras (Headers): Metadatos opcionales.

Esta estructura, como se describe en la entrada de blog, asegura un manejo eficiente de los datos y contribuye a la velocidad de Kafka.

---

### Nota de Estudio: Análisis Detallado del Rendimiento de Apache Kafka

Esta sección proporciona una exploración exhaustiva del rendimiento de Apache Kafka, ampliando el video "System Design: Why is Kafka fast?" de ByteByteGo y extrayendo de recursos adicionales para asegurar una comprensión completa. El análisis está estructurado para cubrir la arquitectura, los componentes y las optimizaciones específicas de Kafka, con explicaciones detalladas y ejemplos para mayor claridad.

#### Antecedentes y Contexto
Apache Kafka, desarrollado como una plataforma distribuida de streaming de eventos, es reconocido por su capacidad para manejar streaming de datos de alto rendimiento y baja latencia, convirtiéndolo en un elemento básico en las arquitecturas de datos modernas. El video, publicado el 29 de junio de 2022 y parte de una lista de reproducción sobre diseño de sistemas, pretende dilucidar por qué Kafka es rápido, un tema de interés significativo dado el crecimiento exponencial de las necesidades de streaming de datos. Este análisis se basa en una entrada de blog detallada de ByteByteGo ([Why is Kafka so fast? How does it work?](https://bytebytego.substack.com/p/why-is-kafka-so-fast-how-does-it)), que complementa el contenido del video y proporciona ideas adicionales.

#### Componentes Principales y Arquitectura de Kafka
La velocidad de Kafka comienza con sus componentes principales:
- **Productores (Producers)**: Son aplicaciones o sistemas que generan y envían eventos a los temas de Kafka. Por ejemplo, una aplicación web podría producir eventos para las interacciones de los usuarios.
- **Brokers**: Son los servidores que forman un clúster, responsables de almacenar datos, gestionar particiones y manejar la replicación. Una configuración típica podría involucrar múltiples brokers para tolerancia a fallos y escalabilidad.
- **Consumidores (Consumers)**: Aplicaciones que se suscriben a temas para leer y procesar eventos, como motores de análisis que procesan datos en tiempo real.

La arquitectura posiciona a Kafka como una plataforma de streaming de eventos, utilizando "evento" en lugar de "mensaje", distinguiéndolo de las colas de mensajes tradicionales. Esto es evidente en su diseño, donde los eventos son inmutables y ordenados por offsets dentro de las particiones, como se detalla en la entrada de blog.

| Componente      | Función                                                                 |
|-----------------|-------------------------------------------------------------------------|
| Productor       | Envía eventos a los temas, iniciando el flujo de datos.                |
| Broker          | Almacena y gestiona datos, maneja la replicación y atiende a los consumidores. |
| Consumidor      | Lee y procesa eventos de los temas, permitiendo análisis en tiempo real. |

La entrada de blog incluye un diagrama en [esta URL](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd3690db-87b8-4165-8798-37d1d083f837_1600x1527.png) que ilustra esta arquitectura, mostrando la interacción entre productores, brokers y consumidores en modo clúster.

#### Arquitectura por Capas: Cómputo y Almacenamiento
La arquitectura de Kafka se bifurca en:
- **Capa de Cómputo (Compute Layer)**: Facilita la comunicación a través de APIs:
  - **API de Productor (Producer API)**: Utilizada por las aplicaciones para enviar eventos.
  - **API de Consumidor (Consumer API)**: Permite leer eventos.
  - **API de Kafka Connect**: Se integra con sistemas externos como bases de datos.
  - **API de Kafka Streams**: Soporta el procesamiento de flujos, como crear un KStream para un tema como "pedidos" (orders) con Serdes para serialización, y ksqlDB para trabajos de procesamiento de flujos con una API REST. Un ejemplo proporcionado es suscribirse a "pedidos", agregar por productos y enviar a "pedidosPorProducto" (ordersByProduct) para análisis.
- **Capa de Almacenamiento (Storage Layer)**: Comprende brokers de Kafka en clústeres, con datos organizados en temas y particiones. Los temas son similares a tablas de base de datos, y las particiones se distribuyen entre nodos, asegurando escalabilidad. Los eventos dentro de las particiones están ordenados por offsets, son inmutables y de solo adición, con la eliminación tratada como un evento, mejorando el rendimiento de escritura.

La entrada de blog detalla esto, señalando que los brokers gestionan particiones, lecturas, escrituras y replicaciones, con un diagrama en [esta URL](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb869cd88-3d6e-43af-8fd0-26f3737d8f1f_1600x559.png) que ilustra la replicación, como la Partición 0 en "pedidos" con tres réplicas: líder en el Broker 1 (offset 4), seguidores en el Broker 2 (offset 2) y Broker 3 (offset 3).

| Capa            | Descripción                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| Capa de Cómputo | APIs para interacción: Productor, Consumidor, Connect, Streams y ksqlDB.    |
| Capa de Almacenamiento | Brokers en clústeres, temas/particiones distribuidos, eventos ordenados por offsets. |

#### Planos de Control y Datos
- **Plano de Control (Control Plane)**: Gestiona los metadatos del clúster, históricamente usando Zookeeper, ahora reemplazado por el módulo KRaft con controladores en brokers seleccionados. Esta simplificación elimina Zookeeper, facilitando la configuración y haciendo la propagación de metadatos más eficiente a través de un tema especial, como se señala en la entrada de blog.
- **Plano de Datos (Data Plane)**: Maneja la replicación de datos, con un proceso donde los seguidores emiten FetchRequest, el líder envía datos y confirma registros antes de un cierto offset, asegurando consistencia. El ejemplo de la Partición 0 con offsets 2, 3 y 4 destaca esto, con un diagrama en [esta URL](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe17a4454-a194-45f9-8a1f-f4882501657c_1095x1600.png).

#### Estructura del Registro y Operaciones del Broker
Cada registro, la abstracción de un evento, incluye:
- Marca de tiempo (Timestamp): Cuándo se creó.
- Clave (Key): Para ordenación, colocación conjunta (colocation) y retención, crucial para el particionado.
- Valor (Value): El contenido de los datos.
- Cabeceras (Headers): Metadatos opcionales.

La clave y el valor son arrays de bytes, codificados/decodificados con serdes, asegurando flexibilidad. Las operaciones del broker implican:
- La solicitud del productor llega al búfer de recepción del socket.
- El hilo de red la mueve a una cola de solicitudes compartida.
- El hilo de E/S valida el CRC, la añade al registro de confirmaciones (commit log) (segmentos de disco con datos e índice).
- Las solicitudes se almacenan en el purgatorio para replicación.
- La respuesta se encola, el hilo de red la envía a través del búfer de envío del socket.

Este proceso, optimizado para E/S secuencial, se detalla en la entrada de blog, con diagramas que ilustran el flujo, contribuyendo significativamente a la velocidad de Kafka.

| Componente del Registro | Propósito                                                                 |
|-------------------------|-------------------------------------------------------------------------|
| Marca de Tiempo         | Registra cuándo se creó el evento.                                      |
| Clave                   | Asegura la ordenación, colocación conjunta y retención para el particionado. |
| Valor                   | Contiene el contenido real de los datos.                                |
| Cabeceras               | Metadatos opcionales para información adicional.                        |

#### Optimizaciones de Rendimiento
Varias decisiones de diseño mejoran la velocidad de Kafka:
- **Registros de Solo Adición (Append-Only Logs)**: Escribir secuencialmente al final de un archivo minimiza el tiempo de búsqueda en disco, similar a añadir entradas a un diario al final, más rápido que insertar en medio del documento.
- **Principio de Cero Copia (Zero-Copy Principle)**: Transfiere datos directamente del productor al consumidor, reduciendo la carga de la CPU, como mover una caja del camión al almacén sin desempaquetar, ahorrando tiempo.
- **Procesamiento por Lotes (Batch Processing)**: Manejar datos en lotes reduce la sobrecarga por registro, mejorando la eficiencia.
- **Replicación Asíncrona (Asynchronous Replication)**: El broker líder atiende solicitudes mientras las réplicas se actualizan, asegurando disponibilidad sin impacto en el rendimiento.
- **Particionado (Partitioning)**: Distribuye datos a través de particiones para procesamiento paralelo, aumentando el rendimiento, un factor clave para manejar grandes volúmenes de datos.

Estas optimizaciones, como se explora en la entrada de blog, son la razón por la que Kafka logra alto rendimiento y baja latencia, haciéndolo adecuado para aplicaciones en tiempo real.

#### Conclusión e Ideas Adicionales
La velocidad de Apache Kafka es el resultado de su arquitectura meticulosamente diseñada y optimizaciones de rendimiento, aprovechando registros de solo adición, principios de cero copia, procesamiento por lotes, replicación asíncrona y particionado eficiente. Este análisis, basado en el video y complementado por la entrada de blog, proporciona una visión completa, inesperada en su profundidad para quienes esperaban una simple descripción general, revelando el intrincado equilibrio de decisiones de diseño que convierten a Kafka en un líder en el streaming de datos.

La entrada de blog también ofrece una prueba gratuita de 7 días para los archivos completos, accesible en [este enlace de suscripción](https://blog.bytebytego.com/subscribe?simple=true&next=https%3A%2F%2Fblog.bytebytego.com%2Fp%2Fwhy-is-kafka-so-fast-how-does-it&utm_source=paywall-free-trial&utm_medium=web&utm_content=137028631&coupon=3920da80), proporcionando más recursos para los interesados.

Esta exploración detallada asegura una comprensión completa, alineándose con la intención del video de educar sobre el rendimiento de Kafka, y está informada por la investigación y las ideas recopiladas de varias fuentes, asegurando precisión y profundidad.

#### Citas Clave
- [Video de YouTube: System Design: Why is Kafka fast?](https://www.youtube.com/watch?v=UNUz1-msbOM)
- [Entrada de blog de ByteByteGo: Why is Kafka so fast? How does it work?](https://bytebytego.substack.com/p/why-is-kafka-so-fast-how-does-it)
- [Diagrama de arquitectura de Kafka - ByteByteGo](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd3690db-87b8-4165-8798-37d1d083f837_1600x1527.png)
- [Diagrama de replicación de Kafka - ByteByteGo](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb869cd88-3d6e-43af-8fd0-26f3737d8f1f_1600x559.png)
- [Diagrama de operaciones del broker de Kafka - ByteByteGo](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe17a4454-a194-45f9-8a1f-f4882501657c_1095x1600.png)
- [Suscripción al boletín de ByteByteGo para la entrada sobre Kafka](https://blog.bytebytego.com/subscribe?simple=true&next=https%3A%2F%2Fblog.bytebytego.com%2Fp%2Fwhy-is-kafka-so-fast-how-does-it&utm_source=paywall-free-trial&utm_medium=web&utm_content=137028631&coupon=3920da80)