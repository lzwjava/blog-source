---
audio: false
generated: false
image: false
lang: es
layout: post
title: Transformando Eclipse en Emacs
translated: true
type: post
---

Como usuario de Emacs durante medio año, simplemente no puedo imaginar cómo solía codificar, moviendo las manos desde la posición estándar para hacer clic en el mouse o presionar las teclas de flecha, sin sentir que era incómodo e insoportable. Ahora, cuando le digo a mis amigos que he configurado los atajos Alt+P y Alt+N para cambiar rápidamente entre archivos XML y el Diseño Gráfico, su respuesta es solo "de acuerdo", lo que implica que usar el mouse para cambiar también está bien.
Para mí, eso es una pesadilla; simplemente no es lo suficientemente rápido. ¡Si eres un usuario de Emacs, lo entiendes!

Este artículo describe técnicas simples para construir un entorno de "edición" rápida en Eclipse. Básicamente, tus manos pueden quedarse en la posición estándar, permitiéndote codificar con máxima eficiencia.

Lo más importante es instalar el complemento Emacs+. Consulta "Emacs+: Experiencia de Emacs en Eclipse".

Para aprovechar al máximo el asistente de código, necesitas habilitar que se desencadene con cualquier carácter y evitar la autocompletación al presionar espacio o =. Recomiendo descargar este archivo jar desde CSDN. Con él y una rápida búsqueda en Google, puedes importar paquetes en un santiamén.

A continuación, personalicemos algunos atajos:

1) Enlaza Alt+P a "Pestaña anterior" y Alt+N a "Pestaña siguiente".

La pestaña secundaria es la barra de pestañas debajo de un editor, como las pestañas "Diseño Gráfico" y "XML" al editar un archivo XML. Esto te permite ver el diseño al instante.

2) Enlaza Ctrl+C, Ctrl+C a "Ejecutar".

Esto está copiado de la configuración de sbcl. El valor predeterminado es Ctrl+F11, que está demasiado lejos para un atajo tan frecuentemente utilizado, lo que hace que los usuarios de Emacs se sientan terribles. ¡Tontamente presioné Ctrl+F11 durante unos días antes de cambiarlo!

3) Enlaza Ctrl+X, Ctrl+O a "Vista siguiente" cuando Windows y en el texto de edición.

Esto te permite saltar instantáneamente del Editor a la Consola al escribir código Java.

4) Enlaza Ctrl+X, O a "Editor siguiente" cuando Windows y en el texto de edición.

Esto te permite cambiar rápidamente entre archivos Java.

5) Enlaza Ctrl+Q a "Corrección rápida".

De esta manera, cuando escribas `@string/xx`, con el cursor en `xx`, presionar Ctrl+Q y luego Enter te llevará instantáneamente a `string.xml`, con el cursor posicionado en el `TODO` dentro de `<string name="xx">TODO</string>`.

6) Enlaza Ctrl+Shift+W a "Cerrar" (cuando en ventanas) y elimina el enlace original (cerrar todo).
El atajo de cierre original es Ctrl+W, que coincide con nuestros hábitos en navegadores, cajas de chat y exploradores de archivos. Sin embargo, entra en conflicto con el comando de corte de Emacs. En realidad, presionar Ctrl+Shift+W por un segundo puede cerrar muchos archivos. Entonces, cambiar Ctrl+Shift+W de "cerrar todo" a "cerrar" no pierde nada.

Hay un problema: después de instalar Emacs+, al editar código y aparecer el asistente de código, presionar las teclas de flecha hacia arriba y hacia abajo no selecciona elementos en la lista de candidatos del asistente de código; en cambio, se mueve hacia arriba y hacia abajo en el código que se está editando. El valor predeterminado es activarlo con F2. Activar el asistente de código pone el enfoque en el asistente de código, pero luego solo puedes usar las teclas de flecha hacia arriba y hacia abajo para seleccionar. ¡Qué genial sería poder usar Ctrl+P y Ctrl+N! La codificación sería increíblemente rápida. Pero el problema es que después de instalar el complemento Emacs+, aunque Eclipse se vuelve más como Emacs, se pierde esta funcionalidad. En un Eclipse limpio, con el diseño de teclado Emacs (no Emacs+Scheme) seleccionado, puedes usar Ctrl+N y Ctrl+P para seleccionar elementos de autocompletar cuando aparece el asistente de código. Alguien preguntó sobre esto en Stack Overflow, pero aún no hay respuesta.

¡Si pudiéramos usar Ctrl+P y Ctrl+N para seleccionar elementos de autocompletar, sería realmente increíble!