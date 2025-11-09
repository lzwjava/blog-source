---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Introducción a Google Cloud Run
translated: true
type: note
---

Cloud Run es una plataforma de computación serverless y completamente administrada en GCP que te permite ejecutar contenedores sin estado directamente en la infraestructura escalable de Google. Está diseñada para desarrolladores que quieren implementar aplicaciones sin preocuparse por los servidores subyacentes, el aprovisionamiento o el escalado. Ya sea que estés construyendo aplicaciones web, APIs, microservicios o cargas de trabajo dirigidas por eventos, Cloud Run maneja la infraestructura para que tú puedas concentrarte en el código.

### Características Clave
- **Ejecución Serverless**: Implementa código en contenedores (que admite cualquier lenguaje o runtime) que escala automáticamente de cero a miles de instancias según las solicitudes entrantes o el tráfico.
- **Precio de Pago por Uso**: Se factura solo por los recursos que consumes—por solicitud o por duración de instancia—haciéndolo rentable para cargas de trabajo variables.
- **Integraciones Incorporadas**: Funciona perfectamente con otros servicios de GCP como Cloud SQL para bases de datos, Cloud Storage para archivos, Pub/Sub para mensajería y más. También admite VPC para redes privadas.
- **Opciones de Implementación**:
  - Empuja una imagen de contenedor preconstruida desde Artifact Registry o Docker Hub.
  - Implementa directamente desde el código fuente usando Cloud Build (admite lenguajes como Node.js, Python, Java, Go, .NET y Ruby).
  - Usa Cloud Run Functions para implementaciones más simples al estilo función-como-servicio.
- **Seguridad y Redes**: Los servicios pueden ser públicos o privados (que requieren autenticación), con soporte para endpoints HTTPS y dominios personalizados.
- **Modos Adicionales**: Más allá de los servicios dirigidos por solicitudes, ofrece Jobs para tareas por lotes (por ejemplo, scripts programados o procesamiento de datos) y Worker Pools para cargas de trabajo de larga duración que no son HTTP.

Para comenzar, puedes implementar a través de la Consola de GCP, la CLI de gcloud o pipelines de CI/CD. Por ejemplo, construye e implementa un simple contenedor "Hola Mundo" en minutos.

### La Consola de Administración de Cloud Run
La sección de Cloud Run en la Consola de GCP proporciona un panel intuitivo para gestionar tus implementaciones. Aquí hay un desglose basado en la vista de Servicios que compartiste:

- **Resumen**: La página principal "Cloud Run > Servicios" enumera todos tus servicios implementados en un formato de tabla. Comienza con un banner de recomendación útil como "Ejecuta tu app en una plataforma completamente administrada" para animar a comenzar rápidamente si eres nuevo.

- **Columnas de la Tabla** (como se muestra en tu fragmento):
  - **Nombre**: El identificador único para cada servicio (por ejemplo, "mi-api").
  - **Tipo de Implementación**: Indica cómo fue implementado—por ejemplo, "Contenedor" para imágenes o "Código Fuente" para implementaciones basadas en código.
  - **Solicitudes/seg**: Métrica en tiempo real de solicitudes por segundo para monitorear la carga de tráfico.
  - **Región**: La región de GCP donde se ejecuta el servicio (por ejemplo, us-central1), lo que afecta la latencia y el cumplimiento.
  - **Autenticación**: Muestra si el servicio es público (permite no autenticados) o requiere autenticación de IAM.
  - **Ingreso**: Controla el enrutamiento del tráfico—por ejemplo, "Todo" para interno/externo, o restringido solo a interno.
  - **Última Implementación**: Marca de tiempo de la actualización más reciente.
  - **Implementado Por**: El usuario o cuenta de servicio que realizó la implementación.

- **Filtros y Acciones**: Encima de la tabla, puedes filtrar por cualquiera de estas columnas para acotar tu lista. Usa el botón "Crear Servicio" para implementar nuevos servicios, o haz clic en el nombre de un servicio para editar configuraciones como límites de CPU/memoria, variables de entorno, configuraciones de escalado o revisiones para división de tráfico.

Esta consola facilita el monitoreo del rendimiento, la visualización de registros y la iteración en las implementaciones sin salir del navegador. Para una exploración práctica, navega a [console.cloud.google.com/run](https://console.cloud.google.com/run) después de habilitar la API.

[¿Qué es Cloud Run?](https://cloud.google.com/run/docs/overview/what-is-cloud-run)  
[Documentación de Cloud Run](https://cloud.google.com/run/docs)