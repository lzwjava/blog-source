---
audio: false
generated: false
image: false
lang: es
layout: post
title: Usando Awesome-CV para Generar un Currículum Profesional
translated: true
---

### Introducción

Antes de usar [ZhiyeApp](https://www.zhiyeapp.com), cambié a la potente y personalizable [Awesome-CV](https://github.com/posquit0/Awesome-CV). Esta plantilla basada en LaTeX facilita la creación de currículums profesionales y es altamente personalizable.

---

### ¿Por qué Awesome-CV?  
- Personalizable: Puedes personalizar secciones, colores y formato.  
- Aspecto profesional: Diseño limpio perfecto para solicitudes de empleo.  
- Fácil de usar: Requiere un conocimiento mínimo de LaTeX.

---

### Ejemplo de mi Currículum

Aquí tienes una versión simplificada del archivo `resume.tex` que utilizo:

```latex
%-------------------------------------------------------------------------------
% CONFIGURACIONES
%-------------------------------------------------------------------------------
\documentclass[11pt, a4paper]{awesome-cv}
```

% Márgenes de página y resaltados de sección
\geometry{left=1.4cm, top=.8cm, right=1.4cm, bottom=1.8cm, footskip=.5cm}
\colorlet{awesome}{awesome-red}
\setbool{acvSectionColorHighlight}{true}

%-------------------------------------------------------------------------------
% INFORMACIÓN PERSONAL
%-------------------------------------------------------------------------------
\name{Zhiwei}{Li}
\position{Ingeniero Full Stack{\enskip\cdotp\enskip}Ingeniero Backend}
\address{Guangzhou, China}
\mobile{(+86) 132-6163-0925}
\email{lzwjava@gmail.com}
\homepage{https://lzwjava.github.io}
\github{lzwjava}
\linkedin{lzwjava}
\quote{``Libertad Verdad"}

%-------------------------------------------------------------------------------
\begin{document}

% Encabezado y Pie de Página
\makecvheader[C]
\makecvfooter{\today}{Zhiwei Li~~~·~~~Currículum}{\thepage}

% Secciones de Contenido
\input{resume/summary.tex}
\input{resume/experience.tex}
\input{resume/education.tex}
\input{resume/corporateprojects.tex}
\input{resume/personalprojects.tex}
\input{resume/blogposts.tex}
\input{resume/papers.tex}
\input{resume/books.tex}
\input{resume/skills.tex}
\input{resume/tools.tex}
\input{resume/knowledge.tex}
\input{resume/certificates.tex}

\end{document}

Makefile para Automatización

Para automatizar el proceso de generación de PDF, utilizo el siguiente archivo Makefile:

```Makefile
.PHONY: awesome-cv
```

```makefile
CC = xelatex
EXAMPLES_DIR = awesome-cv
RESUME_DIR = awesome-cv/resume
RESUME_ZH_DIR = awesome-cv/resume-zh
RESUME_SRCS = $(shell find $(RESUME_DIR) -name '*.tex')
RESUME_ZH_SRCS = $(shell find $(RESUME_ZH_DIR) -name '*.tex')
```

awesome-cv: $(foreach x, coverletter resume-zh resume, $x.pdf)  

*Nota: El texto proporcionado parece ser un fragmento de un archivo Makefile o un comando de línea de comandos. No requiere traducción, ya que es código y nombres de archivos específicos que deben mantenerse en inglés.*

resume.pdf: $(EXAMPLES_DIR)/resume.tex $(RESUME_SRCS)
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

resume-zh.pdf: $(EXAMPLES_DIR)/resume-zh.tex $(RESUME_ZH_SRCS)
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

coverletter.pdf: $(EXAMPLES_DIR)/coverletter.tex
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

clean:
	rm -rf $(EXAMPLES_DIR)/*.pdf
```

### Cómo Funciona

1. Generar PDFs:
   - Ejecuta `make awesome-cv` para generar los siguientes archivos PDF:
     - `resume.pdf`: Currículum en inglés
     - `resume-zh.pdf`: Currículum en chino
     - `coverletter.pdf`: Carta de presentación
     
2. Limpieza:
   - Ejecuta `make clean` para eliminar todos los archivos PDF generados.

### Conclusión

Al aprovechar Awesome-CV y esta configuración de Makefile, generar y mantener currículums profesionales se vuelve sencillo. Ya sea que estés aplicando para roles técnicos o compartiendo tus logros, Awesome-CV te ayuda a presentar tu trabajo de manera hermosa y eficiente.

Consulta el repositorio Awesome-CV para más detalles: Awesome-CV en GitHub.