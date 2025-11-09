---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Cálculo de Hash y Minería de Bitcoin
translated: true
type: note
---

### Cómo Bitcoin calcula los hashes

Bitcoin utiliza una función hash criptográfica llamada **SHA-256** (Secure Hash Algorithm 256-bit) para calcular los hashes. Esta es una función unidireccional que toma datos de entrada (como el encabezado de un bloque) y produce una salida fija de 256 bits (32 bytes) que es única e impredecible.

- **¿Qué se convierte en hash?** Principalmente el encabezado del bloque, que incluye:
  - Número de versión
  - Hash del bloque anterior
  - Merkle root (un resumen de todas las transacciones en el bloque)
  - Marca de tiempo
  - Objetivo de dificultad (bits)
  - Nonce (un número que los mineros ajustan)

- **El proceso:**
  1. El minero ensambla el encabezado del bloque.
  2. Aplica SHA-256 dos veces: `hash = SHA256(SHA256(encabezado))`.
  3. Verifica si el hash resultante está por debajo del objetivo actual (por ejemplo, si comienza con suficientes ceros a la izquierda, como 000000...).
  4. Si no es así, incrementa el nonce y repite. Esta es la parte de "prueba y error" de la Prueba de Trabajo (PoW).

Los hashes son deterministas: la misma entrada siempre da la misma salida, pero pequeños cambios (como sumar 1 al nonce) producen salidas completamente diferentes. Esto hace que sea inviable revertir la ingeniería de las entradas a partir de las salidas.

### ¿Por qué minar Bitcoin? (Y cómo asegura un límite de suministro de 21 millones)

Creo que te referías a "por qué minar" en lugar de "por qué acuñar": la minería es el proceso de validar transacciones y añadir bloques a la blockchain, recompensado con nuevos bitcoins.

- **¿Por qué minar?**
  - **Seguridad:** Los mineros aseguran la red compitiendo para resolver los acertijos de PoW, previniendo ataques como el doble gasto (gastar el mismo BTC dos veces).
  - **Descentralización:** Cualquiera puede minar, distribuyendo el control—sin una autoridad central.
  - **Incentivo:** Los mineros ganan **recompensas de bloque** (BTC recién creados) + tarifas de transacción. Esto arranca la red y compensa los costes de energía.

- **Asegurando el límite de suministro (en realidad es 21 millones, no 10 millones):**
  El protocolo de Bitcoin codifica un suministro total de **21 millones de BTC**, creado a través de recompensas de minería que se **reducen a la mitad** cada 210.000 bloques (~4 años).
  - Comenzó con 50 BTC por bloque en 2009.
  - Se redujo a 25 en 2012, 12.5 en 2016, 6.25 en 2020, 3.125 en 2024, y así sucesivamente.
  - El último bitcoin se minará alrededor de 2140; después de eso, solo quedarán las tarifas.
  - Esto es impuesto por el código: La fórmula de la recompensa es `recompensa = 50 * 0.5^(piso(altura_del_bloque / 210000))`. Nadie puede cambiarlo sin el consenso del 95% de la red, haciendo la inflación predecible y con un límite.

Esta escasez imita al oro, impulsando el valor.

### Cómo funciona la Prueba de Trabajo (PoW)

PoW es el mecanismo de consenso de Bitcoin—un rompecabezas computacional que prueba que un minero invirtió "trabajo" (potencia de CPU/GPU/ASIC) para añadir un bloque.

- **Paso a paso:**
  1. **Recolectar transacciones:** Los mineros reúnen transacciones pendientes en un bloque (hasta ~1-4 MB, dependiendo de SegWit).
  2. **Construir el encabezado:** Incluir la raíz de Merkle de las transacciones, enlace al bloque anterior, etc.
  3. **Establecer el objetivo:** La red ajusta la dificultad cada 2016 bloques para mantener un tiempo promedio de bloque en 10 minutos. Objetivo = un número muy pequeño (por ejemplo, el hash debe ser < 0x00000000FFFF...).
  4. **Encontrar el nonce:** Adivinar nonces por fuerza bruta (0 a 2^32-1). Para cada uno, aplicar hash al encabezado. Si el hash < objetivo, ¡es válido!
  5. **Transmitir el bloque:** Otros nodos verifican (es fácil—solo re-aplicar hash una vez). Si es válido, lo añaden a la cadena; los mineros comienzan con el siguiente bloque.
  6. **Regla de la cadena:** Gana la cadena válida más larga (resuelve bifurcaciones).

PoW hace que sea barato verificar bloques pero caro crearlos, protegiendo contra ataques del 51% (controlar >50% de la tasa de hash para reescribir la historia).

### ¿Por qué tantos cálculos para una transacción?

Las transacciones no requieren directamente una computación masiva de los usuarios—solo firmar con tu clave privada (criptografía de curva elíptica, rápido). El trabajo pesado está en la **minería**:

- **Por bloque, no por transacción:** Un bloque agrupa ~2.000-3.000 transacciones. Los mineros aplican hash billones de veces por bloque para resolver la PoW.
- **Ajuste de dificultad:** A medida que más mineros se unen (mayor tasa de hash total), la dificultad aumenta exponencialmente para mantener bloques de 10 minutos. La tasa de hash global actual es de ~600 EH/s (exahashes por segundo)—¡eso son 600 trillones de hashes por segundo!
- **¿Por qué el desperdicio?**
  - **Coste de seguridad:** La alta computación hace que los ataques no sean económicos. Reescribir un bloque cuesta rehacer toda la PoW posterior.
  - **Resistencia Sybil:** Evita inundar la red con identidades falsas.
  - **Compromiso:** Consume mucha energía (Bitcoin usa ~150 TWh/año, como un país de tamaño medio), pero los proponentes argumentan que es una característica para un dinero sin necesidad de confianza.

Los usuarios pagan tarifas para priorizar transacciones en los bloques; las de baja tarifa esperan.

Si te referías a algo específico (como hardware para la minería), ¡avísame!

**Referencias:**  
[Bitcoin Whitepaper](https://bitcoin.org/bitcoin.pdf)  
[Bitcoin Wiki: Proof of Work](https://en.bitcoin.it/wiki/Proof_of_work)  
[Blockchain.com: Bitcoin Halving](https://www.blockchain.com/learning-crypto/bitcoin-halving)