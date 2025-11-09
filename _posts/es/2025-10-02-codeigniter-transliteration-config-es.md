---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Guía de Configuración de Transliteración de CodeIgniter
translated: true
type: note
---

### Propósito en CodeIgniter
Este es un archivo de configuración (llamado `foreign_characters.php` en CodeIgniter) de la librería **Text Helper**. Se utiliza para la **transliteración**, un proceso que convierte caracteres no ASCII (caracteres con acentos, diacríticos o extranjeros) en sus equivalentes ASCII más cercanos (por ejemplo, ä → ae, ñ → n). Esto ayuda en tareas como la generación de slugs para URLs, cadenas seguras para bases de datos o compatibilidad multiplataforma donde los caracteres especiales podrían causar problemas.

- Es parte de las versiones antiguas de CodeIgniter (anteriores a la 4.x); en CI4, una funcionalidad similar se trasladó a helpers o funciones globales.
- El array utiliza patrones de expresiones regulares (por ejemplo, `/ä|æ|ǽ/` coincide con ä, æ, o ǽ) para reemplazar caracteres con letras simples del inglés.
- Las funciones clave que utilizan esto: `convert_accented_characters()` en el Text Helper, que itera a través de este array y realiza un `preg_replace`.

Este no es código central del framework, sino una utilidad de ayuda, que a menudo se encuentra en `application/config/foreign_characters.php` en las instalaciones.

### Idiomas y Conjuntos de Caracteres Representados
El array cubre caracteres de varios scripts e idiomas para permitir una amplia transliteración. Aquí hay un desglose por categoría, incluyendo ejemplos (del código) y sus idiomas/fuentes:

- **Latino (Europa Occidental)**: Diacríticos comunes en las lenguas romances y germánicas.
  - Acentos (por ejemplo, ÀÁÂ → A, àáâ → a) para francés, español, portugués, catalán.
  - Diéresis (por ejemplo, Ä → Ae, ä → ae, Ü → Ue) para alemán, sueco.
  - Ligaduras (por ejemplo, æ → ae para danés/noruego, œ → oe para francés).
  - Especiales (por ejemplo, ñ → n para español, ł → l para polaco, þ → th para islandés).

- **Griego (Helénico)**: Letras similares al cirílico para el alfabeto griego.
  - Por ejemplo, Γ → G, Δ → Dj, Η → I, Ν → N, Ο → O, Ρ → R, Σ → S, Τ → T (griego antiguo/moderno).

- **Cirílico (Eslavo y Europa del Este)**: Basado en ruso, ucraniano, bielorruso, etc.
  - Básicos: А → A, Б → B, В → V, Г → G, Д → D, Ж → Zh, З → Z, П → P, Р → R, С → S, Т → T, Ф → F, Х → Kh, Ц → Ts, Ч → Ch, Ш → Sh, Щ → Shch, Ъ/Ь (signos suave/duro) → eliminados (sin equivalente), Ю → Yu, Я → Ya.
  - Extras: Ё/ё → Yo/yo (ruso), Є/є → Ye/ye (ucraniano), Ї/ї → Yi/yi (ucraniano), Й → Y (variaciones en ruso/ucraniano).

- **Otros Símbolos/Caracteres**:
  - ß → ss (alemán "Eszett").
  - ½ → (normalmente eliminado o ignorado, no está en este array pero es similar).
  - Extras matemáticos/griegos: ξ → ks, π → p, β → v, μ → m, ψ → ps (utilizado para transliteración científica).

Esto cubre aproximadamente el 90% de los caracteres no ASCII comunes en el contenido web internacional. Si un carácter no está listado, podría tratarse tal cual o ser eliminado. El orden es importante (procesado mediante `preg_replace`), asegurando que los reemplazos de múltiples caracteres ocurran primero. Para aplicaciones modernas, considere el soporte UTF-8 sobre la transliteración. Si necesita adaptar o expandir esto, está en el archivo de ayuda.