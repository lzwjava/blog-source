---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: 'Técnicas de Modulación Analógica: AM, FM, PM'
translated: true
type: note
---

### Técnicas de Modulación: AM, FM y PM

En el contexto de los sistemas de comunicación y el procesamiento de señales, **AM**, **FM** y **PM** se refieren a **técnicas de modulación analógica** fundamentales. Estos métodos se utilizan para codificar (o "modular") una señal portadora de información (como audio o datos) en una onda portadora de mayor frecuencia para una transmisión eficiente a través de medios como ondas de radio, cables o canales inalámbricos. Si bien se asocian principalmente con la comunicación analógica, pueden intersectarse con las conversiones analógico-digital (A/D) y digital-analógico (D/A) en sistemas híbridos, como cuando las señales muestreadas digitalmente se modulan para su transmisión o cuando las señales moduladas recibidas se digitalizan.

Aquí hay un desglose de cada una:

- **AM (Modulación de Amplitud)**:  
  La amplitud (fuerza o altura) de la onda portadora varía en proporción a la amplitud de la señal moduladora, mientras que la frecuencia de la portadora permanece constante. Es simple y se usa ampliamente en la radiodifusión AM. Es susceptible al ruido porque la interferencia afecta directamente la amplitud.  
  *Ejemplo*: En la transmisión de voz, los sonidos más fuertes aumentan los picos de amplitud de la portadora.

- **FM (Modulación de Frecuencia)**:  
  La frecuencia de la onda portadora varía según la amplitud y frecuencia de la señal moduladora, mientras que la amplitud de la portadora se mantiene constante. La FM ofrece una mejor resistencia al ruido y es común en la radio FM, el sonido de TV y las radios bidireccionales.  
  *Ejemplo*: Un audio de tono más alto desplaza la frecuencia de la portadora hacia arriba o hacia abajo proporcionalmente.

- **PM (Modulación de Fase)**:  
  La fase (sincronización o desplazamiento) de la onda portadora se altera en función de los cambios de la señal moduladora, con amplitud y frecuencia constantes. La PM es similar a la FM (están matemáticamente relacionadas mediante la diferenciación) y se usa a menudo en sistemas digitales como la modulación por desplazamiento de fase (PSK), pero en forma analógica, se aplica en algunas comunicaciones satelitales y móviles.  
  *Ejemplo*: Un cambio en la señal moduladora adelanta o retrasa el ciclo de la forma de onda de la portadora.

#### Relación con las Conversiones A/D y D/A
Estas técnicas están más directamente ligadas a la transmisión analógica, pero en los sistemas modernos:
- Durante la **conversión D/A**, una señal digital puede reconstruirse en una forma de onda analógica moduladora antes de aplicar AM/FM/PM para prepararla para la transmisión RF (radiofrecuencia).
- En la **conversión A/D**, una señal modulada analógica recibida (por ejemplo, de radio FM) se demodula primero, luego se muestrea y cuantifica en forma digital.

Para profundizar, consulta recursos sobre modulación analógica en procesamiento de señales.

[Técnicas de Modulación Analógica](https://en.wikipedia.org/wiki/Modulation#Analog_modulation_methods)  
[Comparación FM vs AM](https://www.electronics-tutorials.ws/accircuits/amplitude-modulator.html)