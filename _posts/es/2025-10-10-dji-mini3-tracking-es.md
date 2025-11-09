---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Limitaciones y soluciones del seguimiento del DJI Mini 3
translated: true
type: note
---

El DJI Mini 3 (el modelo básico) no tiene funciones integradas como ActiveTrack (seguimiento visual de objetos) o modo Follow Me (seguimiento basado en GPS) para seguir automáticamente o mantenerse sobre un coche en movimiento para tomar fotos o video. Esta es una limitación clave en comparación con los drones DJI de gama alta. Sin embargo, el DJI Mini 3 Pro sí es compatible con ActiveTrack, que utiliza la cámara del dron para rastrear y seguir visualmente sujetos como coches, personas o vehículos desde atrás, arriba o en otras posiciones, lo que te permite capturar tomas dinámicas mientras el dron mantiene una distancia y altura establecidas.

En cuanto a las APIs para desarrollo personalizado:
- El Mobile SDK de DJI (para aplicaciones Android/iOS) sí es compatible con la serie Mini 3, incluyendo el control básico de vuelo como los comandos de palanca virtual (por ejemplo, para ajustar manualmente la posición/velocidad) y misiones de waypoint. Podrías crear una aplicación personalizada para que el dron siga la ruta de un coche si integras datos GPS en tiempo real del coche (a través de Bluetooth, una aplicación complementaria o un transmisor externo). Esto no sería un seguimiento visual "plug-and-play" pero podría aproximarse a seguirlo desde arriba o atrás calculando desplazamientos (por ejemplo, 10-20 metros atrás y 50 metros arriba).
- Sin embargo, las APIs de misiones ActiveTrack del SDK (para el seguimiento visual automatizado) **no son compatibles** con el Mini 3 ni el Mini 3 Pro; están limitadas a modelos más antiguos como el Mavic Air 2 o Air 2S.
- Para la captura de fotos durante el vuelo, puedes usar las APIs de cámara del SDK para activar tomas automáticamente basadas en temporizadores, distancia o tu lógica personalizada.

Si estás dispuesto a usar aplicaciones de terceros (que utilizan el SDK internamente):
- Aplicaciones como Dronelink o Litchi pueden habilitar un modo básico "Follow Me" en el Mini 3 utilizando el GPS de tu teléfono (o un dispositivo externo). Para rastrear un coche específicamente, necesitarías emparejarlo con una baliza GPS en el vehículo (por ejemplo, a través de un hotspot de smartphone o un rastreador dedicado como una alternativa a Tile o AirTag que envíe datos a la aplicación). Esta configuración ha funcionado para usuarios que siguen coches en carreteras o caminos, con el dron manteniéndose arriba o siguiendo detrás para grabar.

Ten en cuenta aspectos legales/de seguridad: El seguimiento de vehículos en movimiento con drones debe cumplir con las regulaciones locales (por ejemplo, las normas de la FAA en EE. UU. requieren línea de vista visual, no operaciones más allá del rango visual). Prueba en áreas abiertas para evitar obstáculos, y el diseño ligero del Mini 3 limita su resistencia al viento durante persecuciones a alta velocidad.

### Referencias
- [DJI Mini 3 Active Track HACK DJI Mini 3 Follow Me](https://www.youtube.com/watch?v=UYzSdd3iJwA)
- [Does the mini 3 have ai tracking to follow objects like cars](https://www.facebook.com/groups/djimini3ukowners/posts/2726498670890510/)
- [Can someone explain follow me mode? And if it's on mini 3?](https://www.reddit.com/r/dji/comments/13pqbw7/can_someone_explain_follow_me_mode_and_if_its_on/)
- [DJI Mini 3 / Mini 3 Pro - Follow Me Mode With Dronelink](https://www.youtube.com/watch?v=Rhneo8QoXV0)
- [DJI Product SDK Compatibility](https://support.dji.com/help/content?customId=01700000763&spaceId=17&re=US&lang=en&documentType=&paperDocType=ARTICLE)
- [DJI has released MSDK 5.3.0 with support for Mini 3 Pro and Mini 3](https://forum.flylitchi.com/t/dji-has-released-msdk-5-3-0-with-support-for-mini-3-pro-and-mini-3/9512)
- [class ActiveTrackOperator - DJI Mobile SDK Documentation](https://developer.dji.com/api-reference/android-api/Components/Missions/DJIActiveTrackMissionOperator.html)