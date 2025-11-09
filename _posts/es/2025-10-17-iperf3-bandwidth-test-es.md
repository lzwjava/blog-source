---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Herramienta de Prueba de Ancho de Banda de Red iPerf3
translated: true
type: note
---

### ¿Qué es iPerf3?

iPerf3 es una herramienta de línea de comandos de código abierto diseñada para medir el ancho de banda y el rendimiento de la red. Se utiliza comúnmente para probar el rendimiento máximo alcanzable en redes IP simulando tráfico entre dos endpoints (uno actuando como servidor y el otro como cliente). Esto ayuda a diagnosticar problemas como latencia, pérdida de paquetes y cuellos de botella en redes locales o de área extensa.

#### Características principales:
- **Protocolos admitidos**: TCP, UDP y SCTP para escenarios de prueba flexibles.
- **Personalización**: Permite ajustar parámetros como el tamaño del búfer, la duración de la prueba y el tráfico bidireccional.
- **Salida**: Proporciona estadísticas detalladas sobre ancho de banda, jitter y pérdida de datagramas.

#### Ejemplo de uso básico:
Para probar el ancho de banda entre dos máquinas:
1. En el servidor: `iperf3 -s` (inicia el servidor).
2. En el cliente: `iperf3 -c <IP_del_servidor>` (se conecta y ejecuta una prueba de 10 segundos por defecto).

Es una herramienta ligera, multiplataforma (funciona en Linux, Windows, macOS) y es ampliamente utilizada por administradores de red, desarrolladores y profesionales de TI para la resolución de problemas.

#### Historia:
iPerf3 es una reescritura completa de la herramienta iPerf original, iniciada en 2009 por ESnet (Energy Sciences Network) y lanzada por primera vez en 2014. El rediseño tenía como objetivo crear una base de código más pequeña y mantenible, mejorando al mismo tiempo la precisión.

Para más detalles, consulta el sitio oficial o el repositorio de GitHub.

### Referencias
- [iPerf - The TCP, UDP and SCTP network bandwidth measurement tool](https://iperf.fr/)
- [iperf3: A TCP, UDP, and SCTP network bandwidth measurement tool](https://github.com/esnet/iperf)
- [Iperf - Wikipedia](https://en.wikipedia.org/wiki/Iperf)