---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Utiliser Awesome-CV pour Générer un CV Professionnel
translated: true
---

### Introduction

Avant d'utiliser [ZhiyeApp](https://www.zhiyeapp.com), je suis passé au puissant et personnalisable [Awesome-CV](https://github.com/posquit0/Awesome-CV). Ce modèle basé sur LaTeX rend la création de CV professionnels facile et hautement personnalisable.

---

### Pourquoi Awesome-CV ?  
- Personnalisable : Vous pouvez personnaliser les sections, les couleurs et la mise en forme.  
- Design professionnel : Une conception épurée, parfaite pour les candidatures.  
- Facile à utiliser : Nécessite une connaissance minimale de LaTeX.

---

### Exemple de mon CV

Voici une version simplifiée du fichier `resume.tex` que j'utilise :

```latex
%-------------------------------------------------------------------------------
% CONFIGURATIONS
%-------------------------------------------------------------------------------
\documentclass[11pt, a4paper]{awesome-cv}
```

% Marges de la page et surlignage des sections
\geometry{left=1.4cm, top=.8cm, right=1.4cm, bottom=1.8cm, footskip=.5cm}
\colorlet{awesome}{awesome-red}
\setbool{acvSectionColorHighlight}{true}

%-------------------------------------------------------------------------------
% INFORMATIONS PERSONNELLES
%-------------------------------------------------------------------------------
\name{Zhiwei}{Li}
\position{Ingénieur Full Stack{\enskip\cdotp\enskip}Ingénieur Backend}
\address{Guangzhou, Chine}
\mobile{(+86) 132-6163-0925}
\email{lzwjava@gmail.com}
\homepage{https://lzwjava.github.io}
\github{lzwjava}
\linkedin{lzwjava}
\quote{``Liberté Vérité"}

%-------------------------------------------------------------------------------
\begin{document}

% En-tête et Pied de page
\makecvheader[C]
\makecvfooter{\today}{Zhiwei Li~~~·~~~Curriculum Vitae}{\thepage}

% Sections du Contenu
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

Makefile pour l'automatisation

Pour automatiser le processus de génération de PDF, j'utilise le fichier Makefile suivant :

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

resume.pdf: $(EXAMPLES_DIR)/resume.tex $(RESUME_SRCS)
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

resume-zh.pdf: $(EXAMPLES_DIR)/resume-zh.tex $(RESUME_ZH_SRCS)
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

coverletter.pdf: $(EXAMPLES_DIR)/coverletter.tex
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

```makefile
clean:
	rm -rf $(EXAMPLES_DIR)/*.pdf
```

### Comment ça marche

1. Générer des PDFs :
   - Exécutez `make awesome-cv` pour générer les fichiers PDF suivants :
     - `resume.pdf` : CV en anglais
     - `resume-zh.pdf` : CV en chinois
     - `coverletter.pdf` : Lettre de motivation

2. Nettoyage :
   - Exécutez `make clean` pour supprimer tous les fichiers PDF générés.

### Conclusion

En tirant parti d'**Awesome-CV** et de cette configuration de Makefile, la génération et la maintenance de CV professionnels deviennent un jeu d'enfant. Que vous postuliez pour des rôles techniques ou que vous partagiez vos réalisations, **Awesome-CV** vous aide à présenter votre travail de manière élégante et efficace.

Consultez le dépôt Awesome-CV pour plus de détails : Awesome-CV sur GitHub.