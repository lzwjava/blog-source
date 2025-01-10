.PHONY: awesome-cv awesome-cv-en awesome-cv-copy awesome-cv-copy-en audio-pipeline pdf-pipeline pipelines clean copy coverletter-zh.pdf

# Compiler and directories
CC = xelatex
EXAMPLES_DIR = awesome-cv
RESUME_DIR = $(EXAMPLES_DIR)/resume
RESUME_EN_DIR = $(RESUME_DIR)/en
RESUME_ZH_DIR = $(RESUME_DIR)/zh
COVER_LETTER_DIR = $(EXAMPLES_DIR)/coverletter
INTRODUCTION_DIR = $(EXAMPLES_DIR)/introduction

# Source files
RESUME_EN_SRCS = $(shell find $(RESUME_EN_DIR) -name '*.tex' 2>/dev/null)
RESUME_ZH_SRCS = $(shell find $(RESUME_ZH_DIR) -name '*.tex' 2>/dev/null)
INTRODUCTION_SRCS = $(shell find $(INTRODUCTION_DIR) -name '*.tex' 2>/dev/null)

# Targets
# Full awesome-cv (both English and Chinese)
awesome-cv: introduction-en.pdf coverletter-en.pdf introduction-zh.pdf coverletter-zh.pdf resume-zh.pdf resume-en.pdf

# English-only awesome-cv
awesome-cv-en: introduction-en.pdf coverletter-en.pdf resume-en.pdf

# Build rules for each PDF
resume-en.pdf: $(RESUME_EN_DIR)/resume.tex $(RESUME_EN_SRCS)
	$(CC) -output-directory=$(RESUME_EN_DIR) $<

resume-zh.pdf: $(RESUME_ZH_DIR)/resume.tex $(RESUME_ZH_SRCS)
	$(CC) -output-directory=$(RESUME_ZH_DIR) $<

coverletter-en.pdf: $(COVER_LETTER_DIR)/coverletter.tex
	$(CC) -output-directory=$(COVER_LETTER_DIR) $<

coverletter-zh.pdf: $(COVER_LETTER_DIR)/coverletter-zh.tex
	$(CC) -output-directory=$(COVER_LETTER_DIR) $<

introduction-en.pdf: $(INTRODUCTION_DIR)/introduction-en.tex
	$(CC) -output-directory=$(INTRODUCTION_DIR) $<

introduction-zh.pdf: $(INTRODUCTION_DIR)/introduction-zh.tex
	$(CC) -output-directory=$(INTRODUCTION_DIR) $<	

# Pipeline targets
audio-pipeline:
	python audio-pipeline.py --task posts --n 10

pdf-pipeline:
	python pdf-pipeline.py --task posts --n 10

pipelines: audio-pipeline pdf-pipeline

# Clean generated PDFs
clean:
	rm -rf $(EXAMPLES_DIR)/*.pdf

# Copy all PDFs (both English and Chinese) to assets/resume
copy: awesome-cv
	mkdir -p assets/resume

	cp $(RESUME_EN_DIR)/resume-en.pdf assets/resume/Zhiwei.Li.Resume.pdf
	cp $(RESUME_ZH_DIR)/resume.pdf assets/resume/Zhiwei.Li.Resume.ZH.pdf

	cp $(INTRODUCTION_DIR)/introduction-en.pdf assets/resume/Zhiwei.Li.Introduction.EN.pdf
	cp $(INTRODUCTION_DIR)/introduction-zh.pdf assets/resume/Zhiwei.Li.Introduction.ZH.pdf

	cp $(COVER_LETTER_DIR)/coverletter-en.pdf assets/resume/Zhiwei.Li.CoverLetter.EN.pdf
	cp $(COVER_LETTER_DIR)/coverletter-zh.pdf assets/resume/Zhiwei.Li.CoverLetter.ZH.pdf

# Copy only English PDFs to assets/resume
awesome-cv-copy-en: awesome-cv-en
	mkdir -p assets/resume

	cp $(RESUME_EN_DIR)/resume-en.pdf assets/resume/Zhiwei.Li.Resume.pdf
	cp $(INTRODUCTION_DIR)/introduction-en.pdf assets/resume/Zhiwei.Li.Introduction.EN.pdf
	cp $(COVER_LETTER_DIR)/coverletter-en.pdf assets/resume/Zhiwei.Li.CoverLetter.EN.pdf

# Copy all PDFs (wrapper for awesome-cv and copy)
awesome-cv-copy: awesome-cv copy
