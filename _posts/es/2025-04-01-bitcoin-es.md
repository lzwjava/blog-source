---
audio: false
generated: true
lang: es
layout: post
title: Cómo Funciona Bitcoin
translated: true
type: note
---

Técnicamente, Bitcoin funciona a través de una combinación de criptografía, una red peer-to-peer y un mecanismo de consenso llamado Proof-of-Work (PoW). Aquí hay un desglose de los componentes y procesos clave:

**1. Fundamentos Criptográficos:**

*   **Hashing (SHA-256):** Bitcoin depende en gran medida de la función hash criptográfica SHA-256. Esta función toma cualquier dato de entrada y produce una salida de tamaño fijo de 256 bits (el hash). Las propiedades clave de SHA-256 utilizadas en Bitcoin incluyen:
    *   **Determinista:** La misma entrada siempre produce la misma salida.
    *   **Unidireccional:** Es computacionalmente inviable revertir el proceso y encontrar la entrada a partir de la salida.
    *   **Resistente a colisiones:** Es extremadamente difícil encontrar dos entradas diferentes que produzcan la misma salida.
*   **Firmas Digitales (ECDSA):** Bitcoin utiliza el Elliptic Curve Digital Signature Algorithm (ECDSA) para asegurar las transacciones. Cada usuario de Bitcoin tiene un par de claves criptográficas:
    *   **Clave Privada:** Una clave secreta que permite al usuario autorizar (firmar) transacciones.
    *   **Clave Pública:** Una clave derivada de la clave privada que puede compartirse con otros. Se utiliza para verificar la autenticidad de las transacciones firmadas por la clave privada correspondiente.
*   **Direcciones de Bitcoin:** Se derivan de las claves públicas mediante una serie de pasos de hashing y codificación. Son las "direcciones" que los usuarios comparten para recibir Bitcoin.

**2. La Blockchain:**

*   **Libro Mayor Distribuido:** Bitcoin mantiene un libro mayor público y descentralizado llamado blockchain. Este registro contable documenta cada transacción de Bitcoin de manera cronológica y transparente.
*   **Bloques:** Las transacciones se agrupan en bloques. Cada bloque contiene:
    *   Un conjunto de transacciones verificadas.
    *   Una referencia al hash del **bloque anterior** en la cadena. Esto crea la estructura en forma de cadena.
    *   Un **nonce**: Un número aleatorio utilizado en el proceso de minería.
    *   Una **marca de tiempo**.
    *   El hash del bloque actual.
*   **Inmutabilidad:** Una vez que un bloque se agrega a la blockchain, es extremadamente difícil alterarlo porque hacerlo requeriría recalcular los hashes de ese bloque y todos los bloques posteriores, lo que sería computacionalmente inviable para un atacante que controle menos del 51% del poder computacional de la red.

**3. Transacciones:**

*   **Estructura:** Una transacción de Bitcoin típicamente incluye:
    *   **Inputs:** Referencias a transacciones anteriores donde el remitente recibió el Bitcoin que ahora está gastando. Son esencialmente punteros a "unspent transaction outputs" (UTXOs) específicos.
    *   **Outputs:** Especifican la(s) dirección(es) de Bitcoin del destinatario y la cantidad de Bitcoin que se envía a cada uno. Una transacción puede tener múltiples outputs.
    *   **Firma:** Una firma digital creada usando la clave privada del remitente. Esto prueba que el propietario del Bitcoin autorizó la transacción.
*   **Difusión:** Una vez que se crea y firma una transacción, se transmite a la red peer-to-peer de Bitcoin.

**4. Minería y Proof-of-Work:**

*   **Miners:** Son nodos en la red de Bitcoin que realizan el trabajo de verificar y agregar nuevas transacciones a la blockchain.
*   **Verificación de Transacciones:** Los mineros recopilan transacciones pendientes y no confirmadas de la red y verifican su validez (por ejemplo, asegurándose de que el remitente tiene suficiente Bitcoin para gastar y de que las firmas digitales son válidas).
*   **Creación de un Bloque:** Los mineros agrupan estas transacciones verificadas en un nuevo bloque. También incluyen una transacción especial llamada "coinbase transaction" que les otorga Bitcoin recién creados y las tarifas de transacción pagadas por los remitentes en las transacciones incluidas en el bloque.
*   **Proof-of-Work (PoW):** Para agregar un nuevo bloque a la blockchain, los mineros deben resolver un problema computacionalmente difícil utilizando el algoritmo SHA-256. Este proceso se llama "minería".
    *   Los mineros cambian repetidamente el **nonce** (un número aleatorio) en el encabezado del bloque.
    *   Para cada nonce, calculan el hash SHA-256 de todo el encabezado del bloque.
    *   El objetivo es encontrar un nonce que resulte en un hash que comience con un cierto número de ceros a la izquierda. El número de ceros requeridos está determinado por la **dificultad** de la red Bitcoin.
    *   Encontrar dicho hash es cuestión de prueba y error y requiere un poder computacional significativo.
*   **Validación del Bloque y Consenso:** Una vez que un minero encuentra un hash válido (el "proof-of-work"), transmite el nuevo bloque al resto de la red. Otros nodos en la red luego verifican:
    *   Que las transacciones en el bloque son válidas.
    *   Que el hash del bloque es correcto.
    *   Que el hash cumple con el objetivo de dificultad actual.
    *   Que la referencia al hash del bloque anterior es correcta.
*   **Agregar a la Blockchain:** Si el bloque es válido, otros nodos lo aceptan y lo agregan a su copia de la blockchain, extendiendo la cadena. Este proceso asegura que todos los nodos estén de acuerdo en el orden y la validez de las transacciones. La cadena más larga se considera la versión autoritativa.

**5. Incentivos:**

*   **Recompensa de Bloque:** Los mineros que extraen con éxito un nuevo bloque son recompensados con una cierta cantidad de Bitcoin recién creados (actualmente 3.125 BTC, que se reduce a la mitad aproximadamente cada cuatro años en un evento llamado "halving").
*   **Tarifas de Transacción:** Los mineros también recaudan las tarifas de transacción que los usuarios incluyen voluntariamente al enviar Bitcoin. Estas tarifas incentivan a los mineros a priorizar ciertas transacciones.

**6. Descentralización y Seguridad:**

*   **Red Peer-to-Peer:** Bitcoin opera en una red peer-to-peer descentralizada, lo que significa que no hay una autoridad central que la controle. Las transacciones y los bloques se propagan a través de muchas computadoras en todo el mundo.
*   **Resistencia a la Censura:** Debido a que la blockchain está distribuida y requiere un poder computacional significativo para alterarla, es muy difícil para una sola entidad censurar transacciones o controlar la red.
*   **Seguridad a través de la Criptografía:** El uso de criptografía sólida garantiza la seguridad e integridad de las transacciones y de la blockchain. Las claves privadas permiten a los usuarios controlar su Bitcoin, y las firmas digitales evitan la manipulación de las transacciones. El mecanismo Proof-of-Work hace que sea computacionalmente costoso para los actores maliciosos reescribir el historial de transacciones.

**En resumen, la operación técnica de Bitcoin se basa en una interacción sofisticada de técnicas criptográficas, un libro mayor distribuido y transparente, y un mecanismo de consenso computacionalmente intensivo para garantizar seguridad, inmutabilidad y descentralización.**