---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Análisis del Caso de Interrupción de AWS Octubre 2025
translated: true
type: note
---

### Interrupción de AWS del 20 de octubre de 2025: Análisis Detallado del Caso

La interrupción de AWS del 20 de octubre de 2025 fue una perturbación significativa que se originó en la región US East (N. Virginia) (us-east-1), el centro de datos más grande y crítico de AWS. Comenzó tarde el 19 de octubre, hora del Pacífico (PDT), y duró aproximadamente 16 horas, afectando a más de 140 servicios y propagándose globalmente debido a las dependencias de esta región. El incidente puso de relieve vulnerabilidades en la resolución DNS, las interdependencias de servicios y los procesos de recuperación, afectando a millones de usuarios en aplicaciones, sitios web y servicios. A continuación, se presenta un desglose basado en el informe post-mortem oficial de AWS y reportes contemporáneos.

#### Cronología
La interrupción se desarrolló en fases, comenzando con la detección y escalando a fallos en cascada antes de una recuperación escalonada. Momentos clave (todas las horas en PDT):

| Hora | Evento |
|------|--------|
| 11:49 PM (19 Oct) | Se detectaron mayores tasas de error y latencias en múltiples servicios de AWS en us-east-1. |
| 12:11 AM (20 Oct) | AWS reporta públicamente tasas de error elevadas; los reportes iniciales de usuarios se disparan en sitios de monitoreo como DownDetector. |
| 12:26 AM | El problema se identifica en fallos de resolución DNS para los endpoints de la API de DynamoDB en us-east-1. |
| 1:26 AM | Se confirman altas tasas de error específicamente para las APIs de DynamoDB, incluyendo Global Tables. |
| 2:22 AM | Se aplican mitigaciones iniciales; surgen signos tempranos de recuperación. |
| 2:24 AM | El problema de DNS de DynamoDB se resuelve, desencadenando una recuperación parcial del servicio, pero surgen deficiencias en el lanzamiento de EC2 y fallos en las comprobaciones de estado del Network Load Balancer (NLB). |
| 3:35 AM | DNS completamente mitigado; la mayoría de las operaciones de DynamoDB tienen éxito, pero los lanzamientos de EC2 permanecen afectados en todas las Zonas de Disponibilidad (AZs). |
| 4:08 AM | Trabajo continuo en errores de EC2 y retrasos en el sondeo de Lambda para las asignaciones de origen de eventos SQS. |
| 5:48 AM | Recuperación parcial de lanzamientos de EC2 en AZs seleccionadas; los backlog de SQS comienzan a limpiarse. |
| 6:42 AM | Se implementan mitigaciones en todas las AZs; AWS aplica rate limiting en nuevos lanzamientos de instancias EC2 para estabilizar. |
| 7:14 AM | Persisten errores de API y problemas de conectividad en varios servicios; los fallos que impactan a los usuarios alcanzan su punto máximo (ej. interrupciones de aplicaciones). |
| 8:04 AM | La investigación se centra en la red interna de EC2. |
| 8:43 AM | Se identifica la causa principal de los problemas de red: una deficiencia en el subsistema interno de EC2 para el monitoreo de estado del NLB. |
| 9:13 AM | Mitigaciones adicionales para las comprobaciones de estado del NLB. |
| 9:38 AM | Las comprobaciones de estado del NLB se recuperan completamente. |
| 10:03 AM – 12:15 PM | Mejoras progresivas en los lanzamientos de EC2; las invocaciones de Lambda y la conectividad se estabilizan en fases en todas las AZs. |
| 1:03 PM – 2:48 PM | Se reducen las limitaciones (throttles); se procesan los backlog para servicios como Redshift, Amazon Connect y CloudTrail. |
| 3:01 PM | Se restaura la normalidad operativa completa para todos los servicios; se espera que los backlog menores (ej. AWS Config, Redshift) se liquiden en horas. |
| 3:53 PM | AWS declara resuelta la interrupción. |

Los reportes de usuarios en plataformas como DownDetector alcanzaron su punto máximo alrededor de las 6 AM PDT, con más de 5,000 incidentes antes de descender.

#### Causa Principal
La interrupción se originó por un fallo en la resolución DNS que afectó a los endpoints de servicio de DynamoDB en us-east-1. DynamoDB, un servicio de base de datos NoSQL, actúa como un "plano de control" crítico para muchas funciones de AWS, manejando metadatos, sesiones y enrutamiento. Cuando el DNS no pudo resolver estos endpoints, las APIs de DynamoDB experimentaron latencias y errores elevados.

Este problema inicial se resolvió rápidamente, pero desencadenó una cascada:
- Los lanzamientos de instancias EC2 fallaron debido a su dependencia de DynamoDB para el almacenamiento de metadatos.
- Un error subyacente en el subsistema interno de EC2 (responsable de monitorear el estado del NLB) exacerbó los problemas de conectividad de red, lo que llevó a deficiencias más amplias en el balanceo de carga y las llamadas a la API.
- Los esfuerzos de recuperación involucraron la limitación (throttling) (ej., limitando lanzamientos de EC2 e invocaciones de Lambda) para prevenir sobrecargas, pero los reintentos de los servicios dependientes amplificaron la tensión.

AWS confirmó que no fue un ciberataque, sino una falla relacionada con la infraestructura, posiblemente vinculada a una actualización defectuosa de la base de datos DNS o una falla del sistema de respaldo. El efecto dominó global ocurrió porque us-east-1 aloja planos de control clave para servicios como IAM y Lambda, incluso para recursos en otras regiones.

#### Servicios Afectados
Más de 142 servicios de AWS se vieron impactados, principalmente aquellos que dependen de DynamoDB, EC2 o los endpoints de us-east-1. Categorías principales:

- **Bases de Datos y Almacenamiento**: DynamoDB (primario), RDS, Redshift, SQS (backlogs).
- **Computación y Orquestación**: EC2 (lanzamientos), Lambda (invocaciones, sondeo), ECS, EKS, Glue.
- **Redes y Balanceo de Carga**: Network Load Balancer (comprobaciones de estado), API Gateway.
- **Monitoreo y Gestión**: CloudWatch, CloudTrail, EventBridge, IAM (actualizaciones), AWS Config.
- **Otros**: Amazon Connect, Athena y funciones globales como DynamoDB Global Tables.

No todos los servicios estuvieron completamente inactivos; muchos experimentaron errores parciales o retrasos, pero la naturaleza interconectada significó que incluso problemas menores se propagaron.

#### Impactos
La interrupción afectó a ~1/3 de las aplicaciones dependientes de internet, impactando a un estimado de 100+ millones de usuarios en todo el mundo. Ejemplos de alto perfil:
- **Social y Medios**: Snapchat (fallos de inicio de sesión), Reddit (interrupciones), Twitch (problemas de streaming).
- **Gaming**: Roblox (caídas de servidor), Fortnite (fallos en el emparejamiento).
- **Finanzas y Pagos**: Venmo, bancos como Lloyds (retrasos en transacciones), HMRC (servicios fiscales del Reino Unido).
- **Retail y Comercio Electrónico**: Porciones del propio sitio de venta minorista de Amazon; check-ins de aerolíneas (ej., retrasos de Delta, United).
- **Otros**: Dispositivos Alexa (fallos de voz), Twilio (fallos de comunicación).

Las estimaciones económicas sitúan las pérdidas en más de $500 millones, con un aumento del 300% en escaneos de ciberseguridad mientras los usuarios entraban en pánico. Subrayó la centralización de internet: us-east-1 maneja ~30% del tráfico de AWS, convirtiéndolo en un único punto de fragilidad a pesar de los diseños multi-AZ.

#### Resolución y Lecciones Aprendidas
AWS resolvió el problema mediante mitigaciones específicas: correcciones de DNS, parches en el subsistema para EC2/NLB y reducciones progresivas de las limitaciones (throttling). Posterior al incidente, aconsejaron:
- Reintentar peticiones fallidas.
- Limpiar las cachés DNS.
- Distribuir recursos en múltiples AZs/regiones (ej., mediante Auto Scaling Groups).
- Usar cuotas de servicio y caching para amortiguar contra reintentos.

Las conclusiones más amplias incluyen la necesidad de una mejor redundancia en los planos de control, detección de anomalías impulsada por IA para una triaje más rápida y estrategias de nube diversificadas. AWS se comprometió a un análisis de causa raíz (RCA) completo para los clientes, enfatizando que tales eventos, aunque raros, revelan desafíos de escalado a hiperescala.

Esta fue la interrupción más disruptiva de AWS en us-east-1 desde 2021, pero la recuperación fue más rápida que los precedentes históricos debido a las herramientas automatizadas.

#### Referencias
- [AWS Health Dashboard: Service Health - Oct 20, 2025](https://health.aws.amazon.com/health/status?eventID=arn:aws:health:us-east-1::event/MULTIPLE_SERVICES/AWS_MULTIPLE_SERVICES_OPERATIONAL_ISSUE/AWS_MULTIPLE_SERVICES_OPERATIONAL_ISSUE_BA540_514A652BE1A)
- [AWS Outage Analysis: October 20, 2025](https://www.thousandeyes.com/blog/aws-outage-analysis-october-20-2025)
- [Amazon's massive AWS outage points to a key weakness in the modern internet](https://finance.yahoo.com/news/amazons-massive-aws-outage-points-to-a-key-weakness-in-the-modern-internet-145418180.html)
- [What caused Amazon's AWS outage, and why did so many major apps go offline?](https://www.aljazeera.com/news/2025/10/21/what-caused-amazons-aws-outage-and-why-did-so-many-major-apps-go-offline)
- [AWS Outage on October 20: How a DNS Glitch in DynamoDB Disrupted the Internet](https://medium.com/@ansababy/aws-outage-on-october-20-how-a-dns-glitch-in-dynamodb-disrupted-the-internet-40e1f0440a12)
- [Update - AWS services operating normally](https://www.aboutamazon.com/news/aws/aws-service-disruptions-outage-update)
- [AWS was down — live updates following massive outage](https://www.tomsguide.com/news/live/amazon-outage-october-2025)