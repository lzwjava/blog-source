---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Principales Interrupciones de Azure a lo Largo de la Historia
translated: true
type: note
---

Microsoft Azure, lanzado en 2010, ha experimentado varias interrupciones significativas a lo largo de los años, a menudo debido a errores de configuración, fallos de hardware o eventos externos como condiciones climáticas. A continuación se presenta un resumen cronológico de las más notables, centrándose en aquellas con un impacto generalizado en regiones o servicios. Esta lista se basa en informes oficiales, análisis históricos y revisiones de incidentes, destacando fechas, causas, áreas afectadas y duraciones cuando están disponibles.

| Fecha | Causa | Regiones/Servicios Afectados | Duración/Impacto |
|------|-------|---------------------------|-----------------|
| 29 de febrero de 2012 | Error de cálculo del año bisiesto en el código | Norteamérica (Azure Compute) | ~8 horas; interrumpió la gestión de aplicaciones y servicios para los usuarios. |
| 26 de julio de 2012 | Dispositivo de red mal configurado | Europa Occidental (Azure Compute) | >2 horas; indisponibilidad parcial en Europa. |
| 22 de febrero de 2013 | Certificado SSL caducado | Global (Azure Storage) | Varias horas; se emitieron créditos de servicio; también afectó a Xbox Live, Music y Video. |
| 30 de octubre de 2013 | Interrupción parcial de compute (problema de throttling) | Mundial (Azure Compute, funciones de gestión) | ~3-4 horas; afectó a las subidas de archivos y la gestión de sitios. |
| 22 de noviembre de 2013 | Problemas de almacenamiento y red | Centro Norte de EE. UU. (Xbox Live) | Varias horas en el día del lanzamiento de Xbox One; bajo impacto para los clientes pero alta visibilidad. |
| 19 de noviembre de 2014 | Cambio de configuración que causó un bucle infinito en Blob storage | Global (más de 20 servicios, incluido Azure Storage) | ~6-10 horas; capacidad reducida en múltiples regiones; afectó a Xbox Live, MSN y Visual Studio Online. |
| 15 de septiembre de 2016 | Interrupción global de DNS | Mundial (Azure DNS) | ~2 horas; amplias interrupciones de servicio. |
| 7 y 23 de marzo de 2017 | Múltiples incidentes (red y almacenamiento) | Global (Office 365, Skype, Xbox Live) | Hasta 16+ horas cada uno; problemas generalizados de acceso de usuarios. |
| 29 de septiembre de 2017 | Liberación de gas de supresión de incendios durante mantenimiento que provocó apagados | Regiones de EE. UU. (varios servicios) | ~7 horas; fallos intermitentes. |
| 4 de septiembre de 2018 | Rayo que causó un pico de voltaje y fallo del sistema de refrigeración | Centro Sur de EE. UU., múltiples regiones (más de 40 servicios) | >25 horas, algunos efectos hasta 3 días; gran tiempo de inactividad en todos los servicios. |
| 25 de enero de 2020 | Fallo de dependencia backend en Azure SQL Database | Global (casi todas las regiones, incluido US Gov/DoD) | ~6 horas; afectó a SQL DB, Application Gateway, Bastion y Firewall. |
| 1 de abril de 2021 | Problema generalizado de DNS en la infraestructura de red | Global (EE. UU., Europa, Asia, etc.) | ~1.5 horas; afectó a servicios dependientes de la red principal. |
| 1 de junio de 2022 | Problemas con los registros de inicio de sesión de Azure Active Directory | Global (múltiples regiones) | ~9.5 horas; impactó en AAD, Sentinel, Monitor y Resource Manager. |
| 29 de junio de 2022 | Inestabilidad no especificada del backend | Global (docenas de regiones) | ~24 horas intermitentes; afectó a Firewall, Synapse, Backup y más. |
| 25 de enero de 2023 | Comando de router defectuoso que causó una interrupción de red | Global (más de 25 regiones, incluyendo Este de EE. UU., Europa Occidental) | ~3.5 horas; latencia y fallos en M365 (Teams, Outlook), SharePoint y Office 365. |
| 9 de junio de 2023 | Ataque DDoS reclamado por Anonymous Sudan | Global (Azure Portal y servicios en la nube) | ~2.5 horas; portal y servicios relacionados caídos. |
| 13 de noviembre de 2024 | Fallos de resolución DNS para Storage | Múltiples (Este de EE. UU./2, Centro de EE. UU., Oeste de EE. UU./2, etc.) | ~8.5 horas; impactó en Databricks y Storage Accounts. |
| 26 de diciembre de 2024 | Incidente eléctrico en Availability Zone | Centro Sur de EE. UU. (Zona 03) | ~18 horas; afectó a Storage, VMs, Cosmos DB, SQL DB y más. |
| 9 de enero de 2025 | Interrupción de red | Este de EE. UU. 2 | >48 horas; afectó a Databricks, Synapse, Functions, App Service y VMs. |
| 10 de septiembre de 2025 | Sobrecarga del servicio allocator por un cambio de throttling | Este de EE. UU. 2 (Zonas 02/03) | ~10.5 horas; degradó las operaciones de VM, impactando en Backup, Batch, Kubernetes y Synapse. |
| 26-27 de septiembre de 2025 | Valor de certificado malformado en un cambio de configuración | Norte de Suiza (múltiples zonas) | ~22 horas; interrupciones generalizadas en API Management, App Service, Cosmos DB, VMs y Sentinel. |
| 9 de octubre de 2025 | Defecto en el plano de control de Azure Front Door | Europa y África | ~8 horas; latencia/timeouts en portales y servicios (hasta un 17% de tasa de error en África). |
| 9 de octubre de 2025 | Eliminación de configuración posterior por scripts de automatización | Global (portales de gestión) | ~4 horas; problemas de acceso a Azure Portal y otros tras el incidente de AFD. |

Estos incidentes representan una fracción del total de eventos, pero son los más disruptivos según su alcance y duración. Microsoft típicamente emite revisiones post-incidente (PIRs) para el aprendizaje, y la disponibilidad ha mejorado con el tiempo, con SLAs que apuntan a un tiempo de actividad del 99.99%.

## Referencias
- [A History of Microsoft Azure Outages](https://www.datacenterknowledge.com/outages/a-history-of-microsoft-azure-outages)
- [Microsoft Azure Outage History Overview](https://statusgator.com/blog/azure-outage-history/)
- [Azure Status History](https://azure.status.microsoft/en-us/status/history/)
- [Microsoft Azure Wikipedia - Outages Section](https://en.wikipedia.org/wiki/Microsoft_Azure#Outages)