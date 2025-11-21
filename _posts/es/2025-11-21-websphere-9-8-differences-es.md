---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Diferencias Clave Entre WebSphere 9.0 y 8.0
translated: true
type: note
---

### Principales diferencias entre IBM WebSphere Application Server (WAS) 9.0 y 8.0

IBM WebSphere Application Server (WAS) es un servidor de aplicaciones Java EE de nivel empresarial. La versión 8.0 (lanzada en 2011) introdujo el cumplimiento de Java EE 6, mientras que la versión 9.0 (lanzada en 2017) avanzó a Java EE 7 con un enfoque en modernizar el perfil tradicional para alinearse con tiempos de ejecución más ligeros y aptos para la nube, como Liberty. A continuación, describiré las diferencias clave en una tabla para mayor claridad, basándome en la documentación oficial de IBM y las notas de la versión. Estas abarcan la compatibilidad con Java, el cumplimiento de estándares, la arquitectura y la implementación.

| Aspecto                  | WAS 8.0                                                                 | WAS 9.0                                                                 |
|-------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| **Compatibilidad con Java SE**    | Utiliza por defecto Java SE 6; soporte opcional para Java SE 7 mediante configuración. | Utiliza por defecto Java SE 8 como plataforma principal, usando IBM SDK Java 8 para plena compatibilidad con Oracle Java 8. Esto permite expresiones lambda, streams y otras características de SE 8. |
| **Cumplimiento de Java EE** | Soporte completo para Java EE 6, incluyendo JPA 2.0, JSF 2.0 y Servlet 3.0.    | Soporte completo para Java EE 7, añadiendo características como WebSocket 1.0, JSON-P 1.0, Batch 1.0 y utilidades de concurrencia mejoradas. Esto equipara la edición tradicional con las capacidades de Liberty de versiones anteriores. |
| **Integración del Perfil Liberty** | Liberty se introdujo en la versión 8.5 (no en el núcleo de la 8.0); la 8.0 se centra únicamente en el perfil completo tradicional. | Tiempo de ejecución Liberty (versión 16.0.0.2) profundamente integrado como una alternativa ligera y modular al perfil completo, optimizado para aplicaciones nativas de la nube. Liberty está incluido y soporta entrega continua. |
| **Modelo de Implementación**   | Principalmente local; se instala mediante Installation Manager con ediciones como Base y Network Deployment (ND) para clustering. | Primera versión lanzada simultáneamente de forma local y como servicio en IBM Cloud. Soporta implementaciones en nube híbrida con mejores ganchos para containerización. |
| **Rendimiento y Gestión** | Hasta un 20-26% de ganancia en rendimiento sobre WAS 7; gestión inteligente en la edición ND. | Se basa en la 8.0 con más optimizaciones para la eficiencia de recursos; herramientas administrativas mejoradas para migración y comparación de configuraciones. |
| **Fin del Soporte**     | El soporte extendido finalizó en 2019; ya no recibe correcciones.              | Soporte activo hasta al menos 2027, con paquetes de corrección regulares (ej., 9.0.5.x) que abordan seguridad y compatibilidad. |
| **Consideraciones de Migración** | N/A (línea base).                                                        | Migración más fácil desde la 8.x mediante herramientas como la Configuration Comparison Tool; alineación automática de puertos y manejo de APIs obsoletas para la transición a Java SE 8. |

#### Puntos Clave
- **Salto Más Grande**: El cambio a Java EE 7 y Java SE 8 es el más significativo, permitiendo características y estándares Java modernos que se previewearon en Liberty anteriormente. Si ejecutas aplicaciones legacy Java EE 6, la migración a la 9.0 es sencilla pero puede requerir pruebas para cambios específicos de SE 8.
- **Cuándo Actualizar**: Elige la 9.0 para necesidades de nube/híbridas o características de EE 7; mantén la 8.0 (o actualiza a la 8.5.5) solo para mantenimiento a corto plazo de aplicaciones antiguas.
- Para guías de migración detalladas, consulta la documentación oficial de IBM.

**Referencias**:
- [IBM WebSphere Application Server Wikipedia](https://en.wikipedia.org/wiki/IBM_WebSphere_Application_Server)
- [Java SE 8 in WAS Traditional V9](https://www.ibm.com/docs/en/was/9.0.5?topic=waso-java-se-8-in-websphere-application-server-traditional-v9)
- [WAS Version Comparison Slides](https://www.slideshare.net/ejlp12/ibm-websphere-application-server-version-to-version-comparison)
- [WAS Configuration Comparison Tool](https://www.ibm.com/support/pages/websphere-application-server-configuration-comparison-tool)