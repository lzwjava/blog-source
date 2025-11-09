---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Circuito de LED Reactivo al Sonido
translated: true
type: note
---

### Circuito simple de LEDs reactivos a la música en una protoboard

Parece que recuerdas un proyecto genial de LEDs reactivos al sonido de 2021—básicamente, un circuito donde los LEDs laten o "bailan" al ritmo de la música, detectado mediante un micrófono o una entrada de audio. Las "luces de burbujas" probablemente sean solo LEDs coloridos en la protoboard, y la parte de "bajar el volumen" podría referirse a ajustar la sensibilidad o usar un potenciómetro para controlar el brillo/respuesta de los LEDs.

Para una versión súper simple (sin necesidad de microcontrolador, solo componentes básicos), puedes construir uno que encienda múltiples LEDs al ritmo de la música o sonido cercano. Esto utiliza un micrófono electret (a menudo listado como un "altavoz" en tutoriales básicos, pero aquí actúa como micrófono) para captar el audio, algunos diodos para el procesamiento de la señal y transistores implícitamente a través de los zeners para accionar los LEDs. Es compatible con protoboard y cuesta menos de $10 en componentes.

#### Componentes de hardware necesarios
Aquí hay una lista mínima para 6 LEDs (reduce si quieres menos):

| Componente               | Valor/Especificación | Cantidad |
|--------------------------|----------------------|----------|
| Resistor                | 56Ω                 | 6        |
| Capacitor               | 470µF               | 2        |
| Diodo                   | 1N4007 (o similar)  | 2        |
| Diodo Zener             | 1N4148              | 5        |
| Micrófono Electret (altavoz/ mic pequeño) | 8Ω, 0.5W | 1        |
| LED                     | Cualquier color, 5mm | 6       |
| Protoboard              | Tamaño estándar     | 1        |
| Cables puente           | Macho-macho         | ~20      |
| Fuente de alimentación  | Batería de 9V o adaptador de 5-12V | 1 |

Opcional para "control de volumen": Añade un potenciómetro de 10kΩ en serie con el micrófono para ajustar la sensibilidad (como bajar el "volumen" de la señal de entrada).

#### Descripción rápida de la construcción
1.  **Configurar la entrada del micrófono**: Conecta el micrófono entre la alimentación y tierra a través de un capacitor (para la señal de audio AC). Esto capta las vibraciones del sonido y las convierte en pulsos eléctricos.
2.  **Procesamiento de la señal**: Utiliza los diodos y diodos zener en una configuración de rectificador/filtro para convertir la forma de onda de audio en pulsos que activen los LEDs a diferentes intensidades según la fuerza del volumen/ritmo. Los zeners protegen contra picos de voltaje.
3.  **Accionamiento de los LEDs**: Conecta cada LED en paralelo con una resistencia de 56Ω para limitar la corriente. Conecta la señal procesada a los ánodos de los LED—los graves o ritmos más fuertes harán que parpadeen con más brillo/rapidez.
4.  **Alimentación**: Conéctalo a 9V. Reproduce música cerca (el altavoz de un teléfono funciona) y los LEDs deberían sincronizarse con el ritmo. Los condensadores suavizan la señal para un efecto de "baile".
5.  **Consejos para la protoboard**: Coloca el micrófono en un lado, los diodos/condensadores en el medio, y los LEDs en una fila en el otro lado. Prueba con un multímetro para verificar la continuidad antes de encender.

Esto crea ese espectáculo de luces hipnótico sin piezas sofisticadas. Si quieres añadir un potenciómetro para ajustar el volumen, solo colócalo en línea en la señal del micrófono—reducirá la respuesta de los LEDs como mencionaste.

Para esquemas completos y pasos, consulta estos enlaces:

[Circuito simple de LEDs reactivos al sonido](https://www.circuits-diy.com/simple-sound-reactive-leds-circuit/)
[Creando un circuito de LED reactivo al audio (versión aún más simple con un solo LED)](https://www.instructables.com/Creating-An-Audio-Reactive-LED-Circuit/)