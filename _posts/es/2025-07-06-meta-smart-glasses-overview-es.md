---
audio: false
generated: true
lang: es
layout: post
title: 'Las Gafas Inteligentes de Meta: Características y API'
translated: true
type: note
---

Desglosemos la oferta de gafas inteligentes de Meta, incluyendo Ray-Ban y Oakley, su base de usuarios y lo que sus APIs ofrecen a los desarrolladores.

**¿Qué son las gafas Meta VR, Ray-Ban y Oakley inteligentes?**

Es importante aclarar la terminología aquí. "Meta VR Glass" no es un nombre de producto específico que Meta utilice ampliamente. En su lugar, la oferta principal de VR/Realidad Mixta (RM) de Meta es la línea de **Meta Quest** (por ejemplo, Meta Quest 3).

Cuando la gente se refiere a las "gafas Meta" en una forma más general, con formato de gafas, normalmente se refiere a:

*   **Ray-Ban Meta Smart Glasses:** Estas son gafas inteligentes orientadas al consumidor, desarrolladas en asociación con EssilorLuxottica (la empresa detrás de Ray-Ban). Están diseñadas para parecerse a las gafas de sol Ray-Ban convencionales y se centran en funciones como:
    *   Captura de fotos y vídeos manos libres (con un indicador LED visible para la privacidad).
    *   Altavoces de oído abierto para audio (música, podcasts, llamadas).
    *   Micrófonos integrados para llamadas y comandos de voz (incluyendo "Hey Meta" para Meta AI).
    *   Capacidades de transmisión en directo a Facebook e Instagram.
    *   Integración con Meta AI para varias tareas (por ejemplo, obtener información, enviar mensajes, describir el entorno para accesibilidad).
    *   No tienen pantalla integrada ni pantalla de visualización montada en la cabeza para RA (son "gafas inteligentes", no gafas de RA en el sentido típico).

*   **Gafas Oakley Meta (por ejemplo, Oakley Meta HSTN):** Esta es una línea más nueva de "Gafas de IA de Rendimiento" desarrollada en colaboración con Oakley, que también forma parte de EssilorLuxottica. Comparten muchas de las características de las gafas Ray-Ban Meta, pero están diseñadas específicamente para atletas y el rendimiento. Los aspectos clave incluyen:
    *   Estética atrevida y deportiva, típica de Oakley.
    *   Mayor durabilidad y resistencia al agua (IPX4).
    *   Batería de mayor duración.
    *   Cámara de mayor resolución (vídeo 3K).
    *   Integración con Meta AI, ofreciendo funciones adaptadas para atletas (por ejemplo, preguntar sobre las condiciones del viento para el golf).

**¿Cuántos usuarios tienen?**

En febrero de 2025, las **Ray-Ban Meta Smart Glasses** han vendido más de **2 millones de unidades** desde su lanzamiento en septiembre de 2023. EssilorLuxottica planea aumentar la capacidad de producción anual a 10 millones de unidades para finales de 2026, lo que indica una fuerte demanda y la creencia de Meta en el futuro del producto.

Las **Gafas Oakley Meta** son una línea de producto más nueva, con pedidos anticipados comenzando en julio de 2025. Por lo tanto, las cifras de usuarios específicas para las gafas Oakley Meta aún no están disponibles, pero apuntan a una presencia significativa en el mercado.

**¿Qué ofrece su API a los desarrolladores?**

Es importante distinguir entre las APIs para los cascos de VR/RM (como Meta Quest) y las gafas inteligentes (como Ray-Ban Meta y Oakley Meta).

**Para Meta Quest (cascos de VR/RM):**

Meta proporciona una plataforma robusta para desarrolladores para su Meta Horizon OS (anteriormente Quest OS), ofreciendo varias APIs y SDKs para crear experiencias inmersivas de VR y realidad mixta. Las áreas clave para los desarrolladores incluyen:

*   **OpenXR:** Un estándar para crear experiencias de XR de alto rendimiento, permitiendo a los desarrolladores crear aplicaciones de VR/RM multiplataforma.
*   **Meta Horizon Worlds:** Herramientas para crear y dar forma a experiencias dentro de la plataforma de VR social de Meta.
*   **Aplicaciones Android:** Los desarrolladores pueden hacer que las aplicaciones Android existentes sean compatibles con Meta Horizon OS y aprovechar sus características espaciales únicas.
*   **Desarrollo Web:** Diseñar e implementar aplicaciones web 2D que utilicen las capacidades de multitarea de Quest.
*   **Meta Spatial SDK:** Diseñado para la realidad mixta, permitiendo a los desarrolladores transformar aplicaciones 2D con elementos espaciales innovadores.
*   **API de Cámara de Paso a Través (Passthrough):** Permite a los desarrolladores fusionar de forma fluida los mundos virtual y real, creando aplicaciones de realidad mixta.
*   **APIs de Interacción:** Para seguimiento de manos, entrada de controladores, locomoción y más.
*   **APIs de Comando de Voz y Texto a Voz (TTS):** Para integrar control por voz y salida hablada en las aplicaciones.
*   **APIs de Comprensión de Escenas (Scene Understanding):** Para acceder y utilizar datos sobre el entorno físico del usuario (por ejemplo, malla de la escena, anclajes).
*   **APIs de Características Sociales:** Para tablas de clasificación, desafíos, notificaciones de usuario, etc.

**Para las Gafas Inteligentes Ray-Ban Meta y Oakley Meta:**

Actualmente, no hay un SDK o API oficial, completo y de acceso público, específicamente para que desarrolladores externos creen aplicaciones personalizadas que se ejecuten *directamente en* las gafas inteligentes Ray-Ban Meta u Oakley Meta.

Sin embargo, los desarrolladores han sido creativos para encontrar formas de interactuar con estos dispositivos:

*   **Integración con Meta AI:** La forma principal en que los desarrolladores pueden interactuar con estas gafas es a través de su integración con **Meta AI**. Esto significa que los desarrolladores pueden potencialmente aprovechar las capacidades de Meta AI para varias tareas utilizando las APIs existentes para modelos de lenguaje grandes (LLMs) y otros servicios de IA. Por ejemplo, algunos proyectos impulsados por la comunidad han demostrado integraciones "no oficiales" usando Messenger como puente para enviar comandos o recibir datos de las gafas, y luego procesar esos datos con servicios como ChatGPT o Google Gemini a través de sus respectivas APIs. Esto depende de la capacidad integrada de las gafas para interactuar con Meta AI y enviar/recibir mensajes.
*   **Intercambio de Contenido:** Las gafas funcionan principalmente como un dispositivo de captura y compartición. Los desarrolladores pueden interactuar con la **app Meta View** (la aplicación complementaria para las gafas) proporcionando formas de compartir el contenido capturado con las gafas en sus plataformas, de manera similar a cómo se comparte contenido en Instagram, Facebook, WhatsApp, etc.
*   **Características de Accesibilidad:** La Meta AI integrada proporciona funciones de accesibilidad como describir el entorno o leer texto en voz alta. Si bien no es una API directa para que los desarrolladores creen nuevas aplicaciones *en* las gafas, resalta el potencial para la asistencia impulsada por IA que eventualmente podría estar disponible a través de herramientas de desarrollo más abiertas.

Si bien Meta ha declarado su visión a largo plazo para un desarrollo más abierto en futuras gafas inteligentes (potencialmente con pantallas heads-up, como el proyecto rumoreado "Orion"), para las gafas inteligentes Ray-Ban Meta y Oakley Meta actuales, el acceso para desarrolladores es principalmente indirecto, aprovechando su integración con Meta AI y las funcionalidades de intercambio de contenido. La comunidad está explorando activamente alternativas e integraciones no oficiales en ausencia de un SDK público dedicado para el desarrollo de aplicaciones en el dispositivo.