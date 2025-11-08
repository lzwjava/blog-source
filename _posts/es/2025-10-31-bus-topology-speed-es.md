---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Limitaciones de Velocidad en Topología de Bus Explicadas
translated: true
type: note
---

### Limitaciones de la Topología de Bus

Tienes razón sobre las características clave: la topología de bus utiliza un único cable compartido (como el coaxial en las configuraciones clásicas de Ethernet) que es simple y barato pero vulnerable a colisiones. Cuando múltiples dispositivos intentan transmitir al mismo tiempo, las señales se superponen, causando "colisiones" que requieren retransmisión mediante protocolos como CSMA/CD (Acceso Múltiple por Detección de Portadora con Detección de Colisiones).

#### Por Qué ~100 Mbps Parece un Límite Práctico (Aunque el Cable Pueda Hacer Más)
Los cables en sí mismos—ya sean de cobre (por ejemplo, par trenzado o coaxial) o ópticos/fibra—no son el cuello de botella aquí. La fibra óptica puede manejar fácilmente gigabits por segundo (o terabits en configuraciones modernas) sobre largas distancias con pérdidas mínimas. Los límites reales provienen de la **naturaleza de medio compartido del bus** y la sobrecarga física/del protocolo. Esto es lo que limita las velocidades alrededor de 10–100 Mbps en los diseños de bus tradicionales:

1. **Retardo de Propagación y Detección de Colisiones**:
   - Las señales tardan tiempo en viajar por el cable (por ejemplo, ~5 ns/metro en coaxial o ~5 ns/km en fibra).
   - En un bus, cada dispositivo debe "escuchar" las colisiones a lo largo de *toda la longitud de la red*. El protocolo define un "tiempo de ranura" (tiempo mínimo para detectar una colisión), que debe ser mayor que el retardo de propagación de ida y vuelta (RTT) para el peor escenario (señal de un extremo al otro y de regreso).
   - Para Ethernet de 10 Mbps (bus clásico), la longitud máxima del segmento era de ~500m para mantener el RTT por debajo de 51.2 μs (tiempo de ranura de 512 bits).
   - A 100 Mbps, el tiempo de ranura se reduce proporcionalmente (a ~5.12 μs), forzando longitudes máximas a ~100m. Más allá de eso, las colisiones no se detectan, lo que lleva a errores interminables.
   - ¿Llevarlo a 1 Gbps? El tiempo de ranura cae a ~0.512 μs, limitando los segmentos a ~10–20m—impráctico para un "bus" que conecta múltiples dispositivos.

2. **Sobrecarga por Colisiones y Eficiencia**:
   - CSMA/CD añade reintentos: una colisión desperdicia ancho de banda (hasta un 50% de pérdida de eficiencia bajo carga pesada).
   - Las velocidades más altas amplifican esto—colisiones más frecuentes significan más ciclos desperdiciados, reduciendo el rendimiento efectivo.
   - El medio compartido significa que el ancho de banda total se divide entre todos los dispositivos; no hay dedicación por puerto.

3. **Integridad de la Señal y Ruido**:
   - Aunque la fibra resiste mejor la interferencia electromagnética (EMI) que el cobre, las configuraciones de bus aún necesitan un temporizado preciso para la detección de portadora.
   - A altas velocidades, las reflexiones, atenuación o diafonía en una línea compartida degradan las señales más rápido, requiriendo más repetidores (que añaden retardo y costo).

#### ¿Por Qué Cambiar del Bus para Obtener Velocidades Más Rápidas?
Esta es la razón por la que Ethernet evolucionó: después de 100 Mbps (Fast Ethernet), abandonaron el bus puro por la **topología en estrella con switches** (por ejemplo, 1 Gbps+). Los switches crean enlaces punto a punto full-duplex—sin colisiones, ancho de banda completo por dispositivo y tramos más largos. El bus ahora es raro fuera de usos de nicho/industriales.

Si estás pensando en una configuración específica (por ejemplo, CAN bus en coches o el viejo 10BASE-T), los principios son similares: protocolo + física > capacidad del cable.

Para análisis más profundos:  
[Conceptos Básicos de la Topología de Bus Ethernet](https://en.wikipedia.org/wiki/Bus_network)  
[Limitaciones de CSMA/CD](https://www.cisco.com/c/en/us/support/docs/lan-switching/ethernet/10561-3.html)