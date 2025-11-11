---
audio: false
generated: true
lang: es
layout: post
title: Encabezado HTTP Content-Length
translated: true
type: note
---

La unidad del encabezado **Content-Length** en el protocolo HTTP es **bytes**.

En HTTP, el encabezado **Content-Length** se utiliza para indicar el tamaño del cuerpo de la respuesta que el servidor envía al cliente. Este tamaño se especifica como un número decimal que representa el número de bytes (u octetos, donde un octeto equivale a 8 bits) en el cuerpo del mensaje. Según la especificación HTTP/1.1 (RFC 7230, Sección 3.3.2), el campo de encabezado **Content-Length** indica explícitamente el tamaño del cuerpo del mensaje en octetos, lo que confirma que la unidad es bytes.

Por ejemplo, en el caso proporcionado donde el encabezado es `'content-length': '130700923'`, esto significa que el cuerpo de la respuesta tiene una longitud de **130,700,923 bytes**. Para dar una idea de la escala, esto es aproximadamente **124.6 megabytes (MB)**, ya que 1 MB es aproximadamente 1,048,576 bytes (2^20 bytes). Este es un tamaño plausible para un archivo grande o una transferencia de datos en una respuesta HTTP.

Para aclarar aún más:
- El valor es un número entero, no un número fraccionario, lo que descarta unidades como kilobytes o megabytes directamente.
- En HTTP, el cuerpo se transmite como una secuencia de bytes, y **Content-Length** corresponde al número exacto de bytes que el cliente debe esperar.
- Incluso en otras versiones como HTTP/2, donde se utiliza *framing* en lugar de un único encabezado **Content-Length**, el tamaño de la carga útil aún se mide en bytes.

Por lo tanto, la unidad de **Content-Length** en el protocolo HTTP es inequívocamente **bytes**.