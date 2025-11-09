---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Principales Interrupciones de AWS a lo Largo de la Historia
translated: true
type: note
---

### Principales interrupciones en la historia de AWS

Amazon Web Services (AWS) ha impulsado gran parte de internet desde 2006, pero como cualquier infraestructura a gran escala, ha enfrentado interrupciones ocasionales. Las interrupciones son infrecuentes en relación con sus vastas operaciones, pero las principales pueden extenderse a través de servicios dependientes, desde redes sociales hasta plataformas financieras. A continuación, se presenta una tabla que resume las interrupciones históricas clave, centrándose en eventos generalizados o de alto impacto. Estos se extraen de incidentes documentados que afectaron a múltiples servicios o clientes notables.

| Fecha              | Servicios/Regiones Afectados | Causa                          | Impacto |
|--------------------|---------------------------|--------------------------------|--------|
| 15 de febrero de 2008 | S3, EC2 (global)         | Fallo técnico no especificado | Interrumpió el almacenamiento y alojamiento de imágenes para varios sitios web, marcando uno de los primeros problemas importantes de AWS. |
| 21 de abril de 2011    | Múltiples servicios (US-East-1) | Fallo prolongado del centro de datos | Dejó fuera de servicio durante horas a sitios de alto perfil como Reddit y Quora, destacando las primeras preocupaciones sobre la fiabilidad. |
| 28 de febrero de 2017 | EC2, S3, RDS y otros (US-East-1) | Error humano: comando mal escrito durante la depuración | Una interrupción de varias horas afectó a Slack, Docker, Exora y otros; pérdidas estimadas en cientos de millones de dólares; el panel de control en la nube de AWS también falló. |
| 7 de diciembre de 2021  | Servicios del plano de control, incluyendo EC2, RDS, Lambda (US-East-1) | Error de software en el plano de control durante la conmutación por error, lo que llevó a fallos en cascada | La interrupción más larga de la historia reciente (más de 8 horas); afectó a Netflix, Disney+, Capital One y sitios gubernamentales; una segunda interrupción menor el 15 de diciembre afectó a servicios similares. |
| 13 de junio de 2023     | EC2 y servicios relacionados (múltiples regiones) | Problemas regionales no especificados | Una interrupción de gran alcance afectó a medios de comunicación (por ejemplo, Associated Press, Boston Globe) y sistemas de tránsito (NY MTA), durando varias horas. |
| 20 de octubre de 2025  | Endpoints de DynamoDB, lanzamientos de EC2 y múltiples servicios (US-East-1, con efecto global) | Fallo de resolución DNS para los endpoints de servicio de DynamoDB | Interrupción de un día (comenzó tarde el 19 de octubre PDT, resuelta para la tarde del 20 de octubre); impactó a Snapchat, Reddit, Roblox, Fortnite, bancos (por ejemplo, Lloyds) y HMRC; afectó a millones de usuarios al bloquear el acceso a ~1/3 de las aplicaciones dependientes de internet; AWS limitó algunas operaciones para la recuperación. |

Estos incidentes a menudo se originan por errores humanos, problemas de red o factores ambientales, y AWS ha mejorado la resistencia mediante redundancias como configuraciones multi-región. La interrupción de 2025 subraya los riesgos continuos de la dependencia excesiva de US-East-1, la región más ocupada de AWS.

Para más detalles:
- [A History of AWS Cloud and Data Center Outages](https://www.datacenterknowledge.com/outages/a-history-of-aws-cloud-and-data-center-outages)
- [The Biggest AWS Outage in History: December 7, 2021](https://aws.plainenglish.io/the-biggest-aws-outage-in-history-the-december-7-2021-us-east-1-meltdown-and-lessons-learned-2efab5a02de5)
- [What caused the AWS outage](https://www.bbc.com/news/articles/cev1en9077ro)
- [AWS Update on October 2025 Outage](https://www.aboutamazon.com/news/aws/aws-service-disruptions-outage-update)