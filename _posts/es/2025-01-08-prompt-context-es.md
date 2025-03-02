---
audio: false
generated: false
lang: es
layout: post
title: Corregir Indicaciones o Contexto en Lugar de la Salida de la IA
translated: true
---

Existen indicaciones de usuario y indicaciones del sistema. Cuando la salida no funciona bien, debemos agregar la regla en las indicaciones del usuario en lugar de corregirla cada vez.

Como se mencionó en un ensayo anterior, [Nombres en la Traducción de Salida de IA](./naming-en), existen muchos nombres chinos duplicados. Incluso los humanos no siempre pueden traducir nombres del inglés al chino correctamente, por lo que es aún más difícil para las máquinas.

No es difícil definir las reglas para la traducción de nombres. En la vida real, a menudo se necesita contexto. Por ejemplo, en una clase de aproximadamente 30 personas, si dos personas tienen el mismo nombre en inglés (traducción en Pinyin), se vuelve difícil distinguirlos al traducir. Se necesita información adicional, como su apariencia.

Sin embargo, en ciertos contextos—como el blog de alguien, una plataforma de conferencias o la lista de contactos de un usuario—la lista de nombres objetivo posibles se reduce considerablemente. En estos casos, la IA puede traducir perfectamente.

Por lo tanto, deberíamos definir estas reglas en nuestras llamadas API. No cambies la salida; corrige la causa raíz en lugar de ajustar el contenido generado temporalmente. Enfócate en arreglar la razón, no el resultado.

Los editores de código con IA son más inteligentes que los chatbots de IA porque tienen un contexto más amplio. Esto les permite hacer inferencias más precisas sobre su salida.

Lo mismo se aplica a las imágenes, el audio y el video. Estas herramientas deberían proporcionar un contexto más amplio. Por ejemplo, si a las herramientas de creación de IA se les proporciona un conjunto de videos, clips de audio y podcasts, pueden generar nuevos contenidos de manera mucho más efectiva.

Esto es similar a RAG (Generación Aumentada por Recuperación). Para las herramientas de creación de IA, deben encontrar un equilibrio: generar resultados que no sean ni demasiado específicos ni demasiado genéricos. Sin embargo, deben ofrecer herramientas o funcionalidades para que los resultados sean más específicos. ChatGPT, por ejemplo, tiene una funcionalidad de proyecto que te permite subir archivos y luego interactuar con ellos. Otras herramientas de creación necesitan características similares.

