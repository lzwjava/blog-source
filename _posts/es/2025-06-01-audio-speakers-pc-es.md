---
audio: false
generated: true
lang: es
layout: post
title: Conectar Altavoces a la PC
translated: true
type: note
---

Para conectar altavoces de audio a tu computadora utilizando la salida RCA (o "RS out") de la placa base, sigue estos pasos. Ten en cuenta que la placa base MSI MAG B760M Mortar WiFi típicamente no tiene salidas RCA directamente, ya que la mayoría de las placas base modernas utilizan conectores de audio de 3.5mm o HDMI para la salida de audio. Sin embargo, asumiré que te refieres a la salida de audio de la placa base (probablemente un conector de 3.5mm etiquetado para altavoces traseros o line-out) o a un adaptador/conversor RCA.

### Pasos para conectar altavoces de audio con salida RCA:

1.  **Identificar la salida de audio en la placa base**:
    - Revisa el panel posterior de E/S de tu placa base MSI MAG B760M Mortar WiFi. Típicamente tiene múltiples conectores de audio de 3.5mm, incluyendo uno verde (line-out) para altavoces estéreo o una salida para centro/subwoofer (naranja) para configuraciones de sonido envolvente.
    - Si tus altavoces tienen entradas RCA (conectores rojo y blanco), probablemente necesitarás un adaptador o conversor.

2.  **Verificar los requisitos de los altavoces**:
    - Confirma si tus altavoces son **activos** (con amplificador incorporado) o **pasivos** (que requieren un amplificador externo).
        - **Altavoces activos**: Pueden conectarse directamente a la salida de audio de la placa base con el cable o adaptador correcto.
        - **Altavoces pasivos**: Requieren un amplificador o receptor externo con entradas RCA.

3.  **Conseguir el cable/adaptador correcto**:
    - Si tus altavoces tienen entradas RCA, necesitarás un **cable de 3.5mm a RCA** o un adaptador:
        - **Cable macho de 3.5mm a macho RCA**: Conecta el conector de line-out verde de 3.5mm de la placa base (u otra salida de audio designada) a las entradas RCA de tus altavoces o amplificador.
        - **Adaptador hembra de 3.5mm a macho RCA**: Si ya tienes un cable RCA, puedes usar un adaptador hembra de 3.5mm a macho RCA.
    - Producto de ejemplo: Un cable de 3.5mm a RCA (similar al cable SATA de Cable Matters que listaste, pero para audio). Estos están ampliamente disponibles por 10-50 CNY en JD.com.

4.  **Conectar los altavoces**:
    - **Para altavoces activos**:
        - Enchufa el extremo de 3.5mm del cable en el conector de line-out verde en el panel posterior de E/S de la placa base.
        - Conecta los extremos RCA (rojo y blanco) a las entradas RCA correspondientes en tus altavoces.
        - Enciende los altavoces y asegúrate de que su volumen esté subido.
    - **Para altavoces pasivos**:
        - Conecta el extremo de 3.5mm al conector de line-out de la placa base.
        - Enchufa los extremos RCA en las entradas RCA de un amplificador o receptor externo.
        - Conecta los altavoces pasivos a los terminales de altavoz del amplificador (generalmente mediante cable de altavoz, no RCA).
        - Enciende el amplificador y ajusta su configuración.

5.  **Configurar los ajustes de audio**:
    - Enciende tu computadora y asegúrate de que los altavoces estén encendidos.
    - En Windows:
        - Haz clic derecho en el icono del altavoz en la bandeja del sistema y selecciona **Sonidos** o **Configuración de sonido**.
        - En la pestaña **Reproducción**, selecciona el dispositivo de salida (ej. "Altavoces" o "Realtek Audio") y establécelo como predeterminado.
        - Si usas sonido envolvente, ve a **Propiedades > Avanzado** y configura la configuración de altavoces (ej. estéreo o surround 5.1).
    - Instala los últimos **Controladores de Audio Realtek** para tu placa base MSI desde el sitio web oficial de MSI o JD.com si aún no están instalados, para garantizar un rendimiento de audio óptimo.

6.  **Probar el audio**:
    - Reproduce audio (ej. música o un video) para verificar la salida de sonido.
    - Ajusta los niveles de volumen en los altavoces, el amplificador (si se usa) y en Windows.
    - Si no hay sonido, verifica:
        - Que las conexiones del cable estén seguras.
        - Que el dispositivo de reproducción correcto esté seleccionado en Windows.
        - Que la salida de audio de la placa base esté habilitada en el BIOS (rara vez está deshabilitada, pero revisa la configuración del BIOS de MSI en **Advanced > Integrated Peripherals** si es necesario).

### Notas:
- **Audio de la Placa Base**: La MSI MAG B760M Mortar WiFi utiliza un chipset de audio Realtek, que admite salida de audio de alta calidad a través de conectores de 3.5mm. Las salidas RCA no son estándar, por lo que es probable que estés usando un adaptador o te refieras al conector de line-out.
- **Salidas Alternativas**:
    - Si tus altavoces admiten HDMI u óptico (S/PDIF), tu placa base también tiene una salida óptica S/PDIF o HDMI (a través de la GPU para video+audio). Verifica si tus altavoces o amplificador admiten estos para una posible mejor calidad de audio.
    - Las salidas HDMI/DisplayPort de la GPU RTX 4070 pueden transmitir audio a un monitor o receptor con altavoces, si lo prefieres.
- **Costo**: Un cable o adaptador de 3.5mm a RCA es económico (10-50 CNY en JD.com). Asegúrate de que admita audio (no solo datos, como tu cable SATA).
- **Sonido Envolvente**: Si tus altavoces son parte de una configuración 5.1 o 7.1, utiliza los conectores de 3.5mm adicionales (ej. naranja para centro/subwoofer, negro para traseros) y configúralos en Windows.

Si aclaras el modelo de los altavoces o si estás usando un amplificador, puedo proporcionar una guía más específica. Si te referías a una "RS out" diferente (ej. un puerto o dispositivo específico), por favor proporciona detalles y ajustaré las instrucciones.