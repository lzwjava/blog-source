---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Guía de Configuración de Azure Application Insights
translated: true
type: note
---

## ¿Qué es Azure Application Insights?

Azure Application Insights es un servicio de administración del rendimiento de aplicaciones (APM) en Azure Monitor que te ayuda a supervisar aplicaciones web en vivo. Proporciona herramientas para detectar problemas, diagnosticar fallos y comprender el comportamiento de los usuarios a través de datos de telemetría como solicitudes, dependencias, trazas, métricas y registros. Ahora funciona con OpenTelemetry para una compatibilidad más amplia.

## Requisitos previos
- Una suscripción activa de Azure.
- Permisos para crear recursos en Azure (por ejemplo, rol de Propietario o Colaborador).
- El código de tu aplicación (admite .NET, Java, Node.js, Python y más).

## Paso 1: Crear un recurso de Application Insights
1. Inicia sesión en [Azure Portal](https://portal.azure.com).
2. Haz clic en **Crear un recurso** en el menú superior izquierdo.
3. Busca "Application Insights" y selecciónalo de los resultados en **Supervisión y administración**.
4. Completa los detalles:
   - **Suscripción**: Elige tu suscripción de Azure.
   - **Grupo de recursos**: Selecciona uno existente o crea uno nuevo.
   - **Nombre**: Asigna un nombre único a tu recurso.
   - **Región**: Elige una región cercana a tus usuarios o a tu aplicación.
   - **Área de trabajo**: Opcionalmente, vincula a un área de trabajo de Log Analytics existente; de lo contrario, se crea una nueva automáticamente.
5. Revisa y haz clic en **Crear**. La implementación tarda unos minutos.
6. Una vez creado, ve a la página **Información general** de tu recurso y copia la **Cadena de conexión** (pasa el cursor sobre ella y haz clic en el icono de copiar). Esto identifica a dónde tu aplicación envía los datos de telemetría.

**Consejo**: Usa recursos separados para los entornos de desarrollo, prueba y producción para evitar mezclar datos.

## Paso 2: Instrumentar tu aplicación
Agrega soporte para OpenTelemetry para recopilar telemetría automáticamente (solicitudes, excepciones, métricas, etc.). Establece la cadena de conexión a través de una variable de entorno llamada `APPLICATIONINSIGHTS_CONNECTION_STRING` (recomendado para producción).

### Para .NET (ASP.NET Core)
1. Instala el paquete NuGet:
   ```
   dotnet add package Azure.Monitor.OpenTelemetry.AspNetCore
   ```
2. En `Program.cs`:
   ```csharp
   using Azure.Monitor.OpenTelemetry.AspNetCore;

   var builder = WebApplication.CreateBuilder(args);
   builder.Services.AddOpenTelemetry().UseAzureMonitor();
   var app = builder.Build();
   app.Run();
   ```
3. Establece la variable de entorno con tu cadena de conexión y ejecuta la aplicación.

### Para Java
1. Descarga el JAR de Azure Monitor OpenTelemetry Distro (por ejemplo, `applicationinsights-agent-3.x.x.jar`).
2. Crea un archivo de configuración `applicationinsights.json` en el mismo directorio:
   ```json
   {
     "connectionString": "Tu cadena de conexión aquí"
   }
   ```
3. Ejecuta tu aplicación con el agente: `java -javaagent:applicationinsights-agent-3.x.x.jar -jar tu-aplicacion.jar`.

### Para Node.js
1. Instala el paquete:
   ```
   npm install @azure/monitor-opentelemetry
   ```
2. Configura en el punto de entrada de tu aplicación:
   ```javascript
   const { AzureMonitorOpenTelemetry } = require('@azure/monitor-opentelemetry');
   const provider = new AzureMonitorOpenTelemetry({
     connectionString: process.env.APPLICATIONINSIGHTS_CONNECTION_STRING
   });
   provider.start();
   ```
3. Establece la variable de entorno e inicia tu aplicación.

### Para Python
1. Instala el paquete:
   ```
   pip install azure-monitor-opentelemetry
   ```
2. En tu aplicación:
   ```python
   from azure.monitor.opentelemetry import configure_azure_monitor
   configure_azure_monitor(connection_string="Tu cadena de conexión aquí")
   ```
3. Ejecuta la aplicación.

Para otros lenguajes o instrumentación automática (por ejemplo, para Azure App Service), consulta la documentación oficial. Prueba primero localmente.

## Paso 3: Ver y analizar los datos
1. Ejecuta tu aplicación instrumentada y genera algo de actividad (por ejemplo, envía solicitudes).
2. En Azure Portal, abre tu recurso de Application Insights.
3. Revisa la página **Información general**: Ve métricas en vivo, recuentos de solicitudes y tiempos de respuesta (los datos aparecen en ~1-2 minutos).
4. Explora las características:
   - **Métricas en vivo**: Flujo en tiempo real para aplicaciones en producción.
   - **Errores**: Profundiza en excepciones y trazas.
   - **Rendimiento**: Analiza dependencias y solicitudes lentas.
   - **Uso**: Rastrea sesiones de usuario y eventos personalizados.
   - **Alertas**: Configura notificaciones para problemas (por ejemplo, tasas de error altas).
5. Consulta los datos usando el lenguaje de consulta Kusto (KQL) en **Registros** para análisis personalizados.

## Mejores prácticas
- Comienza con telemetría básica; agrega eventos/métricas personalizados según sea necesario.
- Supervisa los costos a través de la página **Uso y costos estimados** (se factura a través de Log Analytics).
- Para la supervisión del navegador, agrega el fragmento del SDK de JavaScript a tus páginas web.

[Crear y configurar recursos de Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/create-workspace-resource)  
[Habilitar OpenTelemetry en Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable)  
[Información general de Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)