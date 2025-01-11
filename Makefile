.PHONY: awesome-cv audio-pipeline pdf-pipeline clean copy

CC = xelatex
EXAMPLES_DIR = awesome-cv
RESUME_DIR = awesome-cv/en
RESUME_ZH_DIR = awesome-cv/zh
COVER_LETTER_DIR = awesome-cv/coverletter
INTRODUCTION_DIR = awesome-cv/en
INTRODUCTION_ZH_DIR = awesome-cv/zh
RESUME_SRCS = $(shell find $(RESUME_DIR) -name '*.tex')
RESUME_ZH_SRCS = $(shell find $(RESUME_ZH_DIR) -name '*.tex')
INTRODUCTION_SRCS = $(shell find $(INTRODUCTION_DIR) -name '*.tex')
INTRODUCTION_ZH_SRCS = $(shell find $(INTRODUCTION_ZH_DIR) -name '*.tex')


# Existing awesome-cv target
awesome-cv: $(foreach x, coverletter coverletter-zh resume-zh resume, $x.pdf)

resume.pdf: $(RESUME_DIR)/resume.tex $(RESUME_SRCS)
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

resume-zh.pdf: $(RESUME_ZH_DIR)/resume-zh.tex $(RESUME_ZH_SRCS)
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

coverletter.pdf: $(COVER_LETTER_DIR)/coverletter.tex
	$(CC) -output-directory=$(COVER_LETTER_DIR) $<

coverletter-zh.pdf: $(COVER_LETTER_DIR)/coverletter-zh.tex
	$(CC) -output-directory=$(COVER_LETTER_DIR) $<

introduction-en.pdf: $(INTRODUCTION_DIR)/introduction-en.tex
	$(CC) -output-directory=$(INTRODUCTION_DIR) $<

introduction-zh.pdf: $(INTRODUCTION_ZH_DIR)/introduction-zh.tex
	$(CC) -output-directory=$(INTRODUCTION_ZH_DIR) $<	

# New audio-pipeline target
audio-pipeline:
	python audio-pipeline.py --task posts --n 10

# New pdf-pipeline target
pdf-pipeline:
	python pdf-pipeline.py --task posts --n 10

pipelines: audio-pipeline pdf-pipeline

introductions: introduction-en.pdf introduction-zh.pdf

# Clean target to remove generated files
clean:
	rm -rf $(EXAMPLES_DIR)/*.pdf

copy:
	mkdir -p assets/resume

	cp awesome-cv/resume.pdf assets/resume/Zhiwei.Li.Resume.pdf
	cp awesome-cv/resume-zh.pdf assets/resume/Zhiwei.Li.Resume.ZH.pdf

copy-introduction:
	cp awesome-cv/en/introduction-en.pdf assets/resume/Zhiwei.Li.Introduction.EN.pdf
	cp awesome-cv/zh/introduction-zh.pdf assets/resume/Zhiwei.Li.Introduction.ZH.pdf