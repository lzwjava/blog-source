.PHONY: awesome-cv awesome-cv-en awesome-cv-copy awesome-cv-copy-en audio-pipeline pdf-pipeline pipelines clean copy papers

# Compiler and directories
CC = xelatex
EXAMPLES_DIR = awesome-cv
RESUME_DIR = $(EXAMPLES_DIR)/resume
COVER_LETTER_DIR = $(EXAMPLES_DIR)/coverletter
INTRODUCTION_DIR = $(EXAMPLES_DIR)/introduction
PAPERS_DIR = assets/papers

# Languages
LANGUAGES = en zh ja

# Source files
RESUME_SRCS = $(foreach lang,$(LANGUAGES),$(shell find $(RESUME_DIR)/$(lang) -name '*.tex' 2>/dev/null))
INTRODUCTION_SRCS = $(foreach lang,$(LANGUAGES),$(shell find $(INTRODUCTION_DIR)/$(lang) -name '*.tex' 2>/dev/null))
PAPERS_SRCS = $(shell find $(PAPERS_DIR) -name '*.tex' 2>/dev/null)

# Targets
# Full awesome-cv (both English and Chinese)
awesome-cv: $(foreach lang,$(LANGUAGES),introduction-$(lang).pdf coverletter-$(lang).pdf resume-$(lang).pdf) $(patsubst $(PAPERS_DIR)/%.tex, $(PAPERS_DIR)/%.pdf, $(PAPERS_SRCS))

# English-only awesome-cv
awesome-cv-en: introduction-en.pdf coverletter-en.pdf resume-en.pdf

# Build rules for each PDF
$(RESUME_DIR)/%/resume.pdf: $(RESUME_DIR)/%/resume.tex $(shell find $(RESUME_DIR)/$* -name '*.tex' 2>/dev/null)
	$(CC) -output-directory=$(RESUME_DIR)/$* $<

$(COVER_LETTER_DIR)/%/coverletter.pdf: $(COVER_LETTER_DIR)/%/coverletter.tex
	$(CC) -output-directory=$(COVER_LETTER_DIR)/$* $<

$(INTRODUCTION_DIR)/%/introduction.pdf: $(INTRODUCTION_DIR)/%/introduction.tex
	$(CC) -output-directory=$(INTRODUCTION_DIR)/$* $<

$(PAPERS_DIR)/%.pdf: $(PAPERS_DIR)/%.tex
	$(CC) -output-directory=$(PAPERS_DIR) $<

papers: $(patsubst $(PAPERS_DIR)/%.tex, $(PAPERS_DIR)/%.pdf, $(PAPERS_SRCS))

# Create specific targets for each language
$(foreach lang,$(LANGUAGES),resume-$(lang).pdf: $(RESUME_DIR)/$(lang)/resume.pdf)
$(foreach lang,$(LANGUAGES),coverletter-$(lang).pdf: $(COVER_LETTER_DIR)/$(lang)/coverletter.pdf)
$(foreach lang,$(LANGUAGES),introduction-$(lang).pdf: $(INTRODUCTION_DIR)/$(lang)/introduction.pdf)

# Pipeline targets
audio-pipeline:
	python audio-pipeline.py --task posts --n 10

pdf-pipeline:
	python pdf-pipeline.py --task posts --n 10

pipelines: audio-pipeline pdf-pipeline

# Clean generated PDFs
clean:
	rm -rf $(EXAMPLES_DIR)/*.pdf $(PAPERS_DIR)/*.pdf

# Copy all PDFs (both English and Chinese) to assets/resume
copy: awesome-cv
	mkdir -p assets/resume
	$(foreach lang,$(LANGUAGES),\
		cp $(RESUME_DIR)/$(lang)/resume.pdf assets/resume/Zhiwei.Li.Resume.$(if $(filter en,$(lang)),,$(lang)).pdf;\
		cp $(INTRODUCTION_DIR)/$(lang)/introduction.pdf assets/resume/Zhiwei.Li.Introduction.$(if $(filter en,$(lang)),,$(lang)).pdf;\
		cp $(COVER_LETTER_DIR)/$(lang)/coverletter.pdf assets/resume/Zhiwei.Li.CoverLetter.$(if $(filter en,$(lang)),,$(lang)).pdf;\
	)

# Copy only English PDFs to assets/resume
awesome-cv-copy-en: awesome-cv-en
	mkdir -p assets/resume
	cp $(RESUME_DIR)/en/resume.pdf assets/resume/Zhiwei.Li.Resume.pdf
	cp $(INTRODUCTION_DIR)/en/introduction.pdf assets/resume/Zhiwei.Li.Introduction.EN.pdf
	cp $(COVER_LETTER_DIR)/en/coverletter.pdf assets/resume/Zhiwei.Li.CoverLetter.EN.pdf

# Copy all PDFs (wrapper for awesome-cv and copy)
awesome-cv-copy: awesome-cv copy
