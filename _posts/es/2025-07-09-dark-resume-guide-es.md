---
audio: false
generated: true
lang: es
layout: post
title: Crear un Currículum Oscuro con LaTeX
translated: true
type: note
---

Para generar un `resume-en-dark.pdf` usando tu `awesome-cv-dark.cls`, necesitarás:

### ✅ 1. Crear un nuevo archivo fuente de LaTeX para la versión oscura

Duplica tu archivo `resume-en.tex` existente en un nuevo archivo que use la clase del tema oscuro:

#### `latex/en/resume-en-dark.tex`

```latex
%-------------------------------------------------------------------------------
% CONFIGURACIONES
%-------------------------------------------------------------------------------
\documentclass[11pt, a4paper]{../awesome-cv-dark} % Usa la versión oscura aquí

% Configurar los márgenes de la página
\geometry{left=1.4cm, top=.8cm, right=1.4cm, bottom=1.8cm, footskip=.5cm}

% Color para los destacados
\colorlet{awesome}{awesome-red}

% Establecer resaltado de sección
\setbool{acvSectionColorHighlight}{true}

\usepackage{fontspec}
\usepackage{xeCJK}
\usepackage{ifthen}

% Incluir el contenido real del currículum (igual que tu versión normal)
\input{resume-en-content.tex}
```

> ✅ Puedes reutilizar tu `resume-en-content.tex` existente para evitar duplicación, o copiar/pegar desde `resume-en.tex`.

---

### ✅ 2. Actualizar el `Makefile`

Añade una nueva regla en tu `Makefile` para generar `resume-en-dark.pdf`.

Encuentra esta parte en el `Makefile`:

```make
latex: $(foreach x, coverletter coverletter-zh resume-zh resume, $x.pdf)
```

Modifícala para incluir el currículum oscuro:

```make
latex: $(foreach x, coverletter coverletter-zh resume-zh resume resume-en-dark, $x.pdf)
```

Luego añade la regla de compilación:

```make
resume-en-dark.pdf: $(RESUME_EN_DIR)/resume-en-dark.tex $(RESUME_SRCS)
	$(CC) -output-directory=$(RESUME_EN_DIR) $<
```

> 🔁 Si mantienes todos los recursos en la misma carpeta (`latex/en/resume-en/`), no necesitas actualizar `RESUME_SRCS`.

---

### ✅ 3. Opcional: Añadir al objetivo `copy`

Si quieres copiar el archivo generado a `assets/resume`, actualiza `copy`:

```make
	cp $(RESUME_EN_DIR)/resume-en-dark.pdf assets/resume/Zhiwei.Li.Resume.Dark.pdf
```

---

### ✅ 4. Compílalo

Ahora puedes ejecutar:

```bash
make resume-en-dark.pdf
```

---

Avísame si tu contenido se comparte entre temas y quieres una estructura más inteligente usando archivos `.tex` compartidos como `resume-en-content.tex`.