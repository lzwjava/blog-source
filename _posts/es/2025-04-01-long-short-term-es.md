---
audio: false
generated: true
lang: es
layout: post
title: Redes de Memoria a Largo y Corto Plazo
translated: true
type: note
---

Las redes de memoria a largo plazo (LSTM) son un tipo de arquitectura de red neuronal recurrente diseñada específicamente para abordar el problema del gradiente que se desvanece y permitir el aprendizaje de dependencias a largo plazo en datos secuenciales. Logran esto a través de una estructura interna más sofisticada llamada **celda LSTM**.

Aquí hay un desglose de cómo funciona una celda LSTM:

**Idea Central: El Estado de la Celda**

El concepto central en una LSTM es el **estado de la celda** (a menudo denotado como 'C<sub>t</sub>'). Piensa en el estado de la celda como una cinta transportadora que recorre toda la secuencia. Lleva información relevante para la historia a largo plazo de la secuencia. La información puede agregarse o eliminarse del estado de la celda a medida que fluye a través de la red mediante estructuras llamadas **compuertas**.

**Las Compuertas**

Las celdas LSTM tienen tres compuertas principales que regulan el flujo de información:

1.  **Compuerta de Olvido:** Esta compuerta decide qué información del estado de celda anterior debe descartarse.
    * Recibe el estado oculto anterior (h<sub>t-1</sub>) y la entrada actual (x<sub>t</sub>).
    * Estos se pasan a través de una capa de red neuronal seguida de una **función de activación sigmoide**.
    * La función sigmoide produce valores entre 0 y 1. Un valor cercano a 0 significa "olvidar completamente esta información", mientras que un valor cercano a 1 significa "conservar completamente esta información".
    * Matemáticamente, la salida de la compuerta de olvido (f<sub>t</sub>) se calcula como:
        ```
        f_t = σ(W_f * [h_{t-1}, x_t] + b_f)
        ```
        donde:
        * σ es la función sigmoide.
        * W<sub>f</sub> es la matriz de pesos para la compuerta de olvido.
        * [h<sub>t-1</sub>, x_t] es la concatenación del estado oculto anterior y la entrada actual.
        * b<sub>f</sub> es el vector de sesgo para la compuerta de olvido.

2.  **Compuerta de Entrada:** Esta compuerta decide qué nueva información de la entrada actual debe agregarse al estado de la celda. Este proceso implica dos pasos:
    * **Capa de la Compuerta de Entrada:** Una capa sigmoide decide qué valores actualizaremos.
        ```
        i_t = σ(W_i * [h_{t-1}, x_t] + b_i)
        ```
        donde:
        * σ es la función sigmoide.
        * W<sub>i</sub> es la matriz de pesos para la compuerta de entrada.
        * [h<sub>t-1</sub>, x_t] es la concatenación del estado oculto anterior y la entrada actual.
        * b<sub>i</sub> es el vector de sesgo para la compuerta de entrada.
    * **Capa de Valores Candidatos:** Una capa tanh crea un vector de nuevos valores candidatos (estado de celda candidato, denotado como 'C̃<sub>t</sub>') que podrían agregarse al estado de la celda. La función tanh produce valores entre -1 y 1, lo que ayuda a regular la red.
        ```
        C̃_t = tanh(W_C * [h_{t-1}, x_t] + b_C)
        ```
        donde:
        * tanh es la función tangente hiperbólica.
        * W<sub>C</sub> es la matriz de pesos para el estado de celda candidato.
        * [h<sub>t-1</sub>, x_t] es la concatenación del estado oculto anterior y la entrada actual.
        * b<sub>C</sub> es el vector de sesgo para el estado de celda candidato.

3.  **Compuerta de Salida:** Esta compuerta decide qué información del estado de celda actual debe emitirse como el estado oculto para el paso de tiempo actual.
    * Recibe el estado oculto anterior (h<sub>t-1</sub>) y la entrada actual (x<sub>t</sub>).
    * Estos se pasan a través de una capa de red neuronal seguida de una **función de activación sigmoide** para determinar qué partes del estado de la celda se van a emitir.
        ```
        o_t = σ(W_o * [h_{t-1}, x_t] + b_o)
        ```
        donde:
        * σ es la función sigmoide.
        * W<sub>o</sub> es la matriz de pesos para la compuerta de salida.
        * [h<sub>t-1</sub>, x_t] es la concatenación del estado oculto anterior y la entrada actual.
        * b<sub>o</sub> es el vector de sesgo para la compuerta de salida.
    * El estado de la celda se pasa luego a través de una **función tanh** para comprimir los valores entre -1 y 1.
    * Finalmente, la salida de la compuerta sigmoide se multiplica elemento por elemento con la salida de la función tanh aplicada al estado de la celda. Esto se convierte en el nuevo estado oculto (h<sub>t</sub>) que se pasa al siguiente paso de tiempo y también puede usarse para hacer predicciones.
        ```
        h_t = o_t * tanh(C_t)
        ```

**Actualización del Estado de la Celda**

El estado de la celda se actualiza en función de las decisiones tomadas por las compuertas de olvido y entrada:

```
C_t = f_t * C_{t-1} + i_t * C̃_t
```

* La compuerta de olvido (f<sub>t</sub>) determina cuánto del estado de celda anterior (C<sub>t-1</sub>) se debe conservar. Si f<sub>t</sub> está cerca de 0, la información se olvida en su mayoría. Si está cerca de 1, la información se conserva en su mayoría.
* La compuerta de entrada (i<sub>t</sub>) determina cuánto de los nuevos valores candidatos (C̃<sub>t</sub>) debe agregarse al estado de la celda. Si i<sub>t</sub> está cerca de 0, la nueva información se ignora en su mayoría. Si está cerca de 1, la nueva información se agrega en su mayoría.

**Cómo las LSTMs Resuelven el Problema del Gradiente que se Desvanece:**

La clave de la capacidad de las LSTM para manejar dependencias a largo plazo reside en el estado de la celda y los mecanismos de compuerta. El estado de la celda actúa como una vía directa para que la información fluya a través de muchos pasos de tiempo sin ser multiplicada repetidamente por pesos, que es la causa principal de los gradientes que se desvanecen en las RNN tradicionales.

Las compuertas permiten a la LSTM aprender cuándo almacenar, acceder y olvidar información en el estado de la celda. Este mecanismo de memoria selectiva permite a la red retener información relevante a lo largo de secuencias largas y usarla cuando sea necesario, mitigando efectivamente el problema del gradiente que se desvanece y permitiendo el aprendizaje de dependencias a largo plazo.

En esencia, las LSTMs proporcionan una forma para que la red mantenga una "memoria" durante períodos prolongados, lo que las hace muy efectivas para tareas que involucran datos secuenciales con dependencias de largo alcance.