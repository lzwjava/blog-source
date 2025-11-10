---
audio: false
generated: true
lang: es
layout: post
title: Guía para Solucionar Errores de la API de Avaloq
translated: true
type: note
---

## Guía Completa de Errores de API de Avaloq

### Errores Comunes a Nivel de Sistema

**1. Errores de Ejecución del Agente Avaloq**
Error en el sistema Avaloq o en Oracle al ejecutar el código del Agente Avaloq. Estos errores pueden ocurrir si el trabajo que se ejecuta en el sistema Avaloq termina con errores.

**Solución de Problemas:**
- Verificar la conectividad de la base de datos Oracle
- Verificar la configuración del Agente Avaloq
- Revisar los registros del sistema en busca de problemas relacionados con la base de datos
- Asegurar los permisos adecuados para el usuario ejecutor

**2. Errores de Cancelación de Trabajos**
La siguiente línea en el registro significa que el trabajo ha sido cancelado debido a un error interno en el sistema Avaloq. El estado final del trabajo es válido para el Agente Avaloq: AAAA-MM-DD hh:mm:ss Trabajo 642 Ejecutar: El trabajo se completó con fallos.

**Solución de Problemas:**
- Revisar los registros del trabajo para conocer las razones específicas del fallo
- Verificar la disponibilidad de recursos del sistema
- Verificar los parámetros y dependencias del trabajo
- Monitorear el rendimiento del sistema durante la ejecución

### Errores Estándar de API HTTP en Contexto Bancario

**1. 400 Solicitud Incorrecta**
Causas comunes en entornos Avaloq:
- Números de cuenta o ID de cliente no válidos
- Montos de transacción mal formados
- Campos obligatorios faltantes en órdenes de trading
- Formatos o rangos de fecha no válidos

**Solución de Problemas:**
- Examinar la URL para asegurarse de que se envían parámetros de datos válidos con sus solicitudes y que se utilizan los encabezados correctos
- Validar todos los parámetros de entrada contra los requisitos del esquema de Avaloq
- Verificar códigos de moneda y formato
- Confirmar el estado y los permisos de la cuenta

**2. 401 No Autorizado**
Causas específicas del sector bancario:
- Credenciales de API no válidas
- Tokens de autenticación caducados
- Permisos de usuario insuficientes para operaciones específicas
- Restricciones en la relación con el cliente

**Solución de Problemas:**
- Verificar la validez de la clave y secreto de la API
- Comprobar los tiempos de expiración del token
- Confirmar que el usuario tiene los permisos bancarios apropiados
- Revisar los mapeos de relación asesor-cliente

**3. 403 Prohibido**
Contexto de gestión de patrimonios:
- Acceso denegado a cuentas de clientes específicas
- Restricciones regulatorias en las operaciones
- Violaciones de las normas de cumplimiento
- Limitaciones basadas en la jurisdicción

**Solución de Problemas:**
- Revisar los derechos de acceso y roles del usuario
- Verificar las reglas y restricciones de cumplimiento
- Confirmar los permisos regulatorios
- Verificar los permisos para transacciones transfronterizas

**4. 404 No Encontrado**
Escenarios específicos del sector bancario:
- Números de cuenta inexistentes
- ID de cartera no válidos
- Referencias de transacción faltantes
- Registros de clientes eliminados o archivados

**Solución de Problemas:**
- Verificar el endpoint y asegurarse de que esté escrito correctamente
- Verificar la existencia y el estado de la cuenta
- Buscar cuentas archivadas o inactivas
- Confirmar la construcción correcta de la URL

**5. 500 Error Interno del Servidor**
Problemas a nivel del sistema:
- Problemas de conectividad de la base de datos
- Fallos del sistema bancario central
- Interrupciones del servicio de integración
- Problemas de memoria o rendimiento

**Solución de Problemas:**
- Consultar los paneles de estado del sistema
- Revisar los grupos de conexión a la base de datos
- Monitorear la utilización de recursos del sistema
- Verificar la disponibilidad de servicios dependientes

### Categorías de Error Específicas de Avaloq

**1. Errores de Unidad de Negocio**
Los trabajos RA Avaloq que se refieren a una Unidad de Negocio que no existe en el sistema Avaloq pueden ejecutarse

**Problemas Comunes:**
- Referencias a unidades de negocio no válidas
- Unidades de negocio inactivas o eliminadas
- Mapeo incorrecto de la jerarquía organizativa

**2. Errores de Integración**
Basado en las capacidades de integración de Avaloq:
- Discrepancias de versión de la API
- Fallos de validación de esquema
- Incompatibilidades de formato de mensaje
- Problemas de tiempo de espera con sistemas externos

**3. Errores de Cumplimiento y Regulatorios**
- Fallos en comprobaciones previas a la operación
- Errores de validación AML/KYC
- Problemas de reporte regulatorio
- Restricciones en transacciones transfronterizas

### Mejores Prácticas para el Manejo de Errores

**1. Registro y Monitoreo**
- Implementar un registro integral de todas las llamadas a la API
- Configurar alertas para patrones de error críticos
- Monitorear los tiempos de respuesta de la API y las tasas de éxito
- Rastrear patrones de error específicos del negocio

**2. Estructura de la Respuesta de Error**
Las respuestas de error típicas de Avaloq deben incluir:
- Código y categoría del error
- Mensaje de error legible para humanos
- Marca de tiempo e ID de solicitud
- Pasos de remediación sugeridos

**3. Lógica de Reintento**
- Implementar retroceso exponencial para errores transitorios
- Evitar reintentos en fallos de autenticación
- Establecer límites máximos de reintento
- Utilizar patrones de cortacircuitos para fallos del sistema

**4. Pruebas y Validación**
Avaloq ha sentado una buena base para ayudar a las empresas a facilitar el camino de prueba e integración de nuevas soluciones gestionando las complejidades en varias fases utilizando la solución sandbox de Avaloq impulsada por AWS.

**Enfoque de Pruebas Recomendado:**
- Utilizar el entorno sandbox de Avaloq para pruebas
- Probar escenarios de error sistemáticamente
- Validar el manejo de errores en diferentes roles de usuario
- Probar puntos de integración con sistemas externos

### Estrategias de Prevención de Errores

**1. Validación de Entrada**
- Validar todos los parámetros de entrada antes de las llamadas a la API
- Utilizar tipos y formatos de datos apropiados
- Implementar validación del lado del cliente donde sea apropiado
- Verificar las reglas de negocio antes del envío

**2. Gestión de Conexiones**
- Implementar un grupo de conexiones adecuado
- Manejar los tiempos de espera de forma elegante
- Utilizar comprobaciones de estado para servicios dependientes
- Monitorear los límites de tasa de la API

**3. Consideraciones de Seguridad**
- Implementar un manejo adecuado de la autenticación
- Utilizar canales de comunicación seguros
- Registrar errores relacionados con la seguridad de forma apropiada
- Manejar datos sensibles en mensajes de error con cuidado

Para códigos de error específicos y procedimientos detallados de solución de problemas, consulte la documentación de su sistema Avaloq o contacte directamente al soporte de Avaloq, ya que muchos detalles de error son específicos de su implementación y configuración.