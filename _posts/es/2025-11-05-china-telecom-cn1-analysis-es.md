---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Análisis de la Red CN1 de China Telecom
translated: true
type: note
---

Según el traceroute que compartiste desde una WiFi de una tienda Meiyijia en Guangzhou, esto parece estar usando la red troncal estándar ChinaNet de China Telecom (a menudo denominada CN1), no la red premium CN2. Aquí tienes un desglose rápido del porqué:

### Indicadores Clave del Traceroute
- **Saltos 5–10 (red troncal China Telecom)**: Las IPs como 14.147.135.198, 183.56.34.41, 202.97.93.89–202.97.116.210, y 203.215.237.42 pertenecen todas a AS4134 (ChinaNet), la principal red troncal nacional/internacional de China Telecom. Estas son comunes en líneas de banda ancha estándar.
  - El rango 202.97.x.x es específicamente de ChinaNet (no CN2).
  - 203.215.237.42 está ubicada en Xiamen, Fujian (todavía dentro de China), propiedad de CHINANET Fujian Province Network (AS4134).
- **No hay firmas de CN2**: CN2 (AS4809) típicamente muestra IPs en rangos como 59.43.0.0/16 o 121.59.0.0/16 durante la fase de la red troncal. Tu traceroute no llega a ninguna de esas.
- **Ruta de salida**: El tráfico sale de China a través de un traspaso estándar de ChinaNet a Microsoft (Azure) en Tokio (salto 11: 104.44.235.92), luego se enruta hacia el sur a Singapur (saltos 14–15). Esta es una ruta común y no optimizada para conexiones básicas de China Telecom—el desvío a través de Japón añade ~300ms de latencia, lo cual se alinea con la congestión de CN1. CN2 a menudo utiliza salidas directas por Hong Kong o más cortas en Asia-Pacífico para una latencia menor (~150–200ms a GitHub desde Guangzhou).
- **Contexto**: Las tiendas Meiyijia en Guangzhou normalmente funcionan con la banda ancha comercial/consumidor de China Telecom, que por defecto usa ChinaNet (CN1) a menos que se actualice explícitamente a CN2 GIA (un complemento empresarial de pago).

### Comparación Rápida CN1 vs. CN2

| Aspecto          | CN1 (ChinaNet)                          | CN2 (Premium)                          |
|-----------------|-----------------------------------------|----------------------------------------|
| **Número AS**   | AS4134                                 | AS4809                                |
| **Latencia Típica a GitHub (desde Guangzhou)** | 250–400ms (congestionado, rutas indirectas) | 100–200ms (optimizado, salidas directas)   |
| **Rangos de IP**   | 202.97.x.x, 183.56.x.x, etc.           | 59.43.x.x, 121.59.x.x, etc.           |
| **Caso de Uso**    | Banda ancha estándar para hogar/empresa       | VPS/cloud/empresa (costo adicional)     |
| **Estilo de Ruta**  | A menudo se desvía (ej., vía Japón/Corea)  | Directo a hubs de HK/EE.UU./Asia             |

Si quieres confirmar o probar más:
- Ejecuta `traceroute github.com` durante las horas pico (ej., noches) para comprobar si hay más congestión.
- Haz ping a un sitio de prueba de CN2 como `www.cn2.net`—si la latencia es menor a 200ms, podrías tener acceso parcial a CN2.
- Contacta al soporte de Meiyijia o China Telecom para consultar el tipo de línea que tienes (menciona "CN2 GIA" si estás considerando una actualización).

[Descripción General de China Telecom CN2](https://www.ctamericas.com/company/global-network/cn2/)  
[IPinfo para 203.215.237.42](https://ipinfo.io/203.215.237.42)  
[Guía CN2 vs ChinaNet](http://chihengcloud.com/en/blog/cloudservice/what-is-cn2-network-a-3-minute-guide-to-types-and-features/)