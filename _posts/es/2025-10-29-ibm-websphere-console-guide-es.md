---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Guía de Navegación de la Consola Administrativa de IBM WebSphere
translated: true
type: note
---

### Consola administrativa de IBM WebSphere Application Server (WAS): Panel de navegación izquierdo

La vista izquierda en la consola administrativa de IBM WebSphere Application Server (WAS) (también conocida como Consola de Soluciones Integradas) es un árbol de navegación jerárquico que organiza las tareas de configuración y gestión. Proporciona acceso rápido a áreas clave para administrar el entorno del servidor, las aplicaciones y los recursos. La estructura exacta puede variar ligeramente según la versión de WAS (por ejemplo, 8.5, 9.0) y la edición (Base vs. Network Deployment), pero las categorías principales de nivel superior son consistentes.

A continuación se muestra una lista de las principales secciones de nivel superior en el árbol de navegación, con breves descripciones de sus propósitos principales. Las subsecciones son expandibles (usando iconos +/−) para tareas más granulares.

#### Principales secciones de nivel superior
- **Aplicaciones**  
  Se utiliza para desplegar, instalar, actualizar, iniciar/detener y gestionar aplicaciones (por ejemplo, archivos EAR/WAR).  
  *Subsecciones clave*: Aplicaciones Empresariales, Aplicaciones Empresariales WebSphere, Módulos Web, Bibliotecas Compartidas.  
  *Tareas comunes*: Instalar nuevas aplicaciones, mapear módulos a servidores, configurar cargadores de clases.

- **Recursos**  
  Configura recursos compartidos como bases de datos, mensajería y agrupaciones de conexiones que las aplicaciones pueden utilizar.  
  *Subsecciones clave*: JDBC (orígenes de datos/proveedores), JMS (colas/temas), Sesiones de JavaMail, Proveedores de URL.  
  *Tareas comunes*: Configurar orígenes de datos JDBC, crear fábricas de conexiones JMS.

- **Servicios**  
  Gestiona servicios a nivel de servidor como seguridad, mensajería y protocolos de comunicación.  
  *Subsecciones clave*: Seguridad (seguridad global, usuarios/grupos, autenticación), Proveedores de Correo, Puertos, Servicio ORB, Servicio de Transacciones.  
  *Tareas comunes*: Habilitar SSL, configurar registros de usuarios, ajustar asignaciones de puertos.

- **Servidores**  
  Maneja instancias de servidor, agrupaciones (clustering) y definiciones de servidores web.  
  *Subsecciones clave*: Tipos de Servidor (servidores de aplicaciones WebSphere, servidores proxy WebSphere), Clusters, Servidores Web.  
  *Tareas comunes*: Iniciar/detener servidores, configurar ajustes JVM, crear clusters para alta disponibilidad.

- **Administración del Sistema**  
  Supervisa la topología general, incluyendo nodos, celdas y configuraciones de la consola.  
  *Subsecciones clave*: Nodos, Celdas, Deployment Manager, Preferencias de la Consola.  
  *Tareas comunes*: Sincronizar nodos, gestionar el gestor de despliegue, establecer temas/ámbitos de la consola.

- **Entorno**  
  Define variables específicas del entorno y alias.  
  *Subsecciones clave*: Variables de WebSphere, Alias de Hosts.  
  *Tareas comunes*: Establecer variables del sistema para rutas o propiedades.

- **Monitorización y Ajuste**  
  Monitoriza el rendimiento y ajusta el comportamiento en tiempo de ejecución.  
  *Subsecciones clave*: Infraestructura de Monitorización de Rendimiento (PMI), Servicios Personalizados, Registro y Traza.  
  *Tareas comunes*: Habilitar métricas, ajustar agrupaciones de hilos, ver métricas de solicitud.

- **Resolución de Problemas**  
  Accede a herramientas de diagnóstico y registros.  
  *Subsecciones clave*: Registros y Trazas, Primeros Pasos.  
  *Tareas comunes*: Descargar registros, habilitar especificaciones de traza.

#### Notas adicionales
- **Selección de Ámbito**: En la parte superior de muchas páginas, puede filtrar por ámbito (Celda, Nodo, Servidor) para limitar la visibilidad.
- **Actividades Guiadas**: A veces aparece como una sección de nivel superior o contextual para asistentes (por ejemplo, para proteger el entorno).
- Para acceder a la consola: Normalmente mediante `https://<host>:<port>/ibm/console` (puerto por defecto 9060 para administración, 9043 para seguro).
- Para detalles específicos de la versión (por ejemplo, WAS 9.0), consulte la documentación oficial de IBM, ya que se producen pequeños cambios en la interfaz de usuario en las actualizaciones.

[WebSphere Administrative Console - 101](https://www.ibm.com/community/101/websphere/administrative-console/)  
[Introduction: Administrative Console (WAS 9.0.5)](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=administration-introduction-administrative-console)  
[WebSphere Application Server V7: Administration Consoles (Redpaper)](https://www.redbooks.ibm.com/redpapers/pdfs/redp4573.pdf)