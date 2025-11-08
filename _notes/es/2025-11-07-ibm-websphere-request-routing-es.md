---
audio: false
generated: true
image: false
lang: es
layout: post
model: anthropic/claude-4.5-sonnet
title: Enrutamiento de Solicitudes de IBM WebSphere Explicado
translated: true
type: note
---

Permíteme explicar cómo IBM WebSphere Application Server (WAS) maneja las solicitudes entrantes y el enrutamiento:

## Flujo de Solicitudes en IBM WAS

Cuando llega una solicitud a IBM WAS, este es el flujo típico:

**1. Capa del Servidor Web (Opcional)**
- La solicitud llega primero a IBM HTTP Server (IHS) u otro servidor web
- El plugin del servidor web enruta a la instancia de WAS apropiada

**2. Punto de Entrada del Contenedor Web**
La solicitud ingresa a WAS a través del **Contenedor Web**, que es parte del motor principal de servlets. La estructura clave de paquetes es:

```
com.ibm.ws.webcontainer.*
```

**3. Cadena de Procesamiento de Solicitudes**

El enrutamiento ocurre a través de varios componentes:

**Framework del Canal de Transporte**
- `com.ibm.ws.channel.*` - maneja la comunicación de red
- Los canales de transporte HTTP reciben la solicitud

**Procesamiento del Contenedor Web**
```
com.ibm.ws.webcontainer.servlet.ServletWrapper
com.ibm.ws.webcontainer.filter.WebAppFilterManager
```

**4. Ejecución de la Cadena de Filtros**

Los filtros funcionan exactamente como los filtros estándar de Java Servlet pero son gestionados por WAS:

- **Definidos en web.xml** de tu aplicación
- Los filtros se encadenan en el orden especificado
- Cada filtro puede inspeccionar/modificar la solicitud y la respuesta
- Utiliza la interfaz estándar `javax.servlet.Filter`

```xml
<filter>
    <filter-name>MyFilter</filter-name>
    <filter-class>com.example.MyFilter</filter-class>
</filter>

<filter-mapping>
    <filter-name>MyFilter</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
```

**Orden de ejecución de los filtros:**
1. WAS carga las configuraciones de los filtros al iniciar la aplicación
2. WebAppFilterManager crea la cadena de filtros
3. En cada solicitud: Solicitud → Filtro1 → Filtro2 → ... → Servlet

## Paquetes Principales en IBM WAS

**Paquetes principales:**
- `com.ibm.ws.webcontainer.*` - Implementación del contenedor web
- `com.ibm.ws.runtime.*` - Servicios de tiempo de ejecución
- `com.ibm.websphere.servlet.*` - Extensiones específicas de WAS para servlets
- `com.ibm.ws.channel.*` - Capa de transporte
- `com.ibm.ejs.*` - Servicios del contenedor EJB
- `com.ibm.ws.naming.*` - Implementación de JNDI

## Mecanismo de Enrutamiento

**Enrutamiento por Host Virtual:**
- Configurado en la consola administrativa de WAS
- Mapea combinaciones de `nombre_de_host:puerto` a aplicaciones
- Configuración: `VirtualHost → Alias de Host → Aplicaciones`

**Enrutamiento por Raíz de Contexto:**
- Cada aplicación tiene una raíz de contexto (ej. `/myapp`)
- WAS mantiene un registro de las aplicaciones desplegadas
- Mapeo de URI: `http://servidor:puerto/raizDeContexto/rutaDelServlet`

**Mapeo de Servlets:**
- Definido en web.xml o anotaciones
- Coincidencia de patrones (exacta, ruta, extensión, por defecto)

## Secuencia de Inicio de la Aplicación

Cuando la aplicación inicia:
1. **Inicialización del ClassLoader** - La aplicación obtiene su propio cargador de clases
2. **Análisis de web.xml** - Se cargan filtros, servlets, listeners
3. **Se activan los ServletContextListeners** - `contextInitialized()`
4. **Filtros instanciados** - Se llama al método `init()`
5. **Servlets de carga al inicio** - Se inicializan los servlets eager
6. **Aplicación marcada como INICIADA** - Lista para aceptar solicitudes

El registro de enrutamiento se actualiza y la aplicación ahora está disponible en su raíz de contexto.

¿Esto aclara cómo WAS maneja el enrutamiento y filtrado de solicitudes?