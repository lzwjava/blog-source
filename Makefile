.PHONY: awesome-cv awesome-cv-en awesome-cv-copy awesome-cv-copy-en audio-pipeline pdf-pipeline pipelines clean copy papers

# ------------------------------------------------------------------------------
# 1) Compiler + directories
# ------------------------------------------------------------------------------
CC = xelatex

EXAMPLES_DIR       = awesome-cv
RESUME_DIR         = $(EXAMPLES_DIR)
COVER_LETTER_DIR   = $(EXAMPLES_DIR)
INTRODUCTION_DIR   = $(EXAMPLES_DIR)
PAPERS_DIR         = assets/papers

# ------------------------------------------------------------------------------
# 2) Files
# ------------------------------------------------------------------------------

# Resumes (note the path for EN is now 'en/resume-en/resume-en.tex')
RESUME_EN_SRC = $(RESUME_DIR)/en/resume-en/resume-en.tex
RESUME_ZH_SRC = $(RESUME_DIR)/zh/resume-zh/resume-zh.tex
RESUME_JA_SRC = $(RESUME_DIR)/ja/resume-ja/resume-ja.tex

RESUME_EN_PDF = $(RESUME_DIR)/en/resume-en/resume-en.pdf
RESUME_ZH_PDF = $(RESUME_DIR)/zh/resume-zh/resume-zh.pdf
RESUME_JA_PDF = $(RESUME_DIR)/ja/resume-ja/resume-ja.pdf

# Cover letters and introductions follow <lang>/coverletter-<lang>.tex, etc.
COVER_LETTER_SRCS = $(wildcard $(COVER_LETTER_DIR)/*/coverletter-*.tex)
INTRODUCTION_SRCS = $(wildcard $(INTRODUCTION_DIR)/*/introduction-*.tex)

# Papers (LaTeX files) inside assets/papers/
PAPERS_SRCS = $(shell find $(PAPERS_DIR) -name '*.tex' 2>/dev/null)

# ------------------------------------------------------------------------------
# 3) Targets
# ------------------------------------------------------------------------------

# Build EVERYTHING (resumes for en/zh/ja, plus cover letters, introductions, and papers)
awesome-cv: \
    $(RESUME_EN_PDF) \
    $(RESUME_ZH_PDF) \
    $(RESUME_JA_PDF) \
    $(patsubst %.tex, %.pdf, $(COVER_LETTER_SRCS)) \
    $(patsubst %.tex, %.pdf, $(INTRODUCTION_SRCS)) \
    $(patsubst $(PAPERS_DIR)/%.tex, $(PAPERS_DIR)/%.pdf, $(PAPERS_SRCS))

# English-only bundle
awesome-cv-en: \
    $(RESUME_EN_PDF) \
    $(COVER_LETTER_DIR)/en/coverletter-en.pdf \
    $(INTRODUCTION_DIR)/en/introduction-en.pdf

# ------------------------------------------------------------------------------
# 4) Build rules for each type of PDF
# ------------------------------------------------------------------------------

# --- Resumes (explicit rules, since they live in distinct subfolders) ---
$(RESUME_EN_PDF): $(RESUME_EN_SRC)
	$(CC) -output-directory=$(dir $@) $<

$(RESUME_ZH_PDF): $(RESUME_ZH_SRC)
	$(CC) -output-directory=$(dir $@) $<

$(RESUME_JA_PDF): $(RESUME_JA_SRC)
	$(CC) -output-directory=$(dir $@) $<

# --- Cover letters (pattern rule) ---
$(COVER_LETTER_DIR)/%/coverletter-%.pdf: $(COVER_LETTER_DIR)/%/coverletter-%.tex
	$(CC) -output-directory=$(dir $@) $<

# --- Introductions (pattern rule) ---
$(INTRODUCTION_DIR)/%/introduction-%.pdf: $(INTRODUCTION_DIR)/%/introduction-%.tex
	$(CC) -output-directory=$(dir $@) $<

# --- Papers (pattern rule) ---
$(PAPERS_DIR)/%.pdf: $(PAPERS_DIR)/%.tex
	$(CC) -output-directory=$(PAPERS_DIR) $<

papers: $(patsubst $(PAPERS_DIR)/%.tex, $(PAPERS_DIR)/%.pdf, $(PAPERS_SRCS))

# ------------------------------------------------------------------------------
# 5) Convenience targets for single PDFs (optional)
# ------------------------------------------------------------------------------
resume-en.pdf: $(RESUME_EN_PDF)
resume-zh.pdf: $(RESUME_ZH_PDF)
resume-ja.pdf: $(RESUME_JA_PDF)

coverletter-en.pdf: $(COVER_LETTER_DIR)/en/coverletter-en.pdf
coverletter-zh.pdf: $(COVER_LETTER_DIR)/zh/coverletter-zh.pdf
coverletter-ja.pdf: $(COVER_LETTER_DIR)/ja/coverletter-ja.pdf

introduction-en.pdf: $(INTRODUCTION_DIR)/en/introduction-en.pdf
introduction-zh.pdf: $(INTRODUCTION_DIR)/zh/introduction-zh.pdf
introduction-ja.pdf: $(INTRODUCTION_DIR)/ja/introduction-ja.pdf

# ------------------------------------------------------------------------------
# 6) Pipeline targets (if you use Python scripts)
# ------------------------------------------------------------------------------
audio-pipeline:
	python audio-pipeline.py --task posts --n 10

pdf-pipeline:
	python pdf-pipeline.py --task posts --n 10

pipelines: audio-pipeline pdf-pipeline

# ------------------------------------------------------------------------------
# 7) Clean
# ------------------------------------------------------------------------------
clean:
	rm -rf $(EXAMPLES_DIR)/*/*.pdf \
	       $(EXAMPLES_DIR)/*/*/*.pdf \
	       $(PAPERS_DIR)/*.pdf

# ------------------------------------------------------------------------------
# 8) Copy PDFs to assets/resume
# ------------------------------------------------------------------------------
copy: awesome-cv
	mkdir -p assets/resume

	# Copy English
	cp $(RESUME_EN_PDF) assets/resume/Zhiwei.Li.Resume.en.pdf
	cp $(INTRODUCTION_DIR)/en/introduction-en.pdf assets/resume/Zhiwei.Li.Introduction.en.pdf
	cp $(COVER_LETTER_DIR)/en/coverletter-en.pdf assets/resume/Zhiwei.Li.CoverLetter.en.pdf

	# Copy Chinese
	cp $(RESUME_ZH_PDF) assets/resume/Zhiwei.Li.Resume.zh.pdf
	cp $(INTRODUCTION_DIR)/zh/introduction-zh.pdf assets/resume/Zhiwei.Li.Introduction.zh.pdf
	cp $(COVER_LETTER_DIR)/zh/coverletter-zh.pdf assets/resume/Zhiwei.Li.CoverLetter.zh.pdf

	# Copy Japanese
	cp $(RESUME_JA_PDF) assets/resume/Zhiwei.Li.Resume.ja.pdf
	cp $(INTRODUCTION_DIR)/ja/introduction-ja.pdf assets/resume/Zhiwei.Li.Introduction.ja.pdf
	cp $(COVER_LETTER_DIR)/ja/coverletter-ja.pdf assets/resume/Zhiwei.Li.CoverLetter.ja.pdf

# Copy only English PDFs to assets/resume
awesome-cv-copy-en: awesome-cv-en
	mkdir -p assets/resume
	cp $(RESUME_EN_PDF) assets/resume/Zhiwei.Li.Resume.pdf
	cp $(INTRODUCTION_DIR)/en/introduction-en.pdf assets/resume/Zhiwei.Li.Introduction.pdf
	cp $(COVER_LETTER_DIR)/en/coverletter-en.pdf assets/resume/Zhiwei.Li.CoverLetter.pdf

# Copy all PDFs (wrapper)
awesome-cv-copy: awesome-cv copy
