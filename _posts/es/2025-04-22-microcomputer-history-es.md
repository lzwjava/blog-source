---
audio: false
generated: true
lang: es
layout: post
title: Historia del Microordenador
translated: true
type: note
---

El curso **Microcomputer and Interface Technology**, según se describe, se centra en la arquitectura, programación e interfaz de los sistemas de microcomputadoras, con un énfasis particular en los microprocesadores Intel 8086/8088 y las tecnologías de interfaz relacionadas (por ejemplo, los chips 8255, 8253, 8251). Para proporcionar una historia completa, rastrearé los orígenes y la evolución de las tecnologías clave cubiertas en el curso, identificaré las figuras clave y las empresas detrás de su desarrollo, y exploraré las historias detrás de su creación. Esto incluye la microcomputadora en sí, los microprocesadores 8086/8088, la programación en lenguaje ensamblador, los sistemas de memoria, las tecnologías de interfaz de E/S y los estándares de bus.

---

### **1. La Microcomputadora: Orígenes y Evolución**

#### **¿Qué es una Microcomputadora?**
Una microcomputadora es una computadora pequeña y asequible construida alrededor de un microprocesador, que integra CPU, memoria y capacidades de E/S. El curso comienza con una descripción general de los sistemas de microcomputadoras, basados en la **arquitectura Von Neumann** (una CPU, memoria para instrucciones y datos, y E/S conectada a través de buses).

#### **Historia y Descubrimiento**
- **Antes de los años 70: Fundamentos**
  - El concepto de una computadora programable se remonta a la Máquina Analítica de **Charles Babbage** (década de 1830), aunque nunca se construyó. El trabajo teórico de **Alan Turing** (1936) y el informe de 1945 de **John von Neumann** sobre el EDVAC formalizaron la computadora de programa almacenado, donde las instrucciones y los datos comparten memoria. Esta **arquitectura Von Neumann** se convirtió en el plano para las microcomputadoras.
  - Las primeras computadoras (por ejemplo, ENIAC, 1945) eran masivas y utilizaban tubos de vacío. La invención del **transistor** (1947, **John Bardeen**, **Walter Brattain**, **William Shockley** en Bell Labs) y del **circuito integrado** (1958, **Jack Kilby** en Texas Instruments y **Robert Noyce** en Fairchild) permitió la electrónica compacta.

- **1971: El Primer Microprocesador**
  - **¿Quién lo Descubrió?**: **Intel**, específicamente los ingenieros **Federico Faggin**, **Ted Hoff** y **Stan Mazor**, desarrollaron el **Intel 4004**, el primer microprocesador, lanzado en noviembre de 1971.
  - **Historia**: Encargado por la empresa japonesa de calculadoras Busicom, a Intel se le encomendó el diseño de un chip para una calculadora programable. Ted Hoff propuso un único chip de propósito general en lugar de múltiples chips especializados, reduciendo costos y complejidad. Federico Faggin dirigió el diseño, comprimiendo 2,300 transistores en un procesador de 4 bits (740 kHz, bus de direcciones de 12 bits). El 4004 podía ejecutar 60,000 instrucciones por segundo, un salto para su época.
  - **Impacto**: El 4004 impulsó la calculadora Busicom 141-PF e inspiró a Intel a comercializarlo como un procesador de propósito general, dando origen a la industria del microprocesador.

- **Años 70: Aparición de la Microcomputadora**
  - **1974**: El **8080** de Intel (8 bits, 2 MHz) impulsó el **Altair 8800** (1975, MITS), la primera microcomputadora comercialmente exitosa. Comercializado como un kit para aficionados, ejecutaba **CP/M** (un sistema operativo temprano) e inspiró a **Bill Gates** y **Paul Allen** a fundar Microsoft, escribiendo un intérprete de BASIC para él.
  - **1977**: El **Apple II** (Steve Wozniak, Steve Jobs), **Commodore PET** y **TRS-80** hicieron las microcomputadoras accesibles para los consumidores, con teclados, pantallas y software.
  - **Historia**: El éxito del Altair se debió a su diseño abierto y a la cobertura en *Popular Electronics*. Los aficionados formaron clubes (por ejemplo, Homebrew Computer Club), fomentando la innovación. El diseño del Apple II de Wozniak priorizó la asequibilidad y la usabilidad, utilizando el procesador MOS 6502.

- **Contexto del Curso**: El curso se centra en el **Intel 8086/8088**, introducido en 1978, que impulsó la **IBM PC** (1981), estandarizando las microcomputadoras para uso empresarial y doméstico.

#### **Figuras Clave**
- **Federico Faggin**: Dirigió el diseño del 4004, luego cofundó Zilog (procesador Z80).
- **Ted Hoff**: Concibió el concepto de microprocesador.
- **Robert Noyce y Gordon Moore**: Fundadores de Intel, impulsaron el desarrollo de CI y microprocesadores.
- **Ed Roberts**: Fundador de MITS, creador del Altair 8800.

---

### **2. El Microprocesador Intel 8086/8088**

#### **¿Qué es?**
El 8086 (16 bits, 5-10 MHz) y el 8088 (bus externo de 8 bits) son microprocesadores centrales para el curso, conocidos por su modelo de memoria segmentado, espacio de direcciones de 1 MB y arquitectura x86, que sigue siendo dominante hoy en día.

#### **Historia y Descubrimiento**
- **1976-1978: Desarrollo**
  - **¿Quién lo Descubrió?**: El equipo de Intel, dirigido por **Stephen Morse** (arquitectura y conjunto de instrucciones), **Bruce Ravenel** (microcódigo) y **Jim McKevitt** (gestión del proyecto), diseñó el 8086, lanzado en junio de 1978. El 8088 siguió en 1979.
  - **Historia**: Intel pretendía superar a los procesadores de 8 bits (por ejemplo, 8080, Z80) para competir en un mercado en crecimiento. El 8086 fue diseñado como un procesador de 16 bits con un bus de direcciones de 20 bits, soportando 1 MB de memoria (frente a 64 KB para los chips de 8 bits). Su conjunto de instrucciones era compatible con el 8080, facilitando las transiciones de software. El 8088, con un bus externo de 8 bits, redujo el costo del sistema, haciéndolo atractivo para IBM.
  - **Desafíos**: La complejidad del 8086 (29,000 transistores) llevó al límite la fabricación de Intel. Su modelo de memoria segmentado (segmentos de 64 KB, direccionamiento por desplazamiento) fue un compromiso para equilibrar el rendimiento y la compatibilidad.

- **1981: Adopción de la IBM PC**
  - **Historia**: IBM, al ingresar al mercado de las PC, eligió el 8088 para su **IBM PC** (modelo 5150) debido a su rentabilidad y al soporte de Intel. La decisión fue influenciada por el equipo de **Bill Lowe** en el laboratorio de IBM en Boca Raton, que priorizó una arquitectura abierta utilizando componentes estándar. El 8088 funcionaba a 4.77 MHz, y el éxito de la PC estandarizó la arquitectura x86.
  - **Impacto**: El diseño abierto de la IBM PC permitió los clones (por ejemplo, Compaq, Dell), impulsando la industria de las PC. **MS-DOS** de Microsoft, desarrollado para la PC, se convirtió en el sistema operativo dominante.

- **Legado**: La arquitectura x86 evolucionó a través del 80286 (1982), 80386 (1985) y los procesadores modernos.

#### **Figuras Clave**
- **Stephen Morse**: Arquitecto principal del 8086.
- **Bill Lowe**: Líder del equipo de IBM que eligió el 8088 para la PC.
- **Intel Team**: Morse, Ravenel, McKevitt y otros.

---

### **3. Programación en Lenguaje Ensamblador**

#### **¿Qué es?**
El lenguaje ensamblador es un lenguaje de programación de bajo nivel que se corresponde directamente con las instrucciones de la máquina. El curso enseña ensamblador para el 8086/8088, cubriendo instrucciones, segmentación y depuración.

#### **Historia y Descubrimiento**
- **Años 1940-1950: Orígenes**
  - Los primeros lenguajes de programación eran código máquina (binario). **Kathleen Booth** (1947) a menudo se le atribuye la escritura del primer ensamblador para la ARC2 en Birkbeck College.
  - **Historia**: Los ensambladores traducen mnemónicos (por ejemplo, `MOV`, `ADD`) a código máquina, haciendo la programación más legible para los humanos. Los primeros sistemas como EDSAC (1949) utilizaban un ensamblador primitivo.

- **Años 1970-1980: Ensamblador para Microprocesadores**
  - Con el Intel 4004, el ensamblador se volvió crucial para programar microprocesadores. Intel proporcionó herramientas como el ensamblador ASM86 para el 8086.
  - **Historia**: El ensamblador del 8086 introdujo conceptos como segmentación (CS, DS, SS, ES) para manejar el espacio de direcciones de 1 MB. Los programadores usaban editores de texto y ensambladores en sistemas de desarrollo (a menudo ejecutándose en minicomputadoras o microcomputadoras más grandes).

- **Contexto del Curso**: Los estudiantes aprenden a programar el 8086 usando ensamblador, enfocándose en la manipulación de registros, aritmética y control de E/S.

#### **Figuras Clave**
- **Kathleen Booth**: Pionera en lenguajes ensambladores.
- **Intel Engineers**: Desarrollaron ASM86 y herramientas relacionadas.

---

### **4. Sistemas de Memoria**

#### **¿Qué es?**
La memoria almacena instrucciones y datos. El curso cubre RAM, ROM y técnicas de expansión de memoria para sistemas 8086.

#### **Historia y Descubrimiento**
- **Años 1940-1950: Memoria Temprana**
  - Las primeras memorias usaban líneas de retardo de mercurio o tubos Williams. La **memoria de núcleo magnético** (1947, **An Wang**; perfeccionada por **Jay Forrester** para Whirlwind, 1953) fue la RAM dominante hasta los años 70.
  - **Historia**: La memoria de núcleo era no volátil pero costosa de fabricar.

- **Años 1970: Memoria de Semiconductores**
  - **Intel**: Desarrolló la primera DRAM comercial, el **Intel 1103** (1970), basado en el trabajo de **Robert Dennard** en IBM (inventor de la DRAM de una celda de transistor, 1966).
  - **Historia**: La DRAM almacenaba bits en condensadores, requiriendo actualización periódica. La RAM estática (SRAM) era más rápida pero más costosa.
  - **ROM**: Almacenaba firmware, con variantes como **EPROM** (borrable mediante luz UV, George Perlegos, 1971) y **EEPROM** (eléctricamente borrable, Eli Harari, 1977).
  - **Contexto del Curso**: El curso cubre la expansión de memoria (por ejemplo, decodificación de direcciones), crítica para sistemas 8086 con espacios de direcciones de 1 MB.

#### **Figuras Clave**
- **Robert Noyce**: Coinventó del CI, permitiendo chips de memoria densos.
- **Ted Hoff**: Diseños tempranos de DRAM en Intel.
- **Dov Frohman**: Inventó la EPROM en Intel.

---

### **5. Tecnología de E/S e Interfaz**

#### **¿Qué es?**
Las interfaces de E/S conectan la CPU a los periféricos (por ejemplo, teclados, impresoras). El curso cubre **8255A** (paralelo), **8253/8254** (temporizador), **8251A** (serial) y sistemas de interrupciones (por ejemplo, **8259A**).

#### **Historia y Descubrimiento**
- **Años 70: Necesidad de E/S**
  - Las primeras microcomputadoras usaban puertos de E/S simples, pero los periféricos exigían chips especializados. Intel desarrolló una familia de controladores periféricos para el 8080 y 8086.
  - **Historia**: A medida que las microcomputadoras se volvían complejas, el control directo de E/S por la CPU se volvió ineficiente. Los chips periféricos de Intel descargaban tareas, mejorando el rendimiento.

- **8255A Interfaz Periférica Programable (1977)**
  - **¿Quién?**: Intel, diseñado para sistemas 8080/8086.
  - **Historia**: El 8255A proporcionaba tres puertos de 8 bits, configurables en modos para E/S básica, E/S con *strobe* o transferencias bidireccionales. Simplificó la interfaz con dispositivos como teclados y pantallas, convirtiéndose en un elemento básico en las PC.
  - **Impacto**: Se utilizó en puertos paralelos de IBM PC (por ejemplo, impresoras).

- **8253/8254 Temporizador de Intervalo Programable (1977/1982)**
  - **¿Quién?**: Intel, evolucionó de diseños de temporizadores anteriores.
  - **Historia**: El 8253 ofrecía tres contadores de 16 bits para temporización (por ejemplo, relojes del sistema) o conteo (por ejemplo, medición de pulsos). El 8254 mejoró la confiabilidad. Se usó en altavoces de PC, actualización de DRAM y relojes en tiempo real.
  - **Impacto**: Esencial para las funciones de temporización de la PC.

- **8251A Interfaz Serial (1976)**
  - **¿Quién?**: Intel, para comunicación serial.
  - **Historia**: El 8251A manejaba protocolos asíncronos (por ejemplo, RS-232) y síncronos, permitiendo módems y terminales. Fue crítico para las primeras redes.
  - **Impacto**: Impulsó los puertos seriales de PC (puertos COM).

- **8259A Controlador de Interrupciones (1979)**
  - **¿Quién?**: Intel, diseñado para sistemas basados en interrupciones.
  - **Historia**: El 8259A gestionaba hasta 8 fuentes de interrupción, con cascada para más, permitiendo que los periféricos señalaran a la CPU de manera eficiente. Fue integral para el sistema de interrupciones de la IBM PC.
  - **Impacto**: Estandarizó el manejo de interrupciones en las PC.

- **Modos de Transferencia de Datos**
  - **E/S Controlada por Programa**: La CPU sondeaba dispositivos, simple pero lento.
  - **Basada en Interrupciones**: Los periféricos activaban interrupciones, enseñado en el curso a través del 8259A.
  - **DMA**: El controlador DMA **Intel 8237** (1980) permitía transferencias de alta velocidad, utilizado en controladores de disco.

#### **Figuras Clave**
- **Ingenieros de Intel**: Equipos anónimos diseñaron estos chips, construyendo sobre los ecosistemas 8080/8086.
- **Gary Kildall**: El sistema operativo CP/M aprovechó estos chips, influyendo en los estándares de E/S de PC.

---

### **6. Buses y Expansión**

#### **¿Qué es?**
Los buses estandarizan la comunicación CPU-memoria-periféricos. El curso cubre **ISA**, **PCI** e interfaces modernas (**USB**, **SPI**, **I²C**).

#### **Historia y Descubrimiento**
- **Años 70: Buses Tempranos**
  - El **bus S-100** (1975, Ed Roberts, MITS) fue un estándar temprano para sistemas tipo Altair, adoptado por aficionados.
  - **Historia**: La apertura del S-100 fomentó un ecosistema de microcomputadoras pero carecía de estandarización.

- **1981: Bus ISA**
  - **¿Quién?**: IBM, para la IBM PC.
  - **Historia**: Diseñado para el 8088, el bus ISA (Arquitectura Estándar Industrial) admitía tarjetas de 8 bits (PC) y 16 bits (PC/AT). Su simplicidad y el dominio del mercado de IBM lo convirtieron en un estándar, aunque lento (8 MHz).
  - **Impacto**: Se utilizó para tarjetas de expansión (por ejemplo, sonido, gráficos) hasta la década de 1990.

- **1992: Bus PCI**
  - **¿Quién?**: Intel, con contribuciones de IBM y Compaq.
  - **Historia**: PCI (Interconexión de Componentes Periféricos) abordó las limitaciones de ISA, ofreciendo velocidad de 33 MHz, rutas de datos de 32 bits y plug-and-play. Se convirtió en el estándar para las PC de la década de 1990.
  - **Impacto**: Evolucionó a PCIe, utilizado hoy en día.

- **Interfaces Modernas**
  - **USB (1996)**: Desarrollado por un consorcio (Intel, Microsoft, Compaq, etc.), dirigido por **Ajay Bhatt** en Intel. USB unificó las conexiones periféricas con conexión en caliente y escalabilidad (1.5 Mbps a 480 Mbps para USB 2.0).
  - **SPI (década de 1980)**: Bus serial de Motorola para comunicación de alta velocidad y corta distancia (por ejemplo, tarjetas SD).
  - **I²C (1982)**: Bus de dos hilos de Philips para periféricos de baja velocidad (por ejemplo, sensores).
  - **Historia**: USB surgió de la necesidad de un conector universal, reemplazando puertos seriales/paralelos. SPI e I²C fueron diseñados para sistemas embebidos, simplificando la comunicación entre chips.

#### **Figuras Clave**
- **Ajay Bhatt**: Arquitecto principal de USB.
- **Ingenieros de IBM**: Definieron ISA para la PC.
- **Equipos de Intel**: Impulsaron los estándares PCI y USB.

---

### **Contexto del Curso y el Instructor**

- **Yang Quansheng**: Existe poca información pública sobre el instructor, probablemente un profesor o ingeniero especializado en ingeniería informática. El enfoque del curso en los chips 8086 e Intel sugiere que fue diseñado en las décadas de 1980-1990, cuando estas tecnologías dominaban la educación en China y a nivel mundial, particularmente para programas de ingeniería.
- **Historia Detrás del Curso**:
  - En la década de 1980, China priorizó la educación en informática y electrónica para ponerse al día con la tecnología occidental. Cursos como este fueron críticos para capacitar ingenieros en diseño de microcomputadoras, sistemas embebidos y automatización industrial.
  - El 8086/8088 y los chips periféricos de Intel eran ideales para la enseñanza debido a su simplicidad, uso generalizado y documentación. La inclusión en el curso de interfaces modernas (USB, SPI, I²C) refleja actualizaciones para mantenerse relevante.
  - **Carreras Objetivo**: Ciencias de la Computación, Ingeniería Electrónica y Automatización se alinean con el enfoque del curso en diseño de hardware, programación e integración de sistemas, habilidades clave para industrias como robótica, telecomunicaciones e informática.

---

### **Significado y Legado**

- **Microcomputadoras**: Transformaron la computación de máquinas del tamaño de una habitación a dispositivos personales y embebidos. La arquitectura x86 del 8086/8088 sigue siendo la columna vertebral de las PC y servidores.
- **Programación en Ensamblador**: Aunque menos común, es vital para tareas de bajo nivel (por ejemplo, kernels de SO, firmware).
- **Chips de Interfaz**: Los principios del 8255, 8253 y 8251 persisten en los microcontroladores modernos (por ejemplo, Arduino, STM32).
- **Buses**: ISA y PCI allanaron el camino para PCIe, mientras que USB, SPI e I²C dominan los sistemas modernos.
- **Impacto Educativo**: Cursos como este capacitaron a generaciones de ingenieros, contribuyendo a los avances tecnológicos globales, particularmente en el auge tecnológico de China.

---

### **Relevancia Moderna**
- **Sistemas Embebidos**: Los sistemas basados en microcontroladores utilizan conceptos similares de E/S, interrupciones y temporización.
- **Sistemas Legados**: Algunos sistemas industriales y militares todavía utilizan diseños basados en 8086.
- **Educación**: La simplicidad del 8086 lo convierte en una herramienta de enseñanza atemporal para la arquitectura de computadoras.
- **Evolución x86**: Las CPU modernas (por ejemplo, Intel Core, AMD Ryzen) trazan su linaje hasta el 8086.

---

Si necesitas detalles específicos (por ejemplo, especificaciones técnicas del 8255, el desarrollo de USB o los antecedentes de Yang Quansheng) o deseas explorar temas relacionados (por ejemplo, la educación tecnológica de China en la década de 1980), ¡avísame!