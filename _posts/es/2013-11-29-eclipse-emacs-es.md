---
audio: false
lang: es
layout: post
title: Transformando Eclipse en Emacs
translated: true
---

Como usuario de Emacs durante medio año, simplemente no puedo imaginar cómo solía codificar, moviendo mis manos de la posición estándar para hacer clic en el mouse o presionar las teclas de flecha sin sentir que era incómodo y desagradable. Ahora, cuando le digo a mis amigos que he configurado los atajos Alt+P y Alt+N para cambiar rápidamente entre archivos XML y el Diseño Gráfico, su respuesta es solo "de acuerdo", lo que implica que usar el mouse para cambiar también está bien. Para mí, eso es una pesadilla; ¡simplemente no es lo suficientemente rápido! Si eres usuario de Emacs, entiendes...

Este artículo describe técnicas simples para construir un entorno de edición rápido de Eclipse. Básicamente, tus manos pueden permanecer en la posición estándar, permitiéndote codificar con la máxima eficiencia.

Lo más importante es instalar el complemento Emacs+. Consulta "Emacs+: Emacs Experience in Eclipse".

Para usar bien el asistente de código, debes habilitarlo para que se active con cualquier carácter e impedir la autocompletación al presionar el espacio o =. Recomiendo descargar este archivo jar de CSDN. Con él y una rápida búsqueda en Google, puedes importar paquetes en poco tiempo.

A continuación, personalicemos algunos atajos:

1) Vincular Alt+P a "Pestaña Anterior" y Alt+N a "Pestaña Siguiente."

La sub-pestaña es la barra de pestañas debajo de un editor, como las pestañas "Diseño Gráfico" y "XML" al editar un archivo XML. Esto te permite ver el diseño al instante.

2) Vincular Ctrl+C, Ctrl+C a "Ejecutar."

Esto se copia de la configuración de sbcl. El valor predeterminado es Ctrl+F11, que está demasiado lejos para un atajo tan utilizado con frecuencia, lo que hace que los usuarios de Emacs se sientan terribles. ¡Tontamente presioné Ctrl+F11 durante unos días antes de cambiarlo!

3) Vincular Ctrl+X, Ctrl+O a "Siguiente Vista." Cuando en Windows y en Edición de Texto.

Esto te permite saltar instantáneamente del Editor a la Consola al escribir código Java.

4) Vincular Ctrl+X, O a "Siguiente Editor." Cuando en Windows y en Edición de Texto.

Esto te permite cambiar rápidamente entre archivos Java.

5) Vincular Ctrl+Q a "Solución Rápida."

De esta manera, cuando escribas `@string/xx`, con el cursor en `xx`, presionar Ctrl+Q y luego Enter te llevará instantáneamente a `string.xml`, con el cursor posicionado en el `TODO` dentro de `<string name="xx">TODO</string>`.

6) Vincular Ctrl+Shift+W a "Cerrar" (cuando en ventanas) y eliminar el acortamiento original (cerrar todos).

El acortamiento original para cerrar es Ctrl+W, que coincide con nuestros hábitos en navegadores, cajas de chat y exploradores de archivos. Sin embargo, entra en conflicto con el comando de corte de Emacs. En realidad, presionar Ctrl+Shift+W durante un segundo puede cerrar muchos archivos. Entonces, cambiar Ctrl+Shift+W de "cerrar todos" a "cerrar" no pierde nada.

Hay un problema: después de instalar Emacs+, al editar código y aparecer el asistente de código, presionar las teclas de flecha hacia arriba y hacia abajo no selecciona elementos en la lista de candidatos del asistente de código; en su lugar, se mueve hacia arriba y hacia abajo en el código que se está editando. El valor predeterminado es activarlo con F2. Activar el asistente de código pone el foco en el asistente de código, pero luego solo puedes usar las teclas de flecha hacia arriba y hacia abajo para seleccionar. ¡Qué increíble sería si pudiéramos usar Ctrl+P y Ctrl+N! La edición de código sería increíblemente rápida. Pero el problema es que después de instalar el complemento Emacs+, aunque Eclipse se vuelve más como Emacs, esta funcionalidad se pierde. En un Eclipse limpio, con la configuración de teclado de Emacs (no Emacs+Scheme) seleccionada, puedes usar Ctrl+N y Ctrl+P para seleccionar elementos de completación cuando aparece el asistente de código. Alguien preguntó sobre esto en Stack Overflow, pero aún no hay respuesta.

Si pudiéramos usar Ctrl+P y Ctrl+N para seleccionar elementos de completación, ¡eso sería realmente increíble!