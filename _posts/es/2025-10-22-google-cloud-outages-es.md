---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Principales interrupciones de Google Cloud Platform
translated: true
type: note
---

### Principales interrupciones en la historia de Google Cloud Platform (GCP)

Google Cloud Platform ha experimentado varias interrupciones significativas desde sus inicios, a menudo debido a errores de software, fallos de hardware, factores ambientales o problemas de capacidad. A continuación, se presenta una tabla que resume algunas de las más notables, seleccionadas por su escala, duración o impacto generalizado. Estos datos provienen de registros históricos hasta mediados de 2025.

| Fecha | Causa | Impacto |
|------|--------|--------|
| 14 de diciembre de 2020 | Reducción accidental de la capacidad en el sistema central de gestión de ID de usuario, afectando la autenticación basada en OAuth. | Interrupción global de ~90 minutos; interrumpió el acceso a Gmail, YouTube, Google Drive, servicios de GCP y aplicaciones como Pokémon GO para millones de usuarios en todo el mundo. |
| Julio de 2022 | Ola de calor extremo (más de 40°C) en Londres que provocó fallos en el sistema de refrigeración en la zona europe-west2-a. | Disrupciones regionales durante ~24 horas; afectó a Cloud Storage, BigQuery, Compute Engine, GKE y otros servicios, forzando failovers a otras regiones. |
| 8 de agosto de 2022 | Incidente eléctrico que provocó un incendio en el centro de datos de Council Bluffs, Iowa (no relacionado con los problemas concurrentes de búsqueda y mapas). | Respuesta localizada al incendio; latencia global en el servicio Cloud Logging durante días, impactando la monitorización y depuración para los usuarios de GCP. |
| 28 de abril de 2023 | Intrusión de agua e incendio en un centro de datos de París, desencadenando fallos multi-cluster en europe-west9-a. | Disrupciones generalizadas en Europa, Asia y América; afectó a VPC, Load Balancing, BigQuery y servicios de red durante horas o días. |
| 7-8 de agosto de 2024 | Fallos en la activación del servicio Cloud TPU durante la habilitación de API para Vertex AI. | Interrupción global durante ~14 horas; bloqueó las cargas y el entrenamiento de modelos de machine learning en Vertex AI en todas las regiones principales. |
| 23 de octubre de 2024 | Fallo de energía y arco eléctrico en la zona europe-west3-c (Frankfurt), degradando la infraestructura de refrigeración. | Interrupción regional de medio día (~8 horas); cierre parcial de la infraestructura, con desvío de tráfico a otras zonas. |
| 7-8 de enero de 2025 | Problemas interconectados que incluyen fallos de autenticación SAML en Apigee, errores HTTP en las APIs Vertex Gemini y bloqueos de publicación en Pub/Sub. | Disrupciones de varias horas durante más de 18 horas; afectó a la gestión de APIs, la inferencia de IA y la mensajería en tiempo real en varias regiones. |
| 12 de junio de 2025 | Error en una nueva función de Service Control (comprobaciones de políticas de cuota) que causó sobrecargas de tareas en regiones grandes como us-central1. | Interrupción global de ~7 horas; dejó fuera de servicio a Spotify, Discord, Fitbit y muchos otros servicios dependientes de GCP, con más de 1.4 millones de informes. |

Estos incidentes resaltan los dolores de crecimiento de GCP, desde los primeros problemas de App Engine a finales de la década de 2000 hasta fallos sistémicos más recientes. Google típicamente emite informes post-mortem y planes de remediación, como la modularización de componentes para "fallar en abierto". Para el estado más reciente, consulta [Google Cloud Service Health](https://status.cloud.google.com/).

[Una historia de las interrupciones de Google Cloud y los centros de datos](https://www.datacenterknowledge.com/outages/a-history-of-google-cloud-and-data-center-outages)  
[Interrupciones de los servicios de Google - Wikipedia](https://en.wikipedia.org/wiki/Google_services_outages)  
[Historial de interrupciones de Google Cloud | StatusGator](https://statusgator.com/blog/google-cloud-outage-history/)  
[Las 10 mayores interrupciones en la nube de 2025 (hasta ahora) - CRN](https://www.crn.com/news/cloud/2025/the-10-biggest-cloud-outages-of-2025-so-far)  
[Análisis de la interrupción de Google Cloud: 12 de junio de 2025 - ThousandEyes](https://www.thousandeyes.com/blog/google-cloud-outage-analysis-june-12-2025)