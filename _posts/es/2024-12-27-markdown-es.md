---
audio: false
generated: false
image: true
lang: es
layout: post
title: 'Problemas con Markdown: Kramdown y XeLaTeX'
translated: true
type: post
---

Para generar PDFs para mi blog de Jekyll usando Markdown, utilizo el siguiente comando de Pandoc:

```python
command = [
    'pandoc',
    input_markdown_path,
    '-o', output_pdf_path,
    '-f', 'markdown',
    '--pdf-engine', 'xelatex',
    '--resource-path=.:assets',
    '-V', f'CJKmainfont={CJK_FONT}',
    '-V', f'CJKsansfont={CJK_FONT}',
    '-V', f'CJKmonofont={CJK_FONT}',
    '-V', f'geometry:{GEOMETRY}',
    '-V', 'classoption=16pt',
    '-V', 'CJKoptions=Scale=1.1',
    '-V', 'linestretch=1.5'
]
```

Soporte para Kramdown y XeLaTeX

Al escribir Markdown que debe funcionar tanto con kramdown (para la salida HTML de Jekyll) como con XeLaTeX (para la salida PDF a través de Pandoc), hay algunas consideraciones a tener en cuenta:

1. Compatibilidad de Rutas de Imágenes
	•	Kramdown (HTML): Prefiere rutas que comiencen con / para referenciar recursos.
	•	XeLaTeX (PDF): Prefiere rutas relativas sin un / inicial.

Solución: Usar rutas relativas que funcionen para ambos:

```
![](assets/images/chatgpt/block.jpg)
```

2. Manejo de atributos de kramdown
	•	{:.responsive} es específico de kramdown para aplicar estilos en la salida HTML.
	•	XeLaTeX no admite estos atributos y generará un error.

Solución: Elimina los atributos específicos de kramdown en Markdown destinado a la generación de PDF. Por ejemplo:

```markdown
<!-- Específico de Kramdown -->
```
![](assets/images/chatgpt/block.jpg){: .responsive }
```

<!-- Compatible with both -->
```
![](assets/images/chatgpt/block.jpg)
```

Si `{:.responsive}` es crítico para el diseño HTML de tu Jekyll, considera agregarlo de manera selectiva para la salida web mientras lo omites en el proceso de generación de PDF.

Flujo de trabajo para compatibilidad dual

1. Escribe contenido en Markdown con dependencias mínimas en características específicas de kramdown.
2. Para estilos avanzados en HTML, aplica clases CSS directamente en tus plantillas de Jekyll en lugar de hacerlo en línea en Markdown.
3. Utiliza opciones de Pandoc para controlar el formato del PDF mientras mantienes la portabilidad del Markdown.

Al seguir estas prácticas, el contenido en Markdown permanece compatible tanto en la representación HTML de Jekyll como en la generación de PDF con XeLaTeX, garantizando un flujo de trabajo fluido para la publicación en múltiples formatos.