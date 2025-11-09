---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Gran Interrupción de la Plataforma Google Cloud
translated: true
type: note
---

### Resumen
El 12 de junio de 2025, Google Cloud Platform (GCP) experimentó una interrupción global importante que duró aproximadamente 7,5 horas (desde las 10:51 PDT hasta las 18:18 PDT). El incidente se originó por un error en una función recién introducida en el sistema Service Control de Google, específicamente relacionado con las comprobaciones de políticas de cuota. Esto provocó que una actualización de cuota automatizada no válida se propagara globalmente, lo que llevó a un rechazo generalizado de API y sobrecargas de tareas, especialmente en regiones de alto tráfico como us-central1 (Iowa). La interrupción afectó el acceso a numerosos servicios de GCP, productos de Google Workspace y aplicaciones de terceros que dependen de la infraestructura de GCP, resultando en más de 1,4 millones de informes de usuarios en Downdetector.

### Cronología
(Todas las horas en US/Pacific, PDT)

- **10:51 AM**: Comienza la interrupción con un aumento de errores 503 en solicitudes de API externas en múltiples productos de GCP y Google Workspace, causando problemas de acceso intermitentes.
- **11:46 AM**: Los equipos de ingeniería confirman impactos generalizados en los servicios; la investigación está en curso.
- **12:09 PM**: Comienzan las mitigaciones; recuperación en la mayoría de las regiones excepto us-central1.
- **12:41 PM**: Se identifica la causa principal como datos de política de cuota no válidos; se implementa una omisión para las comprobaciones de cuota.
- **1:16 PM**: Recuperación completa de la infraestructura en todas las regiones excepto us-central1 y la multi-región US.
- **2:00 PM**: Señales de recuperación en us-central1; se espera mitigación completa en una hora.
- **3:16 PM**: La mayoría de los productos de GCP se recuperan, pero persisten problemas residuales en Dataflow, Vertex AI y Personalized Service Health.
- **5:06 PM**: Dataflow y Personalized Service Health resueltos; los problemas de Vertex AI continúan con un ETA para las 10:00 PM.
- **6:27 PM**: Vertex AI completamente recuperado en todas las regiones.
- **6:18 PM**: El incidente termina oficialmente con la restauración total del servicio.

La mitigación principal tomó aproximadamente 3 horas, pero las acumulaciones residuales y los errores extendieron el impacto total a 7,5 horas.

### Causa Principal
La interrupción fue desencadenada por una falla en la función Service Control, que gestiona las cuotas y políticas de la API. Un sistema automatizado insertó una política de cuota no válida que contenía campos vacíos o nulos en la base de datos. Debido a la replicación global (diseñada para una consistencia casi instantánea), estos datos corruptos se propagaron por todo el mundo en segundos. Cuando las solicitudes de API llegaban a la comprobación de cuota, resultaba en excepciones de puntero nulo y rechazos (errores elevados 503 y 5xx). En regiones grandes como us-central1, la afluencia de solicitudes fallidas causó graves sobrecargas de tareas y fallos en cascada en servicios dependientes. La nueva función carecía de validación suficiente para casos extremos como campos en blanco, y el sistema no "falló en abierto" (permitiendo que las solicitudes procedieran durante las comprobaciones).

### Servicios Afectados
La interrupción impactó a una amplia gama de productos de Google y servicios externos que dependen de GCP. Los servicios principales de GCP y Google Workspace experimentaron diversos grados de interrupción, incluyendo fallos de API y problemas de acceso a la interfaz de usuario (los recursos de streaming e IaaS no se vieron afectados).

#### Principales Productos de Google Cloud Afectados
- **Compute & Storage**: Google Compute Engine, Cloud Storage, Persistent Disk.
- **Bases de datos**: Cloud SQL, Cloud Spanner, Cloud Bigtable, Firestore.
- **Datos y Analítica**: BigQuery, Dataflow, Dataproc, Vertex AI (incluyendo Online Prediction y Feature Store).
- **Redes y Seguridad**: Cloud Load Balancing, Cloud NAT, Identity and Access Management (IAM), Cloud Security Command Center.
- **Herramientas de Desarrollo**: Cloud Build, Cloud Functions, Cloud Run, Artifact Registry.
- **IA/ML**: Vertex AI Search, Speech-to-Text, Document AI, Dialogflow.
- **Otros**: Apigee, Cloud Monitoring, Cloud Logging, Resource Manager API.

#### Principales Productos de Google Workspace Afectados
- Gmail, Google Drive, Google Docs, Google Meet, Google Calendar, Google Chat.

#### Servicios de Terceros Impactados
Muchas aplicaciones de consumo y empresariales alojadas o parcialmente dependientes de GCP experimentaron tiempo de inactividad:
- **Spotify**: Streaming y acceso a la aplicación interrumpidos para ~46,000 usuarios.
- **Discord**: Problemas de chat de voz y conectividad del servidor.
- **Fitbit**: Sincronización y funcionalidad de la aplicación detenidas.
- **Otros**: OpenAI (ChatGPT), Shopify, Snapchat, Twitch, Cloudflare (problemas de DNS en cascada), Anthropic, Replit, Microsoft 365 (parcial), Etsy, Nest.

La escala global amplificó el impacto, ya que GCP impulsa una parte significativa de la infraestructura backend de internet.

### Resolución
Los equipos de ingeniería de Google identificaron rápidamente la política no válida e implementaron una omisión para las comprobaciones de cuota, permitiendo que las solicitudes de API procedieran sin validación durante la crisis. Esto restauró la mayoría de las regiones para las 12:48 PM PDT. Para us-central1, se aplicaron mitigaciones de sobrecarga específicas, seguidas de una limpieza manual de la acumulación en servicios afectados como Dataflow y Vertex AI. El monitoreo confirmó la recuperación completa a las 6:18 PM PDT. No hubo pérdida de datos, pero algunos servicios experimentaron retrasos temporales.

### Impacto
- **Escala**: Más de 1,4 millones de informes en Downdetector, destacando la interrupción global en tiempo real.
- **Económico**: Miles de millones en productividad potencialmente perdida para las empresas; solo Spotify reportó frustración de los usuarios durante las horas pico.
- **Reputación**: Subrayó los riesgos de la concentración en la nube, con llamados a mejores estrategias multi-nube.

### Lecciones Aprendidas y Medidas Preventivas
Google emitió un post-mortem detallado enfatizando la resiliencia:
- **Cambios en la Arquitectura**: Modularizar Service Control para aislar fallos y permitir modos de "fallo en abierto".
- **Validación de Datos**: Propagación incremental de cambios globales con pre-validación; pruebas mejoradas para entradas no válidas.
- **Salvaguardas de Implementación**: Banderas de función obligatorias para actualizaciones críticas; análisis estático y manejo de errores mejorados.
- **Monitoreo y Comunicaciones**: Asegurar que las herramientas de detección de interrupciones permanezcan operativas de forma independiente; alertas automatizadas más rápidas para los clientes.
- **Más Amplio**: Retroceso aleatorio en la lógica de reintento para prevenir cascadas de sobrecarga.

Estos pasos tienen como objetivo prevenir incidentes similares, con auditorías continuas de los sistemas de cuota.

[Informe de Incidente de Google Cloud](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW)  
[Análisis de Interrupción de ThousandEyes](https://www.thousandeyes.com/blog/google-cloud-outage-analysis-june-12-2025)  
[Informe de Ookla Downdetector](https://www.ookla.com/articles/google-cloud-outage-june-2025)  
[Desglose de ByteByteGo](https://blog.bytebytego.com/p/how-the-google-cloud-outage-crashed)  
[Explicación de la Causa Principal en Medium](https://medium.com/@tahirbalarabe2/%EF%B8%8Fhow-a-single-google-cloud-bug-caused-global-internet-outage-on-june-12-2025-652a83ad9e68)