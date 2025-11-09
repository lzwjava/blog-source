---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Comparación de Empaquetado WAR versus EAR
translated: true
type: note
---

### Resumen
En Java EE (ahora Jakarta EE), WAR (Web Archive) y EAR (Enterprise Archive) son formatos de empaquetado estándar para desplegar aplicaciones en servidores de aplicaciones como Tomcat, WildFly o GlassFish. WAR se centra en componentes de la capa web, mientras que EAR agrupa múltiples módulos para aplicaciones empresariales completas. A continuación, se presenta una comparación detallada.

| Aspecto              | WAR (Web Archive)                                                                 | EAR (Enterprise Archive)                                                                 |
|---------------------|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Propósito**       | Despliega aplicaciones web (p. ej., servlets, JSPs, contenido estático) como una única unidad para la funcionalidad de la capa web. | Despliega aplicaciones empresariales empaquetando múltiples submódulos (p. ej., WARs, EJB JARs) para sistemas distribuidos de múltiples capas. |
| **Contenido**       | - Archivos de aplicación web: JSPs, HTML/CSS/JS, servlets.<br>- Librerías: JARs en WEB-INF/lib.<br>- Descriptor de despliegue: web.xml (opcional en versiones modernas). | - Múltiples módulos: WARs, EJB JARs, client JARs.<br>- Librerías compartidas.<br>- Descriptor de despliegue: application.xml.<br>- RARs para adaptadores de recursos (opcional). |
| **Estructura**      | - Raíz: recursos estáticos (p. ej., index.html).<br>- WEB-INF/: classes, lib, web.xml. | - Raíz: META-INF/application.xml.<br>- Subdirectorios para cada módulo (p. ej., myapp.war, myejb.jar). |
| **Extensión de Archivo** | .war                                                                             | .ear                                                                                     |
| **Alcance de Despliegue** | Módulo único; se despliega en contenedores web (p. ej., Tomcat) o servidores de aplicaciones completos. | Múltiples módulos; se despliega solo en servidores de aplicaciones completos (p. ej., JBoss, WebLogic) para características empresariales como transacciones. |
| **Tamaño y Complejidad** | Más pequeño y simple; ideal para aplicaciones web independientes.                              | Más grande y complejo; soporta modularidad y recursos compartidos entre módulos.        |
| **Casos de Uso**    | Portales web, APIs REST, servicios simples (p. ej., aplicaciones web Spring Boot empaquetadas como WAR). | Sistemas empresariales complejos (p. ej., aplicaciones bancarias con interfaz web + lógica de negocio + acceso a datos). |
| **Dependencias**    | Depende del contenedor para servicios web; no tiene soporte integrado para EJB.                    | Soporta EJBs, JMS y dependencias entre módulos; promueve un acoplamiento débil.              |

### Resumen de Diferencias Clave
- **Modularidad**: WAR es monolítico para capas web; EAR permite la composición de múltiples WARs/JARs.
- **Requisitos del Servidor**: WAR funciona en servidores web ligeros; EAR necesita un servidor JEE completo.
- **Evolución**: Con las tendencias de microservicios y cloud-native (p. ej., Spring Boot, Quarkus), los WARs se usan a menudo para despliegues containerizados (Docker), mientras que los EARs son menos comunes pero aún vitales para aplicaciones empresariales heredadas.

Para ejemplos prácticos, consulta la documentación oficial de Jakarta EE: [Jakarta EE Tutorial](https://jakartaee.github.io/tutorial/) o los archivos de Java EE de Oracle: [Java EE Packaging](https://docs.oracle.com/javaee/7/tutorial/packaging.htm).