---
audio: false
generated: true
lang: es
layout: post
title: Circuitos Integrados TTL y CMOS
translated: true
type: note
---

## TTL (Transistor-Transistor Logic)

El TTL fue desarrollado a principios de la década de 1960 por Texas Instruments, y la serie 7400, introducida en 1964, se convirtió en un estándar de la industria. El TTL representó un avance significativo respecto a tecnologías anteriores como la DTL (Lógica Diodo-Transistor).

Acontecimientos clave en la historia del TTL:
- Creado originalmente por James L. Buie en TRW en 1961
- Comercializado por Texas Instruments con su serie 5400/7400
- El TTL estándar evolucionó hacia variantes mejoradas:
  - TTL de alta velocidad (serie 74H)
  - TTL de baja potencia (serie 74L)
  - TTL Schottky (serie 74S), que redujo el retardo de propagación
  - Schottky de baja potencia (serie 74LS)
  - Schottky avanzado de baja potencia (serie 74ALS)
  - Rápido (serie 74F)

El TTL dominó la lógica digital desde finales de la década de 1960 hasta la de 1970 y se utilizó en los primeros microordenadores, calculadoras y diversos equipos industriales. Su adopción generalizada se debió a su estandarización, fiabilidad y coste relativamente bajo.

## CMOS (Complementary Metal-Oxide-Semiconductor)

La tecnología CMOS fue inventada en 1963 por Frank Wanlass en Fairchild Semiconductor. La tecnología adquirió importancia comercial en la década de 1970 y finalmente superó al TTL.

Acontecimientos clave en la historia del CMOS:
- Patente presentada por Frank Wanlass en 1963
- RCA desarrolló la familia lógica CMOS serie 4000 a principios de la década de 1970
- Inicialmente más lento que el TTL, pero ofrecía un consumo de energía significativamente menor
- La serie CMOS de alta densidad (HC/HCT), introducida en la década de 1980, mejoró la velocidad
- El CMOS avanzado (AC/ACT) mejoró aún más el rendimiento a finales de la década de 1980

El CMOS acabó convirtiéndose en la tecnología dominante por varias razones:
- Consumo de energía mucho menor, especialmente en reposo
- Mejor inmunidad al ruido
- Rango de voltaje de operación más amplio
- Mayor densidad de integración
- Escalabilidad de fabricación que permitió que la Ley de Moore continuara

Para la década de 1990, el CMOS se había convertido en la base de prácticamente todos los circuitos integrados digitales, desde simples puertas lógicas hasta microprocesadores complejos. Los procesadores avanzados, chips de memoria y ASIC actuales están casi exclusivamente basados en CMOS, aunque con mejoras significativas respecto a la tecnología básica.

¿Le gustaría obtener información más específica sobre algún aspecto particular de la historia del TTL o el CMOS?

---

# Cómo funcionan los circuitos integrados TTL y CMOS

## TTL (Transistor-Transistor Logic)

El TTL funciona utilizando transistores bipolares de unión (BJT) y opera a través de una disposición específica de estos transistores:

1. **Etapa de entrada**: Utiliza un transistor multi-emisor donde cada emisor sirve como una entrada.

2. **Principio de operación**:
   - Cuando todas las entradas están en ALTO (~5V), la unión base-colector del transistor de entrada está polarizada en directo, y su unión colector-emisor está polarizada en inverso, lo que apaga el transistor de salida.
   - Cuando cualquier entrada pasa a BAJO (~0V), el transistor de entrada se satura, encendiendo el transistor de salida.

3. **Etapa de salida**: Normalmente emplea una disposición de "totem pole" con dos transistores. El transistor superior actúa como pull-up (suministrando corriente), y el transistor inferior actúa como pull-down (consumiendo corriente).

4. **Características**:
   - Opera con una fuente de alimentación de 5V
   - Robusta inmunidad al ruido (normalmente 0.8V para BAJO, 2.0V para ALTO)
   - Capaz de consumir más corriente que de suministrar
   - Componentes activos de pull-up y pull-down

## CMOS (Complementary Metal-Oxide-Semiconductor)

El CMOS funciona utilizando pares complementarios de MOSFETs (Transistores de Efecto de Campo Metal-Óxido-Semiconductor):

1. **Estructura básica**: Cada puerta lógica contiene pares complementarios de transistores P-canal (PMOS) y N-canal (NMOS).

2. **Principio de operación**:
   - Cuando la entrada es BAJA (0V), el transistor PMOS se enciende mientras el transistor NMOS se apaga.
   - Cuando la entrada es ALTA (voltaje de alimentación), el transistor PMOS se apaga mientras el transistor NMOS se enciende.
   - Esto crea una acción de conmutación complementaria donde solo un transistor está encendido a la vez.

3. **Características de potencia**:
   - Consumo de potencia estática casi nulo (la potencia solo se usa durante la conmutación)
   - La corriente fluye solo momentáneamente durante los cambios de estado cuando ambos transistores están parcialmente conduciendo
   - El consumo de energía aumenta con la frecuencia de conmutación

4. **Características clave**:
   - Amplio rango de voltaje de operación (normalmente 3-15V para CMOS antiguo, 1.8-5V para variantes modernas)
   - Alta inmunidad al ruido (normalmente 30-40% del voltaje de alimentación)
   - Capacidades de suministro y consumo de corriente casi iguales
   - Impedancia de entrada muy alta

La diferencia fundamental entre TTL y CMOS es que el TTL utiliza transistores bipolares controlados por corriente, mientras que el CMOS utiliza transistores de efecto de campo controlados por voltaje, lo que resulta en un consumo de energía significativamente menor para el CMOS, pero tradicionalmente velocidades de conmutación más lentas (aunque el CMOS moderno ha superado esta limitación).