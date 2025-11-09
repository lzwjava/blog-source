---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Descripción General de VMware Tanzu Application Service
translated: true
type: note
---

## Introducción a VMware Tanzu Application Service para VM (TAS para VM)

VMware Tanzu Application Service para VM (TAS para VM) es una plataforma-como-servicio (PaaS) comercial construida sobre el proyecto de código abierto Cloud Foundry. Está diseñada para simplificar el despliegue, escalado y gestión de aplicaciones cloud-native, permitiendo a los desarrolladores centrarse en escribir código en lugar de manejar infraestructura. TAS para VM permite el despliegue rápido de aplicaciones en diversos entornos, incluyendo on-premises (como vSphere) o nubes públicas (AWS, Azure, GCP, OpenStack), y admite configuraciones auto-gestionadas y proveedores comerciales certificados.

### Características Principales
- **Fundación de Código Abierto**: Aprovecha la extensibilidad de Cloud Foundry para evitar el vendor lock-in, admitiendo múltiples lenguajes, frameworks y servicios.
- **Despliegue Automatizado**: Despliega aplicaciones usando herramientas familiares (ej. CLI) sin cambios en el código; las aplicaciones se empaquetan en "droplets" (paquetes precompilados) para un staging y ejecución rápidos.
- **Escalabilidad y Resiliencia**: Utiliza Diego para la distribución inteligente de carga entre las VM, escalado automático y tolerancia a fallos para manejar picos de tráfico o fallos.
- **Gestión de Usuarios**: Organiza equipos en "organizaciones" y "espacios" con acceso basado en roles (ej. admin, desarrollador) a través de servidores UAA (User Account and Authentication).
- **Integración de Servicios**: Vincula fácilmente aplicaciones a servicios como bases de datos o APIs a través de Service Brokers, sin modificar el código de la aplicación.
- **Monitorización y Logging**: Agrega logs y métricas a través de Loggregator en un stream "Firehose" para análisis en tiempo real, alertas e integración con herramientas.
- **Opción de Huella Pequeña**: Una versión ligera que se ejecuta en solo 4 VM (frente a 13+ para la estándar), ideal para equipos pequeños o testing, aunque con algunas limitaciones de escala.
- **Infraestructura Flexible**: Desplegada vía BOSH (una herramienta de automatización) y gestionada con Tanzu Operations Manager para una configuración simplificada.

### Beneficios
TAS para VM acelera el time-to-market al permitir que las aplicaciones estén en vivo en minutos, con escalado automático y accesibilidad global. Reduce la sobrecarga de infraestructura, mejora la seguridad a través de espacios de trabajo compartimentados y promueve la portabilidad—las aplicaciones se ejecutan de manera consistente en todos los entornos. Al abstraer la gestión de las VM, reduce costes y complejidad, mientras que la comunidad de Cloud Foundry garantiza una innovación y soporte continuos.

### Cómo Funciona
En esencia, TAS para VM actúa como una PaaS multi-tenant:
1.  **Despliegue**: Usa Tanzu Operations Manager para configurar y desplegar la plataforma en VM gestionadas por BOSH.
2.  **Ciclo de Vida de la Aplicación**: Los desarrolladores suben código vía CLI; el Cloud Controller lo prepara con buildpacks (para la configuración específica del lenguaje) en droplets, luego Diego subasta y ejecuta instancias a través de las VM host.
3.  **Enrutamiento y Acceso**: Gorouter maneja el tráfico entrante, balanceado externamente; UAA autentica a los usuarios.
4.  **Operaciones**: Los componentes internos se comunican a través de mensajería NATS y BOSH DNS; recursos como blobs y configuraciones se almacenan en GitHub, blobstores o MySQL.

TAS para VM extiende Cloud Foundry de código abierto con las características enterprise-grade, el soporte y las certificaciones de VMware, lo que la convierte en una opción robusta para cargas de trabajo de producción.

Para más detalles, consulta la documentación oficial: [Resumen de TAS para VM](https://techdocs.broadcom.com/us/en/vmware-tanzu/platform/tanzu-platform-for-cloud-foundry/6-0/tpcf/concepts-overview.html)