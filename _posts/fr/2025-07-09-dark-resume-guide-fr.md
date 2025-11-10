---
audio: false
generated: true
lang: fr
layout: post
title: Créer un CV sombre avec LaTeX
translated: true
type: note
---

Pour générer un `resume-en-dark.pdf` en utilisant votre `awesome-cv-dark.cls`, vous devrez :

### ✅ 1. Créer un nouveau fichier source LaTeX pour la version sombre

Dupliquez votre fichier `resume-en.tex` existant dans un nouveau fichier qui utilise la classe du thème sombre :

#### `latex/en/resume-en-dark.tex`

```latex
%-------------------------------------------------------------------------------
% CONFIGURATIONS
%-------------------------------------------------------------------------------
\documentclass[11pt, a4paper]{../awesome-cv-dark} % Utilisez la version sombre ici

% Configurer les marges de la page
\geometry{left=1.4cm, top=.8cm, right=1.4cm, bottom=1.8cm, footskip=.5cm}

% Couleur pour les surbrillances
\colorlet{awesome}{awesome-red}

% Définir la surbrillance de section
\setbool{acvSectionColorHighlight}{true}

\usepackage{fontspec}
\usepackage{xeCJK}
\usepackage{ifthen}

% Inclure le contenu réel du CV (identique à votre version normale)
\input{resume-en-content.tex}
```

> ✅ Vous pouvez réutiliser votre `resume-en-content.tex` existant pour éviter la duplication, ou copier/coller depuis `resume-en.tex`.

---

### ✅ 2. Mettre à jour le `Makefile`

Ajoutez une nouvelle règle dans votre `Makefile` pour générer `resume-en-dark.pdf`.

Trouvez cette partie dans le `Makefile` :

```make
latex: $(foreach x, coverletter coverletter-zh resume-zh resume, $x.pdf)
```

Modifiez-la pour inclure le CV sombre :

```make
latex: $(foreach x, coverletter coverletter-zh resume-zh resume resume-en-dark, $x.pdf)
```

Puis ajoutez la règle de compilation :

```make
resume-en-dark.pdf: $(RESUME_EN_DIR)/resume-en-dark.tex $(RESUME_SRCS)
	$(CC) -output-directory=$(RESUME_EN_DIR) $<
```

> 🔁 Si vous conservez tous les assets dans le même dossier (`latex/en/resume-en/`), vous n'avez pas besoin de mettre à jour `RESUME_SRCS`.

---

### ✅ 3. Optionnel : Ajouter à la cible `copy`

Si vous souhaitez copier le fichier généré vers `assets/resume`, mettez à jour `copy` :

```make
	cp $(RESUME_EN_DIR)/resume-en-dark.pdf assets/resume/Zhiwei.Li.Resume.Dark.pdf
```

---

### ✅ 4. Compilez-le

Vous pouvez maintenant simplement exécuter :

```bash
make resume-en-dark.pdf
```

---

Faites-moi savoir si votre contenu est partagé entre les thèmes et si vous souhaitez une structure plus intelligente utilisant des fichiers `.tex` partagés comme `resume-en-content.tex`.