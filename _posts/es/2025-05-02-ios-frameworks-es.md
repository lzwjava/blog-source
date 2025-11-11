---
audio: false
generated: true
lang: es
layout: post
title: Frameworks de iOS
translated: true
type: note
---

Además de UIKit, el sistema iOS proporciona muchos otros frameworks esenciales que los desarrolladores utilizan comúnmente para crear aplicaciones. Estos frameworks manejan varios aspectos más allá de los elementos de la interfaz de usuario. Estos son algunos de los más comunes:

1.  **Foundation:** Este es un framework fundamental que proporciona tipos de datos básicos (como cadenas, números, arrays, diccionarios), tipos de colección, servicios del sistema operativo y patrones de programación centrales. Es la base para muchos otros frameworks y casi siempre se importa en un proyecto de iOS. Incluye componentes esenciales como `URLSession` para networking, `FileManager` para interacciones con el sistema de archivos y `NotificationCenter` para gestionar notificaciones dentro de una aplicación.

2.  **Core Data:** Este framework proporciona una forma robusta y flexible de gestionar los objetos de la capa de modelo en tu aplicación. Te permite persistir datos, gestionar grafos de objetos y manejar la sincronización de datos. Aunque a menudo se describe como una tecnología de base de datos, es más precisamente un framework de gestión de grafos de objetos que puede utilizar diferentes almacenes persistentes, como SQLite, archivos binarios o almacenamiento en memoria.

3.  **Core Animation:** Este framework se utiliza para crear animaciones y efectos visuales fluidos y de alto rendimiento. Funciona junto con UIKit (o AppKit en macOS) para renderizar contenido animado. Puedes usarlo para animar vistas, capas y otros elementos gráficos, creando transiciones y efectos complejos sin manipular directamente los píxeles.

4.  **Core Graphics:** También conocido como Quartz 2D, es un motor de dibujo basado en C que proporciona capacidades de renderizado 2D de bajo nivel. Te permite dibujar puntos, líneas, trazados, formas e imágenes con alta fidelidad. Mientras que UIKit proporciona abstracciones de más alto nivel para el dibujo, Core Graphics se utiliza a menudo para operaciones de dibujo personalizadas, crear gradientes, gestionar contextos y trabajar directamente con primitivas gráficas.

5.  **AVFoundation:** Este framework proporciona un conjunto completo de herramientas para trabajar con medios audiovisuales basados en el tiempo. Puedes usarlo para reproducir, grabar y editar audio y video. Te da control sobre cámaras, micrófonos, motores de reproducción y activos multimedia, lo que lo hace esencial para aplicaciones que involucran contenido multimedia.

6.  **Core Location:** Este framework permite a tu aplicación acceder a los servicios de ubicación del dispositivo, como la ubicación geográfica actual, la altitud y el rumbo del usuario. Puede utilizar GPS, Wi-Fi y señales celulares para determinar la ubicación y admite funciones como el monitoreo de regiones y el geofencing.

7.  **UserNotifications:** Este framework se utiliza para programar y manejar notificaciones locales y remotas. Permite que tu aplicación informe a los usuarios sobre eventos importantes incluso cuando la aplicación no se está ejecutando activamente, mostrando alertas, reproduciendo sonidos o actualizando las insignias en el icono de la aplicación.

8.  **SwiftUI:** Si bien UIKit es el framework tradicional para construir interfaces de usuario con un enfoque imperativo, SwiftUI es un framework más nuevo y declarativo introducido por Apple para construir interfaces de usuario en todas las plataformas de Apple. Proporciona un paradigma diferente para el desarrollo de UI y es cada vez más común en el desarrollo moderno de iOS, a menudo se usa junto con o como alternativa a UIKit, especialmente para nuevos proyectos o características.

Estos frameworks, junto con muchos otros como Metal (para aceleración gráfica), SpriteKit (para juegos en 2D), SceneKit (para gráficos 3D) y Core ML (para machine learning), forman el ecosistema potente que los desarrolladores de iOS aprovechan para crear aplicaciones diversas y ricas en funciones.