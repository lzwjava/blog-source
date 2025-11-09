---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Alibaba Reemplaza a IBM Oracle EMC
translated: true
type: note
---

### La Iniciativa "Remove IOE" de Alibaba

La campaña "Remove IOE" (o "去IOE") de Alibaba, lanzada alrededor de 2008-2009, fue un esfuerzo estratégico para eliminar la dependencia de las soluciones propietarias de los proveedores **IBM**, **Oracle** y **EMC** (acrónimo IOE). El objetivo era reducir costes, mejorar la escalabilidad y fomentar la innovación mediante el cambio a tecnologías de código abierto y desarrolladas internamente. Esto fue crucial para el crecimiento del comercio electrónico de Alibaba, ya que los sistemas IOE eran costosos y menos flexibles para una escala masiva.

#### Qué se Eliminó: La Pila IOE
El "IOE" se refería a una pila empresarial de alta gama e integrada dominada por estos proveedores. Aquí hay un desglose de los componentes clave que Alibaba eliminó progresivamente:

1. **IBM (Hardware y Middleware)**:
   - **Principales Componentes Eliminados**:
     - Mainframes de IBM (por ejemplo, zSeries o System z) y servidores de alta gama como Power Systems.
     - El sistema operativo AIX de IBM (variante Unix propietaria).
     - IBM WebSphere (servidor de aplicaciones/middleware para apps Java).
     - La base de datos IBM DB2 en algunos casos (aunque Oracle era el objetivo principal para las bases de datos).
   - **¿Por qué se Eliminó?** El hardware de IBM era fiable pero costoso, con un alto grado de dependencia del proveedor (lock-in) y no estaba optimizado para el escalado horizontal a escala de nube. Alibaba lo reemplazó con hardware commodity más barato (por ejemplo, servidores Intel/AMD ejecutando Linux).

2. **Oracle (Base de Datos)**:
   - **Principales Componentes Eliminados**:
     - Oracle Database (base de datos relacional empresarial, por ejemplo, Oracle 10g/11g RAC para alta disponibilidad).
     - Middleware de Oracle como Oracle Fusion Middleware o WebLogic Server.
   - **¿Por qué se Eliminó?** Las tarifas de licencia eran exorbitantes (escalaban con los núcleos de CPU y los usuarios), y no era ideal para las cargas de trabajo masivas de lectura/escritura de Alibaba (por ejemplo, los picos de transacciones de Taobao). La naturaleza propietaria de Oracle limitaba la personalización.

3. **EMC (Almacenamiento)**:
   - **Principales Componentes Eliminados**:
     - Arrays de almacenamiento EMC Symmetrix o Clariion (sistemas de almacenamiento empresarial SAN/NAS).
   - **¿Por qué se Eliminó?** Almacenamiento propietario costoso con dependencia del proveedor; difícil de escalar linealmente para datos a nivel de petabyte en el comercio electrónico.

La pila IOE general era un ecosistema "cerrado": servidores IBM ejecutando AIX, Oracle DB encima, almacenado en arrays EMC, con middleware de IBM uniéndolo todo. Esto era común en las empresas tradicionales, pero era un cuello de botella para las necesidades de Alibaba.

#### Qué Reemplazó a la Pila IOE
Alibaba reconstruyó todo sobre bases de código abierto, hardware commodity y desarrollos personalizados. Reemplazos clave:

- **Capa de Hardware/SO (Reemplazando a IBM)**:
  - Servidores commodity x86 (por ejemplo, de Dell, HP o de construcción personalizada).
  - Distribuciones de Linux (inicialmente CentOS/RHEL; más tarde ALINUX propio de Alibaba Cloud).
  - Herramientas de orquestación internas para la gestión de clústeres.

- **Capa de Base de Datos (Reemplazando a Oracle)**:
  - **Inicio de Código Abierto**: MySQL (Alibaba contribuyó enormemente; ahora es un fork de MySQL 5.5/5.6 con parches AliSQL para alta concurrencia).
  - **Desarrollos Personalizados**:
    - **OceanBase**: Base de datos relacional distribuida de Alibaba (NewSQL), diseñada para fiabilidad de grado financiero (soporta transacciones ACID a escala masiva). Ahora es de código abierto y se utiliza en Alipay de Ant Group.
    - Tair/DRDS: Caché en memoria (como Redis) y particionado SQL distribuido para escalado horizontal.
  - Esto permitió manejar miles de millones de consultas diarias sin los costes de licencia de Oracle.

- **Capa de Almacenamiento (Reemplazando a EMC)**:
  - Almacenamiento distribuido basado en Ceph o HDFS.
  - PolarFS de Alibaba o almacenamiento personalizado de bloques/objetos en discos commodity.
  - Más tarde evolucionó hacia Alibaba Cloud OSS (Object Storage Service) y EBS (Elastic Block Store).

- **Capa de Middleware/Aplicación**:
  - HSF (High-Speed Service Framework) para microservicios (reemplazando a WebSphere).
  - Apache Dubbo para RPC/descubrimiento de servicios.
  - Herramientas internas como SOFA (Scalable Open Framework Architecture).

#### Impacto y Legado
- **Ahorro de Costes**: Redujo los costes de hardware/base de datos en un 70-80% inicialmente.
- **Escalabilidad**: Permitió a Alibaba manejar los picos del Día del Soltero (por ejemplo, más de 500,000 pedidos por segundo).
- **Innovación**: Impulsó el negocio de nube de Alibaba (Alibaba Cloud, ahora la más grande del mundo por algunas métricas) y las contribuciones de código abierto (por ejemplo, OceanBase es utilizado por bancos a nivel global).
- **Cronología**: Transición completada alrededor de 2012-2015; "Remove IOE" se convirtió en un mantra para las empresas tecnológicas chinas.

Si preguntas sobre detalles específicos (por ejemplo, desafíos de migración o la pila tecnológica actual de Alibaba), ¡avísame para más detalles! Fuentes: blogs oficiales de Alibaba, charlas de Jack Ma e informes técnicos de esa época.