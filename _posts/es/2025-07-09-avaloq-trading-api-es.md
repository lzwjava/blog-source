---
audio: false
generated: true
lang: es
layout: post
title: Explorando los detalles de la API de trading de Avaloq
translated: true
type: note
---

## Implementación de Trading en Avaloq

### Descripción General de la Plataforma de Trading
Avaloq permite a tus clientes operar cualquier producto, desde productos cotizados en bolsa hasta over-the-counter y cripto, en una única plataforma integral. La plataforma proporciona capacidades de trading completas integradas dentro del sistema bancario central.

### Comprobaciones de Cumplimiento Pre-Operación
El software verifica personas, transacciones y órdenes de valores utilizando reglas de cumplimiento predefinidas. Basándose en estos conjuntos de reglas, el software ACTICO Compliance decide automáticamente si existe un riesgo de cumplimiento. Esta integración muestra que Avaloq admite el cumplimiento pre-operación a través de asociaciones con soluciones de cumplimiento especializadas.

El sistema de comprobación pre-operación típicamente valida:
- Autorización y permisos del cliente
- Límites de riesgo y comprobaciones de exposición
- Requisitos de cumplimiento normativo
- Fondos disponibles y límites de crédito
- Temporización del mercado y restricciones de trading

### Integración API
El módulo Account Management API incluye diferentes endpoints de API que ofrecen conectividad para sistemas de terceros para proporcionar un acceso fácil a funcionalidades específicas. Avaloq proporciona acceso API a través de su plataforma avaloq.one, y existe un repositorio en GitHub con recursos para comenzar a utilizar las Open APIs de Avaloq.

## Enfoque de Implementación

### 1. Colocación de Órdenes de Acciones
Aunque no se encontró documentación específica de XML SOAP en los resultados de búsqueda, la implementación típica implicaría:

**Estructura de la Orden:**
- ID de orden e identificación del cliente
- Identificación del valor (ISIN, ticker, etc.)
- Tipo de orden (market, limit, stop, etc.)
- Parámetros de cantidad y precio
- Especificaciones de time-in-force
- Instrucciones de liquidación

### 2. Proceso de Comprobación Pre-Operación
La validación pre-operación típicamente seguiría este flujo:
- Enviar detalles de la orden al motor de cumplimiento
- Validar contra el perfil y los límites del cliente
- Verificar los requisitos normativos
- Confirmar fondos/valores disponibles
- Devolver aprobación/rechazo con razones

### 3. Llamada a la API XML SOAP
Basándose en las prácticas estándar de la industria financiera y la información disponible, la integración XML SOAP probablemente implicaría:

**Autenticación:**
- Credenciales de API y tokens de seguridad
- Identificación y autorización del cliente

**Formato del Mensaje:**
- Estructura estándar de sobre XML
- Esquemas específicos de Avaloq para operaciones de trading
- Manejo de errores y códigos de respuesta

## Recomendaciones para la Implementación

1.  **Acceso a la Documentación**: Contacta con Avaloq directamente o a través de su red de partners para acceder a la documentación detallada de la API, ya que esto parece estar restringido a clientes con licencia.

2.  **Entorno Sandbox**: Avaloq ha sentado una buena base para ayudar a las empresas a facilitar el proceso de prueba e integración de nuevas soluciones gestionando las complejidades en varias fases utilizando la solución sandbox de Avaloq impulsada por AWS.

3.  **Integración con Partners**: Considera trabajar con partners de implementación certificados por Avaloq que tengan experiencia con sus APIs de trading y puedan proporcionar orientación específica sobre los patrones de integración XML SOAP.

4.  **Integración de Cumplimiento**: La Avaloq Banking Suite funciona de forma fiable con el software ACTICO Compliance a través de una interfaz estándar, lo que sugiere patrones establecidos para la integración de cumplimiento.

Para obtener especificaciones técnicas detalladas, esquemas de API y ejemplos de implementación, necesitarías acceder a la documentación oficial para desarrolladores de Avaloq a través de su portal de clientes o contactar directamente con su equipo de soporte técnico.