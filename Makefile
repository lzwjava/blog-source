.PHONY: awesome-cv audio-pipeline pdf-pipeline clean copy

CC = xelatex
EXAMPLES_DIR = awesome-cv
RESUME_DIR = awesome-cv/resume
RESUME_ZH_DIR = awesome-cv/resume-zh
COVER_LETTER_DIR = awesome-cv/coverletter
INTRODUCTION_DIR = awesome-cv/introduction
RESUME_SRCS = $(shell find $(RESUME_DIR) -name '*.tex')
RESUME_ZH_SRCS = $(shell find $(RESUME_ZH_DIR) -name '*.tex')
INTRODUCTION_SRCS = $(shell find $(INTRODUCTION_DIR) -name '*.tex')


# Existing awesome-cv target
awesome-cv: $(foreach x, coverletter coverletter-zh resume-zh resume, $x.pdf)

resume.pdf: $(EXAMPLES_DIR)/resume.tex $(RESUME_SRCS)
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

resume-zh.pdf: $(EXAMPLES_DIR)/resume-zh.tex $(RESUME_ZH_SRCS)
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

coverletter.pdf: $(COVER_LETTER_DIR)/coverletter.tex
	$(CC) -output-directory=$(COVER_LETTER_DIR) $<

coverletter-zh.pdf: $(COVER_LETTER_DIR)/coverletter-zh.tex
	$(CC) -output-directory=$(COVER_LETTER_DIR) $<

introduction-en.pdf: $(INTRODUCTION_DIR)/introduction-en.tex
	$(CC) -output-directory=$(INTRODUCTION_DIR) $<

introduction-zh.pdf: $(INTRODUCTION_DIR)/introduction-zh.tex
	$(CC) -output-directory=$(INTRODUCTION_DIR) $<	

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

# Copy target for updating resume
copy:
	# Ensure destination directory exists
	mkdir -p assets/resume

	# Copy files with the desired names
	cp awesome-cv/resume.pdf assets/resume/Zhiwei.Li.Resume.pdf
	cp awesome-cv/resume-zh.pdf assets/resume/Zhiwei.Li.Resume.ZH.pdf
