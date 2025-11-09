---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Descripción General de Alertas de Azure Monitor
translated: true
type: note
---

### Información general sobre las alertas en Azure

Las alertas de Azure Monitor son una característica de Azure Monitor que le notifica de forma proactiva cuando se cumplen condiciones específicas en sus recursos de Azure, ayudándole a detectar y resolver problemas antes de que afecten a los usuarios. Funcionan evaluando datos de métricas, registros o registros de actividad frente a reglas predefinidas. Cuando se activa una condición (por ejemplo, el uso de CPU supera el 80%), se activa una alerta, que puede enviar notificaciones por correo electrónico, SMS o desencadenar acciones automatizadas como ejecutar un script.

Las alertas pueden ser con estado (se resuelven automáticamente cuando el problema desaparece) o sin estado (se activan repetidamente hasta que se cierran manualmente), dependiendo de su configuración. Admiten la supervisión en uno o varios recursos y se facturan en función del número de series temporales supervisadas.

#### Tipos de alertas
Azure Monitor admite varios tipos de alertas adaptados a diferentes orígenes de datos:

| Tipo de alerta              | Descripción | Mejor para |
|-------------------------|-------------|----------|
| **Alertas de métrica**      | Evalúan métricas numéricas (por ejemplo, porcentaje de CPU, espacio en disco) a intervalos regulares. Admite umbrales estáticos o dinámicos (basados en IA). | Supervisión del rendimiento de máquinas virtuales, bases de datos o aplicaciones. |
| **Alertas de búsqueda de registros**  | Ejecutan consultas sobre datos de Log Analytics para detectar patrones en los registros. | Análisis complejo de eventos, como picos de errores en registros de aplicaciones. |
| **Alertas del registro de actividad**| Se activan con eventos administrativos u operativos (por ejemplo, creación/eliminación de recursos). | Auditoría de seguridad y cumplimiento. |
| **Alertas de detección inteligente** | Detección de anomalías impulsada por IA para aplicaciones web a través de Application Insights. | Detección automática de problemas en aplicaciones. |
| **Alertas de Prometheus**  | Consultan métricas de Prometheus en servicios administrados como AKS. | Entornos de contenedores y Kubernetes. |

Para la mayoría de los casos de uso, comience con alertas de métrica o de registros.

### Requisitos previos
- Una suscripción de Azure con recursos activos para supervisar.
- Permisos: Rol Lector en el recurso de destino, Colaborador en el grupo de recursos para la regla de alerta y Lector en cualquier grupo de acciones.
- Familiaridad con Azure Portal (portal.azure.com).

### Cómo crear y usar una regla de alerta de métrica (Paso a paso)
Las alertas de métrica son un punto de partida común. Así es como se crea una en Azure Portal. Este proceso toma aproximadamente 5-10 minutos.

1.  **Inicie sesión en Azure Portal**: Vaya a [portal.azure.com](https://portal.azure.com) e inicie sesión.

2.  **Navegue a Alertas**:
    - Desde la página de inicio, busque y seleccione **Monitor**.
    - En el menú de la izquierda, en **Información**, seleccione **Alertas**.
    - Haga clic en **+ Crear** > **Regla de alerta**.

    *Alternativa*: Desde un recurso específico (por ejemplo, una VM), seleccione **Alertas** en el menú izquierdo, luego **+ Crear** > **Regla de alerta**. Esto establece automáticamente el ámbito.

3.  **Establezca el ámbito**:
    - En el panel **Seleccionar un recurso**, elija su suscripción, el tipo de recurso (por ejemplo, Máquinas virtuales) y el recurso específico.
    - Haga clic en **Aplicar**. (Para alertas de múltiples recursos, seleccione varios recursos del mismo tipo en una región).

4.  **Configure la condición**:
    - En la pestaña **Condición**, haga clic en **Nombre de señal** y seleccione una métrica (por ejemplo, "Porcentaje de CPU" para una VM).
      - Use **Ver todas las señales** para filtrar por tipo (por ejemplo, Métricas de plataforma).
    - Vista previa de datos: Establezca un intervalo de tiempo (por ejemplo, últimas 24 horas) para ver valores históricos.
    - Establezca la **Lógica de alerta**:
      - **Umbral**: Estático (por ejemplo, > 80) o Dinámico (ajustado por IA basado en el historial).
      - **Operador**: Mayor que, Menor que, etc.
      - **Agregación**: Promedio, Suma, Mín, Máx durante el período de evaluación.
      - Para dinámico: Elija la sensibilidad (Baja/Media/Alta).
    - (Opcional) **Dividir por dimensiones**: Filtre por atributos como el nombre de la instancia para alertas granulares (por ejemplo, por VM en un conjunto).
    - **Evaluación**: Verifique cada 1-5 minutos; retroceda 5-15 minutos.
    - Haga clic en **Listo**.

5.  **Agregue acciones (Opcional pero recomendado)**:
    - En la pestaña **Acciones**, seleccione **Agregar grupos de acciones**.
    - Elija un grupo existente (para correos electrónicos/SMS) o cree uno:
      - Agregue destinatarios (por ejemplo, correo electrónico de administradores).
      - Agregue acciones como Logic Apps para automatización o webhooks para integraciones.
    - Haga clic en **Listo**.

6.  **Establezca los detalles de la regla**:
    - En la pestaña **Detalles**:
      - **Suscripción** y **Grupo de recursos**: Rellenado automáticamente; cámbielo si es necesario.
      - **Gravedad**: Sev 0 (Crítico) a Sev 4 (Detallado).
      - **Nombre de la regla de alerta**: por ejemplo, "Alerta de CPU alta - VM de Prod".
      - **Descripción**: Notas opcionales.
    - **Opciones avanzadas**:
      - Habilite la regla al crearla.
      - Resolución automática de alertas (la convierte en con estado).
    - Agregue etiquetas si es necesario para la organización.

7.  **Revise y cree**:
    - Vaya a **Revisar + crear**.
    - Valide (corrija cualquier error, como umbrales no válidos).
    - Haga clic en **Crear**. La regla se activa inmediatamente si está habilitada.

Una vez creada, la alerta se activará cuando se cumplan las condiciones, enviando notificaciones y actualizando su estado (por ejemplo, de "Activada" a "Resuelta").

#### Gestión de alertas
- **Ver alertas**: En Monitor > Alertas, vea las alertas activas/activadas. Filtre por tiempo, gravedad o recurso.
- **Editar una regla**: Vaya a Monitor > Alertas > Reglas de alertas, seleccione la regla y haga clic en **Editar**.
- **Probar**: Use la vista previa en el paso 4 para simular.
- **Escalar**: Para múltiples recursos, use Azure CLI/PowerShell o plantillas de ARM. Habilite reglas recomendadas integradas a través de la información de recursos.

### Mejores prácticas
- Comience de forma simple: Una condición por regla inicialmente.
- Use umbrales dinámicos para métricas ruidosas para reducir falsos positivos.
- Integre con grupos de acciones para la remediación automatizada (por ejemplo, escalar una VM).
- Supervise los costos: Se basan en las series supervisadas (gratuito para uso básico; consulte los precios).
- Para registros, siga pasos similares pero seleccione **Alertas de registro** en la creación y escriba una consulta KQL.

Para alertas de registro u otros tipos, el proceso es análogo: reemplace la condición por una consulta.

[Información general sobre las alertas de Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview)  
[Crear regla de alerta de métrica](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-create-metric-alert-rule)  
[Crear regla de alerta de registro](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-create-log-alert-rule)  
[Precios de Azure Monitor](https://azure.microsoft.com/en-us/pricing/details/monitor/)