---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast:free
title: Guía de Configuración e Instalación de la Pila ELG
translated: true
type: note
---

### Descripción General de la Pila ELG (Elasticsearch, Logstash, Grafana)

La pila ELG (a menudo una variante de la pila ELK donde Kibana es reemplazado por Grafana para la visualización) es un conjunto de herramientas de código abierto potente para recopilar, procesar, almacenar y visualizar grandes volúmenes de datos, particularmente registros (logs) de aplicaciones, servidores e infraestructura. Permite el monitoreo, análisis y alertas en tiempo real. Componentes clave:

- **Elasticsearch**: Un motor de búsqueda y análisis distribuido para almacenar, buscar y analizar datos a escala.
- **Logstash**: Un pipeline de procesamiento de datos que ingiere datos de múltiples fuentes, los transforma y los envía a Elasticsearch.
- **Grafana**: Una herramienta de panel de control (dashboard) de visualización y monitoreo que se conecta a fuentes de datos como Elasticsearch para crear gráficos, visualizaciones y alertas.

Esta guía asume conocimientos básicos de Linux (por ejemplo, Ubuntu/Debian; adaptar para otros sistemas operativos). Utilice la documentación oficial para obtener detalles completos. Instalación mediante descargas desde elastic.co y grafana.com.

#### 1. Instalar Elasticsearch
Elasticsearch maneja el almacenamiento e indexación de datos.

- **Prerrequisitos**: Java 11+ (instalar con `sudo apt update && sudo apt install openjdk-11-jdk`).
- Descargar e instalar:
  ```
  wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
  echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-7.x.list
  sudo apt update && sudo apt install elasticsearch
  ```
- Iniciar y habilitar: `sudo systemctl start elasticsearch && sudo systemctl enable elasticsearch`.
- Verificar: Visite `http://localhost:9200` – debería devolver JSON con información del clúster.
- Configuración básica (editar `/etc/elasticsearch/elasticsearch.yml`): Establecer `network.host: 0.0.0.0` para acceso remoto (asegurar con TLS/firewall en producción).

#### 2. Instalar Logstash
Logstash obtiene datos de fuentes (por ejemplo, archivos, syslogs) y los envía a Elasticsearch.

- Instalar junto a Elasticsearch:
  ```
  sudo apt install logstash
  ```
- Iniciar y habilitar: `sudo systemctl start logstash && sudo systemctl enable logstash`.
- Configuración de ejemplo para ingerir logs (`/etc/logstash/conf.d/simple.conf`):
  ```
  input {
    file {
      path => "/var/log/syslog"
      start_position => "beginning"
    }
  }
  filter {
    grok {
      match => { "message" => "%{SYSLOGTIMESTAMP:timestamp} %{SYSLOGHOST:host} %{WORD:program}: %{GREEDYDATA:message}" }
    }
  }
  output {
    elasticsearch {
      hosts => ["localhost:9200"]
    }
    stdout { codec => rubydebug }
  }
  ```
- Probar el pipeline: `sudo /usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/simple.conf` (ejecutar en segundo plano para uso persistente).
- Recargar configuración: `sudo systemctl restart logstash`.

#### 3. Instalar Grafana
Grafana proporciona paneles de control para visualizar datos de Elasticsearch.

- Instalar:
  ```
  wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
  echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee /etc/apt/sources.list.d/grafana.list
  sudo apt update && sudo apt install grafana
  ```
- Iniciar y habilitar: `sudo systemctl start grafana-server && sudo systemctl enable grafana-server`.
- Acceder: Visite `http://localhost:3000` (usuario y contraseña por defecto: admin/admin; cambiar la contraseña).
- Conectar a Elasticsearch:
  1. Ir a Configuration > Data Sources > Add data source.
  2. Seleccionar "Elasticsearch", establecer la URL en `http://localhost:9200`, el nombre del índice (por ejemplo, `logstash-*`) y el campo de tiempo (por ejemplo, `@timestamp`).
  3. Guardar y probar la conexión.

#### Configuración del Pipeline ELG Completo
1. **Flujo de Datos**: Logstash recopila/analiza logs → los envía a Elasticsearch → Grafana consulta y visualiza.
2. **Flujo de Trabajo de Ejemplo**:
   - Enviar datos de ejemplo: Utilice plugins de entrada de Logstash o herramientas como `stdout` para pruebas.
   - Indexar en Elasticsearch: Los logs aparecen como documentos (por ejemplo, mediante la API de Kibana o curl directo: `curl -X GET "localhost:9200/_search?pretty"`).
   - Panel de control en Grafana: Crear paneles (por ejemplo, un gráfico de líneas para errores de log a lo largo del tiempo usando consultas Lucene como `program:kern*`).
3. **Conceptos Básicos de Seguridad**: Utilice HTTPS/TLS, autenticación (por ejemplo, X-Pack para Elasticsearch) y firewalls. Para producción, escale con múltiples nodos/clúster.
4. **Monitoreo**: Habilite el monitoreo JVM en Elasticsearch; Grafana tiene alertas integradas para umbrales.

#### Problemas Comunes y Consejos
- **Falta de Memoria (Out of Memory)**: Aumente el heap de la JVM en `/etc/elasticsearch/jvm.options` (por ejemplo, `-Xms1g -Xmx1g`).
- **Conflictos de Puertos**: Puertos por defecto: Elasticsearch 9200/9300, Logstash 5044, Grafana 3000 – verificar con `netstat -tulpn`.
- **Rendimiento**: Utilice beats (por ejemplo, Filebeat) en lugar de Logstash para envío de datos más ligero.
- **Recursos de Aprendizaje**: Guías oficiales de Elastic (elastic.co/guide), documentación de Grafana (grafana.com/docs). Practique con Docker: Busque "ELG stack Docker Compose" en GitHub.

Para configuraciones personalizadas o solución de problemas de errores específicos, proporcione más detalles. Este es un punto de partida; ELG es excelente para análisis de logs, datos de IoT y monitoreo de aplicaciones.