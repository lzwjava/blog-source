---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Hoja de Ruta Progresiva de Sistemas Distribuidos
translated: true
type: note
---

Excelente — ese es un tema amplio y profundo. Construyamos una **hoja de ruta progresiva** para que domines los *Sistemas Distribuidos*, cubriendo desde los fundamentos (redes malladas, replicación, particionamiento, consenso, etc.) hasta la implementación práctica y la comprensión a nivel de investigación.

A continuación, una **hoja de ruta narrativa (no en tabla)** para que sea más fácil de leer en cualquier pantalla.

---

### **Etapa 1: Fundamentos — Comprender qué significa "Distribuido"**

Antes de sumergirte en Paxos o Raft, debes comprender profundamente qué significa *distribuido* y qué problemas surgen.

**Conceptos Clave**

* ¿Qué es un sistema distribuido (frente a uno centralizado)?
* Comunicación en red: latencia, ancho de banda, fiabilidad.
* Fallos: caída, partición de red, comportamiento bizantino.
* Consistencia, disponibilidad, tolerancia a particiones (teorema CAP).

**Lecturas Recomendadas**

* *"Notes on Distributed Systems for Young Bloods"* de Jeff Hodges
* *Designing Data-Intensive Applications* de Martin Kleppmann (primeros 5 capítulos)
* *The Google SRE Book* (Capítulo 1–2 para la mentalidad de fiabilidad y fallos)

**Práctica**

* Escribe un programa simple cliente-servidor usando sockets TCP en Python o Go.
* Usa Docker para simular particiones de red (`tc netem`).

---

### **Etapa 2: Comunicación y Coordinación**

Ahora céntrate en *cómo se comunican y coordinan los nodos* a través de redes no fiables.

**Temas Centrales**

* RPC (Llamadas a Procedimiento Remoto) y paso de mensajes.
* Formatos de serialización (JSON, Protobuf, Avro).
* Tiempo en sistemas distribuidos: marcas de tiempo de Lamport, relojes vectoriales.
* Elección de líder (Bully, elección basada en Raft).
* Protocolos de rumor (Gossip) y epidémicos.

**Proyectos**

* Implementa una cola de mensajes o un sistema de chat de juguete.
* Añade marcas de tiempo de Lamport para ordenar eventos.

**Recursos Recomendados**

* *"Time, Clocks, and the Ordering of Events in a Distributed System"* (Leslie Lamport, 1978)
* Videos de las conferencias 1–3 del MIT 6.824.

---

### **Etapa 3: Particionamiento y Replicación de Datos**

Este es el núcleo de la escalabilidad y la tolerancia a fallos.

**Conceptos**

* Fragmentación / particionamiento de datos: basado en hash, basado en rangos.
* Modelos de replicación: líder-seguidor, multi-líder, basado en quórum.
* Retraso de replicación y niveles de consistencia (fuerte, eventual, causal).

**Práctica**

* Construye un almacén de clave-valor distribuido simple usando particionamiento por hash.
* Simula añadir/eliminar nodos dinámicamente.

**Sistemas para Estudiar**

* Dynamo (Amazon)
* Cassandra
* Fragmentación en MongoDB
* Hash consistente

**Artículos**

* *Dynamo: Amazon’s Highly Available Key-Value Store* (2007)

---

### **Etapa 4: Consenso y Coordinación (Paxos, Raft, ZAB)**

El consenso es el **corazón** de los sistemas distribuidos — acordar un valor entre nodos no fiables.

**Protocolos Centrales**

* Paxos (y Multi-Paxos)
* Raft (más fácil de entender)
* Replicación con Vistas Selladas (Viewstamped Replication)
* ZAB (usado por ZooKeeper)

**Recursos**

* *Paxos Made Simple* (Lamport)
* *In Search of an Understandable Consensus Algorithm* (artículo de Raft)
* Laboratorios del MIT 6.824 sobre Raft

**Práctica**

* Implementa Raft en Go o Python.
* Usa etcd o ZooKeeper para coordinar microservicios.

---

### **Etapa 5: Tolerancia a Fallos, Recuperación y Membresía**

Aprende cómo los sistemas mantienen el servicio a pesar de caídas de nodos o particiones de red.

**Temas Clave**

* Latidos del corazón y detectores de fallos.
* Protocolos de membresía de clúster (SWIM).
* Puntos de control, instantáneas y compactación de logs.
* Transacciones distribuidas (2PC, 3PC).

**Proyectos**

* Extiende tu almacén de clave-valor para sobrevivir a caídas de nodos usando Raft.
* Experimenta con inyección de fallos (ej., eliminar nodos durante la operación).

**Recomendado**

* *The Chubby Lock Service for Loosely Coupled Distributed Systems* (Google)
* *ZooKeeper: Wait-free Coordination for Internet-scale Systems*

---

### **Etapa 6: Sistemas de Consulta y Cómputo Distribuidos**

Aprende cómo los sistemas de big data (Hadoop, Spark, Flink) utilizan principios distribuidos.

**Conceptos**

* Modelo de programación MapReduce.
* Ejecución de DAG distribuido (Spark, Flink).
* Planificación de tareas y recuperación de fallos.
* Localidad de datos y replicación en el cómputo.

**Proyectos**

* Implementa un framework MapReduce de juguete en Python.
* Escribe un conteo de palabras distribuido.

**Lecturas**

* *MapReduce: Simplified Data Processing on Large Clusters* (Google, 2004)
* *The Spark Paper (Matei Zaharia, 2010)*

---

### **Etapa 7: Temas Avanzados**

Una vez que te sientas cómodo, explora áreas más profundas.

**Direcciones**

* Tolerancia a Fallos Bizantinos (PBFT, Tendermint, HotStuff).
* Membresía por rumor y redes malladas (usadas en malla de servicios y P2P).
* CRDTs (Conflict-free Replicated Data Types) para consistencia eventual.
* Diseño distribuido nativo en la nube (Kubernetes, Istio, Linkerd).
* Observabilidad y trazado (Jaeger, OpenTelemetry).

**Recursos**

* *The Byzantine Generals Problem* (Lamport, 1982)
* *CRDTs: Consistency Without Consensus* (Shapiro, 2011)
* *The Datacenter as a Computer* (Google, 3ª edición)

---

### **Etapa 8: Sistemas del Mundo Real y Práctica**

Finalmente, conecta la teoría con sistemas distribuidos reales en la industria.

**Estudia Arquitecturas**

* Google Spanner, BigTable
* Kafka, Pulsar, NATS
* Plano de control de Kubernetes
* Arquitectura de microservicios de Netflix

**Haz Esto**

* Contribuye a sistemas distribuidos de código abierto (ej., etcd, NATS).
* Diseña tu propio sistema distribuido simple y escribe un documento de diseño al estilo de un artículo.

---

### **Extra: Redes Malladas y de Superposición**

Ya que mencionaste *malla*:

* Aprende sobre topologías de superposición: malla, anillo, árbol, rumor.
* Comprende Kademlia DHT (usado en BitTorrent).
* Aprende cómo las mallas de servicio (como Istio o Linkerd) manejan el tráfico distribuido mediante sidecars.

---

¿Te gustaría que convierta esta hoja de ruta en un **plan de aprendizaje estructurado de 6 o 12 meses** (con objetivos y proyectos semanales)? Eso facilitaría seguirla y medir el progreso.