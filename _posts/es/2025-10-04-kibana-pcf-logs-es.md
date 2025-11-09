---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Configuración de Kibana para Registros de PCF
translated: true
type: note
---

Parece que "kabana" probablemente sea una referencia a **Kibana**, el panel de visualización de datos de código abierto para Elasticsearch. En el contexto de **Pivotal Cloud Foundry (PCF)** (ahora renombrado como VMware Tanzu Application Service), Kibana se usa comúnmente para buscar, visualizar y analizar registros a través del sistema de registro de la plataforma (Loggregator). PCF no ejecuta Kibana de forma nativa de manera independiente, sino que lo integra a través del tile/servicio **Log Search**, que almacena los registros en Elasticsearch y expone Kibana para consultarlos.

Si no es a esto a lo que te refieres, ¡no dudes en aclararlo! A continuación, explicaré cómo configurar y usar Kibana con los registros de PCF. Esto asume que eres un administrador con acceso a PCF Ops Manager y tienes un despliegue de PCF en ejecución (versión 2.0+). Ten en cuenta que el registro de PCF ha evolucionado; consulta la documentación de tu versión para obtener detalles específicos.

### Prerrequisitos
- **Versión de PCF**: Log Search (con Kibana) está disponible en PCF 2.2+. Las versiones anteriores usaban un tile "ELK" (Elasticsearch, Logstash, Kibana) separado.
- **Tiles/Servicios**: Asegúrate de tener el tile **Elastic Runtime** (para Loggregator) y el tile **Log Search** instalados a través de Pivotal Network (ahora Broadcom Support Portal).
- **Acceso**: Privilegios de administrador en Ops Manager y en la herramienta de línea de comandos de PCF (cf).
- **Recursos**: Asigna recursos suficientes (por ejemplo, 4-8 GB de RAM para Log Search, dependiendo del volumen de registros).

### Paso 1: Instalar y Configurar el Tile de Log Search en Ops Manager
El tile de Log Search reenvía los registros de PCF (de aplicaciones, plataformas y componentes del sistema) a Elasticsearch, haciéndolos consultables a través de Kibana.

1. **Descargar e Importar el Tile**:
   - Inicia sesión en el Broadcom Support Portal (anteriormente Pivotal Network).
   - Descarga el tile **Log Search for PCF** (por ejemplo, la versión que coincida con tu release de PCF).
   - En Ops Manager (interfaz web), ve a **Catalog** > **Import a Product** y carga el tile.

2. **Configurar el Tile**:
   - En Ops Manager, ve al tile **Elastic Runtime** > pestaña **Loggregator**:
     - Habilita **Loggregator forwarding to external systems** (por ejemplo, configura el reenvío syslog o HTTP si es necesario, pero para Log Search, es interno).
     - Establece **Loggregator log retention** en un valor como 5-30 días.
   - Ve al tile **Log Search**:
     - **Assign Availability Zones**: Selecciona al menos una AZ para alta disponibilidad.
     - **Elasticsearch Configuration**:
       - Establece el número de instancias (comienza con 3 para producción).
       - Configura el almacenamiento (por ejemplo, discos persistentes de 100 GB).
       - Habilita la seguridad (por ejemplo, TLS para Elasticsearch).
     - **Kibana Configuration**:
       - Habilita Kibana (viene incluido).
       - Establece las credenciales de administrador (nombre de usuario/contraseña).
     - **Loggregator Integration**:
       - Establece el número máximo de líneas de registro por segundo (por ejemplo, 1000-5000 según tu carga).
       - Define los patrones de índice (por ejemplo, conservar los registros durante 7-30 días).
     - **Networking**: Expone Kibana a través de una ruta (por ejemplo, `kibana.TU-DOMINIO-PCF.com`).
   - Haz clic en **Apply Changes** para desplegar. Esto puede tomar 30-60 minutos.

3. **Verificar el Despliegue**:
   - Ejecuta `cf tiles` o verifica en Ops Manager el éxito.
   - Conéctate por SSH a una VM de Log Search (usando BOSH CLI: `bosh ssh log-search/0`) y confirma que Elasticsearch esté ejecutándose (`curl localhost:9200`).

### Paso 2: Acceder a Kibana
Una vez desplegado:

1. **A través de PCF Apps Manager (GUI)**:
   - Inicia sesión en Apps Manager (por ejemplo, `https://apps.TU-DOMINIO-PCF.com`).
   - Busca la instancia de servicio "Log Search" (se crea una automáticamente).
   - Haz clic en la instancia de servicio > pestaña **Logs**. Esto abre una vista integrada de Kibana para búsquedas rápidas de registros.

2. **Acceso Directo a Kibana**:
   - Navega a la URL de Kibana configurada en el tile (por ejemplo, `https://kibana.TU-DOMINIO-PCF.com`).
   - Inicia sesión con las credenciales de administrador que configuraste.
   - Si usas un dominio personalizado, asegúrate de que el DNS esté apuntado correctamente y las rutas estén registradas (verifica con `cf routes`).

3. **Acceso por CLI (Opcional)**:
   - Usa `cf logs NOMBRE-APP` para registros básicos, pero para consultas avanzadas, usa la UI de Kibana o la API.
   - Vincula Log Search a tus aplicaciones: `cf create-service log-search standard my-log-search` luego `cf bind-service NOMBRE-APP my-log-search`.

### Paso 3: Usar Kibana para Registros de PCF
Kibana proporciona una interfaz web para consultar, filtrar y visualizar registros de los componentes de PCF (por ejemplo, registros de aplicaciones, celdas Diego, Gorouter, etc.).

1. **Navegación Básica**:
   - **Pestaña Discover**: Busca registros usando la sintaxis de consulta Lucene.
     - Ejemplo: Buscar errores en una aplicación específica: `source_id:APP:nombre-de-tu-app AND json.message:ERROR`.
     - Campos disponibles: `timestamp`, `source_id` (por ejemplo, `APP:tu-app`, `RTR:router`), `message`, `deployment`, etc.
   - **Pestaña Visualize**: Crea paneles para gráficos (por ejemplo, volumen de registros a lo largo del tiempo, tasas de error).
     - Visualización de ejemplo: Gráfico de barras de registros por source_id.
   - **Pestaña Dashboard**: Guarda y comparte paneles preconstruidos (Log Search incluye unos predeterminados para registros de PCF).

2. **Consultas y Consejos Comunes**:
   - **Filtrar por App**: `source_id:APP:nombre-de-tu-app` (reemplaza con el GUID o nombre real de la aplicación).
   - **Filtrar por Tiempo**: Usa el selector de tiempo (por ejemplo, últimas 24 horas).
   - **Registros del Sistema**: `source_id:DEA` (para celdas Diego) o `source_id:LOGGREGATOR`.
   - **Exportar Registros**: Descarga como CSV/JSON desde Discover.
   - **Avanzado**: Usa Dev Tools de Kibana (consola) para consultar Elasticsearch directamente, por ejemplo:
     ```
     GET /logstash-*/_search
     {
       "query": { "match": { "message": "error" } },
       "sort": [ { "timestamp": { "order": "desc" } } ]
     }
     ```
   - **Retención e Indexación**: Los registros se indexan por día (por ejemplo, `logstash-YYYY.MM.DD`). Configura la rotación en el tile para gestionar el almacenamiento.

3. **Solución de Problemas de Registros**:
   - **¿No Aparecen Registros?** Verifica las reglas de reenvío en Loggregator (Ops Manager > Elastic Runtime > Loggregator). Asegúrate de que las aplicaciones emitan registros (por ejemplo, mediante `console.log` en Node.js).
   - **¿Problemas de Rendimiento?** Escala las instancias de Elasticsearch o ajusta los límites de tasa de registros.
   - **Seguridad**: Habilita la integración de UAA en Log Search para el inicio de sesión SSO en Kibana.
   - **Errores**: Revisa los registros de PCF con `cf logs log-search` o los registros de tareas (errands) de Ops Manager.

### Recursos Adicionales
- **Documentación Oficial**: Documentación de VMware Tanzu sobre [Log Search](https://docs.vmware.com/en/VMware-Tanzu-Application-Service/10.0/tas/GUID-log-search-index.html) (busca tu versión).
- **Herramientas CLI**: Instala `uaac` para autenticación UAA si es necesario, o usa `cf curl` para acceso a la API.
- **Alternativas**: Para necesidades más simples, usa **Log Cache** integrado en PCF (cf CLI: `cf tail NOMBRE-APP`) o integra con herramientas externas como Splunk a través de reenvío syslog.
- **Actualizaciones**: Si estás en una versión heredada de PCF, migra al tile ELK o contacta al soporte de Broadcom.

Si proporcionas más detalles (por ejemplo, tu versión de PCF, mensajes de error o caso de uso específico), ¡puedo afinar esto aún más!