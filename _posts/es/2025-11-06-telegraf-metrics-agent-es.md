---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: 'Telegraf: Agente de Recopilación de Métricas de Código Abierto'
translated: true
type: note
---

Telegraf es un agente de código abierto y basado en plugins desarrollado por InfluxData para recopilar, procesar, agregar y escribir métricas, logs y otros datos de telemetría desde varias fuentes. Es ligero, se ejecuta como un único binario y admite más de 300 plugins de entrada (por ejemplo, para estadísticas del sistema, bases de datos como MySQL/PostgreSQL, servicios en la nube como AWS y aplicaciones como Apache Kafka) y más de 50 plugins de salida (por ejemplo, a InfluxDB, Prometheus, Kafka o Elasticsearch).

### Características Principales

- **Arquitectura basada en agente**: Se despliega fácilmente en servidores, contenedores o dispositivos IoT sin dependencias pesadas.
- **Extensible mediante plugins**: Escrito en Go, permitiendo plugins personalizados si es necesario.
- **Parte del stack TICK**: Se integra perfectamente con InfluxDB para el almacenamiento de datos de series de tiempo, Chronograf para la visualización y Kapacitor para las alertas.
- **Casos de uso**: Común en DevOps para el monitoreo de infraestructura, el seguimiento del rendimiento de aplicaciones y la ingesta de datos de sensores IoT.

Es gratuito bajo la licencia MIT y se mantiene activamente, con la última versión estable a finales de 2025 siendo la v1.29.x. Para la configuración, consulta la documentación oficial en [telegraf.influxdata.com](https://docs.influxdata.com/telegraf/). Si este no es el Telegraf al que te refieres (por ejemplo, una marca o término en otro contexto), ¡proporciona más detalles!