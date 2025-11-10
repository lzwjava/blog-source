---
audio: false
generated: true
lang: es
layout: post
title: 'Meta Spatial SDK: De Android a XR'
translated: true
type: note
---

El **Meta Spatial SDK** es un cambio radical para los desarrolladores que buscan crear aplicaciones inmersivas para los auriculares de RV/RM de Meta, específicamente aquellos que ejecutan **Meta Horizon OS** (como la serie Meta Quest). Su propósito principal es cerrar la brecha entre el desarrollo tradicional de aplicaciones móviles para Android y las capacidades únicas de la computación espacial.

Aquí tienes una introducción concisa al Meta Spatial SDK:

**¿Qué es?**

El Meta Spatial SDK es un nuevo framework que permite a los desarrolladores de Android aprovechar sus habilidades, herramientas y bibliotecas existentes (como Android Studio y Kotlin) para crear experiencias ricas, inmersivas y de realidad mixta en los dispositivos Meta Quest. Antes de este SDK, desarrollar para Quest a menudo requería usar un motor de juego completo como Unity o Unreal, lo que podía ser una barrera significativa para los desarrolladores centrados en móviles.

**Objetivos y Beneficios Clave:**

*   **Democratizar el Desarrollo de XR:** Reduce la barrera de entrada para los desarrolladores móviles, permitiendo que una gama más amplia de creadores construya para la computación espacial.
*   **Aprovechar Habilidades Existentes:** Los desarrolladores pueden utilizar su entorno de desarrollo de Android familiar, reduciendo las curvas de aprendizaje y acelerando el desarrollo.
*   **Extender Aplicaciones 2D a 3D:** Permite a los desarrolladores adaptar aplicaciones Android 2D existentes a Meta Horizon OS y mejorarlas con elementos 3D, funciones de realidad mixta e interacciones espaciales.
*   **Iteración Rápida:** El SDK proporciona un flujo de trabajo rápido, permitiendo una prototipación, construcción y prueba de ideas espaciales más ágil.
*   **Experiencia de Usuario Mejorada:** Facilita la creación de aplicaciones que van más allá de las pantallas planas tradicionales, ofreciendo funciones como renderizado 3D, video passthrough, seguimiento de manos, audio espacial y física para interacciones más atractivas.

**Capacidades y Características Principales:**

*   **Desarrollo Nativo de Android:** Construido sobre Kotlin, se integra perfectamente con el ecosistema de Android.
*   **Características de Realidad Mixta:** El acceso a la cámara de passthrough (Camera2 API) permite fusionar contenido virtual con el mundo real.
*   **Renderizado 3D:** Es compatible con pipelines de gráficos modernos, incluyendo modelos GLTF, physically-based rendering (PBR), animaciones y física de cuerpos rígidos.
*   **Paneles Interactivos:** Permite la creación de paneles de UI 2D dentro del entorno 3D, construidos utilizando frameworks de UI de Android familiares como Jetpack Compose.
*   **Entrada e Interacciones:** Proporciona APIs para el seguimiento de manos, entrada de controladores y otras interacciones naturales del usuario.
*   **Comprensión de la Escena:** Permite a los desarrolladores acceder a datos sobre el entorno físico del usuario.
*   **Audio Espacial:** Herramientas para incorporar sonido espacializado para mejorar la inmersión.
*   **Meta Spatial Editor:** Una herramienta complementaria que permite a los desarrolladores organizar y componer visualmente elementos 2D y 3D dentro de sus aplicaciones espaciales sin necesidad de un editor de motor de juego completo.
*   **Entity-Component-System (ECS):** Un patrón arquitectónico utilizado dentro del SDK para construir aplicaciones espaciales modulares y de alto rendimiento.

En esencia, el Meta Spatial SDK capacita a los desarrolladores de Android para adentrarse fácilmente en el mundo de la realidad virtual y mixta, transformando las aplicaciones móviles tradicionales en experiencias espaciales convincentes en los dispositivos Meta Quest.