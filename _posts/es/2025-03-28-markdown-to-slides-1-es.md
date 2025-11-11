---
audio: false
generated: true
image: false
lang: es
layout: post
title: Markdown a Diapositivas Hecho Fácil
translated: true
type: note
---

Marp CLI te permite convertir archivos Markdown en diapositivas (HTML, PDF, PPTX). Es especialmente útil si quieres escribir presentaciones en Markdown plano con un esfuerzo de formato mínimo.

Aquí tienes una guía paso a paso:

---

### 1. Instalar Marp CLI

Primero necesitas Node.js.

```bash
npm install -g @marp-team/marp-cli
```

Verifica la instalación:

```bash
marp --version
```

---

### 2. Escribe una presentación en Markdown

Crea un archivo, por ejemplo `slides.md`.

```markdown
---
marp: true
theme: default
paginate: true
---

# ¡Hola, Marp!

---

## Diapositiva 2

- Viñeta 1
- Viñeta 2
```

Puntos clave:

* `---` (YAML frontmatter) habilita Marp y la configuración.
* `---` (entre el contenido) separa las diapositivas.

---

### 3. Vista previa en el navegador

Ejecuta un servidor local con recarga automática:

```bash
marp -p slides.md
```

Abre [http://localhost:8080](http://localhost:8080) en tu navegador.

---

### 4. Exportar diapositivas

Genera diferentes formatos:

* HTML (autocontenido):

  ```bash
  marp slides.md -o slides.html
  ```

* PDF:

  ```bash
  marp slides.md -o slides.pdf
  ```

* PowerPoint (PPTX):

  ```bash
  marp slides.md -o slides.pptx
  ```

---

### 5. Opciones útiles

* **Observar cambios** (reconstrucción automática):

  ```bash
  marp -w slides.md
  ```

* **Establecer tema** (default, gaia, uncover o tu CSS personalizado):

  ```bash
  marp --theme-set ./my-theme.css slides.md -o slides.html
  ```

* **Incluir notas del orador**:

  ```markdown
  ---
  marp: true
  ---

  # Título

  <!--
  Estas son notas del orador
  -->
  ```

---

### 6. Integración con editores

* VSCode tiene una [extensión de Marp](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode).
* Muestra vistas previas en vivo mientras editas el Markdown.

---

👉 Con esta configuración, puedes pasar de un archivo `.md` plano a una presentación pulida en minutos.

¿Quieres que te proporcione una **plantilla de archivo Markdown lista para usar** (con diapositiva de título, agenda, contenido y diapositiva de cierre) para que puedas empezar de inmediato?