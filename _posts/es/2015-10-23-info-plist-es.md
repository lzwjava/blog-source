---
audio: false
generated: false
lang: es
layout: post
title: Decodificando el archivo Info.plist
translated: true
---

Si has trabajado con el desarrollo de macOS o iOS, es probable que te hayas topado con un archivo `Info.plist`. Este archivo basado en XML es una parte clave de cualquier aplicación o complemento de Apple, actuando como un pasaporte que le dice al sistema quién es, qué hace y cómo debe comportarse. Hoy, estamos explorando el `Info.plist` de "Reveal-In-GitHub", un complemento de Xcode que introdujimos en una publicación anterior. En lugar de desglosar cada línea, nos centraremos en los conceptos y patrones fundamentales que definen su propósito y funcionalidad.

---

#### ¿Qué es un archivo `Info.plist`?

El `Info.plist` (abreviatura de "Information Property List") es un archivo estructurado que contiene metadatos sobre una aplicación, complemento o paquete. Escrito en XML (con un esquema definido específicamente por Apple), utiliza pares clave-valor para describir esenciales como el nombre de la aplicación, la versión y la compatibilidad. Para "Reveal-In-GitHub", este archivo lo identifica como un complemento de Xcode y asegura que se integre sin problemas con el IDE.

A diferencia del archivo `.pbxproj`, que se trata de *cómo* construir algo, el `Info.plist` se trata de *qué* es ese algo. Es una declaración de identidad e intención.

---

#### Conceptos Clave en el Archivo

1. **Básicos del Paquete**
   Varios claves definen el complemento como un paquete de macOS:
   - **`CFBundleExecutable`**: Establecido en `$(EXECUTABLE_NAME)`, un marcador de posición para el nombre del binario compilado (definido durante el proceso de construcción).
   - **`CFBundleIdentifier`**: `$(PRODUCT_BUNDLE_IDENTIFIER)` se resuelve en `com.lzwjava.Reveal-In-GitHub`, un ID único en estilo de DNS inverso que distingue este complemento de otros.
   - **`CFBundlePackageType`**: `BNDL` lo marca como un paquete, un formato común para complementos y bibliotecas en macOS.
   - **`CFBundleName`**: `$(PRODUCT_NAME)` se convertirá en "Reveal-In-GitHub", el nombre amigable para el usuario.

2. **Versionado y Propiedad**
   - **`CFBundleShortVersionString`**: "1.0" es la versión visible para el usuario.
   - **`CFBundleVersion`**: "1" es un número de construcción interno.
   - **`NSHumanReadableCopyright`**: "Copyright © 2015年 lzwjava. All rights reserved." acredita al creador, `lzwjava`, y data el complemento en 2015.
   - **`CFBundleSignature`**: "????" es un marcador de posición (típicamente un código de cuatro caracteres), aunque es menos crítico para los complementos.

3. **Localización**
   - **`CFBundleDevelopmentRegion`**: "en" establece el inglés como el idioma predeterminado, afectando cómo se localizan los recursos (si los hay).

4. **Compatibilidad del Complemento de Xcode**
   La característica destacada aquí es **`DVTPlugInCompatibilityUUIDs`**, un largo array de UUIDs. Estos coinciden con versiones específicas de Xcode (por ejemplo, Xcode 6, 7, etc.), asegurando que el complemento solo se cargue en IDEs compatibles. Esta lista es inusualmente amplia, sugiriendo que "Reveal-In-GitHub" fue diseñado para funcionar en muchas versiones de Xcode, un signo de una cuidadosa compatibilidad hacia adelante y hacia atrás.

5. **Configuraciones Específicas del Complemento**
   - **`NSPrincipalClass`**: Dejado vacío (`<string></string>`), lo que implica que el complemento podría definir dinámicamente su punto de entrada o depender de las convenciones de Xcode.
   - **`XC4Compatible` y `XC5Compatible`**: Ambos `<true/>`, confirmando la compatibilidad con Xcode 4 y 5.
   - **`XCGCReady`**: `<true/>` indica la preparación para la recolección de basura, una característica de gestión de memoria de macOS más antigua (principalmente obsoleta en 2015 en favor de ARC).
   - **`XCPluginHasUI`**: `<false/>` sugiere que no hay una interfaz de usuario personalizada más allá de lo que está integrado en Xcode, aunque esto parece estar en conflicto con el archivo `.xib` en el `.pbxproj`. Quizás la interfaz de usuario es mínima o se maneja de manera diferente.

---

#### Patrones para Observar

1. **Marcadores de Posición para Flexibilidad**
   Claves como `$(EXECUTABLE_NAME)` y `$(PRODUCT_BUNDLE_IDENTIFIER)` utilizan variables vinculadas al sistema de construcción (definidas en el `.pbxproj`). Esto mantiene el `Info.plist` reutilizable en diferentes configuraciones (por ejemplo, Depuración vs. Liberación).

2. **Diseño Minimalista**
   El archivo es esbelto, enfocándose en lo esencial. No hay iconos elegantes, permisos o configuraciones específicas de la aplicación, solo lo que un complemento de Xcode necesita para funcionar. Esta simplicidad es típica para complementos que extienden una aplicación existente (Xcode) en lugar de programas independientes.

3. **Enfoque en la Compatibilidad**
   La larga lista de `DVTPlugInCompatibilityUUIDs` y las banderas como `XC4Compatible` muestran un complemento construido para durar. Este patrón es común en herramientas de desarrollo, donde los usuarios pueden quedarse con versiones más antiguas de Xcode por estabilidad.

4. **Metadatos sobre Comportamiento**
   A diferencia de los archivos de código, el `Info.plist` no *hace* nada, describe. Su papel es pasivo, proporcionando información que Xcode y macOS interpretan en tiempo de ejecución.

---

#### ¿Qué Nos Dice Esto Sobre Reveal-In-GitHub?

Este `Info.plist` pinta a "Reveal-In-GitHub" como un complemento ligero y enfocado de Xcode de 2015, probablemente creado por un desarrollador independiente (`lzwjava`). Su amplia compatibilidad sugiere que estaba destinado a ser ampliamente utilizable, mientras que la falta de una bandera de interfaz de usuario (a pesar de un `.xib` en el proyecto) sugiere una integración sutil, quizás un elemento de menú o acción contextual en lugar de una interfaz llamativa. Dado el nombre y el contexto del `.pbxproj`, probablemente optimiza los flujos de trabajo de GitHub, como enlazar archivos de Xcode a sus repositorios en línea.

---

#### ¿Por Qué Esto Importa?

El `Info.plist` es el saludo de tu aplicación con el sistema. Para los desarrolladores, entenderlo significa que puedes ajustar la compatibilidad, el versionado o el comportamiento sin tocar el código. Para "Reveal-In-GitHub", es la clave para encajar en Xcode sin problemas. La próxima vez que estés depurando un complemento o creando el tuyo, este archivo será tu punto de partida, pequeño pero poderoso.