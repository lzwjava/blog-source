---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Guía de Verificación de Registros de Kibana
translated: true
type: note
---

Kibana es una herramienta de código abierto para visualización y exploración de datos desarrollada por Elastic. Es un componente clave del **ELK Stack** (Elasticsearch, Logstash, Kibana), ampliamente utilizado para el registro centralizado, monitoreo y análisis. Kibana proporciona una interfaz web para interactuar con los datos almacenados en Elasticsearch, permitiéndote buscar, visualizar y analizar registros en tiempo real. Es especialmente potente para revisar registros de aplicaciones, servidores o servicios en la nube.

Esta guía se centra en usar Kibana para inspeccionar y consultar registros. Cubriremos la configuración, el uso básico, los flujos de trabajo de revisión de registros y consejos avanzados. Asume que trabajas con una configuración ELK básica; si eres nuevo en ELK, comienza instalando primero Elasticsearch y Logstash (Kibana requiere Elasticsearch para funcionar).

## 1. Prerrequisitos
Antes de usar Kibana:
- **Elasticsearch**: Versión 8.x o posterior (Kibana está estrechamente acoplado con las versiones de Elasticsearch). Descárgalo desde [elastic.co](https://www.elastic.co/downloads/elasticsearch).
- **Java**: Elasticsearch requiere JDK 11 o posterior.
- **Requisitos del Sistema**: Al menos 4GB de RAM para desarrollo; más para producción.
- **Fuente de Datos**: Registros ingeridos vía Logstash, Filebeat, o directamente en Elasticsearch (por ejemplo, formato JSON con marcas de tiempo).
- **Acceso de Red**: Kibana se ejecuta en el puerto 5601 por defecto; asegúrate de que sea accesible.

Si aún no tienes registros, usa herramientas como Filebeat para enviar registros de ejemplo (por ejemplo, registros del sistema) a Elasticsearch.

## 2. Instalando Kibana
La instalación de Kibana es sencilla e independiente de la plataforma. Descarga la última versión desde [elastic.co/downloads/kibana](https://www.elastic.co/downloads/kibana) (que coincida con tu versión de Elasticsearch).

### En Linux (Debian/Ubuntu):
1. Añade el repositorio de Elastic:
   ```
   wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
   sudo apt-get install apt-transport-https
   echo "deb https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-8.x.list
   sudo apt-get update && sudo apt-get install kibana
   ```
2. Inicia Kibana:
   ```
   sudo systemctl start kibana
   sudo systemctl enable kibana  # Para inicio automático al arrancar
   ```

### En Windows:
1. Descarga el archivo ZIP y extráelo en `C:\kibana-8.x.x-windows-x86_64`.
2. Abre el Símbolo del Sistema como Administrador y navega a la carpeta extraída.
3. Ejecuta: `bin\kibana.bat`

### En macOS:
1. Usa Homebrew: `brew tap elastic/tap && brew install elastic/tap/kibana-full`.
2. O descarga el TAR.GZ, extráelo y ejecuta `./bin/kibana`.

Para Docker: Usa la imagen oficial:
```
docker run --name kibana -p 5601:5601 -e ELASTICSEARCH_HOSTS=http://elasticsearch:9200 docker.elastic.co/kibana/kibana:8.10.0
```

## 3. Configuración Básica
Edita el archivo de configuración `kibana.yml` (ubicado en `/etc/kibana/` en Linux, o en la carpeta `config/` en otros).

Ajustes clave para la revisión de registros:
```yaml
# Conectar a Elasticsearch (por defecto es localhost:9200)
elasticsearch.hosts: ["http://localhost:9200"]

# Configuración del servidor
server.port: 5601
server.host: "0.0.0.0"  # Enlazar a todas las interfaces para acceso remoto

# Seguridad (habilitar para producción)
# elasticsearch.username: "elastic"
# elasticsearch.password: "tu_contraseña"

# Registros
logging.verbose: true  # Para depurar Kibana mismo

# Patrón de índice (opcional por defecto)
defaultIndex: "logs-*"
```
- Reinicia Kibana después de los cambios: `sudo systemctl restart kibana`.
- Si usas funciones de seguridad (X-Pack), genera certificados o usa autenticación básica.

## 4. Iniciando y Accediendo a Kibana
- Inicia Elasticsearch primero (por ejemplo, `sudo systemctl start elasticsearch`).
- Inicia Kibana como se indicó arriba.
- Abre un navegador web y ve a `http://localhost:5601` (o la IP de tu servidor:5601).
- En el primer inicio de sesión, verás el asistente de configuración. Crea un usuario administrador si se solicita (por defecto: elastic/changeme).

La interfaz incluye aplicaciones como **Discover** (para registros), **Visualize**, **Dashboard**, **Dev Tools** y **Management**.

## 5. Preparando Datos: Patrones de Índice
Los registros en Elasticsearch se almacenan en **índices** (por ejemplo, `logs-2023-10-01`). Para consultarlos en Kibana, crea un **patrón de índice**.

1. Ve a **Stack Management** > **Index Patterns** (barra lateral izquierda, menú de hamburguesa > Management).
2. Haz clic en **Create index pattern**.
3. Introduce un patrón como `logs-*` (coincide con todos los índices de registro) o `filebeat-*` (para registros de Filebeat).
4. Selecciona el **Campo de tiempo** (por ejemplo, `@timestamp` para las marcas de tiempo de registro—crucial para consultas basadas en tiempo).
5. Haz clic en **Create index pattern**.
   - Esto mapea campos como `message` (texto del registro), `host.name`, `level` (error/warn/info), etc.

Actualiza los campos si tus registros cambian. Usa **Discover** para previsualizar.

## 6. Usando Discover para Revisar Registros
La aplicación **Discover** es tu herramienta principal para inspeccionar registros. Es como un visor de registros buscable.

### Navegación Básica:
1. Haz clic en **Discover** en la barra lateral izquierda.
2. Selecciona tu patrón de índice del menú desplegable (parte superior izquierda).
3. Establece el rango de tiempo (parte superior derecha): Usa opciones rápidas como "Last 15 minutes" o personalizado (por ejemplo, Last 7 days). Esto filtra los registros por `@timestamp`.

### Viendo Registros:
- **Recuento de Aciertos**: Muestra el total de registros coincidentes (por ejemplo, 1,234 hits).
- **Tabla de Documentos**: Muestra las entradas de registro en bruto como JSON o texto formateado.
  - Columnas: Por defecto son `@timestamp` y `_source` (registro completo). Arrastra campos desde la barra lateral izquierda (por ejemplo, `message`, `host.name`) para añadir columnas.
  - Expande una fila (haz clic en la flecha) para ver el documento JSON completo.
- **Histograma**: El gráfico superior muestra el volumen de registros a lo largo del tiempo. Haz zoom arrastrando.

### Buscando Registros:
Usa la barra de búsqueda (parte superior) para las consultas. Kibana usa **KQL (Kibana Query Language)** por defecto—sencillo e intuitivo.

- **Búsqueda Básica**:
  - Buscar por palabra clave: `error` (encuentra registros que contengan "error").
  - Específica de campo: `host.name:webserver AND level:error` (registros de "webserver" con nivel de error).
  - Frases: `"user login failed"` (coincidencia exacta).

- **Filtros**:
  - Añade desde la barra lateral: Haz clic en un valor de campo (por ejemplo, `level: ERROR`) > Add filter (lo fija a la consulta).
  - Lógica booleana: `+error -info` (debe tener "error", excluir "info").
  - Rango: Para números/tiempos, por ejemplo, `bytes:>1000` (campo > 1000).

- **Consultas Avanzadas**:
  - Cambia a **sintaxis de consulta Lucene** (a través del menú desplegable de lenguaje de consulta) para necesidades complejas: `message:(error OR warn) AND host.name:prod*`.
  - Usa **Query DSL** en Dev Tools para consultas nativas de Elasticsearch (por ejemplo, POST /logs-*/_search con cuerpo JSON).

### Guardando Búsquedas:
- Haz clic en **Save** (parte superior derecha) para almacenar una búsqueda para reutilizar.
- Comparte mediante **Share** > CSV/URL para exportaciones.

Flujo de Trabajo de Ejemplo: Revisando Registros de Aplicación
1. Ingiere registros (por ejemplo, vía Logstash: archivo de entrada > filtro grok/parse > salida Elasticsearch).
2. En Discover: Rango de tiempo "Last 24 hours".
3. Búsqueda: `app.name:myapp AND level:ERROR`.
4. Añade filtros: `host.name` = servidor específico.
5. Inspecciona: Mira `message` para trazas de pila, correlaciona con `@timestamp`.

## 7. Visualizando Registros
Mientras Discover es para la revisión en bruto, Visualize es para patrones.

### Crear Visualizaciones:
1. Ve a **Visualize Library** > **Create new visualization**.
2. Elige el tipo:
   - **Lens** (fácil): Arrastra campos a buckets (por ejemplo, Eje X: `@timestamp`, Eje Y: recuento de errores).
   - **Gráfico de Áreas/Líneas**: Para el volumen de registros a lo largo del tiempo (Métricas: Count, Buckets: Date Histogram on `@timestamp`).
   - **Tabla de Datos**: Resumen tabular de registros.
   - **Gráfico Circular**: Desglose por `level` (error 40%, info 60%).
3. Aplica filtros/búsquedas desde Discover.
4. Guarda y añade a un **Dashboard** (Analytics > Dashboard > Create new > Add visualization).

Ejemplo: Dashboard de Tasa de Error
- Visualiza: Gráfico de líneas de registros de error por hora.
- Filtro: Rango de tiempo global.
- Incrusta en el Dashboard para monitoreo.

## 8. Características Avanzadas para Análisis de Registros
- **Alertas y Monitoreo**:
  - Usa **Alerts** (Stack Management > Rules) para notificar sobre patrones de registro (por ejemplo, enviar correo si "critical" aparece >5 veces/hora).
  - **Uptime Monitoring** o **APM** para registros de aplicaciones.

- **Machine Learning**:
  - Habilita trabajos de ML (Stack Management > Machine Learning) para detectar anomalías en los volúmenes de registro.

- **Dev Tools**:
  - Consola para consultas crudas de Elasticsearch: por ejemplo,
    ```
    GET logs-*/_search
    {
      "query": { "match": { "message": "error" } },
      "sort": [ { "@timestamp": "desc" } ]
    }
    ```
  - Prueba patrones de índice o ingiere datos.

- **Roles y Seguridad**:
  - En producción, usa **Spaces** para aislar vistas de registro (por ejemplo, dev/prod).
  - Acceso basado en roles: Restringe usuarios a índices específicos.

- **Exportar/Importar**:
  - Exporta búsquedas/dashboards como NDJSON mediante **Stack Management > Saved Objects**.
  - Importa registros mediante **Console** o Beats.

- **Consejos de Rendimiento**:
  - Usa **Field Analyzer** (Index Patterns > field) para mapeos personalizados.
  - Pagina resultados grandes: Ajusta aciertos por página (configuración de Discover).
  - Para big data, fragmenta índices y usa ILM (Index Lifecycle Management).

## 9. Integrando con Fuentes de Registro
- **Filebeat/Logstash**: Envía registros a Elasticsearch.
  - Ejemplo de configuración de Filebeat (`filebeat.yml`):
    ```yaml
    filebeat.inputs:
    - type: log
      paths: [/var/log/*.log]
      fields:
        app: myapp
    output.elasticsearch:
      hosts: ["localhost:9200"]
      index: "logs-%{+yyyy.MM.dd}"
    ```
  - Ejecuta: `./filebeat -e`.
- **Registros en la Nube**: Integra con AWS S3, Azure o Elastic Cloud para configuraciones gestionadas.

## 10. Solución de Problemas Comunes
- **Sin Datos en Discover**:
  - Comprueba la conexión a Elasticsearch: `curl localhost:9200/_cat/indices`.
  - Verifica que el patrón de índice coincida con los índices (por ejemplo, sin error de `*`).
  - Asegúrate de que `@timestamp` esté mapeado como fecha.

- **Kibana No Arranca**:
  - Registros: Revisa `/var/log/kibana/kibana.log` o la salida de la consola.
  - Común: Puerto 5601 en uso, o Elasticsearch no ejecutándose/seguro.

- **Consultas Lentas**:
  - Optimiza: Usa campos keyword para filtros, evita comodines en textos grandes.
  - Aumenta el heap: Edita `jvm.options` para Elasticsearch (por ejemplo, `-Xms4g -Xmx4g`).

- **Errores en los Registros**:
  - 403/401: Problemas de autenticación—habilita la seguridad en `elasticsearch.yml`.
  - Incompatibilidad de Versión: Asegúrate de que la versión de Kibana == versión de Elasticsearch.

- **Recursos**:
  - Documentación Oficial: [elastic.co/guide/en/kibana/current](https://www.elastic.co/guide/en/kibana/current/index.html).
  - Foros: Elastic Discuss o Stack Overflow.
  - Datos de Ejemplo: Carga mediante Kibana (Stack Management > Kibana > Sample Data).

Esta guía debería ayudarte a comenzar con Kibana para la revisión de registros. Comienza poco a poco: configura un stack ELK local, ingiere registros de ejemplo y experimenta en Discover. Para producción, considera Elastic Cloud por facilidad. Si tienes una configuración específica (por ejemplo, Docker, AWS), ¡proporciona más detalles para un consejo personalizado!