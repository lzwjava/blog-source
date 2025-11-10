---
audio: false
generated: true
lang: de
layout: post
title: Dunklen Lebenslauf mit LaTeX erstellen
translated: true
type: note
---

Um eine `resume-en-dark.pdf` mit Ihrer `awesome-cv-dark.cls` zu erstellen, müssen Sie Folgendes tun:

### ✅ 1. Erstellen Sie eine neue LaTeX-Quelldatei für die Dunkelversion

Duplizieren Sie Ihre bestehende `resume-en.tex` in eine neue Datei, die die Dark-Theme-Klasse verwendet:

#### `latex/en/resume-en-dark.tex`

```latex
%-------------------------------------------------------------------------------
% KONFIGURATIONEN
%-------------------------------------------------------------------------------
\documentclass[11pt, a4paper]{../awesome-cv-dark} % Dunkelversion hier verwenden

% Seitenränder konfigurieren
\geometry{left=1.4cm, top=.8cm, right=1.4cm, bottom=1.8cm, footskip=.5cm}

% Farbe für Hervorhebungen
\colorlet{awesome}{awesome-red}

% Abschnittsfarbe hervorheben
\setbool{acvSectionColorHighlight}{true}

\usepackage{fontspec}
\usepackage{xeCJK}
\usepackage{ifthen}

% Den eigentlichen Lebenslauf-Inhalt einbinden (derselbe wie in Ihrer normalen Version)
\input{resume-en-content.tex}
```

> ✅ Sie können Ihre bestehende `resume-en-content.tex` wiederverwenden, um Duplizierung zu vermeiden, oder aus `resume-en.tex` kopieren/einfügen.

---

### ✅ 2. Aktualisieren Sie die `Makefile`

Fügen Sie Ihrer `Makefile` eine neue Regel zum Erstellen von `resume-en-dark.pdf` hinzu.

Suchen Sie diesen Teil in der `Makefile`:

```make
latex: $(foreach x, coverletter coverletter-zh resume-zh resume, $x.pdf)
```

Ändern Sie ihn so, dass der dunkle Lebenslauf enthalten ist:

```make
latex: $(foreach x, coverletter coverletter-zh resume-zh resume resume-en-dark, $x.pdf)
```

Fügen Sie dann die Build-Regel hinzu:

```make
resume-en-dark.pdf: $(RESUME_EN_DIR)/resume-en-dark.tex $(RESUME_SRCS)
	$(CC) -output-directory=$(RESUME_EN_DIR) $<
```

> 🔁 Wenn Sie alle Assets im selben Ordner (`latex/en/resume-en/`) behalten, müssen Sie `RESUME_SRCS` nicht aktualisieren.

---

### ✅ 3. Optional: Zum `copy`-Target hinzufügen

Wenn Sie die generierte Datei nach `assets/resume` kopieren möchten, aktualisieren Sie `copy`:

```make
	cp $(RESUME_EN_DIR)/resume-en-dark.pdf assets/resume/Zhiwei.Li.Resume.Dark.pdf
```

---

### ✅ 4. Bauen Sie es

Jetzt können Sie einfach ausführen:

```bash
make resume-en-dark.pdf
```

---

Lassen Sie mich wissen, ob Ihre Inhalte themenübergreifend genutzt werden und Sie eine intelligentere Struktur mit gemeinsamen `.tex`-Dateien wie `resume-en-content.tex` wünschen.