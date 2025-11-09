---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Gran Interrupción de Azure en Suiza Norte
translated: true
type: note
---

### Interrupción de Azure en Suiza Norte: 26-27 de septiembre de 2025

Este incidente fue una interrupción importante en toda la plataforma en la región de Suiza Norte, que afectó a múltiples zonas de disponibilidad. Duró aproximadamente 22 horas, comenzando a las 23:54 UTC del 26 de septiembre y resolviéndose completamente a las 21:59 UTC del 27 de septiembre. Aunque la mayoría de los servicios se recuperaron alrededor de las 04:00 UTC del 27 de septiembre, algunos problemas residuales requirieron intervención manual más tarde en el día.

#### Causa Raíz
La interrupción se originó por un cambio de configuración planificado en los certificados utilizados para autorizar la comunicación en la infraestructura del balanceador de carga de software. Uno de los nuevos certificados tenía un **valor malformado** que no fue detectado durante la validación. Este cambio siguió una ruta de implementación acelerada, que desplegó inesperadamente el cambio en múltiples zonas sin activar los mecanismos de protección de estado. Como resultado:
- Los balanceadores de carga perdieron conectividad con los recursos de almacenamiento y los nodos.
- Las máquinas virtuales afectadas detectaron desconexiones prolongadas del disco y se apagaron automáticamente para evitar la corrupción de datos.
- Esto se propagó a servicios dependientes, amplificando el impacto.

#### Servicios Afectados
La interrupción afectó a una amplia gama de servicios de Azure alojados en Suiza Norte, incluyendo:
- **Infraestructura central**: Azure Storage, Azure Virtual Machines (VMs), Azure Virtual Machine Scale Sets (VMSS)
- **Bases de datos**: Azure Cosmos DB, Azure SQL Database, Azure SQL Managed Instance, Azure Database for PostgreSQL
- **Procesamiento y aplicaciones**: Azure App Service, Azure API Management, Azure Kubernetes Service (AKS), Azure Databricks
- **Redes y seguridad**: Azure Application Gateway, Azure Firewall, Azure Cache for Redis
- **Análisis y monitoreo**: Azure Synapse Analytics, Azure Data Factory, Azure Stream Analytics, Azure Data Explorer, Azure Log Analytics, Microsoft Sentinel
- **Otros**: Azure Backup, Azure Batch, Azure Site Recovery, Azure Application Insights

Los servicios que dependían de estos (por ejemplo, aplicaciones personalizadas) también se vieron afectados, lo que provocó una indisponibilidad generalizada o un rendimiento degradado.

#### Cronología y Mitigación
- **23:54 UTC, 26 Sep**: Comienza el impacto después del despliegue del cambio de configuración.
- **00:08 UTC, 27 Sep**: El monitoreo automatizado detecta el problema.
- **00:12 UTC, 27 Sep**: Comienza la investigación por parte de los equipos de Azure Storage y Networking.
- **02:33 UTC, 27 Sep**: Se revierte el cambio de configuración.
- **03:40 UTC, 27 Sep**: Se completa la reversión del certificado.
- **04:00 UTC, 27 Sep**: La mayoría de los servicios se recuperan automáticamente; se identifican problemas residuales (por ejemplo, ciertas VM en estados detenidos/no correctos debido a condiciones de carrera o señales de apagado malinterpretadas).
- **06:19–14:15 UTC, 27 Sep**: Se desarrollan y validan scripts de recuperación; se realizan reinicios dirigidos para recursos afectados como VM de SQL Managed Instance, VM de Trusted Launch y clústeres de Service Fabric.
- **16:15 UTC, 27 Sep**: Recuperación parcial para los problemas residuales.
- **21:59 UTC, 27 Sep**: Se confirma la recuperación total después de las validaciones finales.

La mayoría de los recursos se recuperaron automáticamente después de la restauración de la conectividad, pero subconjuntos (por ejemplo, VM con extensiones personalizadas) necesitaron reinicios manuales para resolver problemas en la secuencia de inicio.

#### Lecciones Aprendidas y Mejoras
La Revisión Preliminar del Incidente de Microsoft destaca correcciones proactivas:
- Se añadió auditoría a los sistemas de despliegue y se eliminaron las canalizaciones aceleradas riesgosas (completado).
- Se mejoraron las medidas de seguridad con reversiones automáticas (completado).
- Próximamente: Mejor monitoreo para el estado de los recursos (para noviembre de 2025) y procesos de recuperación resilientes para minimizar el trabajo manual.

Este evento subraya los riesgos de los cambios de configuración en infraestructura compartida, pero la respuesta de Azure limitó la pérdida de datos y permitió una recuperación amplia y rápida.

[Historial de Estado de Azure](https://azure.status.microsoft/en-us/status/history/)