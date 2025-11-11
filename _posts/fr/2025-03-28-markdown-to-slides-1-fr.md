---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Markdown vers diapositives simplifié
translated: true
type: note
---

Marp CLI vous permet de convertir des fichiers Markdown en diapositives (HTML, PDF, PPTX). C'est particulièrement utile si vous souhaitez écrire des présentations en Markdown brut avec un effort de formatage minimal.

Voici un guide étape par étape :

---

### 1. Installer Marp CLI

Vous avez d'abord besoin de Node.js.

```bash
npm install -g @marp-team/marp-cli
```

Vérifiez l'installation :

```bash
marp --version
```

---

### 2. Écrire une présentation en Markdown

Créez un fichier, par exemple `slides.md`.

```markdown
---
marp: true
theme: default
paginate: true
---

# Bonjour, Marp !

---

## Diapositive 2

- Puce 1
- Puce 2
```

Points clés :

* `---` (frontmatter YAML) active Marp et la configuration.
* `---` (entre le contenu) sépare les diapositives.

---

### 3. Prévisualiser dans le navigateur

Lancez un serveur local avec rechargement automatique :

```bash
marp -p slides.md
```

Ouvrez [http://localhost:8080](http://localhost:8080) dans votre navigateur.

---

### 4. Exporter les diapositives

Générez différents formats :

* HTML (autonome) :

  ```bash
  marp slides.md -o slides.html
  ```

* PDF :

  ```bash
  marp slides.md -o slides.pdf
  ```

* PowerPoint (PPTX) :

  ```bash
  marp slides.md -o slides.pptx
  ```

---

### 5. Options utiles

* **Surveiller les changements** (reconstruction automatique) :

  ```bash
  marp -w slides.md
  ```

* **Définir le thème** (default, gaia, uncover, ou votre CSS personnalisé) :

  ```bash
  marp --theme-set ./my-theme.css slides.md -o slides.html
  ```

* **Inclure les notes de l'orateur** :

  ```markdown
  ---
  marp: true
  ---

  # Titre

  <!--
  Ce sont des notes de l'orateur
  -->
  ```

---

### 6. Intégration avec l'éditeur

* VSCode a une [extension Marp](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode).
* Elle affiche des aperçus en direct lors de l'édition du Markdown.

---

👉 Avec cette configuration, vous pouvez passer d'un simple fichier `.md` à une présentation soignée en quelques minutes.

Souhaitez-vous que je vous fournisse un **modèle de fichier Markdown prêt à l'emploi** (avec une diapositive de titre, un ordre du jour, du contenu et une diapositive de clôture) pour que vous puissiez commencer immédiatement ?