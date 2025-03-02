---
audio: false
generated: false
lang: de
layout: post
title: Verwendung von Awesome-CV zur Erstellung eines professionellen Lebenslaufs
translated: true
---

### Einführung

Bevor ich [ZhiyeApp](https://www.zhiyeapp.com) verwendete, wechselte ich zu dem leistungsstarken und anpassbaren [Awesome-CV](https://github.com/posquit0/Awesome-CV). Diese LaTeX-basierte Vorlage macht die Erstellung professioneller Lebensläufe einfach und hochgradig anpassbar.

---

### Warum Awesome-CV?  
- Anpassbar: Sie können Abschnitte, Farben und Formatierung individuell gestalten.  
- Professionelles Aussehen: Sauberes Design, ideal für Bewerbungen.  
- Einfach zu verwenden: Erfordert nur minimale LaTeX-Kenntnisse.

---

### Mein Lebenslauf-Beispiel

Hier ist eine vereinfachte Version der `resume.tex`-Datei, die ich verwende:

```latex
%-------------------------------------------------------------------------------
% KONFIGURATIONEN
%-------------------------------------------------------------------------------
\documentclass[11pt, a4paper]{awesome-cv}
```

% Seitenränder und Abschnittshighlights
\geometry{left=1.4cm, top=.8cm, right=1.4cm, bottom=1.8cm, footskip=.5cm}
\colorlet{awesome}{awesome-red}
\setbool{acvSectionColorHighlight}{true}

%-------------------------------------------------------------------------------
% PERSÖNLICHE INFORMATIONEN
%-------------------------------------------------------------------------------
\name{Zhiwei}{Li}
\position{Full Stack Engineer{\enskip\cdotp\enskip}Backend Engineer}
\address{Guangzhou, China}
\mobile{(+86) 132-6163-0925}
\email{lzwjava@gmail.com}
\homepage{https://lzwjava.github.io}
\github{lzwjava}
\linkedin{lzwjava}
\quote{``Freiheit Wahrheit"}

%-------------------------------------------------------------------------------
\begin{document}

% Kopf- und Fußzeile
\makecvheader[C]
\makecvfooter{\today}{Zhiwei Li~~~·~~~Lebenslauf}{\thepage}

% Inhaltsabschnitte
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

Makefile für Automatisierung

Um den Prozess der PDF-Generierung zu automatisieren, verwende ich die folgende Makefile:

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

clean:
	rm -rf $(EXAMPLES_DIR)/*.pdf
```

### Wie es funktioniert

1. PDFs generieren:
   - Führen Sie `make awesome-cv` aus, um die folgenden PDF-Dateien zu generieren:
     - `resume.pdf`: Englischer Lebenslauf
     - `resume-zh.pdf`: Chinesischer Lebenslauf
     - `coverletter.pdf`: Anschreiben
     
2. Aufräumen:
   - Führen Sie `make clean` aus, um alle generierten PDF-Dateien zu entfernen.

### Fazit

Durch die Nutzung von Awesome-CV und dieser Makefile-Einrichtung wird das Erstellen und Pflegen professioneller Lebensläufe zum Kinderspiel. Egal, ob Sie sich für technische Rollen bewerben oder Ihre Erfolge teilen möchten, Awesome-CV hilft Ihnen dabei, Ihre Arbeit ansprechend und effizient zu präsentieren.

Schau dir das Awesome-CV-Repository für weitere Details an: Awesome-CV auf GitHub.