---
audio: false
generated: false
image: true
lang: es
layout: post
title: Cómo Construir una Computadora
translated: true
type: post
---

![portada](assets/images/computer/cover.jpg)

## Video

<iframe width="100%" height="315" src="https://www.youtube.com/embed/fntYmAJasZ0" title="Reproductor de video de YouTube" frameborder="0" allow="acelerómetro; autoplay; escritura en portapapeles; medios cifrados; giroscopio; imagen en imagen; compartir web" allowfullscreen></iframe>

## Resumen Rápido

* Queremos construir una computadora para hacer aprendizaje automático. Compramos los componentes más recientes y asequibles hasta 2023 para armarla.
* Compramos componentes como el Intel Core i9-13900KF, la placa madre MSI MAG B760M Mortar y la tarjeta gráfica MSI Gaming GeForce RTX 4070, entre otros.
* La computadora no pudo encender. Pedimos ayuda a un experto dos veces. Una vez fue porque el conector de alimentación de la placa madre estaba suelto. La otra razón fue que el conector del botón de encendido del panel frontal estaba flojo.
* En nuestro caso, no necesitamos comprar soportes verticales para la GPU. Deberíamos analizar cuidadosamente la razón en lugar de comprar componentes adicionales para una solución rápida.
* Deberíamos colocar los cables en el otro lado de la caja de la computadora. Así, los cables no cubrirán la placa madre y podremos verla claramente.
* Deberíamos prestar más atención a la compatibilidad entre los componentes, especialmente entre la placa madre, la caja de la PC, la fuente de alimentación y otros componentes. Estos interactúan mucho entre sí.

## Principios

* Comparar globalmente, como JD.com en China, Rakuten en Japón, Amazon en EE. UU.
* Amazon tiene excelentes tablas para comparar productos de la misma serie.
* Encuentra la mejor introducción para aprender, revisa los comentarios negativos.
* Enfócate en dos artículos costosos, la CPU y la GPU.
* ¿Cuál es el mayor error posible en la decisión de compra?
* Visita el sitio web del fabricante para verificar los detalles.
* Verifica la compatibilidad de los artículos.
* Para las especificaciones de los artículos, nos familiarizaremos con ellas en el proceso.
* Podemos saltar entre el sitio web y los enlaces de referencia para aprender.
* Al elaborar un plan final, podemos conocer más y descubrir las preguntas críticas.
* Compra los mejores y más recientes productos cuyo precio puedas permitirte.
## Sitios web

* Francia, https://www.cdiscount.com
* Global, https://www.amazon.com
* Japón, https://www.rakuten.com
* China, https://jd.com
* Corea del Sur, https://www.coupang.com 
* Global, https://www.ebay.com
* Alemania, https://www.otto.de 
* Norteamérica, https://www.bestbuy.com

## Inicio

Esto es lo que encontré en la aplicación china Little Red Book.

* Tarjeta gráfica (GPU): MSI 3080 -- 5219 CNY  
* Placa base + CPU: ASUS Z790-P + i7-13700KF -- 4349 CNY  
* Unidad de estado sólido (SSD): Western Digital 1TB -- 448 CNY  
* Disco duro (HDD): Western Digital 2TB -- 338 CNY  
* Memoria RAM: Kingston 16GB*2 -- 598 CNY  
* Sistema de refrigeración: Thermaltake 360 Refrigeración líquida -- 334 CNY  
* Fuente de alimentación: Great Wall 85W -- 603 CNY  
* Gabinete: Aigo -- 264 CNY  
* Ratón + Teclado: 400 CNY  
* Monitor: Dell U2723QX -- 3600 CNY  
* Costo total aproximado: 16000 CNY

---

## Aprende y Compara

GPU (Unidad de Procesamiento Gráfico, por sus siglas en inglés) es un componente esencial en los sistemas modernos, especialmente para tareas que requieren un alto rendimiento gráfico o de procesamiento paralelo. A continuación, te dejo una breve explicación en español:

---

### ¿Qué es una GPU?

Una **GPU** (Graphics Processing Unit) es un procesador especializado diseñado para manejar operaciones gráficas y de cálculo en paralelo. A diferencia de la CPU (Unidad Central de Procesamiento), que está optimizada para tareas secuenciales, la GPU está diseñada para realizar múltiples operaciones simultáneamente, lo que la hace ideal para aplicaciones como:

- **Renderizado de gráficos**: Juegos, diseño 3D, animación.
- **Cálculos científicos**: Simulaciones, machine learning, análisis de datos.
- **Minería de criptomonedas**: Procesamiento intensivo de algoritmos.

---

### ¿Cómo funciona una GPU?

Las GPU están compuestas por miles de núcleos más pequeños y especializados en comparación con las CPU. Estos núcleos trabajan juntos para realizar operaciones en paralelo, lo que permite procesar grandes volúmenes de datos de manera eficiente. Por ejemplo, en el renderizado de imágenes, la GPU puede calcular el color de millones de píxeles al mismo tiempo.

---

### Aplicaciones comunes de las GPU

1. **Juegos**: Procesamiento de gráficos en tiempo real.
2. **Machine Learning**: Entrenamiento de modelos de inteligencia artificial.
3. **Diseño y animación**: Renderizado de escenas 3D complejas.
4. **Cálculos científicos**: Simulaciones físicas y matemáticas.

---

### Ejemplo de código usando GPU

Si estás trabajando con frameworks como **CUDA** (para NVIDIA) o **OpenCL**, puedes aprovechar la potencia de la GPU para acelerar tus cálculos. Aquí tienes un ejemplo básico en CUDA:

```cpp
__global__ void vectorAdd(int *A, int *B, int *C, int N) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < N) {
        C[idx] = A[idx] + B[idx];
    }
}

int main() {
    int N = 1000;
    int *A, *B, *C;
    // Asignar memoria en la GPU y copiar datos...
    vectorAdd<<<(N + 255) / 256, 256>>>(A, B, C, N);
    // Copiar resultados de vuelta a la CPU...
    return 0;
}
```

---

En resumen, las GPU son herramientas poderosas para tareas que requieren un alto rendimiento en procesamiento paralelo. Su uso se ha extendido más allá de los gráficos, convirtiéndose en un componente clave en áreas como la inteligencia artificial y la computación científica.

Amazon, Tarjeta Gráfica GIGABYTE GeForce RTX 3060 Gaming OC 12G (REV2.0), 3 Ventiladores WINDFORCE, 12GB GDDR6 de 192 bits, Tarjeta de Video GV-N3060GAMING OC-12GD

Amazon, Tarjeta gráfica MSI Gaming GeForce RTX 3080 LHR 10GB GDRR6X 320-Bit HDMI/DP Nvlink Torx Fan 4 RGB Arquitectura Ampere OC (RTX 3080 Gaming Z Trio 10G LHR) (Renovada)

Amazon, ASUS Dual GeForce RTX™ 4060 Ti OC Edition 8GB GDDR6 (PCIe 4.0, 8GB GDDR6, DLSS 3, HDMI 2.1, DisplayPort 1.4a, Diseño de Ventilador Axial-tech, Tecnología 0dB, y Más)

Amazon, MSI Gaming GeForce RTX 3080 LHR 12GB GDRR6X 384-Bit HDMI/DP Nvlink Torx Fan 3 Arquitectura Ampere OC Tarjeta Gráfica (RTX 3080 Ventus 3X Plus 12G OC LHR)

Amazon, MSI Gaming GeForce RTX 4070 12GB GDRR6X 192-Bit HDMI/DP Nvlink TORX Fan 4.0 Arquitectura Ada Lovelace Tarjeta Gráfica (RTX 4070 Ventus 3X 12G OC)

Amazon, MSI Gaming GeForce RTX 4070 12GB GDRR6X 192-Bit HDMI/DP Nvlink TORX Fan 4.0 Arquitectura Ada Lovelace Tarjeta Gráfica (RTX 4070 Gaming X Trio 12G)

---
Placa base
 
Amazon, ASUS ROG Strix B550-A Gaming AMD AM4 Zen 3 Ryzen 5000 y 3ra Gen Ryzen ATX Placa base para gaming (PCIe 4.0, LAN 2.5Gb, BIOS Flashback, Dual M.2 con disipadores, Cabezal RGB Direccionable Gen 2 y Aura Sync)

Amazon, MSI MAG B660 Tomahawk WiFi DDR4 Placa Base para Gaming (ATX, 12ª Generación de Intel Core, Socket LGA 1700, DDR4, PCIe 4, LAN 2.5G, Ranuras M.2, Wi-Fi 6)

Amazon, Placa base gaming MSI B760 Gaming Plus WiFi (Compatible con procesadores Intel de 12ª/13ª generación, LGA 1700, DDR5, PCIe 4.0, M.2, LAN de 2.5Gbps, USB 3.2 Gen2, Wi-Fi 6E, ATX)

Amazon, Placa base MSI MAG B760M Mortar WiFi para gaming (compatible con procesadores Intel de 12ª/13ª generación, LGA 1700, DDR5, PCIe 5.0, M.2, LAN de 2.5Gbps, USB 3.2 Gen2, Wi-Fi 6E, mATX)

Amazon, ASUS TUF Gaming Z790-Plus WiFi LGA 1700 (Intel® 12ª y 13ª Generación) Placa base ATX para gaming (PCIe 5.0, DDR5, 4 ranuras M.2, 16+1 DrMOS, WiFi 6, LAN 2.5Gb, USB 3.2 Gen 2 Tipo-C® frontal, Thunderbolt 4 (USB4), Aura RGB)

Amazon, ASUS Prime Z790-P WiFi LGA 1700 (Intel® 13th & 12th Gen) Placa base ATX (PCIe 5.0, DDR5, 14+1 etapas de potencia, 3X M.2, WiFi 6, Bluetooth v5.2, LAN 2.5Gb, Panel frontal USB 3.2 Gen 2 Tipo-C®, Thunderbolt™ 4/USB4)

---

CPU (Unidad Central de Procesamiento, por sus siglas en inglés) es el componente principal de una computadora responsable de ejecutar instrucciones de programas y procesar datos. Es el "cerebro" del sistema, encargado de realizar operaciones aritméticas, lógicas y de control.

Amazon, Intel Core i7-13700KF (Última Generación) Procesador para Escritorio Gaming de 16 núcleos (8 núcleos P + 8 núcleos E) - Desbloqueado,

Rakuten, Intel Core i7 13700KF BOX Procesador Intel Core i7 de 13ª generación sin GPU integrada CPU

JD.com, Intel Core Pentium CPU procesador para computadora de escritorio, caja original, 12ª generación i9-12900KF【16 núcleos y 24 hilos】, 3799 CNY.

Amazon, Intel Core i9-13900KF (Última Generación) Procesador para PC Gaming de 24 núcleos (8 núcleos P + 16 núcleos E) - Desbloqueado

---

Unidad de Estado Sólido (SSD)

Amazon, Western Digital 1TB WD Blue SN570 NVMe Unidad de Estado Sólido Interna SSD - Gen3 x4 PCIe 8Gb/s, M.2 2280, Hasta 3,500 MB/s - WDS100T3B0C

JD, 三星（SAMSUNG）1TB SSD固态硬盘 M.2接口(NVMe协议PCIe 4.0 x4) 980 PRO （MZ-V8P1T0BW）

Rakuten, Western Digital 1TB WD Green SSD Interno - Unidad de Estado Sólido - SATA III 6Gb/s 2.5/7mm, hasta 545MB/s - WDS100T3G0A

Walmart, WD Blue 1TB SA510 SATA Unidad de Estado Sólido Interna SSD - WDBB8H0010BNC-WRWN

Amazon, SAMSUNG 870 EVO SATA III SSD 1TB 2.5” Unidad de Estado Sólido Interna, Actualización de Memoria y Almacenamiento para PC o Laptop para Profesionales de TI, Creadores, Usuarios Cotidianos, MZ-77E1T0B/AM

Amazon, SAMSUNG 980 SSD 1TB PCle 3.0x4, NVMe M.2 2280, Unidad de Estado Sólido Interna, Almacenamiento para PC, Laptops, Juegos y Más, Tecnología HMB, Intelligent Turbowrite, Velocidades de hasta 3,500MB/s, MZ-V8V1T0B/AM

---

Disco Duro (HDD)

Amazon, Disco Duro Externo Portátil Seagate de 2TB HDD — USB 3.0 para PC, Mac, PlayStation y Xbox - Servicio de Rescate de 1 Año (STGX2000400)

Amazon, Disco Duro Externo de Escritorio WD My Book de 6TB, USB 3.0, HDD Externo con Protección por Contraseña y Software de Copia de Seguridad Automática - WDBBGB0060HBK-NESN

Amazon, Seagate ST8000DM008 BarraCuda 8TB Disco Duro Interno HDD – 3.5 Pulgadas SATA 6 Gb/s 5400 RPM 256MB de Caché para Computadora de Escritorio

JD.com, Western Digital Disco Duro para Escritorio WD Blue Disco Azul de Western Digital 4TB 5400 RPM 256MB SATA CMR

JD.com, Disco Duro para PC Seagate 2TB 7200 RPM 256MB SATA Disco Duro Mecánico Serie Seagate BarraCuda (ST2000DM008)

---

RAM (Memoria de Acceso Aleatorio)

Amazon, CORSAIR VENGEANCE DDR5 RAM 32GB (2x16GB) 5600MHz CL36 Intel XMP iCUE Compatible Memoria para Computadora - Negro (CMK32GX5M2B5600C36)

Amazon, Corsair VENGEANCE LPX DDR4 RAM 32GB (2x16GB) 3200MHz CL16 Intel XMP 2.0 Memoria para Computadora - Negro (CMK32GX4M2E3200C16)

Amazon, Samsung 16GB DDR4 3200MHz SODIMM PC4-25600 CL22 2Rx8 1.2V 260-Pin SO-DIMM Módulo de Memoria RAM para Portátiles y Notebooks M471A2K43DB1-CWE

Amazon, CORSAIR Vengeance DDR5 RAM 64GB (2x32GB) 6000MHz CL30 AMD Expo iCUE Compatible Memoria para Computadora - Gris (CMK64GX5M2B6000Z30)

JD.com, 美商海盗船（USCORSAIR） 64GB(32G×2)套装 DDR5 6000 台式机内存条 复仇者系列 游戏型 黑色

Traducción al español:

JD.com, 美商海盗船（USCORSAIR） Kit de 64GB (32G×2) DDR5 6000 para memoria de escritorio, serie Vengeance, tipo gaming, color negro.

---

Enfriador de Computadora

Amazon, ID-COOLING FROSTFLOW X 240 Enfriador de CPU por Agua AIO Cooler 240mm, Enfriador Líquido para CPU con LED Blanco, 2 Ventiladores PWM de 120mm, Compatible con Intel 1700/1200/115X, AMD AM5/AM4

Amazon, Thermalright Frozen Prism 240 Black ARGB Refrigeración Líquida para CPU con Ventilador ARGB PWM de 120 mm, Especificación de Fila Fría 240 Black, Refrigeración Líquida para Computadora compatible con AMD/AM4/AM5

Amazon, Thermalright Frozen Magic 240 Scenic V2 Refrigeración Líquida para CPU, 240 Fila de Enfriamiento en Blanco, 2×120mm Ventilador PWM, Cojinete S-FDB V2.0, Compatible con AMD/AM4/AM5, Intel 1700/1150/1151/1200/2066

JD.com, 大水牛（BUBALUS）Q6 CPU散热器（兼容AMD/多平台/9CM蓝光风扇/附带硅脂/台式电脑风冷散热器）

JD.com, Thermalright Frozen Prism 240

---

Fuente de Alimentación de Computadora

Amazon, Thermaltake SMART 600W ATX 12V V2.3/EPS 12V 80 Plus Certificado con PFC Activo Fuente de Alimentación PS-SPD-0600NPCWUS-W

Amazon, Thermaltake Toughpower GX1 RGB 600W Gold SLI/Crossfire Ready, Fuente de Alimentación Continua con LED RGB, ATX12V v2.4 / EPS v2.92, Certificación 80 Plus Gold, Garantía de 5 Años, Fuente de Alimentación No Modular, PS-TPD-0600NHFAGU-1

Amazon, Thermaltake Toughpower GF1 650W 80+ Gold SLI/CrossFire Ready, Ultra Silencioso, Ventilador de 140mm con Cojinete Hidráulico, Smart Zero Fan, Fuente de Alimentación Modular Completa, Garantía de 10 Años, PS-TPD-0650FNFAGU-1

Amazon, Corsair CX750F RGB, Fuente de alimentación de 750 vatios, 80 PLUS Bronze, Totalmente modular, RGB, color blanco

JD.com, Corsair CX650F RGB, Fuente de Alimentación de 750 Vatios, 80 PLUS, Totalmente Modular, RGB Blanco

---

Caja de PC

Amazon, SZSKYING Torre para PC Gaming con 10 Ventiladores ARGB, Torre para Computadora con Flujo de Aire 3.0 USB, Panel de Vidrio Templado y Control Remoto en Negro.

JD.com, Aigo Yogo M2

JD.com, Aigo Yueguang Baohe Jing Mini

## Referencia

Aprende sobre los diferentes Intel Cores.

Pregunta a ChatGPT:

¿Cuál es la diferencia entre los P-cores y los E-cores en los procesadores Intel?

Los procesadores Intel de 12ª generación (Alder Lake) y posteriores introdujeron una nueva arquitectura híbrida que combina dos tipos de núcleos: **P-cores** (Performance Cores) y **E-cores** (Efficient Cores). Estas son las principales diferencias entre ellos:

### 1. **P-cores (Performance Cores)**
   - **Diseño**: Están optimizados para un alto rendimiento en tareas de un solo hilo y multihilo.
   - **Velocidad**: Operan a frecuencias más altas, lo que los hace ideales para aplicaciones que requieren un gran poder de procesamiento, como juegos, edición de video o software de ingeniería.
   - **Tecnología**: Utilizan la arquitectura **Golden Cove** (en la 12ª generación) o **Raptor Cove** (en la 13ª generación), que ofrece mejoras en el rendimiento por ciclo de reloj (IPC).
   - **Hiperprocesamiento**: Los P-cores admiten **Hyper-Threading**, lo que permite ejecutar dos hilos simultáneamente por núcleo.
   - **Consumo de energía**: Consumen más energía en comparación con los E-cores, ya que están diseñados para maximizar el rendimiento.

### 2. **E-cores (Efficient Cores)**
   - **Diseño**: Están optimizados para la eficiencia energética y el manejo de tareas en segundo plano o de baja intensidad.
   - **Velocidad**: Operan a frecuencias más bajas, lo que reduce el consumo de energía y el calor generado.
   - **Tecnología**: Utilizan la arquitectura **Gracemont**, que está diseñada para maximizar la eficiencia en lugar del rendimiento bruto.
   - **Hiperprocesamiento**: Los E-cores **no admiten Hyper-Threading**, por lo que cada núcleo maneja un solo hilo.
   - **Consumo de energía**: Consumen menos energía, lo que los hace ideales para tareas como la reproducción de música, navegación web o gestión de procesos en segundo plano.

### 3. **Uso combinado**
   - Intel utiliza un **planificador de tareas** (Thread Director) en el sistema operativo para asignar automáticamente las tareas a los P-cores o E-cores según su intensidad. Por ejemplo:
     - Las tareas exigentes (juegos, renderizado) se asignan a los P-cores.
     - Las tareas ligeras (reproducción de música, actualizaciones en segundo plano) se asignan a los E-cores.
   - Este enfoque híbrido permite un equilibrio entre rendimiento y eficiencia energética, mejorando la duración de la batería en dispositivos portátiles y reduciendo el consumo de energía en equipos de escritorio.

### 4. **Ejemplo práctico**
   - Un procesador como el **Intel Core i7-12700K** tiene 8 P-cores y 4 E-cores, lo que permite un total de 20 hilos (8 P-cores con Hyper-Threading y 4 E-cores sin Hyper-Threading).
   - En tareas intensivas, los P-cores se activan para maximizar el rendimiento, mientras que los E-cores se encargan de las tareas menos exigentes para ahorrar energía.

En resumen, los **P-cores** están diseñados para ofrecer el máximo rendimiento en tareas exigentes, mientras que los **E-cores** priorizan la eficiencia energética en tareas ligeras. Juntos, permiten un equilibrio óptimo entre potencia y consumo de energía.

¿Cuál es la diferencia entre i9 y i7?

Los procesadores Intel Core i9 y i7 son dos de las líneas más populares de la marca, pero tienen diferencias clave que los distinguen. Aquí te explico las principales:

1. **Número de núcleos e hilos**:  
   - Los procesadores i9 suelen tener más núcleos e hilos que los i7. Por ejemplo, un i9 puede tener hasta 16 núcleos y 24 hilos, mientras que un i7 generalmente tiene entre 8 y 12 núcleos y hasta 16 hilos.  
   - Esto significa que el i9 es más adecuado para tareas intensivas como edición de video, renderizado 3D o streaming en vivo.

2. **Frecuencia y overclocking**:  
   - Los i9 suelen tener frecuencias base y turbo más altas que los i7, lo que los hace más rápidos en tareas de un solo núcleo.  
   - Además, los i9 suelen ser más eficientes en overclocking, lo que permite un mayor rendimiento si tienes un sistema de refrigeración adecuado.

3. **Caché**:  
   - Los i9 tienen una caché más grande que los i7, lo que mejora el rendimiento en aplicaciones que requieren acceso rápido a datos.

4. **Precio**:  
   - Los i9 son más caros que los i7 debido a su mayor rendimiento y características avanzadas.

5. **Uso recomendado**:  
   - **i7**: Ideal para usuarios que necesitan un buen rendimiento en multitarea, juegos y aplicaciones profesionales, pero sin llegar a los extremos de un i9.  
   - **i9**: Recomendado para profesionales que trabajan con cargas de trabajo intensivas, como diseño gráfico, edición de video, ingeniería o gaming de alto rendimiento.

En resumen, si buscas el máximo rendimiento y estás dispuesto a pagar más, el i9 es la mejor opción. Si buscas un equilibrio entre rendimiento y precio, el i7 es una excelente alternativa.

Si quieres hacer aprendizaje automático, ¿debería comprar el i7 o el i9?

La elección entre un procesador Intel Core i7 y un Core i9 depende de varios factores, como el tipo de tareas de aprendizaje automático que planeas realizar, tu presupuesto y otros componentes de tu sistema. Aquí hay algunas consideraciones:

1. **Rendimiento**: Los procesadores i9 generalmente ofrecen un mayor número de núcleos y subprocesos, lo que puede ser beneficioso para tareas intensivas en cómputo, como el entrenamiento de modelos de aprendizaje automático. Si planeas trabajar con grandes conjuntos de datos o modelos complejos, un i9 podría ser una mejor opción.

2. **Presupuesto**: Los i9 suelen ser más costosos que los i7. Si tu presupuesto es limitado, un i7 podría ser suficiente para muchas tareas de aprendizaje automático, especialmente si complementas tu sistema con una buena tarjeta gráfica (GPU).

3. **GPU**: En el aprendizaje automático, la GPU suele ser más importante que la CPU para el entrenamiento de modelos. Si planeas usar una GPU potente (como las de NVIDIA), la diferencia entre un i7 y un i9 podría ser menos significativa.

4. **Uso general**: Si además del aprendizaje automático, planeas usar tu computadora para otras tareas intensivas (como renderizado de video o desarrollo de software), un i9 podría ofrecer un mejor rendimiento general.

En resumen, si tu presupuesto lo permite y planeas realizar tareas de aprendizaje automático muy exigentes, un i9 podría ser la mejor opción. Sin embargo, si tu presupuesto es más ajustado o si complementas tu sistema con una buena GPU, un i7 podría ser suficiente para la mayoría de las tareas de aprendizaje automático.

---

El **Intel Core i9-13900** es uno de los procesadores más potentes de la serie 13ª generación de Intel, también conocida como **Raptor Lake**. Este procesador está diseñado para ofrecer un rendimiento excepcional en tareas exigentes, como gaming, edición de video, renderizado 3D y multitarea intensiva.

### Características clave:
- **Núcleos y subprocesos**: El i9-13900 cuenta con una arquitectura híbrida que combina núcleos de alto rendimiento (Performance Cores) y núcleos eficientes (Efficient Cores). En total, ofrece **24 núcleos (8 Performance + 16 Efficient)** y **32 subprocesos** gracias a la tecnología Hyper-Threading.
- **Frecuencias**: Tiene una frecuencia base de **2.0 GHz** en los núcleos Performance y **1.5 GHz** en los Efficient Cores, con una frecuencia turbo máxima de **5.8 GHz** en los núcleos más rápidos.
- **Memoria caché**: Incluye una caché L3 de **36 MB** y una caché L2 de **32 MB**, lo que mejora el rendimiento en aplicaciones que requieren acceso rápido a datos.
- **Tecnologías avanzadas**: Soporta tecnologías como **Intel Turbo Boost Max 3.0**, **Intel Thermal Velocity Boost**, y **Intel Deep Learning Boost** para optimizar el rendimiento en cargas de trabajo específicas.
- **Consumo energético**: Tiene un TDP (Thermal Design Power) base de **65 W**, pero puede alcanzar hasta **253 W** en modo turbo, lo que requiere un sistema de refrigeración robusto.
- **Socket**: Utiliza el socket **LGA 1700**, compatible con placas base Intel 600 y 700 series.

### Rendimiento:
El i9-13900 es ideal para usuarios que buscan el máximo rendimiento en aplicaciones profesionales y gaming de alta gama. Su arquitectura híbrida permite un equilibrio perfecto entre potencia y eficiencia energética, lo que lo convierte en una excelente opción para quienes necesitan un procesador versátil y potente.

Si estás considerando actualizar tu sistema o construir una PC de alto rendimiento, el **Intel Core i9-13900** es una opción destacada en el mercado actual.

https://cpu.userbenchmark.com/Compare/Intel-Core-i9-13900-vs-Intel-Core-i9-13900F/m1977296vsm1994287

---

¿Qué significa F en los procesadores Intel?

En los procesadores Intel, la letra **F** en el nombre del modelo indica que el procesador **no tiene gráficos integrados**. Esto significa que no incluye una GPU (Unidad de Procesamiento Gráfico) integrada en el chip, por lo que necesitarás una tarjeta gráfica dedicada para obtener salida de video.

Por ejemplo:
- **Intel Core i5-12400F**: Este procesador no tiene gráficos integrados.
- **Intel Core i5-12400**: Este procesador sí tiene gráficos integrados.

Los procesadores con la letra F suelen ser más económicos que sus contrapartes con gráficos integrados, lo que los hace populares entre los usuarios que planean usar una tarjeta gráfica dedicada de todos modos. Sin embargo, si no tienes una GPU dedicada, un procesador con la letra F no te permitirá ver nada en la pantalla.

Si tu procesador Intel® Core™ de escritorio incluye la letra F en el sufijo de la línea de productos, entonces necesitarás usar una tarjeta gráfica discreta en tu sistema. Si se utiliza el puerto de gráficos integrados en su lugar, el procesador no arrancará.

---

¿Es mejor Intel K o F?

Si tu procesador Intel tiene una K, significa que puede ser overclockeado y ha sido desbloqueado. La F indica que no tiene iGPU o gráficos integrados en el procesador. Los procesadores de la serie KF suelen ser más económicos que los procesadores K y generalmente no tienen iGPU.

---

https://versus.com/en/asus-prime-z790-p-d4-vs-msi-mag-b760m-mortar-max-wifi

---

¿Es compatible la GPU GeForce RTXTM 4070 GAMING X TRIO 12G con la fuente de alimentación Thermaltake Toughpower GF1 650W?

---

Aprende la descripción del producto cuidadosamente, como esta.

ASUS TUF Gaming Z790-Plus WiFi LGA 1700.

* Socket Intel LGA 1700: Compatible con procesadores Intel Core de 12ª y 13ª generación, soporta PCIe 5.0, DDR5 y listo para Windows 11 de fábrica.
* Solución de energía mejorada: 16+1 DrMOS, conectores ProCool, componentes TUF de grado militar y Digi+ VRM para máxima durabilidad y rendimiento.
* Enfriamiento integral: Disipador de calor para VRM, disipador pasivo para PCH, disipador para M.2, cabezales de ventilador híbridos y utilidad Fan Xpert 4.
* Red de juegos ultrarrápida: WiFi 6 AX201 (802.11 ax), LAN Intel I225-V 2.5Gb, TUF LANGuard y tecnología TurboLAN.
* Conectividad más rápida: 4x M.2/NVMe SSD, cabezal frontal USB 3.2 Gen 2 Tipo-C, USB Gen 2x2 Tipo-C y cabezal Thunderbolt 4 (USB4).
* Amigable para ensamblaje de PC: SafeDIMM, PCIe 5.0 Safeslot, Q-LED, M.2 Q-Latch, escudo I/O premontado.
* Nueva estética TUF Gaming: Nuevo diseño de identidad, efectos LED sincronizables en una amplia gama de equipos de PC compatibles, incluyendo tiras RGB direccionables con Aura Sync.
* Audio inmersivo para juegos y cancelación de ruido AI: El códec Realtek S1200A ofrece una calidad de audio prístina para sumergirte más en la acción del juego o mejorar tus pistas de música o videos favoritos. Comunícate claramente con la tecnología ASUS AI Noise Canceling Mic.

---

https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/

https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/

---

https://www.msi.com/Graphics-Card/GeForce-RTX-4070-GAMING-X-TRIO-12G/Specification

https://www.intel.com/content/www/us/en/products/sku/230497/intel-core-i913900kf-processor-36m-cache-up-to-5-80-ghz/specifications.html

https://www.msi.com/Motherboard/MAG-B760M-MORTAR-WIFI

https://www.thermaltake.com/toughpower-gf1-650w-tt-premium-edition.html

https://file.thermaltake.com/file/qig/Connect_PCIe_Cables_to_High_Power_Consumption_GPU_en.pdf, ¿Cómo conectar correctamente los cables PCIe a tarjetas gráficas de alto consumo de energía?

https://www.whatpsu.com/psu/cpu/Intel-Core-i9-13900K/gpu/NVIDIA-GeForce-RTX-4070-Ti

(Nota: La URL no necesita traducción, ya que es un enlace directo a un sitio web en inglés que proporciona información sobre componentes de hardware como el procesador Intel Core i9-13900K y la tarjeta gráfica NVIDIA GeForce RTX 4070 Ti.)

https://pcpartpicker.com/forums/topic/359090-what-is-this-8-pin-connector-on-my-hard-drive, ¿Qué es este conector de 8 pines en mi disco duro?
## Selección Final

De JD.com.

CPU, Intel Core i9-13900KF (última generación) Procesador para escritorio de gaming, 24 núcleos (8 núcleos P + 16 núcleos E) - Desbloqueado, 4709 CNY.

Placa base, MSI MAG B760M Mortar WiFi Gaming Motherboard (compatible con procesadores Intel de 12ª/13ª generación, LGA 1700, DDR5, PCIe 5.0, M.2, LAN de 2.5Gbps, USB 3.2 Gen2, Wi-Fi 6E, mATX), 1299 CNY

GPU, MSI Gaming GeForce RTX 4070 12GB GDRR6X 192-Bit HDMI/DP Nvlink TORX Fan 4.0 Arquitectura Ada Lovelace Tarjeta Gráfica (RTX 4070 Gaming X Trio 12G), 5199 CNY

SSD, SAMSUNG 980 SSD 1TB PCle 3.0x4, NVMe M.2 2280, Unidad de estado sólido interna, Almacenamiento para PC, portátiles, juegos y más, Tecnología HMB, Intelligent Turbowrite, Velocidades de hasta 3,500 MB/s, MZ-V8V1T0B/AM, 399 CNY

HDD, Disco Duro Interno Western Digital 2TB WD Blue PC - Clase 7200 RPM, SATA 6 Gb/s, 256 MB de Caché, 3.5" - WD20EZBX, 428 CNY

RAM, CCORSAIR Vengeance DDR5 RAM 64GB (2x32GB) 6000MHz CL30 AMD Expo iCUE Compatible Memoria para Computadora - Gris (CMK64GX5M2B6000Z30), 1379 CNY

Cooler, Thermalright Frozen Prism 240 White ARGB AIO Water Cooler, Refrigeración Líquida para CPU, Sistema de Refrigeración por Agua con 2 Ventiladores PWM de 120mm, 1850 RPM de Alta Velocidad, Compatible con AMD/AM4/AM5 e Intel LGA1150/1151/1200/2011/1700, 413 CNY

Fuente de alimentación, Corsair CX650F RGB, 750 vatios, 80 PLUS, Fuente de alimentación modular RGB blanca, 398 CNY

Caja para PC, Aigo Yueguangbaohe Jing Mini, 299 CNY

Cable SATA, Cable Matters Paquete de 3 Cables SATA de 90 Grados en Ángulo Recto de 18 Pulgadas (Cable SATA III de 6.0 Gbps, Cable SATA para SSD, Cable SSD SATA, Cables SATA 3) Negro, 19 CNY

Ratón, Teclado, Monitor: Ya tengo los adicionales en mi casa.

Total: alrededor de 14000 CNY

Esta es simplemente mi decisión final considerando lo que sé y mi presupuesto. Por favor, haz tu propia investigación también.

## Guía de Instalación

http://intel.cn/ProcessorInstall

https://www.intel.cn/content/www/cn/zh/support/articles/000088402/processors.html

Cómo Configurar las Fuentes de Alimentación CORSAIR CX-F RGB Series

[https://youtu.be/XFOOk2LQIWQ](https://youtu.be/XFOOk2LQIWQ)

Tutorial de Ensamblaje de PC (Versión Completa) - MSI

[https://youtu.be/qCPIEYfN_hc](https://youtu.be/qCPIEYfN_hc)  
Guía de instalación del enfriador de CPU THERMALRIGHT FROZEN PRISM para Intel LGA1700 y AMD AM4 AM5

[https://youtu.be/o233hhC-dU8](https://youtu.be/o233hhC-dU8)

MSI® CÓMO instalar los conectores del panel frontal (JFP1)

[https://youtu.be/DPELIdVNZUI](https://youtu.be/DPELIdVNZUI)

Dónde conectar los cables de la caja del PC, cables de alimentación y más - consejos de cableado para computadoras

[https://youtu.be/RYkW2WywN5I](https://youtu.be/RYkW2WywN5I)

¡La instalación de la tarjeta gráfica es realmente sencilla! Solo cuatro pasos simples, especialmente preparados para principiantes (Xiaobai).

[https://www.bilibili.com/video/BV1tx411J7F1/?spm_id_from=888.80997.embed_other.whitelist&t=12&vd_source=89dab4a438fbb42994ef16c0af4d4e91](https://www.bilibili.com/video/BV1tx411J7F1/?spm_id_from=888.80997.embed_other.whitelist&t=12&vd_source=89dab4a438fbb42994ef16c0af4d4e91)
## Información de la BIOS

Información de la CPU:

![cpu](assets/images/computer/cpu.jpg)

También hay información sobre el ventilador, la memoria y el almacenamiento.

## Instalar el Sistema Operativo

Sitio Oficial de Ubuntu

[https://ubuntu.com/](https://ubuntu.com/)

Un entorno de Machine Learning con Ubuntu y aceleración por GPU en 5 pasos

[https://medium.com/@bbloks/a-machine-learning-environment-with-ubuntu-and-gpu-acceleration-in-5-steps-765608325356](https://medium.com/@bbloks/a-machine-learning-environment-with-ubuntu-and-gpu-acceleration-in-5-steps-765608325356)

Crear una memoria USB de arranque en macOS

[https://ubuntu.com/tutorials/create-a-usb-stick-on-macos#4-install-and-run-etcher](https://ubuntu.com/tutorials/create-a-usb-stick-on-macos#4-install-and-run-etcher)

Instalar Ubuntu Desktop

[https://ubuntu.com/tutorials/install-ubuntu-desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop)

## Reflexión

Deberíamos colocar los cables en el otro lado de la caja de la computadora. Así, los cables no cubrirán la placa madre y podremos verla claramente.

Deberíamos consultar con el servicio de atención al cliente de los productos con anticipación para obtener toda la información útil, como videos de instalación. Prefieren subir videos largos en plataformas de video grandes en lugar de mostrarlos en plataformas de comercio electrónico.

Le preguntamos a un experto dos veces para verificar por qué nuestra computadora no podía arrancar. Una razón es que el conector de alimentación de la placa madre está suelto. La otra razón es que el conector del botón de encendido del panel frontal está suelto.

Cuando pedimos a los especialistas que nos ayuden, necesitamos hacerlo nosotros mismos para aprender. Ellos solo deben guiarnos. De lo contrario, olvidaremos fácilmente y no sabremos qué hacer cuando nos enfrentemos a problemas la próxima vez.

No necesitamos comprar soportes verticales para GPU en nuestro caso, como este [soporte](https://a.co/d/1ieE5kd). En lugar de comprar componentes adicionales para una solución rápida, deberíamos analizar cuidadosamente.

Debemos prestar más atención a la compatibilidad entre los componentes, especialmente entre la placa base, la caja de la PC, la fuente de alimentación y otros componentes. Estos interactúan mucho con otros elementos.

## Actualización

Lamento no haber optado por una tarjeta gráfica más grande, ya que los 12 GB de VRAM han demostrado ser insuficientes para mis necesidades.